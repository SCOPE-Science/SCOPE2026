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

Closed neighborhoods are visible via the pair's two-flip vertex, and cannot accept an outside vertex since every geodesic from the center starts in the selected neighborhood. Their induced stars have distinct centers. Empty and singleton sets extend. For the decisive finite exclusion I inspected both frozen C++ predicates and conducted a fresh exhaustive computation, not execution of the supplied C++: `python3 /workspace/checks/q6_orbits.py` (Python 3 and NumPy; log `/workspace/checks/q6_orbits_output.txt`). The independent checker augments representatives of orbits under XOR and coordinate permutations. Deleting one vertex from any candidate, taking the orbit representative for the smaller set, and applying the same isometry to the deleted vertex shows that augmentation covers every next-size orbit. It marks all and only the normalized containing-zero images by translating by each selected origin and applying all 720 coordinate permutations. A same-cardinality colex bitmap separately confirms disjointness and full coverage of each entire normalized domain. Visibility is checked by directed reachability along edges reducing Hamming distance to the target, allowing selected endpoints but not selected interior vertices. Heredity makes all one-vertex extensions a sufficient maximality test. Weighted by normalized orbit sizes, tested totals for sizes 2–7 were 63, 1953, 39711, 595665, 7028847, 67945521; visible totals were 63, 1953, 39696, 594440, 6982332, 66836889, and maximal totals were 0, 0, 0, 0, 0, 7. The sole maximal orbit through size seven is represented by (0,1,2,4,8,16,32), with seven images containing zero. This recovers only the 64 closed neighborhoods, and does not extrapolate to higher dimensions.

## originality

PASS

The known neighborhood construction and upper bound are credited. The supported distinct claim is the matching lower bound and classification of all minimum inclusion-maximal ordinary sets in Q6. Neither known maximum-size Q6 counts nor same-value lower results for other graphs settle that claim.

## value

PASS

The six-cube is a natural member of the explicitly posed lower-visibility family, and its 64 vertices already give nearly 68 million translation-normalized candidates at the critical size. The result establishes both the exact minimum termination size of ordinary visibility extension and the whole minimum configuration type, a useful boundary case for testing general lower-bound and rigidity conjectures. It is more than a known upper bound or a maximum-number recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
