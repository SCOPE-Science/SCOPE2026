---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Residue fibers \(C_a\) all have size \(s\), and distinct \(x\in C_a,y\in C_b\) are adjacent exactly when \(a+b\ne0\) in the residue field. In characteristic two each fiber is independent and all distinct fibers are completely joined, so the ordinary and total formulas reduce to the known complete-multipartite support counts. In odd characteristic, \(C_0\) is independent, each nonzero \(C_a\) is a clique, opposite fibers \(C_a,C_{-a}\) have no cross edges, and every other pair is completely joined. Every set meeting at least two fibers dominates; total domination fails exactly for a set supported on one nonzero opposite pair when one selected side has size one, yielding the displayed correction term. The reconstruction from \(D\) by the highest coefficient differing from \((1+x)^N\) correctly separates characteristic two from odd characteristic and recovers \(s\) and \(q=N/s\).

## originality

FAIL

The final formulas are routine specializations of prior general graph-polynomial theorems once the standard residue-fiber structure of local unit graphs is recognized. A local unit graph is an \(H\)-join over the residue classes: the base graph has \(a\sim b\) exactly when \(a+b\ne0\), and the fiber graph is empty in residue characteristic two, while in odd characteristic it is empty at \(a=0\) and complete at \(a\ne0\). Subramanian--Selvakumar already characterize all total dominating sets and give the total-domination polynomial for arbitrary \(H\)-join graphs; Selvakumar--Manikandan--Murugan do the same for ordinary domination in the more general \(H\)-generalized-join setting. The characteristic-two ordinary and total formulas are even written explicitly in those papers for complete multipartite graphs. The submitted residue-parity formulas follow by direct substitution/support enumeration, and the reconstruction statement is then a short coefficient inspection. Under the rule that stronger prior coverage and direct corollaries count as covered, the final claim does not clear originality.

## value

FAIL

The residue-fiber observation is standard, the all-set counting is supplied by general H-join polynomial theorems, and the reconstruction is a short coefficient read-off. Under the stated value rule requiring a motivated non-implied exact fact, this is a routine specialization rather than a substantive new invariant or structural lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
