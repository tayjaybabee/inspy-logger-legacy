class ApplicationError(BaseException):
    """

    Base class for most of the exceptions in this package.

    """

    def __init__(self):
        pass


class UnknownError(Exception,ApplicationError):

    def __init__(self, info=None):
        super().__init__()
        msg = str('\n\nAn error of type has occurred, someone must have screwed up. ')
        if info is not None:
            e_info = str('\nThere was additional information provided where this error occurred:')
            self.message = str(f'\n\n{msg}\n{e_info}\n\n    {info}')
        else:
            self.message = msg
