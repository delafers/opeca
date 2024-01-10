import djoser
import rest_framework
from django.contrib import admin
from django.urls import path, include, re_path
import NDEdu.views as NDEdu
import NDFGOS.views as NDFGOS
import NDFormsEdu.views as NDFormsEdu
import NDFZ.views as NDFZ
import NDGIA.views as NDGIA
import NDLetter.views as NDLetter
import NDPMPK.views as NDPMPK
import SpecCommon.views as SpecCommon
import SpecDoc.views as SpecDoc
import SpecPedPsy.views as SpecPedPsy
import SpecTeachDef.views as SpecTeachDef
import SpecTeachLog.views as SpecTeachLog
import webs.views as viewsWebs


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    #path('auth/', include('djoser.urls.authtoken')),
    path('api/NDEdu', NDEdu.GetFilesInfo.as_view()),
    path('api/NDFGOS', NDFGOS.GetFilesInfo.as_view()),
    path('api/NDFZ', NDFZ.GetFilesInfo.as_view()),
    path('api/NDGIA', NDGIA.GetFilesInfo.as_view()),
    path('api/NDLetter', NDLetter.GetFilesInfo.as_view()),
    path('api/NDPMPK', NDPMPK.GetFilesInfo.as_view()),
    path('api/SpecCommon', SpecCommon.GetFilesInfo.as_view()),
    path('api/SpecDoc', SpecDoc.GetFilesInfo.as_view()),
    path('api/SpecPedPsy', SpecPedPsy.GetFilesInfo.as_view()),
    path('api/SpecTeachDef', SpecTeachDef.GetFilesInfo.as_view()),
    path('api/SpecTeachLog', SpecTeachLog.GetFilesInfo.as_view()),
    path('api/webinars', viewsWebs.GetWebinars.as_view()),

]
