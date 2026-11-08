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

# Verification of prescribed rank-one idempotent sum fibers

The theorem is proved in RESULT.md without computation. The executable files test a finite set of parameter values using independent direct enumeration of every rank-one idempotent as an outer product and every ordered pair; the predicted fibers are recomputed from each actual target, not from the observed distribution.

Run with Python 3 (no third-party packages):

```sh
python verification/idempotent_rankone_fiber_check.py
python verification/idempotent_rankone_gf4_check.py
```

Reference outputs are embedded as verification/idempotent_rankone_fiber_check.txt and verification/idempotent_rankone_gf4_check.txt. No random sampling is used. The prime-field checker exhausts every target for \((n,q)=(2,2),(2,3),(2,5),(2,7),(3,2),(3,3),(4,2)\), i.e. \(16+81+625+2401+512+19683+65536=88854\) distinct tested targets across parameter settings, and checks all ordered pairs of rank-one idempotents in those settings. The GF(4) checker separately exhausts all \(256\) targets and \(400\) ordered pairs in \(M_2(\mathbb F_4)\) with explicit irreducible-polynomial arithmetic. Thus \(89110\) target cases were explicitly compared across eight settings.

Each checker asserts equality of predicted and observed multiplicities for every target in its finite scope; it terminates on a mismatch. No external solver or original result is imported into the checker. The prime-field predictor computes the image restriction and its invariant/eigenvalue-one lines; the GF(4) predictor uses a separate Jordan-eigenvalue observation for traceless \(2\)-by-\(2\) matrices in characteristic two. This cross-method distinction reduces common-mode errors.

**Limits.** The programs do not enumerate every dimension or field; they do not prove the theorem over all prime powers. The general proof uses no enumeration beyond basic finite projective-line incidence. No independent audit or external certification has been performed.
