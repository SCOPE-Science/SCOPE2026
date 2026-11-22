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

# Reproducibility and checked domain

Run `python3 check_root_spectrum.py` from a directory containing the accompanying standalone script. The script uses only Python 3 standard-library modules. It independently enumerates every spanning acyclic edge set and every choice of one root per component for orders 2 through 6, then takes the direct Boolean Walsh transform. It checks the formulas for all characters at positive integer activities drawn from \(\{1,2,3,n,n+1,2n+1\}\) with duplicates removed.

It also evaluates the analytically derived expressions with exact integers across all symmetry shells for orders 2 through 129 and activities 1 through \(n+3\), checking signs, resonance locations, and Fourier support, and independently checks the formulas for the sharp nonzero unit-activity gaps through order 159. Its recorded output was:

`PASS 759494 exact assertions; independent root-forest enumeration up to n=6; all-symmetry arithmetic through n=159`

The all-order conclusions for real positive activity do not follow from finite code execution; their proof is the multiaffine polynomial evaluation and the monotonicity argument in `RESULT.md`. The count of assertions is the number of individual equality checks as implemented by `eq` in the script, not a measure of independent theoretical proofs.
