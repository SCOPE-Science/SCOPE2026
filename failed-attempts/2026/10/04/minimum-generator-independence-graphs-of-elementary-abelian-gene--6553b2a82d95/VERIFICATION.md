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

For \(G=V\rtimes\langle s\rangle\) with inversion, a generating set containing reflections \(bs\) generates precisely the span of its translations together with the differences of reflection labels, semidirect the first reflection. This gives \(d(G)=t+1\). Two translations extend to a minimum generating set exactly when linearly independent; a nonzero translation and a reflection always extend; and two distinct reflections always extend because their product gives a nonzero translation. The resulting join decomposition and degree formulas follow directly, as does the element-order divisibility statement.

## originality

FAIL

A current published Resultary theorem gives the minimum-size independence graph for every generalized dihedral group \(\operatorname{Dih}(A)\) with finite abelian odd-order kernel \(A\) and \(d(A)\ge2\), with adjacency governed by ranks in the Sylow Frattini quotients and closed degree formulas, and proves Lucchini's degree divisibility for the entire family. The audited elementary-abelian group \(A=\mathbb F_p^t\) is a direct special case. Its linear-independence criterion, clique/multipartite decomposition, and displayed degrees are therefore covered by that broader published classification.

## value

FAIL

The elementary-abelian formulas are clean and useful examples, but once the full odd generalized-dihedral classification is already published they are a routine specialization of a stronger result. They no longer constitute an independently needed structural gap under the common value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
