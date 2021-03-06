from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CompetitionForm
from .models import Competition
import datetime


def competition_rules_view(request):
    return render(request, "competition_rules.html")

def competition_terms_view(request):
    return render(request, "competition_terms.html")

@login_required
def competition(request):
    highest_points = Competition.objects.order_by('-points_accrued').first()
    total_entries = Competition.objects.count()

    try:
        entry_form = Competition.objects.get(customer=request.user)
        points = entry_form.points_accrued
        form = CompetitionForm(instance=entry_form)
    except Competition.DoesNotExist:
        return redirect(competition_new)
    
    submit_date = datetime.date.today()
    closing_date = datetime.date(2021, 7, 2)
    if submit_date > closing_date:
        messages.warning(request, 'Competition date closed')
        return render(request, "competition.html",
            {'form': form, 'points':points,'highest_points':highest_points,'total_entries':total_entries})
    else:    
        if request.method == "POST":
            form = CompetitionForm(request.POST, instance=entry_form)
            if form.is_valid():
                temp = form.save(commit=False)
                temp.customer = request.user
                temp.save()
                messages.success(request, 'You have successfuly updated your score predictions. GOOD LUCK!')
           #     return redirect('/')

            
        return render(request, "competition.html",
            {'form': form, 'points':points,'highest_points':highest_points,'total_entries':total_entries})

def competition_new(request):
    highest_points = Competition.objects.order_by('-points_accrued').first()
    total_entries = Competition.objects.count()
    form = CompetitionForm()
    points = 0
    submit_date = datetime.date.today()
    closing_date = datetime.date(2021, 7, 2)
    if submit_date > closing_date:
        messages.warning(request, 'Competition date closed')
    else:    
        if request.method == "POST":
            form = CompetitionForm(request.POST)
            if form.is_valid():
                temp = form.save(commit=False)
                temp.customer = request.user
                temp.save()
                messages.success(request, 'You have successfuly submitted your score predictions. GOOD LUCK!')
               
        
    return render(request, "competition.html", {'form': form,'points':points,'highest_points':highest_points,'total_entries':total_entries})

