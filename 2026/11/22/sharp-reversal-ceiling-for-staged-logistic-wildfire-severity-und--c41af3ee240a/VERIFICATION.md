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

# Reproduction and boundary checks

Run `python3 checker.py` in the same directory. The script requires only the Python standard library and performs exact Fraction arithmetic: it expands both cubic denominators, checks all six rational sign brackets for three distinct negative roots, checks two exact crossover locations, checks three exact risk differences, and runs 30,000 further exact rational comparisons over one to eight stages and two-stage crossing criteria. The canonical proof of the universal theorem is in `RESULT.md`.

The negative-root interval certificate consists of \((-16/5,-3)\), \((-2,-7/4)\), and \((-6/5,-1)\), with alternating signs at their endpoints, so the cubic has all three required real negative roots. The difference of monic denominator polynomials is \((t-1)(t-2)/50\), yielding exactly two positive crossings. The proof of arbitrary-crossing sharpness relies on existence of a sufficiently small perturbation maintaining real negative simple roots, not on floating-point root-finding.

No stochastic field fit, independent scientific validation, completeness of literature priority, or finite-sample error bound is established. A finite checker output is corroborative evidence, not an infinite-case proof.
