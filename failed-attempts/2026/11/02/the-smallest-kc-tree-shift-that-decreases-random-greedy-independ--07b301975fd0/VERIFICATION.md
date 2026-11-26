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

The path 4–5–6 is bare, the off-path edge 6–7 becomes 4–7, and the number of leaves increases from four to five. Conditioning on the first vertex of a uniform permutation gives the stated exact generating-function recursion because the remaining order after removing its closed neighborhood is uniform. Independent exact verification instead uses i.i.d. uniform priorities and a rooted branch survival polynomial A_v(t): with the parent absent, conditional on priority u at v, its child branches are independent, so A_v(t)=1−integral_0^t product_w A_w(u) du. Summing 1−A_v(1) over root choices gives the mean. An independent rooted-child multiset generation followed by minimum code over all roots covers all unrooted types; every bare path with two nonleaf endpoints is checked in both directions, precisely the proper cases. Reproduced the means 73/15, 34/7, the two 9! histograms, and the census: tree counts 1,1,1,2,3,6,11,23,47; oriented move counts 0,0,0,2,8,26,70,186,470; strict-loss counts zero through eight and four at nine (two losses each of 1/105 and 1/420). Replay: python /workspace/branches/independent_kc.py; output /workspace/branches/independent_kc.log. The stated loss and ratio loss are −1/105 and −1/945. A clarification of the scope prose: uniform selection among unblocked surviving vertices with closed-neighborhood deletion is distributionally equivalent to the specified random order, not a different law. This does not alter the finding.

## originality

FAIL

The major claim, including its witness, exact laws, and minimum order, is covered by a distinct indexed record, e9c71afd7c39. The later catalogue date does not make it earlier work, and this review does not ascribe priority or dependence. It finds exact extant coverage, not a materially independent theorem beyond it; the supporting extension of the census to the number of oriented decreasing moves at order nine does not give a stated structural classification of these moves. The 2019/2020 primary literature does motivate the obstruction but only conjectures the contrary monotonicity.

## value

PASS

A sharp finite counterexample to an explicit conjectural strengthening of a theorem is a meaningful obstruction. Its strict sign matters, irrespective of the small magnitude: it rules out substituting actual expectation for the auxiliary monotone functional in the proposed tree-shift argument. This significance does not remove the exact indexed coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
