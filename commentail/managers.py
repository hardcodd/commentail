from django.db import models


class AbstractCommentManager(models.Manager):
    def live(self):
        """
        Returns only public comments.
        """
        return self.filter(is_public=True, is_removed=False).select_related(
            "user",
        )
