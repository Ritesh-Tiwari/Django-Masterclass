from django.shortcuts import render
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