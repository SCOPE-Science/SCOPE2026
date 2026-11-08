# Typical-case reversals and Gaussian fluctuations for two-facility distance sampling

## Finding

There are two familiar randomized, strategyproof two-facility rules on the real line. The **Global Pair** (also called Pairwise-Distance or the two-facility Product-Gap rule) selects an unordered pair of reports with probability proportional to its distance. **Proportional** first selects one report uniformly, then selects a second with probability proportional to its distance from the first. The corresponding conditional expected social costs are denoted by \(C_n^G\) and \(C_n^P\).

**Theorem.** For independent \(X_1,X_2,\ldots\sim\operatorname{Uniform}[0,1]\), let \(O_n\) be the optimal total nearest-facility cost with at most two facilities anywhere in \([0,1]\). For every \(n\ge3\), define \(R_n^G=C_n^G/O_n\) and \(R_n^P=C_n^P/O_n\) (almost surely the denominator is positive). Then, simultaneously almost surely and in \(L^1\),

\[
R_n^P\longrightarrow \frac{7\pi}{12}-\frac49\approx1.38815127014960,
\qquad
R_n^G\longrightarrow\frac75=1.4.
\]

The Global Pair limit \(7/5\) is a previously established special case of a more general Product-Gap law, **not** claimed as new here. The new conclusions are the exact Proportional constant, its **strict typical-case advantage** over Global Pair despite the different worst-case incentive for mixing the two rules, and the following first-order sampling law:

\[
\sqrt n\left(R_n^G-\frac75\right)
\xrightarrow{d}N\left(0,\frac{147113}{504000}\right).
\]

In particular, \(\Pr(R_n^P<R_n^G)\to1\). For every fixed mixture using Proportional with probability \(\lambda\in[0,1]\), its limiting approximation ratio is

\[
\lambda\left(\frac{7\pi}{12}-\frac49\right)+(1-\lambda)\frac75.
\]

Thus the typical-case optimum among these fixed mixtures is pure Proportional, whereas the published worst-case optimum within the same family uses a nontrivial mixture.

There is no distribution-free dominance. More precisely, let reported locations be independent with masses \(a,1-2a,a\) at \(0,1/2,1\), respectively, where \(0<a<1/2\). The almost-sure limiting **per-agent costs** of Global Pair and Proportional are, respectively,

\[
C^G(a)=\frac{a(1-2a)}{1-a},\qquad
C^P(a)=a(1-2a)\left(3a+\frac12\right).
\]

Consequently,

\[
C^G(a)-C^P(a)=\frac{a(1-2a)^2(1-3a)}{2(1-a)}.
\]

For \(0<a<1/3\), Proportional is strictly better, the rules tie at \(a=1/3\), and for \(1/3<a<1/2\), Global Pair is strictly better. The population two-facility optimum equals \(\frac12\min\{a,1-2a\}>0\), so this is also a strict reversal in approximation ratios.

## Assumptions and scope

Social cost is the sum of distances to the nearer of two open facilities; the mechanism's internal randomization is averaged **conditional on the reported locations**. Random locations are drawn once and nested across \(n\) using a single infinite independent sequence. The optimization benchmark allows arbitrary facility positions; this does not alter the optimum on a line because cluster medians can be taken at reports. Both rules select two reports (possibly coincident only on degenerate tied profiles). Theorems concern truthful reports, no transfers, two facilities, and the stated probability laws; no general incentive theorem is re-proved.

For a probability law \(F\) on \([0,1]\), write \(g_{x,y}(z)=\min\{|z-x|,|z-y|\}\), \(h_F(x)=\int|x-y|\,dF(y)\), and \(c_F(x,y)=\int g_{x,y}(z)\,dF(z)\). When the denominators are positive, define

\[
T_G(F)=\frac{\iint|x-y|c_F(x,y)\,dF(x)dF(y)}{\iint|x-y|\,dF(x)dF(y)},
\]

\[
T_P(F)=\int\frac{\int|x-y|c_F(x,y)\,dF(y)}{h_F(x)}\,dF(x),
\qquad
Q(F)=\inf_{u,v\in[0,1]}\int g_{u,v}(z)\,dF(z).
\]

For the empirical law \(F_n=n^{-1}\sum_i\delta_{X_i}\), one has **exactly** \(C_n^G/n=T_G(F_n)\), \(C_n^P/n=T_P(F_n)\), \(O_n/n=Q(F_n)\), hence \(R_n^G=T_G(F_n)/Q(F_n)\). The diagonal terms have zero pair weight and therefore cause no discrepancy in these formulas.

