from django.conf import settings
from django.urls import path
from todo import views
from todo.features import HAS_TASK_MERGE

app_name = "todo"
id_format = getattr(settings, "DJANGO_TODO_ID_FORMAT", "int")
list_path_prefix = getattr(settings, "DJANGO_TODO_LIST_PATH_PREFIX", "")

urlpatterns = [
    path("", views.list_lists, name="lists"),
    # View reorder_tasks is only called by JQuery for drag/drop task ordering.
    path("reorder_tasks/", views.reorder_tasks, name="reorder_tasks"),
    # Allow users to post tasks from outside django-todo (e.g. for filing tickets - see docs)
    path("ticket/add/", views.external_add, name="external_add"),
    # Three paths into `list_detail` view
    path("mine/", views.list_detail, {"list_slug": "mine"}, name="mine"),
    path(
        "%s<%s:list_id>/<str:list_slug>/completed/" % (list_path_prefix, id_format),
        views.list_detail,
        {"view_completed": True},
        name="list_detail_completed",
    ),
    path(
        "%s<%s:list_id>/<str:list_slug>/" % (list_path_prefix, id_format),
        views.list_detail,
        name="list_detail",
    ),
    path(
        "%s<%s:list_id>/<str:list_slug>/delete/" % (list_path_prefix, id_format),
        views.del_list,
        name="del_list",
    ),
    path("add_list/", views.add_list, name="add_list"),
    path("task/<%s:task_id>/" % id_format, views.task_detail, name="task_detail"),
    path(
        "attachment/remove/<%s:attachment_id>/" % id_format,
        views.remove_attachment,
        name="remove_attachment",
    ),
]

if HAS_TASK_MERGE:
    # ensure mail tracker autocomplete is optional
    from todo.views.task_autocomplete import TaskAutocomplete

    urlpatterns.append(
        path(
            "task/<%s:task_id>/autocomplete/" % id_format,
            TaskAutocomplete.as_view(),
            name="task_autocomplete",
        )
    )

urlpatterns.extend(
    [
        path(
            "toggle_done/<%s:task_id>/" % id_format,
            views.toggle_done,
            name="task_toggle_done",
        ),
        path("delete/<%s:task_id>/" % id_format, views.delete_task, name="delete_task"),
        path("search/", views.search, name="search"),
        path("import_csv/", views.import_csv, name="import_csv"),
    ]
)
