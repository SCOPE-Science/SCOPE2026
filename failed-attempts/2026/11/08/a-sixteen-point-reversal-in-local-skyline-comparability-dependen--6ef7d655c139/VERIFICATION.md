---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For n>=3 planar iid uniform points, conditioning on point 1 being maximal gives a_n=E[I1 J12]=int int(1-u)(1-v)(1-uv)^(n-2)du dv; E I1=H_n/n and E J12=1/2 imply s_n=((n+3)H_n-4n)/[2n(n-1)]. The suffix-rank independent uniform inversion code gives Cov(M,C)=-(n-H_n)/2. The exchangeable index-incidence relation yields t_n=[3n-(n+2)H_n]/[n(n-1)(n-2)]. The strictly increasing forward differences of (n+3)H_n-4n after n15 with exact F15<0<F16 prove the unique sign switch at 16; G_n=(n+2)H_n-3n is positive for n>=3, making disjoint covariance negative. The product inequality prod(1+x_i)>2-prod(1-x_i) in d>=2 supplies strict all-d disjoint negativity. Independently checked exact rational s,t,total and signs n=3..100. This is a valid proof of its bounded domain; finite arithmetic only corroborates the all-n inequalities.

## originality

FAIL

Full-text earlier 2026-11-02 Resultary result gives, on the IDENTICAL iid uniform cube with identical comparability convention, the individual marked expectations U=E I1, V=E(I1 D12), W=E(I1 D23), with D directed domination, as explicit all-n/all-d finite sums and integrals. Since I1 D21=0, the submitted s_n=V_{n,2}-2^(1-2)U_{n,2} and t_n=2W_{n,2}-2^(1-2)U_{n,2}; its total covariance is explicitly given at d=2 in the same prior paper. All principal exact covariance formulas are specializations of the earlier stronger marked-moment theorem. The integer-16 sign threshold is an elementary harmonic inequality after this specialization; the higher-d negative sign follows with an additional one-line product inequality. Novel wording does not overcome this statement implication.

## value

PASS

The marked-versus-disjoint covariance sign reversal at an exact natural integer threshold n=16, while the global covariance stays negative, is a motivated probabilistic dependence phenomenon and an interesting sharp boundary. The all-d disjoint suppression inequality adds structural interpretation. It has scientific interpretive value as a result, but mathematical usefulness does not establish its originality when its exact moment content follows from a stronger prior computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
