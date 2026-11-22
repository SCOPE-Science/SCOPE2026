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

# Reproducibility and limits

`verification/verify_transfer.py` uses only the Python standard library and checks 243 exact Cayley–Hamilton base identities, all first coefficients, the rational generating numerator, mod-seven coprimality and the strict root-separation bound. It reconstructs all 243 normalized transfer states and 2,465 arcs from the local condition. No stored finite table is trusted.

`verification/verify_direct.cpp` is an independently written implementation of the dynamical update rule, not a reimplementation of the transfer construction. It exhausts every labelled initial state on the open \(3\times n\) grid at \(n=2,3,4\) and counts all primitive three-period states. The exact outputs are bundled in the corresponding text files.

The infinite-length theorem follows from the explicitly defined finite transfer and Cayley–Hamilton, not finite-length experiments. No symbolic computer algebra, Lean or outside validation is needed to run the checkers. The uninspected 1980 full text remains a historical novelty risk. No independent external audit was performed.
