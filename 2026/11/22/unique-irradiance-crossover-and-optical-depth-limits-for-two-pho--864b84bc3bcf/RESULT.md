# Unique irradiance crossover and optical-depth limits for two photoinhibited canopy strata

## Finding

Consider two equally thick optical-depth strata containing one fixed photosynthetic type apiece. Both types attenuate light identically, but one has a strictly stronger Steele-type inhibitory response. Although that type is less productive at **every** strictly positive local irradiance, it is globally better in the **upper** stratum precisely above one and only one critical incident irradiance. The critical irradiance also has distinct, exact thin- and thick-canopy scaling limits.

**Theorem.** Let \(a>b>0\), \(L>0\), and \(q=e^{-L}\). At optical depth \(0\le z\le2L\), let \(I(z)=s e^{-z}\) for incident irradiance \(s>0\), and let the two physiological response curves be
\[
f_a(t)=t e^{-at},\qquad f_b(t)=t e^{-bt}. 
\]
For arrangements \(ab\) (type \(a\) above type \(b\)) and \(ba\) (reverse order), define total instantaneous productivity by integrating the local type's response over its stratum. For **every** \(a>b>0\) and \(L>0\), there is exactly one \(s_c(a,b,L)>0\) such that the difference \(\Delta(s)=P_{ab}(s)-P_{ba}(s)\) satisfies
\[
\Delta(s)<0\quad(0<s<s_c),\qquad \Delta(s)=0\quad(s=s_c),\qquad \Delta(s)>0\quad(s>s_c).
\]
Thus the high-irradiance optimum places the pointwise less productive, more inhibited type \(a\) **above** the type \(b\), while the low-irradiance optimum places it below.

The unique threshold is the solution of the explicit scalar equation
\[
\int_{q^2s_c}^{qs_c}(e^{-bt}-e^{-at})\,dt
=
\int_{qs_c}^{s_c}(e^{-bt}-e^{-at})\,dt.
\]
If \(s_0\) is the unique positive root of
\[
s_0\frac{d}{ds}\log\bigl[s(e^{-bs}-e^{-as})\bigr]\bigg|_{s=s_0}=0,
\]
and \(m\) is the unique median of the positive density proportional to \(e^{-bt}-e^{-at}\) on \((0,\infty)\), meaning
\[
\int_0^m(e^{-bt}-e^{-at})\,dt=\tfrac12(1/b-1/a),
\]
then the **two endpoint laws** are
\[
\lim_{L\downarrow0}s_c(a,b,L)=s_0,
\qquad
\lim_{L\to\infty}e^{-L}s_c(a,b,L)=m.
\]
These claims include strict uniqueness for both limiting scalar equations and apply without restrictions on the contrast \(a/b\), other than \(a>b>0\).

## Assumptions and scope

Optical depth \(z\) is dimensionless, with each stratum exactly \(L>0\) thick. The instantaneous Beer–Lambert field \(I(z)=s e^{-z}\) is **independent of the species ordering**. There is no backscattering, differential spectral extinction, acclimation, dark respiration, species relocation, nutrient coupling, or variability in illumination. Per-optical-depth biomass and initial quantum-efficiency prefactors are equal. This is a static two-arrangement comparison; neither leaf biomass nor total optical depth is an optimization variable. Only \(s>0\), \(a>b>0\), and \(L>0\) are quantified. The type with parameter \(a\) has \(f_a(t)<f_b(t)\) for every \(t>0\).

Write \(P_{ab}(s)=\int_0^L f_a(s e^{-z})\,dz+\int_L^{2L} f_b(s e^{-z})\,dz\); define \(P_{ba}\) by exchanging \(a\) and \(b\) in the two ranges.

## Proof

**1. Exact comparison identity.** Set \(g(t)=e^{-bt}-e^{-at}>0\) for \(t>0\), and \(q=e^{-L}\in(0,1)\). On each stratum substitute \(t=s e^{-z}\), so \(dz=-dt/t\). Because \(f_b(t)-f_a(t)=t g(t)\), cancellation gives
\[
\Delta(s)=\underbrace{\int_{q^2s}^{qs}g(t)\,dt}_{N_s}
-\underbrace{\int_{qs}^{s}g(t)\,dt}_{H_s}.
\]
Equivalently, with \(g(t)=e^{-bt}(1-e^{-(a-b)t})\),
\[
\Delta(s)=\frac{e^{-bq^2s}-2e^{-bqs}+e^{-bs}}{b}
-\frac{e^{-aq^2s}-2e^{-aqs}+e^{-as}}{a}.
\]

