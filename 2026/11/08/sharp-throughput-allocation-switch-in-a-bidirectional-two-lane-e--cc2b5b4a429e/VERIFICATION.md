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

# Reproduction and actual check boundaries

The standalone checker `verify_capacity.py` was run against the newly prepared proof with Python 3 and SymPy. It reported `PASS 88775 exact/algebraic/finite-state and bounded-grid checks` after fixing two implementation mistakes in the checker before final validation. The final embedded checker is the successfully executed version.

The check suite verifies exact symbolic change-of-variables, exact critical polynomial elimination, local Hessian formulas, the global-balance equation for every state of all canonical sectors on two periodic rings of lengths \(L=3,4,5\), and the expected signed currents calculated directly from separate left/right hopping rates. It also compares the explicit continuum optimizer with a bounded grid of 81 by 81 density choices for twelve couplings. The finite grid cannot establish optimality over a continuum; the proof in `RESULT.md` establishes global optimality and the uniqueness of the transition analytically. The finite-state tests cannot imply an infinite-volume theorem alone; exact product stationarity follows from the telescoping identity.

Run from a directory containing `verify_capacity.py` and `requirements.txt`: `python -m pip install -r requirements.txt`, then `python verify_capacity.py`. The checker does not read old datasets, papers, or other packages. The mathematical result is not independently audited or externally certified.
