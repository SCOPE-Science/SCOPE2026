# Review of the critical-step tree synchronization theorem

## Correctness

**PASS.** The proof uses the exact globally strict endpoint inequality for the cosine potential, so no uniform positive descent constant is assumed at the threshold. Finiteness and isolation of the critical configurations give convergence of all orbits. The non-sink linearization has expanding directions; the smooth endomorphism stable-set theorem plus the non-identically-zero analytic Jacobian determinant makes its global attraction set null. A simple Perron eigenvalue supplies one center direction, and the invariant-graph calculation establishes both cubic and quintic coefficients. The reciprocal-square recursion rigorously yields the logarithmic correction and a finite remainder constant. Exact symbolic recomputation checks the stated first nonuniform path coefficient.

## Originality

**PASS within the inspected literature and accessible research comparisons.** The closest directly relevant paper, Buescu–D'Aniello–Oliveira (2026, arXiv:2610.10993), proves descent and convergence only for strictly subcritical steps and gives almost-global attraction under a stronger diffeomorphism condition. The present theorem crosses the formerly excluded full-descent endpoint and quantifies the nonhyperbolic relaxation on arbitrary unweighted trees. The general saddle-avoidance theorem of Schaeffer–McCalla (2019, arXiv:1908.01753) explicitly assumes step size strictly below the critical value; it does not derive endpoint convergence or the graph-specific quintic/logarithmic law. A prior scalar two-clock critical-flip result is a one-dimensional special case, not a covering all-tree theorem. Related three-clock work treats small-step stability. Residual risks include earlier unlocated studies of large-step sine gradients and abstract endpoint center-manifold results; the exact multi-graph coefficient may have alternative derivations.

## Value

**PASS.** The maximum admissible descent step is a natural dynamical threshold, not an arbitrarily selected parameter. At that step the classical strict quadratic energy estimate degenerates, local invertibility can fail, and the attractor becomes nonhyperbolic. The theorem still gives a complete all-orbit convergence classification, an almost-global basin statement, and a quantitative graph-dependent relaxation law. The four-vertex path is the first path with a nonuniform Perron vector, where the explicit logarithmic coefficient genuinely records transverse center-manifold coupling rather than a scalar substitution.

## Verification and limitations

Run `python verify.py` after installing SymPy and NumPy. The script checks exact eigenvectors, cubic and fifth-order invariant-graph equations on three small paths, coefficients and a long-iterate illustrative example. These checks do not replace the global analytic inequalities or the geometric stable-set arguments. The conclusion concerns finite, connected, unweighted trees with sine interaction, not general weighted or cyclic graphs. Historical priority is provisional and independent scientific validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
