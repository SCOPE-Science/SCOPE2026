---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For the 35 vertices consisting of triples of [7], a face is a pairwise-intersecting family, i.e. Ind(KG(3,1)). The S7 action partitions the triples into cycles. Discard each orbit with an internal disjoint pair; build the incompatibility graph of remaining cycles. Each fixed simplex corresponds to an independent orbit-set, so reduced Hopf trace is -I(F_g;-1), with no missing empty-face sign. Feng (2026) supplies rational homology only in H6 rank29 and H9 rank7; seven six-subset cross-polytopal cycles supply the top signed seven-point permutation module (Feng–Wang). Thus chi6(g) = chi9(g) - I(F_g;-1). Independent reconstruction of all 15 conjugacy-class orbit graphs gave every stated trace, including chi6(identity)=29 and chi9(identity)=7; the resulting character equals S^(7)+S^(4,3)+S^(2,2,2,1). S7 rational transfer gives one invariant H6 line and no invariant H9 line, so the quotient is a rational homology S6, not proved homotopy S6. The externally published ranks remain premises, not independently derived by these finite checks.

## originality

FAIL

Decisive exact prior coverage: a published October 25, 2026 full-text theorem https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-the-full-mathfrak-s-7-homology-character-of-pairwise-intersectin--dca1fcc16e77/RESULT.md computes the identical S7 homology module H6=S^(7)+S^(4,3)+S^(2,2,2,1), the identical H9 signed permutation module, the fifteen conjugacy-class traces, and the invariant line, for the same intersecting triples on seven points. A November 8 result https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-the-full-sixth-homology-symmetry-of-pairwise-intersecting-triple--6cff67cf08ce/RESULT.md repeats H6 and even gives a uniform fixed-subset character formula. The November 17 submission has no surviving distinct new final claim; its rational quotient S6 follows directly from the previously known invariant line and rational transfer.

## value

FAIL

The full sixth-homology representation is intrinsically meaningful, but the exact 29-dimensional Specht decomposition, 15-class table, and unique invariant quotient direction were all published in the earlier Oct25/Nov8 records. Recomputing an already known exact natural invariant without a genuinely distinct mathematical consequence has no incremental scientific value as a new finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
