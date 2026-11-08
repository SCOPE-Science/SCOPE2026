# Balanced specialist allocation maximizes one-link adaptive pollination-service reliability

## Finding

Let \(n\ge3\) independent pollinator service units be allocated among three permanently present plant species in three **nonempty specialist classes**, of sizes \(m_1,m_2,m_3\ge1\) with \(m_1+m_2+m_3=n\). Each unit survives independently with common probability \(p\in(0,1)\), and \(q=1-p\). Each unit initially has a link only to its assigned plant. After observing which units survived, at most **one new plant–unit interaction** may be added; a surviving unit may serve at most one plant, and the outcome succeeds if a matching assigns distinct surviving units to all three plants.

The exact optimal success probability for a given allocation is
\[
R_n(m_1,m_2,m_3;p)=C_n(p)-\sum_{i=1}^3G_{n,p}(m_i),
\]
where
\[
C_n(p)=\sum_{s=3}^{n}\binom ns p^s q^{n-s},\qquad
G_{n,p}(m)=q^{n-m}\sum_{s=3}^{m}\binom ms p^s q^{m-s},
\]
with an empty sum interpreted as zero. **For every \(n\ge3\) and every \(0<p<1\), the unique optimal class-size multiset is the balanced one:** the sizes differ by at most one. Thus, if \(n=3a+t\), \(t\in\{0,1,2\}\), the optimum has \(t\) classes of size \(a+1\) and \(3-t\) classes of size \(a\), with maximum value
\[
C_n(p)-tG_{n,p}(a+1)-(3-t)G_{n,p}(a).
\]

The physical upper bound \(C_n(p)=\Pr\{\mathrm{Bin}(n,p)\ge3\}\) is attained by some design **if and only if** \(3\le n\le6\). For \(n\ge7\), even the optimal design falls strictly short of this upper bound. The positive shortfall at \(n=7\) is exactly \(p^3q^4\).

## Assumptions and scope

- Exactly three distinct host plants are present, with no plant mortality in the sampling period.
- The \(n\) exchangeable pollinator service units are individually independent Bernoulli survivors with identical probability \(p\); all are initially *exclusive specialists* assigned to exactly one plant. Each of the three initial classes is nonempty.
- After all unit failures are observed, a decision-maker may add **at most one** previously absent interaction joining a surviving unit to another plant; interactions are not deleted. The decision can depend on the realized survivor set.
- A surviving unit has unit service capacity: even if it has two links after intervention it may be matched to only one plant. All three plants succeed only if they receive distinct surviving units.
- This is a static combinatorial availability model, not a population-dynamic model, and is not a claim about realistic animal species serving only one plant.

## Proof

**1. Feasibility after observing survivors.** Let \(S\) be the surviving units and let \(r\) be the number of nonempty initial specialist classes represented in \(S\). A full three-plant matching with at most one new edge requires \(|S|\ge3\). It also requires \(r\ge2\): without added edges, only these \(r\) plant types have an incident surviving unit, and a single new edge can raise the number of incident plant types by at most one. Conversely, if \(r=3\), take one surviving unit from each class and use three original links with no addition. If \(r=2\) and \(|S|\ge3\), take one surviving unit from each represented class, then choose any additional surviving unit; its original plant is among those two already served. Add a new edge from this third unit to the unrepresented plant. This gives a three-edge matching using only one additional interaction. Therefore success is equivalent to \(|S|\ge3\) and survivors from at least two specialist classes.

**2. Exact reliability.** The event \(|S|\ge3\) has probability \(C_n(p)\). Its failure despite at least three survivors occurs precisely when all surviving units belong to one of the three disjoint initial classes. For class \(i\), the probability is \(q^{n-m_i}\Pr\{\mathrm{Bin}(m_i,p)\ge3\}=G_{n,p}(m_i)\). These three events are mutually exclusive. Subtracting establishes the displayed formula with no approximation.

**3. Strict balancing.** Fix \(n\), \(p\) and write \(G(m)=G_{n,p}(m)\), \(t_0=p/q>0\). The binomial theorem gives
\[
G(m)=q^n\sum_{s=3}^{m}\binom ms t_0^s.
\]
For every integer \(1\le m\le n-2\), twice applying Pascal's identity yields the exact second forward difference
\[
G(m+2)-2G(m+1)+G(m)
=q^nt_0^2\bigl((1+t_0)^m-1\bigr)
=p^2q^{n-m-2}(1-q^m)>0.
\]
Hence \(G(m+1)-G(m)\) is strictly increasing for positive integers \(m\). If two class sizes satisfy \(x\ge y+2\), moving one unit from the larger to the smaller changes the total penalty by
\[
G(x-1)+G(y+1)-G(x)-G(y)
=-\bigl(G(x)-G(x-1)-G(y+1)+G(y)\bigr)<0.
\]
All class sizes stay positive. Repeated balancing must end with sizes differing by at most one. Every unbalanced profile admits a strict improving transfer; every balanced profile is a permutation of the same multiset. This proves both optimality and uniqueness up to class relabeling, for all \(n,p\) in the stated range.

