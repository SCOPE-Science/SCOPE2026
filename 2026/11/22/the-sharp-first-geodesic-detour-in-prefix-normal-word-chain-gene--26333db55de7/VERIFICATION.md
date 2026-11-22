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

# Verification and reproducibility

The code files `check_a.py` and `check_b.py` are standalone, depend only on the Python 3 standard library, and each directly checks all length-\(n\) factor intervals of every intermediate binary word.

`python3 check_a.py` enumerates all \(n!\) permutations for each \(1\le n\le7\), accepts exactly those for which each intermediate word passes the prefix-normal inequalities, constructs the complete legal neighboring-transposition graph, and breadth-first searches from every vertex. It prints the full exceptional distance histogram, validates the explicit six-edge witness, and samples its lifts at lengths seven through twelve. Exact output is `check_a.out`.

`python3 check_b.py` independently enumerates generators by bitmask dynamic programming from the all-one word, using integer bit counts to test every contiguous factor; it separately builds the graph and every-pair graph distances and reproduces all exceptional distance classes. Exact output is `check_b.out`.

The finite checks by themselves do not prove anything for unbounded \(n\). The complete argument for all \(n\ge7\) is the zero-appending lemma and the forced forbidden first step with parity. No independent external audit has been performed.
