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

Two equality tests on one vertex cannot both be positive. In each part with at least two tests, one can choose their labels to force two names in that part: choose both positive for different names, or opposite signs for the same name. These conditions can be imposed simultaneously. With disjoint palettes across all r nonempty parts this budgets at most q−r such parts, proving the sorted-size bound. For q>r, test all vertices in the s largest parts and one elsewhere, with a common distinct target name per part. Reserve targets of positives, then assign one remaining name per part with negatives. Each such slot forbids at most one remaining name, distinct across constrained slots; any two jointly accept all remaining names. Thus Hall applies when at least two names remain. When one name remains all r targets have already been reserved and the remaining name is unrestricted. For q=r, colourings are permutations of the part names; r positives followed by reversing just one desired answer is impossible on r tested parts, and a support of r−1 distinct targets works by the identical matching argument with one unconstrained part. The q≥2r full-support bound is sufficient, not necessarily the earliest saturation when parts are singletons. Online, an all-positive branch cannot repeat a vertex, giving depth ≤6 on the octahedron. Six q=3 concepts allow depth at most 2. Independent exact replay of every binary equality split (only empty/too-small branches pruned) on 96 q=4 concepts confirms depth 4 and rules out depth 5 in 1,983 memoized states. An independent hand check: after fixing the first positive answer, only a test in another part can split the 24 surviving concepts with at least eight on each side. Its eight-concept positive child can split 4–4 only by testing the third part; the following four-concept child is a single colouring plus its three one-vertex flips at the untested vertices, with no 2–2 query split. At q=5 the 63-node certificate was checked as data and all 64 distinct proper leaf colourings satisfy their full paths. At q≥6 the static full support gives depth 6. Replay: /workspace/branches/9df1d117-e522-44d7-b354-ed56696bbd49/independent_online_replay.py. The frozen builder/verifier were inspected, not executed.

## originality

PASS

The r=2 slice and the existence of static-versus-online gaps for some proper colouring classes are already covered. The identified new content is the all-part-size palette formula beyond two parts and the one-palette octahedral transition, not the bipartite ranks or the general feasibility of a graph-colouring gap. The searches do not establish absolute priority.

## value

PASS

The formula explains the exact cost of adding a fully testable part, including irregular part sizes, rather than counting one small graph. The octahedron is a natural symmetric three-part contrast with the bipartite equality phenomenon: for the same graph and observations, five names suffice adaptively to test at full vertex depth while any fixed support misses at least one vertex, and neither neighboring palette regime has that gap. No general online classification or global minimality is needed to make that exact cutoff meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
