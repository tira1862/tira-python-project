#custom exception is for when trying to access an entity that does not exist

class IdNotFound(Exception):
    pass