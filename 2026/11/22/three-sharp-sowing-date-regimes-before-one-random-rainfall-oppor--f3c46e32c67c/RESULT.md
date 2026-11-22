# Three sharp sowing-date regimes before one random rainfall opportunity

## Finding

In an idealized restoration experiment with three independently viable sowing cohorts and one common exponentially timed first rain, there are **exactly three global allocation regimes** as the initial cohort-establishment probability increases: all three cohorts planted together, two together and one delayed, or three distinct dates. Both transition constants and all equality cases are exact.

Put
\[
p_1=\frac{8-\sqrt{10}}9,\qquad
p_2=\frac{3+\sqrt{9+48p_1(1-p_1)^2}}8.
\]
Numerically, \(p_1\approx0.5375247044\) and \(p_2\approx0.8512884715\). For every \(p\in(0,1]\), the **unique optimal ordered calendar** \(0\le t_1\le t_2\le t_3<\infty\) is:

1. If \(0<p\le p_1\), \(t_1=t_2=t_3=0\).
2. If \(p_1<p\le p_2\), \(t_1=t_2=0\), \(t_3=\log(p/p_1)\).
3. If \(p_2<p\le1\), let \(y\) be the unique root in \((p_1,3/4)\) of
   \[
   6y^4-7y^3+27py^2-(32p^2+24p)y+24p^2=0.
   \]
   Set
   \[
   u=\frac{8y-6}{y(9y-8)},\qquad v=\frac{uy}{p}.
   \]
   Then \(0<v<u<1\) and \((t_1,t_2,t_3)=(0,-\log u,-\log v)\).

The equality cases at both thresholds belong to the preceding regime; no tie between distinct calendars occurs. At \(p=1\), the optimum has approximately \(t_2=0.1568194\), \(t_3=0.7068959\) in normalized time units, and success probability \(0.78958875\).

## Assumptions and scope

A single effective rainfall time \(R\) is exponential with rate one: \(\Pr(R>r)=e^{-r}\) for \(r\ge0\). Three equally sized, individually labeled seed cohorts may be planted at deterministic ordered dates \(0\le t_1\le t_2\le t_3<\infty\), allowing coincident dates. For a realized rain time \(R=r\), a cohort planted at date \(t_i\le r\) establishes independently of the other cohorts with probability \(p e^{-(r-t_i)}\), where \(0<p\le1\). A cohort planted after rain has establishment probability zero. The shared rain time is the sole source of dependence; conditional establishment events are independent. There are no later effective rains, replanting decisions, measurement errors, density effects, or costs for postponement. The objective is the unconditional probability that **at least one** of the three cohorts establishes at rain. The equal unit rates for rainfall arrival and pre-rain viability loss are part of the theorem's specified model (or a common-rate time rescaling), not an assertion for unequal physical rates.

## Proof

**1. Reduction to an earliest sowing at zero.** A calendar with \(t_1=a>0\) has a success probability equal to \(e^{-a}\) times that of the translated calendar \((0,t_2-a,t_3-a)\): set \(r=a+s\) in the exponential rain density and note that all conditional cohort probabilities depend only on elapsed time since planting. Since the latter calendar has positive success probability, every maximizer has \(t_1=0\). Put \(u=e^{-t_2}\), \(v=e^{-t_3}\), so \(0<v\le u\le1\).

**2. Exact success probability.** For any nonempty subset \(J\) of \(m\) cohorts, conditional independence and exponential integration give
\[
\Pr(\text{all cohorts in }J\text{ establish})
=\frac{p^m}{m+1}\exp\left(\sum_{j\in J}t_j-(m+1)\max_{j\in J}t_j\right).
\]
Inclusion–exclusion, with \(t_1=0\), therefore gives exactly
\[
 F_p(u,v)=\frac p2(1+u+v)-\frac{p^2}{3}\left(u^2+v^2+\frac{v^2}{u}\right)+\frac{p^3}{4}\frac{v^3}{u}.
\]
This formula is continuous at the omitted corner \((u,v)=(0,0)\) when assigned value \(p/2\). That corner is not optimal because
\(F_p(1,1)-p/2=p(1-p/2)^2>0\). On the open edge \(v=0,u>0\), \(\partial_vF_p=p/2>0\); thus no optimum has a cohort permanently delayed to infinity. A global maximizer consequently exists in the positive part of the compact closure.

