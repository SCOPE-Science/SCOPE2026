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

Translate an admissible block to contain zero. Its remaining vertices are an intersecting family of 2-subsets, since disjoint pairs differ in four positions. The weight-four neighbor of zero missing coordinate i sees 1+deg(i) members, so every degree is even. An intersecting nonempty family is a star or the full triangle: once edges ab and ac are present, a member missing a must be bc, after which no other member can occur. A nonempty star has a leaf. The triangle with zero is exactly the two-fixed-coordinate cylinder after translation. The five generator steps restrict to the two fixed coordinates as the three nonzero profiles with multiplicities 3,1,1, proving sufficiency with open neighborhoods. Compatible fixed bits on at most four positions always extend; hence disjoint cylinders either conflict on the same pair or have opposite bits on a shared coordinate. This yields 60+240 disjoint pairs and 40+240+80 disjoint triples (one support, a doubled support, or a triangle of supports). Four cylinders with one support give ten covers; two distinct supports must each supply both cylinders in their opposite shared-coordinate halves, giving sixty. Three triangle supports leave two complementary patterns on the three active coordinates, and both values occur also on each outside coordinate by parity, so the four remaining vertices cannot form a cylinder. Four distinct pairwise-intersecting supports would give a star with impossible mutually opposite bits. Each q-cylinder family has 16-3q blocks, so the complete spectrum is 70z^4+360z^7+300z^10+40z^13+z^16, and the four fixed named colors give 70 times 4! assignments. An independent scan of 65,535 nonempty subsets and least-vertex partition counting reproduced the block sizes, spectrum and optimal split.

## originality

PASS

The strongest objective-specific earlier material inspected mentions the Clebsch graph but does not supply the cylinder-block classification or the polynomial. The strongest indexed structural analogue uses triangles in the two-subset Kneser graph, whose vertices and neighborhood constraints differ. The geometrically related sixteen-point examples do not give an equivalent census. This is a best-of-knowledge decision, not a claim of priority.

## value

PASS

The Clebsch graph is a canonical triangle-free graph and the strong odd condition is motivated independently of this computation. The exact classification is stronger than the optimal chromatic number: it gives all allowable blocks, the complete spectrum, and the possible coordinate geometry of extremizers. These supply exact test data for graph-coloring bounds and distinguish optimal colorings that the minimum alone cannot distinguish.

The dated certificate retains the supplied scientific assessment, sources and limitations.
