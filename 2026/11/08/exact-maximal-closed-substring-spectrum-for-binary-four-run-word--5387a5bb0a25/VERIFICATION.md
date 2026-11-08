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

# Verification of the four-run maximal-closed-substring classification

The proof in RESULT.md is an all-parameter argument. The accompanying `verify.py` is a direct finite cross-check, not a claim of exhaustive verification over all positive integers.

The checker independently enumerates all factor intervals of each word and tests each proposed border for occurrence multiplicity in that factor. It rejects an occurrence when an available one-symbol extension is also closed. This does not use the claimed endpoint classification. The second implementation constructs the claimed endpoints directly from the parameters and compares two complete sets for every run-length quadruple with entries from 1 through 8 (4,096 cases). A separate composition loop tests the exact attainable count spectrum for every length 4 through 32.

Reproduce with `python3 verify.py`. Expected output consists of two PASS lines, one for the 4,096 exact endpoint comparisons and one for the 4–32 spectrum checks. Standard-library Python 3 is sufficient; there are no external files, downloads, random seeds, or platform-specific dependencies. Mathematical limitations and unresolved historical priority are detailed in RESULT.md and REVIEW.md. No independent audit has been performed.
