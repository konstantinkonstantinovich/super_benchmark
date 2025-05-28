class BaseOperation:
    """
    Base operation for all operations.
    Contains __init__ and main method which should run all other methods - execute()
    """

    def __init__(self):
        pass

    def execute(self):
        """
        Main method of any operation. Executes all other methods and returns result.
        """
        raise NotImplementedError("Method execute is not implemented")
