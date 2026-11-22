# Sharp cooperative-consumption threshold for reentrant oxygen loss under vertical mixing

## Finding
Consider a fixed, oxygenated surface reservoir and a deep layer whose vertical exchange both replenishes oxygen and, phenomenologically, stimulates a saturating biological oxygen demand. Define the dimensionless amplitude ratio \(q=r_1/r_0\) and cooperative response exponent \(p>0\). The steady deep-water oxygen concentration is strictly increasing with mixing intensity for all \(0<p\leq 1\), and also for \(p>1\) when
\[
q\leq q_{\mathrm c}(p)=\frac{4p}{(p-1)^2}.
\]
For \(p>1\) and \(q>q_{\mathrm c}(p)\), it instead has **exactly two** positive mixing-rate turning points: a strict local maximum followed by a strict local minimum, and nowhere else changes monotonicity. Explicit formulas for both locations are given below. Any oxygen threshold strictly between those extrema has **exactly three** positive mixing-rate crossings, provided such a threshold is selected in the physical positive-oxygen range. At the critical ratio there is one stationary tangent, not a pair of extrema. The two turning rates separate at square-root order and their concentration gap opens at three-halves order above the transition.

## Assumptions and scope
Let \(C_s,r_0,r_1,K,p\) be strictly positive real parameters. For each externally selected mixing rate \(k>0\), define the linear deep-layer concentration equation
\[
\dot C=k(C_s-C)-r(k),\qquad
r(k)=r_0+r_1\frac{(k/K)^p}{1+(k/K)^p}.
\]
Here \(C_s\) is a **fixed** upper-layer oxygen concentration, \(r_0\) is baseline consumption, \(r_1\) is the incremental capacity for oxygen demand driven by mixing-associated organic-material supply, and \(K\) is a characteristic mixing intensity. This Hill-family law is an *assumption*, not a fit to an observed data set. The dynamics treat oxygen consumption as independent of oxygen concentration; physical interpretation therefore applies only where the predicted deep-layer concentration is positive.

For any real initial condition the unique solution converges exponentially to
\[
C_*(k)=C_s-\frac{r_0}{k}\left[1+q\frac{(k/K)^p}{1+(k/K)^p}\right],\qquad q=\frac{r_1}{r_0}.
\]
No claim is made about a time-dependent mixed-layer oxygen reservoir, transport delays, nonlinear feedback of oxygen availability on respiration, species distributions, or empirical parameter values. The object of this finding is the **global mixing-rate response of this exactly stated model**, not a general theorem for all oxygen-budget systems.

