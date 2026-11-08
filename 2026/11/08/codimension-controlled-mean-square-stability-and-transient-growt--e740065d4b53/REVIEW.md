# Scientific review

## Correctness — PASS
The exact source estimator is substituted without modification, preserving the forward-difference term and the fresh Gaussian draw. Orthogonal Gaussian block moments and parity give a closed triangular recursion for the hinted and unhinted expected squared norms, with strictly positive forcing for every smoothing radius \(\tau>0\). Its scalar spectral inequality is equivalent to the claimed sharp step boundary, and exact solution at equality and beyond establishes linear/exponential divergence. A separately checked identity for the difference of block moments proves the universal partition. The stable transient follows from the same initial-value recursion. The attached checker independently evaluated selected exact Wick moments and finite samples; finite tests are not used as an all-dimensional proof.

## Originality — PASS with residual historical risk
Primary source arXiv:2609.08277, Sections 3--4 and Appendix C, supplies the control-variate update, oracle hint and general variance-descent bounds but does not state the all-time exact codimension stability frontier, divergent-mode partition or arbitrarily large stable transient. The closest relevant published records from mathematical research searches concern other stochastic algorithms or Haar-based subspace descent, and neither implies this specific projected-Gaussian iteration identity. Classical Gaussian smoothing and fourth/sixth moments are known, not claimed new. A hidden historical special-case result remains possible; the accessible full texts and recorded searches did not locate a dominating statement.

## Mathematical value — PASS
The dimension appearing in the actual infinite-horizon stability ceiling is the **unhinted codimension**, whereas full ambient dimension still causes an arbitrarily large transient and controls the finite-difference noise floor. This distinction is material for fixed-hint stochastic optimizer tuning: the stable regime can be far larger than a one-step Euclidean-descent guarantee, without guaranteeing monotone transients. The exact stationary and critical formulas are benchmarks for testing adaptive-hint algorithms and safeguards; they are not asserted to transfer automatically to practical estimated references.

## Limits and comparison
The result treats oracle projected gradients on the isotropic quadratic, not estimated references or general nonlinear objectives. Unlike the source's bounded-gradient general theorem, this quadratic has unbounded gradient. The exact dimension-dependent critical recurrence differs structurally from esGs and from generic zeroth-order bounds. Ghadimi--Lan was identifiable through its accessible abstract, not inspected in full; historical-priority risk survives.

Self-review: passed. Independent audit: not yet performed.
