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

For the generically ordered \(K_r\)-free Fraïssé limit, an injective ordered \(n\)-tuple induces on coordinate set \([n]\) a labeled \(K_r\)-free graph together with one of \(n!\) linear orders. Universality realizes every such finite ordered graph, and homogeneity says two tuples are in the same automorphism orbit exactly when their coordinate-induced ordered structures agree. Hence \(a_r(n)=n!f_r(n)\). The Erdős--Kleitman--Rothschild theorem gives \(\log_2 f_r(n)=\operatorname{ex}(n,K_r)+o(n^2)\), and Turán's theorem gives the coefficient \((r-2)/(2(r-1))\); the \(n!\) factor is \(2^{o(n^2)}\). The inversion formula for \(r\) is elementary algebra. Independent small enumeration reproduced the triangle-free counts \(1,1,2,7,41,388\), agreeing with the package verifier. No correctness defect is present.

## originality

FAIL

The final entropy formula is mechanically determined by standard prior facts. For a homogeneous relational structure, automorphism orbits on injective tuples are exactly isomorphism types of labeled induced finite structures; the profile/age literature formalizes the same orbit-versus-finite-structure correspondence. Cherlin's classification supplies the generic ordered \(K_r\)-free structures. Erdős--Kleitman--Rothschild already gives the quadratic logarithmic count of labeled \(K_r\)-free graphs, and Turán gives its coefficient. Multiplying by the \(n!\) possible linear orders and dividing by \(n^2\) leaves that coefficient unchanged. The recovery formula for \(r\) is a one-line inversion. Although no source located states the combined formula under the title 'tuple-orbit entropy,' every novelty-bearing clause is a direct corollary of these stronger established ingredients.

## value

FAIL

The entropy is a natural invariant, but in this family its exact value is obtained by attaching an \(n!\) order factor to the classical labeled \(K_r\)-free graph count and then reading off Turán density. Parameter recovery is elementary inversion. This cross-literature packaging is informative, yet it does not introduce a new structural lemma, asymptotic estimate, or classification beyond standard prior results, so it falls below the independent-value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
