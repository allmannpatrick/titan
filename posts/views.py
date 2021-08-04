from django.shortcuts import render
from .forms import PostForm
import ml_predict

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from .models import Post


def fluff_result(request):
   #Process images uploaded by users
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            prediction = ml_predict.prediction(img_obj.cover.url)
            return render(request, 'fluff_results.html', {'form': form, 'img_obj': img_obj, 'prediction': prediction})
    else:
        form = PostForm()
    return render(request, 'fluff_results.html', {'form': form})


"""
    
class CreatePostView(CreateView): # new
    model = Post
    form_class = PostForm
    template_name = 'results.html'
    success_url = reverse_lazy('result')
    def form_valid(self, form):
        form.save()
        form.instance = self.request
        img = form.instance
        #prediction = ml_predict.prediction(img)
        return super().form_valid(form)
        
"""        
        
