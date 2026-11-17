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

Reconstructed R,L and M=RLR for two explicit primitive RLR cycles. Exact sympy multiplication verifies detM=1, M^TQM=Q, detQ=3(3η−1)(4η²−9η+3)/(4η⁴)>0 on 1/3<η<(9−√33)/8. The dual Q norm computes all 3 itinerary strips and their sharp minimum radius; 6πr²/sqrt(detQ) yields the stated area, with positive radicand in the open window and sqrt vanishing at endpoints. IMPORTANT SOURCE-PROSE CORRECTION: the sentence claiming same-phase vertical projections merely meet is false (their centers differ by η/3 and each radius is η/3). The disks nevertheless are disjoint by the independent exact Q-distance inequality (η/3)^2 Q_22−4r²=(η−1)(3η³−8η²+5η−1)/(η(3η²−7η+3))>0: η<5/12 gives 3η³−8η²+5η−1<−27η²/4+5η−1<0. Other phases cannot overlap by distinct branch itineraries. This independently closes the proof gap using source equations without altering the final claim. Five exact rational interior parameter checks corroborate but do not prove the interval inequality.

## originality

PASS

Best-of-knowledge: earlier full primary work discovers the toral family and its elliptic three-cycles; it does not determine the explicit maximal centered Q-ellipse in the RLR affine itinerary cell or exact six-disk area. No exact prior coverage found in the specific different-map Resultary comparison.

## value

PASS

A quantitative, sharp and explicitly invariant area lower bound within a natural class is valuable for nonuniformly hyperbolic area-preserving maps, with an exact parameter-window endpoint law. It is not falsely presented as the full island area.

The dated certificate retains the supplied scientific assessment, sources and limitations.
