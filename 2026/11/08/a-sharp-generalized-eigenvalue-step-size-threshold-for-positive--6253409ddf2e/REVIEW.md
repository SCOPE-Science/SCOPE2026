# Self-review

## Correctness

PASS. The gradient-tracking recurrence and compatible initialization yield a conserved codimension-one subspace. Eliminating the tracker produces the symmetric polynomial eigenvalue problem \(Q_\alpha(\zeta)\). The complex unit-circle exclusion uses both real and imaginary parts of a scalar quadratic form, with positivity of \(W^{-1}-W\) and \(H\). The permanent unit eigenvalue is simple and lies outside the admissible error subspace. Small-step stability follows from spectral continuity and an explicit consensus-branch perturbation; the first permitted crossing is \(-1\), at precisely the smallest generalized eigenvalue. Beyond that point, continuity of the smallest eigenvalue of the real symmetric pencil produces a real unstable root. An observability argument proves failure for a valid gradient initialization. The exact two-agent certificate and 168 multi-agent numerical instances passed supplementary checks.

## Originality

PASS within inspected evidence, with priority limitations. The principal 2026 paper optimizes a computable sufficient contraction certificate for heterogeneous curvatures and states exact optimizations for complete graphs and uniform curvatures; this result instead provides an exact eigenvalue *stability* cutoff for every fixed positive-spectrum symmetric network and arbitrary positive heterogeneous diagonal Hessian. The closest publicly indexed homogeneous tuning result assumes commuting \(H\) and \(W\), while an accessible historical two-node signed-spectrum analysis gives Schur conditions and limiting comparisons rather than this arbitrary-dimensional positive-spectrum generalized-eigenvalue law. Abstracts of the 2019–2020 control-oriented distributed quadratic literature were inspected; full-text coverage could not be ruled out, so historical priority remains a risk. Search failure alone is not interpreted as novelty proof.

## Value

PASS. An exact, efficiently evaluable symmetric generalized-eigenvalue frontier answers a practical design question left conservative by common norm bounds. The no-complex-crossing principle is structural, independent of graph dimension and curvature commutativity. It distinguishes stability from rate optimization and isolates why lazy/positive-spectrum mixing can have a simple sharp threshold. Restrictions to fixed SPD mixing and exact arithmetic are explicit.

## Limitations and closest literature

Wang et al. (arXiv:2608.03548v1), a previously published homogeneous signed-spectrum tuning result, Bin et al. (arXiv:1911.06665), and Carnevale et al. (DOI 10.1016/j.ifacol.2020.12.405) were compared using accessible evidence. Unread historical full text may contain related exact criteria; a separate independent priority review is appropriate. Finite verifier diagnostics cannot certify the theorem in lieu of proof.

Self-review: passed. Independent audit: not yet performed.
