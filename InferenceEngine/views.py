from django.http import HttpResponse
import json

from django.shortcuts import render
from .forms import Profile_Form
from .models import User_Profile

#--------------------------------------------------------------

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
def create_profile(request):
    form = Profile_Form()
    if request.method == 'POST':
        form = Profile_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.display_picture = request.FILES['display_picture']
            file_type = user_pr.display_picture.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return render(request, 'profile_maker/error.html')
            user_pr.save()
            return render(request, 'profile_maker/details.html', {'user_pr': user_pr})
    context = {"form": form,}
    return render(request, 'profile_maker/create.html', context)
#--------------------------------------------------------------
def processSingleReq(request):
    FeatureID = request.GET["ID"]
    FeatureReq = request.GET["Req"] # MoSCoW

    return HttpResponse(FeatureID+" >< "+FeatureReq)
# --------------------------------------------------------------
def processReqFile(request):
    result="{id:123}"
    return HttpResponse(json.dumps({'queue': result.id}), content_type="application/json")
# --------------------------------------------------------------
def index(request):
    return HttpResponse('Siamak123')

