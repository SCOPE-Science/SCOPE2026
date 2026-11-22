# Universal second-mode locking for signed circular Bessel covariances

## Finding

Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), and define
\[
\lambda_*=\frac{5\sqrt{22}-14}{6}=1.5753464665\ldots .
\]
For \(\lambda>0\), \(s>0\), and integers \(n\ge0\), put
\[
a_n=(\lambda+n^2)^{-s},\qquad
R_0=\frac{a_1}{a_0},\qquad
R_n=\frac{a_{n-1}+a_{n+1}}{2a_n}\quad(n\ge1).
\]
**Universal spectral locking theorem.** The second harmonic is the *unique* maximizer of \(R_n\) over all integers \(n\ge0\), simultaneously for **every** \(s>0\), if and only if
\[
\boxed{\frac12\le\lambda\le\lambda_*.}
\]
Within this maximal interval, for all \(s>0\),
\[
\max_{n\ge0}R_n=R_2
=\frac12\left[\left(\frac{\lambda+4}{\lambda+1}\right)^s
+\left(\frac{\lambda+4}{\lambda+9}\right)^s\right]>1.
\]
Outside the interval, the second harmonic ceases to maximize for some positive order: when \(\lambda<1/2\), mode \(1\) beats mode \(2\) for sufficiently large \(s\); when \(\lambda>\lambda_*\), mode \(3\) beats mode \(2\) for sufficiently small \(s>0\).

**Sharp covariance consequence.** If \(s>1/2\) and \(1/2\le\lambda\le\lambda_*\), the uniformly convergent Bessel-potential series
\[
C_{\lambda,s}(t)=\sum_{n\in\mathbb Z}(\lambda+n^2)^{-s}e^{int}
\]
defines a real, continuous, stationary circle kernel. For each real \(b\), the signed harmonic modulation
\[
K_{\lambda,s,b}(x,y)=C_{\lambda,s}(x-y)\,[1+b\cos(x-y)]
\]
is positive semidefinite on every finite circle configuration **if and only if**
\[
\boxed{\displaystyle b\ge b_*(\lambda,s):=-\frac{2}{\left(\frac{\lambda+4}{\lambda+1}\right)^s+\left(\frac{\lambda+4}{\lambda+9}\right)^s}.}
\]
At equality, **exactly** the Fourier coefficients of orders \(\pm2\) vanish; all others are strictly positive, and every finite Gram matrix on pairwise distinct sites is strictly positive definite. For strict inequality, all Fourier coefficients are positive. The boundary kernel is not universal in \(C(\mathbb T)\), while the strict-interior kernels are. In the illustrative case \(\lambda=s=1\), the sharp endpoint is \(b_*=-2/3\).

## Assumptions and scope

The circle has angular period \(2\pi\). All Fourier coefficients use the convention \(C(t)=\sum_{n\in\mathbb Z}\widehat C(n)e^{int}\), with no \(1/(2\pi)\) multiplier in the reconstruction. Real \(b\) includes negative values. The spectral-locking statement concerns positive sequences for all \(s>0\); if \(s\le1/2\), the infinite Fourier series is not absolutely summable and is **not asserted to define a continuous covariance function**. The stationary-kernel assertion requires \(s>1/2\). Distinct-site strictness differs from all-frequency strictness and from density of the reproducing-kernel Hilbert space in continuous functions.

## Proof

**1. Reduction to two ordered logarithmic increments.** Put
\[
u_n=\log\frac{\lambda+n^2}{\lambda+(n-1)^2}\quad(n\ge1).
\]
They are positive, and
\[
R_n=\frac{e^{s u_n}+e^{-s u_{n+1}}}{2}\quad(n\ge1),
\qquad R_0=\left(\frac{\lambda}{\lambda+1}\right)^s<1.
\]
Write
\[
F_n=e^{u_n-u_{n+1}}=
\frac{(\lambda+n^2)^2}{[\lambda+(n-1)^2][\lambda+(n+1)^2]}.
\]
The following elementary two-coordinate comparison is used: if \(X\ge x>0\), \(Y<0\), \(y<0\), and \(X+Y\ge x+y\), then for every \(s>0\), \(e^{sX}+e^{sY}\ge e^{sx}+e^{sy}\). Indeed, if \(Y\ge y\), each term is ordered. Otherwise the gain \(X-x\) is at least the loss \(y-Y\), and its integration interval is strictly to the right of the loss interval, so strict monotonicity of the derivative of \(e^{st}\) gives the assertion. Equality is possible only when both coordinates coincide. Thus it suffices to prove simultaneously that \(u_2\ge u_n\) and \(F_2\ge F_n\) for all \(n\ge1\), with at least one strict for \(n\ne2\).

