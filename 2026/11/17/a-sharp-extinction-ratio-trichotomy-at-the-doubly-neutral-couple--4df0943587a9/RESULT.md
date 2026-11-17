# A sharp extinction-ratio trichotomy at the doubly neutral coupled-logistic predator–prey map

## Finding

Consider the prey–predator coupled logistic recurrence
\[
x_{n+1}=x_n(1-x_n-cy_n),\qquad y_{n+1}=y_n(1-y_n+dx_n),
\]
where \(c,d>0\) and both uncoupled growth multipliers equal one. Both populations vanish, but a sharp transition at \(c=1\) changes their relative extinction clocks. Precisely, the following three alternatives hold for every positive initial condition in the rectangle specified below.

When \(0<c<1\),
\[
\lim_{n\to\infty}n(x_n,y_n)=\left(\frac{1-c}{1+cd},\frac{1+d}{1+cd}\right).
\]
When \(c=1\),
\[
\lim_{n\to\infty}ny_n=1,\qquad
\lim_{n\to\infty}n\log n\,x_n=\frac1{1+d},
\]
and an initial-data-dependent constant \(C\in\mathbb R\) exists such that
\[
\frac{y_n}{x_n}=(1+d)\log n+d\log\log n+C+o(1).
\]
When \(c>1\),
\[
\lim_{n\to\infty}ny_n=1,\qquad
\lim_{n\to\infty}n^c x_n=L\in(0,\infty).
\]

## Assumptions and scope

Take arbitrary fixed \(c,d>0\) and any
\[
0<\varepsilon<\min\left\{\frac1{2(1+cd)},\frac1{2d},\frac1{2(1+d)}\right\}.
\]
Require \(0<x_0\le\varepsilon\), \(0<y_0\le d\varepsilon\). The rectangle is invariant: \(x_{n+1}>0\) because \(x_n+cy_n\le\varepsilon(1+cd)<1/2\), and \(0<x_{n+1}\le\varepsilon\). On \([0,d\varepsilon]\) the map \(y\mapsto y(1-y+dx_n)\) is strictly increasing because \(1-2d\varepsilon>0\); its top endpoint maps to at most itself when \(x_n\le\varepsilon\). The positive quadrant requirement excludes boundary orbits, which obey other laws.

## Proof

Write \(r_n=x_n/y_n\) and \(T_n=1/y_n\). Direct division gives the *exact* identities
\[
r_{n+1}-r_n=\frac{r_n y_n[(1-c)-(1+d)r_n]}{1-y_n+dx_n},\qquad
T_{n+1}-T_n=\frac{1-dr_n}{1-y_n+dx_n}.
\tag{1}
\]
For \(0<c<1\), put \(r_*=(1-c)/(1+d)\). A second exact identity is
\[
r_{n+1}-r_*=(r_n-r_*)\frac{1-x_n-y_n}{1-y_n+dx_n}.
\tag{2}
\]
Both factors in the last fraction are positive and their ratio is below one. Thus \(r_n\) remains between \(r_0\) and \(r_*\) when \(c<1\). For \(c\ge1\), the first equation shows \(r_n\) strictly decreases and remains bounded.

Since \(x_{n+1}\le x_n(1-x_n)\), \(x_n\downarrow0\) and \(x_n\le (n+x_0^{-1})^{-1}\). The predator also tends to zero: given \(\delta>0\), eventually \(dx_n\le\delta\), and \(y_{n+1}\le y_n(1+\delta-y_n)\). Every value above \(2\delta\) then contracts until below that threshold, and the interval \([0,3\delta]\) is eventually forward invariant for sufficiently small \(\delta\). Hence \(y_n\to0\). Yet
\[
y_{n+1}\ge y_n(1-y_n),\quad
T_{n+1}\le T_n+2,
\]
using \(y_n<1/2\), so \(\sum_n y_n=\infty\).

If \(c<1\), equation (2) and \(\sum y_n=\infty\) imply \(r_n\to r_*\), since the multiplicative contraction is \(1-(1+d)r_ny_n/(1-y_n+dx_n)\) and \(r_n\) is bounded away from zero. For \(c\ge1\), the first equation and \(\sum y_n=\infty\) imply \(r_n\to0\); otherwise \(r_n\) would decrease by a non-summable multiple of \(y_n\). Inserting the ratio limits into the reciprocal identity (1) and applying Cesàro averaging yields
\[
\frac{T_n}{n}\to \begin{cases}(1+cd)/(1+d),&0<c<1,\\1,&c\ge1.\end{cases}
\]
This proves all stated \(n^{-1}\) leading limits except the faster prey decay.

