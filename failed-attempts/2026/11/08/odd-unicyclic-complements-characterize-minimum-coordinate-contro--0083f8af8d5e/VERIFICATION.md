---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For KG(n,2), the unsigned K_n incidence B gives BB^T=(n-2)I+J and A=J_N+I-B^TB. Hence the Laplacian eigenspaces are constants, ker B of dimension N-n, and B^T(1^perp) of dimension n-1, with distinct eigenvalues for n>=5. PBH demands at least N-n independent dedicated controls. At equality, complement U of n unactuated pair-vertices has invertible unsigned incidence exactly when every component is odd unicyclic (e=v and nonbipartite). The remaining eigenspace imposes zero-sum signs on the controlled graph; only at n=6 and balanced K_3,3 can an obstruction survive, giving ten two-triangle complements. Species/EGF rooted-tree attachments to odd cycles yields exp((artanh T-T)/2) minus ten at n=6. Independently enumerating all 252 candidate complements n=5 gives 162 valid; all 5005 n=6 candidates give 2520 valid and 10 excluded two-triangle cases. Finite checks corroborate, analytic proof is all n.

## originality

FAIL

A Nov 2 2026 published theorem for triangular graph J(n,2)=L(K_n) states the identical minimum N-n, exactly the same odd-unicyclic complement characterization, exactly the n=6 two-triangle exception and identical EGF. Since J(n,2) and KG(n,2) are complement graphs on the same pair-vertex set and L_J+L_KG=N I-J, their nonconstant eigenspaces are identical, with Laplacian eigenvalues transformed λ→N-λ. Hence the PBH coordinate controllability condition for each S is precisely equivalent. The present statement and every exact count are covered, despite different graph titles and eigenvalue names.

## value

FAIL

Odd-unicyclic exact controllability is a motivated natural invariant and the proof is correct, but the complete fixed-Laplacian placement classification and every presented number are an immediate graph-complement restatement of an already published 2026 theorem. No new independent mathematical contribution survives; routine spectral recoding is insufficient for V.

The dated certificate retains the supplied scientific assessment, sources and limitations.
