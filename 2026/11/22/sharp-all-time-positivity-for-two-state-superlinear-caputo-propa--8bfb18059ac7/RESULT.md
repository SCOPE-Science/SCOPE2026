# Sharp all-time positivity for two-state superlinear Caputo propagators

## Finding

Let \(1<\alpha\le2\) and \(u,v>0\). Define the two-state column generator
\[
A=\begin{pmatrix}-u&v\\u&-v\end{pmatrix},\qquad \kappa=u+v,
\]
and the normalized solution of the zero-initial-velocity Caputo matrix problem
\[
{}^C D_t^\alpha P_\alpha(t)=AP_\alpha(t),\qquad
P_\alpha(0)=I,\qquad P_\alpha'(0)=0.
\]
Set \(E_\alpha(z)=\sum_{j=0}^\infty z^j/\Gamma(1+\alpha j)\), \(f_\alpha(s)=E_\alpha(-s^\alpha)\), and
\[
c_\alpha=-\min_{s\ge0}f_\alpha(s).
\]
**Theorem.** For every \(1<\alpha<2\), the minimum exists and \(0<c_\alpha<1\). For all \(u,v>0\), the following are equivalent:
\[
P_\alpha(t)\ \text{has nonnegative entries for every }t\ge0
\quad\Longleftrightarrow\quad
c_\alpha\le\frac uv\le\frac1{c_\alpha}.
\]
In the balanced case \(u=v\), all-time nonnegativity holds. Outside the stated interval, at least one diagonal probability is strictly negative at a finite time. The bounds are attained: at an endpoint rate ratio, one diagonal becomes zero at a global minimizing time. Furthermore,
\[
\lim_{\alpha\downarrow1}c_\alpha=0,
\qquad \lim_{\alpha\uparrow2}c_\alpha=1,
\]
while at \(\alpha=2\), \(f_2(s)=\cos s\), \(c_2=1\), and only \(u=v\) gives nonnegative matrices at all times. For every \(1<\alpha\le2\), \(\det P_\alpha(t)<0\) for some finite \(t\); hence no two-state inhomogeneous continuous-time Markov chain with finite, locally integrable time-varying jump rates has \(P_\alpha(t)\) as its initial-time propagator.

This separates the exact possibility of **nonnegative one-time matrices** from the stronger requirement of a **Markov propagator**. In particular, no assertion of Chapman–Kolmogorov consistency is made.

## Assumptions and scope

For \(1<\alpha<2\), use the Caputo derivative \({}^CD_t^\alpha h(t)=\Gamma(2-\alpha)^{-1}\int_0^t(t-s)^{1-\alpha}h''(s)\,ds\), entrywise in the matrix problem. The classical second derivative is used at \(\alpha=2\). The first initial derivative is exactly zero. All times are real and nonnegative, all rates strictly positive, and there are exactly two states. A column-stochastic matrix has nonnegative real entries and every column sum equal to one. The parameter \(\alpha\) is dimensionless and the argument \(s=\kappa^{1/\alpha}t\) is dimensionless. No stochastic-process interpretation is presupposed for the fractional differential equation.

## Proof

**1. Scalar reduction and the four entries.** The matrix \(\Pi=I+A/\kappa\) has identical columns \(\pi=(v/\kappa,u/\kappa)^T\), with \(\Pi^2=\Pi\), \(A=-\kappa(I-\Pi)\). Termwise matrix Mittag–Leffler functional calculus therefore gives
\[
P_\alpha(t)=\Pi+f_\alpha(\kappa^{1/\alpha}t)(I-\Pi).
\]
Writing \(f=f_\alpha(\kappa^{1/\alpha}t)\), its entries, in the given order, are
\[
P_\alpha(t)=\frac1\kappa
\begin{pmatrix}v+uf&v(1-f)\\u(1-f)&u+vf\end{pmatrix},
\qquad \det P_\alpha(t)=f.
\]
Thus column sums equal one identically. Nonnegativity is equivalent to \(f\le1\) and \(f\ge-\min(v/u,u/v)\).

