# A sharp covariance-maximizing flowering-duration split invisible to one-time richness

## Finding

**Theorem.** Let an annual phase be a circle of circumference \(T>0\). Fix two flowering-season centers at geodesic distance \(d\) with \(0<d\le T/2\). Species \(i\) flowers on the closed circular arc of length \(\ell_i\), centered at its fixed center, where \(0<\ell_i<T\), with endpoints of measure zero. Keep the combined duration \(S=\ell_1+\ell_2\) fixed, and sample one phase \(U\) uniformly from the circle. Write \(X_i=\mathbf 1\{U\text{ lies in species }i\text{'s arc}\}\) and \(N=X_1+X_2\).

A choice of the two lengths with strictly positive \(\operatorname{Cov}(X_1,X_2)\) exists **if and only if**
\[
2d<S<2(T-d).
\]
In this precise feasibility band, covariance is globally maximized by exactly the two label-swapped assignments
\[
(\ell_1,\ell_2)=(S/2+d,S/2-d)\quad\text{or}\quad(S/2-d,S/2+d),
\]
with the sharp value
\[
C_{\max}=\frac{(S/2-d)(T-S/2-d)}{T^2}>0.
\]
The shorter flowering arc is contained in the longer, touching its endpoint at the maximum. No other split attains this maximum.

Moreover, throughout the same feasibility band, all splits with \(t=|\ell_1-\ell_2|/2\le d\) have an **identical complete distribution** of one-time richness:
\[
\Pr(N=0)=\frac{T-S/2-d}{T},\quad
\Pr(N=1)=\frac{2d}{T},\quad
\Pr(N=2)=\frac{S/2-d}{T}.
\]
Nevertheless their binary flowering covariance is \(\operatorname{Cov}(X_1,X_2)=C_{\mathrm{equal}}+t^2/T^2\), strictly increasing with nonnegative imbalance \(t\) until \(d\). The covariance advantage of the maximizing split over equal duration is exactly \(d^2/T^2\), independent of the total duration within the feasibility band.

**Exact sign-inversion witness.** With \(T=1\), \(d=3/10\) and \(S=1\), equal lengths \((1/2,1/2)\) yield covariance \(-1/20\); lengths \((4/5,1/5)\) yield covariance \(1/25\). In both cases the full one-time richness probability vector for counts \((0,1,2)\) is \((1/5,3/5,1/5)\).

## Assumptions and scope

The phase circle models a periodic annual calendar; the two species have fixed centers and contiguous, uniform binary flowering-activity arcs. Neither floral abundance, intensity, stochastic onset, pollinator behavior, nor nonuniform observation effort is represented. The same phase \(U\) is observed for both species. The statement concerns one-time richness under uniform phase sampling, not a longitudinal time series, and \(\operatorname{Cov}(X_1,X_2)\) is a purely temporal statistical association, not evidence of a biological interaction. Lengths are strictly between zero and one full period; endpoints have zero observation probability. Species labels may be exchanged; fixed centers do not move during length reallocation.

## Proof

Set \(u=S/2\) and \(t=|\ell_1-\ell_2|/2\). The lengths are \(u+t,u-t\); feasibility is \(0\le t<\min\{u,T-u\}\). If \(u\le d\), their half-lengths sum to at most the smaller circular center distance, so the arcs have zero intersection, and covariance is \(-\ell_1\ell_2/T^2<0\). If \(u\ge T-d\), the two *complementary* arcs have lengths \(T-\ell_1,T-\ell_2\) and combined half-length \(T-u\le d\); these complementary arcs are disjoint. Since \(\operatorname{Cov}(X_1,X_2)=\operatorname{Cov}(1-X_1,1-X_2)\), covariance then equals \(-(T-\ell_1)(T-\ell_2)/T^2<0\). This includes every case with \(d=T/2\), since there is no interior band.

Suppose henceforth \(d<u<T-d\). There is no intersection wrapping by the longer circular route of length \(T-d\). The intersection length \(H(t)\) is therefore
\[
H(t)=\begin{cases}
u-d,&0\le t\le d,\\
u-t,&d\le t<\min\{u,T-u\},\end{cases}
\]
Here \(u=S/2\). To verify the first case, the sum of arc half-lengths is \(u>d\), while their difference is \(t\le d\), so the direct overlap is exactly \(u-d\). To verify the second, \(t\ge d\) means the shorter arc is contained in the longer arc (the difference of their radii is at least the center distance), so the intersection equals the shorter length \(u-t\). The strict inequality \(u<T-d\) excludes any separate overlap along the opposite circular route.

By uniform phase sampling, \(\mathbb E X_i=\ell_i/T\) and \(\mathbb E(X_1X_2)=H(t)/T\). Hence
\[
C(t)=\operatorname{Cov}(X_1,X_2)=\begin{cases}
\displaystyle\frac{u-d}{T}-\frac{u^2-t^2}{T^2},&0\le t\le d,\\
\displaystyle\frac{(u-t)(T-u-t)}{T^2},&d\le t<\min\{u,T-u\}.
\end{cases}
\]
The first branch is strictly increasing for \(0<t\le d\); the second has derivative \(-(T-2t)/T^2<0\), because every feasible \(t\) is less than \(\min\{u,T-u\}\le T/2\). Therefore \(t=d\) is the unique global maximizing imbalance, with the displayed positive maximum. Outside the band strict negativity was already proved, giving the exact positive-covariance feasibility criterion.

On the plateau \(0\le t\le d\), the joint-flowering probability is \(H/T=(u-d)/T\). Since the sum of the two marginal probabilities is \(2u/T\), the one-time richness distribution is
\[
\Pr(N=2)=\frac{u-d}{T},\quad\Pr(N=1)=\frac{2u-2(u-d)}{T}=\frac{2d}{T},\quad\Pr(N=0)=1-\frac{2u}{T}+\frac{u-d}{T}=\frac{T-u-d}{T}.
\]
The formula for \(C(t)\) in this region yields \(C(t)-C(0)=t^2/T^2\); at \(t=d\), this is the universal sharp gain \(d^2/T^2\). In the exact witness, \(u=1/2\) and \(H=1/5\). For equal lengths the covariance is \(1/5-(1/2)^2=-1/20\); at the maximizing lengths it is \(1/5-(4/5)(1/5)=1/25\). The one-time richness law in either case follows from the preceding formula. This completes the proof.

## Verification

The standalone `checker.py` tests the overlap formula against direct geometric circular-interval intersections for 50,000 deterministic pseudorandom configurations, checks the global maximum and exact gain for 10,000 additional configurations, and verifies the rational sign-inversion witness using exact fractions. These are supplementary checks; the continuous-parameter claims are established by the proof, not inferred from finite testing. Run with `python3 checker.py` in the extracted package directory.

## Relationship to prior work

Austin et al. (2024) studied increasing flowering durations, empirical phenological reassembly, and co-flowering richness; their overlap statistic is a proportion of the focal species' interval overlapped by another. Albor et al. (2020) studied overlap-weighted co-flowering networks using Schoener's index; Stemkovski et al. (2022) studied effects of distributional skewness on temporal overlap; Rafferty et al. (2013) reviewed phenological overlap methods. These results motivate the flowering interval model and demonstrate the importance of measuring overlap, but the materials inspected did not supply the present exact **fixed-total-duration, one-time-richness-equivalence and covariance-maximization** theorem. Geometric arc-intersection formulas, elementary Bernoulli covariance, and the Fréchet nesting bound are standard antecedents and are not claimed as new. The contribution claimed is their constrained, complete ecological association classification and the identical-richness / opposite-covariance construction.

## Limitations

The circular annual boundary and equal within-interval flowering activity are idealizations; real phenological distributions can be skewed, abundances time-varying, and observations nonuniform. The uniform one-time count law does not characterize the full time-indexed count process or species-resolved dates. Fixed total duration is a mathematical budget, not necessarily a controllable ecological intervention. Neither the sign of temporal covariance nor this model demonstrates facilitation or competition. The novelty comparison is limited to the inspected literature and indexed scientific records, not every historical article; independent external validation has not been performed.

## References

1. Austin, M. W., et al. (2024). *Climate change increases flowering duration, driving phenological reassembly and elevated co-flowering richness*. New Phytologist. DOI: 10.1111/nph.19994. First publicly posted 2024-07-24.
2. Albor, C., Arceo-Gómez, G., and Parra-Tabla, V. (2020). *Integrating floral trait and flowering time distribution patterns help reveal a more dynamic nature of co-flowering community assembly processes*. Journal of Ecology. DOI: 10.1111/1365-2745.13486.
3. Stemkovski, M., et al. (2022). *Skewness in bee and flower phenological distributions*. Ecology. DOI: 10.1002/ecy.3890.
4. Rafferty, N. E., et al. (2013). *Phenological overlap of interacting species in a changing climate: an assessment of available approaches*. Ecology and Evolution. DOI: 10.1002/ece3.668.
