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

# Verification

The analytic proof in `RESULT.md` derives the conserved seven-term maximum by taking the subtraction-free logarithmic limit of a previously published positive rational first integral. It identifies each exact polygon vertex by supporting inequalities, proves all-energy rigid rotations via primitive lattice arclength and homeomorphism orientation, and counts integer lattice cycles from their rotation displacement. This is the mathematical justification of the infinite-domain claim; a finite checker is not a proof of it.

The standalone `verify.py` requires Python 3 and SymPy. Running `python verify.py` from the extracted directory produced the recorded output `verification_output.txt`. The checker verified the rational three-return invariant as a symbolic polynomial identity; 502 rational polygon levels and their arc displacement; 3,536 independent off-shell invariance tests; and all 6,174 lattice states over integer levels 2–50. The exact orbit periods and populations matched their claimed formulas. No stochastic inference or numerical tolerances are used. All calculations are finite corroboration.

Limitations: no independently performed audit; possible historical overlaps in unavailable or unindexed articles have not been eliminated. These checks do not certify global research priority.
