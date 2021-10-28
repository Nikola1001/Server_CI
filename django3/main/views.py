from django.views.generic import ListView
from main.models import Post

class HomePageView(ListView):

     model = Post
     template_name = 'homepage.html'
