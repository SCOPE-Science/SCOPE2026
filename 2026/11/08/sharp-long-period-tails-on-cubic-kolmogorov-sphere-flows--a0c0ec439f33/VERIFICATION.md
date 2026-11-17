---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

PASS. Squaring coordinates gives a three-strategy antisymmetric replicator with conserved u+v+w and H=u^c v^b w^a; the positive simplex has strictly concave log H and a single interior center, so each regular level is a simple periodic orbit. The physical-time visits to the three corners have divergent parts L/(2ab), L/(2ac) and L/(2bc), from integrating log-coordinate derivatives and bounded-integral residuals, while connecting arcs stay O(1). Uniform spherical-area sampling pushes (u,v,w) to Dirichlet(1/2,1/2,1/2), so E H^{-q} is finite precisely for q<1/(2 max(a,b,c)), including divergence at equality. T= S/(2abc) log(1/H)+O(1) transfers this to the stated tail and sharp moment cutoff.

## originality

PASS

PASS best knowledge. The flow is an antisymmetric zero-sum three-strategy replicator up to physical-time normalization; conserved weighted product and qualitative periodicity are pre-existing. Benny–Jana–Sarkar identify this sphere family and its local phase portrait; Boone–Piliouras show general three-strategy zero-sum replicator periodicity. Neither inspected principal result evaluates the three vertex physical-time delay constants together with spherical area pushforward to a sharp period-tail and exponential-moment threshold.

## value

PASS

PASS. A periodic foliation can contain extraordinarily slow orbits; the parameter-dependent logarithmic period coefficient and exact exponential integrability threshold quantify the distribution of slow periods for the natural spherical measure. The first-principles physical-time and probability normalizations are substantive and survive without a universal dynamical-systems theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
