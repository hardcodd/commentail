from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import AbstractCommentManager

USER_MODEL = get_user_model()
COMMENT_MAX_LENGTH = getattr(settings, "COMMENT_MAX_LENGTH", 3000)


class BaseAbstractComment(models.Model):
    """
    Abstract base class for comments.
    """

    site = models.ForeignKey(
        Site,
        on_delete=models.CASCADE,
        verbose_name=_("site"),
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        related_name="comments_for_%(class)s",
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        abstract = True


class AbstractComment(BaseAbstractComment):
    objects = AbstractCommentManager()

    user = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s_comments",
    )

    comment = models.TextField(max_length=COMMENT_MAX_LENGTH)

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created at"),
        db_index=True,
    )
    ip_address = models.GenericIPAddressField(
        verbose_name=_("IP address"),
        unpack_ipv4=True,
        null=True,
        blank=True,
    )

    is_public = models.BooleanField(
        default=True,
        verbose_name=_("is public"),
        db_index=True,
    )
    is_removed = models.BooleanField(
        default=False,
        verbose_name=_("is removed"),
        db_index=True,
    )

    class Meta(BaseAbstractComment.Meta):
        abstract = True
        ordering = ["-created_at"]
        permissions = [
            ("can_moderate_comments", _("Can moderate comments")),
        ]
        verbose_name = _("comment")
        verbose_name_plural = _("comments")

    def __str__(self):
        return f"{self.user} - {self.comment[:20]}..."
