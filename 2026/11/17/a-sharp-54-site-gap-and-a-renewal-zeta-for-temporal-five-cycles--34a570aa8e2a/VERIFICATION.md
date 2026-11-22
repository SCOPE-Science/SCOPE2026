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

The Rule22 one-step condition is sum of three adjacent binary bits exactly 1. The inspected t=5 space-time transfer construction is a finite 1024-state graph. A separate implementation generated 1023 edges and SCC sizes 1,2,16,16,16,16,16; one 16-state block has 18 edges, exactly three simple cycles lengths 11,12,13 with 9 vertices common. The inspected checker verifies the remaining four blocks exhaustively; common-vertex intersection precludes disjoint-cycle determinant products, so each block det(I-zB)=1-z^11-z^12-z^13, and -zQ'/Q gives its trace. The one-/two-cycle contributions cancel against F_n fixed points and division by the five temporal phases yields the orbit generating function for every n, not a finite extrapolation. The positive coefficient support is the semigroup <11,12,13>; its union intervals [11k,13k] have last missing values 53,54, conductor 55. An independent direct bit-state enumeration is finite corroboration, not the all-n proof.

## originality

PASS

Best-of-knowledge search and actual statement comparisons across Resultary, primary accessible literature and the assigned proof found no earlier statement implying this specific final claim. Named comparisons below identify exact overlap and inapplicability; failure to find a source is not itself novelty proof, and material uninspected is retained as risk.

## value

PASS

Primitive temporal-five cycles of Rule22 are a natural previously studied attractor class. The full all-circumference rational orbit series, sharp conductor 55, exclusion of n=54 and growth constant classify a meaningful infinite family beyond known isolated periodic patterns; the invariant cannot be inferred from the finite n<=20 atlas or temporal-four census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
