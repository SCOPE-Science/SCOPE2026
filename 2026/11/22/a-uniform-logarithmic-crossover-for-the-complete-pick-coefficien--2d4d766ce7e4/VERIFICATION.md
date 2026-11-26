---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Independently reconstructed the exact positive coefficient measure and the two asymptotic regimes. Let F=1-1/K. The Stieltjes integral for K gives a strictly positive imaginary part in the upper half-plane and positivity on the real line below 1. Thus F is a Herglotz function analytic off [1,∞). Its representing measure has density Im F(x+i0)/π for x>1 by local continuity of the boundary values. There is no atom at 1: Re K(1+iy) tends to infinity by Fatou's lemma. There is no linear term: y Im K(iy)=∫ y²t/(1+y²t²) dν(t)↑∫ dν(t)/t=∞ for the given Stieltjes weight ν, hence F(iy)/y→0. This supplies the n=1 justification as well as all higher coefficients without relying on the sketched outer-arc estimate. For x=e^u the density is x u^(α-1)/(Γ(α)|Li_α(x+i0)|²), against x^(-n-1) dx for coefficient n. The exponent after substitution is therefore -(n-1)u. Positivity is strict, and F(r)↑1 proves normalization. For fixed α<1 the singular Li term and the Laplace integral give Γ(2-α)/(Γ(α)Γ(1-α)^2), the claimed constant by reflection. In the crossover, put L=log n and H=(u^(-ε)-1)/ε, interpreted as log(1/u) at zero. The principal upper-bank expansion gives Re Li=H+O(1+u^(-ε)), uniformly for small ε, with u^(-ε)=1+εH. Thus Re Li ≥ cL on u≤n^(-1/2), for large n at any fixed S. At u=v/n and compact positive v the normalized Li tends uniformly to (e^s-1)/s (continuously 1 at s=0), and the numerator u^(-ε)/Γ(1-ε) to e^s. The scaled integrand for v≤sqrt(n) is bounded by C_S exp(-v/2)(1+v^(-1/4)); the exact imaginary part bounds the rest by an exponentially vanishing tail times log² n. Integrating yields e^s s²/(e^s-1)², including the endpoint. The reconstruction, not the frozen finite floating-point recurrence, checks the uniform quantifier. α=0 is explicitly excluded and has the different reciprocal stated in the record.

## originality

PASS

Best-of-knowledge pass for the specified uniform reciprocal-coefficient crossover and its scaling function only. The endpoint, positivity framework and fixed-parameter asymptotics are not credited as independently new. The closest checked prior covers a different statistic or a non-uniform regime.

## value

PASS

The result identifies the boundary layer between two different asymptotic regimes for a natural coefficient distribution attached to the canonical complete-Pick representation (equivalently an interarrival law). It supplies a quantitative profile for scale-dependent kernels, with an explicit normalization and a demonstrably different answer from fixed-order extrapolation. The useful new content is the entire uniform transition, not a recomputation of a fixed endpoint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
