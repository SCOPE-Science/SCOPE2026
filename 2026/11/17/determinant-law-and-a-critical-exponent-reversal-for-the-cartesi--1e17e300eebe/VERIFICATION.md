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

Run `python3 verify.py` in the directory containing `verify.py`. The checker uses only the Python standard library. It must print successful exact-rational and numerical checks, with no exceptions.

The proof does not depend on the output of this checker. Directly verify that every traceless Hermitian two-by-two matrix has square equal to half its squared trace times the identity; expand the rotated real part to get mean \(F^2/4\) and cosine amplitude \(|\det T|/2\). Check \(0\le\rho\le1\) from the two singular values. Then integrate the powers for the exact formula; strict convexity/concavity of the scalar power gives all \(p\)-dependent inequalities and equality classes. For \(p=4\), independent expansion gives \(\omega_{\mathrm{Cart},4}(T)^4=F^4/16+|\det T|^2/8\).

The checker verifies rational matrix angular moments for integer-even exponents and supports the invariant angular formula numerically at odd exponents. It does not certify all real \(p\), historical novelty, or an independent external review.
