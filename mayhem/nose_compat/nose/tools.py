"""Drop-in replacement for the 3 `nose.tools` names tests/ imports (eq_, raises,
assert_not_in). Real `nose` is long EOL: `nose/importer.py` does `from imp import ...`,
and `imp` was removed in CPython 3.12, so it cannot be installed here at all.
"""
import functools


def eq_(a, b, msg=None):
    assert a == b, msg or "%r != %r" % (a, b)


def assert_not_in(member, container, msg=None):
    assert member not in container, msg or "%r found in %r" % (member, container)


def raises(*exceptions):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except exceptions:
                return
            raise AssertionError("%s not raised" % (exceptions,))
        return wrapper
    return decorator
