# Scientific review

## Correctness — PASS

The stochastic recurrence is obtained directly from the uniform singleton update of Xie–Qi–Han [1, Algorithm 1]. Computing the four scalar second moments produces the displayed exact matrix, not a sufficient Lyapunov inequality. Symbolic determinant algebra identifies the unique positive boundary; a positive-semidefinite-preserving covariance map and table-permutation symmetry show that its spectral radius is the radius of this four-dimensional matrix. Perturbation at zero, the absence of an interior unit Perron eigenvalue, and a real root above one beyond the boundary prove the exact stability interval without numerical extrapolation. The two-step reachable vectors span the whole error state for nonzero initialized solution, ensuring a nonzero dual Perron projection at and beyond the boundary. Conditional-update identities, polynomial factorizations and small finite sample trees were additionally checked by the accompanying script (354 checks). The proof is finite-dimensional, with no reliance on unverified exhaustion of infinite iteration counts.

## Originality — PASS (best-knowledge assessment)

The main source [1, Sections 3.2–3.4 and Appendix 7.2] proves convergence under sufficient stepsize conditions and establishes equivalence to JacSketch, not an exact rank-one if-and-only-if boundary. The original SAGA treatment [2, Sections 2 and 5] and JacSketch theory [3, main convergence sections] give sufficient rates for broader settings. Minibatch stepsize theory [4] and general SGD second-moment stability [5] provide techniques but not the same residual-table recurrence or root. The closest searchable published related findings concern two-client Loopless SVRG, an orthogonal-system Kaczmarz momentum variant, and stationary STORM noise, none of which entails the coherent-row residual-tracker cutoff. Mathematical implication and initialization scope were compared rather than only terminology. An older equivalent SAGA matrix-moment calculation may exist; absence from retrieved material is not proof of absolute novelty. Independent priority verification remains open.

## Mathematical value — PASS

A concrete, natural, maximally coherent rank-one input family is especially useful for assessing whether general variance-reduction stepsize theory is sharp. The exact stability frontier is a positive-root classification for every number of rows and proves nondecay precisely for the initialized method rather than an arbitrary artificial state. The published sufficient step \(1/[m(m+4)]\) is asymptotically a factor \(m+4\) below the true stability limit. This demonstrates a dimension-growing calibration gap and provides a reproducible stability benchmark for similar residual-table stochastic methods. This is not a theorem about general matrices, fastest convergence, or practical parallel execution.

## Literature and residual limitations

Primary material inspected: [1] algorithm, sufficiency theorem, JacSketch correspondence and appendix; [2] SAGA update and rate proof; [3] JacSketch main development and rates; [4] minibatch step theory; [5] SGD spectral stability method. Residual historical-priority risk remains, including an unindexed early quadratic SAGA specialization. Finite scripted checks supplement the analytic proof only.

Self-review: passed. Independent audit: not yet performed.
