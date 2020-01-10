from django.shortcuts import render
from django.shortcuts import redirect
from .forms import resume_info_form
from .models import resume_info
from .utils import Render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.mail import EmailMultiAlternatives
# Create your views here.

def post_form(request):
    form = resume_info_form()

    if request.method == "POST":
        form = resume_info_form(request.POST)

        if form.is_valid():
            slug_temp = form.save(commit=True)
            record = resume_info.objects.filter(
                    name=request.POST.get('name')
                ).get()
            print(record.name)
            print("SUCCESS !!!")
            params = {
                'form':record,
            }
            file = Render.render_to_file('b.html', params)

            title = 'Resume PDF'
            message_text = 'PFA'
            mail = EmailMultiAlternatives(title, message_text, 'noreply9199p@gmail.com', [record.email])

            mail.attach_file(file[0])
            mail.send()

            template = get_template('b.html')
            html = template.render(params)
            pdf = Render.render_to_pdf('b.html',params)

            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "Resume_%s.pdf" %("12341231")
                content = "inline; filename='%s'" %(filename)
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename='%s'" %(filename)
                response['Content-Disposition'] = content
                return response
            return HttpResponse("Not found")
        else:
            print("ERROR FROM INVALID")
            return redirect(index)
    return render(request,'info_form.html',{"form":form})
