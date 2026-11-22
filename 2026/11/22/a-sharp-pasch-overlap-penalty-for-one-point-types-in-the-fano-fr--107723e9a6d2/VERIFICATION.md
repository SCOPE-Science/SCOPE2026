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

# Reproduction and limits

Run `python3 verify.py` using Python 3 with no third-party packages. The script generates all thirty labelled Fano planes by permuting the vector-space model, independently detects Pasch four-block configurations, checks exact forbidden-link agreement for three constructed bases, and reproduces the sharp fractions and integers. It checks all 32768 six-base link masks and locally enumerates all possible compatible second Pasches with up to ten old points. The program terminates with `ALL CHECKS PASSED` on success; see `verification_output.txt` for the actual recorded output.

The infinite-family conclusions and equality characterization are proved in `RESULT.md`, not inferred from the finite computations. In particular, an exhaustive local check through ten points alone would not establish rigidity at larger orders.
