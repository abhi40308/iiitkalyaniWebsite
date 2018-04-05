"""collegesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin


from .views import *

# urlpatterns = [
#     url(r'^$', home_page, name="home"),
#     url(r'^contact_us/$', contact_us, name="contact_us"),
#     url(r'^about_us/$', about_us, name="about_us"),
#     url(r'^academic_cal/$', academic_cal, name="academic_cal"),
#     url(r'^administration/$', administration, name="administration"),
#     url(r'^admission/$', admission, name="admission"),
#     url(r'^admissionpg/$', admissionpg, name="admissionpg"),
#     url(r'^admissionug/$', admissionug, name="admissionug"),
#     url(r'^algoholics/$', algoholics, name="algoholics"),
#     url(r'^anti_ragging/$', anti_ragging, name="anti_ragging"),
#     url(r'^campus/$',campus,name="campus"),
#     url(r'^constitution/$',constitution,name="constitution"),
#     url(r'^course_stru/$',course_stru,name="course_stru"),
#     url(r'^digitalInitiatives/$',digitalInitiatives,name="digitalInitiatives"),
#     url(r'^eBrochure/$',eBrochure,name="eBrochure"),
#     url(r'^facilties/$',facilties,name="facilties"),
#     url(r'^faculty1/$',faculty1,name="faculty1"),
#     url(r'^faculty/$',faculty,name="faculty"),
#     url(r'^facultyOld/$',facultyOld,name="facultyOld"),
#     url(r'^fee_structure/$',fee_structure,name="fee_structure"),
#     url(r'^hostel/$',hostel,name="hostel"),
#     url(r'^iiitpppAct/$',iiitpppAct,name="iiitpppAct"),
#     url(r'^labs/$',labs,name="labs"),
#     url(r'^lib_about/$',lib_about,name="lib_about"),
#     url(r'^lib_contact/$',lib_contact,name="lib_contact"),
#     url(r'^lib_guidelines/$',lib_guidelines,name="lib_guidelines"),
#     url(r'^lib_services/$',lib_services,name="lib_services"),
#     url(r'^library/$',library,name="library"),
#     url(r'^medical/$',medical,name="medical"),
#     url(r'^mentor_institute/$',mentor_institute,name="mentor_institute"),
#     url(r'^music/$',music,name="music"),
#     url(r'^news/$',news,name="news"),
#     url(r'^news_events/$',news_events,name="news_events"),
#     url(r'^notifications/$',notifications,name="notifications"),
#     url(r'^other/$',other,name="other"),
#     url(r'^programmes/$',programmes,name="programmes"),
#     url(r'^reach_iiit_kalyani/$',reach_iiit_kalyani,name="reach_iiit_kalyani"),
#     url(r'^regul_rules/$',regul_rules,name="regul_rules"),
#     url(r'^rti/$',rti,name="rti"),
#     url(r'^sports/$',sports,name="sports"),
#     url(r'^staff/$',staff,name="staff"),
#     url(r'^team/$',team,name="team"),
#     url(r'^webteam/$',webteam,name="webteam"),
#     url(r'^why_iiit/$',why_iiit,name="why_iiit"),
#     url(r'^dnd/$',dnd, name="dnd"),
#     url(r'^im/$',im, name="im"),
#     url(r'^ob/$',ob, name="ob"),
#     url(r'^sc/$',sc, name="sc"),
#     url(r'^sk/$',sk, name="sk"),
#     url(r'^skh/$',skh, name="skh"),
#     url(r'^sp/$',sp, name="sp"),
#     url(r'^tg/$',tg, name="tg"),
#     url(r'^ud/$',ud, name="ud"),
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
	url(r'^$', home_page, name="home"),
	url(r'^dnd/$',dnd, name="dnd"),
	#teams
	url(r'^staff/$',staff,name="staff"),
	url(r'^team/$',team,name="team"),
	url(r'^webteam/$',webteam,name="webteam"),
	#news
	url(r'^news/$',news,name="news"),
	url(r'^events/$',news_events,name="news_events"),
	url(r'^notifications/$',notifications,name="notifications"),
	#gymkhana
	url(r'^gymkhana/sports/$',sports,name="sports"),
	url(r'^gymkhana/algoholics/$', algoholics, name="algoholics"),
	url(r'^gymkhana/music/$',music,name="music"),
	#about
	url(r'^about/mentor_institute/$',mentor_institute,name="mentor_institute"),
	url(r'^about/why_iiit/$',why_iiit,name="why_iiit"),
	url(r'^about/administration/$', administration, name="administration"),
	url(r'^about/iiitpppAct/$',iiitpppAct,name="iiitpppAct"),
	url(r'^about/rti/$',rti,name="rti"),
	url(r'^about/about_us/$', about_us, name="about_us"),
	url(r'^about/reach_iiit_kalyani/$',reach_iiit_kalyani,name="reach_iiit_kalyani"),
	url(r'^about/contact_us/$', contact_us, name="contact_us"),
	url(r'^about/constitution/$',constitution,name="constitution"),
	#academics
	url(r'^academics/academic_cal/$', academic_cal, name="academic_cal"),
	url(r'^academics/programmes/$',programmes,name="programmes"),
	url(r'^academics/admission/$', admission, name="admission"),
	url(r'^academics/admission/admissionpg/$', admissionpg, name="admissionpg"),
	url(r'^academics/admission/admissionug/$', admissionug, name="admissionug"),
	url(r'^academics/course_stru/$',course_stru,name="course_stru"),
	url(r'^academics/fee_structure/$',fee_structure,name="fee_structure"),
	#students
	url(r'^students/regul_rules/$',regul_rules,name="regul_rules"),
	url(r'^students/anti_ragging/$', anti_ragging, name="anti_ragging"),
	url(r'^students/eBrochure/$',eBrochure,name="eBrochure"),
	#facilities
	url(r'^facilties/$',facilties,name="facilties"),
	url(r'^facilties/labs/$',labs,name="labs"),
	url(r'^facilties/other/$',other,name="other"),
	url(r'^facilties/medical/$',medical,name="medical"),
	url(r'^facilties/campus/$',campus,name="campus"),
	url(r'^facilties/hostel/$',hostel,name="hostel"),
	#library
	url(r'^facilties/library/$',library,name="library"),
	url(r'^facilties/library/lib_about/$',lib_about,name="lib_about"),
	url(r'^facilties/library/lib_contact/$',lib_contact,name="lib_contact"),
	url(r'^facilties/library/lib_guidelines/$',lib_guidelines,name="lib_guidelines"),
	url(r'^facilties/library/lib_services/$',lib_services,name="lib_services"),
	url(r'^facilties/library/digitalInitiatives/$',digitalInitiatives,name="digitalInitiatives"),
	#faculty
	url(r'^faculty1/$',faculty1,name="faculty1"),
	url(r'^faculty/$',faculty,name="faculty"),
	url(r'^facultyOld/$',facultyOld,name="facultyOld"),
	url(r'^faculty/im/$',im, name="im"),
	url(r'^faculty/ob/$',ob, name="ob"),
	url(r'^faculty/sc/$',sc, name="sc"),
	url(r'^faculty/sk/$',sk, name="sk"),
	url(r'^faculty/skh/$',skh, name="skh"),
	url(r'^faculty/sp/$',sp, name="sp"),
	url(r'^faculty/tg/$',tg, name="tg"),
	url(r'^faculty/ud/$',ud, name="ud"),
	#admin
	url(r'^admin/', admin.site.urls),
]
# campus
# constitution
# course_stru
# digitalInitiatives
# eBrochure
# faculties
# faculty1
# faculty
# facultyOld
# fee_structure
# hostel
# iiitpppAct
# labs
# lib_about
# lib_contact
# lib_guidelines
# lib_services
# library
# medical
# mentor_institute
# music
# news
# news_events
# notifications
# other
# programmes
# reach_iiit_kalyani
# regul_rules
# rti
# sports
# staff
# team
# webteam
# why_iiit



#     url(r'^campus/$',campus,name="campus"),
#     url(r'^constitution/$',constitution,name="constitution"),
#     url(r'^course_stru/$',course_stru,name="course_stru"),
#     url(r'^digitalInitiatives/$',digitalInitiatives,name="digitalInitiatives"),
#     url(r'^eBrochure/$',eBrochure,name="eBrochure"),
#     url(r'^faculties/$',faculties,name="faculties"),
#     url(r'^faculty1/$',faculty1,name="faculty1"),
#     url(r'^faculty/$',faculty,name="faculty"),
#     url(r'^facultyOld/$',facultyOld,name="facultyOld"),
#     url(r'^fee_structure/$',fee_structure,name="fee_structure"),
#     url(r'^hostel/$',hostel,name="hostel"),
#     url(r'^iiitpppAct/$',iiitpppAct,name="iiitpppAct"),
#     url(r'^labs/$',labs,name="labs"),
#     url(r'^lib_about/$',lib_about,name="lib_about"),
#     url(r'^lib_contact/$',lib_contact,name="lib_contact"),
#     url(r'^lib_guidelines/$',lib_guidelines,name="lib_guidelines"),
#     url(r'^lib_services/$',lib_services,name="lib_services"),
#     url(r'^library/$',library,name="library"),
#     url(r'^medical/$',medical,name="medical"),
#     url(r'^mentor_institute/$',mentor_institute,name="mentor_institute"),
#     url(r'^music/$',music,name="music"),
#     url(r'^news/$',news,name="news"),
#     url(r'^news_events/$',news_events,name="news_events"),
#     url(r'^notifications/$',notifications,name="notifications"),
#     url(r'^other/$',other,name="other"),
#     url(r'^programmes/$',programmes,name="programmes"),
#     url(r'^reach_iiit_kalyani/$',reach_iiit_kalyani,name="reach_iiit_kalyani"),
#     url(r'^regul_rules/$',regul_rules,name="regul_rules"),
#     url(r'^rti/$',rti,name="rti"),
#     url(r'^sports/$',sports,name="sports"),
#     url(r'^staff/$',staff,name="staff"),
#     url(r'^team/$',team,name="team"),
#     url(r'^webteam/$',webteam,name="webteam"),
#     url(r'^why_iiit/$',why_iiit,name="why_iiit"),