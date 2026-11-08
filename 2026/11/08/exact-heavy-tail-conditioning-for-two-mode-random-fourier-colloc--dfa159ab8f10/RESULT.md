# Exact heavy-tail conditioning for two-mode random Fourier collocation

## Finding
For every integer \(m\ge 2\), let \(X_1,\ldots,X_m\) be independent and uniform on the circle \([0,2\pi)\), and take two distinct integer Fourier frequencies \(k_1,k_2\). Define the complex collocation matrix \(A\in\mathbb C^{m\times2}\) by
\[
A_{j\ell}=e^{ik_\ell X_j},\qquad 1\le j\le m,\quad \ell\in\{1,2\}.
\]
For its spectral condition number \(\kappa=\sigma_{\max}(A)/\sigma_{\min}(A)\), the **exact high-condition-number tail** is
\[
\boxed{\lim_{t\to\infty}t^{m-1}\Pr(\kappa>t)=C_m,
\qquad C_m=\frac{m^{m/2}}{\pi^{(m-1)/2}\Gamma((m+1)/2)}.}
\]
The matrix is full column rank almost surely; the distribution of \(\kappa\) is identical for every nonzero integer frequency separation. In particular, for every real \(q>0\),
\[
\boxed{\mathbb E\,\kappa^q<\infty\quad\Longleftrightarrow\quad q<m-1.}
\]
This remains true if \(k_1,k_2\) themselves are random, provided they are almost surely distinct integers and independent of the sample points. With two samples an exact formula holds for all \(t\ge1\):
\[
\Pr(\kappa>t)=\frac4\pi\arctan\frac1t.
\]
Thus two samples give infinite expected condition number, three samples give finite mean but infinite second moment, and four samples yield a finite second moment. The condition number of the normal-equations Gram matrix has moment threshold \((m-1)/2\), rather than \(m-1\).

## Assumptions and scope
The rows are independent samples from uniform Haar measure on the full period, the two columns are unweighted complex exponentials at distinct integer frequencies, all computations use the Euclidean spectral norm, and \(m\) is fixed as the tail threshold \(t\to\infty\). There is no regularization, derivative operator, discretization boundary or additive noise. The resulting law is an exact property of this structured random sampling model, not a generic distribution-free statement about arbitrary random-feature matrices.

## Proof
**Step 1: reduction to uniform phase differences.** Put \(d=k_2-k_1\in\mathbb Z\setminus\{0\}\) and \(\theta_j=dX_j\pmod{2\pi}\). Multiplication by a nonzero integer preserves Haar measure on the circle, so the \(\theta_j\) remain independent and uniform. The Gram matrix and its two eigenvalues are
\[
A^*A=\begin{pmatrix}m&S\\\overline S&m\end{pmatrix},\quad
S=\sum_{j=1}^m e^{i\theta_j},\qquad
\lambda_{\pm}=m\pm|S|.
\]
Since all phases coincide only on a Haar-null subset for \(m\ge2\), \(|S|<m\) almost surely. Consequently
\[
\kappa^2=\frac{m+|S|}{m-|S|}.
\]
This proves full rank and frequency-gap invariance, also after conditioning on any independently randomized distinct integer frequency pair.

**Step 2: isolate the only singular configuration.** Rotation does not change \(|S|\). The phase differences \(v=(\theta_2-\theta_1,\ldots,\theta_m-\theta_1)\) modulo \(2\pi\) are uniformly distributed on the \((m-1)\)-torus, with constant density \((2\pi)^{-(m-1)}\). Equality \(|S|=m\) occurs exactly when \(v=0\) on this torus. By compactness, for every neighborhood of this single point, \(\kappa\) is bounded on the complementary compact set. Large-\(t\) events therefore lie entirely in an arbitrarily small local neighborhood of the origin.

**Step 3: quadratic local geometry.** Write \(r=m-1\), identify \(v\) with a small real vector in \((-\pi,\pi)^r\), and let \(B=I_r-\mathbf1\mathbf1^\mathsf T/m\). With \(v_1=0\), the exact identity
\[
m^2-|S|^2=2\sum_{1\le i<j\le m}(1-\cos(v_i-v_j))
\]
and Taylor's theorem yield
\[
m-|S|=\frac12v^\mathsf TBv+O(\|v\|^4),\qquad
\kappa^2=\frac{4m}{v^\mathsf TBv}\bigl(1+O(\|v\|^2)\bigr).
\]
Here \(B\) is positive definite: its eigenvalues are \(1\), with multiplicity \(m-2\), and \(1/m\), once. In particular, \(\det B=1/m\). The asymptotic remainder is uniform as \(v\) approaches zero. Given any fixed \(\varepsilon>0\), sufficiently near the origin the event \(\kappa>t\) is trapped between the ellipsoids
\[
v^\mathsf TBv<\frac{4m(1-\varepsilon)}{t^2}
\quad\text{and}\quad
v^\mathsf TBv<\frac{4m(1+\varepsilon)}{t^2}
\]
for all sufficiently large \(t\). The two bounds have volumes that converge to one another as \(\varepsilon\downarrow0\).

