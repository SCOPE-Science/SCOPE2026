# Four kinetic channels distinguish separated twin contaminant pulses from one pulse

## Finding

Four calibrated first-order passive-sampler channels whose elimination rates form the arithmetic progression \(\lambda,2\lambda,3\lambda,4\lambda\) admit an exact **single-versus-twin pulse discriminator**. When the aqueous contaminant history is promised to be either one positive rectangular pulse or two positive, equal-height, equal-duration rectangular pulses, the cubic observable

\[
\Delta=Q_1^2Q_4-2Q_1Q_2Q_3+Q_2^3
\]

is exactly zero for every single pulse, strictly negative for every pair with a positive intervening gap, and zero for contiguous equal-height pulses. This distinction requires four channels in the worst case: there are physically realizable single- and separated-twin-pulse histories with identical responses in the first three channels.

More precisely, for a pair with concentration \(C>0\), common duration \(d>0\), intervening clean gap \(g\ge0\), and elapsed time \(s\ge0\) after the second pulse, set

\[
 x=e^{-\lambda s},\qquad r=e^{-\lambda d},\qquad z=e^{-\lambda(d+g)}.
\]

Then \(0<z\le r<1\), \(0<x\le1\), and

\[
\boxed{\Delta=-2C^3x^6z(r-z)(1-r)^3(1+r)(1-z)^2(1-rz).}
\]

For fixed \(C,x,r\), its absolute magnitude has exactly one maximizing positive gap \(g_*\), characterized by the unique \(z_*=re^{-\lambda g_*}\in(0,r)\) solving

\[
\frac1{z_*}-\frac1{r-z_*}-\frac2{1-z_*}-\frac{r}{1-rz_*}=0.
\]

The maximum describes the unstandardized algebraic contrast, **not** a detection-power optimum under measurement noise. The unconstrained maximum presumes that the earlier pulse can lie sufficiently far in the past; a finite deployment horizon can truncate its feasible gap range.

## Assumptions and scope

Let \(\lambda>0\) and four known gains \(k_j>0\). Each initially empty channel obeys

\[
\frac{dM_j(t)}{dt}=k_jc(t)-j\lambda M_j(t),\qquad M_j(0)=0,\qquad j=1,2,3,4.
\]

At common readout time \(T>0\), define normalized measurements \(Q_j=j\lambda M_j(T)/k_j\). Concentration \(c(t)\) is nonnegative, zero except on the stipulated rectangular interval(s), and exactly constant with the same amplitude \(C\) during both intervals in the twin class. Both twin intervals have the same length \(d\), are contained in \([0,T]\), and have an intervening gap \(g\ge0\). A single positive pulse may have arbitrary positive amplitude and any nonzero length inside \([0,T]\). No constant unknown baseline, kinetic nonlinearities, uptake-rate error, fading concentration, or measurement noise is permitted. The initial absence of stored pollutant is substantive. The equal-rate-step assumption is exact.

The signed classification is only guaranteed under this **one-or-equal-twin promise**: a negative contrast rejects a single rectangular pulse but does not identify the number or shapes of events without that promise. Nothing is inferred about actual environmental instruments unless their calibrated responses justify the first-order equations and the rate ratios.

## Proof

**1. Exact channel response.** Integrating the differential equation gives

\[
M_j(T)=k_j\int_0^T e^{-j\lambda(T-t)}c(t)\,dt.
\]

A pulse of amplitude \(C\) extending from \(a\) to \(b\) contributes \(C(e^{-j\lambda(T-b)}-e^{-j\lambda(T-a)})\) to \(Q_j\). For one pulse, write \(u=e^{-\lambda(T-b)}\), \(v=e^{-\lambda(T-a)}\) with \(0<v<u\le1\). Thus \(Q_j=C(u^j-v^j)\). Setting \(S=u+v\), \(P=uv\) gives

\[
\frac{Q_2}{Q_1}=S,\qquad \frac{Q_3}{Q_1}=S^2-P,\qquad \frac{Q_4}{Q_1}=S^3-2PS.
\]

Substitution into \(\Delta/Q_1^3\) gives zero identically. No uniqueness assumption is needed.

**2. Positive-gap twin sign.** Put the recent pulse's ending time at \(T-s\), its starting time at \(T-s-d\), the earlier pulse's ending time at \(T-s-d-g\), and its starting time at \(T-s-2d-g\). The response superposition is

\[
Q_j=Cx^j(1-r^j)(1+z^j).
\]

Expanding the three cubic products defining \(\Delta\) and collecting factors gives exactly the boxed identity. Its factors are strictly positive apart from the explicit minus sign whenever \(C>0\), \(0<x\le1\), and \(0<z<r<1\). Hence \(\Delta<0\) for \(g>0\). When \(g=0\), \(z=r\); the two equal pulses concatenate into a single pulse of amplitude \(C\) and duration \(2d\), so \(\Delta=0\) both by the identity and directly. The factorization is also exactly verified by a stand-alone integer-polynomial calculation in `checker.py`, without sampling parameter points.

**3. Three are insufficient.** Take \(x=r=1/2\), \(z=1/4\), and \(C=1\). These correspond to two equal pulses with positive gap, equal to the pulse duration, and a one-duration trailing observation delay. They produce

\[
(Q_1,Q_2,Q_3,Q_4)=\left(\frac5{16},\frac{51}{256},\frac{455}{4096},\frac{3855}{65536}\right).
\]

The first three values coincide exactly with those of a *single* pulse with

