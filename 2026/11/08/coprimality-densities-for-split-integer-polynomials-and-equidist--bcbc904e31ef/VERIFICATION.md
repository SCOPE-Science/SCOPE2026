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

# Verification and scope

The supplied `verify.py` checks exact finite CRT probabilities for several shift patterns and prime sets; it constructs the product of local factors by exact rational arithmetic and verifies independent enumeration of all residue tuples. It also computes the adjacent-shift prime-truncated Euler factor and counts the first 300,000 integers in the \(\sqrt2\) example, using exact integer square roots to avoid floating point.

The proof's infinite large-prime bound is explicitly imported from Holdridge Theorem 1.3 for polynomial degree at least two and Champagne's linear case, and is not claimed to follow from experiments. The manuscript checks the shift substitution, the preservation of irrational polynomial coefficients, and the finite union across shifts. No independent audit was performed.
