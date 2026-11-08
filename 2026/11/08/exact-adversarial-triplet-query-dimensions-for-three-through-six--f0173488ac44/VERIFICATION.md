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

The standalone verifier `verify_rooted_triplet_online.py` was executed against `rooted_triplet_strategy.json` with Python 3. It returned `ROOTED_TRIPLET_ONLINE_PASS` and checked all rooted binary labeled trees for each size \(3\le n\le6\), all strategy branches, and the full five-taxon upper-bound split test.

The lower-bound certificates contain \(1,7,31,511\) internal query labels and have \(2,8,32,512\) nonempty leaves. The six-taxon upper bound is the immediate 945-versus-1024 counting obstruction. The five-taxon upper bound is independently verified by the 35/17/18/7 split inequalities; the 105-versus-128 counting bound alone would be insufficient.

The checker uses a second tree-generation and predicate-computation method, rather than assuming the certificate generator's ordering of trees. All mathematical computations concern exact finite sets; they do not certify unexamined taxon sizes.
