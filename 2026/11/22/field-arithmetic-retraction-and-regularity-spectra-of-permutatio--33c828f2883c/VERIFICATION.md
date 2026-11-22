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

# Reproducibility

Execute `python3 verify.py` using Python 3 without third-party modules. The program explicitly enumerates all endomorphisms arising from cycle-component selections over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\); tests literal composition for idempotence; and searches the complete finite endomorphism list for a regularity witness. It compares both rank histograms to the two independent enumerator implementations and checks the known all-regular criterion. The file `verification_output.txt` contains the actual captured terminal output, ending in `CHECK_OK 13 exhaustive configurations`.

Finite enumerations verify the listed configurations only. The unrestricted rank identities follow from the combinatorial proofs in `RESULT.md` and the established single-target-cycle Hom classification. No independent audit has been performed.
