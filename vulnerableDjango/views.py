from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from forms import MessageForm
from models import Messages

import md5


@csrf_exempt
def message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            name    = form.cleaned_data['name']
            content = form.cleaned_data['content']
            ip      = request.META['REMOTE_ADDR']

            sess = request.session
            if not sess.has_key( 'name' ) or sess['name'] != name:
                sess['name'] = name

            if name.lower() == 'orange':
                name    = 'Wrong way'
                content = 'Try to pwn a shell instead of cracking md5.'
            elif md5.new(name).hexdigest() == 'e5bc16fcbca0f279df17b66d8c37e109':
                name = 'Orange'

            Messages( name=name,
                      content=content, 
                      ip=ip ).save()
            return HttpResponseRedirect( '/' )
    else:
        sess = request.session.load()
        if sess.has_key( 'name' ):
            default = sess['name']
        else:
            default = 'Guest'

        form = MessageForm( initial={'name': default} )

    messages = Messages.objects.order_by('id').reverse()[:100]
    response = render_to_response( 'message.html',
                                   {'form': form, 'messages': messages} )
    return response