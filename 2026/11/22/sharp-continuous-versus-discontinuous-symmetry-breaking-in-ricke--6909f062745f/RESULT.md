# Sharp continuous-versus-discontinuous symmetry breaking in Ricker recruitment across identical spawning habitats

## Finding

For a fixed positive spawning stock distributed over \(m\geq2\) identical, independent habitats with local Ricker recruitment \(f(x)=x e^{-x}\), the globally recruitment-maximizing allocation has a sharp stock threshold. With two habitats, the optimum leaves the equal split **continuously** at total dimensionless stock \(s=4\). With every \(m\geq3\), it instead switches **discontinuously** at an explicitly defined threshold \(2<s_m<2m\): the equal split is uniquely optimal below \(s_m\), and at \(s_m\) it coexists with strictly unequal maximizers; above \(s_m\) every maximizer has one overfilled habitat and \(m-1\) equally loaded habitats. An exact one-variable formula determines \(s_m\), requiring no search over the allocation simplex.

For \(t>0\) write
\[
A_m(t)=\sum_{j=0}^{m-1}e^{-jt},\qquad S_m(t)=\frac{m(m-1)t A_m(t)}{m-A_m(t)},\qquad s_m=\inf_{t>0}S_m(t).
\]
For \(m=2\), \(s_2=4\); for \(m\geq3\), the infimum is attained at some positive \(t\), and \(2<s_m<2m\). At such a minimizing \(t\), the unequal co-optimizer has one coordinate \(s_m/A_m(t)\) and \(m-1\) coordinates each equal to \(s_m(1-1/A_m(t))/(m-1)\). Each such configuration and its permutations are optimal, together with the equal configuration. The theorem does not claim uniqueness of the minimizing \(t\).

For any \(m\geq2\), the best aggregate recruitment \(W_m(s)\) tends to \((m-1)/e\) as \(s\to\infty\), whereas the equal allocation yields \(E_m(s)=s e^{-s/m}\to0\). Consequently
\[
\frac{W_m(s)}{E_m(s)}\sim\frac{m-1}{e s}e^{s/m}\quad(s\to\infty).
\]
This is an objective-level contrast between maximizing total recruits and equalizing identical per-spawner success, not an empirical claim about spawner choice.

## Assumptions and scope

Fix an integer \(m\geq2\) and dimensionless stock \(s>0\). The feasible allocations are \(x_i\geq0\), \(\sum_{i=1}^m x_i=s\). All habitats have identical strictly local recruitment law \(f(x)=x e^{-x}\); there is no movement of offspring between habitats, environmental randomness, temporal feedback, or habitat-specific capacity. Overall positive multipliers in the Ricker law do not affect maximizers. The objective is \(W_m(s)=\max\sum_{i=1}^m f(x_i)\). Equal allocation yields \(E_m(s)=s e^{-s/m}\). If a spawner instead compares only identical sites' instantaneous per-capita survival \(e^{-x_i}\), the symmetric equal split is the ideal-free allocation for identical sites. The theorem only compares these stipulated mathematical objectives.

## Proof

