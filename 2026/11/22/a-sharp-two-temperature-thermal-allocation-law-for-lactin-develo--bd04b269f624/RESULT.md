# A sharp two-temperature thermal-allocation law for Lactin development

## Finding

In the Lactin-2 exponential development-rate family, an arbitrary temperature history with a fixed mean and two hard thermal bounds has a **unique optimal temperature distribution**. There is a sharp transition between an extremal two-temperature schedule and a constant-temperature schedule. The hotter temperature in the mixed optimum is determined by the *lower* bound alone: increasing the allowable upper temperature beyond that contact value cannot improve the optimum. When the lower bound approaches the unique inflection temperature from below, the optimal performance gain opens cubically, with an explicit universal coefficient.

Write
\[
 r(T)=e^{aT}-B e^{bT}+\lambda,
 \qquad 0<a<b,\quad B>0,\quad \lambda\in\mathbb R.
\]
Define the unique inflection and peak temperatures
\[
 \theta=\frac{\log(a^2/(B b^2))}{b-a},\qquad
 T_p=\frac{\log(a/(B b))}{b-a},\qquad
 \theta<T_p.
\]
For any lower bound \(L<\theta\), there is exactly one contact temperature \(\tau_L\in(\theta,T_p)\) solving
\[
 (\tau_L-L)r'(\tau_L)=r(\tau_L)-r(L).
\]
The contact moves strictly down as the cold bound rises. Let \(U>L\) be the permitted warm bound and \(m\in[L,U]\) the prescribed mean.

If \(L\ge\theta\), the unique optimal law is constant at \(m\). If \(L<\theta\) and \(U\le\tau_L\), the unique optimal law uses exactly \(L\) and \(U\), with upper-temperature weight \((m-L)/(U-L)\) (degenerating to one point when \(m\) is an endpoint). If \(L<\theta<U\) and \(U>\tau_L\), the unique optimal law uses \(L\) and \(\tau_L\) for \(L<m<\tau_L\), with weight \((m-L)/(\tau_L-L)\) at \(\tau_L\), and is constant at \(m\) for \(\tau_L\le m\le U\). No other probability law, continuous or discrete, attains the same expected rate except these specified degeneracies.

In the last case the optimal gain over the constant-mean schedule is positive precisely for \(L<m<\tau_L\). It has exactly one maximum at the unique \(v_L\in(L,\theta)\) satisfying \(r'(v_L)=r'(\tau_L)\). If \(h=\theta-L\downarrow0\) while the warm bound remains strictly above \(\theta\), then
\[
 \tau_L=\theta+\frac h2+O(h^2),\qquad
 v_L=\theta-\frac h2+O(h^2),
\]
and the *maximum* gain obeys the sharp law
\[
 \max_{m\in[L,U]}\bigl\{\sup_{\mu:\,\mathbb E_\mu[T]=m}\mathbb E_\mu[r(T)]-r(m)\bigr\}
 =\frac{a^2(b-a)e^{a\theta}}{12}h^3+O(h^4).
\]
This last maximum statement is taken for fixed \(U>\theta\) and sufficiently small \(h\). The coefficient is strictly positive, and the intercept \(\lambda\) has no effect on any optimizer or on the gain.

## Assumptions and scope

The admissible ambient-temperature laws are all Borel probability measures \(\mu\) supported on the closed interval \([L,U]\), where \(L<U\), having prescribed mean \(\int T\,d\mu(T)=m\). For biological interpretation, require \(r(T)>0\) throughout \([L,U]\); the mathematical inequalities themselves do not need this positivity. The objective is the rate-summation quantity \(\int r(T)\,d\mu(T)\). A measurable temperature history realizing each probability law in its long-run time fractions is allowed, including instantaneous switches, with no rate-limiting thermal inertia or switching cost. Chronological ordering does not enter the rate-summation objective.

The rate is the Lactin-2 model of Lactin et al. (1995) under the identification \(a=\rho\), \(b=1/\Delta\), and \(B=\exp((a-b)T_u)\). The restrictions \(0<a<b\) select the common increasing-then-inhibited thermal-response regime. Any empirical claim concerning animal thermoregulation or survival requires separate evidence; the result treats idealized developmental progress over a fixed observation window, not completion-time stochasticity, acclimation, thermal stress, or optimal climate engineering.

## Proof

