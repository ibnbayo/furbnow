from django.shortcuts import render

# Create your views here.

from . models import Measure

# def measures(request):
#     return render(request=request, template_name='measures.html')

def measures(request):
    measures = Measure.objects.all()
    if request.method == 'POST':
        total_cost = 0
        for measure in measures:
            if str(measure.id) in request.POST:
                total_cost += float(request.POST[str(measure.id)])
        return render(request, 'app/measures.html', {'measures': measures, 'total_cost': total_cost})
    else:
        return render(request, "app/measures.html", {"measures": measures})