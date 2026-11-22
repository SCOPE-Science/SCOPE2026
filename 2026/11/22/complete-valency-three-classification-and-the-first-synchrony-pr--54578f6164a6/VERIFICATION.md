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

# Executed verification
The included `verify_census.py` was executed using Python 3 and the standard library. It enumerated exactly 160000 labeled nonnegative-integer four-by-four matrices with each row sum equal to three; the accepted labeled counts were 1560, 840, and 176 for \(\omega^2=1,2,3\). Canonicalization by all 24 cell permutations yielded 65, 36, and 8 classes. Summing permutation stabilizers over all accepted labeled matrices gave fixed-incidence totals 1560, 864, and 192, agreeing with Burnside's lemma. Testing all 13 nontrivial cell partitions for balanced input produced synchrony-count distributions \((0,47,18)\), \((1,27,8)\), and \((2,5,1)\). The program regenerated the complete sorted CSV of 109 representatives and exited successfully.

A separate SymPy calculation checked the exact characteristic polynomial \(t(t-3)(t^2+q)\) for every CSV representative (109 of 109). The independent principal-minor coefficient calculation inside the standalone checker agreed with the trace predicate for every accepted matrix. The proof that the only possible positive integer \(q\) are \(1,2,3\) is analytic and does not rely on enumeration.

# Scope of verification
The finite enumeration is complete because each of the four rows belongs to the full set of twenty nonnegative length-four integer vectors with sum three. No claim is made about networks of other dimensions or valencies, or about nonlinear bifurcations. The checker does not require proprietary data or any external file other than its own included source, and it writes `canonical_representatives.csv` in the same directory. The scientific review and code executions do not constitute independent audit.
