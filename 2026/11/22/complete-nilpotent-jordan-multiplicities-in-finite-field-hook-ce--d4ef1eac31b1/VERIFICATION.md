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

# Reproducibility and scope of checks

The included `checker.py` runs with Python 3 standard library only. Execute `python checker.py` from the directory containing the packaged artifacts; the accompanying `checker_output.txt` is the captured output of this exact checker. All 19 field/dimension configurations passed: prime fields of orders 2, 3, 5, 7 and extension fields of orders 4 and 9, spanning dimensions \(n+1\) for \(3\le n\le7\) where tested.

For each case, the checker explicitly constructs every nilpotent centralizing matrix from its coordinates, calculates its actual matrix powers, Gaussian-eliminates each power over the finite field, and derives the Jordan type from rank differences. Independently it calculates the exact table's predicted profile and aggregated partition multiplicities. The overall enumeration has 113,305 tested matrices. The test detects arithmetic and boundary errors in these instances but does not make a finite-range calculation an infinite proof. The text proof separately verifies all \(n\ge3\) and every finite field.

No independent audit was performed. Historical priority cannot be certified from a search alone; the classical centralizer normal form and the previously published square-zero subcase are acknowledged.
