from django.conf.urls import url
from django.urls import reverse_lazy

#from django.contrib.auth import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns = [
    #url(r'^$', password_reset,
    #    {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    url(r'^$',PasswordResetView.as_view(),name='password_reset'),
    #url(r'^done/$', password_reset_done, name='password_reset_done'),
	url(r'^done/$', PasswordResetDoneView.as_view() , name='password_reset_done'),
    #url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
    #    {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(),
        {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    #url(r'^complete/$', password_reset_complete, name='password_reset_complete'),
    url(r'^complete/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]