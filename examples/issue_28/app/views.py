import calendar
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.charts.views import GroupByChartView
from flask_appbuilder.models.group import aggregate_count
from flask_babel import lazy_gettext as _


from app import db, appbuilder
from .models import Parent, Child



class ChildView(ModelView):
    datamodel = SQLAInterface(Child)
 
class ParentView(ModelView):
    datamodel = SQLAInterface(Parent)
    related_views = [ChildView]

db.create_all() 
appbuilder.add_view(ParentView, "Parent", icon="fa-folder-open-o", category="Stuff", category_icon='fa-envelope')
appbuilder.add_view(ChildView, "Child", icon="fa-folder-open-o", category="Stuff", category_icon='fa-envelope')

