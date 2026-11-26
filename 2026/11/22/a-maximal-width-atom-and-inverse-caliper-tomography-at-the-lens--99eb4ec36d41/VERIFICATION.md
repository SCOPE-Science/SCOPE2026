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

With x=|U1|, the support of the intersection in each oriented direction is attained at an admissible disk support point, or else at a circle intersection: an interior point of just one smooth boundary arc can be a maximizer only at that disk's support point. The disk-admissibility tests are x≤−b or x≥a on the positive side and x≥b for the small-disk opposite support. The opposite large-disk support is impossible. The chord height identities give a≥|b|, hence the four branches in Eq. (1); a=b only for equal radii, and the zero-length cases and inclusive joins agree. The middle branch derivative is −rb−Hx/sqrt(1−x²), negative in the open branch and zero at its left end for b≤0. Thus the only plateau is at 2r for b<0 and the arcsine law of x gives its probability and linear onset. Solving the monotone middle branch selects the stated square-root inverse; the lower and upper inverse branches agree at their junctions. At the low end the exact linear support stage yields (6). At the high end the decrease is Hx²+O(x⁴) for b>0, (r/2)x²+O(x⁴) at b=0, and r³(x+b)²/(2H²)+O((x+b)³) just off the left plateau when b<0. Multiplying the inverse expansion there by the x-density 2r/(πH) gives (8), treating the atom separately. The lower-tail coefficient fixes d and m then fixes R+r; a positive atom yields 2r=M, otherwise 2H=M and the two-circle triangle area identity determines (R−r)² uniquely. This includes b=0 and R=r and excludes tangencies/containment. A separate bounded replay directly evaluated supports in 720 directions in each of six cases and checked joins, inversion, endpoint coefficients and recovery. Replay: /workspace/branches/d5c1bc79-7240-45dd-82d3-4f48d6d500d4/lens_replay.py. The numerical comparisons corroborate but do not prove the laws.

## originality

PASS

Classical circle geometry and equal-radius support formulas are known. The distinct theorem is the full angular-width law across unequal-radius regimes, especially its maximal atom, singular transition and recovery of the radii and distance from the unlabeled law.

## value

PASS

The full law separates an angular interval of diametral directions from an isolated maximizer; it proves how the maximal atom appears and how its continuous upper tail changes at the boundary. More than a standard calculation of a width or its mean, the lower-edge behavior and atom test reconstruct all intrinsic lens parameters up to radius exchange and rigid motion from unlabelled data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
