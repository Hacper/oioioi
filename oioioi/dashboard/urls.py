from django.conf.urls import patterns, include, url

contest_patterns = patterns('oioioi.dashboard.views',
    url(r'^dashboard/$', 'contest_dashboard_view', name='contest_dashboard'),
    url(r'^dashboard-message/$', 'dashboard_message_edit_view',
        name='dashboard_message_edit'),
)
