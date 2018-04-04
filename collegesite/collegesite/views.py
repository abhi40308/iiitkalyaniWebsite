from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

#Returns rendered "home_page.html" when base url calls home_page function from urls.py
def home_page(request):
    return render(request, "index.html")

def contact_us(request):
    return render(request, "contact_us.html")

def about_us(request):
    return render(request, "about_us.html")

def academic_cal(request):
    return render(request, "Academic_cal.html")

def administration(request):
    return render(request, "administration.html")

def admission(request):
    return render(request, "admission.html")

def admissionpg(request):
    return render(request, "admissionpg.html")

def admissionug(request):
    return render(request, "admissionug.html")

def algoholics(request):
    return render(request, "algoholic.html")

def anti_ragging(request):
    return render(request, "Anti_ragging.html")

def campus(request):
    return render(request, "Campus.html")

def constitution(request):
		return render(request, "Constitution.html")

def course_stru(request):
		return render(request, "Course_stru.html")

def digitalInitiatives(request):
		return render(request, "digital-Initiatives.html")

def eBrochure(request):
		return render(request, "e-Brochure.html")

def facilties(request):
		return render(request, "Facilities_landing_page-v6.html")

def faculty1(request):
		return render(request, "faculty-1.htm")

def faculty(request):
		return render(request, "faculty.html")

def facultyOld(request):
		return render(request, "faculty_old_page.html")

def fee_structure(request):
		return render(request, "fee_structure.html")

def hostel(request):
		return render(request, "Hostel.html")

def iiitpppAct(request):
		return render(request, "iiit-pppAct.html")

def labs(request):
		return render(request, "Labs.html")

def lib_about(request):
		return render(request, "Lib-About.html")

def lib_contact(request):
		return render(request, "Lib-contact.html")

def lib_guidelines(request):
		return render(request, "Lib-Guidelines.html")

def lib_services(request):
		return render(request, "Lib-Services.html")

def library(request):
		return render(request, "Library.html")

def medical(request):
		return render(request, "Medical.html")

def mentor_institute(request):
		return render(request, "Mentor_institute.html")

def music(request):
		return render(request, "music.html")

def news(request):
		return render(request, "news.html")

def news_events(request):
		return render(request, "news_events.html")

def notifications(request):
		return render(request, "notifications.html")

def other(request):
		return render(request, "Other.html")

def programmes(request):
		return render(request, "programmes.html")

def reach_iiit_kalyani(request):
		return render(request, "reach_iiit_kalyani.html")

def regul_rules(request):
		return render(request, "regul_rules.html")

def rti(request):
		return render(request, "rti.html")

def sports(request):
		return render(request, "sports.html")

def staff(request):
		return render(request, "staff.html")

def team(request):
		return render(request, "team.html")

def webteam(request):
		return render(request, "webteam.html")

def why_iiit(request):
		return render(request, "why_iiit.html")

def dnd(request):
		return render(request, "dnd.html")

def im(request):
		return render(request, "im.html")

def ob(request):
		return render(request, "ob.html")

def sc(request):
		return render(request, "sc.html")

def sk(request):
		return render(request, "sk.html")

def skh(request):
		return render(request, "skh.html")

def sp(request):
		return render(request, "sp.html")

def tg(request):
		return render(request, "tg.html")

def ud(request):
		return render(request, "ud.html")

