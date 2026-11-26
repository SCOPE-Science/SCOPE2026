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

The explicit graphs have diameter two. A tied distance ordering is determined by all pairwise comparison signs and is tested at all 16 vertices, not only exterior ones. An independent certificate (workspace branches/b27ad439-4cea-4abd-b145-0a7ff4896b6c/pairmask_check.py, run with Python 3) intersected, over every pair of locations, the families of detector masks containing a distinguishing detector pair. It recovered both 17-coefficient arrays over all 65,536 masks per graph. Independent traversal gave 1728 vertices and 22176 edges for Shrikhande, and 2112 vertices and 30624 edges for rook, with both connected and every eccentricity five. An additional obstruction-mask calculation confirmed the four maximal-failure counts for each graph. The description of the rook witness in RESULT.md line 62 has a nonmaterial wording slip: for two selected rows, the indistinguishable vertices are in the same column in the two unselected rows (and transpose for selected columns). The two traces both consist of the two selected squares in that column; the exterior signatures coincide. In fact only adjacent exterior pairs with identical traces can collide at size eight or greater; the common equal-adjacency mask has size eight for adjacent pairs and six for nonadjacent pairs, while unequal flat traces and detector–exterior collisions can only occur at smaller sizes. The C++ file prints radius, diameter and eccentricities rather than asserting them; the frozen Python checker does assert them and the independent calculation supplies the check. The Bernoulli substitution preserves the exact coefficient difference and clears denominators to the strictly positive expression stated. No uploaded program was executed.

## originality

PASS

The observation predicate is known. The supported distinct claim is the exact all-cardinality centroidal enumerators and optimal exchange censuses for this pair, together with the resulting all-p reliability comparison. The strongest prior same-object record overlaps in minimum size and exchange radius/diameter but uses a different observational predicate and produces different base and edge families. No inspected result supplies or implies the claimed centroidal census.

## value

PASS

This is a natural all-cardinality detector invariant on the canonical nonisomorphic pair with identical strongly regular parameters. The exact difference gives strict success-probability dominance at every nontrivial Bernoulli density, and the obstruction and exchange results answer distinct worst-case and reconfiguration questions. These conclusions are specific to the two graphs, not a general strongly regular graph theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
