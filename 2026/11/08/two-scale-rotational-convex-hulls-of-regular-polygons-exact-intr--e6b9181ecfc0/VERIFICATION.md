---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The inner regular n-gon lies in the outer one iff r cos(π/n−θ)≤cos(π/n), because this is the maximal inner support against each outer edge normal. Strict inequality in the other direction exposes exactly n alternating inner vertices; all n unit-radius vertices remain exposed. The shoelace formula yields area n sin(b) max(c,r cos(b−θ)), and cyclic chord lengths yield the two-case perimeter. On the active angle interval, the squared derivative difference factorizes into 2(cos θ−cos(2b−θ))(rT−c)(T−rc)>0, proving both volumes strictly increasing toward θ=b. Direct expansion at r=c gives a linear area excess and quadratic perimeter excess. Independently computed SciPy convex hulls for 585 n,r,θ cases (n=3..11) and agreed for both area and perimeter. Numeric checks corroborate, not substitute for analytic proof.

## originality

PASS

PASS for the complete exact area/perimeter profiles, strict coupled angular maximizer, and unequal linear versus quadratic onset orders. The contact/vertex-survival criterion alone is covered by the earlier more general gcd-resolved polygon hull-vertex theorem and must not be credited as new. Earlier translative hull and concentric overlap results do not contain the new intrinsic-volume formulas.

## value

PASS

The combined full two-parameter area/perimeter phase diagram for a natural concentric convex-hull construction, strict simultaneous optimizers and distinct onset exponents supply a motivated structural geometric classification beyond known contact counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
