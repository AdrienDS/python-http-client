import json


class HTTPError(Exception):
    """ Base of all other errors"""

    def __init__(self, code, reason=None, body='', headers=None):
        self.status_code = code
        self.reason = reason
        self.body = body
        self.headers = headers or {}

    @property
    def to_dict(self):
        """
        :return: dict of response error from the API
        """
        return json.loads(self.body)


class BadRequestsError(HTTPError):
    pass


class UnauthorizedError(HTTPError):
    pass


class ForbiddenError(HTTPError):
    pass


class NotFoundError(HTTPError):
    pass


class MethodNotAllowedError(HTTPError):
    pass


class PayloadTooLargeError(HTTPError):
    pass


class UnsupportedMediaTypeError(HTTPError):
    pass


class TooManyRequestsError(HTTPError):
    pass


class InternalServerError(HTTPError):
    pass


class ServiceUnavailableError(HTTPError):
    pass


class GatewayTimeoutError(HTTPError):
    pass


err_dict = {
    400: BadRequestsError,
    401: UnauthorizedError,
    403: ForbiddenError,
    404: NotFoundError,
    405: MethodNotAllowedError,
    413: PayloadTooLargeError,
    415: UnsupportedMediaTypeError,
    429: TooManyRequestsError,
    500: InternalServerError,
    503: ServiceUnavailableError,
    504: GatewayTimeoutError
}


def handle_error(error):
    try:
        exc = err_dict[error.status_code](error)
    except KeyError:
        return HTTPError(error)
    return exc
