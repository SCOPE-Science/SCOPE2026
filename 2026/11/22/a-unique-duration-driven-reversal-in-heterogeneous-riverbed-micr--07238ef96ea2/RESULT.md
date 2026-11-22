# A unique duration-driven reversal in heterogeneous riverbed microplastic exchange

## Finding

A closed two-class water-column–riverbed exchange model can reverse which of two environmental phase orders leaves more microplastic suspended, even though each particle class individually has a phase-order preference independent of duration. Under opposite class-specific equilibrium preferences and a consistent ordering of relaxation speeds, such a reversal happens **exactly once** as both phase durations are enlarged in fixed proportion. There is a sharp necessary-and-sufficient composition window and an explicit scalar equation for the crossover.

For classes \(j=1,2\), phases \(i=A,B\), and positive parameters \(k_{ij},r_{ij}\), put
\[
\lambda_{ij}=k_{ij}+r_{ij},\qquad p_{ij}=\frac{r_{ij}}{k_{ij}+r_{ij}}.
\]
Assume
\[
p_{B1}>p_{A1},\quad p_{B2}<p_{A2},\qquad
\lambda_{A1}<\lambda_{A2},\quad\lambda_{B1}<\lambda_{B2}.
\]
For fixed \(\alpha,\beta>0\), phase \(A\) lasts \(\alpha h\) and phase \(B\) lasts \(\beta h\), with \(h>0\). Let \(S_{AB}(h)\) and \(S_{BA}(h)\) be the respective terminal total suspended fractions, with positive class weights \(w_1+w_2=1\). Define
\[
C=w_1(p_{B1}-p_{A1}),\quad D=w_2(p_{A2}-p_{B2}),\quad
q=\frac DC,\quad q_0=\frac{\lambda_{A1}\lambda_{B1}}{\lambda_{A2}\lambda_{B2}}.
\]
Then \(0<q_0<1\) and the following classification holds for **every** initial class-specific water/bed partition:

1. If \(q\le q_0\), then \(S_{AB}(h)>S_{BA}(h)\) for every \(h>0\).
2. If \(q_0<q<1\), there is exactly one \(h_*>0\). For \(h<h_*\), \(S_{AB}(h)<S_{BA}(h)\); for \(h=h_*\) they agree; for \(h>h_*\), \(S_{AB}(h)>S_{BA}(h)\).
3. If \(q\ge1\), then \(S_{AB}(h)<S_{BA}(h)\) for every finite \(h>0\).

The crossover is the unique positive root of
\[
\frac{(1-e^{-\alpha\lambda_{A1}h_*})(1-e^{-\beta\lambda_{B1}h_*})}
{(1-e^{-\alpha\lambda_{A2}h_*})(1-e^{-\beta\lambda_{B2}h_*})}=q.
\]
Its **existence boundaries** \(q_0,1\) are independent of the phase-duration ratio \(\alpha/\beta\), although its location generally is not. For fixed rates and phase proportions, \(h_*\) increases strictly with \(q\) throughout the crossover window.

## Assumptions and scope

The model is a well-mixed, source-free, nonexporting batch with two separately conserved classes of microplastic. The total quantity in each class is fixed and positive; \(w_j>0\) is its fraction of total microplastic, with \(w_1+w_2=1\). For \(x_j(t)\in[0,1]\), the fraction of class \(j\) currently suspended in water, its riverbed fraction is \(1-x_j(t)\). Within phase \(i\) it obeys the linear reversible exchange equation
\[
\frac{dx_j}{dt}=-k_{ij}x_j+r_{ij}(1-x_j)=\lambda_{ij}(p_{ij}-x_j).
\]
Both deposition \(k_{ij}\) and resuspension \(r_{ij}\) are strictly positive. At a phase boundary the rates change instantaneously; no mass is added or removed. Classes do not interact. The two protocols have exactly the same phase durations and differ only in order. Their terminal objective is \(S=w_1x_1+w_2x_2\), not integrated downstream export. All assertions hold for any initial \((x_1(0),x_2(0))\in[0,1]^2\).

The opposite equilibrium preferences and same-direction relaxation-speed inequalities are **hypotheses**, not claims that all real rivers or microplastic types obey them. The variable \(h\) scales both phase durations with fixed positive \(\alpha,\beta\); changing their ratio simultaneously is outside the uniqueness claim.

## Proof

