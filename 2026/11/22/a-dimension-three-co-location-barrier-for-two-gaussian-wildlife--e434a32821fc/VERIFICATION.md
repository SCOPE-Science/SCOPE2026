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

For a coordinate normal of variance sigma², E exp(-k X²/(2 ell²))=(1+k s)^(-1/2); shifting the first-coordinate mean in the single-detector integral adds exp[-a²/(2 ell²(1+s))]. Multiplying the two kernels removes the cross term and contributes exp(-a²/ell²) times the k=2 product over all d coordinates. Conditional inclusion–exclusion therefore gives C_d(t)=A exp(-alpha t)-B exp(-t) with t=a²/ell², alpha=1/[2(1+s)], A=2q(1+s)^(-d/2), B=q²(1+2s)^(-d/2). The ratio of positive to negative derivative terms is (q/q_c) exp[-(1-alpha)t]; it strictly decreases. At equality q=q_c only t=0 has zero right derivative, and every t>0 strictly underperforms. For q>q_c, the unique root is a strict global maximum, including the boundary at zero, since the sign changes from positive to negative. The logarithmic derivative in s has numerator d/2-1-2s and positive denominator. Thus f_d=log q_c starts at zero and decreases strictly for d<=2, or rises and then falls strictly to -infinity for d>=3. This gives one positive crossing and the q<=1 obstruction including equality. At d=4 the exact polynomial reduces to s(s²-s-1)=0, and independent decimal bisection of (1+2s)^3-(1+s)^5 on [0.5,1] yields s_3=0.63770838850224109…. For S=2^(d/2) the expansion uniformly on [S/2,2S] is log(S/s)-(d/4+1)/s+O(d/s²). The endpoints have opposite signs for large d; at the root exponentiation gives S/s=1+(d/4+1)/s+O(d²/s²), which proves the stated correction and remainder. The frozen checker was read, not executed; the numerical root at exactly the transition has ordinary floating-point sensitivity, whereas the analytic derivative decides the equality exactly. The quadrature code is composite Simpson (not the midpoint rule despite one code comment).

## originality

PASS

The precise novelty is limited to the dimension-three onset of a nonzero all-quality co-location interval, the dimension-specific crossings and the high-dimensional expansion. The two-exponential maximization itself and the planar transition are already covered. Factoring transverse Gaussian coordinates is elementary, but the stated cutoff in physical q, its change of kind with dimension and its asymptotic correction require further analysis and are not statements of the closest source.

## value

PASS

This answers a concrete first-detection design question at the transition from a planar to a volumetric model: even perfectly responsive colocated independent devices need not benefit from being separated, and the spread needed to make separation worthwhile has a sharp cutoff. The dimension-three cutoff is pertinent to the idealized volumetric setting, and the asymptotic gives a structural severity scale rather than a new placement algorithm. This is model-level value for a conditional-independent reflected pair, not a field recommendation or an unrestricted design theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
