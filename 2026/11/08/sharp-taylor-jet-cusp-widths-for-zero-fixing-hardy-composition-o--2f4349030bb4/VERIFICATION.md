---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Direct Szego-kernel normalization yields b_phi=(1-r^2)/(1-r^2 h(w)) with h=phi(w)/w, h(0)=a. Schwarz–Pick with |a|<1 gives a strict upper bound |b|<1 away from the origin (including r approaching 1), so all near-tip values have w->0. The real denominator expansion is 1-Re b=(1-a)r^2+o(r^2), while Im b=r^(m+1) Im(c exp(i(m-1)theta))+o(r^(m+1)), uniformly on circles. Every exact vertical section has r^2~epsilon/(1-a); fixed angles attaining ±|c| and the radial intermediate value theorem yield both endpoint limits. Compactness of a small preimage disk gives attained extrema. An independent small-angle numerical bisection for a=.25, c=.15, m=3 approached the predicted normalized width; that finite test is corroborative, not proof.

## originality

PASS

Best-of-knowledge new portion is the sharp transverse-section coefficient for nonzero real linear multiplier a, not the a=0 specialization. A published 2026-11-01 result already gives the entire a=0 cusp-section law and inverse jet invariant; the 2026 Bourdon–Le–Thompson theorem is qualitative for general symbols. Thus the original all-real-a statement has a genuinely broader tangent-parameter range than the exact earlier theorem, with the special case expressly credited. This is not absolute priority confirmation.

## value

PASS

The first nonlinear Taylor jet produces a natural local, unparameterized Berezin-range invariant: the exponent identifies the first nonlinear order and the coefficient recovers normalized magnitude. Extending the exact a=0 cusp law to nonzero real multipliers changes radial depth and yields a useful parameter-sensitive classification; it is more than merely rephrasing the known qualitative cusp.

The dated certificate retains the supplied scientific assessment, sources and limitations.
