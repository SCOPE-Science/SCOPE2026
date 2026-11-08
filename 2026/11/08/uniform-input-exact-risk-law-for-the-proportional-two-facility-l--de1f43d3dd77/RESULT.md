# Uniform-input exact risk law for the Proportional two-facility lottery

## Finding

Consider independent uniform locations on \([0,1]\) and the truthful-report Proportional two-facility mechanism (a uniformly drawn anchor, followed by a second report chosen in proportion to its distance from the anchor). Its conditional expected social cost divided by the optimal two-facility cost converges almost surely, as the number of agents increases, to
\[
\rho_{\mathrm P}=\frac{7\pi}{12}-\frac49=1.3881512701\ldots .
\]
The **realized**, rather than conditional expected, approximation ratio converges in distribution to a nondegenerate random variable \(R\), with
\[
\mathbb E R=\frac{7\pi}{12}-\frac49,\qquad
\mathbb E R^2=\frac{154}{75},\qquad
\operatorname{Var}R=\frac{154}{75}-\left(\frac{7\pi}{12}-\frac49\right)^2.
\]
Its two endpoint probabilities have the exact asymptotics
\[
\Pr( R\le 1+\varepsilon)\sim\frac{4\pi}{5\sqrt2}\varepsilon,
\qquad
\Pr(R>4-\varepsilon)\sim\frac{\varepsilon^3}{384}
\quad(\varepsilon\downarrow0).
\]
Thus an optimal-in-the-limit lottery draw is rare at a linear rate, whereas a nearly worst realized draw has cubic probability. The support of \(R\) is exactly \([1,4]\).

For comparison, Pairwise-Distance (also called Global Pair) has asymptotic conditional mean ratio \(7/5\), near-optimal probability constant \(3\pi/(4\sqrt2)\), and upper-tail constant \(1/256\) in the same model. The Proportional rule has strictly smaller typical mean and both better endpoint constants, although no all-threshold stochastic dominance is claimed. For a profile-independent mixture choosing Proportional with probability \(\lambda\), its asymptotic conditional mean ratio is \(\lambda\rho_{\mathrm P}+(1-\lambda)7/5\); this applies in particular to the published worst-case-optimal Hybrid-Distance weight \(\lambda=(5+4\sqrt3)/23\).

## Assumptions and scope

For each integer \(n\ge3\), let \(X_1,\ldots,X_n\) be i.i.d. \(\operatorname{Uniform}[0,1]\) reports, with all distances absolute. All agents report truthfully. The Proportional mechanism chooses \(I\) uniformly in \(\{1,\ldots,n\}\), then chooses \(J\ne I\) with probability
\[
\Pr(J=j\mid I=i,X_1,\ldots,X_n)
=\frac{|X_i-X_j|}{\sum_{\ell=1}^{n}|X_i-X_\ell|}.
\]
It opens at the two selected reports. Let \(F_n\) be the realized *per-agent* cost and let \(O_n\) be the smallest possible per-agent social cost of two freely placed facilities (not necessarily at reports). Write \(R_n=F_n/O_n\) and \(Q_n=\mathbb E[R_n\mid X_1,\ldots,X_n]\), conditioning only on reports. Almost surely \(O_n>0\), since reports are continuous and \(n\ge3\). All convergence of empirical profiles below concerns the natural infinite i.i.d. coupling. In contrast to \(Q_n\), \(R_n\) retains the mechanism's independent lottery randomness.

Define \(h(u)=\int_0^1|u-z|\,dz=u^2-u+1/2\). The limiting ordered pair has first-coordinate density uniform, conditional second-coordinate density \(|u-v|/h(u)\). Equivalently, sorting its selected sites \(U<V\), their joint density on \(0<u<v<1\) is
\[
q_{\mathrm P}(u,v)=(v-u)\left[\frac1{h(u)}+\frac1{h(v)}\right].
\]
Set \(a=u\), \(b=v-u\), \(c=1-v\). Thus \(a,b,c\ge0\), \(a+b+c=1\); with \(s=a+c\), \(d=a-c\),
\[
R=4(a^2+c^2)+2b^2
 =1+4\left(s-\frac12\right)^2+2d^2.
\]
The limiting ratio law is completely specified by these equations.

