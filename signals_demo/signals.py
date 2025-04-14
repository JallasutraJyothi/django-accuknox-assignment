from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction, IntegrityError
from .models import TestModel
import time
import threading

@receiver(post_save, sender=TestModel)
def signal_handler(sender, instance, **kwargs):
    print("===> Signal Execution")
    
    # Question 1: Synchronous check
    time.sleep(5)
    
    # Question 2: Thread check
    print("Signal thread ID:", threading.get_ident())
    
    # Question 3: Transaction rollback
    raise IntegrityError("Simulated error in signal")
