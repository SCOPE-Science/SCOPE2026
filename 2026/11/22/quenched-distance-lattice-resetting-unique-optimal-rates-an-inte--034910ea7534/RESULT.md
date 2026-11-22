# Quenched-distance lattice resetting: unique optimal rates, an integrability edge, and a rare-tail exponent

## Finding
Consider a one-dimensional continuous-time nearest-neighbor random walk absorbed at the origin, with unit-rate jumps to each neighboring site and independent Poisson resets of rate \(r>0\). Before the walk starts, a positive integer \(J\) is drawn once; every reset returns to that *same* site \(J\). For any probability law \(p_j=\Pr(J=j)\), let \(M(r)=\mathbb E_J\mathbb E[T_r\mid J]\), the population-average mean absorption time.

Set
\[
y=y(r)=\frac{r+2+\sqrt{r^2+4r}}2,\quad r=\frac{(y-1)^2}{y},\quad c_\ell=\Pr(J>\ell),\quad A(y)=\sum_{\ell=0}^{\infty}c_\ell y^\ell.
\]
Let \(R\in[1,\infty]\) be the radius of convergence of \(A\). The following gives a complete optimum classification, including cases where some rates have infinite population-average passage time.

**Exact functional and optimization.** For all \(r>0\), with extended-value interpretation,
\[
M(r)=\frac{yA(y)}{y-1}.
\]
If \(R=1\), \(M(r)=\infty\) at every \(r>0\). If \(R>1\) and \(\Pr(J\ge2)>0\), define, wherever \(A\) is finite,
\[
N(y)=y(y-1)A'(y)-A(y).
\]
Then \(N\) is strictly increasing for \(1<y<R\), beginning with \(N(1)=-\mathbb E J<0\). Consequently the finite part of \(M\) has at most one stationary point, necessarily its strict global minimum. For finite-support laws with positive mass beyond site 1, this point always exists and is the **unique globally optimal finite reset rate**. More generally, if \(R<\infty\), \(A(R)<\infty\), and \(A'(R)<\infty\), a zero \(N(y)=0\) occurs inside \((1,R)\) exactly when \(N(R)>0\); otherwise the global optimum is the finite boundary \(y=R\), or \(r=(R-1)^2/R\). If either \(A(R)\) or \(A'(R)\) diverges, the unique optimum lies in the interior. If \(R=\infty\) and \(\Pr(J\ge2)>0\), it likewise lies in the interior. For \(\Pr(J=1)=1\), \(M\) decreases strictly to an unattained infimum of 1 as \(r\to\infty\).

**A finite optimum at an integrability edge.** Set \(p_j=C2^{-j}j^{-6}\) for \(j\ge2\), where \(C^{-1}=\sum_{j=2}^{\infty}2^{-j}j^{-6}\), and \(p_1=0\). Then \(R=2\), the average passage time is finite for \(0<r\le1/2\) and infinite for \(r>1/2\). Moreover \(N(2)<0\), so the unique global optimum is \(r_*=1/2\), precisely the finite-moment boundary rather than an interior critical point.

**Universal rare-distance law.** Fix an integer \(K\ge2\) and a probability vector \(q_2,\ldots,q_K\) with \(q_K>0\). For \(0<\varepsilon<1\), draw \(J=1\) with probability \(1-\varepsilon\) and \(J=j\ge2\) with probability \(\varepsilon q_j\). The unique optimal reset rate and minimum average mean absorption time satisfy, as \(\varepsilon\downarrow0\),
\[
r_\varepsilon^*\sim[(K-1)q_K\varepsilon]^{-1/K},\qquad
\min_{r>0}M_\varepsilon(r)
=1+\frac{K}{(K-1)^{(K-1)/K}}(q_K\varepsilon)^{1/K}+o(\varepsilon^{1/K}).
\]
Thus the farthest *nonzero-probability* initial distance controls the singular optimizing exponent, however rare that class is. In the exact two-point example with \(q_2=1\), the optimizer in the \(y\) coordinate is \(y_* =1+\sqrt{1+1/\varepsilon}\).

## Assumptions and scope
The state space is the nonnegative integers; state 0 is absorbing, and all sites \(j\ge1\) have two ordinary jump clocks of rate 1 each, with the jump from 1 to 0 absorbed. The initial distance \(J\) is sampled *once per experiment* and is fixed throughout its resetting trajectory. Resets are instantaneous and independent of the jump clocks. The expectation over \(J\) is taken *after* the conditional mean time; this is a quenched-distance population average, and it is not the process in which the resetting site is independently redrawn every cycle. The result concerns mean first passage, not its higher moments or quantiles. At \(r=0\), the unreset one-dimensional walk has infinite mean absorption time for every \(J\ge1\).

