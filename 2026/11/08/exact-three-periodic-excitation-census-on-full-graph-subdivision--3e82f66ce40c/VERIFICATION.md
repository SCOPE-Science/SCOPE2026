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

# Verification record

Two standalone Python programs are included. Running `python verify_direct.py` reproduces `verify_direct.out`. Running `python verify_structure.py` reproduces `verify_structure.out`. Both were executed from the submitted files and their actual text outputs were saved.

The direct program explicitly iterates the three-state excitation map three times on all \(774927\) configurations across five small subdivided graphs and compares primitive-period-three counts with the formula. The structural program tests all \(43\) connected labelled graphs on two through four original vertices by independently enumerating edge-vertex phase extensions, evaluating the product formula, and checking the existence of a simple cycle with length divisible by three. It also checks the complete-graph multinomial values for \(3\le n\le8\).

The proof's unrestricted quantifiers are mathematical, not a computational extrapolation. The computations do not address other primitive periods, basins of attraction, automorphism orbit counts, or global historical novelty. External independent validation has not been performed.
