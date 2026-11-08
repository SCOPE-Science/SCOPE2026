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

Execute the three standalone Python 3 programs from the same extracted folder, in this order:

```
python check_transfer.py
python check_dynamics.py
python check_algebra.py
```

`check_transfer.py` uses exact integer dynamic programming on the nine rung-pair states for \(n=3,\ldots,12\), and tests the closed-form square-flat count. `check_dynamics.py` exhaustively enumerates all initial colorings for \(n=3,4,5\), filters square-flat cases, independently constructs prism adjacency, and evolves both CCA and GHM to an actual repeated configuration to measure rational eventual per-site excitation rates. `check_algebra.py` uses exact rational arithmetic to verify the integer characteristic polynomial of the unweighted transfer and compares two equivalent variance forms.

Saved program outputs are `transfer_output.txt`, `dynamics_output.txt`, and `algebra_output.txt`. These finite checks independently exercise the all-size proof's finite combinatorics and update-rule normalization but do not by themselves prove convergence or the infinite-size local limit. The latter follows from explicit finite-dimensional Perron spectral perturbation and Fourier inversion in `RESULT.md`. No external independent assessment is claimed.