## Proof
**1. Conditional mean.** The reset-free walk, started at \(j\), has first-hit Laplace transform \(h_j(r)=a(r)^j\), where \(0<a(r)<1\) solves \(a+a^{-1}=2+r\). Indeed \((2+r)h_j=h_{j-1}+h_{j+1}\) for \(j\ge1\), with \(h_0=1\) and boundedness as \(j\to\infty\). The smaller root is \(a(r)=1/y(r)\). A renewal cycle succeeds before its independent exponential reset with probability \(h_j(r)\); its expected duration is \((1-h_j(r))/r\). Restarting identically after unsuccessful cycles yields \(\mathbb E[T_r\mid J=j]=(h_j^{-1}-1)/r=(y^j-1)/r\).

**2. Positive-series identity and finite domain.** Because \((y^j-1)/(y-1)=\sum_{\ell=0}^{j-1}y^\ell\), Tonelli's theorem, with no moment hypothesis, gives
\[
\mathbb E[y^J]-1=(y-1)\sum_{\ell\ge0}\Pr(J>\ell)y^\ell=(y-1)A(y),
\]
with extended-value meaning. Substituting \(r=(y-1)^2/y\) proves \(M=yA/(y-1)\). Positivity of the coefficients shows that \(M\) is finite precisely when \(A(y)\) is finite. Since \(c_0=1\) and the coefficients are nonnegative, its interior convergence domain is \(1<y<R\), possibly including \(R\) itself. In particular \(R=1\) makes every positive-rate population mean infinite.