**3. Exclusion of the diagonal boundary except its endpoint.** On \(v=u\),
\[
F_p(u,u)=\frac p2(1+2u)-\frac{p^2}{3}(2u^2+u)+\frac{p^3}{4}u^2.
\]
Its only unconstrained positive maximizer is \(u_b=2(3-p)/[p(8-3p)]\). If \(u_b<1\), then
\[
\left.\partial_v F_p\right|_{u=v=u_b}
=-\frac{p^2(2-p)}{2(8-3p)}<0,
\]
so moving from \((u_b,u_b)\) into \(v<u\) improves the objective. If \(u_b\ge1\), the diagonal is maximized at \((1,1)\), which is already on the boundary \(u=1\). Hence no distinct global optimizer has \(v=u<1\).

**4. Optimize the boundary \(u=1\).** Differentiating gives
\[
\frac{\partial_vF_p(1,v)}p=\frac12-\frac43pv+\frac34p^2v^2.
\]
Its two roots in \(pv\) are \((8\pm\sqrt{10})/9\). The larger exceeds one, while the smaller is \(p_1\). Since \(0<v\le1\) and \(p\le1\), the unique maximum on \(u=1\) is \(v=1\) for \(p\le p_1\), and \(v=p_1/p\) for \(p>p_1\).

**5. Classify all interior stationary points.** Write \(y=pv/u\), so \(0<y<p\). Solving \(\partial_vF_p=0\) gives
\[
u=Z(y):=\frac{8y-6}{y(9y-8)}.
\]
The admissible range \(0<u<1\) forces \(p_1<y<3/4\): for \(0<y<p_1\), one has \(Z(y)>1\); for \(3/4<y<8/9\), one has \(Z(y)<0\); for \(8/9<y\le1\), one again has \(Z(y)>1\). Indeed \(Z(p_1)=1\), \(\lim_{y\uparrow3/4}Z(y)=0\), and
\[
Z'(y)=-\frac{12(6y^2-9y+4)}{y^2(9y-8)^2}<0,
\]
where the numerator quadratic is strictly positive. The remaining stationarity condition is \(G_p(y)=0\), with
\[
G_p(y)=3p+3y-4p^2Z(y)-4y^2Z(y)-2y^2+3y^3Z(y).
\]
It is equivalent to the quartic displayed in the finding. Direct differentiation gives
\[
G_p'(y)=\frac{48p^2(6y^2-9y+4)+y^3(108y^2-207y+112)}{y^2(9y-8)^2}>0.
\]
Both quadratic factors are positive for every real \(y\): their discriminants are \(-15\) and \(-5535\), respectively. At the endpoints,
\[
G_p(p_1)=-4p^2+3p+3p_1(1-p_1)^2,
\qquad \lim_{y\uparrow3/4}G_p(y)=3p+\frac98>0.
\]
The positive root of \(G_p(p_1)=0\) is precisely \(p_2\), and \(p_2>3/4\) follows from \(G_{3/4}(p_1)=3p_1(1-p_1)^2>0\). For \(p<p_2\) there is no interior stationary point; at \(p=p_2\), the only root on the closed interval is \(y=p_1\) and corresponds to the boundary \(u=1\). For \(p>p_2\), strict monotonicity yields exactly one root in \((p_1,3/4)\), and since \(p>p_2>3/4\) it satisfies \(v/u=y/p<1\). It is therefore an admissible, unique interior stationary point.

