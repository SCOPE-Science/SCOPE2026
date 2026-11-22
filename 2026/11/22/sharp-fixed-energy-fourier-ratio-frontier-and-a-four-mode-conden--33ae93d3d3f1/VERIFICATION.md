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

The analytic proof uses an exact Fourier multiplier identity, strict concavity on a finite probability simplex, the bottom four eigenvalues of the grid Laplacian, and a uniform two-dimensional lattice-sum estimate. The explicit family attaining the two-scale lower bound is displayed in `RESULT.md` and satisfies the energy constraint exactly for all sufficiently large grid sizes.

Run the standalone Python 3 checker with `python check.py`. It uses only the Python standard library, computes eigenvalues directly, checks the exact minimax interpolation formula at the endpoint and interior energy budgets, and checks random feasible vectors plus the sharp two-scale bounds. The saved checker passed its supplementary tests. Finite floating-point checks are illustrative only; they do not certify all grid sizes, the infinitely many lattice frequencies in the limiting sum, or publication novelty.

The critical asymptotics hold for a fixed real budget strictly above the continuum fundamental energy; uniformity for a budget that varies with grid size is not proved. Real-valued optimizer existence follows by conjugate-symmetric choices of the otherwise free Fourier phases.
