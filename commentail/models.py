from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from .abstracts import AbstractComment

USER_MODEL = get_user_model()


class Comment(AbstractComment):
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="replies",
        null=True,
        blank=True,
        verbose_name=_("parent comment"),
        db_index=True,
    )

    thread_id = models.PositiveIntegerField(null=True, db_index=True)

    def save(self, *args, **kwargs):
        if self.parent:
            # If this comment is a reply, set the thread_id to the parent's thread_id
            self.thread_id = self.parent.thread_id or self.parent.pk
        else:
            super().save(*args, **kwargs)
            if not self.thread_id:
                # If this is a top-level comment, set the thread_id to its own pk
                self.thread_id = self.pk
        super().save(*args, **kwargs)


class CommentLike(models.Model):
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name="likes",
        verbose_name=_("comment"),
    )
    user = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comment_likes",
        verbose_name=_("user"),
    )

    class Meta:
        unique_together = ("comment", "user")
