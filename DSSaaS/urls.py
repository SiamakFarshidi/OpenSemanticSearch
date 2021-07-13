from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^api/', include(('api.urls','api'), namespace="api")),
	url(r'^entity_rest_api/', include(('entity_rest_api.urls',"entity_rest_api"), namespace="entity_rest_api")),
	url(r'^setup/', include(('setup.urls',"setup"), namespace="setup")),
	url(r'^crawler/', include(('crawler.urls',"crawler"), namespace="crawler")),
	url(r'^files/', include(('files.urls',"files"), namespace="files")),
	url(r'^datasources/', include(('datasources.urls',"datasources"), namespace="datasources")),
	url(r'^annotate/', include(('annotate.urls',"annotate"), namespace="annotate")),
	url('thesaurus/', include(('thesaurus.urls', "thesaurus"),namespace="thesaurus")),
	url(r'^rss_manager/', include(('rss_manager.urls',"rss_manager"), namespace="rss_manager")),
	url(r'^querytagger/', include(('querytagger.urls',"querytagger"), namespace="querytagger")),
	url(r'^search-list/', include(('search_list.urls',"search_list"), namespace="search_list")),
	url(r'^csv/', include(('csv_manager.urls',"csv_manager"), namespace="csv_manager")),
	url(r'^ontologies/', include(('ontologies.urls',"ontologies"), namespace="ontologies")),
	url(r'^hypothesis/', include(('hypothesis.urls',"hypothesis"), namespace="hypothesis")),
	url(r'^graph/', include(('visual_graph_explorer.urls',"graph"), namespace="graph")),
	url(r'^search_entity/', include(('search_entity.urls',"search_entity"), namespace="search_entity")),
	url(r'^morphology/', include(('morphology.urls',"morphology"), namespace="morphology")),
	url(r'^twitter/', include(('twitter.urls',"twitter"), namespace="twitter")),
	url('api-auth/', include(('rest_framework.urls', "rest_framework"), namespace="rest_framework")),
	url(r'^DSS/', include(('InferenceEngine.urls', "InferenceEngine"), namespace="InferenceEngine")),  # home page
]
