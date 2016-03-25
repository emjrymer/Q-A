from django.conf.urls import url
from django.contrib import admin
from app.views import IndexView, SignUpView, QuestionListCreateAPIView, QuestionRetrieveUpdateDestroyAPIView, AnswerListCreateAPIView, AnswerRetrieveUpdateDestroyAPIView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^signup/$', SignUpView.as_view(), name="signup_view"),
    url(r'^login/$', auth_views.login, name="login_view"),
    url(r'^logout/$', auth_views.logout_then_login, name="logout_view"),
    url(r'^api/questions/$', QuestionListCreateAPIView.as_view(), name="post_question"),
    url(r'^api/questions/(?P<pk>\d+)/$', QuestionRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^api/answers/$', AnswerListCreateAPIView.as_view(), name='post_answer'),
    url(r'^api/answers/(?P<pk>\d+)/$', AnswerRetrieveUpdateDestroyAPIView.as_view(), name='edit_answer'),
]
