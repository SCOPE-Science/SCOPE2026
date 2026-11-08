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

# Verification record

The analytic proof gives the full complex rank for every odd prime and every primitive additive character. Its decisive steps are (i) permutation-equivalent abelian convolution, (ii) the exact sum over the principal-unit factor, (iii) exclusion of cancellation in two-point stationary fibers, and (iv) an involution orbit count on quadratic residues.

For computational corroboration, run `python checker.py` with `numpy>=1.23` installed. Direct complex singular-value decompositions checked orders \(p=3,5,7,11,13\) for primitive character parameters \(c=1,2\) (the chosen parameters are units at all these primes). The integer rank predictions and, at \(p\equiv3\pmod4\), every positive singular value matched with numerical tolerance \(10^{-7}\). Exact residue-field orbit enumerations also checked \(p=17,19,23,29,31,37,41\). The checker prints `SQUARE_UNIT_HYPERBOLA_RANK_PASS` on success.

Floating-point verification is **not** an infinite proof and cannot certify exact rank absent the independent analytic argument. Historical literature checks have finite coverage; they do not supply independent scientific validation.
