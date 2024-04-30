from django.contrib import admin

# Register your models here.

from . models import Manufacturers

from import_export.admin import ImportExportModelAdmin

admin.site.register(Manufacturers, ImportExportModelAdmin)