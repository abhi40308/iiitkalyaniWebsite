from django.shortcuts import render
from faculty.models import SK,SKH,TG,OB,UD,SP,SC,IM,DND 

def faculty(request):
	return render(request, "faculty.html")
		
def dnd(request):
	content = DND.objects.all()
	return render(request, "dnd.html",{'content':content})

def im(request):
	content = IM.objects.all()
	return render(request, "im.html",{'content':content})

def ob(request):
	content = OB.objects.all()
	return render(request, "ob.html",{'content':content})

def sc(request):
	content = SC.objects.all()
	return render(request, "sc.html",{'content':content})

def sk(request):
	content = SK.objects.all()
	return render(request, "sk.html",{'content':content})

def skh(request):
	content = SKH.objects.all()
	return render(request, "skh.html",{'content':content})

def sp(request):
	content = SP.objects.all()
	return render(request, "sp.html",{'content':content})

def tg(request):
	content = TG.objects.all()
	return render(request, "tg.html",{'content':content})

def ud(request):
	content = UD.objects.all()
	return render(request, "ud.html",{'content':content})
