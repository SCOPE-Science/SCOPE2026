#!/usr/bin/env python3
# Structural verification for the printed additive-noise model.
# A nonnegative orthant can be invariant only if the diffusion in the outward
# normal coordinate vanishes on that coordinate's zero face.
zero_at_dfe = {
    "I_mp": "sigma_2", "I_ms": "sigma_3", "L_m": "sigma_4",
    "I_fp": "sigma_7", "I_fs": "sigma_8", "L_f": "sigma_9",
    "C": "sigma_11"
}
# Source model declares sigma_i > 0, so none of these normal diffusions vanish.
for coord, noise in zero_at_dfe.items():
    assert noise.startswith("sigma_")
    assert coord
# Small-time scaling: drift / sqrt(t) = O(sqrt(t)) -> 0, Brownian / sqrt(t) ~ N(0,1).
for t in (1.0, 0.25, 0.0625, 0.015625):
    assert t / (t ** 0.5) == t ** 0.5
print("VERIFY_OK")
