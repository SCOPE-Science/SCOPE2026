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

# Verification of clique-windmill Fourier projection theorem

Run `python3 verification_checker.py` using Python 3 and its standard library only. Expected success marker:

`WINDMILL_FOURIER_PROJECTION_EXACT_PASS coefficients= 29268 local_lengths= 15`

The program builds each independent-set indicator directly from the graph definition, computes its complete unnormalized Walsh transform by an integer butterfly, and compares all coefficients against the derived product formula. It compares the number of zeros, extrema, and exact rational \(\ell^1\)- and \(\ell^\infty\)-projection norms after inverse Walsh transform, for the enumerated small parameters. It also evaluates selected character sums directly without using the butterfly implementation. The 15 local lengths correspond to all even peripheral clique orders from 2 to 30, with middle-two-layer Krawtchouk absolute sums checked by a separate coefficient extraction formula. Explicit direct enumeration of those local layer sums is used at peripheral orders up to 8.

All computations use exact integers or `fractions.Fraction`; there is no floating-point or timeout-based inference. Finite checks do not prove the quantified theorem. The proof is in `RESULT.md`, especially the Krawtchouk two-layer recurrence and translation-averaging argument. The theorem makes no statement about independent external validation or uniqueness of noninvariant minimum-norm projections.
