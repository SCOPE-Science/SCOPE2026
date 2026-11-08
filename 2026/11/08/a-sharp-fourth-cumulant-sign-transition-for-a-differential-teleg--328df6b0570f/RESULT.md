# A sharp fourth-cumulant sign transition for a differential telegraph-driven harmonic response

## Finding

Consider two overdamped harmonic responses to the **same** stationary, symmetric telegraph force, with distinct positive relaxation rates. Although each response separately has strictly negative fourth cumulant, their difference has **positive** fourth cumulant at sufficiently slow switching and **negative** fourth cumulant at sufficiently fast switching. The change of sign occurs **exactly once** for every pair of distinct positive relaxation rates.

Precisely, let \(a,b>0\), \(a\ne b\), and \(\gamma>0\). Let \(\sigma_t\in\{-1,1\}\) be a stationary continuous-time Markov chain which flips sign at rate \(\gamma\), independently of any additional Gaussian forcing. Define the unique stationary bounded solutions
\[
\dot X_t=-a(X_t-\sigma_t),\qquad
\dot Y_t=-b(Y_t-\sigma_t),\qquad Z_t=X_t-Y_t.
\]
Let \(S=a+b\), \(\eta=ab/S^2\in(0,1/4]\), and \(x=\gamma/S\). Define
\[
\begin{aligned}
Q_\eta(x)={}&9\eta^2(2+\eta)-4\eta(3+8\eta)x\\
&-8(3+5\eta+13\eta^2)x^2-8(9+4\eta)x^3
-48(1+\eta)x^4.
\end{aligned}
\]
Then \(Q_\eta\) has exactly one positive root \(x_*(\eta)\). The stationary fourth cumulant \(\kappa_4(Z)=\mathbb E[Z^4]-3(\mathbb E[Z^2])^2\) satisfies
\[
\operatorname{sgn}\kappa_4(Z)=
\begin{cases}
+1,&0<\gamma<Sx_*(\eta),\\
0,&\gamma=Sx_*(\eta),\\
-1,&\gamma>Sx_*(\eta).
\end{cases}
\]
The variance is strictly positive and equals
\[
\operatorname{Var}(Z)=\frac{2\gamma(a-b)^2}{(a+b)(a+2\gamma)(b+2\gamma)}.
\]
Thus the excess kurtosis has the same sharp transition. When \(a=b\), \(Z=0\) identically and no kurtosis is defined. A common nonzero multiplicative propulsion amplitude rescales the cumulant but does not change its sign.

The crossover is invariant under a common rescaling of all rates. In the strongly disparate-relaxation limit \(\eta\downarrow0\), its exact singular slope is
\[
\lim_{\eta\downarrow0}\frac{x_*(\eta)}{\eta}=\frac{\sqrt{13}-1}{4}.
\]
For \(a=1\), \(b=2\), the switching threshold is the unique positive root of \(66\gamma^4+267\gamma^3+385\gamma^2+129\gamma-90=0\), approximately \(0.319688498870504\). In this example \(\kappa_4(Z)>0\) at \(\gamma=1/10\) and \(\kappa_4(Z)<0\) at \(\gamma=1/3\).

## Assumptions and scope

Time is continuous, the telegraph chain is stationary and symmetric, and the two stable linear filters are driven by the **same** force, not independent forces. The relaxation parameters and switching intensity are finite and strictly positive. No interaction, inertia, spatial reset, or non-Markovian drive is included. The claim concerns the equal-time stationary fourth cumulant of the **signed contrast**, not the cumulants of either positive-filter output or the whole joint distribution.

The stationary construction is
\[
X_t=a\int_0^\infty e^{-as}\sigma_{t-s}\,ds,\qquad
Y_t=b\int_0^\infty e^{-bs}\sigma_{t-s}\,ds.
\]
It is unique by exponential contraction and bounded by \(|X_t|,|Y_t|\le1\). Hence all moments used below exist, and the stationary law is symmetric under \((X,Y,\sigma)\mapsto(-X,-Y,-\sigma)\).

## Proof

