# Arbitrarily delayed relative mixing in Doeblin circle-copula processes

## Finding

A smooth copula-level construction can have a sharply delayed onset of finite relative-mixing coefficients despite uniform one-step regeneration and exponential maximal-correlation mixing. The delay can be made arbitrarily long without sacrificing a prescribed small upper bound on one-step maximal correlation.

**Theorem.** Fix \(0<a<1\) and \(0<\varepsilon<1\). Define the probability density on the unit circle \(\mathbb T=\mathbb R/\mathbb Z\)
\[
f_a(t)=(1-a)t^{-a}\quad(0<t<1),\qquad
f_{a,\varepsilon}(t)=1-\varepsilon+\varepsilon f_a(t).
\]
Values at integer representatives are immaterial. Let \((U_j)_{j\in\mathbb Z}\) be the stationary, uniform-marginal Markov process with transition density
\[
k_{a,\varepsilon}(u,v)=f_{a,\varepsilon}((u+v)\bmod 1),\qquad u,v\in[0,1].
\]
For the usual past-to-future relative-mixing coefficient \(\psi(n)\), and maximal-correlation coefficient \(\rho(n)\), the following statements hold for **every** positive integer \(n\):

1. **Sharp regularization delay:**
   \[
   \psi(n)<\infty\quad\Longleftrightarrow\quad n(1-a)>1.
   \]
   Thus the first finite coefficient occurs exactly at
   \(n_{\mathrm{reg}}=\lfloor(1-a)^{-1}\rfloor+1\).
2. **Exact even-lag coefficients:** put \(\widehat f_a(k)=\int_0^1f_a(t)e^{-2\pi i kt}\,dt\). Whenever \(2m(1-a)>1\),
   \[
   \psi(2m)=2\varepsilon^{2m}\sum_{k=1}^{\infty}|\widehat f_a(k)|^{2m}.
   \]
   In particular, \(\psi(2)=\varepsilon^2 a^2/(1-2a)\) for \(0<a<1/2\), whereas \(\psi(2)=\infty\) for \(a\ge1/2\).
3. **Spectral and Doeblin bounds:** setting \(r_a=\max_{k\ge1}|\widehat f_a(k)|\in(0,1)\),
   \[
   \rho(n)=(\varepsilon r_a)^n,\qquad
   \sup_u\|\mathcal L(U_n\mid U_0=u)-\operatorname{Unif}[0,1]\|_{\mathrm{TV}}\le\varepsilon^n,
   \]
   while the one-step density is everywhere at least \(1-\varepsilon\) up to null sets. For every prescribed integer \(L\ge1\) and \(\delta>0\), parameters exist with \(\psi(1)=\cdots=\psi(L)=\infty\) and \(\rho(1)<\delta\).
4. **Blow-up at each even-lag boundary:** for fixed \(m\ge1\), put \(a_m=1-(2m)^{-1}\) and \(c(a)=\Gamma(2-a)(2\pi)^{a-1}\). As \(a\uparrow a_m\),
   \[
   \psi(2m)\sim\frac{\varepsilon^{2m}c(a_m)^{2m}}{m(a_m-a)}.
   \]

This is one joint classification theorem; the explicit formulas and extreme separation are consequences of the same Fourier/convolution mechanism.

## Assumptions and scope

All parameters are strictly interior as stated; the state space is the circle with Lebesgue-uniform invariant distribution. The process is time-homogeneous and indexed by integer time, with a two-sided stationary extension. The density may be assigned arbitrary values at its periodic singular points, since all statements are almost-everywhere statements.

For \(n\ge1\), let \(\mathcal F_{-\infty}^{0}=\sigma(U_j:j\le0)\) and \(\mathcal F_n^{\infty}=\sigma(U_j:j\ge n)\). Specifically,
\[
\psi(n)=\sup_{\substack{A\in\mathcal F_{-\infty}^{0},\ B\in\mathcal F_n^{\infty}\\\Pr(A)\Pr(B)>0}}
\left|\frac{\Pr(A\cap B)}{\Pr(A)\Pr(B)}-1\right|,
\]
with extended-real value permitted; \(\rho(n)\) is the supremum of absolute correlations of nonconstant square-integrable real variables measurable respectively with respect to these sigma-fields.

For any stationary Markov kernel with uniform invariant measure and a lag-\(n\) density \(p_n(u,v)\), the Markov property and conditioning imply
\(\psi(n)=\operatorname*{ess\,sup}_{u,v}|p_n(u,v)-1|\). The upper inequality follows by conditioning on the boundary states; the reverse inequality follows by taking small intervals in \(U_0\) and \(U_n\) around Lebesgue density points of the positive/negative deviation. Likewise \(\rho(n)\) equals the centered \(L^2\)-operator norm of the \(n\)-step Markov operator.

## Proof

