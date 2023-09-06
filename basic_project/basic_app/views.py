from django.shortcuts import render
from basic_app.forms import EnquiryForm

def index(request):
    return render(request,'basic_app/index.html')

def enquiry_form_view(request):
    form_empty = EnquiryForm()
    if request.method == 'POST':
        form_filled = EnquiryForm(request.POST)
        if form_filled.is_valid():
            form_filled.save(commit=True)
            print('Form Validated')
            print("Name: " + form_filled.cleaned_data['name'])
            print("email: " + form_filled.cleaned_data['email'])
            print("text: " + form_filled.cleaned_data['text'])
            return render(request, 'basic_app/form_page.html', {'form' : form_empty})
    else:
        print('Form Invalid')
    return render(request, 'basic_app/form_page.html', {'form' : form_empty})
    