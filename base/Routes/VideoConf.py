from django.shortcuts import render

def MeetRoom(request):
    return render(request, 'Conf/conf_index.html')
