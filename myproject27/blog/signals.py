from django.db.models.signals import pre_save , post_save
from django.dispatch import receiver
from .models import Blog

@receiver(pre_save,sender=Blog)
def before_saving_blog(sender,instance,**kwargs):
    print(f"About the save blog[pre-save]{instance.title}")


@receiver(post_save,sender=Blog)
def after_saving_blog(sender,created,instance,**kwargs):
    print(f"About the saved blog[post-save]")
    if created:
        print(f"New blog created:{instance.title}")
    else:
        print(f"blog updated:{instance.title}")