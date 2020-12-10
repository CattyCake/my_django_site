from django.shortcuts import render
from .models import Order
from django.shortcuts import redirect
from .forms import PostForm
from pytz import timezone



def order_list(request):
    orders = Order.objects.order_by('order_name')
    return render(request, 'my_app/orders_list.html', {'orders': orders})

def order_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('lessons_list')
    else:
        form = PostForm()
        return render(request, 'my_app/post_edit.html',{'form': form})

