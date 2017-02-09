from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf    import requires_csrf_token
from .forms import SavingForm
from django.template import loader
from django.http import HttpResponse
from .models import Savings

def index(request):

    if request.method == 'POST':
        form = SavingForm(request.POST)

        if form.is_valid():
            capital = request.POST.get('capital', '')
            years = request.POST.get('years', '')
            interest = request.POST.get('interest', '')
            final_capital = 'calculation'

            I = float(interest)/100/12
            Y = 12 * int(years)
            C = float(capital)

            context = {
                'capital': capital,
                'years': years,
                'interest': interest,
                'final_capital':round(C*(1+I)**Y,2),
                'valid': True,
                'form': form
            }

            s = Savings(capital=capital,years=years,interest=interest,final_capital=round(C*(1+I)**Y,2))
            s.save()

            return render(request,'index.html', context)
    else:
        form = SavingForm()
    return render(request, 'index.html', {'form': form})


def displaydata(request):
    all_users = Savings.objects.all()
    return render(request,'displaydata/displaydata.html', {'all_users': all_users })


