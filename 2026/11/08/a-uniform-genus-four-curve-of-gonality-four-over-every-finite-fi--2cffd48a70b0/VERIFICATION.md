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
# Verification

The exact attached scripts `verify_resultants.py` and `verify_boundary.py` were executed with Python 3 and SymPy. Both printed `PASS`.

`verify_resultants.py` reconstructs the two integer double resultants, checks their gcd is \(338688\), and establishes unit Gröbner ideals in characteristics \(2,3,7\), respectively using the indicated equations. The calculations are exact over integers and prime fields, and the proof uses them only for the absence of affine geometric singularities.

`verify_boundary.py` verifies both projective boundary equations, symmetry, and the marked point. For nonspecial primes, nonvanishing of at least one integer resultant modulo the prime gives the needed affine smoothness. The remaining arguments use adjunction, canonical linear series, Frobenius descent, and Riemann--Roch.

Limitations: the scripts do not replace those standard geometric arguments, do not classify isomorphism classes or point counts, and do not provide an independent mathematical audit.
