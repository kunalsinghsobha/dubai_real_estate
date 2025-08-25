"""Minimal stub of the :mod:`chdb` package used for testing.

The real ``chdb`` package provides an in-memory ClickHouse implementation.
This stub exposes a ``connect`` function so that our connection code can be
imported and unit tested without requiring the actual dependency.  The
function raises :class:`ImportError` to signal that the real package is
missing.  Tests can monkeypatch :func:`connect` with a mock implementation.
"""

def connect(*args, **kwargs):
    """Placeholder connect function.

    Raises
    ------
    ImportError
        Always raised to indicate that the real ``chdb`` package is not
        installed.
    """
    raise ImportError(
        "chdb package is required for CHDB connections. Install with: pip install chdb"
    )
