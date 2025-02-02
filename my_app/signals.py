from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import receiver
from .models import Post, Comment, Tag, Category,Rating
# Pre-save signals: Post saqlanishidan oldin ishga tushadi
@receiver(pre_save, sender=Post)
def pre_save_post(sender,instance,**kwargs):
    print(f"Pre-save: Post saqlanishidan oldin ishladi. {instance.title.upper()}")
    if instance.title:
        instance.title = instance.title.upper()

# Post-save signals: Post saqlangandan keyin ishga tushadi
@receiver(post_save, sender=Post)
def post_save_post(sender, instance, created, **kwargs):
    if created:
        print(f"Post-save: Yangi post yaratildi: {instance.title}")
    else:
        print(f"Post-save: Post yangilandi: {instance.title}")

# Post-delete: Post o'chirilgandan keyin ishga tushadi
@receiver(post_delete, sender=Post)
def post_delete_contact_model(sender, instance, *args, **kwargs):
    print(f"Post-delete: Post o'chirildi: {instance.title}")

# Pre-delete: Post o'chirilmasdan oldin ishga tushadi
@receiver(pre_delete, sender=Post)
def pre_delete_contact_model(sender, instance, *args, **kwargs):
    print(f"Pre-delete: Post o'chirilishidan oldin ishga tushadi: {instance.title}")

