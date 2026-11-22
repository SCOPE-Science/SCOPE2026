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

# Reproducible checks and precise limits

Run `python3 check_rps_tail.py` with Python 3.9 or later, using only the standard library. The script passed **4912 assertions**, including exact support-count comparisons over all nonempty proper subsets for \(2\le m\le10\), the recursive-versus-binomial formula for random positive simplex points, reverse-spacing invariance, the published uniform minimum and two corner expansions.

For a separate numerical cross-check, install NumPy and SciPy and run `python3 quad_rps3.py`. This computes the contribution to \(\Pr(R_3>t)\) from **only** the neighborhoods \(D_1>0.99\) and \(D_3>0.99\), by a transformed Gaussian quadrature over the Dirichlet angular coordinate and bisection of the radial threshold. The rescaled contributions at \(t=20,25,30,35\) were respectively \(9.633941805\), \(10.425546888\), \(10.568414444\), and \(10.594183018\), approaching the analytic coefficient \(2\mathrm B(1/3,1/3)=10.599832502\ldots\).

These computations are finite checks, not proofs of the all-dimension theorem. The proof in `RESULT.md` derives the sector Jacobian, checks every possible vanishing-face exponent analytically, isolates the two dominant corners, and justifies the leading constant by dominated convergence. The quadrature intentionally does not compute the complementary region's finite-threshold probability. No independent mathematical audit has been performed.
