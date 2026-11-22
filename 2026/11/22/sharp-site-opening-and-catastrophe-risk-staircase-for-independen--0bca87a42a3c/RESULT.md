# Sharp site-opening and catastrophe-risk staircase for independent founding attempts

## Finding

Consider any real founding-effort budget \(B>h>0\), site-opening cost \(h\), lineage success probability \(p\in(0,1]\), and independent site-unsuitability probability \(c\in(0,1)\). Each opened site receives a Poisson number of released founders with mean effort \(x_i>0\). In a suitable site each founder independently leaves a lasting lineage with probability \(p\); an unsuitable site fails regardless of the release. There are as many identical, independent candidate sites as the budget can open. The goal is the probability that **at least one** site establishes a lasting lineage, not expected final population size or the number of successful sites.

Define
\[
F_c(x)=c+(1-c)e^{-px},\qquad g_c(x)=-\log F_c(x).
\]
For any fixed feasible number \(m\) of opened sites, the *unique* success-maximizing allocation uses the complete budget and assigns the same effort \(x_m=B/m-h\) to each site; its establishment probability is exactly
\[
P_m=1-\left[c+(1-c)e^{-p(B/m-h)}\right]^m.
\]
Feasible integers are \(m\ge1\) and \(mh<B\). Let \(x_*(c,p,h)>0\) be the unique solution of
\[
\boxed{g_c(x)=(x+h)\frac{p(1-c)e^{-px}}{c+(1-c)e^{-px}}.}
\]
Then the continuously relaxed optimum uses \(m_0=B/(h+x_*)\) sites. The **exact integer optimum** is obtained by checking at most the two adjacent feasible integers bracketing \(m_0\), or the nearest feasible endpoint if both do not exist. There can be at most two optimal integer counts, and in that case they are adjacent.

As \(c\) increases, \(x_*\) decreases strictly, while every globally optimal *integer* site count moves weakly upward: there is no reversal to fewer sites. More precisely, adjacent feasible counts \(m\) and \(m+1\) cross at **at most one** \(c\in(0,1)\), in the direction from \(m\) to \(m+1\). A crossing occurs if and only if
\[
(m+1)\left(1-e^{-p x_{m+1}}\right)>m\left(1-e^{-p x_m}\right).
\]
When it exists, its unique value is given by the one-dimensional equation
\[
(m+1)g_c(x_{m+1})=m g_c(x_m).
\]
The optimized integer count therefore follows a possibly truncated, strictly ordered staircase with single adjacent ties, not a continuously varying or re-entrant schedule.

The continuous effort has the explicit limiting descriptions
\[
\begin{aligned}
& p x_*\longrightarrow y_\beta\quad(c\uparrow1),
\quad e^{y_\beta}=1+y_\beta+\beta,\quad y_\beta>0,\quad\beta=ph;\\
& px_*=\log\frac{1-c}{c}-\log\log\frac{1-c}{c}+\log(ph)+o(1)
\quad(c\downarrow0).
\end{aligned}
\]
For \(B=10\), \(h=p=1\), the uniquely optimal integer counts are \(m=3\) at \(c=0.1\) and \(m=5\) at \(c=0.9\), with total establishment probabilities approximately \(0.9934319292\) and \(0.2785496225\), respectively.

## Assumptions and scope

Budgets and Poisson arrival intensities are continuous, but the number of opened sites is an integer. Opening an unused site is never allowed; \(mh<B\) ensures every open site has positive founder effort. A site has a single latent suitability state drawn independently of other sites, and lineage outcomes are independent conditional on suitability. No dispersal between established sites, mating limitation, density dependence, correlated environmental failures, temporal reallocation, site-quality heterogeneity, or future maintenance costs are included. The comparison concerns one-shot establishment before ongoing population dynamics, not a prediction for any named species. Fixed \(B\), \(h\), and \(p\) are maintained when varying \(c\).

## Proof

**1. From Poisson founders to an exact product objective.** Independent thinning of a Poisson random release with mean \(x\) leaves Poisson \(px\) successful lineages at a suitable site; its zero-lineage probability is \(e^{-px}\). Marginalizing over suitability gives \(F_c(x)\). Independent site outcomes yield \(P=1-\prod_i F_c(x_i)\).

