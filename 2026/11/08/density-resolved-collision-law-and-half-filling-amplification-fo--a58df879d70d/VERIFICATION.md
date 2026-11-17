---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The Rule-184 local map f(a,b,c)=(1-b)a+bc conserves particle count on cyclic words. A 16-state paired de Bruijn matrix T(z) enforces equality of two outputs at each site; closed walks correspond bijectively to ordered input pairs with weight z^{|x|}. Independent exact SymPy reconstruction confirmed det(tI-T)=t^10(t²+z)(t⁴-(1+z)t³-z t²+z(z+1)t-2z²). Hence the formal log determinant identity proves all-length ∑C_n(z)u^n=-u∂_u log D(u,z). At z=1 the largest simple eigenvalue λ=1/2+sqrt(5/4+sqrt3) uniquely dominates, yielding C_n(1)~λ^n. Independently verified the proposed 12-state principal directed component has strictly positive adjacency sixth power, and unit-weight and z-weight loops break all nonzero-frequency phase periodicity. Implicit differentiation of the quartic gives density mean 1/2, variance σ²=(λ²−1)/(4(2λ−1)(λ²−λ−1))>0; ordinary analytic Perron saddle yields C_{n,n/2}~λ^n/sqrt(2πnσ²), and Stirling on binomial(n,n/2)^2 produces sqrt(πn/(8σ²))(λ/4)^n. Independent direct output-fiber enumeration for n=3,...,9 matched palindromic coefficients: C_4=[1,4,18,4,1], C_6=[1,6,27,56,27,6,1], C_8=[1,8,44,136,234,136,44,8,1]. Finite tests do not prove asymptotics.

## originality

PASS

PASS best knowledge, qualified by inaccessible 2004 close primary chapter. Earlier Rule-184 exact works classify current, flow, block preimages, time-to-relaxation, image sets or maximal predecessor fibers; none of the read complete texts yields this global density-resolved one-step second moment and half-filling local-limit prefactor. Earlier Rule-4 collision moments are for a different map. The 2004 Rule-184 de Bruijn chapter is plausible and inaccessible in full, so the assessment does not declare it non-covering.

## value

PASS

Conserved-density output-fiber squared multiplicities are a canonical information-loss and order-two Rényi statistic of deterministic traffic CA. The exact two-variable rational series resolves every microcanonical sector; the sharp sqrt(n) amplification distinguishes half-filled and unrestricted independent input ensembles. This exact structural transfer computation goes beyond a known finite table or long-time traffic-flow rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
