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

# Reproduction and verification

Run `python3 verify.py` in a Python 3 installation. The script uses only the standard library and a fixed pseudorandom seed. In the saved package, its successful output begins `PASS 50694 finite diagnostic assertions`.

The diagnostic independently multiplies the specified \(3\times3\) matrix factors and compares their densities to the closed exponential/rotation expression across six distinct angles, orders 1–18, and seeded finite delay vectors. It also checks the interior and terminal partial-sum identities, the algebraic cutoff, the critical-endpoint positivity margin, and explicit finite negative-density witnesses at values above the proposed cutoff. These are finite diagnostic assertions; they do **not** verify the infinitude of possible orders or the density of an irrational rotation orbit.

The all-orders result is established analytically in `RESULT.md`: the summation-by-parts decomposition has nonnegative coefficients, its terminal coefficient is strictly larger than the sharp intermediate infimum, and irrational powers of \(e^{i\varphi}\) are dense on the unit circle. For a fixed integer order and finite waiting times, \(e^{-T_k}>0\), so strict positivity of the normalized bracket implies strict positivity of the actual density. For the necessity statement, a sufficiently large but finite final waiting time and subsequent arbitrarily small positive perturbations of the remaining delays yield an actual negative density when the cutoff is exceeded.

The numerical check of the strict endpoint at finitely many sample points is not substituted for the analytic terminal-weight argument. Nor do these checks prove historical novelty. The matrix-product normalization and non-Markovian pole obstruction are cited results, not new checker-certified claims.
