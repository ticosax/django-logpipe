from typing import Any

from rest_framework import serializers

from .abc import Record


class LogPipeError(Exception):
    pass


class LogPipeMessageError(LogPipeError):
    message: Record

    def __init__(self, descr: Any, message: Record):
        super().__init__(descr)
        self.message = message


class UnknownFormatError(LogPipeError):
    pass


class IgnoredMessageTypeError(LogPipeMessageError):
    pass


class UnknownMessageTypeError(LogPipeMessageError):
    pass


class UnknownMessageVersionError(LogPipeMessageError):
    pass


class InvalidMessageError(LogPipeMessageError):
    pass


class ValidationError(LogPipeMessageError, serializers.ValidationError):
    pass


class MissingTopicError(LogPipeError):
    pass


class ShardProvisionedThroughputExceededError(LogPipeError):
    """
    Shard exhausted its provisioned throughput capacity.
    We failed to recover from this error after n retry with 5s waiting time.
    """

    def __init__(self, retries: int):
        self.message = f"After {retries} attempt{'s' if retries else ''}, we couldn't get records from Kinesis. Giving up."
