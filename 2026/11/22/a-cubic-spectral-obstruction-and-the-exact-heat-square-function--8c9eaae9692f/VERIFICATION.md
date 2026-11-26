---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1,
  "record_status": "passed"
}
---
# Verification and scope

The proof in `RESULT.md` controls all cycle lengths by exact integration, polynomial factorization and Fourier-mode orthogonality. No finite test is used as an infinite certificate. The dichotomy assumes a nonzero real or complex Hilbert target. For the zero target every input vanishes on every cycle, so the inequality always holds and the least nonnegative constant is zero.

The following finite checks can be reproduced by arithmetic in the displayed identities:

- On \(C_6\) use the two vectors \(u=(1,1/2,-1/2,-1,-1/2,1/2)\), \(v=(1,-1,1,-1,1,-1)\), with eigenvalues \(1,4\). With \(s=-1/64\) the exact counting-measure deficit is \(-20493/640000\).
- On \(C_4\) with scalar complex target, use \(u=(1,-1,1,-1)\) and \(v=(1+i,0,-1-i,0)\). Then \(q=(3,1,3,1)\) and \(c=(2,0,-2,0)\). The counting-measure deficit is \(136/81\), agreeing with \((17/81)\sum_jc_j^2\).

The original supplementary `check_cycle_square.py` (unchanged) contains symbolic polynomial and coefficient checks, and floating-point diagnostics on \(C_5\) through \(C_{500}\) and complex-valued examples on \(C_4\). Neither those finite diagnostics nor the exact sample checks determine the best constant on the failing sizes.
