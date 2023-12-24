from .models import forms
from django.forms import ModelForm
from .models import Details,Course


class PersonCreationForm(ModelForm):
    class Meta:
        model = Details
        fields = ['name','address','email','date_of_birth','age','phone_number','department','course','purpose','materials_provided']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')