**1. Structure of a global maximum.** Existence follows from compactness of the simplex. We have
\[
f'(x)=(1-x)e^{-x},\quad f''(x)=(x-2)e^{-x},\quad f'(0)=1.
\]
Every maximizer is interior. Indeed, if \(x_i=0\) and \(x_j>0\), transferring a sufficiently small positive amount from \(j\) to \(i\) changes the objective initially at rate \(f'(0)-f'(x_j)>0\). At an interior maximum all derivatives \(f'(x_i)\) coincide. No two coordinates can exceed \(2\), since transferring mass between them gives strictly positive second variation \(f''(x_i)+f''(x_j)>0\), impossible at a local maximum. If no coordinate exceeds \(2\), strict concavity of \(f\) on \([0,2]\) and Jensen's inequality force all coordinates equal. Otherwise precisely one coordinate \(v>2\) exists; all others lie below \(2\), and derivative equality forces them to be the same \(u\in(1,2)\), because \(f'\) is strictly decreasing on \((0,2)\) and \(f'(v)<0\). Thus every global optimum is either equal or has exactly one higher coordinate and \(m-1\) equal lower coordinates.

**2. Compare each possible asymmetric split with the equal one.** Parameterize the high coordinate as \(ps\), where \(1/m<p<1\); the other coordinates are \(qs\), where \(q=(1-p)/(m-1)\). The ratio of the asymmetric total recruitment to the equal total recruitment is
\[
G_{m,p}(s)=p e^{-s(p-1/m)}+(1-p)e^{s(1/m-q)}.
\]
It obeys \(G_{m,p}(0)=1\), \(G'_{m,p}(0)=1/m-[p^2+(m-1)q^2]<0\), \(G''_{m,p}(s)>0\) for all \(s\geq0\), and \(G_{m,p}(s)\to\infty\). Therefore the strictly convex function crosses \(1\) at exactly one positive value \(s_p\); it lies below \(1\) for \(0<s<s_p\) and above \(1\) for \(s>s_p\). Introduce \(t=s_p(1/m-q)>0\), so the first exponential is \(e^{-(m-1)t}\) and the second is \(e^t\). The equality \(G_{m,p}(s_p)=1\) gives
\[
p=\frac{1-e^{-t}}{1-e^{-mt}}=\frac1{A_m(t)}.
\]
This parametrizes every \(1/m<p<1\) bijectively by \(t>0\). Solving for \(s_p\) gives \(s_p=S_m(t)\), exactly as displayed above. In view of Step 1, whether equal allocation is globally optimal is completely determined by the infimum of these crossing stocks. If every \(G_{m,p}(s)<1\), it is uniquely global; if some exceeds one, it is not global. If a positive \(t\) attains the threshold, the corresponding asymmetric allocation is a global co-maximizer there, since no other split can beat equality.

**3. Two-habitat criticality.** When \(m=2\),
\[
S_2(t)=2t\coth(t/2)>4\quad(t>0),\qquad\lim_{t\downarrow0}S_2(t)=4.
\]
Hence the equal allocation is uniquely optimal through \(s=4\). For \(s>4\), writing the allocations as \(s/2\pm z\), \(0\leq z\leq s/2\), gives the objective
\[
2e^{-s/2}\left[(s/2)\cosh z-z\sinh z\right].
\]
Its derivative has the sign of \((s/2-1)\tanh z-z\). Since \(z\coth z\) increases strictly from \(1\) to \(\infty\) for \(z>0\), there is exactly one positive maximizer \(z(s)\in(0,s/2)\), determined by \(z\coth z=s/2-1\), and its coordinate swap. Furthermore \(z(s)\to0\) as \(s\downarrow4\). The expansion \(z\coth z=1+z^2/3+O(z^4)\) gives \(z(s)\sim\sqrt{3(s-4)/2}\).

**4. At least three habitats: discontinuity.** Elementary Taylor expansion of the finite geometric sum gives
\[
S_m(t)=2m\left[1-\frac{m-2}{6}t+O(t^2)\right]\quad(t\downarrow0),
\]
whereas \(S_m(t)\sim mt\to\infty\) as \(t\to\infty\). When \(m\geq3\) the initial derivative is negative, so \(s_m<2m\), and the infimum is attained at an interior positive \(t_*\). Also \(s_m>2\): at \(s=2\), every allocation lies in \([0,2]\), hence strict concavity gives a unique equal maximizer. If unequal allocations equaled or surpassed the equal one for stocks approaching \(2\) from above, choose maximizing ones; by compactness their limit would be the unique equal maximizer at \(s=2\). But at that equal point \(f''(2/m)<0\) (strict local concavity on a neighborhood of the equal vector), so no such nearby unequal maximizer exists. Thus there is a neighborhood above \(2\) of unique equal optimality.

For \(s<s_m\) every fixed asymmetric \(p\) has \(s<s_p\) and loses strictly; thus equality is uniquely optimal. At \(s=s_m\) the positive minimizer \(t_*\) gives a strict unequal co-optimizer along with equality; its \(m\) permutations are distinct. At every \(s>s_m\), the same \(p_*=1/A_m(t_*)\) satisfies \(G_{m,p_*}(s)>1\), so equality is strictly suboptimal and Step 1 forces one coordinate above \(2\), the other \(m-1\) coordinates equal in \((1,2)\). Because \(s_m<2m\), the equal split is a strict local maximum at the global crossover, so the optimal imbalance arrives with a positive jump: this is a discontinuous global-allocation transition, unlike \(m=2\).

**5. Large-stock limit.** Every maximizing nonuniform configuration at sufficiently large \(s\) has \(v=s-(m-1)u>2\) and \(1<u<2\). Therefore \(v\to\infty\), and equality \(f'(u)=f'(v)\to0^-\) forces \(u\to1^+\). Thus its objective \((m-1)f(u)+f(v)\to(m-1)/e\). Dividing by \(E_m(s)=s e^{-s/m}\) yields the claimed asymptotic ratio.

## Verification

A standalone Python 3 standard-library file, `verify.py`, tests the closed crossing formula, two-habitat stationarity and transition, numerical threshold minimizations for habitat counts 3 through 12, candidate allocations against equal allocation on both sides of the threshold, and large-stock limits. It produces 3,186 successful diagnostic assertions. These finite checks are **not** the proof of the continuum and unbounded claims; Steps 1–5 are that proof. Numerical illustrations: \(s_3\approx5.7743134717\), \(s_4\approx7.3082225585\), \(s_5\approx8.7306070302\). These decimals are diagnostic approximations to the exact variational definition, not interval-certified constants.

## Relationship to prior work

Skoglund, Whitlock, Petersson, Palm and Leonardsson (2022) explicitly model localized Ricker and Beverton–Holt recruitment, compare assumed spawning-habitat selection patterns, and analyze stock–recruitment estimation bias. That paper supplies the scientific reason to examine spatially aggregated local stock–recruitment, but the inspected modeling, results and discussion do not state the optimizing identical-patch theorem, sharp critical habitat-count distinction, or exact all-\(m\) threshold. Bouchard, Bardonnet, Buoro and Tentelier (2018) examine spatial aggregation of nests and recruitment in Atlantic salmon, emphasizing empirical variability and Beverton–Holt-type local compensation, not this fixed-total Ricker maximization. General local Ricker overcompensation and resource-allocation calculus are known; the present contribution is the specified exact, globally complete allocation transition and asymptotic objective gap, not the Ricker function itself. No claim of comprehensive historical priority is made.

## Limitations

Identical habitats, fixed stock, exact deterministic local Ricker laws, independent patches, and freely controllable continuous allocations are restrictive mathematical hypotheses. The equal-split comparison is an ideal-free benchmark only under identical per-capita survival and perfect information. No behavioral equilibrium, empirical recruitment measurement, long-run stochastic persistence, or policy recommendation is proved. The variational formula need not give a closed elementary numerical constant for all \(m\); uniqueness of its minimizing parameter is not claimed. Independent external validation and comprehensive historical-priority verification have not occurred. Relevant broader ideal-free and Ricker competition literatures may contain equivalent formulations.

## References

1. S. Skoglund, R. Whitlock, E. Petersson, S. Palm, K. Leonardsson. *From spawner habitat selection to stock-recruitment: Implications for assessment*. Ecology and Evolution **12** (2022), e9679. First public issue date 2022-12-28. https://doi.org/10.1002/ece3.9679 .
2. C. Bouchard, A. Bardonnet, M. Buoro, C. Tentelier. *Effects of spatial aggregation of nests on population recruitment: the case of a small population of Atlantic salmon*. Ecosphere **9** (2018), e02178. https://doi.org/10.1002/ecs2.2178 .
3. Å. Brännström, D. J. T. Sumpter. *The role of competition and clustering in population dynamics*. Proceedings of the Royal Society B (2005). https://doi.org/10.1098/rspb.2005.3185 .
