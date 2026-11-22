# A universal interior-release law for invasion-exposed habitat restoration

## Finding

**Theorem (unique precommitted release and its two horizon scales).** Consider two initially empty habitat sites, with site 1 made available at time zero and site 2 made available at a predetermined time \(t\in[0,T]\), where \(T>0\) is a fixed evaluation horizon. Site 1 first becomes permanently occupied by a native colonizer at rate \(a>0\) or an invasive colonizer at rate \(b>0\), whichever arrives first. Site 2, after being made available, receives invasive colonizers at rate \(d>0\); it receives native colonizers at rate \(c>0\) only after native occupation of site 1. All active arrival clocks are independent homogeneous Poisson processes; each site's first arrival permanently occupies it. The success event is native occupation of *both* sites by \(T\).

Put \(k=a+b\), \(h=c+d\), and
\[
J(u)=\int_0^u e^{-(k+d)y}\bigl(1-e^{-h(u-y)}\bigr)\,dy,\qquad u\ge0.
\]
There is, for **every** set of positive rates and every \(T>0\), exactly one global success-probability-maximizing fixed release time \(t_T\), and \(0<t_T<T\). It is the unique solution of
\[
d e^{h(T-t_T)}J(T-t_T)=\frac{h}{k}(e^{k t_T}-1).
\]
Moreover \(t_T\) is continuously differentiable and strictly increases with \(T\), with \(0<dt_T/dT<1\). Its sharp limiting laws are
\[
t_T=\frac d2 T^2+O(T^3)\quad(T\downarrow0),
\]
\[
t_T=\frac{h}{k+h}T-\frac{1}{k+h}\log\frac{h(k+d)}{kd}+o(1)\quad(T\to\infty).
\]
For large horizons the optimal success probability tends to \(ac/(kh)\), while immediately opening both sites tends to \(ac/[h(k+d)]\); their limiting difference is \(acd/[hk(k+d)]>0\). Only \(a+b\), rather than the two first-site rates separately, influences the optimal time. The requirement \(d>0\) is sharp: when \(d=0\) with \(a,b,c>0\), opening site 2 at \(t=0\) is uniquely optimal.

## Assumptions and scope

A decision consists of one **nonadaptive**, deterministic opening time \(t\) for site 2. Opening itself has no cost or effect on biological rates. Before opening, site 2 cannot be colonized by either class. After opening, invasive propagules may arrive before site 1 is native, whereas native propagules reach site 2 only following native settlement of site 1. Once either class occupies a site, no extinction, displacement, retry, or recolonization occurs during the horizon. First-site invasion prevents the specified two-native-site success event. Independent Poisson arrivals have constant positive rates \(a,b,c,d\). This is a minimal source-dependent colonization and secondary-invasion benchmark, not an estimate of field probabilities.

## Proof

Write \(S\) for the first successful native colonization time at site 1 *provided it wins against the invader*. The subprobability density of that event is \(a e^{-ks}\,ds\), where \(k=a+b\). Conditional on \(S=s\le t\), both classes first compete for site 2 at \(t\), and the probability of native settlement by \(T\) is \(\frac c h(1-e^{-h(T-t)})\). Conditional on \(t<s\le T\), the site-2 invader must not arrive in \([t,s)\), an event of probability \(e^{-d(s-t)}\); after \(s\), the native must win the site-2 race by \(T\), with probability \(\frac c h(1-e^{-h(T-s)})\). Integrating disjoint scenarios gives the exact objective
\[
P_T(t)=\frac{ac}{h}\left[\frac{1-e^{-kt}}{k}\bigl(1-e^{-h(T-t)}\bigr)
+e^{-kt}J(T-t)\right]. \tag{1}
\]
This derives the success probability without treating the first-site event as certain or assuming that a second-site invasion can be undone.

