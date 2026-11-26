---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Distance differences are exactly products of the sign matrix with ternary difference vectors, every such vector being realized by two binary vertices. At most three independent rows allow at most four distinct column patterns modulo negation, so five columns force a ternary dependency. Any resolving four-row matrix has rank four by the same projection argument. Signed maximal minors span its kernel; every order-four sign determinant is divisible by eight and bounded by sixteen. Thus failure to have a minor of magnitude sixteen would give a nonzero ternary null vector. Such a minor is a Hadamard block. The remaining column has even inner products with its columns, sum of their squares sixteen and none of magnitude four (that would duplicate a column up to sign). They are all ±2, so the primitive null vector has one magnitude two and four magnitudes one. Its sign pattern and distinguished coordinate recover the complementary root and hole; the only sign rows orthogonal to it are the eight asserted representatives. One must use one from each pair, and each transversal has a nonsingular J₄−2I₄ block up to signs, so it resolves. Across distinct roots the distance between suitable representatives is one or two; a common projected neighbor would require their difference to be e_i+e_j modulo complementation. Hence at distance one there is no shared antipodal pair, and at distance two there are precisely two, not enough for one exchange. At a fixed root a move either flips a representative in one of four pairs or fills the hole with either sign while opening a new hole. The overlap lower bound is attained by correcting a differing hole first, then sign flips; shell j is binomial(4,j)+8·binomial(3,j−1). The independent direct replay `python3 audit-evidence/q5.py` tested all 4,960 triples and 35,960 four-sets by distance vectors, confirmed the exact generated family, and used all-source BFS to reproduce all components, edge counts, distance formula and shells. No smaller set resolves since it would extend to a resolving triple. The supplied artifacts were inspected, not used as independent output.

## originality

FAIL

There is demonstrable equivalent coverage in a distinct catalogued Q₅ result: the entire optimizer and unrestricted exchange theorem appears there, and that result additionally treats a stricter move rule not part of the frozen claim. The comparison establishes redundancy of mathematical content in the inspected corpus, not that the later-dated catalogue entry had priority or that either proof derives from the other. The inspected earlier literature alone does not establish exact coverage.

## value

FAIL

For an otherwise natural and useful optimizer-reconfiguration question, the exact signed census, inability to change roots and full distance law are all covered in another distinct result. The alternative algebraic proof provides corroboration but no additional scientific claim beyond that coverage, and the slide-frozen extension in that other result cannot be credited to this frozen one.

The dated certificate retains the supplied scientific assessment, sources and limitations.
