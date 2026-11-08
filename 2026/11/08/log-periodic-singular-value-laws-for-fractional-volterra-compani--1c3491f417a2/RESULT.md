# Log-periodic singular-value laws for fractional Volterra companions on Hardy space

## Finding

For \(0<\eta\le1/2\), there is an absolute \(\epsilon_0>0\) such that for each \(0<\epsilon<\epsilon_0\), a positive radial doubling weight gives a compact fractional Volterra-type operator on \(H^2\) whose singular-value counting function has a nonconstant log-periodic first-order profile. In particular, there is no Weyl coefficient \(\lim_{n\to\infty} n s_n\); nonetheless its logarithmic singular-value average exists and has an explicit elliptic-integral value independent of the oscillation amplitude.

Write \(N(t;T)=\#\{j:s_j(T)>t\}\). With the definitions below, as \(t\downarrow0\),
\[
N(t;T)=\frac{\Psi_{\epsilon,\eta}(\log(1/t))}{t}+o(1/t).
\]
For sufficiently small positive \(\epsilon\), the positive continuous \(2\pi\)-periodic function \(\Psi_{\epsilon,\eta}\) is nonconstant. Moreover,
\[
\lim_{n\to\infty}\frac{\sum_{j=1}^{n}s_j(T)}{\log n}
=\frac{1+\eta}{\pi} E\!\left(\frac{2\sqrt\eta}{1+\eta}\right),
\qquad
T\in\mathcal S_p\iff p>1,
\]
where \(E(k)=\int_0^{\pi/2}\sqrt{1-k^2\sin^2 v}\,dv\). Thus \(T\) is in weak \(\mathcal S_1\) but not in trace class.

## Assumptions and scope

The Hardy space is the classical complex \(H^2(\mathbb D)\), with orthonormal monomials \(e_n(z)=z^n\). Fix \(0<\eta\le1/2\) and \(0<\epsilon<\epsilon_0\), where \(\epsilon_0\) is a sufficiently small absolute positive constant as established in Step 5. Set
\[
\mu_\epsilon(r)=1+\epsilon\cos\!\left(\log\frac1{1-r}\right),\quad
m_j=\int_0^1r^j\mu_\epsilon(r)\,dr,\quad d_n=m_{2n+1}.
\]
This positive bounded radial weight is radial doubling because it is uniformly comparable to Lebesgue radial measure. Define the fractional integral \(I^\mu f=\sum_{n\ge0}d_n\widehat f(n)z^n\) and fractional derivative \(D^\mu f=\sum_{n\ge0}\widehat f(n)z^n/d_n\). Put \(g(z)=d_1z+\eta d_2z^2\) and \(T=V_{\mu,g}=I^\mu(fD^\mu g)\). Then \(D^\mu g=z+\eta z^2\), and exactly
\[
Te_n=d_{n+1}e_{n+1}+\eta d_{n+2}e_{n+2}\quad(n\ge0).
\]
Set \(a=\epsilon|\Gamma(1-i)|\), \(\phi=\log2+\arg\Gamma(1-i)\), \(q(v)=1+a\cos(v+\phi)\), and \(r_\eta(\theta)=|1+\eta e^{i\theta}|\). Take \(\epsilon_0\) small enough that \(a<1/\sqrt2\) and the nonvanishing first-harmonic estimate in Step 5 holds. For each real \(u\) and \(\theta\), let \(x_\theta(u)\) be the unique positive solution of
\[
2x=r_\eta(\theta)q(u+\log x),
\quad \Psi_{\epsilon,\eta}(u)=\frac1{2\pi}\int_0^{2\pi}x_\theta(u)\,d\theta.
\]
The uniqueness holds because \(q(v)-q'(v)=1+a(\cos(v+\phi)+\sin(v+\phi))>0\). The bounds \(\tfrac12(1-a)(1-\eta)\le x_\theta(u)\le\tfrac12(1+a)(1+\eta)\) show that the profile is well-defined, positive, continuous and periodic.

## Proof

**Step 1: exact operator and moments.** Positivity of the weight makes all \(d_n>0\). The beta integral gives the exact identity
\[
m_j=\frac1{j+1}+\epsilon\operatorname{Re}B(j+1,1-i).
\]
The complex gamma-ratio asymptotic \(\Gamma(j+1)/\Gamma(j+2-i)=(j+1)^{-1+i}(1+O(j^{-1}))\) implies
\[
 d_n=\frac{1}{2n}q(\log n)+O(n^{-2})\quad(n\to\infty),
\]
where the error is uniform in \(\epsilon\) on a fixed bounded interval. In particular \(c/n\le d_n\le C/n\) for large \(n\). The formula for \(Te_n\) proves compactness, because it is the sum of two shifted diagonal sequences tending to zero.

**Step 2: exact Jacobi Gram matrix.** On \(\ell^2(\mathbb N_0)\), \(T^*T\) is tridiagonal: its diagonal at input index \(n\) equals \(d_{n+1}^2+\eta^2d_{n+2}^2\); its adjacent off-diagonal between \(n\) and \(n+1\) equals \(\eta d_{n+2}^2\). For indices near \(Nx\) with \(x>0\), after multiplying by \(N^2\), the local eigenvalue symbol of this positive Jacobi matrix along any subsequence where \(\log N\bmod 2\pi\to u\) is
\[
\left(\frac{q(u+\log x)}{2x}\right)^2
(1+\eta^2+2\eta\cos\theta)
=\left(\frac{q(u+\log x)r_\eta(\theta)}{2x}\right)^2.
\]

**Step 3: finite-block spectral counting.** Fix \(0<\delta<R<\infty\). Compress to input indices from \(\lceil\delta N\rceil\) through \(\lfloor RN\rfloor\). Because the bandwidth of \(T^*T\) is one, the normalized trace of each fixed power of \(N^2T^*T\) on this block converges, uniformly in the limiting phase \(u\), to
\[
 \frac1{2\pi}\int_\delta^R\int_0^{2\pi}
 \left(\frac{q(u+\log x)r_\eta(\theta)}{2x}\right)^{2k}\,d\theta\,dx.
\]
Indeed, in a trace expansion only finitely many closed nearest-neighbor walks of each fixed length contribute; away from the \(O(1)\) endpoint rows, their edge weights differ by \(o(1)\) uniformly from their frozen-row values, and the sum is a Riemann sum. Polynomial approximation on the uniformly bounded spectral interval gives the same limit for all continuous test functions. For the indicator of eigenvalues above \(1\), the relevant level set has zero planar measure: for every fixed \(u,\theta\), the function \(x\mapsto r_\eta(\theta)q(u+\log x)/(2x)\) decreases strictly. Hence along each phase subsequence the count of squared singular values above \(N^{-2}\) on this block, divided by \(N\), tends to the \(x,\theta\) area of the region where the displayed local singular symbol exceeds \(1\).

The discarded low-input block has rank at most \(\delta N+O(1)\). The high-input tail of \(T\), starting beyond \(RN\), has norm at most \((1+\eta)\sup_{j\ge RN}d_j=O((RN)^{-1})\). Weyl rank inequalities control the former, and the threshold perturbation inequalities \(N_{>t+\|E\|}(A)\le N_{>t}(A+E)\le N_{>t-\|E\|}(A)\) control the latter. First let \(N\to\infty\), then \(\delta\downarrow0\) and \(R\to\infty\). The strict monotonicity in \(x\) ensures continuity in the threshold. We obtain
\[
\frac{N(1/N;T)}N-\Psi_{\epsilon,\eta}(\log N)\longrightarrow0.
\]
Applying this to general real \(t\downarrow0\), by using \(N=1/t\) rather than integer \(N\) (or replacing it by its integer part), yields the asserted counting formula. The phase-subsequence argument is uniform since every phase sequence in the compact circle has a convergent subsequence.

**Step 4: universal period average and operator-ideal endpoint.** Equivalently
\[
\Psi(u)=\frac1{2\pi}\int_0^{2\pi}\int_0^\infty
 \mathbf1_{\{2x<r_\eta(\theta)q(u+\log x)\}}\,dx\,d\theta.
\]
Integrate over one period in \(u\) and change variables on the periodic phase. Tonelli and the layer-cake formula give
\[
\frac1{2\pi}\int_0^{2\pi}\Psi(u)\,du
=\frac12\frac1{2\pi}\int_0^{2\pi}r_\eta(\theta)\,d\theta,
\]
since the mean of \(q\) equals \(1\). The last quantity is \((1+\eta)E(2\sqrt\eta/(1+\eta))/\pi\). Since \(T\) is a two-term shift with \(d_n\asymp1/n\) and \(0<\eta<1\), factorization through \(I+\eta S\) (boundedly invertible) implies \(s_n(T)\asymp n^{-1}\). The exact layer-cake identity for \(\sum_{j\le n}s_j\), together with \(N(t)=t^{-1}\Psi(\log(1/t))+o(t^{-1})\), shows that the quotient by \(\log n\) approaches the period mean; the bounded periodic primitive contributes only \(O(1)\). This also gives the sharp \(\mathcal S_p\) membership and weak trace-class statements.

**Step 5: genuine nonconstancy.** Uniformly for \(0\le\eta\le1/2\), differentiate the implicit equation defining \(x_\theta(u)\) at \(a=0\):
\[
\left.\partial_a x_\theta(u)\right|_{a=0}
=\frac{r_\eta(\theta)}2
 \cos\left(u+\log\frac{r_\eta(\theta)}2+\phi\right).
\]
The coefficient of the first oscillatory Fourier harmonic of \(\Psi\), to first order in \(a\), has complex amplitude proportional to
\[
 e^{i(\phi-\log2)}\frac1{2\pi}
 \int_0^{2\pi}r_\eta(\theta)^{1+i}\,d\theta.
\]
For \(\eta\le1/2\), \(r_\eta(\theta)\in[1/2,3/2]\), so \(\operatorname{Re}r_\eta(\theta)^{1+i}=r_\eta(\theta)\cos(\log r_\eta(\theta))\) is uniformly positive. The implicit-function expansion is uniform over \(u,\theta,\eta\) on their compact parameter sets, so a common \(a_0>0\), hence a common \(\epsilon_0>0\), makes that harmonic nonzero. Therefore \(\Psi\) is nonconstant. Since a convergent \(n s_n(T)\) would force \(tN(t;T)\) to converge, the nonconstant phase law excludes such convergence.

## Verification

The identity for the beta moments, the Gram entries and the finite-band symbol can be directly checked algebraically. A standalone numerical checker (CHECK.py, with requirements.txt) computes the exact complex beta moments by the gamma-ratio function, counts finite Jacobi eigenvalues by a symmetric Sturm recurrence, independently evaluates the implicit profile by fixed-point iteration, and compares the two across several finite truncations. It also verifies the predicted equality of the mean profile and the elliptic angular mean numerically. These are finite corroborations; the infinite-dimensional assertion follows from Steps 1–5. Execute `python CHECK.py` in an environment satisfying requirements.txt.

## Relationship to prior work

Moreno (2026, arXiv:2610.37548) analyzes essential norms for fractional Volterra-type operators, and Bellavita–Moreno–Nikolaidis–Peláez (2025, arXiv:2506.18122) proves qualitative Hardy-space boundedness, compactness and Schatten membership criteria. Neither of the inspected works states the present log-periodic singular counting profile or the invariant logarithmic-average coefficient. Pushnitski (2017, arXiv:1710.02652), Theorem 1.2, provides singular-value asymptotics for banded matrices whose rescaled diagonals converge to constants; our matrix has rescaled coefficients oscillating with \(\log n\), preventing direct application. General locally Toeplitz spectral-distribution principles provide background for the finite-block method, so broader implication is an identified publication-priority risk.

## Limitations

The smallness condition on \(\epsilon\) is sufficient to prove nonconstancy, not claimed sharp. The result treats the explicit two-term polynomial \(z+\eta z^2\), not general analytic symbols. It does not provide a pointwise limit for scaled singular values (indeed the limit generally fails); it gives an exact periodic first-order counting law and an averaged endpoint. A general theorem about oscillatory banded matrices could imply the result in different language; independent validation and exhaustive priority certification have not been performed.

## References

1. Á. M. Moreno, *Essential norms of fractional Volterra-type operators* (2026), arXiv:2610.37548, first version dated 2026-10-27.
2. C. Bellavita, Á. M. Moreno, G. Nikolaidis, J. Á. Peláez, *Fractional Volterra-type operator induced by radial weight acting on Hardy space* (2025), arXiv:2506.18122, first version dated 2025-06-22.
3. A. Pushnitski, *Spectral asymptotics for a class of Toeplitz operators on the Bergman space* (2017), arXiv:1710.02652, especially Theorem 1.2 on banded matrices.
