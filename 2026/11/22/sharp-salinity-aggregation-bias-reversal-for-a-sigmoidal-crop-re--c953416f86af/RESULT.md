# Sharp salinity-aggregation bias reversal for a sigmoidal crop response

## Finding

Let a landscape consist of a nonconstant area-weighted distribution \(X\) of baseline root-zone salinity, with \(0<a\le X\le b<\infty\) almost surely, and write \(\mu=\mathbb E X\). Assume all patches share the same half-yield salinity \(C_{50}>0\) and positive response exponent \(p\). Under a common salinity multiplier \(\lambda>0\), the van Genuchten–Gupta-type relative yield at salinity \(c\) is

\[
G_p(c)=\frac{1}{1+(c/C_{50})^p}.
\]

Define the *area-aggregation bias* as distributed minus averaged-input yield,

\[
\Delta_p(\lambda)=\mathbb E\,G_p(\lambda X)-G_p(\lambda\mu).
\]

Then the sharp response-exponent classification is:

1. If \(0<p\le1\), then \(\Delta_p(\lambda)>0\) for every \(\lambda>0\).
2. If \(p>1\), there is exactly one \(\lambda_*>0\), with \(\Delta_p(\lambda)<0\) for \(0<\lambda<\lambda_*\), equality at \(\lambda_*\), and \(\Delta_p(\lambda)>0\) for \(\lambda>\lambda_*\). With \(u_p=((p-1)/(p+1))^{1/p}\), the crossing lies strictly in \((C_{50}u_p/b,\ C_{50}u_p/a)\).
3. For the original common exponent \(p=3\) and two **equal-area** salinity classes \(X=\mu-\delta\) and \(X=\mu+\delta\), where \(0<\delta<\mu\), the crossing is explicitly

\[
\lambda_* = C_{50}\left(\frac{3\mu}{6\mu^4-3\mu^2\delta^2+\delta^4}\right)^{1/3}.
\]

The dimensionless ratio \(\lambda_*\mu/C_{50}\) strictly increases with \(\delta/\mu\) and satisfies the **sharp uniform limits**

\[
2^{-1/3}<\frac{\lambda_*\mu}{C_{50}}<(3/4)^{1/3}.
\]

The bounds are approached only as \(\delta/\mu\) tends to \(0\) or \(1\), respectively; neither is attained for the stipulated two positive, distinct salinities.

## Assumptions and scope

The distribution represents positive area fractions, not measurement noise; \(X\) has compact support bounded away from zero. The common multiplier scales all patch salinities proportionally while preserving their proportions, crop response parameters, and area weights. Patches contribute equal normalized potential yield per unit area. The theorem concerns the mathematical response function, not salinity transport, groundwater flow, yield calibration, or the economic feasibility of varying \(\lambda\). The identical \(C_{50}\) and \(p\) assumptions across patches are essential to the stated reduction.

## Proof

Put \(t=(\lambda/C_{50})^p>0\), \(v=\mu^p\), and \(Z=X^p\). Direct common-denominator subtraction gives

\[
\Delta_p(\lambda)=\frac{t}{1+tv}\,H(t),\qquad
H(t)=\mathbb E\frac{v-Z}{1+tZ}.
\]

Since \(X\) is nonconstant with mean \(\mu\), its law has positive mass on both sides of \(\mu\). Split \(H=A-B\), with

\[
A(t)=\mathbb E\frac{(v-Z)_+}{1+tZ},\quad
B(t)=\mathbb E\frac{(Z-v)_+}{1+tZ},
\]

both strictly positive for all \(t\ge0\). For \(t_2>t_1\ge0\), pair a point \(z<v\) from \(A\) with \(w>v\) from \(B\). Its contribution to \(A(t_2)B(t_1)-A(t_1)B(t_2)\) has the positive numerator

\[
(t_2-t_1)(w-z)(v-z)(w-v)
\]

over the four positive factors \((1+t_jz)(1+t_jw)\), \(j=1,2\). Integrating over all such pairs proves that \(A(t)/B(t)\) is strictly increasing. Thus \(H(t)\) can cross zero at most once, necessarily from negative to positive.

At \(t=0\), \(H(0)=\mu^p-\mathbb EX^p\). Strict Jensen inequalities make this positive for \(0<p<1\), zero for \(p=1\), and negative for \(p>1\). Monotonicity of \(A/B\) makes \(H(t)>0\) for every \(t>0\) if \(p\le1\). For \(p>1\), bounded positive support permits passing to the limit:

\[
\lim_{t\to\infty}tH(t)
=\mu^p\mathbb E X^{-p}-1>0,
\]

again by strict Jensen, this time for \(x\mapsto x^{-p}\). Continuity, the sign at zero, and strict ratio monotonicity give existence and uniqueness and the asserted signs.

