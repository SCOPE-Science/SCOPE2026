# Optimal snapshot calendars for a single transient ecological presence episode

## Finding

In a stochastic presence episode with a single exponential arrival and independent exponential departure, the optimal times for a fixed number of instantaneous ecological observations have a unique all-size formula. Their gaps increase with time, and enforcing equal spacing incurs a sharp logarithmic penalty in missed-episode probability as the observation count grows.

Let \(r=\alpha/\mu\). Define \(b_0=0\), and for \(k\ge1\) set

\[
b_k=\begin{cases}
[r-(r-1)b_{k-1}]^{-1/(r-1)},&r\ne1,\\
\exp(b_{k-1}-1),&r=1.
\end{cases}
\]

The optimal detection probability is exactly \(b_n\) and the *unique* optimal times are

\[
t_i=\frac{1}{\mu}\sum_{k=n-i+1}^{n}[-\log b_k],\qquad 1\le i\le n.
\]

In particular, when \(\alpha=2\mu\),

\[
b_n=\frac{n}{n+1},\qquad
 t_i=\frac1\mu\log\left(\frac{n+1}{n-i+1}\right).
\]

For every fixed positive rate ratio, \(n(1-b_n)\to2\mu/\alpha\) and \(t_n\sim2\log n/\alpha\). If all observation gaps must instead equal a common optimally chosen interval, the minimum miss probability is asymptotic to \(\mu\log n/(2\alpha n)\), whereas the unrestricted optimum is asymptotic to \(2\mu/(\alpha n)\). Their ratio is asymptotic to \((\log n)/4\).

## Assumptions and scope

Fix arbitrary rates \(\alpha>0\) and \(\mu>0\) and an integer \(n\ge1\). There is exactly one possible occupancy episode: its initial time is \(A\sim\operatorname{Exp}(\alpha)\) and its duration is an independent \(L\sim\operatorname{Exp}(\mu)\). The site is occupied precisely during \([A,A+L)\). One may choose \(n\) predetermined noiseless instantaneous observations at strictly increasing finite times \(0<t_1<\dots<t_n\). Observation at any occupied instant detects the episode perfectly; after disappearance the site never becomes occupied again. There is no time horizon, monitoring-duration cost, travel cost, imperfect detectability, or adaptive switching to another site. Success is the probability that at least one observation falls within the episode.

Write the dimensionless observation times \(u_i=\mu t_i\) and gaps \(h_i=u_i-u_{i-1}\), with \(u_0=0\), and \(r=\alpha/\mu\). Each gap must be positive; the dynamic program extends continuously to nonnegative gaps so that attainment and uniqueness can be proved.

## Proof

**1. Disjoint first detections.** A successful episode has exactly one earliest observing time. For the earliest detection to occur at observation \(i\), its arrival must lie strictly after the preceding observation, and it must still be present at observation \(i\). Hence

\[
D_n(h_1,\ldots,h_n)=\sum_{i=1}^{n}e^{-r u_{i-1}}g_r(h_i),
\quad
g_r(h)=\int_0^h r e^{-rs}e^{-(h-s)}\,ds.
\]

Evaluation yields

\[
g_r(h)=\begin{cases}
\dfrac{r}{r-1}(e^{-h}-e^{-rh}),&r\ne1,\\
h e^{-h},&r=1.
\end{cases}
\]

This disjoint decomposition is exact, including episodes arriving before the first observation or disappearing between observations.

**2. Bellman recursion and unique maximizers.** Let \(b_k\) be the largest possible probability of detecting an episode with \(k\) remaining observations, starting from an as-yet-unobserved unoccupied state at the origin. Independence and exponential memorylessness imply

\[
b_0=0,\qquad b_k=\max_{h\ge0}\{g_r(h)+e^{-rh}b_{k-1}\}.
\]

When \(r\ne1\), differentiation with respect to \(h\) gives

