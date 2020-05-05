from todo.abstract_models import get_attachment_upload_dir  # noqa
from todo.get_model import get_model

TaskList = get_model("TaskList")
Task = get_model("Task")
Comment = get_model("Comment")
Attachment = get_model("Attachment")
