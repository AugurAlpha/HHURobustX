from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.template import Context
import MySQLdb
from AcFun.models import *
import datetime,hashlib,os,subprocess
pageNumber = 25
path = os.getcwd()
upload_loc = path + '/submitCodes/%s'
# Create your views here.

def index(request):
	return render_to_response('index.html')

def get_oj_problemlist(request):
	p = problem.objects.all()
	dict = {}
	dict['problemlist'] = p
	data = Context(dict)

	return render_to_response('oj_problemlist.html', data)


def get_oj_topic(request):
	return render_to_response('oj_topic.html')


def get_manage(request):
	return render_to_response('manage.html')


def add_oj_problem(request):
	title = request.POST.get('protitle')
	desc = request.POST.get('prodesc')
	input = request.POST.get('proinput')
	output = request.POST.get('prooutput')

	p = problem(title=title,
		description = desc,
		input = input,
		output = output)
	p.save()
	return HttpResponseRedirect('/manage')

def get_oj_problem(request, id):
	try:
		p = problem.objects.get(id = id)
	except Exception, e:
		print e
		return render_to_response('oj_problem.html', {})
	else:
		return render_to_response('oj_problem.html', {"problem" : p})


def submit_oj_problem(request, id):
	if request.method == 'GET':
		return render_to_response('oj_problemSubmit.html', {'proId' : id})
	else:
		problemId = request.POST.get('proId', '')
		language = request.POST.get('lang', '')
		sourceCode = request.POST.get('sourceCode', '')

		#hash = hashlib.md5(sourceCode).hexdigest()
		#p = oj_problemSubmit.objects.filter(md5 = hash)
		p = problemSubmit(problemId = problemId,
			language = language, 
			sourceCode = '',
			status = 0, 
			submit_time = datetime.datetime.now()) #not handle
		p.save()
		#print problemId, language, sourceCode

		uploadLoc = upload_loc % p.id
		print os.path, uploadLoc
		if not os.path.exists(uploadLoc):
			os.makedirs(uploadLoc)
		fn = uploadLoc + '/code'
		des = open(fn, 'wb')
		des.write(sourceCode)
		des.close()


		id = p.id
		p = problemSubmit.objects.get(id=id)
		p.sourceCode = fn
		p.save()

		return HttpResponseRedirect('/oj/status')


def get_oj_status(request):
	p = problemSubmit.objects.order_by('-id')
	for status in p:
		lang = status.language
		if  lang == 1:
			status.language = 'C'
		elif lang == 2:
			status.language = 'C++'
		elif  lang == 3:
			status.language = 'Java'
		elif lang == 4:
			status.language = 'Python'
	

	return render_to_response('oj_status.html', {'status': p})

