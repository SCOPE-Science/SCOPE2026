---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The theorem in RESULT.md lines 3–46 is correct for the intrinsic sum metric over the continuous product of positive-length circles. On each circle, the half-turn sends the distance s to ell/2−s, including s=0 and s=ell/2. Summing proves ρ(τx,a)=D−ρ(x,a). Substituting y=τx converts the maximum of the nearer distances to D minus the minimum of the farther distances, with a,b unchanged. In the latter problem, the triangle inequality gives lower bound ρ(a,b)/2, and a product of shortest-arc midpoints attains it simultaneously in every coordinate, including ties and coincident sites. Applying τ to this midpoint recovers the frozen proof's longer-arc witness. Maximizing ρ(a,b) is exactly saturating each coordinate's cap ell_j/2; this proves the antipodal rigidity and subtracting D/2 proves the excess formula. This checks all dimensions and cases without sampling. Inspected VERIFICATION.md and verification/checker.py lines 7–47, including the nested support missed by the batch excerpt; the 32,000 exact rational assertions are source-recorded only, not rerun, and test identities at specified pairs and points rather than an exhaustive continuum check.

## originality

PASS

Best-of-knowledge pass only for absence of an identified equivalent published statement or stronger stated result giving the entire continuous prescribed-pair profile. Unit-square optimization is a verified same-day overlap and not distinct content; the classical antipodal metric condition and two-point midpoint radius are not novel. The exact frozen profile is a mechanically obtainable deduction from those facts, which is decisive for value below. No priority claim is made for the observation or inference of within-day precedence.

## value

FAIL

The facility problem is natural and the formula correct, but the proposed new contribution adds no nonmechanical exact fact: half-turn complementation is immediate coordinate by coordinate and simply rewrites the quantity as D minus the textbook enclosing radius of a two-point set in a geodesic space. That enclosing radius is forced by the triangle inequality and attained at any shortest-path midpoint. Once this equivalence is written down, no product-torus optimization, exceptional aspect or boundary regime remains to classify. Saturation of each coordinate gives rigidity and subtraction gives the excess formula verbatim from that automatic identity. The asserted useful comparison of arbitrary sites is exactly this routine deduction, not a further geometric constraint or outcome. Reject on that scientific basis, not on an access failure or on proof length alone. There is no independently valuable remainder in the frozen claim that can be rescued by narrower wording.

The dated certificate retains the supplied scientific assessment, sources and limitations.
