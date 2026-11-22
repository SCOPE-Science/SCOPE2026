---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

On every strict-input-order chamber, median T_n selects one coordinate per output row; because T_n(x+c1)=T_nx+c1, exact global quotient Lipschitz norm equals maximum ||Q_n S Q_n|| across finitely many selector matrices. Each column j is selected by at most three output windows (n≥4), giving universal √3 upper bound. At n=2 the three-entry multiset repeats one neighbor twice, so median swaps the two values and quotient norm is 1; at n=3 every window is the whole triple, output is constant and centered norm 0. At n=4 and 5 the original exact rational certificate enumerates 24 and 120 strict orders (12 and 60 selectors) and verifies 2Q_n−Q_nSᵀQ_nSQ_n PSD for every selector; independently enumerated all 12/60 and computed maximal squared norms exactly 2, with source strict-chamber witnesses. At n≥6 explicit distinct base points produce selector column1 at outputs0..2 and column4 at outputs3..5; h=e1−e4 has mean zero, ||h||²=2, ||S h||²=6 and output mean zero, so √3 attained by nearby same-chamber input pairs. Independent selector enumeration at n=6 yields maximal squared norm 3; finite numerical eigenvalues corroborate source exact rational PSD only, not the infinite n≥6 witness proof.

## originality

PASS

PASS best of knowledge: prior same-operator calculations use uncentered ℓp and cyclic total variation, while the mean-centered Euclidean quotient has a genuine five-site defect (√2 versus ordinary √3) and first achieves √3 at six sites. The prior full articles were inspected for norms and quantifiers.

## value

PASS

The sharp dimension at which a natural nonlinear local median filter saturates centered Hilbert perturbation amplification is a concrete sensitivity threshold. The first centering defect at five sites distinguishes quotient geometry from ordinary ℓ2 and BV, a mathematically motivated stability invariant with exact all-n answer. This is neither a renaming nor a known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
