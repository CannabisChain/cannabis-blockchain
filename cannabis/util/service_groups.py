from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "cannabis_harvester cannabis_timelord_launcher cannabis_timelord cannabis_farmer cannabis_full_node cannabis_wallet".split(),
    "node": "cannabis_full_node".split(),
    "harvester": "cannabis_harvester".split(),
    "farmer": "cannabis_harvester cannabis_farmer cannabis_full_node cannabis_wallet".split(),
    "farmer-no-wallet": "cannabis_harvester cannabis_farmer cannabis_full_node".split(),
    "farmer-only": "cannabis_farmer".split(),
    "timelord": "cannabis_timelord_launcher cannabis_timelord cannabis_full_node".split(),
    "timelord-only": "cannabis_timelord".split(),
    "timelord-launcher-only": "cannabis_timelord_launcher".split(),
    "wallet": "cannabis_wallet cannabis_full_node".split(),
    "wallet-only": "cannabis_wallet".split(),
    "introducer": "cannabis_introducer".split(),
    "simulator": "cannabis_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
