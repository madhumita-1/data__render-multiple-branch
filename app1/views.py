from django.shortcuts import render
def data_render(request):
    d={'name':'madhu','age':'22'}
    return render(request,'data_render.html,context=d)    

