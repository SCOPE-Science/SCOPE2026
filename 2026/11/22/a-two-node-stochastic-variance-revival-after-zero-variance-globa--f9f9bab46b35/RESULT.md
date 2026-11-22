# A two-node stochastic-variance revival after zero-variance global Lanczos correction

## Finding

For every integer \(n\ge3\) and any number \(s\ge1\) of independent Rademacher probes, the full-size (identity-started) global-Lanczos/Hermite-corrected estimator of \(\operatorname{tr}(A^{-1})\) can have **zero sampling variance at one global Lanczos node and strictly positive variance at two nodes**, even while the deterministic global-Lanczos trace error strictly decreases. An explicit real symmetric positive-definite family with spectral condition number \(9/4\) exhibits an exact finite-sample binomial law at two nodes. For every \(n\ge3\), arbitrarily large two-node/one-node variance ratios persist under irreducible positive-definite tridiagonal perturbations with condition number less than \(3\). Dimension \(3\) is the smallest dimension in which this two-depth reversal is possible.

Set, for \(n\ge3\),
\[
A_n(0)=\begin{pmatrix}13/8&5/8\\5/8&13/8\end{pmatrix}\oplus[5/4]\oplus(3/2)I_{n-3}.
\]
Let \(\widehat T_{m,s}\) denote the exact-residual GLHutch estimator described below, \(m=1,2\). Then
\[
\operatorname{Var}(\widehat T_{1,s})=0,\qquad
\operatorname{Var}(\widehat T_{2,s})=\frac{\Delta_n^2}{s},\qquad
\Delta_n=\frac{35(3n-7)(33n-49)}{9(153n-49)^2}>0.
\]
Indeed, for independent equiprobable signs \(\xi_1,\ldots,\xi_s\),
\[
\widehat T_{2,s}-\operatorname{tr}(A_n(0)^{-1})
=-\frac{\Delta_n}{s}\sum_{j=1}^s\xi_j.
\]
Meanwhile the deterministic quadrature deficits at nodes one and two are respectively
\[
E_1=\frac{11}{45},\qquad
E_2=\frac{213n-539}{45(153n-49)},\qquad 0<E_2<E_1.
\]

## Assumptions and scope

All matrices, Lanczos operations, matrix functions and residual quadratic forms are evaluated in exact arithmetic. For a symmetric positive-definite \(A\in\mathbb R^{n\times n}\), apply **scalar-coefficient full-size global Lanczos starting from \(B=I_n\)** with Frobenius inner product. Its \(m\) Gauss nodes are the roots of the monic orthogonal polynomial \(q_m\) for the counting spectral measure \(\nu_A=n^{-1}\sum_{i=1}^n\delta_{\lambda_i(A)}\). Let \(h_m\) be the degree-at-most-\(2m-1\) Hermite interpolant of \(f(x)=1/x\) at those nodes, and put \(M_m=A^{-1}-h_m(A)\). Let \(\psi_m=\operatorname{tr}(h_m(A))\) be the exact full-size global-Lanczos Gauss trace approximation. The **idealized** corrected estimator is
\[
\widehat T_{m,s}=\psi_m+\frac1s\sum_{j=1}^s z_j^{\mathsf T}M_m z_j,
\quad z_j\in\{-1,+1\}^n\text{ with independent fair coordinates}.
\]
The phrase "exact residual" means there is no additional inner Krylov approximation error. The same argument applies for separately sampled independent probe sets at each node count; no between-depth coupling is required for the variance comparison. A positive integer \(s\) is arbitrary and held fixed between depth one and depth two. The phrase "variance" always refers to Rademacher sampling variance, not the deterministic Gauss error or a Gaussian-probe variance.

For the irreducible extension, define the symmetric path adjacency \(K_n=\sum_{i=2}^{n-1}(e_i e_{i+1}^{\mathsf T}+e_{i+1}e_i^{\mathsf T})\) with one-based indices and put \(A_n(t)=A_n(0)+tK_n\).

## Proof