For \(c>1\), let \(k=c-1>0\). Since \(y_n\sim1/n\), the logarithm of the exact ratio update satisfies
\[
\log\frac{r_{n+1}}{r_n}=-k y_n-(1+d)x_n+O((x_n+y_n)^2).
\]
For each fixed \(0<\delta<k\), summation first gives \(r_n=O(n^{-k+\delta})\). Therefore \(x_n=r_ny_n=O(n^{-1-k+\delta})\), so \(\sum x_n<\infty\). The reciprocal identity yields
\[
T_{n+1}-T_n=1-dr_n+O(y_n),
\]
and consequently \(T_n=n+O(n^{\max\{1-k+\delta,0\}}+\log n)\) (with an extra logarithm in a boundary exponent, which is harmless). Thus \(\sum_n|y_n-1/n|<\infty\). Expanding \(\log(x_{n+1}/x_n)=-x_n-cy_n+O((x_n+y_n)^2)\) now shows that \(\log x_n+c\log n\) converges to a finite real number. Exponentiating proves \(n^c x_n\to L\in(0,\infty)\).

For the critical case \(c=1\), put \(w_n=y_n/x_n=1/r_n\). Division of the recurrence yields the exact additive law
\[
w_{n+1}-w_n=\frac{(1+d)y_n}{1-x_n-y_n}.
\tag{3}
\]
Since \(ny_n\to1\), equation (3) first gives \(w_n\sim(1+d)\log n\), hence \(x_n\sim[(1+d)n\log n]^{-1}\). To obtain the next order, use \(T_n=1/y_n\) in (1):
\[
T_{n+1}-T_n=1-\frac d{w_n}+O(y_n).
\tag{4}
\]
The first estimate \(w_n\sim(1+d)\log n\) implies \(T_n=n+O(n/\log n)\) and \(y_n=n^{-1}+O((n\log n)^{-1})\). Equation (3), whose denominator contributes only a summable \(O(y_n^2)\), upgrades this to \(w_n=(1+d)\log n+O(\log\log n)\). Substitution into (4), together with \(\sum_{j\le n}(\log j)^{-1}=n/\log n+O(n/\log^2 n)\), gives
\[
T_n=n-\frac d{1+d}\frac n{\log n}+O\left(\frac{n\log\log n}{\log^2 n}\right),
\]
so
\[
y_n=\frac1n+\frac{d}{1+d}\frac1{n\log n}
+O\left(\frac{\log\log n}{n\log^2 n}\right).
\]
The error sequence on the right is summable. Summing (3) and using the standard harmonic and logarithmic-harmonic sums now gives the finite limit
\[
\lim_{n\to\infty}\left[w_n-(1+d)\log n-d\log\log n\right]=C\in\mathbb R,
\]
completing the proof. All error bounds hold for fixed \(c,d,x_0,y_0\) and all sufficiently large integers \(n\).

## Verification

A standalone exact-symbolic and numerical checker is supplied as `CHECK.py`. It symbolically verifies equations (1)–(3), evaluates invariant-domain inequalities for representative rational coefficients, and numerically tests the three limiting regimes and critical two-term ratio. Finite checks illustrate rather than establish the infinite-time statements.

## Relationship to prior work

Al-Kaff, El-Metwally, Elsadany and Elabbasy (2024) study this coupled-logistic population model, identifying equilibria, local bifurcations and chaotic regimes. Their origin theorem identifies nonhyperbolicity at a unit growth multiplier, but the inspected text does not derive the simultaneous-unit-growth, all-positive-orbit asymptotic trichotomy or the logarithm–loglog ratio coefficient. Satoh and Aihara (1990) investigated a relabeling of the coupled logistic predator–prey map numerically; this earlier model origin is credited rather than claimed as novel. Other coupled-logistic bifurcation analyses address different parameter regimes and do not explicitly establish these rates in inspected available material. Generic parabolic-map theory provides context but does not by itself document the displayed parameter-uniform trichotomy for this ecological model.

## Limitations

The result holds only for initial states in the stated positive invariant rectangle, with both intrinsic logistic multipliers exactly one. It does not classify larger-data trajectories, perturbations of those multipliers, singular initial states on the coordinate axes, or global bifurcations. The positive constant \(L\) and real constant \(C\) depend on initial conditions. Bibliographic completeness is limited by inaccessible full text of one relevant 2018 coupled-logistic bifurcation paper and the 1990 numerical source; explicit independent publication-priority verification has not been performed.

## References

1. M. O. Al-Kaff, H. A. El-Metwally, A.-E. A. Elsadany, and E. M. Elabbasy, *Exploring chaos and bifurcation in a discrete prey–predator based on coupled logistic map*, Scientific Reports 14, 16118 (2024), https://doi.org/10.1038/s41598-024-62439-8. Public online date: 2024-07-12.
2. K. Satoh and T. Aihara, *Numerical Study on a Coupled-Logistic Map as a Simple Model for a Predator-Prey System*, Journal of the Physical Society of Japan 59, 1184–1198 (1990), https://doi.org/10.1143/JPSJ.59.1184.
3. A. A. Elsadany, A. M. Yousef, and A. Elsonbaty, *Further analytical bifurcation analysis and applications of coupled logistic maps*, Applied Mathematics and Computation 338, 314–336 (2018), https://doi.org/10.1016/j.amc.2018.06.008.