**6. Global attainment and uniqueness.** Any global maximizer is on \(u=1\), on \(v=u\), or is an interior stationary point; the other closure boundaries were excluded in Steps 2–3. For \(p\le p_1\), no interior stationary point is possible since \(y>p_1\) would contradict \(y<p\). For \(p_1<p\le p_2\), none exists by Step 5, so the unique boundary optimum wins. For \(p>p_2\), the boundary candidate \((u,v)=(1,p_1/p)\) has \(G_p(p_1)<0\), or equivalently a negative inward-boundary derivative \(\partial_uF_p\); decreasing \(u\) and adjusting \(v\) improves it. The unique interior stationary point must therefore be the attained global maximizer. All equalities and strict inequalities in the stated three-regime classification follow.

## Verification

The standard-library-only program `check.py` computes the exact piecewise optimizer using bisection for the unique quartic root. It checks exact algebraic identities at representative rational parameters, numerical integration of the original shared-rain success law, the boundary thresholds and a deterministic pseudorandom search over feasible calendars. Run `python3 check.py` from the containing directory. The proof above—not a finite grid or random comparison—establishes the theorem for all \(p\in(0,1]\) and all deterministic admissible calendars.

## Relationship to prior work

Farrell and colleagues (2023) report strong effects of precipitation timing relative to seeding at dryland restoration sites and propose seeding at multiple times. Their study motivates the mathematical question but does not, in the available abstract, assert a common exponential first-rain model or the two analytic threshold constants. ten Brink, Gremer and Kokko (2020) develop theory of germination timing and dormancy in unpredictable environments; their inspected primary article considers evolutionary germination timing and variable seasons, not three externally chosen seed releases competing for one stochastic rain. Agoungbome and colleagues (2023) evaluate rainfall-dependent sowing windows by agronomic simulation, not this exact finite-cohort probability optimization. Denton and colleagues (2024) study precipitation timing and restoration success empirically.

Related mathematical work on exact observation calendars for transient occupancy, and work on diversified seed banks, addresses fundamentally different events or objective functions. A search of relevant published records, the accessible prior claim ledger, and primary literature did not identify this three-regime result or a stronger theorem directly implying it. Search absence is not proof of novelty: broader operations-research scheduling and perishable-reliability literature may contain equivalent formulations. The motivating primary paper's complete text could not be inspected through the available access routes; it remains a stated priority risk.

## Limitations

The model assumes one independent exponential rain clock, only one effective rainfall event, matched exponential decay rates, independent within-rain establishment conditional on rain, precisely three identical cohort attempts, a fixed initial success parameter, deterministic nonadaptive timing, and no season deadline. It is not an empirical estimate of viable seed mortality, not a recommended seeding schedule for any actual site, and does not claim the same thresholds with multiple rains, differing clock rates, correlated seeds, or cohort-specific viability. No field validation or independent external audit has been performed. Historical priority is provisional, including the uninspected full motivating primary study and broader reliability-optimization literature.

## References

1. Farrell, H. L., et al. (2023). *Soil surface treatments and precipitation timing determine seedling development across southwestern US restoration sites.* Ecological Applications 33, e2834. First publicly published March 2, 2023. https://doi.org/10.1002/eap.2834
2. ten Brink, H., Gremer, J. R., and Kokko, H. (2020). *Optimal germination timing in unpredictable environments: the importance of dormancy for both among- and within-season variation.* Ecology Letters 23, 620–630. https://doi.org/10.1111/ele.13461
3. Agoungbome, S. M. D., et al. (2023). *Optimal Sowing Windows under Rainfall Variability in Rainfed Agriculture in West Africa.* Agronomy 13, 167. https://doi.org/10.3390/agronomy13010167
4. Denton, E. M., et al. (2024). *Spring precipitation amount and timing predict restoration success in a semi-arid ecosystem.* Journal of Applied Ecology. https://doi.org/10.1111/1365-2664.14779
