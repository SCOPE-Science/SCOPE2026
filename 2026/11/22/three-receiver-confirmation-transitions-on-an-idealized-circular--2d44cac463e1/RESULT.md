# Three-receiver confirmation transitions on an idealized circular seismic fault

## Finding

Consider three identical receivers distributed on a circular seismic source corridor of circumference \(C\). Each receiver has an arc-length detection footprint of length \(\ell\), where \(0<\ell\le C/3\). When an event occurs uniformly in arclength, each receiver whose footprint covers the event independently reports a timely positive signal with probability \(p\in(0,1)\). Receivers outside the event footprint never report a positive signal. Independently of the event and the signals, an action uses the one-positive-signal alarm rule with probability \(1-\theta\), and the two-distinct-positive-signals rule with probability \(\theta\in[0,1]\).

Let \(P_*\) be the maximal probability that the appropriate rule is satisfied, optimized over **all** triples of receiver positions on the circle, including coincident positions. Define

\[
\begin{aligned}
 f_1&=(1-\theta)p,\\
 f_2&=(1-\theta)(2p-p^2)+\theta p^2,\\
 f_3&=(1-\theta)(3p-3p^2+p^3)+\theta(3p^2-2p^3).
\end{aligned}
\]

Then the exact global answer is

\[
\boxed{P_*={\ell\over C}\max\{3f_1,\ f_1+f_2,\ f_3\}.}
\]

The exact transition is

\[
\boxed{\theta_c(p)={2-p\over4-3p},\qquad {1\over2}<\theta_c(p)<1.}
\]

For \(0\le\theta<1/2\), a placement is optimal **if and only if** the three detection footprints are pairwise disjoint up to zero-length intersections. For \(1/2<\theta<\theta_c(p)\), a placement is optimal **if and only if** its multiplicity-two region has length \(\ell\) and its multiplicity-three region has zero length; this includes both a pair of coincident receivers with one separated receiver and a three-distinct-receiver staggered chain. For \(\theta_c(p)<\theta\le1\), a placement is optimal **if and only if** all three footprints coincide.

The equality cases are complete. At \(\theta=1/2\), every placement having zero length of triple coverage is optimal, regardless of its double coverage. At \(\theta=\theta_c(p)\), precisely those placements whose double- plus triple-coverage lengths sum to \(\ell\) are optimal. The optimal geometry depends on \(p,\theta\) but not on \(\ell/C\), as long as the stated sparse-footprint condition holds. The intermediate phase is absent from the corresponding two-receiver problem.

## Assumptions and scope

The circular corridor is a one-dimensional *idealization*, not a measured fault geometry or an assertion that real seismic waves travel along faults at a constant speed. One interpretation is an effective on-time footprint \(\ell=2v_P(T_S-\tau)\), where \(v_P>0\) is an assumed along-corridor P-wave velocity, \(T_S>\tau\) is a common action deadline relative to source initiation, and \(\tau\) is a fixed processing/communication delay. The condition \(2v_P(T_S-\tau)\le C/3\) is essential to the result. The earthquake source is uniform in arclength, all three devices have identical known conditional reporting probability \(p\), and instrument reports are independent even when footprints or positions coincide. No positive reports are generated for sources outside a footprint. The mixed action is selected independently of instrument reports and location.

A 'receiver' means a distinct instrument. Overlapping or coincident instruments are permitted by the *mathematical* feasible set, which does not impose minimum physical spacing, correlated noise, site constraints, station failures, false positives, uncertain speed, station installation costs, or finite signal-propagation geometry beyond the fixed footprints. Thus the result is a reference benchmark for how confirmation requirements alter station clustering, not a deployment instruction.

## Proof

**1. Conditional probabilities.** Given that exactly \(j\in\{0,1,2,3\}\) of the three footprints cover the event, the number of timely reports is binomial with parameters \((j,p)\). Hence the chance of satisfying the mixed rule is \(f_j\), with \(f_0=0\) and the explicit \(f_1,f_2,f_3\) above.

**2. Exact multiplicity reduction.** For any three footprints, let \(m_j\) be the arclength where exactly \(j\) footprints cover an event, ignoring the measure-zero endpoints. Counting the footprints gives

