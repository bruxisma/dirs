from dirs import User


def test_config_home():
    assert User.config_home().is_dir()


def test_cache_home():
    assert User.cache_home().is_dir()


def test_data_home():
    assert User.data_home().is_dir()


def test_data(user: User):
    assert user.data == User.data_home()


def test_config(user: User):
    assert user.config == User.config_home()
    assert user.config.is_dir()


def test_cache(user: User):
    assert user.cache == User.cache_home()
    assert user.config.is_dir()