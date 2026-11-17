# Self-review

## Correctness — PASS

The one-sided Fréchet derivative of the positive-operator parallel sum is exactly \(H\mapsto CHC^*\), where \(C=B(A+B)^{-1}\). Its induced norm on self-adjoint directions is \(\|C\|^2\), with rank-one positive directions approaching equality. Integration over the convex spectral box proves the global upper bound, and perturbations near an interior approximation to an extremal pair prove global sharpness. For each unit vector, the spectral box bounds both operator images by radius \((\kappa-1)/2\) around the common center \((\kappa+1)z/2\). The parallelogram identity gives a scalar envelope; the derivative of this scalar envelope changes its maximizer at \(\kappa=2+\sqrt5\). Explicit planar symmetric reflections realize equality, and the algebraic second threshold is \(\kappa=5+2\sqrt6\). This establishes the theorem analytically on arbitrary real or complex Hilbert spaces of dimension at least two. The finite diagnostic script checks representative extremizers and samples but does not establish the proof.

## Originality — PASS, qualified

Alwadani, arXiv:2611.05523v1 (2026), Sections 2–3, studies monotonicity, paramonotonicity, and decomposition invariance of set-valued parallel sums; it neither optimizes operator-norm sensitivity on common positive spectral boxes nor supplies the two thresholds. Luo–Song–Xu, arXiv:1806.07033v1 (2018), especially Corollaries 3.2–3.3, supplies the *prior* pointwise perturbation coefficient involving \(\|(A+B)^{-1}B\|^2\); the differential identity and pointwise bound are credited. The present result optimizes that coefficient exactly over all positive pairs sharing a prescribed spectral interval and proves sharpness with noncommuting two-dimensional pairs; that optimization and explicit two-threshold expression are absent from the inspected paper. Naik–Johnson, arXiv:2607.10166v1 (2026), Section 4, gives conditional norm estimates in a block-complementability framework, not this common spectral-box envelope. Searches for matrix-parallel-sum sensitivity and its aliases and comparisons to accessible historical mathematical claims found no direct covering statement. An equivalent bound in older matrix-inequality or electrical-network literature remains a genuine publication-priority risk; failed search is not proof of novelty.

## Mathematical value — PASS

Parallel sum is a natural effective-conductance and monotone-operator composition. A *uniform* perturbation estimate with only a spectral interval as input is useful when matrix orientation is unknown; pointwise coefficients cannot be evaluated without the full matrices. The formula determines an exact dimension-independent operator invariant, displays a sharp phase transition from commuting to noncommuting extremizers, and determines the precise loss of nonexpansiveness. The sharpness is nontrivial even in dimension two and makes clear why scalar estimates cease to suffice. The result does not address joint two-argument perturbations, singular operators, or separate spectral ranges.

## Closest literature and remaining limitations

The most consequential antecedent is Luo–Song–Xu (arXiv:1806.07033), which already gives the pointwise one-sided perturbation coefficient. The other inspected sources concern qualitative parallel sums and conditional block-operator norm inequalities. Exact publication priority remains unverified, independent audit has not been performed, and the theorem assumes a common strictly positive spectral box.

Self-review: passed. Independent audit: not yet performed.
