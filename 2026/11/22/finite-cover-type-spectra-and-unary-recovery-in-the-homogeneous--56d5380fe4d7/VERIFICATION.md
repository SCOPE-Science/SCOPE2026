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

# Verification of exact type spectrum

Run `python3 verify.py` from the directory containing `verify.py` using a Python 3 interpreter. No third-party dependencies are required. The checker forms actual finite two-element fibres, considers every choice of the binary matching bit to old and new fibres, and deduplicates the resulting ordered complete coloured diagrams. These counts are independently compared with the explicit formula for 40 parameter/arity/matching configurations. A separate exact rational coefficient expansion of the stated exponential generating function is checked against the formula for 288 cases. The recorded output of a successful execution is provided in `verification-output.txt`.

The finite checks cover only \(f+s\le3\), \(r\le3\) in the direct diagrams, and 36 occupancy pairs over eight arities in the formal-series calculation. They do not alone prove an infinite theorem; the labelled-class decomposition in `RESULT.md` proves it. The script is a direct finite-diagram check, not an independent human mathematical audit.