\[
\frac{d}{dh}\bigl(g_r(h)+e^{-rh}b\bigr)
=\frac{r e^{-rh}}{r-1}
\left[r-(r-1)b-e^{(r-1)h}\right].
\]

For every \(0\le b<1\), this derivative is positive before and negative after the single positive critical point

\[
h_*(b)=\frac{\log[r-(r-1)b]}{r-1}.
\]

For \(r=1\), the optimized expression is \((h+b)e^{-h}\), with its unique maximizer at \(h_*(b)=1-b\). Substitution in either case gives the optimized value \(e^{-h_*(b)}\). Thus the stated recursion follows, with \(h_k=-\log b_k>0\). The maximizing gap is chosen in reverse \(k\)-order as observations are consumed, so \(h_i=-\log b_{n-i+1}\).

Adding an available observation strictly improves the value whenever it is below one: the objective has positive right derivative at \(h=0\), equal to \(r(1-b)\). Therefore \(0<b_1<b_2<\cdots<1\). Every Bellman maximizer is unique, so the full calendar is uniquely optimal. Since \(b_k\) increases, the gaps \(-\log b_{n-i+1}\) strictly increase with \(i\) whenever \(n>1\). The recurrence is continuous up to \(b=1\). If the increasing limit were below one the strict improvement at that limit would contradict the fixed-point equation, so \(b_k\uparrow1\).

**3. Exact rate-ratio example.** If \(r=2\), the recursion becomes \(b_k=(2-b_{k-1})^{-1}\), which inductively gives \(b_k=k/(k+1)\). The gap between observations \(i-1\) and \(i\) is therefore \(\mu^{-1}\log[(n-i+2)/(n-i+1)]\). Summing these gaps telescopes to the stated times.

**4. Asymptotic optimum.** Put \(\epsilon_k=1-b_k\). Taylor expansion of the exact recurrence, including the continuous case \(r=1\), gives

\[
\epsilon_{k+1}=\epsilon_k-\frac r2\epsilon_k^2+O_r(\epsilon_k^3).
\]

Since \(\epsilon_k\downarrow0\), it follows that \(\epsilon_{k+1}^{-1}-\epsilon_k^{-1}\to r/2\). Summing these differences and dividing by \(k\) yields \(k\epsilon_k\to2/r\). Consequently \(-\log b_k\sim2/(rk)\); summing the decreasing-index gaps shows \(t_n=(1/\mu)\sum_{k=1}^n(-\log b_k)\sim2\log n/\alpha\).

**5. Strict and asymptotically logarithmic cost of equal spacing.** With every dimensionless gap equal to \(h>0\), the detection probability is

\[
D_n^{\rm eq}(h)=H_r(h)(1-e^{-rnh}),\qquad
H_r(h)=\frac{g_r(h)}{1-e^{-rh}}.
\]

Here \(0<H_r(h)<1\) for every positive \(h\); indeed the numerator counts intervals arriving and surviving to the observation, a strict subset of intervals arriving during the gap. Direct expansion gives \(H_r(h)=1-h/2+O_r(h^2)\) as \(h\downarrow0\). The equal-grid miss probability can be written

\[
E_n(h)=[1-H_r(h)]+H_r(h)e^{-rnh}
=e^{-rnh}+[1-H_r(h)](1-e^{-rnh}).
\]

Choosing \(h=(\log n)/(rn)\) proves an upper bound \(\inf_{h>0}E_n(h)\le(1+o(1))(\log n)/(2rn)\). A minimizing gap exists because the detection probability tends to zero as \(h\downarrow0\) and as \(h\to\infty\). For any minimizing sequence \(h_n\), the upper bound forces \(h_n\to0\), because \(1-H_r(h)\) is bounded away from zero outside every neighborhood of zero. It also forces \(e^{-rnh_n}\le E_n(h_n)=O((\log n)/n)\), hence \(rnh_n\ge\log n-\log\log n-O_r(1)\). The expansion \(1-H_r(h_n)\sim h_n/2\) supplies the matching lower bound

