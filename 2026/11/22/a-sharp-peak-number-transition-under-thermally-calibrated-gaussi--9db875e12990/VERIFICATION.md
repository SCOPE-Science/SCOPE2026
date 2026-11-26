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

The last-reset age A is exponential, and first reset couples any initial distributions, giving a unique stationary law. At age A the damped reset noise and subsequent OU noise have total variance V exp(−2κA)+V(1−exp(−2κA))=V; the resulting Gaussian is independent in distribution of age and sign. exp(−κA) has density a u^(a−1) on (0,1), giving the stated dimensionless convolution. For 0<a≤1 a layer-cake decomposition into centered uniforms gives a strictly negative derivative on the positive half-line after Gaussian convolution. For a>1 the derivative of the input has an interior signed power and jumps of magnitude a/2 at the endpoints. Convolving gives the stated positive prefactor times H_{a,t}(w)−1. The ratio sinh(uw)/sinh(w) strictly decreases in w for 0<u<1 by monotonicity of z coth z, and goes from u to zero. This gives exactly the claimed derivative signs at all positive positions. H_a(0)=1−1/a, H'_a(t)>0, and H_a tends to infinity as t increases, so the unique critical t exists and strictly separates the modes. At t_c the Taylor coefficient in w² is −H'_a(t_c)/6, and the positive prefactor vanishes linearly in w: the stationary density has zero second and negative fourth derivative at the center. The positive root approaches zero by monotonicity and continuity of the sign kernel; its equation expanded in w² yields w²=6(t−t_c)+o(t−t_c). Since w is dimensionless position divided by s, m²=3(s_c−s)+o(s_c−s). H_2(t)=(exp(t)−1)/(2t) gives the numerical root (independently checked). The bound H_a(t)≤(a−1)exp(t)/a proves divergence of t_c as a decreases to one; for U~Beta(a,1), E[1−U²]=2/(a+2) and E[(1−U²)²]=8/((a+2)(a+4)), giving a(H_a(t)−1)→2t−1 locally uniformly and t_c→1/2. Finite quadratures are only corroboration.

## originality

PASS

Last-reset renewal, one-dimensional Gaussian smoothing, curvature-zero mode boundaries in related models, and coefficient 3 in the analogous run-and-tumble bifurcation are established. The distinct result is the global mode classification and explicit threshold for complete equal thermal-packet resets: its compact input is the symmetric truncated power |u|^(a−1), not the compact telegraph Beta profile or an age-dependent-width point-reset law. The checked primary run-and-tumble work is an important additional comparison beyond the cited resetting papers.

## value

PASS

Thermal-width packet resetting is a natural parameter calibration that retains a diffusive bath while making the smearing exact. The result shows that rate alone is insufficient above a=1, gives the precise thermal variance at which distinct maxima disappear, and rules out further peaks globally. This matters when interpreting a reset-induced change in the stationary density, and distinguishes it from the flat transition of idealized point targets, rather than just evaluating a known moment or a generic local coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