**3. All finite-domain optima.** On \((1,R)\) termwise differentiation is valid and yields
\[
\frac{dM}{dy}=\frac{N(y)}{(y-1)^2},\qquad
N'(y)=(y-1)[2A'(y)+yA''(y)]>0,
\]
provided \(\Pr(J\ge2)>0\). For \(R>1\), \(A(1)=\mathbb E J<\infty\), so \(N(1)=-\mathbb E J<0\) and \(M(y)\to\infty\) as \(y\downarrow1\). If \(R=\infty\), the positive weight at some site \(j\ge2\) gives \(M(y)\ge p_j y(y^j-1)/(y-1)^2\to\infty\) as \(y\to\infty\), ensuring a unique zero of \(N\). If \(R<\infty\) and \(A(R)=\infty\), the same left-end and right-end divergence force the zero. If \(A(R)<\infty\) but \(A'(R)=\infty\), then \(N(y)\to\infty\), so there is again a unique zero. If both boundary values are finite, strict monotonicity of \(N\) gives an interior zero exactly when \(N(R)>0\); otherwise \(M\) decreases to its attained boundary minimum. For \(J\equiv1\), \(A=1\), and \(M(y)=y/(y-1)\) decreases to 1.

**4. The integrability-edge construction.** For \(p_j=C2^{-j}j^{-6}\), the geometric root test gives \(R=2\). Both \(A(2)\) and \(A'(2)\) are finite, since their series have respective \(j^{-6}\) and \(j^{-5}\) tails. Direct substitution in \(N(2)=2A'(2)-A(2)\) gives
\[
N(2)=C\sum_{j=2}^{\infty}\frac{j-3+3\cdot2^{-j}}{j^6}.
\]
The term at \(j=2\) equals \(-1/256\). The positive terms at \(j\ge3\) are strictly bounded by
\[
\frac{3}{8\cdot3^6}+\frac1{4^5}+\int_4^\infty x^{-5}\,dx+\frac3{4^6}\sum_{j=4}^\infty2^{-j}
=\frac1{1944}+\frac2{1024}+\frac3{32768}<\frac1{256}.
\]
Consequently \(N(2)<0\). With \(r(2)=1/2\), the claimed unique boundary optimum and divergence beyond it follow. This argument uses only exact rational inequalities.

**5. Rare-distance scaling.** The finite-support mixture has \(A_\varepsilon(y)=1+\varepsilon\sum_{j=2}^Kq_j\sum_{\ell=1}^{j-1}y^\ell\). Hence \(N_\varepsilon(y)=-1+\varepsilon P(y)\) where \(P\) is a polynomial of degree \(K\) and positive leading coefficient \((K-1)q_K\). The unique zero therefore tends to infinity and satisfies \(y_\varepsilon^*\sim[(K-1)q_K\varepsilon]^{-1/K}\), with \(r(y)/y\to1\). At this root, the exact expression for \(M_\varepsilon\) has uniform expansion
\[
M_\varepsilon(y_\varepsilon^*)=1+(y_\varepsilon^*)^{-1}
+\varepsilon q_K(y_\varepsilon^*)^{K-1}
+o(\varepsilon^{1/K}),
\]
where all lower-degree terms and \((y_\varepsilon^*)^{-2}\) are smaller. The root identity implies \(\varepsilon q_K(y_\varepsilon^*)^{K-1}\sim[(K-1)y_\varepsilon^*]^{-1}\), giving the displayed optimal value. For \(K=2\), \(A=1+\varepsilon y\), \(N=-1+\varepsilon(y^2-2y)\), with the stated exact positive root.

## Verification
`checker.py` uses the Python standard library and can be run with `python checker.py`. It compares the exact mean against an independently implemented finite-volume tridiagonal first-passage equation, checks derivative identities and unique finite-support optima across randomly generated mixture laws, and verifies the rare-distance scaling for several finite cutoffs and rarity levels. The code's finite examples do not establish the infinite-support theorem; its proof is the positive-series and strict-monotonicity argument above. The integrability-edge example is certified by the explicit rational series bound, not by truncation or a computer output.

## Relationship to prior work
Hartmann and Majumdar (2025), section V.A, equation (39), obtain the exact mean first-passage formula for a **fixed** reset location and analyze its optimization for a given starting site. That conditional formula is used and credited here. Their paper credits an earlier fixed-site one-dimensional derivation to Christophorov (2021). The new distinction is that a starting/reset location is sampled once from a possibly unbounded distribution, and optimization concerns the *average of conditional first-passage times*. This gives a monotone tail-generating-function criterion, an integrability-edge optimizer, and the farthest-distance singular scaling. These are not obtained merely by stating a fixed-site optimum for each population member. Distributed-reset optimization with a newly resampled reset position studies a different renewal law and does not imply this quenched-distance conclusion: Julián-Salgado, Dagdug and Boyer (2025), section II, explicitly resample positions independently at every reset. García-Valladares, Prados, Manacorda and Plata (2025/2026) instead draw a single fixed *target* in a finite continuous interval and optimize a possibly spatially dependent bulk-reset rate; that distinct boundary and control problem likewise does not supply the present lattice integrability/unique-optimum classification.

## Limitations
The theorem is one-dimensional with symmetric unit-rate jumps and instantaneous Poisson resetting to an immutable sampled site. In particular, it does not classify independent fresh-site resetting, two-dimensional walks, partial absorption, or finite-time quantile objectives. The optimizer's uniqueness at the integrability edge includes the possibility that arbitrarily nearby larger reset rates have infinite *population-average* mean, despite every fixed-site conditional mean remaining finite. The novelty comparison is based on inspected primary sources and indexed results and cannot exclude every unpublished or unindexed equivalent theorem. No independent mathematical audit has been performed.

## References
- A. K. Hartmann and S. N. Majumdar, *Diffusion with stochastic resetting on a lattice*, arXiv:2505.19903 (first posted 2025-05-26); Physical Review E **112**, 034102 (2025), DOI:10.1103/1xkk-7q63, especially equation (39). https://arxiv.org/abs/2505.19903
- N. Christophorov, *Peculiarities of random walks with resetting in a one-dimensional chain*, Journal of Physics A **54**, 015001 (2021), DOI:10.1088/1751-8121/abc765 (preceding fixed-site result, as cited in Hartmann and Majumdar).
- E. García-Valladares, C. A. Plata, A. Prados, A. Manacorda, *Optimal resetting strategies for search processes in heterogeneous environments*, arXiv:2305.14245 (2023), DOI:10.1088/1367-2630/ad06da (heterogeneous resetting in a continuous-space setting). https://arxiv.org/abs/2305.14245
- P. Julián-Salgado, L. Dagdug, D. Boyer, *Abrupt transitions in the optimization of diffusion with distributed resetting*, arXiv:2507.14483 (2025) (freshly sampled reset-position protocol, distinct from fixed-quenched starting distances). https://arxiv.org/abs/2507.14483
- G. García-Valladares, A. Prados, A. Manacorda, C. A. Plata, *How target distributions shape optimal stochastic resetting*, arXiv:2505.16626 (first submitted 2025-05-22), Phys. Rev. E **113**, 024107 (2026) (finite-interval, fixed-random-target Brownian search). https://arxiv.org/abs/2505.16626
