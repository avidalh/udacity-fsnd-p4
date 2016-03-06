from lib.models import SpeakerForm


def copySpeakerToForm(speaker):
    """Copy speaker fields to form"""
    form = SpeakerForm()
    for field in form.all_fields():
        if hasattr(speaker, field.name):
            value = getattr(speaker, field.name)
            setattr(form, field.name, value)

    return form
