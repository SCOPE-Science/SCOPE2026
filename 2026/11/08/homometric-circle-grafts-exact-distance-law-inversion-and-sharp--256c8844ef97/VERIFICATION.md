---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Partition two independently arclength-uniform sample points among circle/circle, circle/tree, same attached rooted tree, and distinct attached trees, accounting for both orientations. This yields exact L² Laplace formula C² Q_s+2Cmτ Q_s U_s+mτ² V_s+2τ² U_s² Σ_{i<j}exp(-s δ_C(a_i,a_j)) with L=C+mτ, Q_s=2(1-exp(-sC/2))/(sC), U_s>0. Division by U_s² reconstructs finite exponential mixture and its multiset of shorter-arc sites, proving the complete iff. For m<=3, the three circular pair distances reconstruct unordered cyclic gaps: either all gaps<=C/2 (sum recovered distances=C) or one gap>C/2, in which case two small distances sum to the third and missing large gap=C-third; equal-boundary handled. For m=4, A={0,1,3,4}, B={0,1,2,5} on C=8 have equal shorter-pair hist (1,1,2,3,3,4), unequal cyclic-gap multisets (1,1,2,4) vs (1,1,3,3). Independently verified grids of circumference 4..16 have no 3-site collisions, while analytic argument treats all C>0 and arbitrary finite rooted T.

## originality

PASS

The circular four-site homometric set itself is classical and Mémoli–Needham give general weighted-circle autocorrelation and metric-measure inverse questions. The claim survives only as the exact converse Laplace inversion for *identical rooted-tree attachments* at fixed (C,T,m), and its all-tree sharp m<=3 rigidity vs m=4 collision. The highly relevant Mémoli–Needham full primary paper was inaccessible in this execution, so no categorical whole-paper absence is claimed; its general partition ideas are closely related and an equivalent specialization is a serious residual risk. The accessible statement snippets/abstract do not decisively show a dominating theorem.

## value

PASS

The theorem supplies a natural complete classification of what the entire intrinsic two-point distance law can and cannot recover for a nontrivial continuous family of unicyclic metric graphs, with an exact constructive invariant and minimal rigidity threshold. It is considerably more informative than observing another known homometric pair. Uniform validity for every positive rooted-tree geometry gives independent inverse-geometry value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
