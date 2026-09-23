
from django.urls import path

from hr import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logout_view, name="logout"),
    # path("viewemployees/", viewemployees, name="viewemployees"),
    path('employees/',views.employee_list,name='employee_list'),
    path('employees/add/',views.employee_create,name='employee_create'),
    path("employees/<int:id>/edit/", views.employee_update, name="employee_update"),
    path("employees/<int:id>/delete/", views.employee_delete, name="employee_delete"),
    path("leave_approval/",views.leave_approval,name="leave_approval"),
    path("leave/<int:id>/action/",views.leave_action,name="leave_action"),
    path("department_list/",views.department_list,name="department_list"),
    path("designation_list/",views.designation_list,name="designation_list"),
    path('departments/add/',views.department_create,name='department_create'),
    path('departments/edit/<int:id>/',views.department_update,name='department_update'),
    path('departments/delete/<int:id>/',views.department_delete,name='department_delete'),
    path('designations/add/',views.designation_create,name='designation_create'),
    path('designations/edit/<int:id>/',views.designation_update,name='designation_update'),
    path('designations/delete/<int:id>/',views.designation_delete,name='designation_delete'),

]