**2. Exact allocation at fixed site count.** Direct differentiation gives
\[
\begin{split}
g_c'(x)&=\frac{p(1-c)e^{-px}}{F_c(x)}>0,\\
g_c''(x)&=-\frac{p^2c(1-c)e^{-px}}{F_c(x)^2}<0.
\end{split}
\]
Thus total success is strictly increasing in each effort. Since \(\log(1-P)=-\sum_i g_c(x_i)\), strict concavity of \(g_c\) and Jensen's strict equality case imply \(\sum_i g_c(x_i)\le m g_c((B-mh)/m)\), with equality only at the uniform allocation. All allocated effort is used because \(g_c'>0\).

**3. Unique relaxed optimum and two-candidate integer rule.** Put \(x=B/m-h\) and \(J(m)=m g_c(B/m-h)\) on the real interval \((0,B/h)\). Then
\[
J''(m)=\frac{B^2}{m^3}g_c''(B/m-h)<0.
\]
Also \(J\to0\) at both endpoints. Hence there is a unique interior maximum. Using \(m=B/(x+h)\), maximizing \(J\) is equivalent to maximizing \(g_c(x)/(x+h)\) for \(x>0\). Its derivative has numerator
\[
H(x)=(x+h)g_c'(x)-g_c(x),\qquad H'(x)=(x+h)g_c''(x)<0.
\]
At \(x=0\), \(H(0)=hp(1-c)>0\), while \(H(\infty)=\log c<0\). Exactly one root \(x_*\) exists. Strict concavity of \(J\) means all integer maximizers, if available, lie in the pair \(\{\lfloor m_0\rfloor,\lceil m_0\rceil\}\) intersected with feasible integers, with the nearest boundary integer used when the interval lies outside the feasible set. A tie cannot involve nonadjacent counts.

**4. Monotone catastrophe-risk policy and sharp integer crossovers.** Set \(r=(1-c)/c\), \(y=px\), and
\[
G_r(y)=g_c(y/p)=\log\frac{1+r}{1+re^{-y}}=\int_0^y v_r(t)\,dt,
\quad v_r(t)=\frac{re^{-t}}{1+re^{-t}}.
\]
For \(r_2>r_1>0\),
\[
\frac{v_{r_2}(t)}{v_{r_1}(t)}
=\frac{r_2}{r_1}\frac{1+r_1e^{-t}}{1+r_2e^{-t}}
\]
is *strictly increasing* in \(t\ge0\). Consequently, for every \(s>t>0\), the ratio \(G_r(s)/G_r(t)\) is strictly increasing in \(r\): write the ratio \(G_{r_2}/G_{r_1}\) as a weighted mean of the increasing pointwise ratio \(v_{r_2}/v_{r_1}\), and note that its mean over \([0,s]\) strictly exceeds that over \([0,t]\). Equivalently \(g_c(s/p)/g_c(t/p)\) strictly *decreases* in \(c\). Since the comparison of adjacent counts is
\[
P_{m+1}>P_m\quad\Longleftrightarrow\quad
\frac{g_c(x_m)}{g_c(x_{m+1})}<\frac{m+1}{m},
\]
each adjacent advantage crosses at most once, in favor of more sites as \(c\) increases. At \(c\downarrow0\), \(g_c(x)\to px\), and
\[
m g_c(x_m)-(m+1)g_c(x_{m+1})\longrightarrow ph>0,
\]
so the smaller count wins initially. At \(c\uparrow1\), \(g_c(x)/(1-c)\to1-e^{-px}\); a strict switch occurs precisely under the stated condition. Equality at the endpoint does not give a switch inside \((0,1)\). Nonadjacent global jumps would require a tie between nonadjacent integer optima at an intermediate catastrophe rate, ruled out by strict concavity. Hence the entire optimal integer policy is nondecreasing.

