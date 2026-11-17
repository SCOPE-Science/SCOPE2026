---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For arbitrary W, traces of Laplacian on E=(v,v) and O=(v,-v) give lambda2<=min(n ybar,2 xbar+(n-2)ybar). Scalar maximization under c*xbar+(n-1)ybar<=B/n gives threshold 2(n-1)/(n-2). Symmetric eigen-decomposition attains; equality in O trace and PSD forces E_odd eigenspace, and row-column overlap for n>=3 forces classwise-constant conductances. Universal proof is algebraic, not based on verifier output.

## originality

FAIL

Exact mathematical identity under t=c and budget-normalization B: scale earlier unit-budget allocation by B; both values, all optimizer classes, critical interval and rigidity coincide for all n>=3 and c>0. The prior theorem dominates the final claim, not just a title/parameter match.

## value

FAIL

Although weighted spectral-gap optimization is a natural question, every final quantitative conclusion including all asymmetric optimizers is identical to the published October 13 theorem; no new mathematically useful invariant remains in this package.

The dated certificate retains the supplied scientific assessment, sources and limitations.