**Step 4: exact leading measure.** The \(r\)-dimensional ellipsoid \(v^\mathsf TBv<4m/t^2\) has volume
\[
\frac{\pi^{r/2}}{\Gamma(r/2+1)}\frac{(4m)^{r/2}}{t^r\sqrt{\det B}}.
\]
Multiplying by the torus density \((2\pi)^{-r}\), substituting \(\det B=1/m\), and squeezing by Step 3 gives
\[
\lim_{t\to\infty} t^r\Pr(\kappa>t)
=\frac{m^{m/2}}{\pi^{r/2}\Gamma(r/2+1)}=C_m>0.
\]
This proves the constant and exponent for every fixed \(m\ge2\), not merely along a subsequence.

**Step 5: moments and the two-sample formula.** For any nonnegative random variable and \(q>0\), tail integration gives \(\mathbb E\kappa^q=q\int_0^\infty t^{q-1}\Pr(\kappa>t)\,dt\). The positive finite tail constant gives convergence precisely when \(q<m-1\) and logarithmic divergence at equality. Because \(\kappa_2(A^*A)=\kappa^2\), its positive moments have threshold \((m-1)/2\). When \(m=2\), set \(\Delta=\theta_2-\theta_1\pmod{2\pi}\). Then \(|S|=2|\cos(\Delta/2)|\), and for \(t\ge1\),
\[
\Pr(\kappa>t)=\frac2\pi\arccos\frac{t^2-1}{t^2+1}
=\frac4\pi\arctan\frac1t.
\]
This also independently verifies \(C_2=4/\pi\).

## Verification
Run the complete standalone standard-library script with `python3 verify.py`. It checks exact rational determinants and phase-difference quadratic identities for eleven sample sizes, evaluates the exact \(m=2\) distribution against angular quadrature, compares deterministic torus integrals for \(m=3\) to the sharp constant, and tests the local expansion. Successful replay reports `VERIFY_OK` and the number of check groups. These finite computations support the algebraic reduction; only the preceding proof establishes the infinite tail law and moment cutoff.

## Relationship to prior work
Ming and Yu [1], especially Section 5 and Appendix E, prove rapidly decaying high-index singular values and large condition-number lower bounds for broad Fourier-feature PDE collocation matrices. Their results require a growing collection of features and do not give an exact probability tail or moment threshold for the two-column, uniformly sampled Fourier design above. Their earlier one-dimensional analysis [2] likewise treats the feature-rich PDE matrix setting. Tucci and Whiting [3] investigate random Vandermonde eigenvalues, including inverse behavior and square large-dimensional ensembles, but not this fixed-two-column, variable-row ensemble with exact tail constant. Kunis and Nagel [4] obtain deterministic conditioning bounds for nearly colliding Vandermonde nodes, rather than the present probability law for independently uniform sampling points. The two-column Gram identity is elementary and is used without novelty claim; the asserted contribution is the full sharp tail coefficient, moment threshold for every sample count, and frequency-gap invariance under the specified sampling law.

## Limitations
No statement is made for nonuniform or dependent sampling nodes, noninteger frequencies, more than two Fourier modes, real-only sine/cosine columns, weighted observations, derivative-collocation matrices, or regularized least squares. A heavy tail need not imply poor typical conditioning; it describes rare configurations in the exact model. Historical priority cannot be certified exhaustively, especially for results under alternative terminology such as Steinhaus sums or small-ball estimates. Independent mathematical audit has not been performed.

## References
[1] P. Ming and H. Yu, *Spectral Convergence of Random Feature Method in Multiple Dimensions*, arXiv:2609.03401v1 (first publicly available 2026-09-03), https://arxiv.org/abs/2609.03401 .

[2] P. Ming and H. Yu, *Spectral connvergece of random feature method in one dimension*, arXiv:2507.07371 (first publicly available 2025-07-10), https://arxiv.org/abs/2507.07371 .

[3] G. H. Tucci and P. A. Whiting, *Asymptotic Behavior of the Maximum and Minimum Singular Value of Random Vandermonde Matrices*, arXiv:1202.3184, https://arxiv.org/abs/1202.3184 .

[4] S. Kunis and D. Nagel, *On the condition number of Vandermonde matrices with pairs of nearly-colliding nodes*, *Numerical Algorithms* 87, 473–496 (2021); public online 2020-07-21, https://doi.org/10.1007/s11075-020-00974-x .
