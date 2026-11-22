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

# Reproducibility and mathematical scope

Run `python verify.py` (Python 3 standard library only). It implements the exact union-of-power return partition using three signed, absolutely convergent Laplace sums. For each of eight coprime exponent pairs \((2,3),(2,5),(3,4),(3,5),(3,7),(4,5),(4,7),(4,9)\), it finds the unique saddle numerically at marker densities \(10^{-3},10^{-5},10^{-7}\), compares first and second asymptotic approximations, and checks finite integer-power intersections and the exponent-order identity.

**Actual extracted-file execution:** 24 saddle/entropy checks, eight finite intersection checks, and eight exponent-order checks completed without assertion failure. Truncations use an exponential threshold of 64; the neglected positive tails can be bounded by decreasing-tail integrals beyond the cutoff. Tests do not verify the limit for all densities or infinitely many exponent pairs.

Analytical correctness rests instead on the explicit inclusion-exclusion equality for coprime power sets, the induced entropy inequality and attaining renewal process, the twice-differentiable Euler-summation expansion, and the second-order saddle calculation recorded in `RESULT.md`. The argument covers arbitrary fixed coprime integers \(2\le r<s\) in the low-density limit. There is no independent audit or external formal certification.
