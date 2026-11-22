# Sharp maximum-entry sensitivity of absolutely monotone matrix functions on positive spectral intervals

## Finding
For every integer \(n\ge1\), every \(b>0\), and every real power series \(f(t)=\sum_{k=0}^{\infty}a_k t^k\) with nonnegative coefficients \(a_k\ge0\) and convergence radius strictly larger than \(b\), let \(\mathcal K_{n,b}=\{A=A^{\mathsf T}:0\preceq A\preceq bI\}\). Define the maximum absolute-entry matrix norm \(\|X\|_{\max}=\max_{i,j}|X_{ij}|\), and \(c_n=(1+\sqrt n)/2\). The exact two-input Lipschitz coefficient is
\[
\sup_{A\ne B\in\mathcal K_{n,b}}\frac{\|f(A)-f(B)\|_{\max}}{\|A-B\|_{\max}}=a_1+\sum_{k=2}^{\infty}a_k b^{k-1}\bigl(2c_n+(k-2)c_n^2\bigr).
\]
In particular, for \(f(t)=t^k\), \(k\ge2\), this is \(b^{k-1}(2c_n+(k-2)c_n^2)\); for \(f(t)=(1-t)^{-1}\) with \(0<b<1\), it is \((1+c_n b/(1-b))^2\). The formula is sharp as a supremum of distinct admissible input pairs; actual finite-pair attainment is not asserted.

## Assumptions and scope
All matrices are real symmetric; positive-semidefinite inequalities are in Loewner order. Input perturbations are symmetric, but the norm is the maximum of their individual entries, not an operator or Schatten norm. The coefficient positivity hypothesis and radius \(>b\) guarantee absolute uniform convergence of the power series and of its derivative on a neighborhood of the specified spectral interval. For \(n=1\), \(c_1=1\) and the result reduces to \(f'(b)\). The bound does not assert anything about general signed-coefficient functions, nonsymmetric matrices, or other matrix norms.

## Proof
**Row lemma.** If a real symmetric matrix satisfies \(0\preceq P\preceq I\), then \(P^2\preceq P\); hence at every row \(i\), \(\sum_{j\ne i}P_{ij}^2\le P_{ii}(1-P_{ii})\). By Cauchy–Schwarz, putting \(q=P_{ii}\in[0,1]\),
\[
\sum_j|P_{ij}|\le q+\sqrt{(n-1)q(1-q)}\le(1+\sqrt n)/2=c_n.
\]
The final bound is the maximum of the explicitly displayed scalar expression. Equality is obtained at \(P=uu^{\mathsf T}\) where \(u\) is the positive unit vector with \(u_1^2=(1+1/\sqrt n)/2\) and all remaining coordinates equal. For \(n=1\), take \(P=[1]\). Therefore every \(0\preceq A\preceq bI\) satisfies \(\|A^j\|_{\infty\to\infty}\le c_n b^j\) for each integer \(j\ge1\); transpose symmetry gives the same column bound.

**Derivative bound.** For \(k\ge1\) and symmetric \(E\), differentiation gives the exact algebraic identity
\[
D(A^k)[E]=\sum_{j=0}^{k-1}A^j E A^{k-1-j}.
\]
If \(\|E\|_{\max}\le1\), the two end terms of the sum for \(k\ge2\) have entries of absolute value at most \(c_n b^{k-1}\) each. Each of its \(k-2\) interior terms has entries at most \(c_n^2 b^{k-1}\), by its two row/column sum bounds. For \(k=1\), the norm is exactly one. Summing the derivative termwise with \(a_k\ge0\) yields the claimed universal upper bound on \(\|Df(A)[E]\|_{\max}\). Integrating along the convex segment between any two matrices in \(\mathcal K_{n,b}\) yields the two-input upper bound.

**Sharpness.** Fix the rank-one projection \(P=uu^{\mathsf T}\) from the row lemma and the all-ones symmetric matrix \(J\). Its row-one sum is \(\sum_jP_{1j}=c_n\); also \((PJP)_{11}=c_n^2\). At \(A=bP\), the \((1,1)\)-entry of \(D(A^k)[J]\) is \(b^{k-1}(2c_n+(k-2)c_n^2)\) for every \(k\ge2\), and the \(k=1\) term equals one. All terms are nonnegative, so the derivative entry for \(f\) equals the full proposed constant. As \(bP\) lies at the boundary, set \(A_\epsilon=(b-\epsilon)P+\epsilon(I-P)\) for \(0<\epsilon<b/2\); then \(0\prec A_\epsilon\prec bI\) and \(Df(A_\epsilon)[J]\to Df(bP)[J]\). For each \(\epsilon\) take sufficiently small \(h>0\) so \(A_\epsilon+hJ\in\mathcal K_{n,b}\). The distinct-pair ratio converges first as \(h\downarrow0\) and then \(\epsilon\downarrow0\) to the lower bound. Thus it matches the universal upper bound.

**Resolvent specialization.** For \(0<b<1\), insert \(a_k=1\) to sum the two geometric series: \(1+2c_n b/(1-b)+c_n^2b^2/(1-b)^2=(1+c_n b/(1-b))^2\).

## Verification
The accompanying `check.py` verifies the projection row extremizer, exact rank-one directional derivative formula for matrix powers, resolvent derivative identity, and randomly sampled interior two-input inequalities. These finite checks are secondary to the algebraic proof and do not certify the infinitely many matrices or series. Run `python check.py` with NumPy installed; no network access or external data are needed.

## Relationship to prior work
Matrix-function Fréchet derivatives and their computation are developed in Kandolf–Koskela–Relton–Schweitzer (2020 preprint, 2021 publication); their full open-access treatment is algorithmic and uses norm-dependent condition estimation, without this sharp maximum-entry spectral-interval formula. Crouzeix–Kressner (2020) gives bivariate spectral-norm derivative control, rather than the current maximum-entry norm and positive-coefficient extremizers. An existing sharp bound for positive mixtures of exponentials on **negative half-line** spectral domains yields upper bounds after translating an interval but does not imply the present exact *two-sided constrained* coefficient: the latter requires preserving the lower positive-semidefinite cap and has, for the resolvent, the distinct constant \((1+c_n b/(1-b))^2\). The elementary sharp row-contraction bound is an ingredient, not itself a full matrix-function derivative classification.

## Limitations
No claim is made for signed Taylor coefficients, general operator-monotone functions, arbitrary matrix entries restricted independently without spectral constraints, or complex nonsymmetric matrices. The supremum may not be achieved by two distinct matrices; the proof uses an interior approximation. The prior-art search is not a proof of worldwide novelty, and independent mathematical validation has not been performed.

## References
1. P. Kandolf, A. Koskela, S. D. Relton, M. Schweitzer, *Computing low-rank approximations of the Fréchet derivative of a matrix function using Krylov subspace methods*, arXiv:2008.12926 (first posted 2020-08-29), https://arxiv.org/abs/2008.12926; open-access full text https://onlinelibrary.wiley.com/doi/full/10.1002/nla.2401.
2. M. Crouzeix, D. Kressner, *A bivariate extension of the Crouzeix–Palencia result with an application to Fréchet derivatives of matrix functions*, arXiv:2007.09784 (first posted 2020-07-19), https://arxiv.org/abs/2007.09784.