To see that \(x_*\) decreases strictly with \(c\), observe that \(G_r(y)/v_r(y)-y\) is strictly increasing in \(y\), because its derivative is \(-G_r(y)v_r'(y)/v_r(y)^2>0\). For fixed \(y\), the ratio \(G_r(y)/v_r(y)\) strictly decreases with \(r\): its integral representation is \(\int_0^y v_r(t)/v_r(y)\,dt\) and the pointwise ratio decreases as \(r\) increases for \(t<y\). Therefore the equation \(G_r(y)/v_r(y)-y=ph\) forces \(y_*=px_*\) to strictly increase with \(r\), hence strictly decrease with \(c\).

**5. Limits.** For \(c\uparrow1\), divide the stationarity equation by \(1-c\) and use \(g_c(x)/(1-c)\to1-e^{-px}\); compactness follows from the strict monotone root and its bracketing, yielding \(e^y=1+y+ph\), with one positive root. For \(c\downarrow0\) put \(r=(1-c)/c\), \(L=\log r\), \(y=px_*\), \(z=re^{-y}\), and \(\beta=ph\). The exact stationarity equation rearranges to
\[
\beta z=\log(1+r)+z\log(1+1/r)-\log(1+z)-z\log(1+1/z).
\]
For \(r\) sufficiently large, \(\beta-\log(1+1/r)>\beta/2\), so \(z=O(L)\). The last three terms beyond \(\log(1+r)\) are \(o(L)\), since \(\log(1+z)=O(\log L)\), \(z\log(1+1/z)\le1\), and \(z\log(1+1/r)=o(1)\). Thus \(z\sim L/\beta\) and \(y=L-\log z=L-\log L+\log\beta+o(1)\), as claimed. This also implies \(x_*\to\infty\) and for any fixed budget the optimal integer site count is one for all sufficiently small \(c>0\).

## Verification

Run `python3 check_founder.py` with Python 3 and standard library only. The tests check the unique stationarity root, concavity, optimal integer candidates against exhaustive feasible enumeration for multiple parameter grids, monotone site count on parameter grids, and the two displayed numerical examples. Diagnostics cannot certify universal quantified statements; Steps 1–5 provide the analytic proof. The two example establishment probabilities are computed by direct substitution into the exact \(P_m\) expression.

## Relationship to prior work

Duncan, Blackburn, Rossinelli and Bacher (2014), especially their sections on demographic stochasticity and environmental heterogeneity, provide the population-founding and unsuitability mechanisms that motivate the single-site failure function. Their work derives and fits establishment-probability curves rather than optimizing the number of independent sites under opening costs. Berger-Tal, Bar-David and Saltz (2012) examine multiple reintroduction sites and compare release schedules using an individual-based deer simulation over a fixed small set of sites; they do not establish the present exact independent Poisson founder and fixed site-opening budget policy. Canessa et al. (2014) optimize reintroduction release schedules and stage-specific choices in a structured population model; their objective, assumptions and decisions differ. Helmstedt and Possingham (2014) address one or two fenced reserve configurations under longer-term costs, and Helmstedt and Possingham (2016, first published after the archive cutoff) optimize a fixed three-site time-dependent reintroduction program. Neither inspected statement implies the arbitrary-count one-shot Poisson allocation theorem and strictly ordered catastrophe-risk staircase. This is not a claim that no related general stochastic resource-allocation theorem exists; broad theorem-based priority remains a residual risk.

## Limitations

Poisson numbers of independent founders, identical sites, independent binary unsuitability, and continuous effort are restrictive. If founders are allocated as fixed integers, if success requires mating pairs or quorum effects, or if environmental failures are correlated, Jensen-based equal allocation and the staircase need not remain valid. No empirical parameter identification, uncertain-cost robustness, time-dependent reintroduction, correlated risks, or optimality for alternate success objectives is asserted. Existing stochastic programming and convexity/majorization methods could encompass special cases; the originality comparison is limited to the expressly inspected materials. No independent audit has been performed.

## References

1. Duncan, R. P., Blackburn, T. M., Rossinelli, S. & Bacher, S. (2014), *Quantifying invasion risk: the relationship between establishment probability and founding population size*, Methods in Ecology and Evolution, DOI: https://doi.org/10.1111/2041-210X.12288 (first published 23 October 2014).
2. Canessa, S., Hunter, D., McFadden, M., Marantelli, G. & McCarthy, M. A. (2014), *Optimal release strategies for cost-effective reintroductions*, Journal of Applied Ecology, DOI: https://doi.org/10.1111/1365-2664.12253 (first published 15 March 2014).
3. Helmstedt, K. J., Possingham, H. P., Brennan, K. E. C., Rhodes, J. R. & Bode, M. (2014), *Cost-efficient fenced reserves for conservation: single large or two small?*, Ecological Applications, DOI: https://doi.org/10.1890/13-1579.1 (first online 1 October 2014).
4. Helmstedt, K. J. & Possingham, H. P. (2016 online; 2017 issue), *Costs are key when reintroducing threatened species to multiple release sites*, Animal Conservation, DOI: https://doi.org/10.1111/acv.12319 (first online 29 November 2016).
5. Berger-Tal, O., Bar-David, S. & Saltz, D. (2012), *Effectiveness of Multiple Release Sites in Reintroduction of Persian Fallow Deer*, Conservation Biology, DOI: https://doi.org/10.1111/j.1523-1739.2011.01746.x (2011 article metadata; 2012 volume).
