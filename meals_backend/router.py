from meats.views import MeatViewSet
from veggies.views import VeggieViewSet
from dishes.views import DishViewSet
from meals.views import MealViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('meats', MeatViewSet, base_name='meat')
router.register('veggies', VeggieViewSet, base_name='veggie')
router.register('dishes', DishViewSet, base_name='dish')
router.register('meals' , MealViewSet, base_name='meal')