## Proof

**1. Mechanism limit.** Let \(\mu_n=n^{-1}\sum_i\delta_{X_i}\) and \(\mu\) be the uniform probability measure. Almost surely \(\mu_n\Rightarrow\mu\), and consequently \(\sup_{u\in[0,1]}|h_n(u)-h(u)|\to0\) for \(h_n(u)=\int|u-z|\,\mu_n(dz)\); one may use a finite Lipschitz net or convergence in \(W_1\) on the compact interval. Because \(h\ge1/4\), \(h_n\) is uniformly bounded away from zero eventually. Conditional on the reports, the joint ordered selection probability measure is
\[
\mu_n(du)\frac{|u-v|}{h_n(u)}\mu_n(dv).
\]
This converges weakly to \(du\,|u-v|\,dv/h(u)\). Moreover, for
\(f_n(u,v)=\int\min\{|x-u|,|x-v|\}\,\mu_n(dx)\), the uniform bound
\(\sup_{u,v}|f_n(u,v)-f(u,v)|\le W_1(\mu_n,\mu)\to0\) holds, where \(f\) uses \(\mu\). Minimizing over \([0,1]^2\) therefore gives \(O_n\to\min f=1/8\): two medians of the equally split uniform interval are exactly \(1/4\) and \(3/4\). It follows both that \(R_n\Rightarrow R=8f(U,V)\) and that \(Q_n\to\mathbb E R\) almost surely (conditional expected costs converge by weak convergence of the selection kernels and bounded continuous integrands). These assertions also imply convergence of the unconditional mean of \(Q_n\), since the published profile-wise four-approximation bounds it by \(4\), though that extra expectation conclusion is not needed for the theorem.

**2. Limiting cost formula.** For \(u<v\), the nearest-facility boundary is \((u+v)/2\); integrating the uniform distance gives
\[
f(u,v)=\frac{u^2+(1-v)^2}{2}+\frac{(v-u)^2}{4}.
\]
The unsorted pair density follows from the first-uniform/second-distance-biased rule, and summing the two possible orders gives \(q_{\mathrm P}\). Transforming to \((a,c)\) has unit Jacobian and yields the density
\[
(1-a-c)\left(\frac1{h(a)}+\frac1{h(c)}\right),
\quad a\ge0,\ c\ge0,\ a+c\le1.
\]
Substitution of the cost expression proves the stated quadratic formula for \(R\). Its unique minimum is at \((a,c)=(1/4,1/4)\), and its maxima on the closed triangle are at \((1,0)\) and \((0,1)\), proving support \([1,4]\) by continuity and positivity of the density in the interior.

**3. Exact moments.** Let \(N_j(u)=\int_0^1|u-v|f(u,v)^j\,dv\), where \(j=1,2\). Direct integration after splitting at \(v=u\) gives the polynomial identities
\[
N_1(u)=\frac{34u^4-68u^3+54u^2-20u+5}{48},
\]
\[
N_2(u)=\frac{11(2u^2-2u+1)(11u^4-22u^3+15u^2-4u+1)}{480}.
\]
The first identity implies
\[
\frac{N_1(u)}{h(u)}
=\frac{17u^2}{24}-\frac{17u}{24}+\frac1{16}
+\frac7{48(2u^2-2u+1)}.
\]
Since \(\int_0^1(2u^2-2u+1)^{-1}du=\pi/2\), integration gives \(\mathbb E f(U,V)=7\pi/96-1/18\). The second identity immediately gives \(\mathbb E f(U,V)^2=77/2400\). Multiplication by \(8\) and \(64\) respectively produces both moment formulas.

**4. Sharp tails.** With \(s=a+c,d=a-c\), the density in \((s,d)\) coordinates is
\[
\frac{1-s}{2}\left(\frac1{h((s+d)/2)}+\frac1{h((s-d)/2)}\right),
\qquad 0\le s\le1,\quad|d|\le s.
\]
At its interior minimizer \((s,d)=(1/2,0)\) it equals \(8/5\). The ellipse \(4(s-1/2)^2+2d^2\le\varepsilon\) has area \(\pi\varepsilon/(2\sqrt2)\) and stays inside the domain for sufficiently small \(\varepsilon\). Continuity of the density gives the stated lower-tail coefficient.

