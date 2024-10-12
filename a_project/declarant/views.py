from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms.declaration import DeclarantForm 

'''def declarant_view(request):
    if request.method == 'POST':
        form = DeclarantForm(request.POST)
        if form.is_valid():
            # Les données sont valides, vous pouvez les enregistrer
            form.save()
            
            # Rediriger vers une page de succès ou afficher un message
            return HttpResponse('Form successfully submitted.')
        else:
            # Le formulaire n'est pas valide, afficher les erreurs
            return render(request, 'base.html', {'form': form})
    else:
        form = DeclarantForm()
        return render(request, 'base.html', {'form': form}) '''

def profile(request):
    return render(request, 'profile.html')
