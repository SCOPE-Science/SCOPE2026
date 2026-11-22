# A sharp invariant-measure birth and equal statistical basins at a discontinuous quadratic border

## Finding

Consider the quadratic member of the fixed-point-free power-map family of Lawnik, Moysis and Volos, with the natural symmetric parameters \(a=b=1/2\), power \(d=2\), and remaining parameter \(0<c\le 1/2\):
\[
F_c(x)=\begin{cases}
\frac12+2x-2x^2,&0\le x\le\frac12,\\[2pt]
4c(x-\frac12)^2,&\frac12<x\le1.
\end{cases}
\]
The left endpoint \(x=1/2\) belongs to the **upper** branch. The map has no fixed point for any \(c\) in the stated range.

Put \(c_*=27/64\). The following three statements classify every orbit and every invariant Borel probability on \([0,1]\).

**(i) Subcritical absence of stationary probability.** If \(0<c<c_*\), there is no periodic orbit and no invariant Borel probability measure. For **every** initial \(x\in[0,1]\), its \(\omega\)-limit set is \(\{0,1/2\}\), and its empirical measures converge weakly to
\[
\nu=\tfrac12(\delta_0+\delta_{1/2}),
\qquad (F_c)_*\nu=\tfrac12(\delta_{1/2}+\delta_1)\ne\nu.
\]
Thus the common limiting empirical probability is not invariant.

**(ii) Critical birth with a positive physical basin.** At \(c=c_*\), there is exactly one primitive two-cycle \(\{1/3,17/18\}\); its probability \(\mu_*=(\delta_{1/3}+\delta_{17/18})/2\) is the unique invariant Borel probability. Its statistical-attraction basin has Lebesgue measure \(2/9\), while the complementary ghost basin has measure \(7/9\). For any left initial point \(x\in(1/3,1/2]\),
\[
\lim_{n\to\infty}n\bigl(F_{c_*}^{2n}(x)-1/3\bigr)=4/9.
\]
All nonperiodic initial points in the complementary ghost basin still have empirical limit \(\nu\), which is not invariant.

**(iii) Supercritical coexistence and exact basin geometry.** For every \(c_*<c\le1/2\), there are exactly two primitive two-cycles, represented by the two roots
\[
0<r_-(c)<1/3<r_+(c)\le1/2,
\qquad 16c\,r_\pm(c)(1-r_\pm(c))^2=1.
\]
Their respective upper-phase coordinates are \(u_\pm=1/2+2r_\pm-2r_\pm^2\). The lower cycle is repelling, and the upper cycle attracts an open set of initial conditions. Every invariant Borel probability is a convex combination of the two cycle probabilities \(\mu_\pm=(\delta_{r_\pm}+\delta_{u_\pm})/2\), but only \(\mu_+\) is a physical measure (one with a positive-Lebesgue-measure empirical-attraction basin).

Set \(s(c)=1/2+\sqrt{r_-(c)/(4c)}\). Up to the two separator points and an exceptional endpoint of measure zero, the two empirical basins are exactly
\[
B_{\rm ghost}=(0,r_-)\cup(1/2,s),\qquad
B_{\rm physical}=(r_-,1/2]\cup(s,1].
\]
On the ghost basin, the empirical limit is the non-invariant \(\nu\); on the physical basin, it is \(\mu_+\). At \(r_-\) and \(s\), the orbit lies on the repelling two-cycle, so its empirical limit is \(\mu_-\). The endpoint \(0\) belongs to the physical basin. Consequently the exact ghost-basin length is
\[
\boxed{\mathcal L(c)=r_-(c)+\sqrt{r_-(c)/(4c)}},
\]
strictly decreasing from \(7/9\) at \(c=c_*\) to \(1/2\) at \(c=1/2\). At this last symmetric endpoint,
\[
r_-=(3-\sqrt5)/4,\quad r_+=1/2,\quad
s=(1+\sqrt5)/4,
\]
and the physical two-cycle \(\{1/2,1\}\) and the non-invariant ghost each attract **exactly half of Lebesgue initial conditions** in the empirical sense.

