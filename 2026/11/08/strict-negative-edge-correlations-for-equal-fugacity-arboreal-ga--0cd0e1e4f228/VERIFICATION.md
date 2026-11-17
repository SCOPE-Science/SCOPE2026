---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Each right vertex has zero/one/two/three chosen neighbors of three left vertices. Cycles prohibit degree-three together with another right degree>=2, equal paired two-neighbor supports, and three different degree-two supports. Hence only zero, one, or two compatible high-degree right vertices; yields Z_n=A^(n-2)[A^2+nBA+3n(n-1)b^4] with A=1+3b,B=3b^2+b^3. One-edge E and two-edge Q_R,Q_L,Q_D enumerations were inspected and the Rayleigh differences Δ=E^2-QZ independently recomputed exactly using polynomial arithmetic: Δ_R=b^4(n-1)P_R, Δ_L=2b^4P_L, Δ_D=b^4P_D. Each P has 15 strictly positive integer monomials in b and h=n-1; thus all three covariances strictly negative for b>0, n>=5. Independent source checker includes exact finite enumeration, but the general claim follows from symbolic identities and combinatorial classification, not a finite run.

## originality

PASS

The 2026 complete-bipartite negative-correlation result covers uniform forests at beta=1 for arbitrary m,n, and Wagner covers small K3,4 with heterogeneous weights; the candidate proves every positive common beta on an unbounded family K3n. The new fugacity-continuum statement is not a corollary of the isolated beta=1 theorem. A general Rayleigh theorem could imply it, but one was not established by the inspected highly relevant primary results.

## value

PASS

The arboreal-gas negative dependence problem is actively studied and is not generally trivial. An infinite complete-bipartite family with a proof uniform over all common positive fugacities is a mathematically motivated parametric extension of the known β=1 graph theorem and can inform further Rayleigh investigations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
