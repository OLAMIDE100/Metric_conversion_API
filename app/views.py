from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class ConvTemp(View):
    def post(self, request):
       
        Value = request.POST.get("Value")
        Units =  request.POST.get("Units")


        if (Units == '' or Value == ''):

            data = {"answer": f" ENTER VALUE OR UNIT"}

            return JsonResponse(data,status=201)
        else:
            if Units == 'fahrenheit':
                result = (int(Value) - 32) *  0.5556
                data = {"answer": f"{result} celsuis"}

            elif Units == 'celsuis':

                result = (int(Value) * 1.8) + 32 

                data = {"answer": f"{result} fahrenheit"}
    
            return JsonResponse(data,status=201)