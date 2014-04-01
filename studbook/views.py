from django.shortcuts import render

from studbook.models import Stud
from studbook.forms import StudForm

# Create your views here.
def home_page(request):

    studs = Stud.objects.all()

    return render(
        request,
        'home.html',
        {
            'studs': studs
        }
    )

def new(request):
    # Handle file upload
    if request.method == 'POST':
        form = StudForm(request.POST, request.FILES)
        if form.is_valid():

            stud = Stud(
                dog_name = request.POST.get('new_dog_name'),
                owner_name = request.POST.get('new_owner_name'),
                dog_pic = request.FILES.get('new_dog_pic')
            )
            stud.save()

    return HttpResponseRedirect('/')