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

# Reproducibility and limitations

Run `python3 verify_perm_pair.py` with a standard Python 3 installation; no third-party libraries or data are required. The program enumerates literal term equality matrices for ordered pairs on disjoint cycles, not merely the proof's signature classification. It checks against an independent overcomplete pool of possible cycles, and prints the depth, exact type count, minimal witness size and all cycle lengths for depths one to five. For depths one and two it exhausts the integer partitions of every smaller order. It also deletes each cycle of an extremal witness and checks the resulting loss of universality. The recorded run concluded `VERIFY_OK 1305`.

The script checks finite instances only. The general proof and the uniqueness at the minimum use the signed-difference interval lemma and forced-cycle lower bound in `RESULT.md`; neither follows from finite enumeration. The program does not certify publication priority or model correctness independently, and no independent audit has been performed.
