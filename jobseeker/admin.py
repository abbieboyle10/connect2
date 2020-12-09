from django.contrib import admin

# Register your models here.

from .models import Employee_Basics
from .models import Employer_Basics
from .models import Follow_Employers
from .models import Employee_Education
from .models import Employee_Work_History
from .models import Employee_Skills


admin.site.register(Employee_Basics)
admin.site.register(Employer_Basics)
admin.site.register(Follow_Employers)
admin.site.register(Employee_Education)
admin.site.register(Employee_Work_History)
admin.site.register(Employee_Skills)
