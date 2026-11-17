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

With independent coordinate picks, D=sum 1_{N_i>0} and H=sum 1_{N_i odd}; the parity character identities E(-1)^{N_i}=(1-2/n)^t and E(-1)^{N_i+N_j}=(1-4/n)^t yield exact marginal variances; conditioning N_i=0 gives the cross-covariance np/2[1+(n-1)b-na]. Since 1-2/n is a strict convex mixture of 1 and 1-2/(n-1), strict Jensen for t≥2 proves positivity. Taylor expansions at t/n→c produce the stated positive variance limits and rho(c); at t=Θ(nlogn), a=p²[1+O(t/n²)], b=a[1+O(t/n²)], and covariance~np/2 with variances~np,n/4, so correlation~sqrt(p) and exponent −β/2. Independent enumeration of flip sequences n=3,t=2; n=4,t=3; n=5,t=4; n=7,t=5 reproduces five exact moments.

## originality

PASS

The finite cross-covariance is a corollary of a prior richness/frequency formula and its positivity follows Jensen; both are explicitly treated as antecedents. The new result is the normalized exploration-displacement correlation function and logarithmic polynomial-decay exponent across two finite equal-box scales, not found in inspected more general infinite-urn processes.

## value

PASS

Exploration diversity and parity displacement are two canonical observables of the same hypercube walk. The exact two-scale normalized dependence law identifies when the walk progressively loses linear correlation with the set of explored axes, a natural statistic for random walks/occupancy; beyond the known numerator it needs fresh variance and uniform asymptotics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
