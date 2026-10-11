# Independent mathematical audit

## correctness

PASS

The balanced two-site specialization is correct. Symmetry forces each scaling vector to remain a scalar multiple of the all-ones vector, so at effective temperature \(\varepsilon=\eta/p\) the scaled Gibbs kernel is exactly \(Z=[2(1+z)]^{-1}\begin{psmallmatrix}1&z\\z&1\end{psmallmatrix}\), with \(z=e^{-p\Delta/\eta}\), and it already has both target marginals. The primal cost is therefore \(U=\Delta z/(1+z)\). Substitution into the source dual certificate cancels the arbitrary scalar scaling and gives \(L=-(\eta/p)\log(1+z)\). The displayed derivative of \(G=U-L\) has three strictly negative terms, so the stopping-index ceiling formulas and the asymptotic ratio follow. The actual package verifier at blob 4b561642645ad69448db32e1d2d7b5119cd4b34f was inspected and independently reconstructs the same scalar equations; its numerical checks are supplementary to the analytic proof.

## originality

FAIL

The scientific content is mechanically implied by the primary source once its general certificate is specialized to the symmetric two-atom problem. Chin and Schiffer already state the inverse-linear effective-temperature schedules for BDRS and O-BDRS, the matrix-scaling representation, and the anytime primal-dual certificate. On the uniform two-by-two kernel, one row scaling and one column scaling give the displayed plan immediately; zero repair, the scalar upper and lower bounds, and the stopping-count law then require only elementary substitution and one derivative. The absence of the exact closed form from the paper does not make this routine special case original under the implication-based bar.

## value

FAIL

The closed form is a useful unit test for an implementation, but scientifically it is a routine symmetric plug-in to a general certificate specifically designed to be evaluated at each iterate. The exact tolerance ratio is simply the already-published faster effective-temperature schedule passed through a monotone scalar gap. With no new mechanism, boundary, optimality theorem, or nontrivial classification, it does not clear the independent value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
