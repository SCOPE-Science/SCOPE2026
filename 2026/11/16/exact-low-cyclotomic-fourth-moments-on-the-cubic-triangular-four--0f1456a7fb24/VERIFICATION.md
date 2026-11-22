---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Fourier Parseval expresses M4 as the sum of squares of ordered-pair convolution coefficients and independently ordered-pair autocorrelations. Three independent character/constant phases uniquely enforce a00=a10=a01=1, leaving precisely q^7 gauge representatives. The source C++ code enumerates all 1+128+2187+16384+279936=298636 representatives via exact Gaussian/Eisenstein integer pair norms, cross-checks two forms and classifies minima, next levels, maxima; the Python orbit code normalizes all six barycentric permutations and conjugation. A separate vectorized integer convolution enumeration reproduced every minimum, count, maximum, next value and number of distinct moments, and a separately written symmetry check reproduced orbit-size partitions [1], [3], [2,6], [3,6,6,6,6,6,12], [6]. Source maximum 442 uses termwise triangle-inequality equality to enforce coefficient characters. This is exhaustive only for the five finite alphabets, not unrestricted phases.

## originality

PASS

Exact phase moments for degree-two triangle and 3x3 square are published, but differ as support sets and their extrema cannot imply the degree-three ten-site classification. The ten-site minima, next-value gaps and full minimizer orbits were not present in the inspected full prior statements. No claim of priority over unindexed polyphase array tables.

## value

PASS

The complete degree-three planar triangular aperture is a natural next Fourier/antenna support after the published six-site degree-two triangle; the exact low-degree cyclotomic family is a mathematically natural small alphabet class. Its nonmonotone q response and complete orbit structure are unknown from the nearby different geometries and provide a reproducible exact design benchmark, not an arbitrary one-entry calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
