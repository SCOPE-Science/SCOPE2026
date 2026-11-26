---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For a=rζ the rational function h_a=b_a−a belongs to VMOA_0, and harmonic reproduction and unit boundary modulus give Φ_h(z)=1−|b_a(z)|². Its maximum is one at z=a. A common Lebesgue point of f and |f|² makes Φ_f vanish nontangentially. After rotating ζ to 1, write z=(r−w)/(1−rw) with |w|<=s<1. Then |1−z|=(1−r)|1+w|/|1−rw| and 1−|z|²=(1−r²)(1−|w|²)/|1−rw|². Their quotient bounds |1−z|/(1−|z|) by a constant depending only on s, while |1−z|=O_s(1−r), so the entire large-variance disk is in a fixed cone and Φ_f is uniformly small there. Minkowski bounds the mixed norm by |t|+o(1) inside the disk and by ||f||_G+|t|sqrt(1−s²) outside; take r→1 before s→1. For the matching lower bounds, at each fixed interior z the perturbation variance tends to zero and one may then take the supremum of the remaining Φ_f; at the moving z=a the perturbation has variance one and Φ_f(a)→0. This proves the law without assuming norm attainment. For every point of each closed ball, t=±1 gives a unit perturbation with both endpoint norms tending to one. The covariance spot check in RESULT.md follows by summing the geometric series for h_r(z)=−(1−r²)z/(1−rz); it is not the proof. Replay is symbolic via RESULT.md Steps 1–5; no code or mesh data is required.

## originality

FAIL

There is full statement-level coverage in a separately indexed document: Resultary 85e69ab98cd8 states the identical exact Garsia-norm law, for the same rational Blaschke perturbations at a full-measure set of common boundary points and all fixed complex scalars, and the identical four-space conclusion. Its proof uses the same localization and two lower-bound tests. The companion 14b6949994e9 also gives the complete strong-extremity conclusion. The directory dates are later than the frozen record's; this verdict records demonstrable equivalent coverage at review, not that either document had earlier priority or is independent of the frozen work. No distinct mathematical remainder of the frozen finding is established against this comparison.

## value

PASS

As mathematics, a norm-specific geometric limit with explicit admissible norm-one perturbations supplies a useful mechanism for the empty strong-extremity classification. It distinguishes strong from ordinary extremity even in VMO, where all sphere points are ordinary extreme. The substantive question and mechanism are valuable; the originality failure is the exact equivalent coverage, not lack of mathematical motivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
