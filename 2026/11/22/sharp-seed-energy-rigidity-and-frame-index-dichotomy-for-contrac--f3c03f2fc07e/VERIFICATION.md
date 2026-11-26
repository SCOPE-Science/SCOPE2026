---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Re-audited repairs/3/RESULT.md. Frozen RESULT.md line 37 incorrectly suggests E_N need not be monotone. Writing R_N=P_(N+1)^(-2), the exact decrement is E_N−E_(N+1)=A x_(N+1)(R_N−1)≥0, now stated and proved. In the repaired claim the diagonal Stein relation gives the partial-trace lower bound s_M+Σ_(n<M)x_n s_n; summing initial diagonals is exactly seed energy by nonnegative summation. Strong stability of W* gives the tight defect construction, even for infinite trace. At finite equality the β-ratios are at most one and their limits with summable q_k give lim s_n=A and s_n=A where x_n>0. At zero-deficit indices the sequence cannot decrease before the next pinned value or the limit A, so all s_n=A; positivity then forces S=AI. Rank and the positive-product Riesz orbit establish the cardinality assertions. The repaired booster has diagonal A up to N and A/P_k² thereafter, and the exact energy formula and limit remain unchanged. Frozen checker.py is only a finite exact diagnostic; the proof and decrement calculation are the replay path, without executing the supplied script.

## originality

PASS

For the corrected finding, credit the known Parseval defect-rank index, canonical shift defect seeds, and one-generator positive-product and strict-contraction index cases. The distinct claim is the sharp budget over arbitrary seed families, finite-energy equality rigidity, the explicit nonincreasing finite-seed approximation, and the extension by the budget to all zero-product shifts.

## value

PASS

The result separates two useful design budgets: one seed may suffice while every energy-minimizing family needs infinitely many, and norm-one shifts may still rule out all finite acquisition families. The sharp energy and explicit near-minimizers quantify that distinction, including boundary examples. The corrected monotonicity supplies an exact improvement guarantee as the truncated defect family is enlarged.

The dated certificate retains the supplied scientific assessment, sources and limitations.