For nonnegative integers \(i,j\), and parity \(k\in\{0,1\}\), put \(M_{i,j,k}=\mathbb E[X^iY^j\sigma^k]\). The stationary generator acts on monomials as
\[
\begin{aligned}
\mathcal L(X^iY^j\sigma^k)={}&-(ia+jb+2k\gamma)X^iY^j\sigma^k\\
&+iaX^{i-1}Y^j\sigma^{1-k}
+jbX^iY^{j-1}\sigma^{1-k},
\end{aligned}
\]
where terms with negative exponents are omitted. Thus, for \(i+j\ge1\),
\[
M_{i,j,k}=\frac{iaM_{i-1,j,1-k}+jbM_{i,j-1,1-k}}
{ia+jb+2k\gamma},\qquad
M_{0,0,0}=1,\quad M_{0,0,1}=0.
\]
This triangular identity is exact for all finite degrees. Writing \(m_n=\sum_{j=0}^{n}(-1)^j\binom njM_{n-j,j,0}\), symmetry yields \(m_1=m_3=0\). Evaluating the recurrence at degrees two and four gives the stated variance and
\[
\kappa_4(Z)=\frac{12\gamma(a-b)^4 S^6Q_\eta(\gamma/S)}{H(a,b,\gamma)},
\]
with the strictly positive denominator
\[
\begin{aligned}
H={}&(a+b)(a+3b)(3a+b)(a+2\gamma)^2(b+2\gamma)^2\\
&\times(3a+2\gamma)(3b+2\gamma)
(a+2b+2\gamma)(2a+b+2\gamma).
\end{aligned}
\]
The accompanying verification program checks the full rational polynomial identity exactly, coefficient by coefficient, rather than only substituting numerical parameters.

For \(\eta>0\), the constant term of \(Q_\eta\) is positive and **every** positive-degree coefficient is strictly negative. Consequently \(Q_\eta(0)>0\), \(Q_\eta'(x)<0\) for all \(x>0\), and \(Q_\eta(x)\to-\infty\) as \(x\to\infty\). The intermediate-value theorem and strict monotonicity give exactly one positive root and all claimed signs.

For the disparate-rate asymptotic, set \(x=c\eta\) and divide \(Q_\eta(c\eta)\) by \(\eta^2\). Uniformly for bounded \(c\), this tends to \(18-12c-24c^2\). The unique positive zero is \((\sqrt{13}-1)/4\). Bracketing the unique root on either side of this zero and using strict monotonicity proves the stated limit.

Finally, each individual filter is strictly platykurtic, since the same generator gives
\[
\kappa_4(X)=-\frac{6a^3}{(a+2\gamma)^2(3a+2\gamma)}<0,
\qquad
\kappa_4(Y)=-\frac{6b^3}{(b+2\gamma)^2(3b+2\gamma)}<0.
\]
Thus the positive contrast cumulant is not inherited from an already positive marginal; it is caused by **signed subtraction** of differently lagged responses to their common telegraph force.

## Verification

Run `python check.py` with SymPy installed (see `requirements.txt`). The checker (i) recomputes every generator moment through degree four symbolically, (ii) checks the displayed factorization and variance as exact rational identities, (iii) independently assembles and solves the full stationary moment linear system for eight rational parameter triples, including the degenerate equal-rate boundary, (iv) checks the polynomial sign structure, and (v) checks the explicit \((a,b)=(1,2)\) rational example on both sides of the transition. These finite tests supplement, but do not replace, the analytical recurrence and monotonic-polynomial proof.

## Relationship to prior work

Sarkar, Santra and Basu [1] show that harmonic oscillator chains driven by stationary active telegraph or Gaussian reservoirs can agree at the two-point level but differ in higher-order boundary fluctuations. Their inspected model uses boundary reservoirs for an inertial oscillator chain; it does not give the signed-contrast kurtosis transition of two first-order filters driven by a **single shared** telegraph source. Smith, Le Doussal, Majumdar and Schehr [2] analyze harmonic confinement and, in their interacting-particle extension, **independent** active forcing for the two particles; their explicit one-dimensional single-filter statistics do not classify the common-drive difference here.

The general ordered-time negative fourth cumulant of the symmetric telegraph signal and nonnegative-filter sign rigidity are standard points of comparison: those results constrain each positive linear response but **do not constrain a difference**, whose impulse response \(ae^{-as}-be^{-bs}\) changes sign when \(a\ne b\). The present new classification consists of the explicit rational crossover and its uniqueness for all two distinct rates, not the generator method or the componentwise sign.

## Limitations

The result is a stationary, equal-time, fourth-order statement, not an inequality for all higher cumulants, finite-time laws, or arbitrary signed filters. Both output filters have identical unit DC gain; changing their gains changes the contrast and is not covered. Although the comparison with [1] and [2] and targeted scientific searches found no explicit same-claim classification, broader stochastic-filter literature might contain an equivalent result under different terminology. No claim of absolute publication novelty or independent validation is made. Additional independent centered Gaussian noises change the contrast variance but not its fourth cumulant, provided they are independent of the telegraph source.

## References

[1] R. Sarkar, I. Santra and U. Basu, *Stationary states of activity-driven harmonic chains*, arXiv:2210.09035 (first public version 2022-10-17), https://arxiv.org/abs/2210.09035.

[2] N. R. Smith, P. Le Doussal, S. N. Majumdar and G. Schehr, *Exact position distribution of a harmonically-confined run-and-tumble particle in two dimensions*, arXiv:2207.10445 (first public version 2022-07-21), https://arxiv.org/abs/2207.10445.