**1. Normalization, regeneration and lag kernels.** The integral of \(f_a\) is \((1-a)\int_0^1t^{-a}\,dt=1\), and integrating \(k_{a,\varepsilon}(u,v)\) in either coordinate gives 1 by circular translation. The density is symmetric in \(u,v\), so the chain is reversible under uniform measure. The lower bound \(k_{a,\varepsilon}\ge1-\varepsilon\) gives uniform regeneration.

Let \(\Pi\) be the projection onto constant functions, and \(P_a\) the Markov operator associated with \(f_a(u+v)\). Because \(P_a\Pi=\Pi P_a=\Pi\), the mixed operator \(P=\Pi+\varepsilon(P_a-\Pi)\) satisfies, for every integer \(n\ge1\),
\[
P^n=\Pi+\varepsilon^n(P_a^n-\Pi).
\]
Let \(\widetilde f_a(t)=f_a((-t)\bmod1)\), and use normalized circular convolution. Direct integration, or induction using \(U_{j+1}=Z_{j+1}-U_j\pmod1\) for independent \(Z_j\sim f_a\), gives
\[
h_{n,a}=f_a^{*\lceil n/2\rceil}*\widetilde f_a^{*\lfloor n/2\rfloor},\qquad
p_n(u,v)=1+\varepsilon^n\bigl[h_{n,a}((v+(-1)^{n-1}u)\bmod1)-1\bigr].
\]
In the displayed argument, \(n\) odd gives \(u+v\), and \(n\) even gives \(v-u\). Therefore
\(\psi(n)=\varepsilon^n\|h_{n,a}-1\|_{L^\infty(\mathbb T)}\), allowing infinity. The same mixture identity proves the total-variation bound.

**2. Fourier asymptotics and the exact spectral rate.** With the convention in the theorem,
\[
\widehat f_a(k)=(1-a)\int_0^1 t^{-a}e^{-2\pi i kt}\,dt.
\]
For positive integers \(k\), the oscillatory gamma integral on \((0,\infty)\) and integration by parts on \((1,\infty)\) yield
\[
\widehat f_a(k)
=c(a)e^{-i\pi(1-a)/2}k^{-(1-a)}+O_a(k^{-1}),\qquad
c(a)=\Gamma(2-a)(2\pi)^{a-1}>0.
\]
This estimate is uniform for \(a\) in compact subintervals of \((0,1)\). For a nonzero integer \(k\), strict triangle inequality gives \(|\widehat f_a(k)|<1\), since the density is positive almost everywhere and the character is nonconstant. Riemann–Lebesgue gives convergence of these coefficients to zero; nonuniformity of \(f_a\) supplies at least one nonzero coefficient. Thus \(0<r_a<1\).

On characters \(e_k(u)=e^{2\pi iku}\), one has \(P_a e_k=\overline{\widehat f_a(k)}e_{-k}\) and \(P_a^2e_k=|\widehat f_a(k)|^2e_k\). On each real two-dimensional sine/cosine subspace, the symmetric operator has eigenvalues \(\pm|\widehat f_a(k)|\). On centered functions the mixed operator is \(\varepsilon P_a\), so its \(n\)-step norm, and hence \(\rho(n)\), is exactly \((\varepsilon r_a)^n\).

**3. Necessary and sufficient boundedness of the lag density.** Circular convolution gives
\[
\widehat h_{n,a}(k)=
\begin{cases}
|\widehat f_a(k)|^n,&n\text{ even},\\
\widehat f_a(k)|\widehat f_a(k)|^{n-1},&n\text{ odd}.
\end{cases}
\]
If \(n(1-a)>1\), then \(p=n/(n-1)\) satisfies \(ap<1\) (and \(n\ge2\)); hence \(f_a,\widetilde f_a\in L^p(\mathbb T)\). Generalized Young convolution gives \(\|h_{n,a}\|_\infty\le\|f_a\|_p^n<\infty\). Equivalently, the Fourier coefficients are absolutely summable by the displayed asymptotic.

Conversely suppose \(n(1-a)\le1\). The Fourier coefficients of \(h_{n,a}\) at positive frequencies have asymptotically positive real parts of exact order \(k^{-n(1-a)}\): this is immediate for even \(n\); for odd \(n\) the limiting phase has positive cosine \(\cos(\pi(1-a)/2)>0\). Thus the Fejér means of \(h_{n,a}\), evaluated at zero, tend to \(+\infty\), since their Fourier expansion has positive divergent tail comparable to \(\sum k^{-n(1-a)}\). A bounded density cannot have unbounded Fejér means because each Fejér kernel is nonnegative of integral one. Thus \(\|h_{n,a}\|_\infty=\infty\), proving the exact cutoff **including equality** and odd lags. The argument establishes essential unboundedness, not merely an isolated infinite value.

