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

# Finite exact verification

Run `python check_clique_corona.py` with Python 3 and no external dependencies. The checker generates graph adjacency lists, enumerates all vertex-incidence masks and tests independence, applies an unnormalized fast Walsh--Hadamard transform to the full Boolean indicator, and compares the resulting **signed** multiplier counts with the three-case formula. It also checks the spectral rank and the least positive multiplier and independently applies a second transform to the computed zero/nonzero frequency support to evaluate the endpoint projection norm as an exact rational number.

The twelve fully checked pairs \((h,b)\) are \((2,1)\), \((2,2)\), \((3,1)\), \((3,2)\), \((3,3)\), \((4,1)\), \((4,2)\), \((4,3)\), \((5,1)\), \((5,2)\), \((6,1)\), and \((7,1)\). These cover both the added-Hamming-shell resonance and its absence, including values of \(q\) below and above the core dimension, with at most sixteen graph vertices. All comparisons use integers or exact rational arithmetic. The observed terminal output is `CLIQUE_CORONA_EXACT_PASS 12 complete transforms`.

Computed examples: \((h,b)=(4,1)\) gives rank \(76\), least positive multiplier \(8\), and sharp endpoint norm \(97/32\); \((4,2)\) gives rank \(207\), multiplier \(64\), and norm \(7809/2048\); \((4,3)\) gives rank \(464\), multiplier \(512\), and norm \(9251/2048\). Both resonant and nonresonant formulas agree with direct transforms. The all-parameter statements rely on the complete algebraic proof in `RESULT.md`; these finite tests are not a substitute for a proof and are not an independent audit.