**1. Exact phase composition and elimination of unknown initial conditions.** For class \(j\), phase \(i\) of duration \(t\) acts by the affine map
\[
T_{ij}^{(t)}(x)=p_{ij}+(x-p_{ij})e^{-\lambda_{ij}t}.
\]
Direct expansion of the two map compositions gives
\[
(T_{Bj}^{(\beta h)}\circ T_{Aj}^{(\alpha h)})(x)
-(T_{Aj}^{(\alpha h)}\circ T_{Bj}^{(\beta h)})(x)
=(p_{Bj}-p_{Aj})(1-e^{-\alpha\lambda_{Aj}h})(1-e^{-\beta\lambda_{Bj}h}).
\]
The unknown \(x\) cancels identically. Set \(F_j(h)=(1-e^{-\alpha\lambda_{Aj}h})(1-e^{-\beta\lambda_{Bj}h})>0\). Summing over the two positive weights yields
\[
\Delta(h):=S_{AB}(h)-S_{BA}(h)=C F_1(h)-D F_2(h)=C F_2(h)(R(h)-q),
\qquad R(h)=\frac{F_1(h)}{F_2(h)}.
\]

**2. Strict monotonicity, limits, and all boundary cases.** For fixed \(h>0\), the function \(z\mapsto z/(e^{zh}-1)\) is strictly decreasing on \((0,\infty)\): its derivative has numerator \(e^{zh}-1-zh e^{zh}<0\), because \(u\mapsto e^u(1-u)-1\) is strictly decreasing from zero for \(u>0\). Consequently
\[
\frac{d}{dh}\log R(h)
=\left[\frac{\alpha\lambda_{A1}}{e^{\alpha\lambda_{A1}h}-1}-\frac{\alpha\lambda_{A2}}{e^{\alpha\lambda_{A2}h}-1}\right]
+\left[\frac{\beta\lambda_{B1}}{e^{\beta\lambda_{B1}h}-1}-\frac{\beta\lambda_{B2}}{e^{\beta\lambda_{B2}h}-1}\right]>0.
\]
The Taylor expansion \(1-e^{-ch}\sim ch\) as \(h\downarrow0\) gives \(R(h)\to q_0\), with the factors \(\alpha\beta\) cancelling. As \(h\to\infty\), \(F_1,F_2\to1\), hence \(R(h)\to1\). Strict monotonicity therefore maps \((0,\infty)\) bijectively to \((q_0,1)\). The sign of \(\Delta\) is exactly the sign of \(R-q\); all three cases, their strict boundaries, uniqueness, and initial-condition invariance follow. The same strict monotonicity makes the unique root strictly increasing in \(q\).

**3. Sharp mixture-weight window.** Put \(d_1=p_{B1}-p_{A1}>0\) and \(d_2=p_{A2}-p_{B2}>0\). Substituting \(q=(1-w_1)d_2/(w_1d_1)\) in \(q_0<q<1\) gives the equivalent *necessary and sufficient* window
\[
\frac{d_2}{d_1+d_2}<w_1<\frac{d_2}{d_2+q_0d_1}.
\]
Both endpoints are excluded, and the interval is nonempty because \(q_0<1\). Thus the boundary is sharp and finite-time reversal is impossible for a single class, for equal-direction class equilibrium responses, or outside this window under the stated speed inequalities.

**4. Root behavior at both sharp boundaries.** Write \(a_j=\alpha\lambda_{Aj}\), \(b_j=\beta\lambda_{Bj}\) and \(L=(a_2-a_1)+(b_2-b_1)>0\). Expansion gives \(R(h)=q_0[1+Lh/2+O(h^2)]\). Hence, as \(q\downarrow q_0\) with the rates fixed,
\[
h_* =\frac{2(q-q_0)}{q_0 L}+O((q-q_0)^2).
\]
For \(q\uparrow1\), put \(\mu=\min(a_1,b_1)>0\) and let \(c=2\) if \(a_1=b_1\), otherwise \(c=1\). Since \(a_2>a_1\) and \(b_2>b_1\),
\[
1-R(h)=c e^{-\mu h}(1+o(1)),\qquad
h_*=\frac{1}{\mu}\log\frac{c}{1-q}+o(1).
\]
Thus the threshold diverges logarithmically at the upper composition boundary. These estimates are consequences of the same exact comparison, not assumptions.

**5. Explicit admissible example.** Choose \(\alpha=\beta=1\), \(w_1=7/10\), \(w_2=3/10\), and
\[
(p_{A1},p_{B1},\lambda_{A1},\lambda_{B1})=(1/5,4/5,1,2),
\qquad(p_{A2},p_{B2},\lambda_{A2},\lambda_{B2})=(4/5,1/5,3,5).
\]
All physical rates are strictly positive by \(r_{ij}=\lambda_{ij}p_{ij}\), \(k_{ij}=\lambda_{ij}(1-p_{ij})\). Here \(C=21/50\), \(D=9/50\), \(q=3/7\), \(q_0=2/15\). The unique reversal occurs at \(h_*\approx0.6642424443730566\), independently of initial bed loads. Exact rational interval arithmetic on Taylor enclosures for the exponentials certifies
\[
0.66424243<h_*<0.66424246.
\]
At \(h=0.1\), \(\Delta\approx-0.01111139425\), whereas at \(h=1\), \(\Delta\approx0.05967450396\). These are dimensionless illustrative rates, not fitted river data.

