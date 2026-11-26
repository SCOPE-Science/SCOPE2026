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

The frozen mathematics and narrowed replacement agree on the slide and mixed-metric counts. From the five XOR generators, translations and generator permutations give exactly the two required minimum-placement orbits: translate a path center to zero; for an independent triple translate one member to zero and use transitivity on intersecting pairs of two-generator index sets. Explicit move legality is one replacement, with XOR in {1,2,4,8,15} for a slide. A separate exhaustive reproduction from the graph and propagation rule (branches/46c08968-162c-4d3f-8745-85ceb2dcef1a/independent_check.py) confirms the 320 minima and all 51,040 unordered distance pairs. It gives 1,120 slide edges, degrees 9 and 5, slide eccentricity six, a single last-layer placement equal to the antineighborhood, and the reported 12,560/27,520/10,800/160 gap counts. Each of the 160 involution pairs is disjoint and has jump distance three. The explicit six-slide and three-jump witnesses are legal. This is exhaustive for the given graph, not an assertion for other folded cubes or the complement. The supplied code was inspected, not executed; the repair leaves its inputs and numerical claims unchanged.

## originality

PASS

PASS only for the delivered narrowed theorem in repairs/4/RESULT.md and repairs/4/SLOGAN.txt. Originality of the frozen attribution fails: the minimum-placement classification and jump metric are covered by 99315adae8ca, and the very same antineighborhood involution on that family is covered by c9e2c260f397. These are distinct records, not the frozen record itself; their common catalogue date does not establish an ordering. The replacement explicitly credits both and claims the slide graph, unique slide-antipode interpretation and exact slide-versus-jump gaps only.

## value

PASS

The repaired theorem ties the unique most remote optimum under local sensor movement to a directly defined feature of initial observability: the three initially missed vertices. It quantifies exactly when local moves impose three extra steps and shows a meaningful structural contrast between the two symmetry orbits, despite jump regularity. This is useful independently of the known seed census and is a motivated fixed-graph metric benchmark, not a claim about physical grid movement or a wider family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
