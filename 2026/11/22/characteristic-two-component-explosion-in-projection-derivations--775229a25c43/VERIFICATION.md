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

# Verification and reproducibility

The package contains `verify_rectangular_derivations.py`, runnable with Python 3 and its standard library. It constructs the defining multiplication from the \(e,B,C,C\otimes B\) basis, tests the original Leibniz equation on each ordered basis pair, evaluates \(D^2=D\) directly, computes ranks by finite-field Gaussian elimination, and compares rank histograms with separately enumerated projection pairs. Exact exhaustive normal-form tests use \((m,n,p)=(2,2,2),(2,2,3),(2,2,5),(2,3,2),(3,2,2)\). The additional binary \((m,n)=(2,2)\) test independently enumerates every one of the \(65,536\) linear maps on the four-dimensional algebra, including maps not supplied by the normal form, and finds exactly \(16\) derivations of which \(9\) are idempotent.

The executable verifies only these prime-field finite instances. The arbitrary-field structural theorem, extension-field counts, and geometric components rest on the full algebraic proof in `RESULT.md`; no infinite certification is inferred from the computational tests. The classification has received the documented self-review, but independent audit was not performed.
