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

Scaling s by sqrt(K_s K_i) leaves the objective multiplied by the positive constant mu_max alpha. With z=d^2, the sum of the dimensionless responses is 2[mB-(alpha+m)z]/[(B+z)^2-(alpha+2m)^2 z]. Differentiating gives the stated quadratic sign test, whose endpoint at z=m^2 is strictly negative (the concentrated allocation has derivative f'(2m)-f'(0)<0). If P(0)<=0, convexity forces P<0 on (0,m^2], even exactly at criticality. If P(0)>0 the quadratic has one crossing in (0,m^2) and another past m^2. Its discriminant gives the smaller root as stated. The critical cubic increases from a negative value past sqrt(3) to infinity, and implicit differentiation of this root gives the asserted onset. Independently, m^2-d_*^2=[(alpha+2m)sqrt(B)-m]/(alpha+m) is asymptotic to 2m at fixed alpha, so d_*/m tends to 1 and m-d_* tends to 1. A separate bounded SymPy replay verified the derivative, discriminant, onset, high-load expansion and alpha=1,m=3 example, including 7.53068755883% gain.

## originality

PASS

The bounded comparison supports the distinct all-positive-alpha Haldane allocation law, not priority for substrate inhibition or for symmetry breaking in separable allocation problems generally. Strong same-day structural analogues treat mathematically different objectives and do not give the Haldane critical cubic, explicit pair, and onset. Primary full-text access limitations are recorded below.

## value

PASS

The response peaks at load 1, but the optimal allocation stays homogeneous up to a strictly larger critical mean. The exact law distinguishes inhibition from useful heterogeneity, rules out concentration in one unit, identifies all maximizing allocations, and quantifies onset and retained response. This is a meaningful benchmark for the stated static kinetic model, not a reactor operating prescription.

The dated certificate retains the supplied scientific assessment, sources and limitations.
