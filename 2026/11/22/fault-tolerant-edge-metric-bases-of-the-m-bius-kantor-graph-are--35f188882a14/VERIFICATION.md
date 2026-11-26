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

Using the explicitly stipulated two-witness criterion (equivalently requiring a resolving set that still resolves after each deletion), I reconstructed GP(8,3) from its modular adjacency rule, found distances by Floyd–Warshall, and exhaustively tested the complementary indistinguishability sets; replay with python3 /workspace/evidence/1-exhaustive.py. Every resolving 3-set is excluded; 368 resolving 4-sets exist. There are no robust 4-sets, hence no smaller robust sets by monotonicity, and the 16 robust 5-sets are exactly the 16 distinct radius-three shells, all with cardinality five. In each of the two eight-set shore classes every set meets exactly one other in two vertices and all six others in three; the 64 cross-shore pairs are disjoint. Adjacency is 5 minus the overlap being at most k, giving precisely the five claimed graphs and threshold. The empty set is excluded by ordinary resolution and by the operative two-witness definition; a deletion-only formula should not be read as admitting the empty set vacuously. The finite exhaustive proof is for this one labelled graph. Inspected RESULT.md, VERIFICATION.md, check_py.py and check_cpp.cpp without running the uploaded programs.

## originality

PASS

No inspected prior statement covers the minimum one-failure EDGE resolving-set family on GP(8,3) or its intrinsic shell/exchange geometry. The ordinary dimension and its 368 bases are contextual, and there is a separate indexed record giving exactly those ordinary results. Neither the lower-bound principle nor the ordinary invariant is credited as new.

## value

PASS

On a canonical cubic symmetric graph, the exact optimum family is a graph-intrinsic orbit of distance shells rather than a bare feasible count. It answers whether optimal resilient placements can be moved between the shores without replacing every landmark, and exactly classifies the intermediate budgets. This is meaningful at the finite graph scale without a wider family claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
