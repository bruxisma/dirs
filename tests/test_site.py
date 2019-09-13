from dirs import Site


class TestDefaultSite:
    def test_config(self, site: Site):
        assert list(Site.config_dirs()) == site.config


class TestXDGPaths:
    pass


def test_config_dirs():
    assert list(Site.config_dirs())


def test_data_dirs():
    assert list(Site.data_dirs())


def test_config():
    assert list(Site.config_dirs()) == Site("").config


def test_data():
    assert list(Site.data_dirs()) == Site("").data

