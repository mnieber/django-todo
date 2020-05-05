from todo.abstract_models import (AbstractAttachment, AbstractComment,
                                  AbstractTask, AbstractTaskList)


class Comment(AbstractComment):
    pass


class Attachment(AbstractAttachment):
    pass


class Task(AbstractTask):
    pass


class TaskList(AbstractTaskList):
    pass