Set \(u=T-t\). Differentiating the two integrals, with the common boundary terms cancelling, gives
\[
P_T'(t)=\frac{ac}{h}e^{-kt-hu}
\left[d e^{hu}J(u)-\frac hk(e^{kt}-1)\right]. \tag{2}
\]
For fixed rates let \(F(u)=d e^{hu}J(u)\) and \(G(t)=\frac hk(e^{kt}-1)\). The integrand of \(J\) is nonnegative, \(J(0)=0\), and
\[
J'(u)=h\int_0^u e^{-(k+d)y-h(u-y)}\,dy>0\qquad(u>0).
\]
Therefore \(F'(u)>0\) for \(u>0\) and \(G'(t)=h e^{kt}>0\). The difference \(F(T-t)-G(t)\) strictly decreases from a positive value at \(t=0\) to a negative value at \(t=T\). Equation (2) thus changes sign exactly once from positive to negative. This proves a unique interior **global**, not merely local, maximizer. Implicit differentiation of \(F(T-t_T)=G(t_T)\) yields
\[
\frac{dt_T}{dT}=\frac{F'(T-t_T)}{F'(T-t_T)+G'(t_T)}\in(0,1).
\]

For small \(u\), \(J(u)=hu^2/2+O(u^3)\). Since \(G(t_T)=F(T-t_T)=O(T^2)\) and \(G(t)\ge ht\), first \(t_T=O(T^2)\). Substituting into the stationary equation then gives \(t_T=dT^2/2+O(T^3)\).

For \(T\to\infty\), the stationary equation forces both \(t_T\to\infty\) and \(T-t_T\to\infty\): boundedness of either would make the increasing exponential on the other side unbalanced. Dominated convergence gives \(J(u)\to 1/(k+d)\). Hence
\[
\frac{d}{k+d}e^{h(T-t_T)}(1+o(1))
=\frac hk e^{kt_T}(1+o(1)),
\]
which upon taking logarithms gives the asserted linear law and constant offset. Equation (1) then yields \(P_T(t_T)\to ac/(kh)\). At \(t=0\), equation (1) reduces to \(P_T(0)=acJ(T)/h\to ac/[h(k+d)]\). These results imply the exact limiting advantage. Finally, at \(d=0\), differentiating equation (1) directly gives \(P_T'(t)<0\) for every \(t\in(0,T)\), proving the boundary statement.

## Verification

The accompanying standalone Python 3 script `check.py` uses an independently implemented composite Simpson integral for the two disjoint success scenarios and compares it with equation (1) for 1,600 seeded random positive-rate parameter sets. It also compares derivatives by finite differences, checks the analytic global maximizer against 26 mesh timings per case, checks monotonicity in \(T\), and tests the short- and long-horizon formulas for three additional parameter sets. All checks passed in the supplied environment. These finite calculations corroborate, but do **not** replace, the analytic proof.

Illustration: with \((a,b,c,d,T)=(2,1,3,1,1)\), the optimal opening is \(t_T\approx0.349542503\) and the two-native success probabilities are \(P_T(t_T)\approx0.397028630\) and \(P_T(0)\approx0.340658177\). These rates are hypothetical.

## Relationship to prior work

Torres and colleagues (2023) experimentally studied the order and timing of invasive-species removal, finding that different removal sequences and simultaneous removals alter native and secondary-invader outcomes. Their study motivates staged restoration but does not specify a two-site source-dependent exponential-clock objective or an analytical release-time classification. Torres and colleagues (2024) discussed inverse priority effects using three-species Lotka–Volterra competition models, a different dynamical structure. Tielke and Vos (2024) studied restoration windows and simultaneous versus sequential reintroduction in deterministic food-web models, not fixed release of a source-dependent second site under competing Poisson arrival clocks. Southwell, Heard and McCarthy (2017, online) optimized biodiversity-offset creation timing for a single-species spatial metapopulation with financial growth of the offset; that is a distinct objective and mechanism, but its full text could not be inspected. The present result must therefore be read as a proved property of the stated minimal model, with historical priority provisional rather than universally certified.

## Limitations

The result assumes time-homogeneous independent colonization hazards, permanent occupancy after the first arrival, one obligate native source, fixed nonadaptive timing, no hidden pre-opening colonists, no density-dependent interactions and no intervention cost. Its exact asymptotics require arbitrarily long mathematical horizons and do not predict field outcomes. It does not show that staged removal always improves ecological restoration in general: changing the underlying biology can reverse the conclusion. The full text of a relevant historical biodiversity-offset study was inaccessible, so priority is not independently established.

## References

1. Torres, A., Morán-López, T., Rodriguez-Cabal, M. A., and Núñez, M. A. (2023, first published November 20). *Inverse priority effects: The order and timing of removal of invasive species influence community reassembly*. Journal of Applied Ecology. https://doi.org/10.1111/1365-2664.14529
2. Torres, A., et al. (2024, first published January 6). *Inverse priority effects: A role for historical contingency during species losses*. Ecology Letters. https://doi.org/10.1111/ele.14360
3. Tielke, A.-K., and Vos, M. (2024, first published January 14). *Successful reintroduction of species: improving on windows of opportunity for biodiversity repair*. Restoration Ecology. https://doi.org/10.1111/rec.14091
4. Southwell, D. M., Heard, G. W., and McCarthy, M. A. (2017, accepted manuscript first available December 20). *Optimal timing of biodiversity offsetting for metapopulations*. Ecological Applications. https://doi.org/10.1002/eap.1666
5. Weidlich, E. W. A., et al. (2020, first published November 6). *Priority effects and ecological restoration*. Restoration Ecology. https://doi.org/10.1111/rec.13317
