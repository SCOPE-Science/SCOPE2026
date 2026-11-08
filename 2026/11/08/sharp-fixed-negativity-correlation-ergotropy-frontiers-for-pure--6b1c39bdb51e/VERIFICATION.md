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

Use Python 3 and NumPy. Place `verify_frontier.py` in the same directory and run `python3 verify_frontier.py`. The script requires no external datasets or precomputed files, uses a fixed random seed for reproducibility, and prints the assertion count on success.

The current run of the packaged script returned `PASS: 72109 deterministic finite checks; source formula independent 9x9 checks and negativity matrix checks`. It checked 113 values of \(s\in[1,\sqrt3]\), with 209 ordered-spectrum points per section, plus endpoint, optimizer and full nine-dimensional density-matrix checks. It independently computes the global versus local work-extraction difference from the Hamiltonian and eigenvalue ordering, and logarithmic negativity from the trace norm of the matrix partial transpose after random local-unitary rotations.

These finite checks are supporting evidence, not a proof for all \(s\) or all spectra; the complete theorem is deduced analytically from the exact single-coordinate parametrization, its derivative and boundary inequalities in `RESULT.md`. The equality cases at maximal entanglement use their exact limiting spectrum because subtractive radicals can lose floating-point precision at that endpoint. No independent audit or external validation has been performed.
