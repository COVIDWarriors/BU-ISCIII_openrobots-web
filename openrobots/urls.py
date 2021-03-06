from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    #path('createPCRProtocolFile', views.create_pcr_protocol_file, name = 'create_pcr_protocol_file'),
    #path('createExtractionProtocolFile', views.create_extraction_protocol_file, name = 'create_extraction_protocol_file'),
    path('defineLabware', views.define_labware, name = 'define_labware'),
    path('defineRobot', views.define_robot, name = 'define_robot'),
    path('detailLabwareInventory=<int:labware_id>', views.detail_labware_inventory, name = 'detail_labware_inventory'),
    path('detailModuleInventory=<int:module_id>', views.detail_module_inventory, name = 'detail_module_inventory'),
    path('detailRobotInventory=<int:robot_id>', views.detail_robot_inventory, name = 'detail_robot_inventory'),
    path('detailActionRobot=<int:action_id>', views.detail_action_robot, name = 'detail_action_robot'),
    path('displayTemplateFile=<int:p_template_id>', views.display_template_file, name = 'display_template_file'),
    path('labwareInventory', views.labware_inventory, name = 'labware_inventory'),
    path('modulesInventory', views.modules_inventory, name = 'modules_inventory'),
    path('uploadProtocolTemplates', views.upload_protocol_templates, name = 'upload_protocol_templates'),
    path('listOfRequests', views.list_of_requests, name = 'list_of_requests'),
    path('requestProtocolStationA', views.request_protocol_station_A, name = 'request_protocol_station_A'),
    path('requestProtocolStationB', views.request_protocol_station_B, name = 'request_protocol_station_B'),
    path('requestProtocolStationC', views.request_protocol_station_C, name = 'request_protocol_station_C'),
    path('robotInventory', views.robot_inventory, name = 'robot_inventory'),
    path('robotsJobs', views.robots_jobs, name ='robots_jobs'),
	]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