The function \(G_p\) is strictly concave when \(0<c/C_{50}<u_p\) and strictly convex when \(c/C_{50}>u_p\) for \(p>1\), as follows by factoring the sign of its second derivative as \((p+1)(c/C_{50})^p-(p-1)\). Jensen therefore supplies the stated strict bounds on \(\lambda_*\) using the support endpoints \(a,b\).

For the equal-area two-point specialization with \(p=3\), write \(t=(\lambda/C_{50})^3\). Exact rational reduction yields

\[
\Delta_3(\lambda)=\frac{\delta^2 t\,[t(6\mu^4-3\mu^2\delta^2+\delta^4)-3\mu]}{(1+t\mu^3)(1+t(\mu-\delta)^3)(1+t(\mu+\delta)^3)}.
\]

All denominator factors are positive and the coefficient of \(t\) in the square brackets is positive. Setting those brackets to zero proves the closed form. With \(q=\delta/\mu\in(0,1)\),

\[
\frac{\lambda_*\mu}{C_{50}}=\left(\frac{3}{6-3q^2+q^4}\right)^{1/3}.
\]

The denominator's derivative is \(-6q+4q^3<0\) on \((0,1)\); its limiting values are \(6\) and \(4\). This proves strict increase, both sharp limiting constants, and nonattainment.

## Verification

The standalone `checker.py` uses seeded finite examples to verify the bias signs for \(0<p\le1\), bracket the unique crossing for \(p>1\), and verify the cubic equal-area formula and its sharp dimensionless bounds. It prints the number of successful diagnostic assertions; the analytical proof above supplies the infinite-domain argument.

For example, the two equal-area classes \(5\) and \(15\) dS/m, with \(C_{50}=12\) dS/m and \(p=3\), have \(\mu=10\) and \(\delta=5\) dS/m. The unique multiplier is approximately \(\lambda_*=0.991871359132\). At \(0.7\lambda_*\), distributed minus averaged-input relative yield is about \(-0.04720618\); at \(1.3\lambda_*\), it is about \(0.08296294\).

## Relationship to prior work

Van Genuchten and Gupta (1993) supply the sigmoidal crop-salinity response and highlight \(p=3\) as a useful common exponent. Their analysis fits local yield response curves and does not derive an area-heterogeneity crossover, an exact two-class bias threshold, or its sharp contrast bounds. Alzraiee, Gates and Garcia (2013) model stochastic root-zone salinity and yield variation in irrigated fields; their publisher abstract does not state this exact threshold and the full paper could not be inspected. Hoffmann and colleagues (2015, 2016) study spatial aggregation errors in crop models; the cited papers do not give this specific salinity-response theorem.

Variation-diminishing theory for totally positive integral kernels supplies a broad general mathematical mechanism for limiting the number of sign reversals. Accordingly, the *at-most-one* sign-change step is **not** claimed as a new general theorem of integral transforms. The present statement instead combines an applied response-exponent classification, sign existence, and a directly usable exact cubic two-area threshold with sharp heterogeneity bounds. This is a model-specific result; its historical-priority status beyond inspected sources is not independently established.

## Limitations

Only deterministic common-multiplier salinity scaling and the specified Hill-type response are treated. Spatial salinity variations need not remain proportional under actual irrigation or leaching; nonlinear spatial feedback, patchwise different yield potential, response heterogeneity, salinity-induced soil-structure changes, correlated exposure, and empirical uncertainty can invalidate the modeling assumptions. The proof gives no field-level calibration or guarantee about any particular crop. General variation-diminishing mathematics may imply additional aspects of the sign theorem, and uninspected applied sources could contain equivalent or stronger exact results.

## References

- M. Th. van Genuchten and S. K. Gupta, *A Reassessment of the Crop Tolerance Response Function*, Journal of the Indian Society of Soil Science **41** (1993), 730–737. Author-hosted original full text: https://www.ars.usda.gov/arsuserfiles/20361500/pdf_pubs/P1295.pdf
- A. H. Alzraiee, T. K. Gates and L. A. Garcia, *Modeling Subsurface Heterogeneity of Irrigated and Drained Fields. II: Multivariate Stochastic Analysis of Root-Zone Hydrosalinity and Crop Yield*, Journal of Irrigation and Drainage Engineering **139** (2013), 809–820; first online 2013-04-13. https://doi.org/10.1061/(ASCE)IR.1943-4774.0000587
- H. Hoffmann et al., *Variability of effects of spatial climate data aggregation on regional yield simulation by crop models*, Climate Research **65** (2015), 53–69. https://doi.org/10.3354/cr01326
- H. Hoffmann et al., *Impact of Spatial Soil and Climate Input Data Aggregation on Regional Yield Simulations*, PLOS ONE **11** (2016), e0151782. https://doi.org/10.1371/journal.pone.0151782
- *Applications of total positivity theory to 1D prescribed curvature problems*, Journal of Mathematical Analysis and Applications (2015), discussing established variation-diminishing theorems. https://doi.org/10.1016/j.jmaa.2015.03.002