\[
u=\frac{51+\sqrt{1297}}{160},\qquad
v=\frac{51-\sqrt{1297}}{160},\qquad
C'=\frac{25}{\sqrt{1297}}.
\]

Indeed, \(0<v<u<1\), \(u+v=51/80\), \(uv=163/3200\), and \(C'(u-v)=5/16\). These equalities imply the three reported values by the one-pulse response formulas. Both histories can be placed in the same deployment: take \(T=4\log 2/\lambda\), with twin pulses occupying the first and third successive intervals of length \(\log2/\lambda\). The inferred single-pulse endpoints lie within the deployment because \(v>1/16=e^{-\lambda T}\). But the twin history has \(\Delta=-189/1048576\ne0\), so channel four distinguishes it. This exact alias proves that no classifier based only on the first three responses can distinguish *every* one-pulse history from *every* separated equal twin.

**4. Uniqueness of the gap maximizing contrast magnitude.** At fixed \(C,x,r\), the only gap-dependent factor of \(|\Delta|\) is \(f_r(z)=z(r-z)(1-z)^2(1-rz)\), where \(z=re^{-\lambda g}\). The function is positive for \(0<z<r\) and vanishes at both endpoints. Its logarithmic derivative is the displayed equation for \(z_*\), and its second logarithmic derivative is

\[
-\frac1{z^2}-\frac1{(r-z)^2}-\frac2{(1-z)^2}-\frac{r^2}{(1-rz)^2}<0.
\]

The logarithmic derivative therefore falls strictly from \(+\infty\) to \(-\infty\), proving a unique interior maximizer and a unique positive \(g_*\). A finite horizon permits only \(0\le g\le T-s-2d\); if this bound is smaller than \(g_*\), the constrained maximum is attained at that boundary.

## Verification

The attached `checker.py` uses only the Python standard library. Run `python3 checker.py` from the extracted directory. It computes sparse bivariate integer polynomials to confirm the entire symbolic factorization exactly, verifies the three-channel alias and contrast using rational arithmetic, checks 1300+ rational physical parameter configurations, compares the analytical response with independently integrated first-order equations over seeded schedules, and diagnoses monotonicity of the logarithmic derivative. Analytical factor signs and strict concavity, not finite tests, establish the universal statements. The exact program output and its limits appear in `VERIFICATION.md`.

## Relationship to prior work

Schäfer, Paschke and Liess (online July 16, 2008) experimentally studied response to one short aquatic contamination pulse and biofouling; Shaw and Mueller (online February 4, 2009) studied fluctuating herbicide concentrations and the accuracy of first-order uptake predictions; Hawker (online December 2, 2009) modeled several variable-concentration inputs, including a contamination pulse. These works motivate the first-order convolution but do not, in the inspected accessible material, supply the exact four-rate event-count sign test or its sharp three-rate alias. The full texts of these three closely relevant articles were not all accessible; no definitive negative claim about their full contents is made.

The classical Prony/exponential-moment framework supplies broad algebraic tools for recovering exponential sums and is a genuine partial conceptual predecessor. The present claim is narrower and different: it determines the *minimal* number of readout channels for a strict model-class distinction under positive, equal-duration, equal-height twin pulses, including an explicit three-channel ambiguity and a fixed-sign four-channel factorization. It does not claim a new general moment-inversion procedure. A 2023 open-access water-monitoring review was also inspected for physical assumptions and limitations, not as evidence of mathematical novelty.

## Limitations

The difference between zero and strictly negative is noise-free: arbitrarily small gaps and remote earlier pulses make \(|\Delta|\) arbitrarily small. Channel gain and clearance-rate uncertainties, background contamination, unequal event heights or durations, and more than two events can invalidate the sign classification. Equal event height is essential: with independently variable heights the same cubic contrast need not have a fixed sign. Nor is the model a claim that passive samplers with four perfectly harmonic clearances are readily realizable; calibration and identifiability of a common analyte remain practical hurdles. Full access to several closely relevant historical primary articles was unavailable, so historical priority requires further verification. This is a conditional, structural inverse-result, not a certified field diagnostic.

## References

1. Schäfer, R. B., Paschke, A. and Liess, M. (2008), *Aquatic passive sampling of a short-term thiacloprid pulse with the Chemcatcher: impact of biofouling and use of a diffusion-limiting membrane on the sampling rate*, Journal of Chromatography A 1203, 1–6. https://doi.org/10.1016/j.chroma.2008.05.098 (first online July 16, 2008).
2. Shaw, M. and Mueller, J. F. (2009), *Time Integrative Passive Sampling: How Well Do Chemcatchers Integrate Fluctuating Pollutant Concentrations?*, Environmental Science & Technology 43, 1443–1448. https://doi.org/10.1021/es8021446 (first online February 4, 2009).
3. Hawker, D. W. (2009/2010), *Modeling the response of passive samplers to varying ambient fluid concentrations of organic contaminants*, Environmental Toxicology and Chemistry 29, 591–596. https://doi.org/10.1002/etc.69 (first online December 2, 2009).
4. Kunis, S., Peter, T., Römer, T. and von der Ohe, U. (2015), *A multivariate generalization of Prony's method*, arXiv:1506.00450, https://arxiv.org/abs/1506.00450.
5. Koljančić, N. and Špánik, I. (2023), *Investigative Approaches for Pollutants in Water: Aligning with Water Framework Directive Maximum Allowable Concentrations*, Water 16(1), 27. https://doi.org/10.3390/w16010027 (first online December 20, 2023; contextual review, not the dated motivating source).
