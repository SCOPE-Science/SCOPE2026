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

For uniform length-n Motzkin excursions, the first-return equation M=1+wzM+z²(M+v-1)M correctly marks each H and each adjacent UD peak; ground horizontals are separated by F=M/[1-(u-1)wzM]. Differentiating yields exact six moment series M, R=zM², P=z²M/sqrt((1-3z)(1+z)), RP=2z³M²/sqrt(Delta), H=zM/sqrt(Delta), RH=zM²+2z²M²/sqrt(Delta). Singularity transfer at unique dominant 1/3 through second relative correction cancels order n and order 1 in Cov(R,P), leaving -1/n+O(n^-2), while Cov(R,H)=2+O(n^-1). Independently enumerated all paths of lengths 0..11 and checked definitions; n>=5 exact computed RP covariance is negative. The supplied symbolic finite checker has the full transfer coefficient table; infinite asymptotics rely on formal singularity analysis, not the finite test.

## originality

PASS

Exact second-order negative cross-covariance between height-zero horizontals and global adjacent UD peaks is not supplied by inspected marginal/height-weight results; the horizontal–horizontal comparison is substantially prior and treated as context.

## value

PASS

Boundary–bulk covariance between ground-level horizontal steps and strict local UD peaks is a natural dependence statistic on uniform Motzkin excursions. The cancellation of leading n and constant terms leaves a sharp negative -1/n interaction, contrasted with a positive limit 2 for global horizontal counts. The exact coefficient is a meaningful second-order benchmark, not a routine one-statistic mean or arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
