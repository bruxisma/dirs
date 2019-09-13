from pathlib import Path
import pytest

from dirs import Site, User


@pytest.fixture
def site() -> Site:
    return Site("")


@pytest.fixture
def user() -> User:
    return User("")


def pytest_addoption(parser):
    parser.addoption(
        "--config-dir", action="append", help="Additional paths for Site.config_dirs()"
    )
    parser.addoption("--data-dir", action="append", help="Additional paths for Site.data_dirs()")

    parser.addoption("--config-home", type=Path, help="Manual override for User.config_home()")
    parser.addoption("--cache-home", type=Path, help="Manual override for User.cache_home()")
    parser.addoption("--data-home", type=Path, help="Manual override for User.data_home()")

