# Two sharp sampling-order reversals for three-coordinate descent

## Finding
Consider exact coordinate minimization on the strongly convex quadratic
\[
f_\rho(x)=\tfrac12x^{\mathsf T}H_\rho x,\qquad H_\rho=(1-\rho)I_3+\rho\mathbf1\mathbf1^{\mathsf T},\qquad x^{(0)}=\mathbf1,
\]
where \(-\tfrac12<\rho<1\). Compare one epoch of three coordinate updates using independent uniform selections **with replacement** (RCD) against a uniformly random permutation **without replacement** (RPCD). Let \(X_\rho\) be the final RCD objective and let \(P_\rho\) be the final RPCD objective, which is independent of the sampled permutation. The full law is four equality-pattern classes:

| Sequence class | Number of ordered index triples | Final objective |
|---|---:|---|
| all the same, \(iii\) | 3 | \((1-\rho)(1+2\rho)\) |
| two equal adjacent, \(iij\) or \(ijj\) | 12 | \(\tfrac12(1-\rho)(1+2\rho)(2\rho^2-\rho+1)\) |
| first equals last, \(iji\) | 6 | \(\tfrac12(1-\rho)(1+2\rho)(2\rho^4-\rho^3+\rho^2-\rho+1)\) |
| all distinct, \(ijk\) | 6 | \(P_\rho=\tfrac12\rho^2(1-\rho)(1+2\rho)(2\rho^2-5\rho+5)\) |

Every ordered triple has probability \(1/27\). Consequently, for \(-\tfrac12<\rho\le\tfrac12\), \(X_\rho\ge P_\rho\) almost surely, whereas for \(\tfrac12<\rho<1\),
\[
\Pr(X_\rho<P_\rho)=\frac29,\qquad \Pr(X_\rho=P_\rho)=\frac29,\qquad \Pr(X_\rho>P_\rho)=\frac59.
\]
Thus **the exact stochastic-order threshold is \(\rho=\tfrac12\)**. Above it, neither method first-order stochastically dominates the other, even though every coordinate update is objective-nonincreasing.

The mean difference has a distinct, sharp threshold:
\[
\boxed{\mathbb E X_\rho-P_\rho=\frac{(2-\rho)(1-\rho)^2(1+2\rho)^2(4-5\rho)}{18}.}
\]
In particular, on \(\tfrac12<\rho<\tfrac45\), RCD beats permutation with probability \(2/9\), yet its **mean loss is greater**; at \(\rho=\tfrac45\) their means agree; on \(\tfrac45<\rho<1\), the mean loss for RCD is **smaller**. These statements compare equal numbers of coordinate-gradient evaluations at the same fixed initialization and are not claims about long-run convergence rates.

Within the analogous equicorrelation-and-consensus-initialization family, dimension three is minimal for an RCD realization to beat an all-distinct ordering after one epoch: the one-dimensional case coincides and the two-dimensional case has no improving repeats.

## Assumptions and scope
The parameter satisfies \(-\tfrac12<\rho<1\), so \(H_\rho\) has eigenvalues \(1-\rho\) (multiplicity two) and \(1+2\rho\) (multiplicity one), all positive. Coordinate gradients are exact, all diagonal entries of \(H_\rho\) equal one, and the objective is minimized at zero. A random RCD epoch is **exactly three independent uniform index draws**, including repeated indices; an RPCD epoch is a uniformly drawn permutation of the same three indices. The vectors and objective values are computed after precisely three successive updates. There is no additional step-length or line-search parameter.

## Proof
For each coordinate \(i\in\{1,2,3\}\), exact coordinate minimization is the linear map
\[
U_i x=x-e_i(H_\rho x)_i,
\]
because the coordinate second derivative equals one. Consequently, for an ordered triple \((i,j,k)\), the final vector is \(U_kU_jU_i\mathbf1\) and its objective is the corresponding quadratic form. Every permutation of coordinate labels commutes with \(H_\rho\) and fixes the initial vector, so the resulting objective depends only on the equality pattern of the triple.

Take representative zero-indexed coordinate triples \((0,0,0)\), \((0,0,1)\), \((0,1,0)\) and \((0,1,2)\). Direct successive substitution in \(U_i\), with simultaneous relabeling allowed, gives respectively the terminal vectors
\[
(-2\rho,1,1),\quad (-2\rho,\rho(2\rho-1),1),
\]
\[
(-\rho(2\rho^2-\rho+1),\rho(2\rho-1),1),\quad
(-2\rho,\rho(2\rho-1),-\rho^2(2\rho-3)).
\]
For a triple with adjacent equal indices, its second consecutive update is idempotent: \(U_i^2=U_i\), so \(iij\) and \(ijj\) have identical values after relabeling. Substituting these four representative vectors into
\[
 f_\rho(v)=\tfrac12\big[(1-\rho)\sum_{a=1}^3v_a^2+\rho(\sum_{a=1}^3v_a)^2\big]
\]
gives exactly the four entries in the table. Counting triples gives \(3\) all-equal, \(12\) adjacent-equal, \(6\) alternating-repeat, and \(6\) all-distinct cases, summing to \(3^3=27\).

