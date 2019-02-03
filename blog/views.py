from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import Http404

from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django import forms
from django.http import HttpResponse
try:
    from django.utils import simplejson as json
except ImportError:
    import json

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import bleach
from django.conf import settings
from .untitled1 import *

# Create your views here.
#context={"img":"blog/lsup.png"}
def home(request,pk,balance):
    messages.success(request, f'Your news is legitimate and real,and your stake is refunded.')
    post = Post.objects.filter(pk=pk).first()
    post.author.profile.balance = balance
    post.author.profile.save()
    return redirect('blog-home')

class PostListView(ListView):

    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'

    paginate_by = 5
    ordering = ['-date_posted']
    #success_url = '/blog/'

def curr2(request,pk):

    post = Post.objects.filter(pk=pk).first()
    print (post.title,pk)
    writer = post.writer
    balance = post.author.profile.balance
    return redirect('https://rogo.serveo.net/submit/{}/{}/{}/{}'.format(pk,-1,writer,balance))


def ml(request, pk, balance):
    print("dhvjgsv",balance)
    post = Post.objects.filter(pk=pk).first()
    post.author.profile.balance = balance
    print(post.author.profile.balance)
    post.author.profile.save()
    text= post.content
    print (text)
    writer = post.writer

    is_valid_news = verify_news(str(text))
    post.is_real = is_valid_news
    post.save()
    print(is_valid_news)
    if(is_valid_news):
        return redirect('https://rogo.serveo.net/submit/{}/{}/{}/{}'.format(pk,1,writer,balance))
    else:
        messages.info(request, f'Your news has been detected as fake.Your stake is lost.')
        return redirect('blog-home')


#CommentForm(instance=comment_first),

class PostDetailView(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)

        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','writer', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)





@login_required
@require_POST
def like(request):
    if request.method == 'POST':
        user = request.user
        pkey = request.POST.get('pkey',None)
        ld = request.POST.get('liked')
        type = request.POST.get('type')
        ctx = None
        if type=='Post':
            post = get_object_or_404(Post,pk=pkey)
            if (ld =='Yes'):
                if post.likes.filter(id=user.id).exists():
                    # user has already liked this company
                    # remove like/user
                    #post.likes.remove(user)
                    message = 'You have liked this once.'
                else:
                    # add a new like for a company
                    post.likes.add(user)
                    if post.dislikes.filter(id=user.id).exists():
                        post.dislikes.remove(user)
                    message = 'You liked this.Your vote will be updated soon.'
            else:
                if post.dislikes.filter(id=user.id).exists():
                    # user has already liked this company
                    # remove like/user
                    #post.likes.remove(user)
                    message = 'You have disliked this once.'
                else:
                    # add a new like for a company
                    post.dislikes.add(user)
                    if post.likes.filter(id=user.id).exists():
                        post.likes.remove(user)
                    message = 'You disliked this.Your vote will be updated soon.'

            ctx = {'likes_count': post.total_likes, 'message': message}


    # use mimetype instead of content_type if django < 5
    #return redirect('blog-home')
    return HttpResponse(json.dumps(ctx), content_type='application/json')


'''
@login_required
@require_POST
def like(request):
    if request.method == 'POST':
        user = request.user
        pkey = request.POST.get('pkey',None)
        post = get_object_or_404(Post,pk=pkey)
        print ("like")
        if post.likes.filter(id=user.id).exists():
            # user has already liked this company
            # remove like/user
            #post.likes.remove(user)
            message = 'You already liked this'
        else:
            # add a new like for a company
            post.likes.add(user)
            if post.dislikes.filter(id=user.id).exists():
                post.dislikes.remove(user)
            message = 'You liked this'

    ctx = {'likes_count': post.total_likes, 'message': message}
    # use mimetype instead of content_type if django < 5
    #return redirect('blog-home')
    return HttpResponse(json.dumps(ctx), content_type='application/json')
'''
