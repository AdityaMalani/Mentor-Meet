from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from classroom.views import classroom, students, teachers

urlpatterns = [
    path('', include('classroom.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
    path('quiz/reportadd/<str:pk>/',teachers.Addreport,name='add_report'),
    path('quiz/reportadded/<str:pk>',teachers.reportadded,name='report_added'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
