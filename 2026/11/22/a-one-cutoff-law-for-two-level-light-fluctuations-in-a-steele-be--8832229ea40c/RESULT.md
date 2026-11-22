# A one-cutoff law for two-level light fluctuations in a Steele–Beer water column

## Finding

For any two strictly positive, distinct surface irradiance levels and any nonzero duty fraction, the *instantaneous Steele photosynthesis model*, averaged over a uniformly populated Beer-attenuating water column, has a **sharp one-cutoff law** for the benefit of fluctuations. As optical depth increases, averaging production at the two surface levels can change from exceeding production at their fixed weighted mean to falling below it **at most once**, and only in that direction. An exact test, using the light levels and duty fraction alone, tells whether such a positive optical-depth crossover exists. If it does, the crossover is unique. Otherwise fluctuations reduce the modeled depth-mean production at every positive optical depth.

More precisely, let \(0<p<1\), \(d>0\), \(m>(1-p)d\), \(q=1-p\), and let the normalized lower and upper surface irradiances be \(x=m-qd>0\) and \(y=m+pd>x\). The lower level occupies fraction \(p\) of the time and the upper occupies fraction \(q\), so their mean is \(m\). Set

\[
J_p(z)=p e^{qz}+q e^{-pz}-1\quad(z>0),\qquad
m_0(p,d)=\frac{dJ'_p(d)}{J_p(d)}.
\]

For **every** positive optical depth \(h\), define the dimensionless time-and-depth averaged gain \(G(h)=pM_x(h)+qM_y(h)-M_m(h)\), with \(M\) defined below. Then:

1. If \(m\le m_0(p,d)\), \(G(h)<0\) for every \(h>0\).
2. If \(m>m_0(p,d)\), there is exactly one \(h_c>0\), with \(G(h)>0\) for \(0<h<h_c\), \(G(h_c)=0\), and \(G(h)<0\) for \(h>h_c\).
3. For each \(h>0\), the exact condition is \(G(h)>0\) if and only if

\[
m>\frac{\log J_p(d)-\log J_p(de^{-h})}{1-e^{-h}}.
\]

The test includes all strict and equality cases; for fixed \(p,d\) the threshold \(m_0(p,d)\) exceeds the positivity boundary \((1-p)d\). For fixed \(p,d\) and \(m\to\infty\) the unique cutoff satisfies the **sharp high-light scale**

\[
h_c=\frac m2-\frac12\log\!\left(\frac{2J_p(d)}{p(1-p)d^2}\right)+o(1).
\]

For equal-duration symmetric levels \(m-\delta,m+\delta\), \(m>\delta>0\), the onset threshold simplifies to

\[
m_0=\delta\coth(\delta/2),\qquad
m_c(h,\delta)=\frac{2}{1-e^{-h}}\log\!\left(\frac{\sinh(\delta/2)}{\sinh(\delta e^{-h}/2)}\right).
\]

Here \(G(h)>0\) precisely when \(m>m_c(h,\delta)\). As \(m\downarrow\delta\coth(\delta/2)\) from above,

\[
h_c=\frac{4\sinh^2(\delta/2)}{\delta^2}\left[m-\delta\coth(\delta/2)\right]+O\!\left(\left[m-\delta\coth(\delta/2)\right]^2\right).
\]

## Assumptions and scope

The physiological optimum is a fixed \(I_*>0\), the fixed maximum rate is \(P_{\max}>0\), and irradiance \(s\) is normalized by \(I_*\). The local *instantaneous* Steele gross-production response is \(P(I)=P_{\max}(I/I_*)\exp(1-I/I_*)\), for positive \(I\). Incident irradiance at physical depth \(z\in[0,L]\) is \(sI_*e^{-kz}\); the optical depth is \(h=kL>0\). Biomass is uniform and stationary with depth; \(k,L,P_{\max},I_*\), all biochemical parameters and the duty fraction are held fixed in every comparison. Time averaging uses the quasi-static or slow-fluctuation limit: production is the weighted average of *instantaneous* responses at the two light levels. No time-dependent physiological acclimation, respiration, spectral modification, chlorophyll change, or light-mixing memory is modeled. The dimensionless uniform-depth mean is

\[
M_s(h)=\frac1{LP_{\max}}\int_0^L P(sI_*e^{-kz})\,dz
=\frac e h\left(e^{-s e^{-h}}-e^{-s}\right),\quad h>0,
\]

with continuous extension \(M_s(0)=s e^{1-s}\). All probability weights, light levels, depth ranges, and equality conventions above are exact; no noise or parameter uncertainty is included.

## Proof

**1. Reduce the gain to a Laplace Jensen gap.** The indicated depth integral follows by the substitution \(u=s e^{-kz}\). Put \(a=e^{-h}\in(0,1)\), and let

\[
D(t)=p e^{-xt}+q e^{-yt}-e^{-mt}=e^{-mt}J_p(dt),\quad t\ge0.
\]

By strict convexity of the exponential, \(D(t)>0\) for every \(t>0\), while \(D(0)=D'(0)=0\) and \(D''(0)=pq(y-x)^2=pqd^2>0\). Since \(x>0\), \(D(t)\to0\) as \(t\to\infty\). Direct substitution gives

\[
G(h)=\frac e h[D(e^{-h})-D(1)].
\]

**2. Prove strict unimodality of \(D\) from a three-exponential zero bound.** The derivative is

\[
D'(t)=-pxe^{-xt}-qye^{-yt}+me^{-mt}.
\]

Multiplication by \(e^{xt}>0\) yields \(-px+me^{-(m-x)t}-qy e^{-(y-x)t}\). Its derivative is a combination of only two distinct exponentials and therefore has at most one real zero: their ratio is strictly monotone. Rolle's theorem implies the multiplied \(D'\) has at most two distinct real zeros. One is \(t=0\); it is simple with positive derivative \(D''(0)=pqd^2\). At large \(t\) the multiplied derivative tends to \(-px<0\). The intermediate value theorem therefore forces **exactly one** additional zero \(t_*\in(0,\infty)\), positive derivative sign on \((0,t_*)\), and negative derivative sign on \((t_*,\infty)\). Thus \(D\) is strictly increasing up to one unique maximum and strictly decreasing afterward. This argument is not a numerical zero count.

**3. Establish the complete cutoff and equality cases.** If \(D'(1)\ge0\), then \(t_*\ge1\), so \(D(a)<D(1)\) for every \(0<a<1\). If \(D'(1)<0\), then \(t_*<1\); \(D(a)>D(1)\) just below \(a=1\), while \(D(0)=0<D(1)\). Strict increase on \((0,t_*)\) gives exactly one \(a_c\in(0,t_*)\) with \(D(a_c)=D(1)\). On \((a_c,1)\) the difference is strictly positive, on \((0,a_c)\) strictly negative. Since \(a=e^{-h}\) decreases strictly with \(h\), the unique optical depth is \(h_c=-\log a_c\). At \(h=h_c\) equality holds, and no other positive equality is possible.

Because \(D'(1)=e^{-m}[dJ'_p(d)-mJ_p(d)]\) with \(J_p(d)>0\), the supercritical condition is precisely \(m>m_0(p,d)\). The derivative identity

