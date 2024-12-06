from django.contrib import admin
from . import models


admin.site.register(models.Product)
admin.site.register(models.Income)
admin.site.register(models.User)
admin.site.register(models.Cost)
admin.site.register(models.Staffdailywork)

