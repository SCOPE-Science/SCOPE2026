---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For all integer 2<=p<q, the vertex law includes all partial permutation matrices, including empty matching; the exact cell probabilities are a=F_(p-1,q-1)/F_(p,q), b=F_(p-2,q-2)/F_(p,q) for disjoint row/column cells, and zero for mutually conflicting cells. Its covariance operator is a I+b(J_p-I_p)⊗(J_q-I_q)-a² J_p⊗J_q. Tensoring constant and contrast subspaces yields four dimensions and eigenvalues λ0=a+(p-1)(q-1)b-pqa², λR=a-(q-1)b, λC=a-(p-1)b, λI=a+b. Strict positive first gap follows from p simple positive zeros of L_p^(q-p), which factor the matching size PGF into distinct Bernoulli factors; λR−λ0=Σ(π_i−πbar)²/[q(p−1)]>0. Other gaps (q-p)b and pb are explicit, λ0>0 by varied matching size. Fixed p, q→∞ matching-size deficit gives λ0=q^-2+O_p(q^-3), λI=q^-1+O_p(q^-2), condition ratio q+O_p(1). Independently counted small boards and exact rational eigenvalues; finite checks are not the universal Laguerre proof.

## originality

PASS

PASS for genuinely rectangular 2<=p<q four distinct covariance modes, strict Laguerre root-spread gap, and anisotropy. A complete published same-measure result for square boards p=q has only three distinct modes (row/column degeneracy) and does not determine strictly ordered four modes on unequal rectangles. Heuer–Striker supplies vertices and polytope faces but not covariance; Heilmann–Lieb and classical Laguerre zeros support a lemma, not the targeted covariance. Historical monomer-dimer/rook-correlation literature remains potential priority risk.

## value

PASS

Uniform-vertex inertia is a natural geometric statistic of complete bipartite matching polytopes. Unequal board sides split the square row/column degeneracy into four rigorously ordered scales and create a precise fixed-short-side condition number, a motivated structural classification rather than renaming known spectra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
