---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of double-occurrence subsequence classification

The file `verify_two_scattered.py` uses only Python 3's standard library and is executable with `python3 verify_two_scattered.py`. Its exact integer output is embedded in `verification_output.txt`.

Three separate algorithmic mechanisms are applied: a capped dynamic program independently counts the indexed scattered copies of each pattern in each host; explicit backtracking reconstructs every embedding for hosts having exactly two; and a product of geometric-series coefficients computes the prediction separately for each fork coordinate. A fourth exact expression for the coefficient at host length \(m+2\) is checked.

The exhaustive domain is all adjacency-distinct targets of lengths two through four for alphabet sizes two and three, and lengths two through three for size four; all hosts to lengths ten, eight and seven, respectively, within these domains. Altogether 534 instances and 1,472,158 host words were checked. Exactly 147,576 two-occurrence host words were individually backtracked; every one had precisely one differing coordinate between its two embeddings. The resulting per-fork histograms matched the gap-product formula, not merely the total count. Binary tests supplement the theorem, whose scope is alphabet size at least three.

The proof in RESULT.md establishes the theorem for arbitrary target and host lengths; finite enumeration does not prove its all-length content. No external independent audit has been performed. No claim is made for patterns with equal adjacent letters, for more than two indexed embeddings, or for a non-labeled alphabet.