**4. Even-lag sharp constants and critical blow-up.** For \(n=2m\) past the cutoff, \(h_{2m,a}\) has a uniformly absolutely convergent Fourier series with nonnegative Fourier coefficients. Consequently
\[
\|h_{2m,a}-1\|_\infty=2\sum_{k\ge1}|\widehat f_a(k)|^{2m},
\]
because the triangle upper bound is attained at argument zero. For \(m=1\) and \(a<1/2\), Plancherel gives
\[
2\sum_{k\ge1}|\widehat f_a(k)|^2
=\int_0^1f_a(t)^2dt-1
=\frac{(1-a)^2}{1-2a}-1=\frac{a^2}{1-2a}.
\]
For fixed \(m\), put \(s=2m(1-a)\). Uniformly as \(a\uparrow a_m=1-1/(2m)\), the Fourier asymptotic implies
\[
\sum_{k\ge1}|\widehat f_a(k)|^{2m}
=c(a)^{2m}\zeta(s)+O_m(1),
\]
since the relative Fourier error is \(O(k^{-a})\), giving an absolutely summable remainder uniformly near \(a_m>0\). Finally \(\zeta(s)\sim(s-1)^{-1}=[2m(a_m-a)]^{-1}\), yielding the displayed pole coefficient.

**5. Arbitrarily delayed onset despite strong regeneration.** Given \(L\ge2\), choose \(a=1-1/L\); then the finite-coefficient condition fails at every \(1\le n\le L\). Given \(L=1\), use any \(a>0\). With \(0<\varepsilon<\min(1,\delta)\), the coefficient \(\rho(1)=\varepsilon r_a<\delta\) and the total-variation distance is at most \(\varepsilon^n\). Every chain is eventually exponentially \(\psi\)-mixing: select \(N\) with \(N(1-a)>1\), use the absolutely summable Fourier series of \(h_{N,a}\), and for \(n\ge N\) bound
\[
\psi(n)\le2\varepsilon^n\sum_{k\ge1}|\widehat f_a(k)|^n
\le 2\varepsilon^n r_a^{n-N}\sum_{k\ge1}|\widehat f_a(k)|^N.
\]
This completes the theorem.

## Verification

The companion `CHECK.py` uses exact rational identities and independent complex incomplete-gamma evaluations of the Fourier coefficients. It checks the two-step formula, spectral coefficient asymptotic, positive even-lag Fourier partial sums, the critical divergence, and the strict integer threshold. The program requires Python and `mpmath` and prints `ALL NUMERICAL CONSISTENCY CHECKS PASSED` when those tests succeed. Its finite tests are **not** a substitute for the all-index Fourier/Young/Fejér proof above.

## Relationship to prior work

Lalancette and Zimmerman [1] introduce the copula density \(f((u+v)\bmod1)\) for arbitrary univariate densities, including highly irregular generators, and establish smoothness of the resulting copula. Their later paper [2] extends the family to reflected signatures, establishes a convolution-based copula semigroup, and provides Fourier decompositions. These constructions and the general Markov product are **prior work**, not claimed here.

Longla [3] treats relative-mixing criteria for copula-generated Markov processes, including sufficient conditions based on bounded multi-step densities and applications to other copula families. The present claim instead classifies the **exact first lag with finite \(\psi\)** in a singular power-generated subfamily, establishes the exact even-lag values, and demonstrates arbitrary finite delay despite a uniform Doeblin minorization. Classical Fourier/Young/Fejér inequalities and the gamma-integral asymptotic are used as standard mathematical tools, not claimed as new.

## Limitations

The theorem concerns the specific power-cusp generator mixed with a uniform component; it does not assert a universal lag cutoff for all irregular copulas. The exact closed series is supplied for even lags; odd-lag finiteness and exponential bounds, but not an odd-lag closed supremum, are proved. The Markov chain is on a continuous state space and is not a finite-state chain. The identification of the sharp classification as new is literature-search qualified rather than an independently certified priority claim.

## References

[1] M. Lalancette and R. Zimmerman, *A new family of smooth copulas with arbitrarily irregular densities*, arXiv:2204.04336, initially submitted 9 April 2022. https://arxiv.org/abs/2204.04336

[2] M. Lalancette and R. Zimmerman, *A Tractable Family of Smooth Copulas with Rotational Dependence: Properties, Inference, and Application*, arXiv:2509.26635, submitted 30 September 2025. https://arxiv.org/abs/2509.26635

[3] M. Longla, *On Some Mixing Properties of Copula-Based Markov Chains*, *Journal of Statistical Theory and Applications* (2022). https://doi.org/10.1007/s44199-022-00045-1

[4] Y. Katznelson, *An Introduction to Harmonic Analysis* (3rd ed., Cambridge University Press, 2004). Classical Fourier–Fejér, Riemann–Lebesgue and convolution estimates are used; see also the group-Fourier discussion in [2].
