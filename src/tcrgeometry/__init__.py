# src/tcrgeometry/__init__.py
from __future__ import annotations
from importlib.resources import files
from pathlib import Path

# ---- Package-wide data path (installed resource) ----
# Points to: tcrgeometry/data/consensus_output
# 'files()' returns a Traversable; coerce to a usable Path-like.
_DEFAULT_DATA_PATH = files("tcrgeometry.data").joinpath("consensus_output")
DATA_PATH: Path = Path(str(_DEFAULT_DATA_PATH))

__all__ = [
    "DATA_PATH",
    "calc_tcr_geometry",
    "calc_tcr_geometry_MD",
    "change_tcr_geometry",
    "get_anchor_coords",
]

# ---- Public API (lazy imports to avoid circulars) ----
def calc_tcr_geometry(*args, **kwargs):
    from .calc_geometry import run
    return run(*args, **kwargs)

def calc_tcr_geometry_MD(*args, **kwargs):
    from .calc_geometry_MD import run
    return run(*args, **kwargs)

def change_tcr_geometry(*args, **kwargs):
    from .change_geometry import run
    return run(*args, **kwargs)

def get_anchor_coords(*args, **kwargs):
    from .get_anchor_coords import run
    return run(*args, **kwargs)
