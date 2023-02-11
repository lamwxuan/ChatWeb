from urllib import request
from django.shortcuts import redirect

from django.shortcuts import render, HttpResponse

from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt

def rediret_to_index(request):
    return redirect("/index")

# Create your views here.
def index(request):

    name = "liam"
    print(request.GET)
    
    return render(request, "index.html", {"n1": name})



# Create your views here.
@xframe_options_exempt
def welcome(request):
    return render(request, "welcome.html")


#sponse(json.dumps(resp))

def create_bot(bot_type):
    sk = ''
    orgId = 'org-CmiqYxt4No1NIDimA7unHXcj'

    """
    create a channel instance
    :param channel_type: channel type code
    :return: channel instance
    """
    if bot_type == 'openAI':

        # OpenAI 官方对话模型API
        from chatgpt.chatgpt import OpenAIBot
        return OpenAIBot()
    raise RuntimeError