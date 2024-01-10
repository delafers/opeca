from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include, re_path
import webs.views as viewsWebs
import news.views as viewsMain
import NPD.views as viewsNPD
import OtherFiles.views as viewsOtherFiles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/webinars', viewsWebs.GetWebinars.as_view()),
    path('api/news', viewsMain.GetFiles.as_view()),
    path('api/NPD', viewsNPD.GetFilesInfo.as_view()),
    path('api/other', viewsOtherFiles.GetFilesInfo.as_view()),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
