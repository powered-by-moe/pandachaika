import typing

from core.base.types import ProviderSettings, DataDict

if typing.TYPE_CHECKING:
    from core.base.setup import Settings


class OwnSettings(ProviderSettings):
    def __init__(self, global_settings: 'Settings', config: typing.Dict[str, typing.Any]) -> None:
        super().__init__(global_settings, config)


def parse_config(global_settings: 'Settings', config: typing.Dict[str, typing.Any]) -> 'OwnSettings':

    settings = OwnSettings(global_settings, config)

    return settings
