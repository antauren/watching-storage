from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from .storage_information_view import format_duration


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)

    visits = Visit.objects.filter(passcard_id=passcard.id)

    this_passcard_visits = [
        {
            "entered_at": visit.entered_at.strftime('%Y-%m-%d %H:%M:%S'),
            "duration": format_duration(Visit.get_duration(visit)),
            "is_strange": Visit.is_visit_long(visit)
        }
        for visit in visits

    ]

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
