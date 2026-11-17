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

The statement and proof in `RESULT.md` are self-contained modulo the standard identification of \((\ell^\infty)^*\) with bounded finitely additive measures and the standard fact that compact operators carry bounded weakly null sequences to norm-null sequences.

Run `python3 checker.py` from the same directory. The expected output is `PASS: 21537 finite identities and estimates`. The checker independently forms weighted differences and product differences on 120 randomly generated finite rooted trees; compares conjugated rows, tail coefficients and phase-attaining inputs; and checks 22 cutoffs of the exponentially weighted compact example. The finite tests verify algebraic and numerical consistency only, not the universal infinite-tree assertion.

The analytical upper estimate uses finite-rank correction \(P_KA+(I-P_K)AP_K\), with exact residual norm \(E_K\). The lower estimate constructs disjoint band-supported input vectors; finite additivity and bounded total variation make them weakly null even in \(\ell^\infty\). Those statements cover every compact competitor, all locally finite infinite trees, and all strictly positive weights. Formula equality, compactness and the weighted-ray example were checked against these hypotheses. No Lean/external proof certificate or independent mathematical audit is claimed.
