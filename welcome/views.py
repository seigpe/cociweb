import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import  json


from . import database
from .models import PageView,Contratos
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    return HttpResponse(PageView.objects.count())



@csrf_exempt
def new_case(request):
    if request.method == 'GET':
        CaseForm = model_form(Case,CaseRegistration)
        form = CaseForm()
        data = CaseRegistration()
        context = RequestContext(request, {
                                           'form': data,
                                               })
        return render_to_response("begifujur/case.html",context)
    if request.method == 'POST':
        CaseForm = model_form(Case,CaseRegistration)
        form = CaseForm(request.POST)
        data= CaseRegistration(request.POST)
        if request.method == 'POST' and data.validate():
            status = request.POST.get('status')
            name = request.POST.get('name')
            priority = request.POST.get('priority')
            description=request.POST.get('description')
            inicio,fin= Case.allocate_ids(1)
            ### existe el sensor?
            dato= Case (id=inicio,name=name, priority=int(priority),description=description, status=status)       
            dato.put()   
            return HttpResponse('dato cargado')
        else:
            context = RequestContext(request, {
                                                'form': data,
                                                })
            return render_to_response("begifujur/case.html",context)


@csrf_exempt
def list_cases_json(request):
    size = request.POST.get('jtPageSize',100)
    start = request.POST.get('jtStartIndex',0)
    #dato= ndb.gql('select  * from Case order by time desc ')

    #datos_salida=dato.fetch(int(size),offset=int(start))
    result = {"Records":[], "Result":"OK","TotalRecordCount":''}
    
    #if datos_salida is not None:
    #    for case in datos_salida:
    #        cadena = {'Name':'','Username':'','Status':'','Time':'','Priority':'','Data':'','Description':'','Link':''}
    #        cadena['Name']=case.name
    #        cadena['osUsername']=case.username
    #        cadena['Status']=case.status
    #        cadena['Time']=str(case.time)
    #        cadena['Priority']=case.priority
    #        cadena['Data']=case.data
    #        cadena['Description']=case.description
    #        cadena['Link']= '<A target="_parent" HREF="/edit_case/caseid='+str(case.key.id())+'"><img src="/img/list_metro.png" /></A>'  
    #        result['Records'].append ( cadena)
    result['TotalRecordCount']=Contratos.objects.count()
    
    
    result = {"Records": [ {'Contrato':'121314','Nombre':'sd','Alias':'fd','Fecha':'df'} ], "Result":"OK","TotalRecordCount":'1'}
    
    print result
    return HttpResponse(json.dumps(result)) 

def list_cases(request):
    #template_menu = loader.get_template('begifujur/list_cases.html')
    #context = RequestContext(request, {
    #    'query': '',
    #    'sensor_id': ''
    #})
    #return HttpResponse(template_menu.render(context))
    hostname = os.getenv('HOSTNAME', 'unknown')

    return render(request, 'welcome/listado.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