**1. Single change of curvature.** Differentiating shows
\[
 r''(T)=a^2e^{aT}-Bb^2e^{bT},\qquad
 r'''(\theta)=-a^2(b-a)e^{a\theta}<0.
\]
Consequently \(r\) is strictly convex below \(\theta\) and strictly concave above \(\theta\). It is increasing up to its unique maximum at \(T_p>\theta\) and decreasing afterwards. In particular, when \(L\ge\theta\), strict Jensen inequality directly gives the constant-mean optimizer, uniquely.

**2. Unique supporting contact.** For \(L<\theta\), define
\[
 H_L(t)=(t-L)r'(t)-[r(t)-r(L)].
\]
The identities \(H_L(L)=0\), \(H'_L(t)=(t-L)r''(t)\), \(H_L(\theta)>0\), and
\(H_L(T_p)=r(L)-r(T_p)<0\) show that \(H_L\) first increases strictly and then decreases strictly, crossing zero just once at \(\tau_L\in(\theta,T_p)\). Moreover, for \(t>L\),
\[
 \frac{d}{dt}\frac{r(t)-r(L)}{t-L}=\frac{H_L(t)}{(t-L)^2}.
\]
Thus the chord slope from \(L\) increases strictly up to \(\tau_L\), then decreases strictly. At the contact the chord from \(L\) is tangent to \(r\). The contact is independent of \(U\), \(m\), and \(\lambda\).

**3. Exact concave envelope.** If \(U\le\tau_L\), the chord from \((L,r(L))\) to \((U,r(U))\) strictly exceeds \(r\) at every interior point: the strict increase of the chord slope proves this directly. The chord is therefore the least concave majorant on \([L,U]\). If \(U>\tau_L\), let \(\ell\) be the chord from \((L,r(L))\) to \((\tau_L,r(\tau_L))\). The function equal to \(\ell\) on \([L,\tau_L]\) and to \(r\) on \([\tau_L,U]\) is a concave majorant: strict chord-slope increase proves \(\ell>r\) inside the first interval, strict concavity applies on the second, and derivatives agree at the contact. Any concave majorant must lie above the chord between its own endpoint values, so this majorant is the least one. It has one linear piece followed by a strictly concave piece.

For every admissible \(\mu\), the two inequalities \(\int r\,d\mu\le\int \operatorname{cav}r\,d\mu\le\operatorname{cav}r(m)\) establish the upper bound. In each piece the asserted one- or two-atom law attains equality. Strict inequality between \(r\) and its chord except at contact points, followed by the strict-Jensen equality criterion on the non-linear piece, proves uniqueness in every regime. This includes exactly the transition \(U=\tau_L\), the mean \(m=\tau_L\), and both endpoint means.

**4. Contact monotonicity.** The strict slope maximum implies \(r'(L)<r'(\tau_L)<r'(\theta)\). Implicit differentiation in the contact equation yields
\[
 \frac{d\tau_L}{dL}
 =\frac{r'(\tau_L)-r'(L)}{(\tau_L-L)r''(\tau_L)}<0.
\]

**5. Cubic gain onset.** Suppose \(L=\theta-h\) with \(h\downarrow0\) and fixed \(U>\theta\). Taylor expansion of \(H_L(\theta+kh)=0\) at the nonzero third derivative gives, to leading order, \(2k^2+k-1=0\). The admissible root is \(k=1/2\); smoothness yields \(\tau_L=\theta+h/2+O(h^2)\). The chord-minus-rate gain \(g_L(m)=\ell(m)-r(m)\), for \(m\in[L,\tau_L]\), has derivative \(r'(\tau_L)-r'(m)\). Since \(r'\) increases below \(\theta\), decreases above it, and \(r'(L)<r'(\tau_L)<r'(\theta)\), this gain has one strict interior maximum at \(v_L\in(L,\theta)\), and the Taylor expansion of \(r'\) gives \(v_L=\theta-h/2+O(h^2)\). At \(m=\theta+sh\) with fixed \(-1<s<1/2\), direct cubic expansion of the tangent chord yields
\[
 g_L(m)=\frac{-r'''(\theta)}{6}h^3(s+1)(s-1/2)^2+O(h^4).
