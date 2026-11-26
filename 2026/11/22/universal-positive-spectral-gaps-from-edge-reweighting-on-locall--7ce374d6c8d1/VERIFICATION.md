---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Deleting the first n edges leaves at most n+1 components, so the union of their finite components is finite. Every vertex outside that union has a simple ray in its infinite component by local finiteness. Choosing for v_j the largest admissible deletion prefix among lengths at most j ensures that for fixed n, only the finite exceptional union and indices j<n can have rays using e_n. With multiplicity m_n, resistance r_n=2^(−n)/(1+m_n) is positive and has total load Σ_n m_n r_n≤1. Along each simple ray an ℓ² function tends to zero, and telescoping plus Cauchy–Schwarz bounds |f(v)|² by that ray's resistance sum times the common *total* energy; summing over starts gives the stated bound without treating the rays as edge-disjoint. The maximal weighted gradient is closed by coordinate convergence and dense by local finiteness; its form gives a selfadjoint operator bounded below by I. For a bounded above form, delta functions give c_e≤B, and finite-set indicators force |∂F|/|F|≥A/B. Conversely with maximum degree d, coarea on |f|² and Cauchy–Schwarz give the unweighted lower bound h²/(2d) and the upper bound 2d, extending by density. The signs of orientations do not affect coefficient squares and the semi-frame weights are √c_e. The argument uses counting measure and an edge sum counted once.

## originality

PASS

The bounded-degree Cheeger implications are standard; they are not a distinct originality claim. The supported contribution is unrestricted existence of finite positive edge-by-edge conductances yielding a positive counting-measure gap on every graph in scope, hence the graph-incidence case of a general lower-semi-frame question. The strongest inspected results give conditional gap bounds or propose general rescalability, not this existence statement.

## value

PASS

This resolves a natural existence question for a graph-incidence family and separates lower stability from bounded invertible frame behavior. The escaping-ray construction removes any degree bound or unweighted expansion requirement for the one-sided result; the obstruction explains exactly why the same strategy cannot produce a two-sided bound on amenable bounded-degree hosts. That distinction is useful independently of how optimal the weights are.

The dated certificate retains the supplied scientific assessment, sources and limitations.
