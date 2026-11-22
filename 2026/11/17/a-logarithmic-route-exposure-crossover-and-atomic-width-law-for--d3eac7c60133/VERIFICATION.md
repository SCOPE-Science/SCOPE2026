---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Every feasible unit flow on the internally edge-disjoint routes is a convex combination of route-edge incidence vectors with squared edge-coordinate Euclidean norms L and ell and zero mutual inner products. Under the isometry to the orthogonal simplex, the Gaussian projected onto H={sum y_i/sqrt(L_i)=0} has vertex scores (sqrt(L)Z-lambda,sqrt(ell)G_i-lambda)/||g_H||, so the common lambda cancels EXACTLY in width and in extremal order. The conditional probability of maximizing the long leg is integral phi(z)Phi(sqrt(L/ell)z)^m dz, and min gives a second equal disjoint event. Max_i G_i/sqrt(log m)->sqrt2 and min_i G_i/sqrt(log m)->-sqrt2; chi_m radial norm divided by sqrt(m)->1, without assumed independence. Continuous mapping yields the three regimes and critical joint indicator, with exceptional threshold sqrt(2/c) having zero boundary mass. For critical means E R_m^4=O((ell log m)^2) and E (m/||g_H||^2)^2=m^2/((m-2)(m-4)), so Cauchy–Schwarz gives uniform second moments; integration of the half normal yields 2 sqrt2 Phi(t)+2 sqrt(c)phi(t). Checked finite Gaussian exposure integral against its conditioning identity and Gaussian range projection proof from frozen RESULT.md. Exact path tree/blob and code inspected; finite Monte Carlo is not an infinite proof.

## originality

PASS

Best-of-knowledge distinction is the three-regime intrinsic Euclidean spherical width law and the exceptional normal-cone exposure indicator for one route whose length scales as ell log m; the orthogonal-simplex identification and ordinary Gaussian extrema are explicitly pre-existing ingredients.

## value

PASS

This is a motivated probabilistic geometry problem: keeping the same simplex face lattice while changing one route length creates a phase transition in a natural spherical width and a nontrivial atom identified with a vertex normal-cone exposure probability. The exact finite-angle integral and critical joint law are useful geometric invariants not implied by a combinatorial vertex list or generic Gaussian-max theorem. The calculation does not claim arbitrary network geometries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