**4. Sharp physical upper-bound threshold.** No policy succeeds with fewer than three survivors, so \(R_n\le C_n\). For \(0<p<1\), \(G_{n,p}(m)=0\) exactly when \(m\le2\); for \(m\ge3\), the term for \(s=3\) is strictly positive. Therefore \(R_n=C_n\) exactly when every class has size at most two. Three nonempty classes can hold \(n\ge3\) units with that property precisely for \(n\le6\). For \(n=7\), the balanced profile \((3,2,2)\) incurs exactly \(G_{7,p}(3)=p^3q^4\).

## Verification

A standalone standard-library Python checker (`checker.py`) independently enumerates every survivor subset and each possible distinct-unit matching with at most one added edge. It confirms the formula and strict balanced optimality for all positive ordered compositions with \(3\le n\le9\) and \(p\in\{1/4,1/2,3/4\}\). It passed 252 exact rational identity checks and 252 optimization comparisons. These finite tests corroborate the proof; the all-\(n\), all-\(p\) theorem rests on the preceding mathematical argument, not the enumeration.

For illustration, at \(n=6\), \(p=1/2\), balanced classes \((2,2,2)\) give \(R_6=\Pr\{\mathrm{Bin}(6,1/2)\ge3\}=21/32\), whereas without any new edge all classes must retain a unit, giving \((3/4)^3=27/64\). At \(n=7\), \(p=1/2\), the balanced allocation \((3,2,2)\) gives \(49/64\), versus \(83/128\) for the unbalanced allocation \((5,1,1)\).

## Relationship to prior work

Ramos-Jiliberto et al. (2012) study adaptive rewiring and species persistence in empirical mutualistic networks, using population and topological dynamics. Their study motivates a need for solvable adaptive-intervention benchmarks; it does not establish the all-size balanced allocation formula in this discrete, exclusive-service model. Pedroso and Ikeda (2016) study maximum-expected matching with sequential recourse after failures on an existing graph, predominantly in kidney exchange, rather than adding a newly permitted plant–pollinator interaction after Bernoulli unit failures. Dourado et al. (2015) study robust recoverable matchings after edge failures; available material does not establish the present stochastic allocation problem. El-Neweihi, Proschan and Sethuraman (1986) give broader majorization methods for series–parallel/parallel–series reliability; the present post-observation matching event involves an additional three-survivor constraint and is not identified as one of those standard systems. The strict exchange argument uses classical convexity, not a claim that majorization is new.

## Limitations

The intervention is one **additional** feasible interaction after complete observation, not a rewiring that removes an existing interaction; service units are capacity-one and initially exclusive to one plant. Equal independent survival probabilities and no plant loss are essential to the symmetric balancing conclusion. No cost, behavior, time delay, field validation, or coupling to population abundances is modeled. The search did not establish exhaustive historical priority: older reliability-allocation results and unavailable complete matching literature may contain equivalent consequences. Claims are mathematical and should not be interpreted as empirical restoration advice.

## References

1. Ramos-Jiliberto, R., Valdovinos, F. S., Moisset de Espanés, P., and Flores, J. D. (2012). *Topological plasticity increases robustness of mutualistic networks*. Journal of Animal Ecology 81, 896–904. First published 2012-02-07. https://doi.org/10.1111/j.1365-2656.2012.01960.x
2. Pedroso, J. P., and Ikeda, S. (2016). *Maximum-expectation matching under recourse*. arXiv:1605.08616, submitted 2016-05-27. https://arxiv.org/html/1605.08616v1
3. Dourado, M. C., et al. (2015). *Robust recoverable perfect matchings*. Networks 66, 210–213. First published 2015-08-06. https://doi.org/10.1002/net.21624
4. El-Neweihi, E., Proschan, F., and Sethuraman, J. (1986). *Optimal allocation of components in parallel–series and series–parallel systems*. Journal of Applied Probability 23, 770–777. https://doi.org/10.2307/3214014
