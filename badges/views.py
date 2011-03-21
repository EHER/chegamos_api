from badges.models import Badge
from django.http import HttpResponse

def index(request):
	badges_list = Badge.objects.all()
	output = ', '.join([b.name for b in badges_list])
	return HttpResponse(output)
	
def detail(request, badge_id):
	return HttpResponse("Badge %s" % badge_id)

