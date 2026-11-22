# Sharp symmetry breaking for two fixed-budget compartments with substrate-inhibited kinetics

## Finding

In an idealized *instantaneous*, noninteracting pair of equal-volume, equal-biomass compartments, the substrate-inhibited Haldane–Andrews response has a complete sharp allocation law. Fix any positive substrate constants \(K_s,K_i\), a positive total concentration budget \(2\bar s\), and common positive specific-rate scale \(\mu_{\max}\). The two nonnegative concentrations satisfy \(s_1+s_2=2\bar s\). We maximize the sum of their instantaneous specific responses
\[
\mathcal R(s_1,s_2)=\mu_{\max}\left[\frac{s_1}{K_s+s_1+s_1^2/K_i}+\frac{s_2}{K_s+s_2+s_2^2/K_i}\right].
\]
Set
\[
\sigma=\sqrt{K_sK_i},\qquad \alpha=\sqrt{K_i/K_s},\qquad m=\bar s/\sigma,
\quad B=1+\alpha m+m^2.
\]
Let \(m_c=m_c(\alpha)\) be the **unique positive** root of \(m_c^3-3m_c-\alpha=0\) (necessarily \(m_c>\sqrt3\)).

- For \(0<m\le m_c\), the **unique** ordered maximizer is the homogeneous allocation \(s_1=s_2=\bar s\).
- For \(m>m_c\), there are **exactly two** ordered maximizers, obtained by exchanging the two entries in
\[
(s_1,s_2)=\sigma(m-d_*,m+d_*),\qquad
 d_* =\sqrt{\frac{m B-(\alpha+2m)\sqrt B}{\alpha+m}},
\qquad 0<d_*<m.
\]
Neither complete concentration in one compartment nor equal splitting is optimal in the latter regime.

The transition is continuous but has the sharp square-root onset
\[
d_*\sim\sqrt{\frac{3(m_c^2-1)}{2m_c}}\,\sqrt{m-m_c}\quad(m\downarrow m_c),
\]
and the high-load optimal *less-exposed* compartment tends to the **individual optimal concentration**:
\[
 m-d_*\longrightarrow1,\qquad s_{\rm low}\longrightarrow\sqrt{K_s K_i}\quad(m\to\infty).
\]
Thus, despite the individual rate starting to decline already at dimensionless concentration \(1\), fixed-mean heterogeneity is globally advantageous only beyond the strictly larger threshold \(m_c>\sqrt3\).

## Assumptions and scope

- Two independent, equal-volume, equal-biomass compartments have identical kinetic constants and equal response weight. Substrate concentration is static over a short response-assessment interval, not a self-consistent chemostat steady state. The only coupling is the exact fixed-sum constraint. Concentrations may be zero; there is no cap on either other than the total.
- The Haldane–Andrews law is an assumed phenomenological instantaneous specific-rate response. No spatial diffusion, microbial growth feedback, maintenance, toxicity-dependent mortality, mass-transfer limitation, temporal substrate depletion, or product inhibition is inferred from it.
- All \(K_s,K_i,\mu_{\max},\bar s\) are strictly positive. The threshold statement concerns **all** such parameters, not merely a numerical case.
- The physical interpretation is comparison of *sum of two rates for equal biomass*, not removal flux after variable reactor residence times. The dimensionless objective differs from the physical objective by the positive multiplier \(\mu_{\max}\alpha\).

## Proof

Write \(u_j=s_j/\sigma\) and \(f_\alpha(u)=u/(1+\alpha u+u^2)\). The fixed-sum constraint makes every feasible unordered allocation equal to \((m-d,m+d)\) for some \(0\le d\le m\). Put \(F(d)=f_\alpha(m-d)+f_\alpha(m+d)\) and \(D_{\pm}=1+\alpha(m\pm d)+(m\pm d)^2>0\). Direct differentiation and a common-denominator expansion give the **exact identity**
\[
 F'(d)=\frac{4d\,P(d^2)}{D_-^2D_+^2},\qquad
 P(z)=(\alpha+m)z^2-2mBz+B(m^3-3m-\alpha).
\]
The two endpoint signs are
\[
 P(0)=B(m^3-3m-\alpha),\qquad
 P(m^2)=-(\alpha^2m+4\alpha m^2+\alpha+4m^3+3m)<0.
\]
The strictly convex quadratic \(P\) has leading coefficient \(\alpha+m>0\). The cubic \(m^3-3m-\alpha\) is negative on \((0,\sqrt3]\) and strictly increasing on \((\sqrt3,\infty)\), with one positive root \(m_c>\sqrt3\).

When \(m\le m_c\), both endpoint values of \(P\) on \([0,m^2]\) are nonpositive and the latter strictly negative. Strict convexity gives \(P(z)<0\) for every \(0<z<m^2\). Consequently \(F\) decreases strictly on \((0,m]\), and \(d=0\) is the unique global maximizer. At the critical value, \(P(0)=0\) still gives strict decrease for every positive \(d\).

When \(m>m_c\), \(P(0)>0>P(m^2)\). Since \(P\) is an upward-opening quadratic, it has precisely one zero in \((0,m^2)\), with sign positive before and negative after that zero; its second zero exceeds \(m^2\). Therefore \(F\) increases and then decreases exactly once, proving a unique optimizing imbalance \(d_*>0\) (and exactly two ordered allocations). The discriminant is \(4(\alpha+2m)^2B\), so the smaller quadratic root gives the displayed expression for \(d_*^2\). This also proves \(d_*<m\) and excludes the concentrated endpoint.

