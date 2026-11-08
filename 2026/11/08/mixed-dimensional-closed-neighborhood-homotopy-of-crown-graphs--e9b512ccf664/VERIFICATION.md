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

The standard-library script `verify_crown_neighborhood.py` enumerates all simplices directly from graph adjacency, checks the exact two-subcomplex union and their graph intersection, verifies the relative free-face collapses pair by pair, and computes complete reduced binary simplicial homology in every dimension for \(2\le n\le8\). It additionally computes \(K_{n,n}\) controls for \(2\le n\le6\). Execute `python3 verify_crown_neighborhood.py` in this directory; the expected full output is `verification_output.txt`, ending `ALL_VERIFY_OK`.

This finite checker is not an unrestricted proof or an independent mathematical audit. The integral homotopy theorem for every \(n\ge5\) follows from the two-sided simplicial cover, explicit relative collapses, the exact graph intersection and the homotopy-pushout argument in `RESULT.md`. All integer-homology and fundamental-group claims use that homotopy decomposition, not lifting mod-two ranks.
