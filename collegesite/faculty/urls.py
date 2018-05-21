from django.conf.urls import url
from . import views

urlpatterns = [url('^$',views.faculty,name='faculty'),
			   url('^sk/$',views.sk,name='sk'),
			   url('^skh/$',views.skh,name='skh'),
			   url('^sp/$',views.sp,name='sp'),
			   url('^sc/$',views.sc,name='sc'),
			   url('^im/$',views.im,name='im'),
			   url('^tg/$',views.tg,name='tg'),
			   url('^ud/$',views.ud,name='ud'),
			   url('^ob/$',views.ob,name='ob'),
			   url('^dnd/$',views.dnd,name='dnd'),
			   ]
			   
