# Log-clock Lamperti universality and the exact mean-bias boundary for fractional trial-driven telegraphs

## Finding

Consider independent Bernoulli directions and Mittag–Leffler holding times indexed by the *number of previous visits to the same direction*, as in the Bernoulli telegraph of Pote and Kataria [1]. The following is a single occupation-time theorem, including its exact finite-count identity and logarithmic rare-direction boundary.

For each integer \(n\ge1\), let \(p_n\in(0,1)\), let \(M_n\sim\operatorname{Bin}(n,p_n)\), and put \(K_n=n-M_n\). Independently of the trials, take two mutually independent sequences of positive holding times \((R_j)_{j\ge1}\) and \((L_j)_{j\ge1}\) with Laplace transforms
\[
\mathbb E e^{-sR_j}=\frac{j\lambda}{j\lambda+s^\alpha},\qquad
\mathbb E e^{-sL_j}=\frac{j\mu}{j\mu+s^\alpha},\qquad s\ge0,
\]
where \(0<\alpha\le1\) and \(\lambda,\mu>0\). These are precisely the two directional Mittag–Leffler sequences in [1]. Define the completed positive/negative residence times and the completed positive occupation fraction by
\[
A_n=\sum_{j=1}^{M_n}R_j,\quad B_n=\sum_{j=1}^{K_n}L_j,\quad F_n=\frac{A_n}{A_n+B_n},
\]
with an empty sum equal to zero. Their sum is the time of the \(n\)-th completed motion interval; if the two physical velocities are \(+v_1\) and \(-v_2\), the average velocity at this event time is \((v_1+v_2)F_n-v_2\).