For the onset, apply the implicit-function theorem to \(P(z,m)\) at \((z,m)=(0,m_c)\). Here \(\partial_zP=-2m_c B_c<0\) and \(\partial_mP=B_c(3m_c^2-3)>0\), so
\[
 d_*^2=\frac{3(m_c^2-1)}{2m_c}(m-m_c)+O((m-m_c)^2).
\]
The square-root asymptotic follows. For fixed \(\alpha>0\), expansion of the exact smaller root as \(m\to\infty\) gives \(d_*^2=m^2-2m+1+O(m^{-1})\), hence \(d_*=m-1+O(m^{-1})\). Finally \(f_\alpha'(u)=(1-u^2)/(1+\alpha u+u^2)^2\) is positive for \(u<1\) and negative for \(u>1\), so the limiting smaller-compartment concentration is exactly the individual optimum. No numerical or finite search is used to prove global optimality.

## Verification

The accompanying standalone `verify_haldane.py` checks all five critical derivative/discriminant identities *symbolically* using SymPy. It also uses exact rational arithmetic for 600 parameter evaluations and tests 101 imbalances in each of 99 deterministic parameter-budget cases. The packaged replay printed **10,667 checks passed**; no probabilistic experiment is taken as a universal proof. Run `python verify_haldane.py` with Python 3 and SymPy installed.

For \(\alpha=1\) and \(m=3\), \(d_*=1.854800600587\ldots\), so the optimal concentrations are \(1.145199399413\ldots\) and \(4.854800600587\ldots\) in units of \(\sigma\). The dimensionless sum rises from \(6/13=0.461538461538\ldots\) for equal concentrations to \(0.496295481041\ldots\), a gain of about \(7.53069\%\). This numerical example illustrates but does not establish the theorem.

## Relationship to prior work

The underlying inhibition response is classical; this result does **not** claim to discover substrate inhibition or its single-compartment optimum. Tan, Wang and Marshall (1996) provide a general physical interpretation of models including Haldane–Andrews kinetics. Reed, Lieb and Nijhout (2010) explain biological regulatory roles of substrate inhibition. Gharasoo and colleagues (2015) analyze inhibition combined with *finite-rate bioavailability transfer*, identifying distinct kinetic crossover thresholds; their modeled rate law is not a fixed-sum two-compartment objective. The more general engineering literature on reactor cascades optimizes residence time, conversion and dynamic steady states rather than the specified static independent-compartment response sum. In particular, the accessible 2021 cascade design study and 2022 two-tank mathematical analysis use serially connected, flow-coupled tanks, not fixed-sum independent response evaluations.

A literature and mathematical-result comparison found no established statement forcing the exact all-parameter fixed-sum threshold, both ordered maxima, square-root onset and asymptotic preservation of one optimal compartment. This **does not prove global priority**. Classical convex-envelope and nonconcave resource-allocation results are a residual possible source of stronger covering formulations; the exact implication was not established by the inspected sources.

## Limitations

The result applies only to **two** equally weighted compartments under the stipulated static constraint and canonical quadratic-in-substrate inhibition denominator. It neither optimizes continuous-time reactor control nor asserts a health, wastewater or agricultural prescription. Finite checker experiments do not independently certify the theorem. An external independent audit and historical literature assessment have not been performed. Earlier sources with only year/month-level dating establish historical context but not a verified first-public **day** for this specific theorem.

## References

- Tan, Y., Wang, Z. X., and Marshall, K. C. (1996), *Modeling substrate inhibition of microbial growth*, *Biotechnology and Bioengineering* 52, 602–608, first published 1996-12-05, https://doi.org/10.1002/(SICI)1097-0290(19961205)52:5%3C602::AID-BIT7%3E3.0.CO;2-N.
- Reed, M. C., Lieb, A., and Nijhout, H. F. (2010), *The biological significance of substrate inhibition: A mechanism with diverse functions*, *BioEssays* 32, 422–429, first published 2010-04-22, https://doi.org/10.1002/bies.200900167.
- Gharasoo, M., Centler, F., Van Cappellen, P., Wick, L. Y., and Thullner, M. (2015), *Kinetics of Substrate Biodegradation under the Cumulative Effects of Bioavailability and Self-Inhibition*, *Environmental Science & Technology* 49, 5529–5537, published online 2015-04-15, https://doi.org/10.1021/es505837v.
- Abu Reesh, I. M. (2021), *Optimum Design of N Continuous Stirred-Tank Bioreactors in Series for Fermentation Processes Based on Simultaneous Substrate and Product Inhibition*, *Processes* 9, 1419, https://doi.org/10.3390/pr9081419.
- Stacey, A. J., and Shepherd, J. J. (2022), *Analysis of a continuously stirred two tank reactor cascade with Haldane kinetics*, *Computational and Applied Mathematics* 41, 127, https://doi.org/10.1007/s40314-022-01807-4.
- Andrews, J. F. (1968), *A mathematical model for the continuous culture of microorganisms utilizing inhibitory substrates*, *Biotechnology and Bioengineering* 10, 707–723, https://doi.org/10.1002/bit.260100602. Historical origin of the microbial rate model; a full day of first public release was not verified.
