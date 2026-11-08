# Sharp one-node Gaussian Lanczos log-determinant bias and a multiplicity crossover

## Finding

Let \(n\ge 2\), \(\kappa>1\), and let \(A\) range over real symmetric positive-definite \(n\times n\) matrices with spectral condition number at most \(\kappa\). For \(g\sim\mathcal N(0,I_n)\), the one-node stochastic Lanczos quadrature estimate of the log-determinant is
\[
Q_1(g;A)=\|g\|_2^2\log\!\left(\frac{g^\mathsf T A g}{g^\mathsf T g}\right).
\]
Write its signed expectation bias as \(B(A)=\mathbb E Q_1(g;A)-\log\det A\). For \(1\le j<n\), define
\[
B_j(n,\kappa)=n\int_0^1\log(1+(\kappa-1)t)\,
\frac{t^{j/2-1}(1-t)^{(n-j)/2-1}}{\mathrm B(j/2,(n-j)/2)}\,dt-j\log\kappa.
\]
Then the sharp bound is
\[
0\le B(A)\le \max_{1\le j<n}B_j(n,\kappa).
\]
For \(\kappa>1\), every maximizer on this matrix class has, up to orthogonal similarity and common positive scaling, exactly \(j\) eigenvalues equal to \(\kappa\) and \(n-j\) equal to \(1\), with \(j\) maximizing the finite expression above. The bias is strictly positive for every nonscalar \(A\).

In dimension two the sharp value simplifies to
\[
\max_A B(A)=4\log\cosh\!\left(\frac{\log\kappa}{4}\right).
\]
For fixed \(n\), as \(\delta=\log\kappa\downarrow0\),
\[
B_j(n,e^\delta)=\frac{j(n-j)}{2(n+2)}\delta^2+
\frac{j(n-j)(n-2j)}{6(n+2)(n+4)}\delta^3+O_n(\delta^4).
\]
Consequently, for all sufficiently small positive \(\delta\), the unique maximizing multiplicity is \(j=\lfloor n/2\rfloor\). As \(\kappa\to\infty\),
\[
B_j(n,\kappa)=(n-j)\log\kappa+
 n\bigl[\psi(j/2)-\psi(n/2)\bigr]+o(1),
\]
where \(\psi\) is the digamma function; the unique maximizing multiplicity is then \(j=1\). Thus every fixed dimension \(n\ge4\) has at least one crossover of the worst-case spectral multiplicity as conditioning increases. Neither uniqueness nor monotonicity of the crossover is claimed.

## Assumptions and scope

The Gaussian probe has independent standard normal coordinates, the matrix is deterministic and strictly positive-definite, and computation is in exact arithmetic. One Lanczos iteration produces the scalar Ritz value \(g^\mathsf T A g/\|g\|_2^2\). The spectral condition number is the ratio of maximum to minimum eigenvalue. The integral is well defined at its beta-density endpoints; \(\mathrm B\) denotes the Euler beta function. At \(A=aI_n\) the bias is zero, and at \(\kappa=1\) it vanishes identically by continuity. The variance and probability tails of \(Q_1\) are not asserted.

## Proof

**(1) Exact angular expectation.** Orthogonally diagonalize \(A\) and write \(g=Ru\), where \(u\) is Haar uniform on the unit sphere and \(R^2=\|g\|_2^2\) is independent of \(u\), with \(\mathbb E R^2=n\). The coordinates \(w_i=u_i^2\) sum to one and have the Dirichlet distribution with all parameters \(1/2\). If the eigenvalues are \(\lambda_i=e^{x_i}\), then
\[
B(A)=n\mathbb E_w\log\!\left(\sum_{i=1}^n w_i e^{x_i}\right)-\sum_{i=1}^n x_i.
\]
Indeed, \(\log\det A=\sum_i x_i\) and the radius factors independently. The expression is invariant under a common additive shift of the \(x_i\).

**(2) Sharp endpoint reduction.** For every fixed \(w\) with all coordinates positive, Jensen's inequality gives
\[\log\!\left(\sum_i w_i e^{x_i}\right)\ge\sum_i w_i x_i.\]
Using \(\mathbb E w_i=1/n\), this proves \(B(A)\ge0\), strictly for nonscalar \(A\). Translate the logarithmic eigenvalues so that their minimum is zero. The condition-number restriction places all \(x_i\) in the box \([0,\log\kappa]^n\). For each \(i\), let \(p_i=w_i e^{x_i}/\sum_k w_k e^{x_k}\). Then
\[
\frac{\partial^2 B}{\partial x_i^2}=n\mathbb E[p_i(1-p_i)]>0,
\]
because \(0<p_i<1\) almost surely when \(n\ge2\). Thus \(B\) is strictly convex separately in each coordinate. Iteratively moving coordinates to an endpoint cannot decrease the bias, and no interior coordinate can occur in a global maximizer. The endpoint cases with all eigenvalues equal have zero bias; all other endpoints have \(j\) upper eigenvalues, \(1\le j<n\).

**(3) Evaluation on endpoint spectra.** At an endpoint with \(j\) upper eigenvalues, \(T=\sum_{i=1}^{j}w_i\) has the beta law \(\operatorname{Beta}(j/2,(n-j)/2)\). Consequently the bias is precisely \(B_j(n,\kappa)\). This proves the finite maximum and all equality cases.

