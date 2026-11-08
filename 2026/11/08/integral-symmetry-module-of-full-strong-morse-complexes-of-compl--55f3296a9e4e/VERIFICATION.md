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
# Verification and scope

`python3 verify.py` executes with the Python standard library; `verify_output.txt` records the actual run. The verifier independently enumerates every vertex filtration for \(n=2,3,4,5,6\), builds its strong gradient from the number of earlier neighbors, and confirms equality of **all** faces with those arising from the closed facet formula. It checks that all \(3n\) mixed faces are exactly the predicted edges and that no claimed facet is contained in another. The complete simplicial chain action on fixed faces is evaluated with orientation signs to produce Lefschetz traces for selected swaps and vertex permutations, then compared with the two character formulas.

The proof is independent of finite computation: the three-partition description of all filtrations yields an exact all-parameter facet census; elementary contractibility of each side yields a relative homology exact sequence over \(\mathbb Z\); and the signed bridge permutation action determines the integral module. No external/independent audit was performed.
