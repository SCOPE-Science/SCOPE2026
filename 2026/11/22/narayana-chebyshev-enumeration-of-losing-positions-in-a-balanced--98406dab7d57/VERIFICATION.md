---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

A balanced nonempty word can delete itself, and the empty word loses. For nonzero balance each endpoint deletion preserves the total balance and cuts the itinerary exactly at an interior A (prefix) or B (suffix), leaving that symbol as an endpoint. In the interior game, a Dyck word leaves only nonzero-sum interiors when cut at a legal symbol. In a non-Dyck word, cutting the suffix from the first negative step leaves a Dyck prefix; if there is no negative step, cutting through the last unmatched A leaves a Dyck suffix. Induction applies to the strictly length-decreasing game. Excursions between consecutive visits to {0,h} concatenate uniquely: an exterior return has the primitive Catalan series P, while the interior return and crossing entries follow by cofactors of I-zA on the length-(h-1) path, whose determinant is D_(h-1). For h=1 these reduce to no interior return and a single-step crossing. An interior with j pairs and k peaks contributes k A-to-B changes and k-1 reverse changes; the outer endpoints add two equal-boundary pairs when j>0. This gives the stated Narayana weights and the lone v_h term when j=0. Letter exchange handles negative balance; finite valuation makes all sums coefficientwise valid. On b^i a^j b, j=i+1 is balanced, j<=i produces a first interior B, and j>=i+2 gives itinerary AABB. The slice has infinitely many distinct left residuals, establishing nonregularity.

## originality

PASS

Credit the Dyck criterion for the reduced interior game to the known Timber analysis. The distinct result is the reduction from balanced end deletions of the original word, together with the exact original-length census across all endpoint heights. The general framework, the known reduced P-language, and the related same-day records do not supply that weighted census in the passages examined.

## value

PASS

Counting every losing binary starting word by actual length is a natural complement to the known reduced-game criterion. The itinerary eradicates most original letter positions, so its known Dyck classification does not say how often positions occur. The exact height-resolved factors recover this lost length information and allow computation at every length without solving the complete game tree. Nonregularity also distinguishes this rule from games governed by a finite-state losing language.

The dated certificate retains the supplied scientific assessment, sources and limitations.