**1. Exact inverse Hermite remainder.** For any positive spectrum and any monic \(q_m\) whose \(m\) roots are positive Gauss nodes, the polynomial
\[
h_m(x)=\frac{1-q_m(x)^2/q_m(0)^2}{x}
\]
has degree at most \(2m-1\) because the numerator vanishes at \(x=0\). At every Gauss node, \(1/x-h_m(x)\) has a double zero. Thus this is the required Hermite interpolant and
\[
M_m=\frac{q_m(A)^2A^{-1}}{q_m(0)^2}\succeq0.
\tag{1}
\]
Global-Lanczos Gauss quadrature is exact for polynomials of degree at most \(2m-1\), whence \(\psi_m=\operatorname{tr}(h_m(A))\) and \(E_m=\operatorname{tr}(M_m)\). Moreover, for a real symmetric matrix \(M\), independent fair-sign probes satisfy
\[
\operatorname{Var}\!\left(\frac1s\sum_{j=1}^s z_j^{\mathsf T}Mz_j\right)
=\frac4s\sum_{1\le i<j\le n}M_{ij}^2.
\tag{2}
\]

**2. The global polynomials.** The eigenvalues of \(A_n(0)\) are \(1,5/4,9/4\), together with \(n-3\) copies of \(3/2\). Their first three sums are
\[
\sum_i\lambda_i=\frac{3n}{2},\quad
\sum_i\lambda_i^2=\frac{18n+7}{8},\quad
\sum_i\lambda_i^3=\frac{108n+135}{32}.
\]
Orthogonality against constants and linear polynomials yields
\[
q_1(x)=x-\frac32,\qquad
q_2(x)=x^2-\frac{93}{28}x+\frac{153n-49}{56n}.
\tag{3}
\]
There are at least three distinct eigenvalues, so two global iterations exist without breakdown. Inserting \(q_1\) into (1) gives
\[
M_1=\operatorname{diag}(1/9,1/9,1/45,0,\ldots,0).
\tag{4}
\]
It follows from (2) that the one-node corrected estimator equals \(\operatorname{tr}(A^{-1})\) for every choice of sign probes, although \(\operatorname{tr}(M_1)=11/45\).

**3. Exact two-node sign law.** For each scalar spectral value \(x>0\), write
\[
r_2(x)=\frac{q_2(x)^2}{xq_2(0)^2}.
\]
Direct substitution from (3) gives
\[
r_2(1)=\left(\frac{23n-49}{153n-49}\right)^2,\qquad
r_2(9/4)=\frac49\left(\frac{18n-49}{153n-49}\right)^2,
\]
and their difference factors as
\[
r_2(1)-r_2(9/4)
=\frac{35(3n-7)(33n-49)}{9(153n-49)^2}=\Delta_n>0.
\tag{5}
\]
The first two-coordinate block has the eigenvectors \((1,-1)^{\mathsf T}/\sqrt2\) at eigenvalue \(1\) and \((1,1)^{\mathsf T}/\sqrt2\) at eigenvalue \(9/4\). As (1) is a function of \(A\), its *only* nonzero off-diagonal entries are
\[
(M_2)_{12}=(M_2)_{21}=-\frac{\Delta_n}{2}.
\]
Hence \(z^{\mathsf T}M_2z=\operatorname{tr}(M_2)-\Delta_nz_1z_2\). The products of two independent signs are independent fair signs across probes, proving the stated exact law and variance. Summing \(r_2\) on the spectrum gives
\[
\operatorname{tr}(M_2)=\frac{213n-539}{45(153n-49)}.
\]
It is positive and smaller than \(11/45\) for all \(n\ge3\), with the strict difference \(98n/[3(153n-49)]\).

