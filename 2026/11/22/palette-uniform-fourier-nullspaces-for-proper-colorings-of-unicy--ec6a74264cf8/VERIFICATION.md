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

# Verification and reproducibility

Run `python3 check.py` from this package using Python 3.10+; it has no third-party dependencies. It directly enumerates proper colorings and compares exact character sums against the independently implemented edge-frequency formula.

The completed test execution reported `PASS TOTAL 5209 exhaustive frequency comparisons` over eleven graph/palette cases (cyclic orders three, four and five; noncyclic Klein-four; cycles and independently decorated unicyclic graphs), plus four selected checks at cycle length six with five colors. All tests passed. The six-cycle sample includes a genuinely zero balanced frequency.

For cyclic prime-order palettes, integer root-of-unity coefficients are compared by equalities of integer residue counts; for the cyclic group of order four the real and imaginary parts are compared as integer count differences. The Klein-four test uses only signs and integer arithmetic. No numerical tolerance is used.

The proof in `RESULT.md`, not finite testing, establishes every palette order, all permitted cycle lengths and arbitrarily many attached tree vertices. No general-purpose computer-assisted infinite certification and no independent audit are asserted.