\]
This cubic profile has its unique positive maximum at \(s=-1/2\), with value \(-r'''(\theta)h^3/12+O(h^4)\). Substituting the exact third derivative from step 1 gives the stated coefficient. For \(m\ge\tau_L\), the gain is zero. These are asymptotic equalities, not estimates obtained solely from finite sampling.

## Verification

The standalone `CHECK.py` uses only the Python standard library, a fixed pseudorandom seed, and 100-step interval bisection. It passed **85,188 deterministic diagnostic assertions** covering positive and negative curvature regions, strict contact location, the exact tangency residual, domination by the predicted upper envelope over sampled temperatures, comparisons against randomized two-temperature feasible mixtures, admissible positive rates in an example, contact monotonicity, and the sharp cubic gain coefficient. Such sampling does not prove a continuum theorem; the proof above is the certificate for all real parameters in scope.

For an independently reproducible illustration, take \(a=0.1\), \(b=0.2\), \(B=e^{-2}/4\), \(\lambda=0\), \(L=15\), and \(U=31\). The rate is positive on the whole interval because \(B e^{bT}/e^{aT}=e^{(T-20)/10}/4\le e^{11/10}/4<1\); \(\theta=20\), \(T_p\approx26.931472\), and \(\tau_L\approx21.943678\). At mean \(m=20\), the optimum alternates between \(15\) and \(\tau_L\), giving \(\mathbb E[r(T)]\approx5.564356\), versus \(r(20)\approx5.541792\) under constant temperature. These rates are mathematical model units, not fitted field observations.

To reproduce, run `python3 CHECK.py` from the directory containing that file. The script exits nonzero if a diagnostic assertion fails.

## Relationship to prior work

Lactin, Holliday, Johnson, and Craigen (1995) introduced the revised double-exponential temperature-development curve and its intercept; the original full paper was not available during this comparison, but the published abstract and independent implementation documentation confirm the functional form. Ruel and Ayres (1999), inspected in their full six-page article, explicitly discuss temperature-dependent insect developmental rates that accelerate at cool temperatures and decelerate at hot temperatures, including qualitative consequences of Jensen's inequality. Martin and Huey (2008), inspected in full text, optimize the mean of a **pre-specified family** of body-temperature distributions, using numerical experiments, whereas the present result optimizes over **all** laws with a fixed mean and interval bounds. Denny (2019) analyzes averaging over given temperature variation; von Schmalensee and colleagues (2021) assess rate summation against observed fluctuating microclimates; and Rebaudo and Rabhi (2018) review insect thermal-development curves. None of the materially inspected texts states this exact Lactin family upper-concave-envelope transition, unique contact, warm-bound invariance, or sharp cubic gain onset.

The general concave-envelope method and Jensen's inequality are classical and are **not** claimed as new. The asserted contribution is the complete strict parameter/boundary classification and onset coefficient for this named ecological rate law. This statement is an evidence-based priority comparison, not an assertion that a literature search proves uniqueness.

## Limitations

The original Lactin et al. (1995) article's full text remained inaccessible after lawful open-access and arXiv attempts, and the institutional full-text route reported disconnected access. A covered formulation in an uninspected source remains a residual historical-priority risk. Only the empirical model, not a calibrated individual species, is analyzed. Optimizing rate summation is not equivalent to maximizing survival, realized time to maturity, or net fitness when temperature alters mortality, plasticity, maturation thresholds, costs, or carrying capacity. Instantaneous switches and any arbitrary probability law are idealized admissibility assumptions. The conclusion does not justify real-world thermal intervention without validation.

## References

1. Lactin, D. J., Holliday, N. J., Johnson, D. L., and Craigen, R. (1995). “Improved Rate Model of Temperature-Dependent Development by Arthropods.” *Environmental Entomology* 24, 68–75. https://doi.org/10.1093/ee/24.1.68 (first public source date 1995-02-01; primary motivating rate family).
2. `rTPC` reference manual, “Lactin2 model for fitting thermal performance curves.” https://search.r-project.org/CRAN/refmans/rTPC/html/lactin2_1995.html (model equation confirmation).
3. Ruel, J. J., and Ayres, M. P. (1999). “Jensen's Inequality Predicts Effects of Environmental Variation.” *Trends in Ecology & Evolution* 14, 361–366. https://doi.org/10.1016/S0169-5347(99)01664-X ; lawful full text https://research.fs.usda.gov/download/treesearch/1948.pdf .
4. Martin, T. L., and Huey, R. B. (2008). “Why ‘Suboptimal’ Is Optimal: Jensen's Inequality and Ectotherm Thermal Preferences.” *The American Naturalist* 171, E102–E118. https://doi.org/10.1086/527502 .
5. Rebaudo, F., and Rabhi, V.-B. (2018). “Modeling temperature-dependent development rate and phenology in insects: review of major developments, challenges, and future directions.” *Entomologia Experimentalis et Applicata* 166, 607–617. https://doi.org/10.1111/eea.12693 .
6. Denny, M. (2019). “Performance in a variable world: using Jensen's inequality to scale up from individuals to populations.” *Conservation Physiology* 7, coz053. https://doi.org/10.1093/conphys/coz053 .
7. von Schmalensee, L., et al. (2021). “Thermal performance under constant temperatures can accurately predict insect development times across naturally variable microclimates.” *Ecology Letters* 24, 1633–1645. https://doi.org/10.1111/ele.13779 .
