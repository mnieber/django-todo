import importlib

from django.conf import settings


def get_model_as_str(model_name):
    module_map = getattr(settings, "DJANGO_TODO_MODELS", {})
    if model_name in module_map:
        return module_map.get(model_name)[0]
    return "todo.%s" % model_name


def get_model_import_path(model_name):
    module_map = getattr(settings, "DJANGO_TODO_MODELS", {})
    if model_name in module_map:
        row = module_map.get(model_name)
        app_name, klass = row[0].rsplit(".", 1)
        package = row[1]
        return "%s.%s" % (package, klass)
    return "todo.default_models.%s" % model_name


def get_model(model_name):
    module, klass = get_model_import_path(model_name).rsplit(".", 1)
    return getattr(importlib.import_module(module), klass)
