from django.conf.urls import url
from django.contrib import admin
from app.views import up_vote, down_vote, AnswerCreateView, QuestionCreateView, MyProfileView, QuestionDetailView, IndexView, SignUpView, QuestionListCreateAPIView, QuestionRetrieveUpdateDestroyAPIView, AnswerListCreateAPIView, AnswerRetrieveUpdateDestroyAPIView
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
    url(r'^myprofile/(?P<pk>\d+)/$', MyProfileView.as_view(), name="profile"),
    url(r'^questiondetail/(?P<pk>\d+)/$', QuestionDetailView.as_view(), name='question_detail_view'),
    url(r'^questioncreate/$', QuestionCreateView.as_view(), name='question_create_view'),
    url(r'^question/(?P<q_id>\d+)/answer/$', AnswerCreateView.as_view(), name='answer_create_view'),
    url(r'^upvote/(?P<a_id>\d+)/$', up_vote, name='up_ans_view'),
    url(r'^downvote/(?P<a_id>\d+)$', down_vote, name='down_ans_view'),
]
