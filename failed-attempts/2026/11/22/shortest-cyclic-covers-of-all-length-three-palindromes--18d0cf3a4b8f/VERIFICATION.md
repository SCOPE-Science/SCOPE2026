---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Each distinct unordered pair requires three traversals: two traversals alone could support both opposite backtracks only if each occurrence immediately followed the other in cyclic order, impossible when the word has length at least q²≥4. Each loop requires two traversals. The closed walk has even off-diagonal degree at each vertex; for even q the three-traversal baseline gives odd degree everywhere, costing at least q/2 additional traversals. Doubling one matching in the even case yields the connected Eulerian graph for the construction. Replace one traversal of each ordinary pair by a three-step alternating walk and double each loop; this preserves the closed tour and supplies precisely the required witnesses, including the constant triples. I independently recovered exact minima 8, 15 and 28 for q=2,3,4 by breadth-first search on the pair-state graph with an accumulated palindrome mask. One can fix the root state to 00 by rotating to an occurrence of 000. The bounded check corroborates, but does not replace, the all-q proof.

## originality

FAIL

A distinct indexed result states the exact minimum for all ordinary four-letter palindromes abba, including aaaa. The two extremal problems are exactly equivalent: if L3 and L4 denote the respective minima, L4(q)=L3(q)+q². In a cyclic run decomposition an off-diagonal aba needs a singleton b-run flanked by a-runs, and an off-diagonal abba needs a b-run of length exactly two with the same flanks. Each such central run witnesses just one required ordered pair. Choose one run for each of the q(q−1) pairs and lengthen each singleton from one to two to turn a triple cover into a four-letter cover; also lengthen one constant run of length at least three for each letter by one. The latter runs are disjoint from the chosen centers. This adds exactly q² letters and preserves all run adjacencies. Conversely shorten each of the chosen central runs from two to one and one constant run of length at least four per letter by one. This removes exactly q² letters and gives a triple cover. The exact four-letter formula therefore implies the exact triple formula, and its Euler-tour witnesses transfer by compression. This is demonstrable mathematical coverage, not a claim about publication priority or which proof came first.

## value

FAIL

The problem is natural and the local edge-parity proof is clear, but the claimed invariant and a sharp witness are mechanically obtainable by the same uniform run edit from the already indexed exact four-letter result. The frozen claim supplies no distinct classification or new range of invariants; the independent small-case replay does not change that.

The dated certificate retains the supplied scientific assessment, sources and limitations.
