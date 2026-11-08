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

# Reproducibility and limits

With Python 3, run `python3 verify.py` from the directory containing `verify.py`, `RESULT.md` and this file. No third-party libraries, network access, input files or external services are required. Recorded stdout is provided in `verify-output.txt`.

The verifier uses exact integers and rational arithmetic. It expands each coefficient numerator in the proof for cycle sizes two through five; tests the nonnegative integer-polynomial coefficient certificates, the exceptional five-state factor, its sign-change count and strict rational root bracket; and independently reconstructs full one-step matrices using exact Gauss–Jordan inversion on sizes two through eight at six rational step lengths. It additionally checks selected small- and large-step signs and mass preservation. The recorded execution produced `VERIFY_OK 1476 exact-arithmetic assertions`.

The verifier does not exhaust all cycle sizes or real step lengths. The all-dimension fourth-jump obstruction is proved analytically by a Taylor coefficient, and eventual positivity by diagonalizing the finite cyclic shift. Descartes' rule of signs completes the unique five-state root classification. The calculation uses no random simulation. The external scientific audit is not performed.