Near a maximum, write \(a=1-b-c\) with \(b,c\downarrow0\) (and symmetrically interchange \(a,c\)). The deficit is
\[
4-R=8(b+c)-6b^2-8bc-8c^2,
\]
and the density in \((b,c)\) is \(4b+o(b)\), uniformly as \(b+c\to0\). The leading integration region is \(b+c<\varepsilon/8\). Each of the two corners therefore contributes \(4\int_0^{\varepsilon/8}\!\int_0^{\varepsilon/8-b}b\,dc\,db=\varepsilon^3/768\), and together they give \(\varepsilon^3/384\). There are no other maximum points, so this exhausts the event.

**5. Comparison.** The Pairwise-Distance rule draws an unordered pair with density proportional to its separation. In the uniform-input limit its triangular gap density is \(6b\); inserting the same cost \(R=4(a^2+c^2)+2b^2\) yields mean \(7/5\). At the lower-tail ellipse its \((s,d)\) density is \(3(1-s)=3/2\), giving \(3\pi/(4\sqrt2)\); at either upper-tail corner its \((b,c)\) density is \(6b\), giving \(1/256\). These are comparison facts only; the new theorem's principal claims concern Proportional.

## Verification

The standalone \(verification/checker.py\) uses exact rational polynomial integration to check both conditional cost moment polynomials at enough rational anchor points to imply the full polynomial identities, checks the rational second moment and numerical first moment independently, and verifies finite-population mechanism calculations and the endpoint algebra. Run using \(python3\) with no third-party packages. Independent numerical quadrature of the mechanism's oriented sampling law gave per-agent limiting mean \(0.17351890876870024\) and second moment \(0.03208333333333333\), matching \(7\pi/96-1/18\) and \(77/2400\). Finite samples illustrate convergence but do not certify the infinite-population theorem.

## Relationship to prior work

Lu, Sun, Wang, and Zhu (2010) introduced the Proportional mechanism and proved its four-approximation worst-case guarantee. Ma and Peng (2026) introduced Global Pair, analyzed its dispersion-dependent worst-case interplay with Proportional, and established a better fixed mixture. Chan, Lin, and Wang (2026) sharpened the optimal fixed-mixture worst-case ratio and studied Gap-Product. Aziz, Mackenzie, and Suzuki (2026) studied random-anchor volume extensions to more facilities. Their inspected relevant statements concern strategyproofness, worst-case performance, or multi-facility generalizations, rather than the uniform-population distribution, exact Proportional moments, or endpoint event probabilities established here. The distinct gap-weighted Pairwise-Distance law cannot be substituted for the uniform-anchor Proportional law because the anchor marginals differ.

## Limitations

This is a distribution-specific theorem for independent uniform locations on a segment and truthful reports. The near-optimal and near-worst-tail statements take the population limit before \(\varepsilon\downarrow0\); they are not uniform finite-population estimates. The realized limiting ratio is random, whereas the conditional expected approximation ratio converges to a constant; no claim that finite-population realized second moments converge is made. There is no claim that Proportional stochastically dominates Pairwise-Distance at all thresholds, or that average-case superiority holds for every population distribution. Originality checks may miss unindexed or unpublished equivalent analyses; no independent scientific audit has been performed.

## References

- P. Lu, X. Sun, Y. Wang, and Z. A. Zhu, *Asymptotically Optimal Strategy-Proof Mechanisms for Two-Facility Games*, EC 2010, DOI: https://doi.org/10.1145/1807342.1807393.
- M. Ma and B. Peng, *Breaking the 4-Approximation Barrier in Strategyproof Two-Facility Location*, first posted 2026-08-10, https://arxiv.org/abs/2608.09061.
- H. Aziz, S. Mackenzie, and M. Suzuki, *Anchoring for Truthfulness: The Random-Anchor Volume Mechanism for Multi-Facility Location*, first posted 2026-08-17, https://arxiv.org/abs/2608.16550.
- H. Chan, J. Lin, and C. Wang, *Randomized Strategyproof Facility Location: Two Facilities and Beyond*, first posted 2026-08-23, https://arxiv.org/abs/2608.22484.
