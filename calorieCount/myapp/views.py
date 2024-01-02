from django.shortcuts import redirect, render
from .models import Food, Consume
# Create your views here
def index(request):
    if request.method == 'POST':
        food_consume = request.POST.get('food_consumed')
        consume = Food.objects.get(name=food_consume)
        user = request.user
        consume = Consume(user=user, food_consume=consume)
        consume.save()
        foods = Food.objects.all()
    else:
         foods = Food.objects.all()

    consume_food = Consume.objects.filter(user=request.user )
   
    return render(request,'myapp/index.html',{'foods':foods, 'consume_food':consume_food })


def delete_consume(request, id):
    Consume_food = Consume.objects.get(id=id)
    if request.method == "POST":
        Consume_food.delete()
        return redirect('/')
    else:
        return render (request, "myapp/delete.html")