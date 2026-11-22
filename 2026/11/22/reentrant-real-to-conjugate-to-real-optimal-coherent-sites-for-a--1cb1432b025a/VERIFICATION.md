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

## Reproduction instructions
Use Python 3's standard library and run `python3 check.py` in this directory. The script has no network or optional-library dependencies. Its finite diagnostic tests reconstruct the two positive roots of \(a^3-2a^2-7a+4\) and real stationary points by bisection, evaluate predicted global sites, compare to fixed polar grids, and independently test the exact square-completion identity at off-axis points. A successful run prints `PASS` and a count of 118354. This is numerical corroboration, not an infinite mathematical certificate.

## Analytic checks and limits
The proof derives all nonreal stationary sites from \(\overline w f_a(w)=f_a'(w)\), establishes global optimality by an exact angular-square identity, and excludes real-axis competitors using strict log concavity and the resultant \(-a(a+4)(a^3-2a^2-7a+4)\). The square-completion identity and resultant were also checked by symbolic expansion/elimination during the mathematical review. Threshold values are approximate; the exact specifications are the positive roots of the cubic. A separate independent audit has not been performed.
