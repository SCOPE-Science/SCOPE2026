# Scientific review: centered Euclidean group soft thresholding

## Correctness — PASS

The explicit proximal identity follows from an orthogonal split into constants and the centered subspace. At nonzero active contrast the Jacobian is a convex combination of the identity on contrasts and a rank-one orthogonal projector. For a path, quotient variation is precisely the \(\ell_1\) norm of first differences, permitting a reduction of every rank-one norm to step directions and edge-sign vectors. The exact symmetric two-vector eigenvalue identity, \(\|D^{\mathsf T}\varepsilon\|_2^2\le4n-6\), and \(\|Qh^{(j)}\|_2^2=j(n-j)/n\) reconstruct the formula without numerical assumptions. Alternating edge signs and a middle step give an explicit sharp family. Strict derivative bounds at every finite positive-contrast point prove nonattainment for \(n\ge3\), while zero penalty and the two-coordinate case have equality witnesses. The all-dimension proof is independent of the finite checker.

## Originality — PASS, with stated historical risk

The full technical discussion of the Euclidean prox map in Argyriou et al., arXiv:1104.1436, gives the underlying radial rule but not a path-variation coefficient. The full group-lasso calculations in Friedman–Hastie–Tibshirani, arXiv:1001.0736, concern orthonormal regression blocks rather than variation of two filtered inputs. Chambolle–Pock (2016), sections 2–3, gives Hilbertian proximal nonexpansivity and discrete-variation context, not the precise mean-preserving, cross-norm, finite-path constant. The Yuan–Lin (2005) full text could not be examined; only publisher metadata and abstract were available. That source is relevant historical background and is not asserted to be absent of any result based solely on its abstract. Searches for radial/group shrinkage, prox operators, finite-path variation, equivalent rank-one projection norms and stronger nonexpansivity assertions found no primary result covering the specific formula, the finite-attainment distinction, or its zero-penalty transition. These comparisons justify a qualified originality conclusion, not a guarantee of global priority.

## Value — PASS

Euclidean group soft thresholding is a canonical proximal building block; preserving the mean makes path variation a meaningful perturbation seminorm. The result identifies a substantive failure of Hilbert stability to transfer to the BV geometry: the exact factor scales linearly with dimension, is strictly unattained for each positive threshold when there are at least three coordinates, and disappears discontinuously if the penalty is set to zero. An explicit extremizing geometry identifies alternating gradients and a central step as the mechanism, and supplies sharp finite-dimensional benchmarks. This addresses a natural structural stability question rather than a prescribed small numerical slice.

## Limits and source risks

The proof applies to one global mean-centered Euclidean shrinkage group on a nonperiodic uniformly weighted path. General graph variations, several overlapping groups and other proximal penalties are unproved. Finite computations only corroborate arithmetic and boundary limits. Earlier unindexed notes or inaccessible primary full texts may limit a historical priority claim.

Self-review: passed. Independent audit: not yet performed.
