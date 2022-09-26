class BaseError(Exception):
    message = 'Ошибка'


class NotEnoughSpace(BaseError):
    message = 'Не достаточно места на складе'


class NotEnoughProduct(BaseError):
    message = 'Не достаточно товара на складе'


class TooManyDifferentProducts(BaseError):
    message = 'Слишком много разных товаров'


class InvalidRequest(BaseError):
    message = 'Неправильный запрос. Попробуйте снова'