## Proof

**1. Deterministic continuum integrals.** Let \(F_0\) be uniform on \([0,1]\). For \(0\le x\le y\le1\), integrating across the midpoint between the facilities gives

\[
c_{F_0}(x,y)=\frac{x^2+(1-y)^2}{2}+\frac{(y-x)^2}{4}.
\]

For any \(t\in[0,1]\) define

\[
A(t)=\int_0^1|t-y|c_{F_0}(t,y)\,dy
=\frac{34t^4-68t^3+54t^2-20t+5}{48},
\quad h_{F_0}(t)=t^2-t+\frac12.
\]

Direct integration yields \(N=\int A(t)dt=7/120\) and \(D=\int h_{F_0}(t)dt=1/3\), so \(T_G(F_0)=N/D=7/40\). Polynomial division gives the **exact** identity

\[
\frac{A(t)}{h_{F_0}(t)}
=\frac{17(t^2-t)}{24}+\frac1{16}+\frac7{96h_{F_0}(t)}.
\]

Since \(\int_0^1h_{F_0}(t)^{-1}dt=\pi\), we get \(T_P(F_0)=-1/18+7\pi/96\). Any pair of sites \(u<v\) partitions the unit interval at \((u+v)/2=s\). Each side's best one-facility total cost is at least its length squared over four; hence \(Q(F_0)\ge[s^2+(1-s)^2]/4\ge1/8\), with equality uniquely at the ordered pair \((1/4,3/4)\). Dividing by \(1/8\) proves both displayed ratio constants, with \(\frac{7\pi}{12}-\frac49<\frac75\) following, for example, from \(\pi<22/7\).

**2. Almost-sure and mean limits.** The empirical distribution converges weakly almost surely to \(F_0\). All kernels above are bounded and continuous on the compact cube, giving \(T_G(F_n)\to T_G(F_0)\). Moreover \(h_{F_n}\to h_{F_0}\) uniformly and \(h_{F_0}\ge1/4\); the Proportional integrand converges uniformly by bounded-Lipschitz kernel estimates. Thus \(T_P(F_n)\to T_P(F_0)\). Uniform convergence of \((u,v)\mapsto\int g_{u,v}\,dF_n\) implies \(Q(F_n)\to1/8\). For either mechanism the published worst-case guarantee gives \(0\le R_n\le4\) when \(O_n>0\); bounded convergence yields convergence in \(L^1\) and hence of the expected ratios. Fixed mixtures follow by linearity.

**3. The sharp conditional-cost central limit law.** Define, for \(t\in[0,1]\),

\[
B(t)=\int_0^1\!\int_0^1 |x-y|g_{x,y}(t)\,dx\,dy.
\]

For \(0\le t\le1/2\), direct integration over the regions \(x,y\le t\), \(x,y\ge t\), and the two parts of \(x<t<y\) separated by \(x+y=2t\) gives

\[
B(t)=\frac{1-4t+12t^2-8t^3-4t^4}{12},
\qquad B(1-t)=B(t).
\]

The numerator \(N(F)=\iint |x-y|c_F(x,y)dF(x)dF(y)\) is a bounded third-order von Mises functional and \(D(F)=\iint|x-y|dF(x)dF(y)\) is second order. The one-point contamination influence of \(T_G(F)=N(F)/D(F)\) at \(F_0\) is

\[
I_T(t)=\frac{2A(t)+B(t)-3N-T_G(F_0)(2h_{F_0}(t)-2D)}{D}.
\]

For \(0\le t\le1/2\) this simplifies to

\[
I_T(t)=\frac{130t^4-420t^3+348t^2-98t+7}{40},
\qquad I_T(1-t)=I_T(t).
\]

The unique uniform-population two-median optimizer implies the empirical optimum has influence \(I_Q(t)=g_{1/4,3/4}(t)-1/8\). For completeness: uniform convergence of the empirical objective yields consistency of its optimizing pair; bounded-Lipschitz finite-dimensional indexing gives stochastic equicontinuity, while the empirical optimum's improvement over the value at the population optimizer is sandwiched between zero and an \(o_p(n^{-1/2})\) empirical-process difference. Thus

\[
\sqrt n\left(Q(F_n)-\frac18\right)
=\frac1{\sqrt n}\sum_{i=1}^n I_Q(X_i)+o_p(1).
\]

