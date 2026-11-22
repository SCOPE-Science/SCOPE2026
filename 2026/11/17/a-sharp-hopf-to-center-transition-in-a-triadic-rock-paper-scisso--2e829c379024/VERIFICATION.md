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

The final theorem uses exactly the specified cyclic A and B1,B2,B3 pairwise/triadic payoff tensors on the probability simplex, with 1<α≤2, 0<β≤1 and b>(2α−β−1)/4 so a*=(1+4b+β−2α)/(3+2α−β)>0. The original-time orthonormal chart X=(u1−u2)/√2,Y=(u1+u2−2u3)/√6 makes the linear real part −D(a−a*)/18, D=3+2α−β, and strictly positive ω. At a=a* the exact quartic equivariant field has only z,conj(z)^2,z²conj(z),z⁴,zconj(z)^3 monomials; their full coefficients are displayed and algebraically constructed from all three matrices by inspected check_hopf.py. The nonresonant quadratic term adds a purely imaginary correction −2i|Q|²/(3ω), so the genuine real cubic coefficient is ℓ=(1+b)(1−β)/(2D). For β<1, ℓ>0 with μ<0 when a>a*, producing a unique local repelling Hopf cycle, normal-form radius²=D²(a−a*)/[9(1+b)(1−β)]+O((a−a*)²). For β=1, exact full-quartic reversibility under (X,Y)↦(−X,Y) (not merely a vanished cubic) and positive angular velocity imply fixed-line half-turn returns, hence every sufficiently small nonstationary orbit is periodic: a true nonlinear center. The nondegenerate statement is not extended to β=1.

## originality

PASS

Griffin–Wu 2023 introduced the identical well-mixed payoff tensors and Hopf crossing, describing a subcritical cycle numerically; its inspected primary model and local analysis do not give the exact all-parameter radial Lyapunov coefficient or prove the endpoint β=1 is a reversible center. Griffin–Feng–Wu 2024 computes a first Lyapunov coefficient for a distinct four-dimensional spatial travelling-wave reduction with different payoff matrices: neither its coefficient nor travelling waves imply this well-mixed two-dimensional result. Standard reversible-system theory makes the method known, not the verified endpoint identity for these coefficients. Resultary returned other reversible centers in different games, not this model. An unindexed analytic treatment remains a stated risk.

## value

PASS

A natural published higher-order RPS model has a sharp change from a generically repelling local Hopf cycle to a full annulus of neutral cycles at an admissible parameter endpoint. This mathematically distinguishes mere vanishing first Lyapunov coefficient from a genuine nonlinear center and resolves a parameter-wide bifurcation criticality question beyond prior numerical classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