**2. Spectral proof of the precise scalar range.** For \(1<\alpha<2\), the standard large-negative-argument Mittag–Leffler expansion (see Honain et al., Theorem 1) yields
\[
f_\alpha(s)=\frac{s^{-\alpha}}{\Gamma(1-\alpha)}+O(s^{-2\alpha})
\quad(s\to\infty).
\]
Because \(\Gamma(1-\alpha)<0\), this shows that \(f_\alpha\) eventually becomes strictly negative, tends to zero, and belongs to \(L^1(0,\infty)\). Its one-sided Laplace transform is the classical identity
\[
\int_0^\infty e^{-zs}f_\alpha(s)\,ds=
\frac{z^{\alpha-1}}{1+z^\alpha},\qquad z>0.
\]
Extending \(f_\alpha\) evenly to the real line and evaluating the Fourier transform through the boundary \(z=i\omega\) in the right half-plane gives, by Fourier inversion,
\[
f_\alpha(s)=\int_{-\infty}^{\infty}\cos(s\omega)g_\alpha(\omega)\,d\omega,
\]
where
\[
g_\alpha(\omega)=\frac{\sin(\pi\alpha/2)\,|\omega|^{\alpha-1}}
{\pi\,[1+2|\omega|^\alpha\cos(\pi\alpha/2)+|\omega|^{2\alpha}]}.
\]
This density is nonnegative, strictly positive for every \(\omega\ne0\), and has total mass one. Indeed, with \(\theta=\pi\alpha/2\) and \(y=\omega^\alpha\),
\[
2\int_0^\infty g_\alpha(\omega)\,d\omega
=\frac{2\sin\theta}{\pi\alpha}
\int_0^\infty\frac{dy}{y^2+2y\cos\theta+1}
=\frac{2\theta}{\pi\alpha}=1.
\]
Thus \(f_\alpha\) is the characteristic function of a non-atomic probability law with positive density on both half-lines. In particular, \(|f_\alpha(s)|<1\) for every \(s>0\), since equality in the characteristic-function triangle inequality at a positive argument would force \(e^{is\omega}\) to be constant on a set of full continuous density. The negative values noted above and the limit \(f_\alpha(s)\to0\) ensure its global minimum is achieved at a finite positive \(s\). Therefore \(0<c_\alpha<1\), and the exact scalar range is contained in \([-c_\alpha,1]\), with both endpoints attained.

**3. The sharp rate interval.** Substitute the exact range into the entry formula of Step 1. All off-diagonal entries are nonnegative; the two diagonals are both nonnegative for all \(t\) if and only if \(c_\alpha\le \min(v/u,u/v)\), equivalently \(c_\alpha\le u/v\le c_\alpha^{-1}\). At equality, \(s\) can be chosen as a global minimizer and the limiting diagonal is zero. Outside the interval, the same time makes that diagonal strictly negative. This establishes both necessity and sufficiency for all times and all rate pairs.

**4. Endpoint orders.** As \(\alpha\downarrow1\), \(g_\alpha(\omega)\to[\pi(1+\omega^2)]^{-1}\) for every \(\omega\ne0\). Both are probability densities, so Scheffé's lemma yields convergence in \(L^1\). Their characteristic functions therefore converge uniformly on the whole real line to \(e^{-|s|}\). This is nonnegative, so \(c_\alpha\to0\). As \(\alpha\uparrow2\), the defining entire-function series yields \(f_\alpha(\pi)\to\cos\pi=-1\), whereas \(c_\alpha\le1\), hence \(c_\alpha\to1\). At \(\alpha=2\), the same matrix formula gives \(f_2(s)=\cos s\) and exactly \(u=v\).

