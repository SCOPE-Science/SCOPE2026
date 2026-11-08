# Joint Gaussian–Poisson decoupling at the circular isolation threshold

## Finding

For fixed \(x\in\mathbb R\), let \(n\) independent uniform points lie on the circle of circumference one, and connect vertices whenever their geodesic circular distance is at most \(r_n=(\log n+x)/(2n)\). Denote the numbers of connected components and isolated vertices by \(K_n\) and \(I_n\). Write \(c=e^{-x/2}\), \(\mu_n=c\sqrt n\). Then

\[
\left(\frac{K_n-\mu_n}{\sqrt{\mu_n}}, I_n\right)
\ \xrightarrow{d}\ (Z,P),
\qquad Z\sim N(0,1),\quad P\sim\operatorname{Poisson}(c^2),\quad Z\perp P.
\]

Nevertheless, the *unscaled* covariance has a nonzero limit:

\[
\lim_{n\to\infty}\operatorname{Cov}(K_n,I_n)=2c^2=2e^{-x}.
\]

Thus mesoscopic component-count fluctuations and the finite isolated-vertex count become asymptotically independent, while their raw covariance does not vanish. The novelty asserted here is this **joint intermediate-scale limit and residual covariance**, not the previously known exact conditional distribution of component sizes.

## Assumptions and scope

The graph has exactly \(n\) vertices sampled independently from normalized arclength measure on \(\mathbb R/\mathbb Z\), not a Poisson-distributed vertex number. Edges depend deterministically on shortest-arc distance, with no additional bond randomness. Fix any real \(x\) throughout the limit \(n\to\infty\); the displayed radius is positive and below one half for all sufficiently large \(n\). Weak convergence is in \(\mathbb R\times\mathbb Z_{\ge0}\), with the discrete topology on its second coordinate. The covariance is defined for the same finite-\(n\) law.

Let \(G_{n,1},\ldots,G_{n,n}\) be the successive positive circular spacings of the ordered sample points. They have the uniform Dirichlet law. Define the number of *long gaps*,
\[
H_n=\sum_{i=1}^n\mathbf1\{G_{n,i}>r_n\}.
\]

With cyclic indices, the graph satisfies
\[
K_n=\max(1,H_n),\qquad
I_n=\sum_{i=1}^n\mathbf1\{G_{n,i-1}>r_n,\ G_{n,i}>r_n\}.
\]

The identities hold for all \(n\ge3\) and \(0<r_n<1/2\). When two or more long gaps exist, no edge can bypass either gap via the other side of the circle; when zero or one exists, the graph is connected. A point is isolated exactly when the two incident gaps exceed the radius.

## Proof

**1. The Gaussian component scale.** Introduce independent unit exponential variables \(E_1,\ldots,E_n\) and \(S_n=\sum_iE_i\). The vector of gaps has the distribution of \((E_i/S_n)_{i=1}^n\). Set \(t_n=nr_n=(\log n+x)/2\) and
\[
B_n=\sum_{i=1}^n\mathbf1\{E_i>t_n\}.
\]

Then \(B_n\sim\operatorname{Bin}(n,c/\sqrt n)\), with \(\mathbb EB_n=\mu_n\), \(\operatorname{Var}B_n=\mu_n(1-c/\sqrt n)\), and the binomial triangular-array central limit theorem yields
\[
(B_n-\mu_n)/\sqrt{\mu_n}\xrightarrow{d}N(0,1).
\]

To compare thresholds \(r_nS_n\) and \(t_n\), fix \(M>0\) and work on \(\{|S_n-n|\le M\sqrt n\}\), whose complementary probability is at most \(M^{-2}\). Every index contributing to \(|H_n-B_n|\) then has \(|E_i-t_n|\le Mr_n\sqrt n=O_M((\log n)/\sqrt n)\). The expected number of indices in this exponential-density window is \(O_M(\log n)\). By Markov's inequality, their number divided by \(n^{1/4}\) tends to zero in probability; subsequently send \(M\to\infty\). Hence
\[
H_n-B_n=o_{\mathbb P}(n^{1/4}),\qquad H_n/\sqrt n\xrightarrow{\mathbb P}c.
\]

Since \(|K_n-H_n|\le1\), this proves the stated component-count Gaussian limit.

**2. Conditional Poisson isolation law.** Conditional on \(H_n=h\), every \(h\)-subset of the \(n\) cyclic gap locations is equiprobable. In particular, after rooting at a uniformly chosen long gap, the successive component vertex sizes form a uniformly chosen ordered composition of \(n\) into \(h\) positive parts. This *exact conditional composition fact* is contained in Huillet's 2003 analysis and is used here as prior knowledge, not a novelty claim. For \(1\le h<n\) and each fixed integer \(k\ge0\) with \(k\le h-1\), the number of singleton parts has factorial moment
\[
\mathbb E[(I_n)_k\mid H_n=h]
=(h)_k\frac{\binom{n-k-1}{h-k-1}}{\binom{n-1}{h-1}}
=\frac{(h)_k(h-1)_k}{(n-1)_k},
\]

where \((a)_k\) is the falling factorial (and \((a)_0=1\)). If \(h/\sqrt n\to c\), these factorial moments tend to \((c^2)^k\) for every fixed \(k\). Tightness follows from the first moment; ordinary moments are polynomials in factorial moments; the Poisson distribution is moment-determinate. Thus the conditional isolation law tends to \(\operatorname{Poisson}(c^2)\) along **every** deterministic sequence \(h/\sqrt n\to c\).