\[
 m_1+2m_2+3m_3=3\ell.
\]

As the source distribution is uniform, the mixed success probability satisfies

\[
 C P=m_1f_1+m_2f_2+m_3f_3
 =3\ell f_1+m_2(f_2-2f_1)+m_3(f_3-3f_1).
\tag{1}
\]

**3. Sharp geometric constraint.** Always

\[
 m_2\ge0,\quad m_3\ge0,\quad m_2+m_3\le\ell.
\tag{2}
\]

To show the last inequality, first suppose the union of footprints is the entire circle. Then its length is \(C\), whereas the total footprint length is \(3\ell\le C\). Consequently the footprints partition the circle up to null sets and \(m_2+m_3=0\). Otherwise cut the circle at a point outside all footprints and identify the three connected arcs with ordinary equal-length intervals on the line. Order them by their left endpoints, calling them \(I_1,I_2,I_3\). Their right endpoints have the same order because all lengths equal \(\ell\). Every point covered by at least two intervals belongs to the middle interval \(I_2\): the only nontrivial case is membership in both \(I_1,I_3\), which entails membership in \(I_2\) by endpoint ordering. Thus the region of multiplicity at least two has length at most \(|I_2|=\ell\). This proves (2).

The three vertices of the triangle in (2) are **all attainable** when \(3\ell\le C\): \((m_2,m_3)=(0,0)\) uses three disjoint arcs; \((\ell,0)\) uses two coincident arcs and a disjoint third (alternatively three successively half-shifted arcs); and \((0,\ell)\) uses three coincident arcs. By the linear identity (1), optimizing over the larger triangle (2) gives the exact maximum and is attained by these constructions. The values at its vertices are respectively \(3\ell f_1\), \(\ell(f_1+f_2)\), and \(\ell f_3\), proving the boxed formula.

**4. Strict phases and equality cases.** Direct subtraction yields

\[
\begin{aligned}
 f_2-2f_1&=p^2(2\theta-1),\\
 f_3-f_2-f_1&=p^2\big[(4-3p)\theta-(2-p)\big],\\
 f_3-3f_1&=p^2\big[(6-3p)\theta-(3-p)\big].
\end{aligned}
\]

Because \(p\in(0,1)\), \(1/2<\theta_c=(2-p)/(4-3p)<1\). Below \(1/2\), the coefficients of both \(m_2,m_3\) in (1) are negative and only \((0,0)\) is optimal. Between \(1/2\) and \(\theta_c\), the coefficient of \(m_2\) is strictly positive and exceeds that of \(m_3\); the sole maximizing multiplicity point is \((\ell,0)\). Above \(\theta_c\), the coefficient of \(m_3\) is strictly positive and exceeds that of \(m_2\); the sole maximizing multiplicity point is \((0,\ell)\). At \(\theta=1/2\), the \(m_2\) coefficient vanishes but the \(m_3\) coefficient equals \(-p^3/2<0\), giving exactly \(m_3=0\). At \(\theta=\theta_c\), both coefficients agree and are strictly positive, giving exactly \(m_2+m_3=\ell\). These facts also prove all the placement equality conditions, not uniqueness of physical coordinates.

For two receivers, with overlap length \(z\in[0,\ell]\), the same reduction is \(CP_2=2\ell f_1+z(f_2-2f_1)\), so only separate and coincident extremal regimes occur; there is no intermediate multiplicity profile.

## Verification

The standalone \(\texttt{checker.py}\) integrates success probabilities over the actual circular arc intersections by sorting footprint endpoints, **not** by reusing the triangle inequality. It checks 18,000 pseudorandom configurations, footprint sizes, reporting probabilities and confirmation fractions against the exact upper bound and its three attaining constructions; it also tests 14 equality-boundary cases and multiplicity accounting. These finite calculations are supplementary checks only. The proof above establishes the theorem over the entire continuous parameter domain.

