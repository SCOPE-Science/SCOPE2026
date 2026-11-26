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

A term occurring at least 2p-1 times must have order 2p: otherwise order-many copies already form a forbidden subsequence. It occurs exactly 2p-1 times. Normalize it to 1; zero is forbidden by itself, and p with p copies of 1 is also forbidden. The p-1 remaining terms therefore have gcd-weights 1 or 2. For a nonempty residual submultiset U of weight D<=2p-2, precisely 2p-D available copies of 1 bring its weight to 2p, and the resulting sum modulo 2p is twice the sum of a(x)=(x-d(x))/2 modulo p. This proves both directions, since dominant copies alone cannot have weight 2p. The prime-order lemma holds: in any ordering of a zero-sum-free sequence of length p-1, all p prefix sums, including the empty prefix, are distinct and exhaust C_p. Swapping unequal neighbors would change only their intermediate prefix sum, which is impossible if both sets of prefix sums exhaust C_p. This also clarifies the manuscript's compressed subset-sum argument: saturation of C_p before the last term would allow a zero sum using one remaining term, so growth cannot stop prematurely under the avoidance hypothesis. No change to the claim is needed. The nonzero common value h lifts to 2h+1 or 2h+2, with one inadmissible lift at each of the distinct h=(p-1)/2 and h=p-1. Thus there are 2+p(p-3) residual multisets per generator, of which 2+2(p-3) have one residual type and (p-2)(p-3) have two. Uniqueness of the dominant term and its common residue establishes the labelled census, including p=3 with no support-three case. Gao–Mu Theorem 1.1 makes 3p-2 the sharp avoiding length. Independent exact replay `python3 /workspace/checks/cross.py 3 5 7` enumerates all avoiding multisets at these lengths via set-valued subset DP and gets totals 4,48,180, with support counts (4,0),(24,24),(60,120); this does not prove dominance outside these finite cases.

## originality

PASS

The supported distinct claim is the exact inverse description and labelled support census in the dominant-generator regime, not the sharp threshold, its standard two-symbol witness, the prime-order inverse lemma, or an unrestricted inverse theorem. The closest primary statements contain those ingredients but do not effect the weight/sum reduction and complete this restricted classification.

## value

PASS

This natural threshold inverse question replaces a single known construction with a structural classification of every witness carrying the maximum possible generator multiplicity, in infinitely many orders. It identifies mixed-order and three-supported extremizers and gives the exact number in each support stratum. The weight-to-prime-group correspondence is the useful refinement, rather than the elementary algebra of the final count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
