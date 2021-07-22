from pkg_resources import DistributionNotFound, get_distribution, resource_filename

try:
    __version__ = get_distribution("cannabis-blockchain").version
except DistributionNotFound:
    # package is not installed
    __version__ = "unknown"

PYINSTALLER_SPEC_PATH = resource_filename("cannabis", "pyinstaller.spec")
