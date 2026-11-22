# Sharp dose saturation and square-root placement for an additive river aerator

## Finding

An idealized river with an exponential oxygen-demand load, two unequal positive decay rates, and one instantaneous, nonnegative oxygen deficit reduction has a unique optimal **location** for every strictly positive fixed available dose, when the goal is to minimize the largest oxygen deficit over the entire downstream half-line. There is an explicit critical dose above which additional available aeration cannot improve the minimax deficit because the water cannot be oxygenated above its assumed saturation concentration. Below this dose, the optimal location moves strictly upstream with increasing dose; in the weak-dose limit, its displacement upstream from the untreated oxygen-sag maximum scales as the square root of the dose, not linearly.

Let \(0<a<b\), \(L_0>0\), and \(\Delta>0\). Define
\[
K=\frac{aL_0}{b-a},\qquad g(t)=K(e^{-at}-e^{-bt}),\qquad t_c=\frac{\log(b/a)}{b-a},\qquad M=g(t_c).
\]
Put
\[
s_\star=-\frac{\log(1-M/K)}{b-a},\qquad \Delta_\star=g(s_\star)=M e^{-a s_\star}.
\]
Then \(0<s_\star<t_c\) and \(0<\Delta_\star<M\). The exact minimax location \(s_\Delta\) and optimal maximum deficit \(R_\Delta\) satisfy the following exhaustive classification:

* If \(\Delta\ge\Delta_\star\), then \(s_\Delta=s_\star\) and \(R_\Delta=\Delta_\star\).
* If \(0<\Delta<\Delta_\star\), then \(s_\Delta\) is the unique solution in \((s_\star,t_c)\) of
\[
 g(s)=\left(1-\frac ab\right)K e^{-as}
 \left(\frac{aK e^{-as}}{b(K e^{-bs}+\Delta)}\right)^{a/(b-a)},
\]
and \(R_\Delta=g(s_\Delta)\). The map \(\Delta\mapsto s_\Delta\) is strictly decreasing on \((0,\Delta_\star)\), and \(\Delta\mapsto R_\Delta\) is strictly decreasing there.
* As \(\Delta\downarrow0\),
\[
s_\Delta=t_c-\sqrt{\frac{2\Delta}{abM}}+O(\Delta),\qquad R_\Delta=M-\Delta+O(\Delta^{3/2}).
\]

All location optima are unique on the full unbounded nonnegative domain, including at the critical dose. The expansion concerns fixed \(a,b,L_0\) and \(\Delta\downarrow0\); at exactly zero dose, every location ties and uniqueness fails.

## Assumptions and scope

Travel time \(t\ge0\) parameterizes a steady, spatially homogeneous, advective river with no sediment demand, oxygen photosynthesis terms, or saturation overshoot. Biochemical oxygen demand is \(L(t)=L_0e^{-at}\), and deficit below oxygen saturation obeys
\[
 D'(t)=aL_0 e^{-at}-bD(t),\qquad D(0)=0
\]
between interventions. One instantaneous additive oxygen dose with available deficit reduction \(\Delta>0\) is placed at a chosen travel-time location \(s\ge0\) and saturates when the pre-existing deficit is smaller than its capacity:
\[
D(s^+)=\max\{D(s^-)-\Delta,0\}.
\]
The intervention does not change biochemical demand. The risk includes the one-sided upstream deficit \(D(s^-)\), as well as all post-intervention values; the objective is \(\min_{s\ge0}\sup_{t\ge0}D_s(t)\). This is a fixed **additive** pulse, as distinct from a device that always removes a fixed fraction of the pre-existing deficit. Travel time can be converted to spatial position only after specifying advection velocity.

## Proof

