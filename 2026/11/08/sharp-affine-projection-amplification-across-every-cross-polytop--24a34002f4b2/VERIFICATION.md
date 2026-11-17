---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Face-balanced cross-polytope skeleton sampling has support s/d and signed Dirichlet(1,...,1), covariance 2/[d(s+1)] I. Exact affine kernel 1+d(s+1)x·y/2; Beta-tail integration gives 1+(s+1)/2(1-2/[d(s+1)])^s. Convexity and positive-measure opposite-sign kernel rows force only vertices to maximize. Log derivative of g(t)=t(1-2/[dt])^(t-1) gives strict rank increase; radial disintegration derives solid endpoint and stricter volume gap; Bernoulli remainder proves uniform 1/d bound and half-step law. Independent exact-fraction checks sampled all ranks for d<=23.

## originality

PASS

Best-of-knowledge PASS. Earlier published results give cross-polytope boundary s=d and full-volume endpoints, and the 2023 numerical mesh paper gives methods, but no inspected theorem yields exact norms for each intermediate face rank and uniform half-step law. Source-specific partial-inspection limits are documented.

## value

PASS

PASS. Sampling uniform ranked faces is a natural stability interpolation between vertex observations, boundary data and solid measurements; exact all-rank constants, unique norming locations and uniform limiting half-step law are independent structural information not supplied by the known endpoint cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
