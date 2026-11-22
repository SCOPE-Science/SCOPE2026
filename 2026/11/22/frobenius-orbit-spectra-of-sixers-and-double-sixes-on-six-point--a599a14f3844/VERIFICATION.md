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

# Reproducibility and scope

Run `python3 verify.py` with a standard Python 3 interpreter; no third-party packages or remote services are needed. The expected final marker is `CUBIC_SIXER_S6_FROBENIUS_EXHAUSTIVE_OK`. The script checks the full finite domain of 27 geometric exceptional-line classes, all 296010 candidate six-element subsets, 72 sixers, 36 double-sixes, and all 720 permutations. It calculates intersection products over the integers, not by floating-point approximation, verifies complementary-six incidence, and verifies the closed fixed-point formulas against every permutation and the eleven conjugacy-class profiles. The supplied `check_output.txt` is the captured successful output from the included script.

Finite verification is not used to assert that arbitrary cubic surfaces have such a blowup model, that a given cycle type occurs over every field, or that Severi–Brauer surfaces split: those depend on the stated geometric hypotheses and standard Brauer-group theorem. A formal independent mathematical audit has not been performed.
