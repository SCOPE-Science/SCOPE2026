---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Möbius inversion on subspace lattice F2^3 gives E tau = sum_7H 9/(9-a_H b_H) -2 sum_7L 9/(9-a_L b_L)+72/(9-a_0 b_0). The 120 possible size-three multisets of eight vectors produce exactly 5922 full-rank unordered pairs, all covered including zeros/repeats. Independent exact rational enumeration found 55 values, unique min 125/56 on 28 pairs with A=U\{0} and B any 3 distinct outside U; next min 127/56 on 42 pairs. Failing t-step histories for equality are 3(2^t+1) among 9^t, giving tail 3(2/9)^t+3(1/9)^t. The enumeration is finite AND exhaustive for the theorem domain, not extrapolated to larger codes.

## originality

PASS

Theorem II.3 of Kong et al. supplies general Möbius recovery formula for a specified code/layout, not optimization across all non-MDS binary rank-3, six-column 3+3 allocations. Binary [6,3] MDS is impossible, so its MDS optimization result does not apply. Earlier small-field single-container coverage and rank-two optimal code theorem differ. No located exact 125/56 sharp bound and Fano family.

## value

PASS

This is a mathematically motivated first non-MDS small-field balanced two-container coverage depth optimum, including all repetition and zero degeneracies, its complete exact Fano-geometric equality family and full recovery tail. It fills the precise model gap identified in distributed DNA coverage literature. An exhaustive exact finite census is substantive because it covers the complete natural parameter domain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
