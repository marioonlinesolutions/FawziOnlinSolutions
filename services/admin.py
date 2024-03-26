from django.contrib import admin
from .models import Project 
from embed_video.admin import AdminVideoMixin
from .models import Video, Article



class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
      pass
admin.site.register(Video, MyModelAdmin)




admin.site.register(Article)






class MyModelAdmin(admin.ModelAdmin):
      pass  
admin.site.register(Project, MyModelAdmin)
