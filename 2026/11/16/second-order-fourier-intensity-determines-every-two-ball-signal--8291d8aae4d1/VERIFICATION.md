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

For additive f=1_{B(c1,r1)}+1_{B(c2,r2)} in d>=2 with radii positive and known unit component density, I(0)=(V1+V2)^2 and -Hess I(0)/(2I(0)) equals the covariance of the normalized mixture. The law of total covariance yields Sigma=aI_d+(V1 V2/S²) vv^T, a=(V1r1²+V2r2²)/[S(d+2)]. A nonzero transverse direction makes min eigenvalue exactly a for d>=2; the separation and unoriented displacement eigenspace follow from the rank-one gap. For q=1+2/d>1, t^q+(S-t)^q strictly monotone on (0,S/2), so the first two scalar observations determine an unordered pair of positive volumes, including equal radii. The spectral gap and leading eigenvector then determine centers up to translation/reflection, including coincident centers. First-order intensity jet vanishes by evenness and order-zero data only fix S, proving minimal order two. Recomputed exact d=2 radii 1,2 and separation 5: covariance eigenvalues 17/20 and 97/20. Open-ball boundary measure zero, and overlaps are additive sums not union indicators. No noisy-data stability claimed.

## originality

PASS

A covariance decomposition is a standard ingredient, but the precise sharp minimal second-order phaseless identification of both radii and relative vector for all additive two-ball signals in every d>=2 is not established by the inspected 1D union-of-interval study or general phase retrieval survey abstracts. The significant same-topic Xia/Xu source could not be read in full (authorized Oxford VPN disconnected); this source is named as a priority risk rather than automatically failing O. Best-of-knowledge PASS, not a claim of certified historical uniqueness.

## value

PASS

Recovering a geometric two-component signal from only intensity's value and Hessian, rather than all frequencies, is a sharp finite-measurement inverse result on a natural object class. The full positive-radius, overlap, and coincident-center boundary treatment and minimum-jet obstruction make this a useful identifiability theorem, even though its proof uses simple covariance algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
