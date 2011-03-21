from piston.handler import BaseHandler
from chegamos_api.badges.models import Badge, Rule, History

class BadgeHandler(BaseHandler):
	model = Badge

class RuleHandler(BaseHandler):
	model = Rule 

class HistoryHandler(BaseHandler):
	model = History 

