---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and limits

From the package root, run `python3 artifacts/verify.py`. The program depends only on Python's standard library (`fractions`, `itertools`, `math`). It checks 680 exact-rational midpoint-grid divisibility chains: initial panel counts 1 or 2, depths 1–4, every sequence of refinement ratios from \(\{2,3,4,5\}\). Each case computes the collected node weights directly and tests the precise parity classification, alternating magnitude growth, the bad-block negative-mass formula, absolute norm, largest weight, the constant moment and polynomial moments through degree five. Five additional representative chains are checked through all degrees claimed by polynomial exactness. The expected deterministic output is in `artifacts/verification.txt`.

The verification script is an executable finite corroboration. The proof for every integer-divisibility chain, regardless of depth, is in `RESULT.md`, and is based on exact rational Lagrange weights, parity of midpoint-node overlaps, an analytic bound on adjacent magnitudes, and midpoint Euler–Maclaurin exactness. The finite computations do not establish infinite generality on their own. Historical novelty and all potential applications require independent consideration. No external review or independent validation is claimed.