**5. Probability matrices do not imply Markov dynamics.** The negative minimum ensures a finite \(t\) with \(\det P_\alpha(t)=f<0\) regardless of rates, even when the entries remain nonnegative. If a two-state time-inhomogeneous continuous-time Markov chain has a locally integrable finite rate generator \(B(t)\), its fundamental propagator satisfies \(\det P(t)=\exp(\int_0^t\operatorname{tr}B(s)\,ds)>0\) for every finite \(t\), by Liouville's determinant formula. Such a chain is therefore impossible here. On the weaker level of marginal consistency from the initial state, if the rate criterion holds, a two-state measurable stochastic process can be constructed for each deterministic starting state \(i\): sample a uniform \(U\) on \([0,1]\), set \(X(0)=i\), and take \(X(t)=i\) when \(U\le P_{ii}(t)\), and the other state otherwise. This only realizes \(\Pr[X(t)=j\mid X(0)=i]=P_{ji}(t)\), **not** the same matrix as conditional transitions across arbitrary positive starting times, and does not satisfy a Markov generator equation. This distinction is essential.

## Verification

The functional calculus can be checked by the identity \(A^2=-\kappa A\). The Fourier density is derived directly from the Laplace transform, and its normalization integral is evaluated explicitly above. The finite-dimensional equivalence reduces to two exact inequalities; no numerical minimization or finite enumeration is used to certify the universal theorem. A standalone standard-library checker in `CHECK.py` verifies representative two-state matrices, column normalization, determinant identity, and a concrete nonpositive case at order \(\alpha=3/2\). The checker is diagnostic only and cannot establish the infinite-time or all-parameter assertions.

## Relationship to prior work

Van Mieghem (2026, arXiv:2611.02954v1) derives the general high-order matrix Mittag–Leffler solution and argues that replacing a Markov derivative by order greater than one does not yield a valid stochastic dynamical theory. The present statement does not assert the contrary: it isolates the strictly weaker, natural question of when the **zero-initial-velocity two-state solution is nonnegative at each time**, and proves a complete rate criterion plus the determinant obstruction. Honain et al. (2024) establish oscillatory and asymptotic scalar Mittag–Leffler facts and study numerical matrix approximation, not a two-state probability-positivity phase diagram. Facciaroni et al. (2025) and Di Crescenzo–Meoli (2016) construct non-Markovian two-state/fractional chains in the distinct regime of derivative orders at most one. The scalar Laplace and Fourier identities are standard tools and are not claimed as independent novelty.

## Limitations

The constant \(c_\alpha\) is specified exactly as a natural global minimum of a classical special function; no elementary closed formula, strict monotonicity in \(\alpha\), or certified decimal approximation is asserted. The result covers only two-state generators with strictly positive rates and zero initial derivative; other initial derivatives can destroy positivity. Entrywise stochasticity from initial time zero is not a Markov or semi-Markov process theorem. The constructed one-time marginal process is not asserted to satisfy any nonlocal governing equation at arbitrary starting times. No claim is made for three or more states, nonconstant matrices, or \(\alpha>2\). Independent validation and exhaustive historical-priority verification have not been performed.

## References

1. P. Van Mieghem, *High-order fractional linear differential equations do not describe stochastic processes with finite state space*, arXiv:2611.02954v1 (first posted 2026-11-02), https://arxiv.org/html/2611.02954v1.
2. A. H. Honain, K. M. Furati, I. O. Sarumi, A. Q. M. Khaliq, *Rational Approximations for the Oscillatory Two-Parameter Mittag–Leffler Function*, Fractal and Fractional 8 (2024), 319, https://doi.org/10.3390/fractalfract8060319.
3. L. Facciaroni, C. Ricciuti, E. Scalas, B. Toaldo, *Para-Markov chains and related non-local equations*, Fractional Calculus and Applied Analysis 28 (2025), 1071–1093, https://doi.org/10.1007/s13540-025-00390-9.
4. A. Di Crescenzo and A. Meoli, *On a fractional alternating Poisson process*, AIMS Mathematics 1 (2016), 212–224, https://doi.org/10.3934/Math.2016.3.212.
