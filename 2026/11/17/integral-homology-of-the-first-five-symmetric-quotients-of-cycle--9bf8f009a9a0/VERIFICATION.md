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

# Verification

From this directory, run `python3 verify.py`; no third-party packages are necessary. The program constructs strict nonempty forest-face-chain orbits via birth-color words, checks all boundary compositions, performs integral elementary cancellations, and checks the exact resulting free ranks and invariant factors. `verification_run.txt` contains the observed outputs for sizes 3 through 7.

The check enumerates all orbit flags for each specified finite size. The independent labeled enumeration checks the complete orbit-flag counts at sizes 4 and 5. It neither checks infinitely many values of the board order nor proves absence of equivalent prior work. The theorem is precisely the exhaustive finite range established by the script and the proof of the orbit-chain model.
