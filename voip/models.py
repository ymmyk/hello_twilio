from django.db import models

class Number(models.Model):
    tracking_number = models.CharField(max_length=32, db_index=True, null=False, blank=False)
    forwarding_number = models.CharField(max_length=32, null=False, blank=False)
    description = models.CharField(max_length=64, null=False, blank=False)
    record = models.BooleanField(default=False, null=False, blank=True)

class Calls(models.Model):
    number = models.ForeignKey(Number, related_name='calls', blank=False, null=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add = True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now = True, null=False, blank=False)

    twilio_call_id = models.CharField(max_length=64, blank=True, null=True)
    caller_number = models.CharField(max_length=32, blank=True, null=True)
    caller_name = models.CharField(max_length=32, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