**4. Arbitrarily large inflation on irreducible tridiagonal matrices.** For \(0<t<1/16\), \(A_n(t)\) is tridiagonal with every adjacent off-diagonal nonzero and is irreducible. By \(\|K_n\|_2\le2\) and Weyl's bound, its spectrum lies in \([1-2t,9/4+2t]\), so it is positive definite and \(\kappa_2(A_n(t))<(9/4+1/8)/(1-1/8)=19/7<3\). Both Hermite residuals depend analytically on sufficiently small \(t\), since their spectral-moment denominators and \(q_m(0)\) are nonzero at zero. At \(t=0\), every off-diagonal of \(M_1(t)\) vanishes. Yet
\[
\left.\frac{d}{dt}(M_1(t))_{23}\right|_{t=0}=-\frac2{15}
\quad(n=3),\qquad
\left.\frac{d}{dt}(M_1(t))_{34}\right|_{t=0}=-\frac4{45}
\quad(n\ge4).
\]
These follow by differentiating \(M_1(t)=A_n(t)^{-1}-4I/3+4A_n(t)/9\) and using \((A^{-1})'=-A^{-1}K_nA^{-1}\). Consequently \(\operatorname{Var}(\widehat T_{1,s}(t))=c_nt^2/s+o(t^2)\) for some \(c_n>0\), whereas \(\operatorname{Var}(\widehat T_{2,s}(t))\to\Delta_n^2/s>0\). Thus their ratio grows as \(\Theta_n(t^{-2})\). The strict inequality \(E_2<E_1\) persists for sufficiently small positive \(t\), by continuity.

**5. Minimum dimension.** In dimension at most two, the spectral measure has no more than two distinct atoms, so global Lanczos terminates with exact quadrature by its second node. Its two-node Hermite remainder is therefore zero; a zero-to-positive two-node variance reversal is impossible. Dimension three is attained above.

For \(n=3\), the entirely explicit residuals are
\[
M_1=\operatorname{diag}(1/9,1/9,1/45),\qquad
M_2=\frac1{30258}\begin{pmatrix}37&-35&0\\-35&37&0\\0&0&90\end{pmatrix}.
\]
Thus \(E_1=11/45\), \(E_2=2/369\), and one-probe corrected variance at two nodes is exactly \(1225/228886641\).

## Verification

Run the standalone standard-library checker using `python3 verify.py`. It computes the first three exact spectral moments, constructs both exact Hermite residuals by rational matrix algebra, checks their traces and off-diagonal entries in all dimensions \(3\le n\le30\), exhaustively enumerates all sign probes for dimensions \(3\le n\le8\), and checks four irreducible matrix families at three rational perturbation scales. It reported **1360 exact-rational assertions passed**. These finite checks supplement, rather than replace, the proof for arbitrary dimension and asymptotic perturbations.

## Relationship to prior work

Rinelli, Simunec and Vermeiren [1, §2.6, §3.1, §4.1–4.2] introduce and analyze the full-size global-Lanczos Hermite residual and GLHutch correction, including the off-diagonal Rademacher variance formula. The present statement uses their estimator unchanged at the level of an exactly evaluated correction; its claimed addition is an explicit, dimension-minimal *cross-depth reversal*, exact binomial law, and arbitrarily large ratio within well-conditioned irreducible tridiagonal matrices. A reduced deterministic quadrature deficit by itself does not order Rademacher variances because the latter depend on the residual's off-diagonal entries, not only on its trace or eigenvalues.

Hallman and Troester [2] analyze multilevel Chebyshev-based stochastic trace estimators and allocation across approximation levels, but do not determine this identity-started global-Lanczos Hermite residual's exact cross-depth sign-probe distribution. Chen and Hallman [3] develop block-Krylov deflation-based stochastic estimators, not the full-size scalar-coefficient Hermite correction used here. These distinctions concern exact algorithms and the statements inspected, not a proof that no equivalent result exists elsewhere.

## Limitations

The result concerns only \(f(x)=1/x\), precisely specified spectra and small tridiagonal perturbations, real symmetric positive-definite matrices and independent Rademacher probes. It uses **exact residual quadratic forms**, so it does not assert failure of an implementation with nonzero inner-Krylov approximation error, nor a general claim that adding global-Lanczos nodes always increases variance. It also does not address Gaussian probes, XTrace/XNysTrace, numerical rounding or optimal runtime budget allocation. The mathematical novelty assessment is literature-limited; an unindexed equivalent spectral-Hermite variance identity remains possible. Independent validation has not been performed.

## References

[1] M. Rinelli, I. Simunec and R. Vermeiren, *Global Lanczos with stochastic error correction for trace estimation of matrix functions*, arXiv:2611.18864v1, first public 2026-11-13, https://arxiv.org/abs/2611.18864.

[2] E. Hallman and D. Troester, *A multilevel approach to stochastic trace estimation*, arXiv:2103.10516v1, https://arxiv.org/abs/2103.10516.

[3] T. Chen and E. Hallman, *Krylov-aware stochastic trace estimation*, arXiv:2205.01736v3, https://arxiv.org/abs/2205.01736.
