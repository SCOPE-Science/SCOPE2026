---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The 2026 primary source proves for arbitrary real normed spaces that locally finite tilability is equivalent to admitting an equivalent norm that is both \(K\)-polyhedral and LFC. Restrict such a norm to a linear subspace \(Y\). Every finite-dimensional \(E\subseteq Y\) is also a finite-dimensional subspace of \(X\), so the restricted unit-ball section is the same polytope. LFC is inherited by intersecting the witnessing neighborhood with \(Y\) and restricting the finitely many continuous functionals. Equivalent-norm constants also restrict unchanged. Applying the same characterization to \(Y\) proves the statement without completeness or closedness assumptions.

## originality

FAIL

The full 2026 source was inspected through Theorem 4.6 and its surrounding definitions. That theorem already states, for arbitrary normed spaces, an if-and-only-if characterization by an equivalent \(K\)-polyhedral LFC norm. Both defining properties are immediately hereditary to linear subspaces by restriction. Consequently the audited theorem is a direct corollary of the published characterization, even though the source does not spell out the corollary in the inspected pages. Under the owner rule that corollaries are covered without matching wording, this is decisive prior coverage. The older Fonf result also already makes the separable Banach special case implicit.

## value

FAIL

Heredity is a natural closure property, but here its proof is completely automatic from the newly published iff characterization: restrict the norm, observe the two defining properties persist, and reapply the theorem. Under the common value bar this is a routine corollary rather than an independently substantive structural lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
