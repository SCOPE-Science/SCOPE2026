---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS. The source iterate formula yields d_k=sum_{j<k}e_j-(k-1)e_k, orthogonal for k!=l with squared lengths k(k-1). The resulting right-simplex coordinate halfspaces give exact inradius r=[sum_{k=2}^n1/sqrt(k(k-1))+sqrt((n-1)/n)]^{-1}, with all facets tangent; its all-vertex sphere has radius squared n(n^2-1)/12. The source exact positive tail weights and inactive-distance inequalities give the claimed minimum-enclosing radius and triangular contact condition for all n. The original checker uses rational tests up to n=100; separate independent checks gave correct inradius clearances n=3..15 and algebraic tail threshold. This verifies mathematics, not originality.

## originality

FAIL

FAIL for the final submitted conjunction. The 2023 stack-sorting paper Corollary 3.9 supplies the exact iterate coordinates. The 2025 same-object paper Ake–Lewis–Louie–Vindas-Meléndez Lemma 4.4 computes EVERY successive Euclidean altitude sqrt(i(i+1)), by the explicit nested hyperplanes; these altitudes equal the lengths of the canonical origin-to-vertex edge vectors, implying the alleged new perpendicularity and edge spectrum. More decisively, the PUBLIC full general theorem “Weighted terminal simplices have a sorted active-set formula for their minimum enclosing sphere” already determines the entire minimum ball and positive contacts for conv{-a 1,b_i e_i}, a>0; letting a down to 0 covers this right axis simplex. Setting b_i^2=i(i+1) makes its mu_p=(p-2)/sum b_i^-2 equal n(m-1)(p-2)/p, with exactly the same tail/triangular threshold and contact formulas. Thus the key touted sharp minimum-sphere discovery is a mathematical corollary, not merely same-looking parameters. The remaining inradius follows by standard facet clearances from already implicit orthogonal edge data, with no materially distinct original structural lemma.

## value

FAIL

FAIL for the original submitted novelty/value claim. Its principal triangular minimum-ball contact classification is an already-covered specialization of the full weighted terminal simplex active-set theorem. The orthogonality is already implicit in the 2025 nested-altitude proof, and the remaining exact inradius and all-vertex sphere are direct textbook right-simplex clearance/midpoint calculations once the published iterate coordinates and altitudes are substituted. No additional motivated unresolved invariant, independent structural result, or reason that this mechanical restatement is needed beyond those prior results was established. Correctness and reproducibility do not by themselves establish V.

The dated certificate retains the supplied scientific assessment, sources and limitations.
