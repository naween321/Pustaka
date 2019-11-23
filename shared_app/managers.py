from django.db import models
from django.utils import timezone
from django.db.models.query import QuerySet


class BaseQuerySet(QuerySet):
    """
        Prevents objects from being hard-deleted. Instead, sets the
        ``date_deleted``, effectively soft-deleting the object.
    """

    def delete(self):
        for obj in self:
            obj.deleted_at = timezone.now()
            obj.save()

    def undelete(self):
        for obj in self:
            obj.deleted_at = None
            obj.save()

    def hard_delete(self):
        for obj in self:
            obj.delete()


class BaseManager(models.Manager):
    """
        Only exposes objects that have NOT been soft-deleted.
    """

    def get_queryset(self):
        return BaseQuerySet(self.model, using=self.db).filter(deleted_at__isnull=True)
