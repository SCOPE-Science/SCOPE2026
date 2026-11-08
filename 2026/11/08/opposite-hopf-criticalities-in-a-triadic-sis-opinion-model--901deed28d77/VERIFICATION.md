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

# Reproducibility and scope

The self-contained symbolic checker is `CHECK.py` (Python 3 with SymPy). It differentiates the actual polynomial planar epidemic–opinion field, checks the Hopf parameter surface, rederives the canonical real coordinates, obtains the first Lyapunov coefficient from derivatives, and verifies exact rational parameter crossings and endemic-root ordering. Execute `python CHECK.py` from the directory containing the files. A successful run prints `PASS`.

The substantive existence of periodic orbits follows from the smooth finite-dimensional nondegenerate Hopf bifurcation theorem applied at the two exactly verified points; the symbolic script independently checks its hypotheses other than the abstract theorem. Exact calculations involve real rational algebra plus formal positive variables, not finite enumeration or numerical inference.

This verifies **local** behavior on the synchronous invariant set only. Positive periodic states remain below the opinion sign-switching threshold for sufficiently small amplitude. Neither unsynchronized stability nor global attraction is claimed. A point with vanishing first Lyapunov coefficient is identified but its higher degeneracy and cycle count are not classified.
