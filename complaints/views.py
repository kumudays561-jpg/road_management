from django.shortcuts import render, redirect
from .forms import ComplaintForm
from .models import Complaint
from django.contrib.auth.decorators import login_required

@login_required
def add_complaint(request):

    if request.method == 'POST':
        form = ComplaintForm(request.POST,request.FILES)

        if form.is_valid():

            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()

            return redirect('complaint_list')

    else:
        form = ComplaintForm()

    return render(
        request,
        'complaints/add_complaint.html',
        {'form': form}
    )

@login_required
def complaint_list(request):

    complaints = Complaint.objects.all()

    return render(
        request,
        'complaints/list.html',
        {'complaints': complaints}
    )

@login_required
def engineer_dashboard(request):

    complaints = Complaint.objects.filter(
        assigned_engineer=request.user
    )

    return render(
        request,
        'complaints/engineer_dashboard.html',
        {'complaints': complaints}
    )

@login_required
def update_status(request, complaint_id):

    complaint = Complaint.objects.get(
        id=complaint_id
    )

    complaint.status = "Resolved"
    complaint.save()

    return redirect('engineer_dashboard')