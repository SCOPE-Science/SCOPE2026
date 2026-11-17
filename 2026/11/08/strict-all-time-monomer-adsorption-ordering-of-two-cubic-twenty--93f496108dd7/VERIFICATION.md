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

For a candidate vertex subset S with uniform arrival order, conditioning on the earliest attempted v gives f_G(S)=1+(1/|S|)sum_{v∈S}f_G(S\N[v]) where N[v] is closed. Multiplying by |S|! gives integer DP a_G(S)=|S|!+sum_{v∈S}(|S|-1)!/|S\N[v]|! *a_G(S\N[v]); this exhausts all 2^20 masks. The average over |S|=k yields exact mu_G(k) and differences delta_k=mu_H(k)-mu_D(k). The supplied complete rational 21-entry table has delta_0..delta_4=0, delta_5=1/3876, each delta_5..delta_20>0 and delta_20=2030003/3144960. Independently reimplemented an exact integer mask recursion in C++ using 128-bit arithmetic and recomputed every mu and delta without running repository code; results matched all 21 rational table entries, including positive signs. Bernoulli-p subset sampling for independent exponential first attempts gives E[X_H(t)-X_D(t)]=sum_k binom(20,k)p^k(1-p)^(20-k)delta_k, with p=1-exp(-t): positive for each t>0, and leading coefficient binom(20,5)*delta_5=4. The inspected separate available-candidate polynomial and occupied-independent-set recursions give full terminal distributions D: {6:1/90,7:302009/336960,8:31207/336960}, H: {6:1055/6912,7:2152/7371,8:81557/207360,10:37763/232960}; their survival tails reverse order between thresholds 7 and 8. This is exhaustive finite computation on named 20-vertex graphs, not a claim for arbitrary graphs.

## originality

PASS

Resultary searches for these exact canonical generalized Petersen graphs and hard-core monomer kinetics found no earlier evaluated all-time pair comparison; related exact jamming laws concern Petersen dimers, Shrikhande/rook monomers, Frucht or other graph classes. Pippenger (1989) treats regular high-girth regimes and provides the foundational RSA model; its available abstract does not state the computed finite-pair inequality, but complete full text is inaccessible via publisher, OA, arXiv and authorized institutional route. Static independence-complex studies of the two graphs do not determine the order-weighted greedy histories. Best-of-knowledge credit applies to the complete exact Bernstein ordering and terminal crossing, not RSA or graph topology generally.

## value

PASS

A motivated exact kinetic comparison of two canonical 20-vertex cubic networks of equal order/degree, with a strict all-time sign certificate, a sharp fifth-attempt onset linked to five-cycles and full terminal law crossing. The exact 21 rational coefficients distinguish dynamics beyond degree and static independence-set counts and are independently useful fixed-graph invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
