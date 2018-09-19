from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from voip.models import Number, Call

@login_required
def index(request):
    return render(request, 'index.html')

# http://localhost:8000/call?To=+18163213211&CallSid=TEST&CallerName=Test&From=+19133213211
def call(request):
    info = request.POST if request.POST else request.GET
    # fields: https://www.twilio.com/docs/voice/twiml
    number = get_object_or_404(Number, tracking_number=info.get('To').replace(" ", "+"))
    call = Call(number_id=number.id, twilio_call_id=info.get('CallSid'), caller_number=info.get('From'),
                caller_name=info.get('CallerName'))
    call.save()
    context = {
        "call": call,
        "number": number,
    }
    return render(request, 'call.xml', context, content_type="text/xml; charset=utf-8")

# http://localhost:8000/status/28?CallDuration=23
def status(request, call_id):
    info = request.POST if request.POST else request.GET
    call = get_object_or_404(Call, pk=call_id)
    call.duration = info.get('CallDuration', 0)
    call.save(update_fields=['duration', 'updated_at'])
    return render(request, 'status.xml', content_type="text/xml; charset=utf-8")

# http://localhost:8000/record/28?RecordingUrl=http://example.com/asdf.mp3
def record(request, call_id):
    info = request.POST if request.POST else request.GET
    call = get_object_or_404(Call, pk=call_id)
    call.recording_url = info.get('RecordingUrl')
    call.save(update_fields=['recording_url', 'updated_at'])
    return render(request, 'status.xml', content_type="text/xml; charset=utf-8")