Subtracting the all-distinct value \(P_\rho\) from the other three gives the exact factorizations
\[
\begin{aligned}
f_{iii}-P_\rho&=\tfrac12(1-\rho)^2(1+2\rho)^2(\rho^2-2\rho+2),\\
f_{iij}-P_\rho&=\tfrac12(1-\rho)^4(1+2\rho)^2,\\
f_{iji}-P_\rho&=\tfrac12(1-\rho)^2(1+2\rho)^2(1-2\rho).
\end{aligned}
\]
In the stated open positive-definiteness interval, the first two differences are strictly positive (the first has the positive factor \((\rho-1)^2+1\)), while the last has the sign of \(1-2\rho\). Thus the probability comparisons and the two-sided failure of first-order stochastic dominance beyond \(\rho=1/2\) follow exactly. For the latter assertion, one method is deterministic at \(P_\rho\) and the other takes values on both sides with positive probability.

Finally the weighted mean is
\[
\mathbb E X_\rho=\frac{3f_{iii}+12f_{iij}+6f_{iji}+6P_\rho}{27},
\]
which, after factorization, yields the displayed mean-difference formula. All factors except \(4-5\rho\) are positive in the permitted interval; its unique root is \(\rho=4/5\).

For the minimal-dimension assertion, take the two-dimensional equicorrelation Hessian \(\begin{psmallmatrix}1&\rho\\\rho&1\end{psmallmatrix}\), \(-1<\rho<1\), initialized at \((1,1)\). Updating both distinct coordinates gives \(\tfrac12\rho^2(1-\rho^2)\), whereas updating the same coordinate twice gives \(\tfrac12(1-\rho^2)\). The latter exceeds the former by \(\tfrac12(1-\rho^2)^2>0\). In one dimension both protocols are identical. This proves minimality **within this specific symmetric family**, not among arbitrary positive-definite Hessians.

## Verification
Run `python artifacts/verify.py` (Python 3 and SymPy). The verifier constructs every coordinate update matrix independently, checks the exact symbolic objective of all \(27\) triples, verifies their pattern multiplicities and the three factorizations, computes the exact mean law, tests nine rational correlation parameters across both thresholds, and checks the two-dimensional boundary case. The recorded output is `artifacts/verification.txt`. These finite and symbolic tests corroborate the displayed algebra; the signs and full-parameter conclusions follow from the explicit factorizations in the proof, not from finite sampling.

For instance at \(\rho=3/5\), permutation gives \(6732/15625\) while the alternating-repeat path gives \(5522/15625\); at \(\rho=9/10\), the mean difference is \(-539/225000\).

## Relationship to prior work
Lee and Wright (2016) established exact expected recurrences for random-permutation coordinate descent on permutation-invariant quadratics, as well as the standard RCD/RPCD definitions. Gürbüzbalaban, Ozdaglar, Vanli and Wright (2018) compared convergence performance of the sampling rules on structured, diagonally dominant quadratic problems. Abbaszadehpeivasti, de Klerk and Zamani (2022) gave semidefinite-programming performance analyses for cyclic and randomized coordinate descent. Kim, Lee and Yun (2025) compared contraction-rate bounds for a class of permutation-invariant Hessians. These studies motivate the comparison but address expected objective or multi-epoch convergence guarantees rather than the full finite first-epoch outcome law for the fixed consensus initialization, its sharp pathwise threshold, and the exact \(2/9\) reversal probability. The derived mean identity is not asserted independent of general expectation recurrences in the earlier literature; the outcome distribution and stochastic-order distinction are the target of the finding.

## Limitations
This is a finite three-coordinate model with equal diagonal and off-diagonal Hessian entries and consensus initialization. It does not extend the stochastic-order statements to arbitrary initial vectors, dimension, Hessian, nonquadratic objectives, multiple epochs, or noise. The four pattern classes may yield coincident numerical values at exceptional parameter choices; multiplicities remain correct. The sample realization in which RCD wins is possible despite negative first-epoch expected performance in an interval, not a global algorithm recommendation. Specialist literature may contain equivalent first-epoch distributions; independent publication-priority verification remains outstanding.

## References
- H. Abbaszadehpeivasti, E. de Klerk, M. Zamani, *Convergence rate analysis of randomized and cyclic coordinate descent for convex optimization through semidefinite programming*, first public December 23, 2022, https://arxiv.org/abs/2212.12384 .
- C.-P. Lee and S. J. Wright, *Random Permutations Fix a Worst Case for Cyclic Coordinate Descent*, first public July 28, 2016, https://arxiv.org/abs/1607.08320 .
- M. Gürbüzbalaban, A. Ozdaglar, N. D. Vanli, S. J. Wright, *Randomness and Permutations in Coordinate Descent Methods*, first public March 22, 2018, https://arxiv.org/abs/1803.08200 .
- D. Kim, J. Lee, C. Yun, *Provable Benefit of Random Permutations over Uniform Sampling in Stochastic Coordinate Descent*, first public May 29, 2025, https://arxiv.org/abs/2505.23152 .