The bounded-kernel V-statistic Hoeffding expansion similarly gives \(\sqrt n(T_G(F_n)-7/40)=n^{-1/2}\sum_i I_T(X_i)+o_p(1)\). Applying the ratio delta method, its influence is

\[
I_R(t)=8I_T(t)-\frac{56}{5}I_Q(t).
\]

On \(0\le t\le1/4\) and \(1/4\le t\le1/2\), respectively, these expressions reduce to

\[
I_R(t)=\frac{2t(65t^3-210t^2+174t-21)}{5},
\]

\[
I_R(t)=\frac{2(65t^4-210t^3+174t^2-77t+14)}{5};
\qquad I_R(1-t)=I_R(t).
\]

Direct rational-polynomial integration verifies \(\int_0^1 I_R(t)dt=0\) and

\[
\int_0^1 I_R(t)^2dt=\frac{147113}{504000}>0.
\]

The ordinary iid central limit theorem completes the Gaussian assertion. The centering and variance apply to the **conditional expected** mechanism cost divided by the empirical optimum, not to the randomness of the one pair finally drawn.

**4. Three-support reversal.** Take \(F_a=a\delta_0+(1-2a)\delta_{1/2}+a\delta_1\). Both end sites have distance degree \(1/2\), and the midpoint has distance degree \(a\). Enumerating the three distinct pairs in the two mechanism definitions gives \(T_G(F_a)=a(1-2a)/(1-a)\) and \(T_P(F_a)=a(1-2a)(3a+1/2)\). Factor their difference as in the Finding. All three sites have positive mass; the empirical masses converge almost surely, and the mechanism functionals are continuous there, proving the asserted random-population limits and strict sign change. The optimum is \(Q(F_a)=\min\{a,1-2a\}/2\).

## Verification

The standalone standard-library script `verify.py` checks the rational-polynomial influence and variance identities, the Proportional quotient identity, the exact three-support formulas against direct finite-agent enumeration, 242 small exact profiles, and independent midpoint quadrature of both uniform-population integrals. Execute from this directory using `python3 verify.py`; the expected final marker is `VERIFY_OK`. A separate seeded simulation of uniform random profiles at increasing sizes corroborated the two limits and the Gaussian standard-deviation scale, but does not prove convergence. The proof above is the evidence for the infinite claims.

## Relationship to prior work

Ma and Peng (August 10, 2026) introduced Global Pair and analyzed strategyproofness and worst-case performance. Chan, Lin and Wang (August 23, 2026), and independently Jia (August 20, 2026), analyze the same two-facility distance-weighted mechanism and its mixtures with Proportional, including a sharp **worst-case** mixing rule. The classical Proportional mechanism comes from Lu and collaborators (2010). Existing Product-Gap uniform-sample results already yield the Global Pair \(7/5\) mean: that number is reproduced as a benchmark, not offered as new. The result here concerns the Proportional exact \(\pi\)-valued typical-case benchmark, the three-atom reversal, and the sharp **empirical-population conditional-cost** Gaussian law of Global Pair; neither a worst-case bound nor a Dirichlet limit for a randomly selected facility pair by itself gives that Gaussian variance.

## Limitations

The exact continuous formulas concern one-dimensional independent uniform sampling; the atomic phase diagram concerns the specified three-site symmetric law. Nothing is claimed about arbitrary densities, strategic deviations under correlated reports, optimal sample-dependent mixture selection, or a joint Gaussian limit of the two mechanisms. The sample-population Gaussian law describes expected cost after averaging mechanism randomization, not ex-post pair-selection noise. The novelty assessment is best-knowledge and not a publication-priority certificate; general empirical-process theory supplies machinery, and an equivalent specialized calculation could exist in unindexed literature. No independent scientific audit has been performed.

## References

1. Mengfan Ma and Bo Peng, *Breaking the 4-Approximation Barrier in Strategyproof Two-Facility Location*, arXiv:2608.09061, first public version August 10, 2026, https://arxiv.org/abs/2608.09061.
2. Jianhao Jia, *Product Gap Mechanisms for Multi-Facility Location*, arXiv:2608.19633, first public version August 20, 2026, https://arxiv.org/abs/2608.19633.
3. Hau Chan, Jianan Lin and Chenhao Wang, *Randomized Strategyproof Facility Location: Two Facilities and Beyond*, arXiv:2608.22484, first public version August 23, 2026, https://arxiv.org/abs/2608.22484.
4. Lu, Sun, Wang and Zhu, *Asymptotically Optimal Strategy-Proof Mechanisms for Two-Facility Games*, EC 2010, referenced for the established Proportional mechanism.
