from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits = [
        {
            "who_entered": get_who_entered(visit),
            "entered_at": visit.entered_at.strftime('%Y-%m-%d %H:%M:%S'),
            "duration": format_duration(Visit.get_duration(visit)),
            "is_strange": Visit.is_visit_long(visit)
        }
        for visit in visits

    ]

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }

    return render(request, 'storage_information.html', context)


def get_who_entered(visit):
    post = Passcard.objects.get(id=visit.passcard_id)

    return post.owner_name


def format_duration(duration):
    hours, minutes, _ = convert_timedelta(duration)
    
    return '{}ч {}мин'.format(hours, minutes)


def convert_timedelta(duration):
    days, seconds = duration.days, duration.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)

    return hours, minutes, seconds
