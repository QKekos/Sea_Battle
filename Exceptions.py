
class FieldException(Exception):
    pass


class FieldUsedPointException(FieldException):
    def __str__(self):
        return 'This point already used'


class FieldCantAddShipException(FieldException):
    pass


class NonExistingShipError(FieldException):
    def __str__(self):
        return 'Ship can be only 1 at width'