**2. The exact locking interval.** Direct algebra yields
\[
F_1=\frac{(\lambda+1)^2}{\lambda(\lambda+4)},\qquad
F_2=\frac{(\lambda+4)^2}{(\lambda+1)(\lambda+9)},
\]
and \(F_1\le1\) for \(\lambda\ge1/2\), whereas \(F_2>1\) for \(\lambda<7/2\). Moreover,
\[
F_2-F_3=
\frac{295-140\lambda-30\lambda^2}
{(\lambda+1)(\lambda+4)(\lambda+9)(\lambda+16)}.
\]
The positive root of its numerator is \(\lambda_*=(5\sqrt{22}-14)/6\). To control **all** larger indices, regard \(F_n\) as the restriction of
\[
F(\sqrt y)=\frac{(\lambda+y)^2}{(\lambda+y+1)^2-4y},\quad y\ge0.
\]
Its derivative has the exact sign of \(3\lambda+1-y\), since
\[
\frac{d}{dy}F(\sqrt y)=
\frac{2(\lambda+y)(3\lambda+1-y)}{[(\lambda+y+1)^2-4y]^2}.
\]
For \(1/2\le\lambda\le\lambda_*\), one has \(3\lambda+1<9\); hence \(F_n\) decreases strictly for integers \(n\ge3\). Together with \(F_2\ge F_3\) and \(F_1\le1<F_2\), this proves \(F_2\ge F_n\) for all \(n\ge1\), with a possible equality only at \(n=3,\lambda=\lambda_*\).

Also \(F_n>1\) for every integer \(n\ge2\), because
\[
(\lambda+n^2)^2-[\lambda+(n-1)^2][\lambda+(n+1)^2]
=2n^2-2\lambda-1>0.
\]
Thus \(u_n>u_{n+1}\) for \(n\ge2\). Furthermore \(F_1\le1\) implies \(u_2\ge u_1\). Hence \(u_2\ge u_n\) for every \(n\ge1\), strictly for all \(n\ge3\). The two-coordinate comparison now gives \(R_2>R_n\) for \(n\ge1,\ n\ne2\), including the upper endpoint where \(F_2=F_3\). Finally \(F_2>1\) implies, by arithmetic–geometric mean,
\[
R_2\ge F_2^{s/2}>1>R_0.
\]
This proves the claimed unique maximizer for every positive \(s\).

**3. Maximality.** If \(0<\lambda<1/2\), then \(F_1>1\), equivalently \(u_1>u_2\). As \(s\to\infty\), the leading exponential of \(2R_1\) is \(e^{su_1}\), whereas that of \(2R_2\) is \(e^{su_2}\); therefore \(R_1>R_2\) for all sufficiently large \(s\). If \(\lambda>\lambda_*\), then \(F_3>F_2\), so the one-sided small-order expansion
\[
R_n=1+\frac{s}{2}\log F_n+O_\lambda(s^2),\qquad n\ge1,
\]
shows \(R_3>R_2\) for all sufficiently small \(s>0\). Thus no larger interval of \(\lambda\) can possess universal second-mode locking.

