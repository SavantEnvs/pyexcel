"""pytest plugin: call nose-style setUp()/tearDown() on plain (non-unittest.TestCase)
test classes. Older pytest ran these itself ("nose-style tests"); that support was
removed in pytest 8 (https://docs.pytest.org/en/stable/deprecations.html#support-for-
nose-tests). tests/ predates the removal and still relies on it (e.g. `class
TestSheetRow:` with a plain `def setUp(self)`), so test.sh loads this plugin
(`-p pytest_nose_setup`) instead of patching every upstream test file.
"""
import unittest


def _instance_of(item):
    instance = getattr(item, "instance", None)
    if instance is None or isinstance(instance, unittest.TestCase):
        return None
    return instance


def pytest_runtest_setup(item):
    instance = _instance_of(item)
    setup = getattr(instance, "setUp", None)
    if callable(setup):
        setup()


def pytest_runtest_teardown(item, nextitem):
    instance = _instance_of(item)
    teardown = getattr(instance, "tearDown", None)
    if callable(teardown):
        teardown()