\[
\inf_{h>0}E_n(h)\sim\frac{\log n}{2rn}.
\]

Because the globally optimal gaps are strictly increasing for \(n>1\), no equal-spaced calendar can be globally optimal for those sizes. Finally division by \(1-b_n\sim2/(rn)\) gives the logarithmic miss-probability factor \((\log n)/4\). This ratio is an asymptotic statement, not a finite-size lower bound.

## Verification

The standalone file `verify_timed_presence.py` is runnable with ordinary Python 3 and no third-party packages. Running `python verify_timed_presence.py` passes **9,032** checks of exact rational special cases, Bellman values, direct numerical quadrature of the arrival-survival event, numerical optimization, random calendars, and asymptotic diagnostics. The rational special case checks the closed formula over many observation counts. The analytical argument above, not the finite computation, establishes global optimality, uniqueness, and the limits for every admissible parameter.

## Relationship to prior work

Kendall, Hines, Nichols and Grant (2013) motivate non-closure within a season through staggered arrival and departure of animals. The publisher's article metadata and abstract were accessible, but the complete primary text was not; it therefore remains a specified priority risk. MacKenzie and Royle (2005) optimize occupancy-study allocation and statistical precision under conventional sampling assumptions. Guillera-Arroita, Hauser and McCarthy (2014) analyze continuous effort, occupied sites and management upon detection, rather than choosing times at which to intercept a single transient episode. Moore and McCarthy (2016) optimize allocations and visit counts under spatial and temporal variations in detection rates; their inspected full text does not imply the exact transient-episode recurrence or equal-grid loss. Yu, Karaman and Rus (2013) consider stochastic event arrivals and continuous robot monitoring at multiple stations with different optimization criteria. Classical inspection scheduling is conceptually related; the abstract of Parmigiani (1996), concerned with failure inspections, does not establish these claims.

A literature search and comparison of accessible related research did not identify a prior result implying the full statement. That is a best-knowledge comparison, not proof of first discovery or exhaustive coverage.

## Limitations

The model has one entry, one irreversible departure, exponential laws, perfect instantaneous detection, a single site, freely chosen finite observation times and a fixed number of visits. It does not cover imperfect detection, repeat colonization, multiple sites, travel/cost constraints, a hard calendar deadline, learned entry rates, or adaptive policy changes. Relative finite-size error bounds are not claimed by the displayed asymptotics. Priority is provisional because a plausible primary 2013 article and parts of broad inspection-scheduling literature were not available in full. Independent validation has not been performed.

## References

1. Kendall, W. L., Hines, J. E., Nichols, J. D., and Grant, E. H. C. (2013). *Relaxing the closure assumption in occupancy models: staggered arrival and departure times*. Ecology 94, 610–617. First available publication 2013-03-01. https://doi.org/10.1890/12-1720.1
2. MacKenzie, D. I. and Royle, J. A. (2005). *Designing efficient occupancy studies: general advice and tips on allocation of survey effort*. Journal of Applied Ecology 42, 1105–1114. https://doi.org/10.1111/j.1365-2664.2005.01098.x
3. Guillera-Arroita, G., Hauser, C. E., and McCarthy, M. A. (2014). *Optimal surveillance strategy for invasive species management when surveys stop after detection*. Ecology and Evolution 4, 1751–1760. https://doi.org/10.1002/ece3.1056
4. Moore, A. L. and McCarthy, M. A. (2016). *Optimizing ecological survey effort over space and time*. Methods in Ecology and Evolution 7, 891–899. https://doi.org/10.1111/2041-210X.12564
5. Yu, J., Karaman, S., and Rus, D. (2013). *Persistent Monitoring of Events with Stochastic Arrivals at Multiple Stations*. https://arxiv.org/abs/1309.6041
6. Parmigiani, G. (1996). *Optimal Scheduling of Fallible Inspections*. Operations Research 44, 360–367. https://doi.org/10.1287/opre.44.2.360