**4. Fourier positivity, singular frequencies, and strictness.** For \(s>1/2\) the base Fourier series converges absolutely. Multiplication by \(1+b\cos t\) produces Fourier coefficients
\[
w_n=a_{|n|}+\frac b2(a_{|n-1|}+a_{|n+1|})
=a_{|n|}(1+bR_{|n|}),\qquad n\in\mathbb Z,
\]
where the \(n=0\) formula uses \(R_0=a_1/a_0\). The Fourier characterization of positive-definite stationary kernels on compact abelian groups is \(w_n\ge0\) for every \(n\). Since the unique maximum of \(R_n\) occurs at \(n=2\), these inequalities are equivalent to \(b\ge -1/R_2\), giving the displayed formula. At equality, \(w_{\pm2}=0\) and \(w_n>0\) otherwise; below it, \(w_{\pm2}<0\). If \(b>-1/R_2\), all Fourier coefficients are positive.

For any \(m\) distinct angles \(t_1,\ldots,t_m\), the boundary Gram quadratic form equals \(\sum_{n\in\mathbb Z}w_n|\sum_{j=1}^m c_je^{int_j}|^2\). If it vanishes, all moments at the consecutive frequencies \(n=3,4,\ldots,m+2\) vanish. The Vandermonde determinant of \(e^{it_1},\ldots,e^{it_m}\) is nonzero, forcing every \(c_j=0\), so the Gram matrix is strictly positive definite. In the interior every character occurs with positive Fourier weight, and trigonometric polynomials lie in the uniform closure of the RKHS; at equality, the missing second-frequency character prevents density. This completes the proof.

## Verification

The standalone file `CHECK.py`, executed with Python 3 and no third-party packages, checked \(9,329\) exact-rational and numerical assertions. Rational arithmetic tested shifted-ratio inequalities and the critical spectral zero at all orders \(s=1,\ldots,6\), for multiple \(\lambda\) in the locking interval and 70 Fourier frequencies. Floating-point tests covered fractional orders, the upper endpoint and both outside-interval failure mechanisms. These bounded tests are **not** a substitute for the universal inequalities and Vandermonde argument proved above.

## Relationship to prior work

The spectral construction is motivated by the Laplace–Beltrami Matérn kernels of Borovitskiy et al. (2020), especially their spectral kernel expression in Theorem 5. Bachmayr et al. (2019) study the periodization and spectra of Matérn covariances. Their primary results do not provide a sign-changing cosine-mask positivity threshold or an all-smoothness active-frequency classification. A separately published 2026 result gives a cutoff and an unbounded Fourier-frequency staircase for a *geodesic exponential* circle kernel, whose coefficients contain an alternating-parity factor and are not the sequence \((\lambda+n^2)^{-s}\); its explicit criterion does not imply the present locking interval. Pure Poisson spectral families and stretched exponential Fourier kernels likewise have different shifted-ratio structure. Novelty is assessed against these concrete implications, not inferred from searches alone.

## Limitations

The sharp interval is maximal for **all** orders \(s>0\); for the restricted covariance regime \(s>1/2\), no claim is made that the interval is maximal. The theorem does not classify the maximizing Fourier mode for all \(\lambda\) outside this interval or for arbitrary higher cosine harmonics. At \(s\le1/2\), no continuous-kernel interpretation is asserted. Bibliographic coverage is limited; an equivalent older result in the literature may exist. No independent mathematical validation has been performed.

## References

1. M. Bachmayr, I. G. Graham, V. K. Nguyen, R. Scheichl, *Unified Analysis of Periodization-Based Sampling Methods for Matérn Covariances*, arXiv:1905.13522, first publicly posted 2019-05-31; SIAM J. Numer. Anal. 58 (2020), 2953–2980; DOI: 10.1137/19M1269877. https://arxiv.org/abs/1905.13522
2. V. Borovitskiy, A. Terenin, P. Mostowsky, M. P. Deisenroth, *Matérn Gaussian Processes on Riemannian Manifolds*, arXiv:2006.10160, first publicly posted 2020-06-17; NeurIPS 33 (2020), Theorem 5. https://arxiv.org/abs/2006.10160
3. *Sharp circle-covariance modulation threshold and an unbounded Fourier-mode staircase*, published research record, 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-circle-covariance-modulation-threshold-and-an-unbounded-fo--3df14ed06eed