**1. Exact unimodal response.** Without aeration, direct integration yields \(D(t)=g(t)\). Its derivative vanishes only at \(t=t_c\), where \(g\) achieves strict global maximum \(M\), with \(g''(t_c)=-abM\). For a chosen site \(s\) put \(r(s)=\min\{\Delta,g(s)\}\). The full intervention response is
\[
D_s(t)=\begin{cases}g(t),&0\le t<s,\\g(t)-r(s)e^{-b(t-s)},&t\ge s.\end{cases}
\]
For \(0<s<t_c\), every post-intervention branch increases strictly up to \(t_c\), because its derivative is \(g'(t)+b r(s)e^{-b(t-s)}>0\) for \(s\le t\le t_c\). After \(t_c\) its derivative has exactly one zero: write the branch as \(P e^{-a y}-Qe^{-b y}\), with \(y=t-s\), \(P=K e^{-as}>0\), and \(Q=K e^{-bs}+r(s)>0\). Its stationary point is
\[
y_p=\frac{\log(bQ/(aP))}{b-a}>t_c-s>0,
\]
and is a strict maximum. The post-intervention maximum is therefore
\[
E_\Delta(s)=\left(1-\frac ab\right)P\left(\frac{aP}{bQ}\right)^{a/(b-a)}.
\]

**2. Strict minimax crossing.** For \(0<s<t_c\), the largest upstream deficit is \(g(s)\), which is strictly increasing. In the downstream formula, the intervention subtracts \(c(s)e^{-bt}\) from the same pristine curve, where \(c(s)=r(s)e^{bs}\). This coefficient is strictly increasing on \((0,t_c)\). Indeed, when dose-limited, \(c(s)=\Delta e^{bs}\), and when capped, \(c(s)=g(s)e^{bs}=K(e^{(b-a)s}-1)\). The two branches are continuous at their switch. Consequently the downstream maximum \(E_\Delta(s)\) is strictly decreasing, since it is attained after \(t_c\) and the value of the downstream response at every fixed \(t\ge t_c\) strictly decreases as \(s\) increases. As \(s\downarrow0\), \(g(s)\to0<E_\Delta(s)\to M\). At \(s=t_c\), \(g(t_c)=M>E_\Delta(t_c)\) for positive dose. There is exactly one crossing, which is the unique global minimizer of \(\max\{g(s),E_\Delta(s)\}\) for \(s\in(0,t_c)\). Every site at or beyond \(t_c\) incurs the upstream risk \(M\), strictly worse than the crossing.

**3. Critical dose and explicit branch.** At a site where \(r(s)=g(s)\), the deficit is reset to zero. The downstream branch simplifies for \(y=t-s\) to \(D_s(s+y)=K e^{-as}(e^{-ay}-e^{-by})\), so its maximum is exactly \(M e^{-as}\). The strict crossing of \(g(s)\) and \(M e^{-as}\) occurs at \(s=s_\star\): divide their equality by \(e^{-as}\) to obtain \(K(1-e^{-(b-a)s})=M\). Strict monotonicity yields \(s_\star\in(0,t_c)\), and the dose needed for complete deficit reset there is \(\Delta_\star=g(s_\star)\). For any available dose at least this large, the crossing and optimum stay at \(s_\star\). For lower doses, the post-intervention maximum at \(s_\star\) is strictly above the saturated value and therefore exceeds \(g(s_\star)\); the unique crossing moves right to \((s_\star,t_c)\). There \(g(s)>g(s_\star)>\Delta\), so the aerator is dose-limited, \(r(s)=\Delta\), and substituting that into the preceding peak formula yields the stated scalar equation. At fixed \(s\), \(E_\Delta(s)\) strictly decreases with \(\Delta\) until capping. On the entire lower-dose optimum interval it is uncapped. The increasing/decreasing crossing therefore moves strictly left as dose increases, and the optimum risk decreases strictly because \(g\) increases with site position.

**4. Weak-dose singular displacement.** Let \(u=t_c-s_\Delta\). Continuity of the strict crossing as \(\Delta\downarrow0\) gives \(u\to0\). Smooth maximization of the post-intervention branch and the envelope derivative with respect to dose imply, uniformly for \(s\) near \(t_c\),
\[
 E_\Delta(s)=M-\Delta e^{-b(t_c-s)}+O(\Delta^2).
\]
The upstream deficit has the quadratic expansion \(g(t_c-u)=M-\frac12abM u^2+O(u^3)\). Their equality first gives \(u=O(\sqrt\Delta)\), and then \(\frac12abMu^2=\Delta+O(\Delta^{3/2})\). Therefore \(u=\sqrt{2\Delta/(abM)}+O(\Delta)\). Substitution in either expression yields \(R_\Delta=M-\Delta+O(\Delta^{3/2})\), completing all claims.

## Verification

The elementary instance \(a=1\), \(b=2\), \(L_0=1\) gives \(K=1\), \(t_c=\log2\), \(M=1/4\), \(s_\star=\log(4/3)\), and \(\Delta_\star=3/16\) exactly. With \(\Delta=1/10\), the optimal location is approximately \(0.34997783284302425\) and worst deficit approximately \(0.20809639077514855\). Above critical dose the optimal maximum deficit remains \(3/16\), regardless of additional available dose.

Run `python3 CHECK.py` with the standard Python 3 library in the same directory as this document. The checker rederives the analytic peak formula, searches for the balancing site by bisection, tests 150 seeded positive parameter triples against hundreds of alternative locations, tests exact benchmark constants, and checks the leading weak-dose expansion. Its successful replay produced **48,022 diagnostic assertions**. This finite sampling is not an exhaustive proof; the strict-monotone crossing and Taylor argument above supply the universal proof.

## Relationship to prior work

The underlying oxygen sag equation is due to Streeter and Phelps (1925), and the operational question is motivated by work on river aeration placement and watershed quality controls. The archived 1971 EPA methodology discusses efficient aeration placement relative to the unassisted sag and oxygen-standard targets. Rinaldi and Soncini-Sessa (1977) develop aerator cost optimization and a general extremal placement condition for variable impulses under permissible-deficit constraints. Their general insight of balancing limiting deficits is not claimed as new. However, the fixed-dose, physically capped, **one-aerator unbounded-reach minimax** problem, its exact complete-dose threshold, and its square-root weak-dose location law were not located in the accessible portions of those sources. A published analysis of a **fixed-fraction** single aerator (see the specific published-finding corpus reference below) has a different control law, since the actual fraction remaining in the additive-dose model depends on the chosen site; its finite-reach saturation theorem does not directly imply the present dosage phase diagram.

A close 1975 optimization title by Koivo and Phillips could only be assessed bibliographically; equivalently broad impulse/control results could subsume the formula despite different objectives. The 2014 open-access watershed placement study by Chiang and colleagues demonstrates the continuing operational motivation but does not cover the underlying river aeration control problem. Historical priority is therefore provisional and no claim of an independently certified first result is made.

## Limitations

The mathematical result treats instantaneous perfectly mixed aeration with a fixed **maximum available** oxygen dose, a zero-deficit saturation cap, a uniform two-rate steady river, no oxygen supersaturation, a single location, and an unbounded reach. No cost, flow-dependent transport, changing reaeration coefficient, multiple outfalls, nonlinear oxygen demand, or finite-reach constraint is optimized. Large-dose saturation is a consequence of the physical cap and a single site, not a universal principle for aeration design. A date of first issuance is not established for the 1925 original report (which is dated only by month) or for the 1977 report; the separately identified 2014-03-11 open-access source is used as a verifiable day-specific public motivating date, without re-dating the older literature. Independent verification has not been performed.

## References

1. H. W. Streeter and E. B. Phelps, *A Study of the Pollution and Natural Purification of the Ohio River*, U.S. Public Health Bulletin 146 (marked February 1925), https://udspace.udel.edu/server/api/core/bitstreams/6f57c427-5f4f-4435-9d8c-87e3c8c02a66/content .
2. U.S. EPA (1971), *Engineering Methodology for River and Stream Reaeration*, https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=93000JJQ.TXT .
3. S. Rinaldi and R. Soncini-Sessa (1977), *Optimal Allocation of Artificial In-Stream Aeration*, IIASA RR-77-007, https://pure.iiasa.ac.at/708/1/RR-77-007.pdf .
4. A. J. Koivo and G. Phillips (1975), *Optimization of Dissolved Oxygen Concentration in Polluted Streams Using Instream Aeration*, IFAC Sixth Triennial World Congress, https://www.sciencedirect.com/science/article/pii/S1474667017675906 . Full text was not accessible.
5. L.-C. Chiang, I. Chaubey, C. Maringanti and T. Huang (2014), *Comparing the Selection and Placement of Best Management Practices in Improving Water Quality Using a Multiobjective Optimization and Targeting Method*, published March 11, 2014, https://doi.org/10.3390/ijerph110302992 .
6. *Finite-reach saturation and a quadratic placement law for one fractional river aerator* (public mathematical finding), https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-finite-reach-saturation-and-a-quadratic-placement-law-for-one-fr--0af40980b939/RESULT.md .
