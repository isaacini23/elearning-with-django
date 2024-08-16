
from django.urls import path, include
from . import views

urlpatterns = [
    path(r'^$', views.course_list, name='course_list'),
    path(r'(?P<course_pk>\d+)/t(?P<step_pk>\d+)/$', views.text_detail, name='text_detail'),
    path(r'(?P<course_pk>\d+)/q(?P<step_pk>\d+)/$', views.quiz_detail, name='quiz_detail'),
    path(r'(?P<course_pk>\d+)/create_quiz/$', views.quiz_create, name='create_quiz'),
    path(r'(?P<course_pk>\d+)/edit_quiz(?P<quiz_pk>\d+)/$', views.quiz_edit, name='edit_quiz'),
    path(r'(?P<quiz_pk>\d+)/create_question/(?P<question_type>mc|tf)/$', views.create_question, name='create_question'),
    path(r'(?P<quiz_pk>\d+)/edit_question(?P<question_pk>\d+)/$', views.edit_question, name='edit_question'),
    path(r'(?P<question_pk>\d+)/create_answer/$', views.answer_form, name='create_answer'),
    path(r'(?P<pk>\d+)/$', views.course_detail, name='course_detail'),  # This url should be under the step_detail url.
]