Because \(H_n/\sqrt n\to c\) in probability, this conditional convergence holds in probability under the random conditioning \(H_n\). For bounded continuous \(f\) on the nonnegative integers and bounded continuous \(g\) on the real line, conditioning on \(H_n\) gives
\[
\mathbb E\left[g\!\left(\frac{K_n-\mu_n}{\sqrt{\mu_n}}\right)f(I_n)\right]
\longrightarrow \mathbb E[g(Z)]\,\mathbb E[f(P)].
\]

The product limit proves joint convergence and independence of its two coordinates.

**3. Sharp unscaled cross covariance.** For any \(j\) distinct cyclic gaps, the Dirichlet-simplex volume identity gives
\[
\Pr(G_{n,i_1}>r_n,\ldots,G_{n,i_j}>r_n)
= a_{j,n}:=(1-jr_n)_+^{n-1}.
\]

The case of one long gap, one adjacent pair, and the mixed sum therefore yields the **exact** identities
\[
\mathbb EH_n=n a_{1,n},\quad\mathbb EI_n=n a_{2,n},\quad
\mathbb E[H_nI_n]=2n a_{2,n}+n(n-2)a_{3,n},
\]

and consequently
\[
\operatorname{Cov}(H_n,I_n)
=2n a_{2,n}+n(n-2)a_{3,n}-n^2a_{1,n}a_{2,n}.
\]

Since \(a_{j,n}=c^j n^{-j/2}(1+O_x((\log n)^2/n))\) for each fixed \(j=1,2,3\), the first term tends to \(2c^2\), while the difference of the last two terms is \(O_x((\log n)^2/\sqrt n)\to0\). Finally \(K_n-H_n=\mathbf1\{H_n=0\}\), and \(I_n=0\) on that event, giving
\[
\operatorname{Cov}(K_n,I_n)-\operatorname{Cov}(H_n,I_n)
=-\Pr(H_n=0)\,\mathbb EI_n\longrightarrow0.
\]

This proves the residual covariance claim.

## Verification

Execute \(\texttt{python3 verify.py}\) with Python 3 and no external packages. It checks the exact conditional singleton distribution and factorial moments against all cyclic gap subsets for orders three through eleven, checks joint Dirichlet inclusion–exclusion probabilities and mixed moments with rational arithmetic for orders three through eight, and checks the scaling formulas numerically at three choices of the window parameter. The bundled executable passed 1048 assertions. Finite enumeration and numerical experiments are cross-checks, not substitutes for the general proof above.

## Relationship to prior work

Huillet, *Random covering of the circle: the size of the connected components* (2003), gives the exact uniform-subset/composition law used in step 2 and studies the Poisson-component regime \(nr_n=\log(n/\rho)\) and the fixed-intensity Gaussian regime \(nr_n=\rho\). The present window \(nr_n=(\log n+x)/2\) has a diverging but sublinear number of components, alongside order-one isolates, and is not one of those two stated limit regimes. The full finite conditional formula is prior art; the joint intermediate-scale Gaussian–Poisson law and nonzero covariance limit are the proposed addition.

Zhao, Yağan and Gligor (2015) identify the isolation-versus-connectivity threshold gap for points on an **interval**, not this joint law on a circle. Decreusefond and Ferraz (2011) study a **Poisson** number of points and component counts, including a circle variant, without this fixed-size joint limit. Holst and Hüsler (1984) consider joint limits of gap number with vacancy and extreme gap lengths; their unavailable full text is a priority risk. Penrose (2018) treats Poisson approximation for finite component-size counts in a broader random connection model; that does not by itself yield joint convergence with the mesoscopic total component count.

## Limitations

The theorem applies only to uniform fixed-size sampling on the one-dimensional circle, the hard distance-threshold rule, and fixed \(x\) in the stated critical window. It does not give convergence rates, uniformity in an unbounded window parameter, or results for soft graphs, other dimensions, or variable point counts. No uniform error bound or independent historical uniqueness determination is asserted. The 1984 Holst–Hüsler full text was not accessed, so an implicit overlap cannot be ruled out. The known 2003 full joint finite-size formulas are acknowledged as coverage of those **finite conditional identities**, rather than presented as novel.

## References

1. T. Huillet, *Random covering of the circle: the size of the connected components*, Advances in Applied Probability **35** (2003), 563–582, https://doi.org/10.1239/aap/1059486818. Author-uploaded full text: https://www.researchgate.net/publication/38349613_Random_covering_of_the_circle_the_size_of_the_connected_components.
2. J. Zhao, O. Yağan, V. Gligor, *A curious gap in one-dimensional geometric random graphs between connectivity and the absence of isolated node*, arXiv:1502.00404, initially posted 2015-02-02, https://arxiv.org/abs/1502.00404.
3. L. Decreusefond, E. Ferraz, *On the One Dimensional Poisson Random Geometric Graph*, Journal of Probability and Statistics (2011), article 350382, https://doi.org/10.1155/2011/350382.
4. L. Holst and J. Hüsler, *On the random coverage of the circle*, Journal of Applied Probability **21** (1984), 558–566, https://doi.org/10.2307/3213617.
5. M. D. Penrose, *Inhomogeneous random graphs, isolated vertices, and Poisson approximation*, Journal of Applied Probability **55** (2018), 112–136, https://doi.org/10.1017/jpr.2018.9.
