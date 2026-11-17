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

# Exact finite verification

Run `python verify.py` with `collapse_certificate.json` in the same directory. The script separately enumerates maximal matchings using backtracking and all edge combinations, compares full simplex sets, replays each certified free-face pair against the **entire** current complex, checks the saved final complex, and calculates cycle rank and connected-component counts of the terminal graph. The five checks include all orbit types for every ladder of sizes three through five. Recorded output is `verification_output.txt`.

These finite checks prove only the explicitly listed five graph cases. They do not prove any uniform pattern for larger ladders or certify independent review. The integer homotopy conclusion follows because elementary simplicial collapses preserve homotopy and the remaining spaces are graphs.
