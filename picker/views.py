from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Plan, Location
from django.views import generic
from .forms import PlanForm

# Create your views here.
def index(request):
    """
    View function for site home page
    """
    num_plans = Plan.objects.all().count()
    num_locs = Location.objects.all().count()

    return render(
        request,
        'index.html', 
        context={'num_plans': num_plans, 'num_locs': num_locs},       
    )

def add_plan(request):
    if request.method == "POST":
        form = PlanForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('plans')
    else:
        form = PlanForm()
    
    return render(request, 'picker/add_plan.html', {'form': form})

def pick(request):
    the_pick = Plan.objects.order_by("?").first()
    return render(
        request,
        'picker/pick.html',
    )

class PlanListView(generic.ListView):
    model = Plan
    context_object_name = 'plan_list'
    paginate_by = 10

class PlanDetailView(generic.DetailView):
    model = Plan

class LocationListView(generic.ListView):
    model = Location
    context_object_name = "location_list"
    paginate_by = 10

class LocationDetailView(generic.DetailView):
    model = Location