For example, at \(p=0.8\), \(\theta=0.625\), \(\ell/C=0.25\), the exact mean success probabilities for disjoint, paired-plus-disjoint and all-coincident footprints are \(0.225\), \(0.265\) and \(0.233\), respectively. The critical confirmation fraction is \(\theta_c=0.75\), so the intermediate geometry is strictly best. Three distinct receivers centered at normalized arc positions \(0.125,0.25,0.375\) also attain \(0.265\) when \(C=1\) and \(\ell=0.25\).

## Relationship to prior work

Zhang et al. (2023) analyze the impact of seismic-station spacing and the distinction between single-station and multi-station early warning, with a realistic blind-zone framework, but they do not optimize a mixed one- versus two-confirmation probability for three equal arclength footprints. Papadopoulos et al. (2023) provide a general probabilistic framework for early-warning value and false-alarm tradeoffs; their geographical risk model is not this exact three-interval optimization.

Litvak et al., *Increasing Detection Performance of Surveillance Sensor Networks*, Section 5.2, already analyze optimal overlapping placement of **two** imperfect sensors, including false-alarm effects, and Section 5.3 studies groups of co-located sensors. The binomial detection algebra and overlap tradeoff are therefore established prior ideas, not claimed as inventions here. Their studied decision problems do not supply the three equal-arclength mixed-confirmation formula or its intermediate strictly optimal regime. Asano, Brass and Sasahara's *Disc Covering Problem with Application to Digital Halftoning* provides an established exactly-once interval-coverage optimization, selecting from prescribed intervals; its objective favors removing triple intersections, rather than the competing one- versus two-report benefits with three freely chosen positions. Shan, Xu and Cheng (2016) study probabilistic target coverage and minimum sensor counts, not the same continuum global optimum. Ammari (2023) develops planar \(k\)-coverage density and tiling, a broader but different design problem; this paper's accessible text does not establish the specific three-arc mixed rule. The familiar \(k\)-coverage and Bonferroni concepts are prior art. No global claim of first discovery across all surveillance and interval-optimization literature is made.

## Limitations

The \(\ell\le C/3\) cutoff is necessary for the stated phase diagram: longer footprints can wrap into mandatory overlaps, invalidating the sharp triangle's three feasible vertices. Co-location may create strongly correlated site errors and is usually operationally unattractive; the theorem does not account for it. False alarms are treated only indirectly through the externally specified mixture of action confirmation requirements; it does not optimize actual false-alarm costs or predict earthquake rates. Uniform source location, equal footprint lengths and probabilities, independent reports, and fixed deadlines are strong idealizations. The reported novelty assessment is conditional on accessible comparisons and does not establish historical priority. Independent validation has not been performed.

## References

1. Y. Zhang, Z. Wu, F. Romanelli et al., "Earthquake Early Warning System (EEWS) empowered by Time-Dependent Neo-Deterministic Seismic Hazard Assessment (TD-NDSHA)", *Terra Nova* 35 (2023), 230–239, first online 2023-03-03. https://doi.org/10.1111/ter.12647. Full text: https://arts.units.it/retrieve/80c7613b-13b7-46d0-8ef6-de936e9c18de/Terra%20Nova%20-%202023%20-%20Zhang.pdf
2. A. N. Papadopoulos et al., "A framework to quantify the effectiveness of earthquake early warning in mitigating seismic risk", *Earthquake Spectra* (2023), first online 2023-02-24. https://doi.org/10.1177/87552930231153424.
3. N. Litvak et al., "Increasing Detection Performance of Surveillance Sensor Networks", Sections 5.2–5.3, https://miis.maths.ox.ac.uk/268/2/thales-report.pdf.
4. T. Asano, P. Brass and S. Sasahara, "Disc Covering Problem with Application to Digital Halftoning", https://www.jaist.ac.jp/~t-asano/papers/Disc-covering.pdf.
5. A. Shan, X. Xu and Z. Cheng, "Target Coverage in Wireless Sensor Networks with Probabilistic Sensors", *Sensors* 16 (2016), 1372. https://doi.org/10.3390/s16091372.
6. H. M. Ammari, "A Computational Geometry-based Approach for Planar k-Coverage in Wireless Sensor Networks", *ACM Transactions on Sensor Networks* 19 (2023), article 35. https://doi.org/10.1145/3564272.
