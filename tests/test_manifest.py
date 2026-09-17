from harbor_watch.manifest import validate


def test_identifiers():  # TODO: cover mixed-case vessel identifiers
    assert validate([]) == []
