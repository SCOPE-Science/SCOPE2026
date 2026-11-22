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

The analytic checks reconstruct: (1) Fourier alias-class equivalence by character inversion on a finite subgroup; (2) the sharp zero-sum weighted \(\ell^1\)-to-\(\ell^2\) inequality and two-coefficient equality; (3) the cross-class orthogonality inequality and unique active class; (4) reduction of every rectangular-grid alias pair to a single axis; (5) strict concavity/convexity and the full equality list; (6) the exact ambiguity diameter; (7) the published optimized-sampling comparison under \(r>0\), \(q=2\), \(\theta=1\), \(d=1\).

Execute `python verify_alias_wiener.py` with Python 3. No third-party modules are needed. The completed deterministic finite diagnostic printed `WEIGHTED_WIENER_ALIAS_KERNEL_FINITE_CHECK_OK 9029`. Its frequency searches and random finite nullspaces do not prove statements over arbitrary infinite Fourier series; those are established by the preceding exact inequalities and absolute convergence.

No independent audit or external mathematical certification is represented by this record.