The saddle-node onset is sharp:
\[
\boxed{r_\pm(c)=\frac13\pm\frac{16}{27}\sqrt{c-c_*}+O(c-c_*)}
\quad(c\downarrow c_*).
\]
All ghost trajectories converge in the even phase **doubly exponentially**: for every left initial \(x\) in the ghost basin, writing \(x_n=F_c^{2n}(x)\), there is \(\Lambda_c(x)>0\) such that
\[
\boxed{x_n=\frac{1+o(1)}{16c}\exp(-\Lambda_c(x)2^n).}
\]
For a right ghost initial point the same formula holds after one preliminary iteration into the left branch, with its own positive constant.

## Assumptions and scope

All arithmetic is exact real arithmetic. The phase space is the closed interval \([0,1]\); the exact branch convention at \(1/2\) is part of the definition. The parameter range \(0<c\le1/2\) is the maximal range of this one-parameter slice in which every positive right-branch input maps into the left half after one step. The term **ghost** means a trajectory whose limit set is \(\{0,1/2\}\) even though that set is not forward invariant, not an additional invariant attractor. Empirical limits are weak limits of \(N^{-1}\sum_{j=0}^{N-1}\delta_{F_c^j(x)}\); a physical measure must itself be invariant. Lebesgue basin lengths are unnormalized lengths in \([0,1]\), hence equal to probability for a uniform initial point. The two-cycle statement includes critical and endpoint parameter values exactly as written; no assertions are made about \(c>1/2\).

## Proof

