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

Run `python verification.py` with Python 3 and `sympy`, `numpy`, `scipy`, `mpmath` installed. The checker was executed successfully with output:

`PASS 428 deterministic assertions: polynomial algebra, shape ordering, unique positive root, endpoint asymptotics, independent Gamma-CDF quadrature`

Symbolic checks simplify the derivative's quartic polynomial and the positive shape derivative identically, rather than relying on floating-point comparisons. Numerical checks evaluate the derivative sign and the direct spectral response on a range of positive shape/frequency pairs, compare positive quartic roots against independent root computations, test shape ordering, and evaluate low-/high-frequency asymptotic ratios. Independent high-precision integration of the gamma cumulative distribution times the exponential age kernel verifies the complex renewal factor at four parameter triples.

# Scope of verification

The finite checks do not establish an infinite quantifier or guarantee novelty. Universal statements follow from the analytical age-integral identity, one-sign-change quartic proof, strict positive shape derivative and controlled polynomial asymptotics in RESULT.md. No experimental confirmation of gamma maturation in a physical double-well system is asserted.
