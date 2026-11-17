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
The source program `code/verify_cycle_dual.py` independently builds all disconnected triples, enumerates the full Alexander dual and the proposed model in finite cases, and explicitly checks each elementary free-face collapse. It tests all relevant common-neighbor clique identities and near/far pair counts. Its actual unedited standard output is included at `code/OUTPUT.txt`. For larger cycles, the program checks local structural identities only. The theorem is established by the symbolic proof in `RESULT.md`, not by extrapolating finite data.

The interval \(n\ge4p+1\) is essential for the stated common-neighbor shape and clique-nerve argument. The phrase 'collapse' refers to the Alexander dual, not to the original three-cut complex. The result gives integer homology of the original, not shellability or an integral homotopy decomposition of it.

The checks and review are same-model only. No independent mathematical audit was performed.