**(4) Two-dimensional closed form.** For \(n=2,j=1\), \(T\) has the arcsine law. Setting \(t=\sin^2\theta\) gives
\[
\mathbb E\log(1+(\kappa-1)T)
=\frac2\pi\int_0^{\pi/2}\log(1+(\kappa-1)\sin^2\theta)\,d\theta
=2\log\!\left(\frac{1+\sqrt\kappa}{2}\right).
\]
Substitution in \(B_1\) yields the stated hyperbolic-cosine formula.

**(5) Low-condition-number expansion.** Put \(\delta=\log\kappa\). The first three derivatives at \(\delta=0\) of \(\log(1+(e^\delta-1)T)\) are \(T\), \(T(1-T)\), and \(T(1-T)(1-2T)\). The beta moments are
\[
\mathbb ET=\frac jn,\qquad
\mathbb E[T(1-T)]=\frac{j(n-j)}{n(n+2)},\qquad
\mathbb E[T(1-T)(1-2T)]=\frac{j(n-j)(n-2j)}{n(n+2)(n+4)}.
\]
Taylor expansion cancels the linear term and gives the displayed formula. Among integer \(1\le j<n\), \(j(n-j)\) is maximized uniquely at \(n/2\) when \(n\) is even. When \(n\) is odd, the only second-order tie is between \((n-1)/2\) and \((n+1)/2\), and the third-order term is strictly larger for the smaller choice. Thus the small-\(\delta\) maximizer is unique and equals \(\lfloor n/2\rfloor\).

**(6) High-condition-number expansion.** Rewrite
\[
\log(1+(\kappa-1)T)=\log\kappa+\log\!\left(T+\frac{1-T}{\kappa}\right).
\]
As \(\kappa\to\infty\), the second term decreases to \(\log T\). Its absolute value is bounded by \(|\log T|\), which is integrable for the beta parameters here. Dominated convergence gives \(\mathbb E\log T=\psi(j/2)-\psi(n/2)\), proving the expansion. For fixed \(n\), its leading slope is \(n-j\), uniquely largest at \(j=1\). This proves the eventual singleton maximizer and, for \(n\ge4\), existence of at least one multiplicity change.

## Verification

Run `python3 verify.py` in the directory containing this manuscript. The standalone Python standard-library script evaluates the beta integral by angular Simpson quadrature, checks the dimension-two closed form, tests endpoint spectra and sampled interior spectra, compares maximizing multiplicities across conditioning ranges, and cross-checks with seeded Gaussian simulations. The exact analytical proof above, not finite computation or simulation, establishes the universal statements. A successful run reports `VERIFY_OK 3934` and prints five sample dimension/conditioning cases.

## Relationship to prior work

Stochastic Lanczos quadrature approximates matrix-function quadratic forms using Gaussian quadrature, as treated by Ubaru, Chen, and Saad (2017). Cortinovis and Kressner (2022) analyze randomized trace estimation and log-determinants, while Cortinovis and Toni (2026) discuss employing a single Gaussian probe with several Lanczos iterations. Mbingui, Tambue, and Karambal (first public June 5, 2026) develop stochastic Krylov techniques for large-scale log-determinants. These sources motivate this analysis, but their inspected materials do not supply the present condition-number-sharp *one-node expectation-bias* optimization, its beta-integral extremizers, or its near- versus far-conditioned multiplicity crossover. The Mbingui–Tambue–Karambal complete preprint was not available for line-by-line inspection; its abstract and algorithm description were reviewed, so historical priority remains qualified.

## Limitations

The bound concerns the expected signed error of exactly one Lanczos quadrature node with an unnormalized Gaussian probe. It is not a high-probability absolute-error guarantee, and it is not a guarantee for every realization. The theorem does not cover non-Gaussian probe distributions, multiple Lanczos iterations, finite-precision roundoff, or the stochastic trace-estimation variance. Earlier equivalent formulations of a log-sum-exp spectral extremum might exist outside inspected sources. An independent mathematical audit has not been performed.

## References

1. V. R. Mbingui, A. Tambue, and I. Karambal, *Optimal Stochastic Krylov based Techniques for Large-Scale Log-Determinant Estimation*, arXiv:2606.07004, first submitted June 5, 2026. https://arxiv.org/abs/2606.07004
2. S. Ubaru, J. Chen, and Y. Saad, *Fast Estimation of tr(f(A)) via Stochastic Lanczos Quadrature*, SIAM Journal on Matrix Analysis and Applications 38 (2017), 1075–1099. https://doi.org/10.1137/16M1104974
3. A. Cortinovis and D. Kressner, *On Randomized Trace Estimates for Indefinite Matrices with an Application to Determinants*, Foundations of Computational Mathematics 22 (2022). https://doi.org/10.1007/s10208-021-09525-9
4. A. Cortinovis and D. Toni, *Detecting When One Probe Vector is Enough for Preconditioned Log-Determinant Approximation*, Numerical Linear Algebra with Applications 33 (2026), e70106. https://doi.org/10.1002/nla.70106
