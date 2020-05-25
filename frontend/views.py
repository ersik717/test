from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.
def index_view(request):
	return render(request, 'frontend/index.html', context=None)


# class HelloWorldView(APIView):

# 	def get(self, request):
# 		return Response(data={"hello":"world"}, status=status.HTTP_200_OK)

