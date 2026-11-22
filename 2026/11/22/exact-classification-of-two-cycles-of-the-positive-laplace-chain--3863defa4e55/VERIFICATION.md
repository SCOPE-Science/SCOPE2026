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

## Exact analytical checks
The necessary identity \(q'=r'=-qr\) implies \(q-r=c\). The three real cases \(c=0\), \(c>0\), \(c<0\) yield precisely one reciprocal affine Laplace transform or a pair of geometric rational transforms. Both members of the latter are strictly positive and have the same Laplace abscissa, and differentiation verifies both directions of the cycle. Their total masses differ by the strictly positive lattice spacing; therefore both cannot be one.

## Reproducibility
Run `python3 verify.py`. It uses the standard library's exact `Fraction` arithmetic to check derivative identities, finite geometric truncation errors and probability-slice normalizations for multiple rational parameter choices. These finite checks do not prove the infinite classification, which rests on the differential identity, complete case split and Laplace uniqueness.

## Limits
No result about higher-period cycles, rates of convergence, or uniqueness of preperiodic chains is implied. No independent audit has been performed.
