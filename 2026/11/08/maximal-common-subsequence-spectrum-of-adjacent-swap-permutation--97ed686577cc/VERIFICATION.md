---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For a distinct-letter permutation order R, greedy scattered embedding in R^k is equivalent to at most k−1 weak descents of the word; an insertion cannot lower a descent count. An inclusion-maximal common subsequence saturates descent budgets for both orders P=AxyB and Q=AyxB, since otherwise a feasible additional letter can be inserted. The two almost-identical linear orders determine a no-free-insertion transition graph: permissible maximal words concatenate r forced A, B blocks separated by nonempty alternating x/y segments. Each reset consumes one descent in each order and internal xy and yx transitions consume the remaining exactly k−r each. Then lengths are 2k+(q−3)r, r=1..k, and the coefficient enumerator comes from H=(2+u+v)/(1−uv) for alternating segments. Diagonal extraction of (2+u+v)/(1−uv(3+u+v)) yields central binomial binom(2k,k). Independent exhaustive distinct-subsequence intersection and single-insertion maximality for q=4, P=0123, Q=0213, k=1..3 found total MCS 2,6,20 with length histograms {3:2}, {5:2,6:4}, {7:2,8:10,9:8}. These do not establish arbitrary k; the symbolic proof does.

## originality

PASS

General algorithms for maximal common subsequences were published earlier, but do not give a closed symbolic spectrum for adjacent-swapped permutation powers in the inspected material. A published ternary single-swap equal-power case already yields central binomial count and is openly credited; the q>=4 classification is not a direct consequence because shorter non-LCS maximal words arise and require the unique alternating-segment decomposition and finer r-distribution. Opposite/reversed powers are different pairs and have no such varying maximal-length spectrum.

## value

PASS

Maximal common subsequences can be significantly shorter than the longest ones, so algorithmic searches and maximal-antichain output size need exact length profiles. This natural adjacent-swap perturbation exposes an unbounded gap and nevertheless a universal central binomial total, together with a complete symbolic size spectrum; these precise facts are useful benchmark extremal combinatorics beyond novelty or code correctness alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