\[
\frac{J'_p(d)}{J_p(d)}-q=\frac{q(1-e^{-pd})}{J_p(d)}>0
\]

proves \(m_0(p,d)>qd\). Finally \(D(a)>D(1)\) is equivalent, upon taking the positive \(J_p\) logarithms, to the exact finite-\(h\) inequality in the Finding section.

**4. Equal-duration special case.** Set \(p=q=1/2\) and \(d=2\delta\). Then \(J_{1/2}(2\delta t)=\cosh(\delta t)-1=2\sinh^2(\delta t/2)\), yielding the two displayed threshold formulas. Expand the exact secant formula at \(a=e^{-h}=1-h+O(h^2)\):

\[
m_c(h,\delta)=\delta\coth(\delta/2)
+\frac{\delta^2}{4\sinh^2(\delta/2)}h+O(h^2).
\]

The positive linear coefficient and the implicit-function theorem give the stated near-onset expansion for \(h_c\).

**5. High-light cutoff.** Fix \(p,d\) and let \(m\to\infty\). The unique critical point \(t_*\) of \(D\) satisfies \(m=dJ'_p(dt_*)/J_p(dt_*)\). The Taylor identities \(J_p(z)=pqz^2/2+O(z^3)\) and \(J'_p(z)=pqz+O(z^2)\) imply \(t_*=2/m+O(m^{-2})\) (uniqueness also prevents a nonzero limiting critical point). Since \(0<a_c<t_*\), we have \(a_c=O(m^{-1})\). The crossing equation becomes

\[
e^{-ma_c}J_p(da_c)=e^{-m}J_p(d).
\]

On \(0<a_c<t_*\), the factor \(e^{-ma_c}\) is uniformly bounded below by a positive constant for large \(m\), and \(J_p(da_c)\) is bounded below by a positive constant times \(a_c^2\). Hence \(a_c=O(e^{-m/2})\), so \(ma_c\to0\), and the crossing equation refines to

\[
a_c=\left(\frac{2J_p(d)}{pqd^2}\right)^{1/2}e^{-m/2}(1+o(1)).
\]

Taking negative logarithms gives the displayed asymptotic formula. This completes the exact theorem.

## Verification

The included standard-library program `verify.py` independently compares the depth-integral formula with composite Simpson quadrature, tests algebraic finite-depth thresholds for deterministic randomized physically admissible parameters, checks both sides of hundreds of numerically isolated crossings, and tests symmetric formulas and the large-mean expansion. Run `python verify.py`. It reports 10,510 successful diagnostic assertions on the specified deterministic seed. These finite tests are supplementary and do not establish the infinite-domain theorem.

For the balanced example \(p=1/2\), \(\delta=1\), \(m=3\), the exact surface-limit threshold is \(\coth(1/2)=2.163953413738653\ldots\) and the unique positive optical-depth crossover is \(h_c\approx0.7794130637455141\). For \(p=0.3\), \(d=2\), \(m=3\), the crossover is \(h_c\approx0.5396594205107994\). The units are multiples of the physiological optimum irradiance and the optical depth \(kL\), respectively.

## Relationship to prior work

Steele (1962) provided the instantaneous photoinhibited irradiance curve **and** an explicit time average for triangular diurnal illumination; Bannister (1974, especially the depth-integral production equation) integrated its exponential kernel and allowed arbitrary time profiles in a daily production integral. These equations and the instantaneous/depth-averaged production formula are **not** claimed as new. Thornley (1974) studied time-dependent responses to fluctuating light, and Litchman (2000) compared equal-duration high and low illuminations experimentally, while emphasizing that time averaging of instantaneous rates is at best a slow-response approximation. Walsby (1997) used measured temporal irradiance and depth distributions for numerical water-column estimates. Graham et al. (2017) observed frequency-dependent penalties outside quasi-static predictions.

A separate published mathematical result, *A sharp optical-depth optimum for a uniformly mixed photoinhibited water column* (2026; public result `1f66622b0c1c`), classifies the optimum **of** the depth mean \(M_s(h)\) for a fixed surface irradiance. That result does not assert the sign or the number of crossings of the weighted Jensen difference \(pM_x(h)+qM_y(h)-M_m(h)\) as \(h\) varies, and no implication from its fixed-irradiance maximizer establishes the present one-cutoff and duty-fraction theorem. In particular, this finding compares a fixed mean to a genuine two-point distribution and proves a parameter-wide sign classification, not an isolated optimum.

The verified comparison did not locate the exact global crossover theorem in accessible primary material. The earlier integration formulas make parts of its algebra elementary and could permit independent rediscovery. Relevant full text of Thornley (1974), Idso and Foster (1975), and Walsby (1997) could not be completely checked; their possible stronger coverage and general results on exponential sums remain historical-priority risks. Absence in a search is not proof of novelty.

## Limitations

The theorem is conditional on the *instantaneous* Steele functional form, positive lower irradiance, strict two-level light, uniform biomass, Beer attenuation, and fixed physiological parameters. It is not a result for arbitrary probability laws of irradiance, dynamic physiological acclimation, frequency-dependent growth, water-column vertical advection, time-varying turbidity, nonuniform pigments, spectral photoinhibition, net respiration, measured carbon uptake, or environmental management. The cutoff of **modeled instantaneous gross production** cannot be interpreted as a reliable biological productivity threshold outside those assumptions. No independent scientific verification has been conducted; the supplied diagnostics only support the analytical proof.

## References

1. J. H. Steele, “Environmental Control of Photosynthesis in the Sea,” *Limnology and Oceanography* **7** (1962), 137–150, DOI `10.4319/lo.1962.7.2.0137` (published April 1962, day not recorded in publisher source). [Full paper](https://aslopubs.onlinelibrary.wiley.com/doi/pdf/10.4319/lo.1962.7.2.0137).
2. T. T. Bannister, “Production Equations in Terms of Chlorophyll Concentration, Quantum Yield, and Upper Limit to Production,” *Limnology and Oceanography* **19** (1974), 1–12, DOI `10.4319/lo.1974.19.1.0001` (published January 1974, day not recorded in publisher source). [Full paper](https://aslopubs.onlinelibrary.wiley.com/doi/pdf/10.4319/lo.1974.19.1.0001).
3. J. H. M. Thornley, “Light Fluctuations and Photosynthesis,” *Annals of Botany* **38** (1974), 363–373, DOI `10.1093/oxfordjournals.aob.a084820` (publisher's dated publication record: 1974-03-01; full text inaccessible during comparison).
4. E. Litchman, “Growth Rates of Phytoplankton under Fluctuating Light,” *Freshwater Biology* **44** (2000), 223–235. [Full paper](https://repository.si.edu/server/api/core/bitstreams/8e431958-f920-4917-a1de-6d9c1e66ea61/content).
5. A. E. Walsby, “Numerical Integration of Phytoplankton Photosynthesis Through Time and Depth in a Water Column,” *New Phytologist* **136** (1997), 189–209, DOI `10.1046/j.1469-8137.1997.00736.x` (abstract and references accessible; complete text not verified).
6. P. J. Graham et al., “A Penalty on Photosynthetic Growth in Fluctuating Light,” *Scientific Reports* **7** (2017), 12513, DOI `10.1038/s41598-017-12923-1`.
7. “A Sharp Optical-Depth Optimum for a Uniformly Mixed Photoinhibited Water Column,” published 2026, [full result](https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-a-sharp-optical-depth-optimum-for-a-uniformly-mixed-photoinhibit--1f66622b0c1c/RESULT.md).
8. S. B. Idso and J. M. Foster, “An Analytical Study of Three Characteristic Forms of Light-Forced Primary Production in Aquatic Ecosystems,” *Oecologia* **18** (1975), 145–154, DOI `10.1007/BF00348095` (abstract accessible; full text not verified).
