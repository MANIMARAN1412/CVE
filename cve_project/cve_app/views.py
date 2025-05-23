from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import CVE
from .serializers import CVESerializer
from django.views.generic import DetailView
from django.core.paginator import Paginator
from django.contrib import messages

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
class CVEViewSet(viewsets.ModelViewSet):
    queryset = CVE.objects.all().order_by('-last_modified_date')
    serializer_class = CVESerializer
    pagination_class = CustomPagination

def cve_list(request):
    cves = CVE.objects.all().order_by('-last_modified_date')
    paginator = Paginator(cves, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'cve_app/cve_list.html', {'page_obj': page_obj})

def cve_create(request):
    if request.method == 'POST':
        
        CVE.objects.create(
            cve_id=request.POST['cve_id'],
            identifier=request.POST['identifier'],
            published_date=request.POST['published_date'],
            last_modified_date=request.POST['last_modified_date'],
            status=request.POST['status']
        )
        messages.success(request, 'CVE created successfully!')
        return redirect('cve_list')
    return render(request, 'cve_app/cve_form.html')

def cve_update(request, pk):
    cve = get_object_or_404(CVE, pk=pk)
    if request.method == 'POST':
        
        cve.cve_id = request.POST['cve_id']
        cve.identifier = request.POST['identifier']
        cve.published_date = request.POST['published_date']
        cve.last_modified_date = request.POST['last_modified_date']
        cve.status = request.POST['status']
        cve.save()
        messages.success(request, 'CVE updated successfully!')
        return redirect('cve_list')
    return render(request, 'cve_app/cve_form.html', {'cve': cve})

def cve_delete(request, pk):
    cve = get_object_or_404(CVE, pk=pk)
    if request.method == 'POST':
        cve.delete()
        messages.success(request, 'CVE deleted successfully!')
        return redirect('cve_list')
    return render(request, 'cve_app/cve_confirm_delete.html', {'cve': cve})

def cve_detail(request, pk):
    cve = get_object_or_404(CVE, pk=pk)
    return render(request, 'cve_app/cve_detail.html', {'cve': cve})
