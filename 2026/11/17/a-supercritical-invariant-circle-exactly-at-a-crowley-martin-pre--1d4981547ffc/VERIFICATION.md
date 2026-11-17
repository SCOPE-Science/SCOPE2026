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

Run `python verify_vertex_ns.py` with Python 3 and SymPy. The program checks, using exact arithmetic, the prey-nullcline maximum, the fixed point, both Jacobian matrices, the unit roots, cubic tensor contractions, normalized left and right eigenvectors, the exact resonant coefficient \(G=-7/20+i\sqrt7/140\), the radial coefficient \(\ell_1=-1/4\), and the transversality derivative \(1/4\). The observed final line is `ALL EXACT CHECKS PASSED`.

The proof's passage from the computed nonzero cubic coefficient to a locally attracting invariant circle invokes the standard nonresonant Neimark–Sacker bifurcation theorem. The symbolic calculation checks its model-specific hypotheses but is not itself an independent proof or audit of the general theorem. The result is restricted to a neighborhood of \((1,2)\) and sufficiently small positive \(h-1\). No global orbit claims or extrapolations from numerical trajectories are made.
