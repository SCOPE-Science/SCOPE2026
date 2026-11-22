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

# Reproducible checks

Run `python3 checker.py` with standard Python 3.10 or newer. The supplied `checker_output.txt` records a successful local execution. The checker directly evaluates the quandle operation and the homomorphism identity for each normal-form map in three small parameter configurations and independently checks the symbolic Gaussian/Stirling polynomial. It also exhaustively checks all \(4^4\) functions for the four-point case.

Results for \((p,d)=(2,1),(3,1),(2,2)\) count respectively \(16\), \(243\) and \(16384\) endomorphisms with full rank histograms matching the theorem. Additional coefficient/checksum tests cover \((p,d)=(3,2),(2,3)\) without attempting exhaustive enumeration of their many functions. The mathematically critical statement that all endomorphisms are of normal form is proved directly in `RESULT.md` by comparing translation differences. These computational checks are finite corroboration, not a substitute for that general argument.

No independent audit or external mathematical certification has been performed; a historical-priority risk remains for inaccessible or undiscovered prior full texts.
