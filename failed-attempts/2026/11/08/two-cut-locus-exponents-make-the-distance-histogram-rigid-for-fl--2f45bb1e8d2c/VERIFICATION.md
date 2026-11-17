---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Deck transformations have translation displacements a and shortest glide vertical displacement b; first disk overlaps at r=min(a,b)/2. The local mean quotient-disk deficit is an ordinary lens Lambda_r(a) plus a periodized glide-lens integral. Expand Lambda near tangency to obtain (8sqrt(a)/3)epsilon^(3/2), integrate over transverse O(sqrt(epsilon)) glide offsets to obtain (2pi b/a)epsilon^2. Thus the first exponent distinguishes which is shorter. Independent mpmath high-precision quadrature at three aspect ratios verified leading ratios 1.001748418, 1.002499221 and 1.001827548 at epsilon=.005. Pointwise asymptotics, not uniform near degenerate aspect ratio.

## originality

FAIL

FAIL due to strong direct prior coverage. The October 25 complete theorem on EXACT SAME metric quotient, pair sampling, and parameters gives a complete CDF, its small-radius area identity and a cubic terminal-distance tail that already reconstructs ordered translation L and glide H for every aspect ratio. Another November 8 published result supplies an explicit full all-radius CDF integral for the same K_(a,b), from which the local first-transition lens exponents follow by elementary expansion. The submitted restatement that full distribution determines ordered parameters is strictly implied. The local exponents are a routine local consequence of already published full distribution and not a surviving independent priority claim on their own.

## value

FAIL

FAIL as presented: reconstructing ordered periods from distance CDF and full distributional geometry are already proved with a stronger global formula; extracting the first tangency exponent via standard two-disk lens asymptotics does not establish a motivated additional unknown invariant beyond previously exact full CDF. Correctness of the local calculation is acknowledged, but correctness alone cannot rescue already covered principal claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