**1. Complete two-step reduction.** Write \(L(x)=1/2+2x-2x^2\) on \([0,1/2]\) and \(R_c(y)=4c(y-1/2)^2\) on \((1/2,1]\). For \(x\in(0,1/2]\), \(L(x)\in(1/2,1]\); for \(y\in(1/2,1]\), \(R_c(y)\in(0,c]\subset(0,1/2]\). Hence all positive orbits alternate between the halves after at most one step. For positive left coordinates the exact continuous return map is
\[
G_c(x)=R_c(L(x))=16c x^2(1-x)^2,\qquad 0<x\le1/2.
\]
It extends continuously to \([0,1/2]\) with \(G_c(0)=0\), although **the true map satisfies** \(F_c^2(0)=1\), not zero. Moreover \(0\mapsto1/2\mapsto1\mapsto c\), with \(c>0\) in the left half. The extension is strictly increasing on \((0,1/2)\), because \(G_c'(x)=32cx(1-x)(1-2x)>0\), and maps \([0,1/2]\) into \([0,c]\). Consequently every positive left orbit is monotone under \(G_c\) from the first return onwards and converges to a fixed point of the continuous extension. No nonfixed cycles of \(G_c\) exist. All genuine periodic orbits of \(F_c\) therefore have least period two.

**2. Exact threshold and periodic census.** For \(x>0\), the return fixed-point condition becomes
\[
G_c(x)=x\iff 16c x(1-x)^2=1.
\]
The function \(x(1-x)^2\) increases on \((0,1/3)\) and decreases on \((1/3,1/2]\), reaching its strict maximum \(4/27\). Therefore the largest possible ratio \(G_c(x)/x\) is \(64c/27\), giving exactly the threshold \(c_*=27/64\). Below threshold \(G_c(x)<x\) for every positive left point, so all returns decrease to zero. At threshold there is exactly one positive return fixed point at \(x=1/3\). The identity
\[
G_{c_*}(x)-x=\frac{x(3x-4)(3x-1)^2}{4}
\]
shows that points below \(1/3\) decrease to zero, while points above \(1/3\) decrease to \(1/3\). Above threshold and up to \(c=1/2\), exactly two positive return fixed points exist, \(r_-<1/3<r_+\), with \(r_+=1/2\) only for \(c=1/2\). The sign of \(G_c(x)-x\), together with monotonicity, proves that points below \(r_-\) decrease to zero, points above \(r_-\) converge to \(r_+\), and the point \(r_-\) itself is fixed. Since \(G_c'(r)=1+r(\log[16c x(1-x)^2])'|_{x=r}\), this derivative is greater than one at \(r_-\) and less than one at \(r_+\), with derivative zero at \(r_+=1/2\). Thus the lower and upper cycles are respectively repelling and attracting.

**3. All initial conditions and exact basin lengths.** On the right, \(R_c\) is strictly increasing. The preimage under \(R_c\) of a left separator \(r\in(0,c)\) is \(s=1/2+\sqrt{r/(4c)}\). At \(c=c_*\), the separator is \(r=1/3\), so \(s=17/18\); the ghost basin is \((0,1/3)\cup(1/2,17/18)\), length \(1/3+4/9=7/9\), while the periodic basin has length \(2/9\). At \(c>c_*\), take \(r=r_-\), obtaining the two basins in the Finding. The endpoint \(0\) enters at \(c\) after three steps, which is strictly above the separator for \(c\ge c_*\), so it belongs to the periodic basin. If \(c<c_*\), its subsequent positive returns tend to zero like those of every other initial point. Both separator points form the lower repelling two-cycle for \(c>c_*\), or the sole neutral two-cycle at equality. The ghost fraction \(\mathcal L(c)\) is strictly decreasing for \(c>c_*\): on \((0,1/3)\), the map \(r\mapsto r(1-r)^2\) increases, so \(r_-(c)\) strictly decreases with \(c\); the term \(\sqrt{r_-(c)/(4c)}\) also decreases. At \(c=1/2\), factoring
\[
G_{1/2}(x)-x=x(2x-1)(4x^2-6x+1)
\]
gives \(r_-=(3-\sqrt5)/4\); the right separator is \(s=(1+\sqrt5)/4=1-r_-\), and \(\mathcal L(1/2)=1/2\). The return multiplier at the separating cycle is exactly \(6-2\sqrt5>1\).

**4. Stationarity versus empirical limits.** Every ghost orbit has successive left returns tending to \(0\) and intervening right-phase coordinates tending to \(L(0)=1/2\), so its empirical measures converge weakly to \(\nu=(\delta_0+\delta_{1/2})/2\). But \(F_c(0)=1/2\), \(F_c(1/2)=1\); hence \((F_c)_*\nu=(\delta_{1/2}+\delta_1)/2\ne\nu\). Every other orbit asymptotically follows one of the explicitly identified two-cycles, so its empirical limit is the corresponding invariant cycle probability. For **any** invariant Borel probability \(\sigma\) and **any** continuous observable \(\varphi\), bounded dominated convergence applied to the pointwise convergent time averages gives \(\int\varphi\,d\sigma\) as the corresponding weighted combination of integrals against \(\nu\) and the cycle probabilities, with weights equal to \(\sigma\)-masses of their Borel basins. Continuous observables determine probabilities on a compact interval. Thus \(\sigma\) is such a convex combination. Stationarity of \(\sigma\), invariance of the cycle probabilities and non-invariance of \(\nu\) force the ghost coefficient to vanish. Below threshold only \(\nu\) is available and so **no invariant probability exists**. At threshold the unique stationary probability is \(\mu_*\). Above threshold the entire invariant simplex is \(\operatorname{conv}\{\mu_-,\mu_+\}\). Only \(\mu_+\) has a positive-length empirical basin; the repelling cycle has a zero-length basin. This proves the physical-measure claims.

**5. Sharp rates.** At the fold, \(H(x,c)=G_c(x)-x\) satisfies \(H(1/3,c_*)=H_x(1/3,c_*)=0\), \(H_c(1/3,c_*)=64/81\) and \(H_{xx}(1/3,c_*)/2=-9/4\). The two simple roots born at \(c>c_*\) therefore satisfy \(r_\pm=1/3\pm\sqrt{(64/81)/(9/4)}\sqrt{c-c_*}+O(c-c_*)\), giving the coefficient \(16/27\). At \(c=c_*\), if a left return starts above \(1/3\), its displacement \(e_n=x_n-1/3>0\) decreases to zero and obeys \(e_{n+1}=e_n-(9/4)e_n^2+O(e_n^3)\). Consequently \(e_{n+1}^{-1}-e_n^{-1}\to9/4\), and Cesàro averaging yields \(ne_n\to4/9\).

For a ghost orbit, let \(x_n=G_c^n(x)>0\), so \(x_n\to0\), and set \(y_n=16c x_n\). The exact identity \(y_{n+1}=y_n^2(1-x_n)^2\) implies that the sequence \(\Lambda_n=-2^{-n}\log y_n\) is increasing, since \(\Lambda_{n+1}-\Lambda_n=-2^{-n}\log(1-x_n)>0\), and it converges finitely because \(0<x_n\le1/2\). Once \(x_n\) is sufficiently small, \(y_n<1\), so \(\Lambda_n>0\) and its limit \(\Lambda_c(x)>0\). Moreover \(2^n(\Lambda_c(x)-\Lambda_n)\to0\) by bounding the geometric tail using \(x_j\to0\). This gives \(x_n=(16c)^{-1}\exp[-\Lambda_c(x)2^n+o(1)]\), as asserted.

## Verification

A standalone standard-library script `check.py` verifies the exact critical and symmetric polynomial factorizations, threshold coefficients, the quadratic-field two-cycle identity, repelling multiplier, exact endpoint basin fractions and representative high-precision return orbits. Run `python check.py` from the directory containing `RESULT.md` and `check.py`. The finite numerical diagnostics are secondary; the arguments in the Proof section supply the quantifiers over all real parameters and initial states.

## Relationship to prior work

The original 2023 paper [1] introduces this exact two-branch power family and proves absence of fixed points for exponents at least one. Its Section 4.1 contains numerical Lyapunov and phase diagrams, not the exact border-slice invariant-probability bifurcation, empirical-limit partition, or basin lengths. Published analyses of the same family with strict \(a>b\) [5] concern an alternating return with positive image at zero and thus do not extend their global-cycle assertions to the discontinuous \(a=b\) boundary. A complementary border result [6] proves disappearance of invariant probability only under the sufficient contraction condition \(c<b/d^2\), which here means \(c<1/8\); it does not cover the sharp threshold \(27/64\) or the coexisting physical and ghost basins above it. The classical idea that omega limits may fail invariance for discontinuous maps, and the possibility of lacking stationary probability, are already established in [2,3], and are not claimed as new. The originality assessed here is this model's sharp one-parameter three-regime classification, explicit measure simplex, and quantitative basin jump and half-basin phenomenon.

## Limitations

The classification is restricted to the mathematically natural symmetric quadratic border slice and the maximal strict alternation range \(0<c\le1/2\); it does not describe all parameters of the source family, stochastic perturbations or finite-precision implementations. The existence of non-invariant omega sets is not itself a new general phenomenon. A 2024 follow-up by some of the originating authors [4] concerns a different construction using logistic and tent transformations; its accepted manuscript was not available for full-text comparison at inspection, so possible unforeseen related coverage remains a publication-priority risk. No cryptographic-security conclusion is made.

## References

1. M. Lawnik, L. Moysis and C. Volos, “A Family of 1D Chaotic Maps without Equilibria,” *Symmetry* **15** (2023), 1311, equation (15); first public date 2023-06-27. https://doi.org/10.3390/sym15071311
2. S. Kryzhevich, “Invariant measures for interval translations and some other piecewise continuous maps,” *Mathematical Modelling of Natural Phenomena* **15** (2020), article 15; arXiv:1812.04534. https://arxiv.org/abs/1812.04534
3. E. Catsigeras, P. Guiraud, A. Meyroneinc and E. Ugalde, “On the asymptotic properties of piecewise contracting maps,” *Dynamical Systems* **31** (2016), 107–135; arXiv:1108.1501. https://arxiv.org/html/1108.1501v2
4. M. Lawnik, L. Moysis, M. S. Baptista and C. Volos, “Discrete one-dimensional piecewise chaotic systems without fixed points,” *Nonlinear Dynamics* **112** (2024), 6679–6693. https://doi.org/10.1007/s11071-024-09349-6
5. “A cusp of coexisting two-cycles in a fixed-point-free quadratic interval map,” published research finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-cusp-of-coexisting-two-cycles-in-a-fixed-point-free-quadratic--dd9acbf9570b ; “General strict-alternation power-family classification,” published research finding (2026), source record recoverable in same research collection.
6. “An attracting two-cycle disappears into a nonstationary ghost at a discontinuity,” published research finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-an-attracting-two-cycle-disappears-into-a-nonstationary-ghost-at--3ab687079720
