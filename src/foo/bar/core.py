"""Example core module.

Uses numpy to generate random numbers.
"""

import numpy as np
import numpy.typing as npt


def random(shape=(10,), dtype: npt.DTypeLike = float) -> npt.NDArray:
    return np.random.random(shape).astype(dtype)
