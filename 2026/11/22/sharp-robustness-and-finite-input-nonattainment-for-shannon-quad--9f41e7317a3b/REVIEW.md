# Mathematical review

## Correctness

**PASS.** The log barrier inherent in the negative Shannon entropy guarantees interior predictions. A direct implicit derivative calculation gives a weighted centering Jacobian. Its cross-norm reduces to signed quadratic forms by positive semidefiniteness; Jensen optimization over the two sign blocks gives the exact coefficient, and a balanced sign perturbation makes the bound sharp. A separate second-variation argument confirms the same sharp reciprocal modulus for strong convexity. Uniqueness of extremal probabilities and continuity along score segments establish finite-secant nonattainment. A standalone rational checker supports but cannot replace the proof.

## Originality

**PASS, with historical-priority caveat.** The cited Fenchel–Young and generalized-entropy papers establish the regularization framework and general smoothness, not the displayed sharp mixed coefficient, finite-dimensional odd-parity gap and extremal geometry. Related pure-quadratic and Tsallis sharp coefficients are closer than a title comparison might suggest: they recover limiting regimes but do not assert the exact mixed penalty or its finite-score nonattainment. Targeted database queries and full-text inspection did not reveal a dominating formula. An exact strong-convexity inequality in older, differently indexed convex analysis literature remains a material possibility.

## Mathematical value

**PASS.** The result supplies the exact global robustness budget for a natural combination of Shannon entropy and quadratic concentration penalties, including a dimension-parity correction that the usual dimension-only norm bound misses. It identifies the unique worst-conditioned probability shape (up to permutation) and a qualitative difference between local sharpness and finite-score attainment, quantities relevant to smooth probability prediction and regularization design. It is not merely an endpoint reparameterization: the mixed regularizer's exact constant and attainment classification require simultaneous optimization of two different curvature terms.

## Scope and limitations

The result is finite-dimensional and concerns strictly positive parameters and unweighted norms. No algorithmic convergence, statistical performance, weighted variants, or independent mathematical certification is claimed. Relevant inspected full texts are arXiv:1805.09717, arXiv:1901.02324 and arXiv:2108.01988; additional historical coverage remains possible.

Self-review: passed. Independent audit: not yet performed.