## Verification

The self-contained Python standard-library program `check.py` independently composes phase maps, computes the closed-form swap difference, tests the strict-ratio prediction on 12,000 randomly chosen positive rate combinations, and solves the illustrative scalar equation by bisection. It also encloses the exponentials in the illustrative root bracket using exact rational alternating-series bounds (not a floating-point sign test). Run `python3 check.py` in the same folder; its recorded deterministic execution passed 36,020 supplementary comparisons. The infinite-domain claim rests on the analytic proof above; finite randomized tests are not a proof of uniqueness.

## Relationship to prior work

Mancini, Serra, Colomer and Solari (2023) measured different settling behaviors of distinct microplastic materials in particle-laden flows. Their article supplies the motivation for type-dependent rates; its analyzed flume profiles do not state a time-order crossover theorem for the conserved two-class exchange batch. Drummond and colleagues (2022) analyzed water-column/riverbed mobile–immobile transport with reversible retention and long-tailed residence times, using a different spatial and memory-based formulation; it provides physical context, not the exact mixed two-phase terminal comparison here. Akdogan and Guven (2024) developed a more detailed particle-shape-dependent settling/resuspension model; its accessible abstract describes flow scenarios and nonmonotone turbulence effects. Its complete text could not be checked here, so coverage by an uninspected discussion remains a priority risk. The simple affine two-state relaxation map and the monotonicity of exponential ratios are classical building blocks; novelty is asserted only for their stated two-class **sharp composition/duration phase diagram**, not for those general ingredients or environmental processes.

Related published mathematical results on serial nutrient-removal ordering and three-stage stormwater wash-off concern nonconservative removal or source-driven scalar maps, rather than a closed two-class opposing-equilibria mixture. A previously recorded single-class mobile/bed hydrological two-regime result gives a duration-independent **single-class** order sign with downstream export. That result cannot by itself establish the mixed-class unique scale-dependent crossover or its sharp weight boundaries; it is acknowledged, not reasserted as new.

## Limitations

The model has no external inputs, advection, spatial gradients, permanent burial, export, time-varying within-phase coefficients, interclass aggregation, feedback or measurement error. Particle types can differ in both equilibrium partition and timescale; the theorem requires strictly opposite equilibrium responses and one class uniformly slower in both phases. These inequalities have not been verified in a particular river. Without the speed order, more complicated sign changes may occur; no universal crossing bound is claimed there. Actual environmental flow histories may violate the fixed phase-duration-ratio assumption. The result compares terminal suspended stock only, **not** cumulative exported pollutant mass, water quality or optimal field management. Literature priority is provisional pending independent comparison with any inaccessible full texts. No independent external validation is asserted.

## References

1. Mancini, M., Serra, T., Colomer, J., Solari, L. (2023). *Suspended sediments mediate microplastic sedimentation in unidirectional flows*. Science of the Total Environment **890**, 164363. First publicly available 2023-05-20. DOI: https://doi.org/10.1016/j.scitotenv.2023.164363. Full open article: https://flore.unifi.it/bitstream/2158/1318752/2/1-s2.0-S0048969723029844-main.pdf.
2. Drummond, J. D., et al. (2022). *Microplastic accumulation in riverbed sediment via hyporheic exchange from headwaters to mainstems*. Science Advances **8**, eabi9305. DOI: https://doi.org/10.1126/sciadv.abi9305. Open text: https://pmc.ncbi.nlm.nih.gov/articles/PMC8754297/.
3. Akdogan, Z., Guven, B. (2024). *Modeling the settling and resuspension of microplastics in rivers: Effect of particle properties and flow conditions*. Water Research **264**, 122181. DOI: https://doi.org/10.1016/j.watres.2024.122181. Abstract inspected; complete text not accessible.
4. Nizzetto, L., et al. (2016). *A theoretical assessment of microplastic transport in river catchments and their retention by soils and river sediments*. Environmental Science: Processes & Impacts **18**, 1050–1059. DOI: https://doi.org/10.1039/C6EM00206D. Accessible abstract consulted; full manuscript access not confirmed.
5. Published mathematical comparisons: https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-three-stage-stormwater-exposure-ordering-with-continued-po--056749ef0302 and https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-two-index-ordering-law-for-serial-saturating-nutrient-removal--15d05df5ff61. These are neighboring, not identical, model objectives.
