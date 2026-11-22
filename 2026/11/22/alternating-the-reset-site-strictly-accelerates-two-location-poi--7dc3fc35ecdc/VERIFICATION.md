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

# Reproduction
Run `python verify.py` (Python 3, SymPy, NumPy). The checker must print `PASS` and compares:

- The Cramer's-rule renewal expression, its exact \(c\)-derivative, and the independent-location \(c=1/2\) identity by symbolic simplification.
- 120 exact rational samples of success probabilities, rate and switching probability, including both endpoint strategies.
- 20 independently assembled killed-generator linear systems for phase-tagged walks on finite cyclic lattices against separately solved no-reset discounted first-passage probabilities.
- One continuum Brownian-ring example and its exact positive iid-to-alternating mean gain.

The mathematical proof in RESULT.md establishes the universal assertion; sampling finite parameter grids, finite rings and floating-point checks alone could not establish it. A comparison of the full 2026 iid-resetting-ring source with its precise assumption about independent successive restart draws is recorded separately. No independent scientific audit has yet been conducted.
