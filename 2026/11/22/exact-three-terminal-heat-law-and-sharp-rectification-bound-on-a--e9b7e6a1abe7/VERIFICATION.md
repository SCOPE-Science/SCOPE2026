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

Independently quotient the eight microstates by global spin reversal: let p₀ be the stationary mass of the aligned class and p_i the mass of the class with odd spin i. Transitions 0→i, i→0 have rates (1−t_i)/2 and (1+t_i)/2; transitions between distinct odd-spin classes have rate 1/2. Stationarity and normalization give p_i=(1−t_i p₀)/(4+t_i) and p₀=[1−Σ_i 1/(4+t_i)]/[1−Σ_i t_i/(4+t_i)]. The nonzero energy changes at bath i are +4J out of the aligned class and −4J out of its own odd-spin class. Thus Q_i=2J[(1−t_i)p₀−(1+t_i)p_i]. Symbolic rational simplification reproduces every current and correlation in the record, with C_ij=1−2(p_i+p_j); all allowed rates are positive and Δ>25. Pair coefficients are positive and antisymmetric in the contribution to the two currents. A strict hot or cold extreme has the indicated sign; at equilibrium all currents vanish. For two distinct fixed other parameters the numerator is an affine decreasing function of t_i and changes sign exactly once between them. In the two placements, cancellation in the total hot currents gives the stated R. For D=8−xy−2y, 4/3−R=[8(1−y)+x(6−y)]/(3D); D stays positive and bounded on the closed parameter triangle. This proves the strict upper bound and that approaching equality requires x→0 and y→1; R>1 follows from y>x.

## originality

PASS

The distinct supported result is the explicit three-terminal current and sharp hot-placement ratio for the equal-bond triangle. Existing Glauber moment methods, positivity of total entropy production, and the general idea of one-versus-two-spin rectification are not credited as new. The strongest distinct catalogue comparison is the same-date three-spin path; its quantified law is for a missing edge and does not determine the triangle's law. Closest inspected exact chain work assumes bipartite alternating sites on an even ring.

## value

PASS

A symmetric closed triangle is a minimal three-terminal spin network, and its extra bond is precisely what separates it from the open three-spin rectifier. The positive pair law and unique balance setting quantify which reservoirs supply, absorb, or exchange zero net heat, beyond stationarity alone. The sharp bath-placement ratio supplies a fully normalized finite-model benchmark for rectification and its attainable limit, with no thermodynamic-limit claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
