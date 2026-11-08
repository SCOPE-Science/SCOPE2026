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

# Reproducibility and boundaries

The analytic argument reduces the unrestricted parameter case to rational estimates. Define \(h_i=r_i+\sum_jb_{ij}\), \(\rho_i=\sum_j|b_{ij}|\), \(H=\max_i(|h_i|+\rho_i)\), \(L=32(1+H)\). For each coordinate, verify the algebraic identity
\[
G_i(x)=\sum_jb_{ij}(x_j-1)-h_i(x_i^2-1)-Lx_i^2(x_i-1).
\]
The lower boundary has positive margin at least \(\frac14[9L/16-\rho_i-7|h_i|/4]\); the upper boundary has negative margin at most \(-\frac14[25L/16-\rho_i-9|h_i|/4]\). In logarithmic coordinates the \(\ell^\infty\) Jacobian logarithmic norm is bounded by
\[
-\frac{9L}{64}+\frac{25|h_i|}{8}+\frac{5\rho_i}{4}\le-\frac92-\frac H8.
\]
These exact inequalities imply strict invariance and the exponential bound for every dimension and all real prescribed parameters.

Run the standalone program `python verification/check.py` with Python 3, SymPy, NumPy, and SciPy. The observed output in the reviewed package was:

`VERIFY_OK exact_completion=1 exact_uniform_constants=4 example_positive_cube=5 quadratic_order_obstruction=1`

The numerical trajectories have finite duration and verify only particular parameters. The universal statements rest on the explicit inequalities and first-exit / contraction argument. No independent audit has been performed. The entire-positive-orthant global-attraction claim is unproved and is not part of this result.
