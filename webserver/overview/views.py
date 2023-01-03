from django.shortcuts import render
from django.template import loader

# Create your views here.

def mainoverview(request) :
    # template = loader.get_template('overview\overviewpage.html')
    histring ="gonna say hi to pass args"
    context = {'sayhi' : histring}

    return render(request,'overview\overviewpage.html',context)
