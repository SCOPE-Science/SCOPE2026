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

The exact combinatorial construction enumerates all spanning trees by deleting path edges and selecting exactly one spoke per surviving path block. It proves the bivariate polynomial for every positive integer path length. A residue calculation at the unique positive dominant pole yields the fixed-conductance moments and central limit law. An exact rational Sturm sign-variation comparison proves the unique optimizer.

To replay the finite computations, run `python3 verify_fan.py` (Python 3 standard library only) in the directory containing the supplied checker. The packaged checker compares exact rational polynomials with exhaustive edge-subset enumeration for path lengths 1 through 7 and conductances 1/2, 1, 2 and 5/3; performs a separate moment recursion; computes the exact Sturm sign sequences and verifies the rational derivative polynomial identity. Expected terminating line: `VERIFY_OK 36 groups of independent exact/numerical checks`.

Numerical large-size moment ratios and algebraic-root approximations check consistency but do not replace the proof or certify novelty. No finite-size uniqueness claim, uniform-in-conductance central limit theorem, or independent audit is asserted.