**(i) Exact exponent-invariance of the finite-count mean.** Let \(G_m\) and \(G'_k\) be independent maxima of \(m\) and \(k\) independent unit-rate exponential variables, respectively, with \(G_0=G'_0=0\), and independent of \(M_n\). For every \(n\ge1\) and every \(0<\alpha\le1\),
\[
\boxed{\mathbb E F_n=\mathbb E\frac{\mu G_{M_n}}{\mu G_{M_n}+\lambda G'_{n-M_n}}.}
\]
Thus the expected completed-time occupation fraction is *exactly independent* of the fractional index \(\alpha\), even though the holding-time laws have infinite mean when \(\alpha<1\).

**(ii) Sharp log-clock universality and thinning boundary.** Assume the two limits
\[
\beta_+=\lim_{n\to\infty}\frac{\log(1+np_n)}{\log n},\qquad
\beta_-=\lim_{n\to\infty}\frac{\log(1+n(1-p_n))}{\log n}
\]
exist. Then \(0\le\beta_\pm\le1\) and \(\max(\beta_+,\beta_-)=1\). Let \(Z_+\) and \(Z_-\) be independent nonnegative variables with
\[
\mathbb E e^{-sZ_+}=\exp\left(-\frac{\beta_+}{\lambda}s^\alpha\right),\qquad
\mathbb E e^{-sZ_-}=\exp\left(-\frac{\beta_-}{\mu}s^\alpha\right).
\]
Here a zero coefficient produces a zero variable; when \(\alpha=1\), the variables are the displayed deterministic coefficients. Then
\[
\boxed{\left(\frac{A_n}{(\log n)^{1/\alpha}},\frac{B_n}{(\log n)^{1/\alpha}},F_n\right)
\Longrightarrow\left(Z_+,Z_-,\frac{Z_+}{Z_++Z_-}\right).}
\]
For \(0<\alpha<1\) and \(a=\beta_+/\lambda>0\), \(b=\beta_-/\mu>0\), the last coordinate has the Lamperti stable-ratio density
\[
\boxed{f(r)=\frac{ab\sin(\pi\alpha)}{\pi}\,
\frac{r^{\alpha-1}(1-r)^{\alpha-1}}
{a^2(1-r)^{2\alpha}+b^2r^{2\alpha}+2ab\cos(\pi\alpha)r^\alpha(1-r)^\alpha}},\quad 0<r<1.}
\]
If \(a=0\), the ratio limit equals zero; if \(b=0\), it equals one. If \(\alpha=1\), it is the constant \(a/(a+b)\). In every case,
\[
\boxed{\lim_{n\to\infty}\mathbb E F_n=\frac{a}{a+b}.}
\]
In particular, **every fixed** \(p_n=p\in(0,1)\) gives \(a=1/\lambda\), \(b=1/\mu\), so the leading occupation law is independent of the direction-trial bias. By contrast, if \(p_n=n^{-\delta}\) with \(0<\delta<1\), then \(\beta_+=1-\delta\), \(\beta_-=1\), and the limiting mean is \((1-\delta)\mu/((1-\delta)\mu+\lambda)\). For \(\delta\ge1\), the positive fraction tends to zero. This is the precise polynomial-thinning boundary of fixed-bias universality.

**(iii) First recovery of the hidden trial bias.** For any fixed \(p_n=p\in(0,1)\), *uniformly in the choice of* \(0<\alpha\le1\),
\[
\boxed{\mathbb E F_n=\frac{\mu}{\lambda+\mu}
+\frac{\lambda\mu}{(\lambda+\mu)^2}\frac{\log(p/(1-p))}{\log n}
+O_{p,\lambda,\mu}\bigl((\log n)^{-2}\bigr).}
\]
Thus the trial bias, absent from the leading limiting law, first enters the mean through its log odds at order \(1/\log n\). The exact finite-count identity makes this coefficient independent of the fractional index.

## Assumptions and scope

All claims refer to the first \(n\) **completed motion intervals**, not to residence times stopped at a deterministic physical time. For the triangular experiment, the independent Bernoulli directions have a common within-row success probability \(p_n\), with no coupling across rows required. Direction-specific holding times use the occurrence index in that direction; replacing it by the global trial index changes the model. The parameters \(\alpha,\lambda,\mu\) are fixed as \(n\to\infty\). The stable-ratio density requires \(0<\alpha<1\) and both limiting effective directional intensities positive; endpoint cases are stated separately. Empty sums and exponential maxima are zero; since \(n\ge1\) and holding times are positive, the denominator of \(F_n\) is positive almost surely.

## Proof

**Step 1 (exact operational-time representation).** Let \(D_\alpha(t)\) denote a positive stable subordinator, with \(\mathbb E e^{-sD_\alpha(t)}=e^{-ts^\alpha}\). For \(\alpha=1\), take \(D_1(t)=t\). If \(E_j\) is exponential with rate \(j\lambda\), then \(D_\alpha(E_j)\) has Laplace transform \(j\lambda/(j\lambda+s^\alpha)\). Independent increments imply that the sum of the first \(m\) such waiting times has the same distribution as \(D_\alpha(H_m^{\lambda})\), where \(H_m^\lambda\) is a sum of independent exponentials of rates \(\lambda,2\lambda,\ldots,m\lambda\). The exponential spacing identity gives
\[
H_m^\lambda\stackrel d=G_m/\lambda,
\]
where \(G_m\) is the maximum of \(m\) independent unit-rate exponentials. The two directions are independent conditionally on \(M_n\). Hence, with independent stable subordinators,
\[
(A_n,B_n)\mid(M_n=m)\stackrel d=
\bigl(D_\alpha(G_m/\lambda),\widetilde D_\alpha(G'_{n-m}/\mu)\bigr).
\]
The equality is distributional, not a claim of a pathwise identification with an existing renewal process.

**Step 2 (exact mean ratio for stable clocks).** For independent positive stable \(U,V\) with Laplace transforms \(e^{-as^\alpha}\), \(e^{-bs^\alpha}\), where \(a,b\ge0\) and \(a+b>0\), Tonelli and differentiation under the Laplace transform give
\[
\mathbb E\frac{U}{U+V}
=\int_0^\infty \mathbb E[Ue^{-tU}]\,\mathbb E[e^{-tV}]\,dt
=\int_0^\infty a\alpha t^{\alpha-1}e^{-(a+b)t^\alpha}\,dt
=\frac{a}{a+b}.
\]
For \(\alpha=1\) this is immediate because both clocks are constants. Conditional on the two exponential maxima in Step 1, take \(a=G_m/\lambda\) and \(b=G'_k/\mu\) to obtain the exact finite-count identity in (i), including one-direction-empty cases.

**Step 3 (joint logarithmic stable limit).** Conditional on \(M_n=m\), the joint Laplace transform is the exact product
\[
\mathbb E[e^{-u A_n-v B_n}\mid M_n=m]
=\prod_{j=1}^{m}\frac{j\lambda}{j\lambda+u^\alpha}
\prod_{j=1}^{n-m}\frac{j\mu}{j\mu+v^\alpha}.
\]
Write \(L=\log n\), \(r_n=L^{1/\alpha}\) and \(H_m=\sum_{j=1}^{m}1/j\), with \(H_0=0\). For fixed \(s,t\ge0\), after setting \(u=s/r_n\), \(v=t/r_n\), expansion of \(\log(1+x)\), with \(\sum_{j\ge1}j^{-2}<\infty\), gives *uniformly in* \(m\in\{0,\ldots,n\}\),
\[
\log\mathbb E[e^{-(sA_n+tB_n)/r_n}\mid M_n=m]
=-\frac{s^\alpha}{\lambda L}H_m-\frac{t^\alpha}{\mu L}H_{n-m}
+O_{s,t,\alpha,\lambda,\mu}(L^{-2}).
\]
Under the assumed logarithmic limits of the binomial means, \(H_{M_n}/L\to\beta_+\) and \(H_{n-M_n}/L\to\beta_-\) in probability. Indeed, if \(np_n=n^{\beta_++o(1)}\) with \(\beta_+>0\), binomial concentration yields \(M_n/(np_n)\to1\); if \(\beta_+=0\), Markov's inequality gives \(M_n<n^\varepsilon\) with probability tending to one for each \(\varepsilon>0\). The second coordinate is identical. Conditional transforms are bounded by one, so averaging yields the product Laplace transform of the independent stable limits. As \(n p_n+n(1-p_n)=n\), at least one exponent equals one. Hence the two stable limits cannot both vanish, and continuity of \((x,y)\mapsto x/(x+y)\) away from the origin proves the joint assertion with the fraction.

**Step 4 (Lamperti density and limiting mean).** Put \(a=\beta_+/\lambda\), \(b=\beta_-/\mu\). For \(a,b>0\), the Stieltjes transform of the stable ratio \(R=Z_+/(Z_++Z_-)\), obtained using the same Laplace differentiation as Step 2, is
\[
\mathbb E\frac1{z+R}=
\frac{a(z+1)^{\alpha-1}+bz^{\alpha-1}}
{a(z+1)^\alpha+bz^\alpha},\qquad z>0.
\]
Stieltjes inversion on the cut \((-1,0)\) yields exactly the density displayed in (ii); it has no endpoint atom because both positive stable variables are strictly positive. The boundedness \(0\le F_n\le1\) and weak convergence give convergence of expectations, whose value equals \(a/(a+b)\) by Step 2. If one effective coefficient is zero, the corresponding stable variable is zero and the ratio is an endpoint constant.

**Step 5 (sharp finite-count bias correction).** Fix \(p_n=p\in(0,1)\), set \(q=1-p\), and let \(G_m,G'_k\) be as in (i). Conditional on typical \(M_n\),
\[
\mathbb E G_{M_n}=\log n+\log p+\gamma+O_{p}(n^{-1}),\qquad
\mathbb E G'_{n-M_n}=\log n+\log q+\gamma+O_p(n^{-1}),
\]
where \(\gamma\) is Euler's constant. This uses \(\mathbb E G_m=H_m=\log m+\gamma+O(m^{-1})\) and exponentially small binomial tails. Both \(G_{M_n}-\log n\) and \(G'_{n-M_n}-\log n\) have uniformly bounded second moments for fixed \(p\), since \(\operatorname{Var}(G_m)=\sum_{j=1}^{m}j^{-2}\le\pi^2/6\) and the count is concentrated on a linear scale. Write \(G_{M_n}=L+U_n\) and \(G'_{n-M_n}=L+V_n\). A second-order Taylor estimate for the bounded ratio \(\mu(L+U_n)/(\mu(L+U_n)+\lambda(L+V_n))\), on \(|U_n|+|V_n|\le L/2\), and a second-moment bound on its complement show that
\[
\mathbb E F_n=\frac{\mu}{\lambda+\mu}
+\frac{\lambda\mu}{(\lambda+\mu)^2}\frac{\mathbb E U_n-\mathbb E V_n}{L}
+O_{p,\lambda,\mu}(L^{-2}).
\]
Here \(\mathbb E U_n-\mathbb E V_n=\log(p/q)+O_p(n^{-1})\), so the displayed formula (iii) follows. Every step after the exact expectation identity is free of \(\alpha\), establishing the advertised uniformity.

## Verification

The independently constructed finite-state weighted recursion and the binomial-mixture transform agree in exact rational arithmetic for \(n=1,\ldots,25\) in a nontrivial fractional case. Numerical integration of the Stieltjes-inversion density checks its normalization and mean for four parameter triples. Simulated exponential maxima check the predicted log-odds coefficient at success probabilities away from \(1/2\); this simulation is diagnostic, not the proof. The accompanying `checker.py` reproduces deterministic checks using the Python standard library. The infinite limits and first-order correction are established by Steps 1–5; no finite computation is presented as an exhaustive infinite verification.

## Relationship to prior work

Pote and Kataria [1] introduced the indicated direction-indexed Mittag–Leffler holding times and derived finite-event arrival-time and position densities, but do not state the logarithmic joint occupation law, polynomial thinning boundary, exact invariance of the finite-count occupation mean across \(\alpha\), or its sharp log-odds correction. Crimaldi, Di Crescenzo, Iuliano and Martinucci [2] solved the exponential directional-clock case, including logistic stationary *physical-position* behavior under a parameter balance; their \(\alpha=1\) positional law must not be mistaken for the present \(\alpha<1\) event-indexed stable occupation theorem. Classical Lamperti stable-ratio laws [3,4] supply the known ratio family; here the new input is its operational-time realization with direction-indexed varying clocks, the Bernoulli-propensity universality and thinning boundary, and the exact finite-size bias-invariant mean plus its first correction. General fractional-Poisson subordination [5] explains the Mittag–Leffler/stable connection but does not identify these marked direction-count laws.

## Limitations

The result concerns completed intervals at a fixed **event index**, not occupation at fixed physical time, and it does not assert a stationary velocity process. No result is claimed for direction-dependent fractional indices, dependent trial sequences, or an index attached to the global rather than directional event number. Weak convergence of occupation fractions alone does not imply any assertion about almost-sure convergence. The result has not received an independent mathematical audit, and broad historical-priority uncertainty remains concerning nonhomogeneous stable-occupation results not identified in the searched sources.

## References

[1] R. B. Pote and K. K. Kataria, *On a Telegraph Process with Generalized Mittag-Leffler Waiting times and Velocity Driven by Random trials*, arXiv:2608.23301v1 (first publicly posted 2026-08-24), https://arxiv.org/abs/2608.23301 . Primary MSC2020: 60K15.

[2] I. Crimaldi, A. Di Crescenzo, A. Iuliano and B. Martinucci, *A generalized telegraph process with velocity driven by random trials*, arXiv:1209.3006v1 (2012), later *Advances in Applied Probability* 45 (2013), 1111–1136, https://arxiv.org/abs/1209.3006 .

[3] J. Lamperti, *An occupation time theorem for a class of stochastic processes*, *Transactions of the American Mathematical Society* 88 (1958), 380–387, https://doi.org/10.2307/1993222 .

[4] T. Akimoto, *Statistics of the number of renewals, occupation times and correlation in ordinary, equilibrium and aging alternating renewal processes*, arXiv:2306.00359v1 (2023), https://arxiv.org/abs/2306.00359 .

[5] M. M. Meerschaert, E. Nane and P. Vellaisamy, *The fractional Poisson process and the inverse stable subordinator*, arXiv:1007.5051 (2010), https://arxiv.org/abs/1007.5051 .
