# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 flxk1
"""loomground-escalation — How much autonomy do these factors leave?

One narrow problem. See :mod:`loomground_escalation.escalation` for the reasoning;
this module only re-exports it and the version.
"""

from ._version import __version__
from .escalation import (
    Ladder,
    Factor,
    Escalation,
    ceiling,
    autonomy_verdict,
    fold_autonomy,
    relax,
)

__all__ = [
    "__version__",
    "Ladder",
    "Factor",
    "Escalation",
    "ceiling",
    "autonomy_verdict",
    "fold_autonomy",
    "relax",
]