**2. Strict single crossing.** Define the positive ratio
\[
R(s)=\frac{\int_{q^2}^{q}g(su)\,du}{\int_q^1g(sv)\,dv}=\frac{N_s}{H_s}.
\]
Its logarithmic kernel elasticity is
\[
E(t)=t\frac{g'(t)}{g(t)}=-bt+\frac{(a-b)t}{e^{(a-b)t}-1}.
\]
For \(c=a-b>0\), direct differentiation yields
\[
E'(t)=-b+c\,\frac{e^{ct}-1-ct e^{ct}}{(e^{ct}-1)^2}<0
\qquad(t>0),
\]
since \(e^x(1-x)-1<0\) for every \(x>0\), as follows by differentiating this function and using its zero at \(x=0\). Therefore, for \(u\in(q^2,q)\) and \(v\in(q,1)\), one has \(E(su)>E(sv)\). Differentiating \(\log R\) is justified by smooth positive integrands on finite intervals: \(s\,d\log R/ds\) equals the \(g(su)\)-weighted mean of \(E(su)\) over the lower interval minus the \(g(sv)\)-weighted mean of \(E(sv)\) over the upper one. Every value in the first mean strictly exceeds every value in the second, hence \(R'(s)>0\) for all \(s>0\).

Since \(g(t)\sim(a-b)t\) as \(t\downarrow0\), evaluating the elementary endpoint integrals yields
\[
\lim_{s\downarrow0}R(s)=\frac{\int_{q^2}^{q}u\,du}{\int_q^1v\,dv}=q^2<1.
\]
As \(s\to\infty\), \(g(t)\sim e^{-bt}\) on the growing integration ranges, and the ratio of endpoint integrals is asymptotic to \(\exp[b(q-q^2)s]\), which diverges to infinity. Hence by continuity and strict increase \(R(s)=1\) at exactly one positive \(s_c\). The sign of \(\Delta(s)=H_s(R(s)-1)\) gives exactly the stated three-way global classification. There are only two permissible arrangements, so this also proves global optimality and uniqueness away from equality.

**3. Thin-stratum limit.** Let \(F_s(z)=s e^{-z}g(s e^{-z})\). The identity from step 1 can also be written as
\[
\Delta(s)=\int_L^{2L}F_s(z)\,dz-\int_0^LF_s(z)\,dz.
\]
For fixed positive \(s\), Taylor expansion uniformly on compact positive \(s\)-intervals gives
\[
\Delta(s)=-s\,[g(s)+s g'(s)]L^2+O(L^3).
\]
Moreover \(g(s)+s g'(s)=g(s)(1+E(s))\). The strict decrease of \(E\), with \(E(0+)=1\) and \(E(\infty)=-\infty\), implies a unique \(s_0>0\) such that \(1+E(s_0)=0\). At any fixed positive \(s\) immediately below/above \(s_0\), the leading coefficient of \(\Delta\) is respectively negative/positive for all sufficiently small \(L\). Bracketing the unique crossing from step 2 between such values proves \(s_c\to s_0\) as \(L\downarrow0\).

**4. Thick-stratum limit.** Put \(y=qs\) and let \(q\downarrow0\). For any fixed \(y>0\), dominated convergence, using positive integrable \(g\), gives
\[
\Delta(y/q)=\int_{qy}^y g(t)\,dt-\int_y^{y/q}g(t)\,dt
\longrightarrow 2\int_0^y g(t)\,dt-\int_0^\infty g(t)\,dt.
\]
The total integral is exactly \(1/b-1/a>0\). Its cumulative distribution function is strictly increasing from zero to the total, so the limiting expression has a unique positive zero \(m\), with negative sign below and positive sign above. Apply the same bracketing of the unique threshold to conclude \(q s_c\to m\), which is the asserted second law.

**5. Exact sign witnesses and magnitude.** For \(a=2\), \(b=1\), and \(q=1/2\), set \(z=e^{-s/4}\). Then
\[
\Delta(s)=z-\tfrac52z^2+2z^4-\tfrac12z^8.
\]
At \(s=4\log2\), \(z=1/2\) and \(\Delta=-1/512\); at \(s=4\log3\), \(z=1/3\) and \(\Delta=526/6561\). The unique threshold lies strictly between these two explicit light values (numerically \(s_c\approx2.802054039187418\)). At \(s=5\), independently integrating the two response curves gives \(P_{ab}\approx0.207766071771\) and \(P_{ba}\approx0.113020577437\). These numerical values are illustrations, not premises of the general proof.

## Verification

The included `verify.py` runs without third-party dependencies using Python 3 standard-library arithmetic. Run `python3 verify.py` after extracting the embedded artifact. It checks exact-rational sign witnesses, separate production integrals versus the difference identity, the single crossing and monotonic ratio across a deterministic parameter sample, and convergence toward the two limiting scalar equations. The recorded run passed **7,839 deterministic assertions**. Its finite checks corroborate the analytic argument above and are not relied upon to infer uniqueness over all real parameters.

## Relationship to prior work

The response curve is a normalized photoinhibition law associated with Steele's work on light-inhibited photosynthesis. Gutschick and Wiegel (1988) optimize a depth-varying **specific leaf mass** with saturating leaf responses and continuous resources; their full available paper uses a different objective/control and does not state the two-type, two-permutation irradiance threshold or its limiting laws. Beyschlag and colleagues (1990) investigate differences in species photosynthetic characteristics and canopy positioning; the accessible abstract establishes numerical model sensitivity, but the full Part II was not accessible for an exhaustive comparison. Werner and colleagues (2001) provide a full-text mechanistic canopy photoinhibition simulation with nonuniform leaf illumination and adaptation; that model has no universal ordering theorem with arbitrary \(a>b\) and \(L>0\). Relevant indexed results on single-type optical-depth optimization and on fixed-budget independent modules likewise do not imply a permutation threshold when shading is independent of the order. These are claim-versus-implication comparisons, not mere title matches. Detailed literature and overlap risks are in `AUDIT.json`.

## Limitations

This establishes a static mathematical result, **not** an empirical recommendation to place light-sensitive crops above light-tolerant crops. The two physiological response curves have equal low-light slopes and the same imposed Beer–Lambert attenuation; differences in absorption, pigments, respiration, acclimation, leaf angles, competition, or canopy microclimate can change the conclusion. A historical priority assessment is provisional: the full 1990 Beyschlag et al. Part II could not be read after searches of lawful open copies and a bounded institutional access attempt. The proof does not claim that the general rearrangement method is new, nor that a larger biological optimization model exhibits exactly one threshold.

The first precisely verified publisher-publication date used as the motivating date is **21 December 2001** for Werner et al.; Steele's earlier seminal article is dated only to the month of April 1962 in the inspected publisher record, not to a verified calendar day. This date choice is not a claim that Steele or later background articles first appeared in 2001.

## References

1. J. H. Steele, "Environmental Control of Photosynthesis in the Sea," *Limnology and Oceanography* **7** (1962), 137–150. https://doi.org/10.4319/lo.1962.7.2.0137
2. V. P. Gutschick and F. W. Wiegel, "Optimizing the Canopy Photosynthetic Rate by Patterns of Investment in Specific Leaf Mass," *The American Naturalist* **132** (1988), 67–86. https://doi.org/10.1086/284838
3. W. Beyschlag, P. W. Barnes, R. J. Ryel, M. M. Caldwell, and S. D. Flint, "Plant Competition for Light Analyzed with a Multispecies Canopy Model. II. Influence of Photosynthetic Characteristics in Mixtures of Wheat and Wild Oat," *Oecologia* **82** (1990), 374–380. https://doi.org/10.1007/BF00317486
4. C. Werner, R. J. Ryel, O. Correia, and W. Beyschlag, "Effects of Photoinhibition on Whole-Plant Carbon Gain Assessed with a Photosynthesis Model," *Plant, Cell & Environment* **24** (2001), 27–40. https://doi.org/10.1046/j.1365-3040.2001.00651.x
