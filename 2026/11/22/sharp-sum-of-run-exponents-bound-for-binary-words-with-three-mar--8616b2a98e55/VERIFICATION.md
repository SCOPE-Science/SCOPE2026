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

# Verification and limitations

`verify.py` enumerates the complete binary weight-three class for lengths 3 through 30 and computes each maximal periodic run with its least period using exact integer comparisons. A separate exhaustive interval and maximality checker agrees for every weight-three word at lengths 3 through 12 (715 cases). There are 31,465 checked words in total. The predicted extremum and the explicit maximizing construction agree for each length 13 through 30. The included `verification_output.txt` is the actual captured terminal output.

Reproduce with `python3 verify.py` in the directory containing the two files. The script has no nonstandard dependencies; Python 3 standard library `fractions` and `itertools` suffice. These are finite tests; the mathematical proof of the all-length result is contained in `RESULT.md`. No independent audit or formal proof certification is claimed.