## Proof
Set \(x=k/K>0\) and \(z=x^p>0\). Write
\[
C_*(Kx)=C_s-\frac{r_0}{K}\left[\frac1x+q\frac{x^{p-1}}{1+x^p}\right].
\]
Direct differentiation (with respect to \(x\)) yields the exact sign factorization
\[
\frac{K}{r_0}\frac{\mathrm d C_*(Kx)}{\mathrm d x}
=\frac{Q(z)}{x^2(1+z)^2},\quad
Q(z)=(q+1)z^2+[2-q(p-1)]z+1.
\]
The denominator is strictly positive. If \(0<p\leq1\), all coefficients of \(Q\) are positive. If \(p>1\), its discriminant is
\[
\Delta=q\bigl(q(p-1)^2-4p\bigr).
\]
For \(0<q<4p/(p-1)^2\) the quadratic is strictly positive on \(z>0\). At equality, it has a single positive double root
\[
z_0=\frac{p-1}{p+1};
\]
its derivative vanishes at one \(x>0\) only, with no change of sign; hence \(C_*\) is still strictly increasing. For \(q>4p/(p-1)^2\), the roots are
\[
z_{\pm}=\frac{q(p-1)-2\pm\sqrt{q\{q(p-1)^2-4p\}}}{2(q+1)}.
\]
Both roots are strictly positive, distinct, and smaller than \(p-1\). Indeed the quadratic is positive at \(z=0\) and \(z=p-1\), negative at its interior vertex under the stated inequality, and both roots are positive because \(q(p-1)>2\). Thus \(Q\) is positive before \(z_-\), negative between the roots, and positive after \(z_+\). Exactly two critical mixing rates exist:
\[
k_-=K z_-^{1/p},\qquad k_+=K z_+^{1/p},\qquad 0<k_-<k_+.
\]
The sign sequence for \(C_*'(k)\) is positive, negative, positive, establishing the complete classification.

Moreover \(C_*(k)\to-\infty\) as \(k\downarrow0\), and \(C_*(k)\uparrow C_s\) as \(k\to\infty\) (the latter limit is from below, because consumption is positive). Define \(C_{\max}=C_*(k_-)\) and \(C_{\min}=C_*(k_+)\). Then \(C_{\min}<C_{\max}<C_s\). By continuity and strict monotonicity on each of the three intervals, every \(\theta\in(C_{\min},C_{\max})\) has exactly three positive solutions of \(C_*(k)=\theta\). Conversely, a level outside this open interval cannot have three positive solutions, because no more than one solution lies on each monotonicity interval; at either endpoint there is one tangent and one simple solution. More precisely, in the two-turning-point case the root counts for \(C_*(k)=\theta\) are one for \(\theta<C_{\min}\), two for \(\theta=C_{\min}\), three for \(C_{\min}<\theta<C_{\max}\), two for \(\theta=C_{\max}\), one for \(C_{\max}<\theta<C_s\), and zero for \(\theta\ge C_s\). In the monotonically increasing cases there is one root for \(\theta<C_s\) and none for \(\theta\ge C_s\). The physically useful three-crossing regime is obtained, for example, when \(C_{\min}>0\) and \(\theta\in(C_{\min},C_{\max})\).

Finally fix \(p>1\) and put \(q=q_{\mathrm c}(p)+\varepsilon\) with \(\varepsilon\downarrow0\). The root formula and smoothness of \(z\mapsto z^{1/p}\) at \(z_0>0\) give
\[
\frac{k_+-k_-}{K\sqrt\varepsilon}\longrightarrow
\frac{2(p-1)^2}{\sqrt p\,(p+1)^2}
\left(\frac{p-1}{p+1}\right)^{1/p-1}>0.
\]
Between the two roots, \(-Q(z)=(q+1)(z-z_-)(z_+-z)\). Integrating the positive quantity \(-\mathrm d C_*/\mathrm d k\) over \([k_-,k_+]\) and using the smooth positive nonvanishing denominator near \(z_0\) proves \(C_{\max}-C_{\min}=\Theta(\varepsilon^{3/2})\). These asymptotics are local in the fixed exponent \(p\); no uniformity as \(p\downarrow1\) is asserted.

## Verification
The standalone Python 3 script `verify.py` (standard library only) numerically checks the exact derivative identity, critical and supercritical sign patterns, turning locations, splitting coefficient, and three-crossing example. Run `python3 verify.py`. A successful run prints `CHECKS_PASSED 21781`. These floating-point tests **supplement** the preceding proof; they are not a numerical substitute for its universally quantified claims.

For a dimensionless example, take \(p=2\), \(q=12\), \(r_0=K=1\), \(C_s=10\). The local oxygen maximum and minimum occur at \(k_-\approx0.3437237693\) and \(k_+\approx0.8068982214\), with oxygen concentrations \(C_{\max}\approx3.4018261326\) and \(C_{\min}\approx2.8961910488\). A strictly positive threshold \(\theta=3.1\) is crossed at precisely three positive roots, approximately \(0.2386124868\), \(0.5591007603\), and \(1.0863447239\). This example remains positive in the entire interval between its two extrema.

## Relationship to prior work
Williams et al. investigated vertical oxygen replenishment by turbulence in the central North Sea and explicitly distinguished oxygen transport from organic-matter supply that can stimulate deep biological consumption. Their 2024 article page reports that its public discussion began on June 26, 2023. Rippeth et al. (2024) similarly measured the dependence of oxygen fluxes on mixing and water-column structure. Große et al. (2016) studied physical/biological drivers of North Sea oxygen deficits using a large ecosystem model. Daewel et al. (2022) simulated wind-wake effects on productivity and deep oxygen.

Those studies motivate the competing channels but do not, in the materials inspected, state the present exact Hill-response condition, its two critical rates, and its three-crossing classification. Hill response functions and their biophysical interpretation are established tools (see Martinez-Corral et al., 2024); originality is claimed only for the **specific complete steady mixing/consumption phase diagram** in the explicitly defined model, and historical priority is not guaranteed.

## Limitations
The fixed surface concentration, constant baseline consumption, cooperative Hill-shaped incremental demand, instantaneous response, steady-state comparison, and one well-mixed deep compartment are idealizations. No empirical source establishes the Hill exponent or amplitude ratio for the studied shelf sea, so the sharp threshold is conditional rather than an observed tipping point. When the formula yields negative oxygen, the prescribed oxygen-independent consumption law is physically invalid; the positive-equilibrium regime is the proper domain for ecological interpretation. No robustness to more general consumption curves, finite oxygen inventory, oxygen-dependent respiration or transient forcing is proved. No independent external mathematical review has been conducted.

## References
1. Williams, C. A. J., et al. "Vertical mixing alleviates autumnal oxygen deficiency in the central North Sea." *Biogeosciences* 21 (2024), 1961–1971. Public discussion began 2023-06-26; article published 2024-04-17. https://doi.org/10.5194/bg-21-1961-2024 . Full accessible article: https://bg.copernicus.org/articles/21/1961/2024/bg-21-1961-2024.html .
2. Rippeth, T. P., et al. "The deepwater oxygen deficit in stratified shallow seas is mediated by diapycnal mixing." *Nature Communications* 15 (2024), 3136, published 2024-04-11. https://doi.org/10.1038/s41467-024-47548-2 .
3. Große, F., et al. "Looking beyond stratification: a model-based analysis of the biological drivers of oxygen deficiency in the North Sea." *Biogeosciences* 13 (2016), 2511–2535. https://doi.org/10.5194/bg-13-2511-2016 .
4. Daewel, U., et al. "Offshore wind farms are projected to impact primary production and bottom water deoxygenation in the North Sea." *Communications Earth & Environment* 3 (2022), 292. https://doi.org/10.1038/s43247-022-00625-0 .
5. Martinez-Corral, R., et al. "The Hill function is the universal Hopfield barrier for sharpness of input–output responses." *Proceedings of the National Academy of Sciences* 121 (2024), e2318329121. First public preprint 2024-03-28. https://doi.org/10.1073/pnas.2318329121 .
