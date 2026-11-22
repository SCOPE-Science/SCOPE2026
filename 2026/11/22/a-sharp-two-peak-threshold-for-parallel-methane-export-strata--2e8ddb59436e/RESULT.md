# A sharp two-peak threshold for parallel methane-export strata

## Finding

Two independent, equally flushed, two-stage methane-producing strata can generate **two distinct strict local maxima** in total steady exported methane as common flushing intensity varies, although each individual stratum has only one peak. The exact necessary rate-scale separation is
\[
R>R_*=7+4\sqrt{3}.
\]
For each such contrast, a sharp, nonempty interval of positive production-weight ratios gives exactly two peaks, with equality boundaries having only one peak and one horizontal nonextremal stationary point. This is a complete classification for the specified two-stratum rational flux, not a prediction about observed wetlands.

## Assumptions and scope

Consider two noncommunicating hydrologic microstrata \(i\in\{1,2\}\), each with a constant feed of available precursor \(I_i>0\), substrate stock \(S_i\), methane stock \(M_i\), positive conversion coefficient \(0<\kappa_i<a_i\), and positive loss rate \(a_i\). Under a common positive effective hydraulic export/flushing rate \(v\), let
\[
\dot S_i=I_i-(a_i+v)S_i,\qquad
\dot M_i=\kappa_i S_i-(a_i+v)M_i,
\qquad \mathcal F_i=vM_i.
\]
The substrate's fixed loss \(a_i\) includes conversion \(\kappa_i\) plus a nonconversion sink \(a_i-\kappa_i\). This is a deliberately idealized, positive, mass-balanced linear proxy: export removes both stocks at the same effective rate in a stratum; no water-table response, oxygen feedback, redox dynamics, or nonlinear microbial kinetics is asserted. Different stratum rates and source strengths remain independent of \(v\). For constant \(v\), the unique positive attracting equilibrium gives
\[
\mathcal F_i^*(v)=\frac{I_i\kappa_i v}{(a_i+v)^2}.
\]
After rescaling the rate by \(a_1\), relabeling so \(a_2/a_1=R>1\), and dividing by the sum of positive amplitudes, the **mode locations and number** are those of
\[
F_{R,w}(v)=w\frac{v}{(v+1)^2}+(1-w)\frac{v}{(v+R)^2},
\qquad R>1,\quad 0<w<1,\quad v>0.
\]
Here \(v\) is dimensionless and \(w=I_1\kappa_1/(I_1\kappa_1+I_2\kappa_2)\). This normalization affects magnitude only, not critical-point locations. If \(a_1=a_2\), the aggregate has one peak; if one stratum has zero weight the single surviving term has one peak. Those degeneracies are excluded from the strict-contrast theorem.

## Proof

**1. Confinement of all extrema.** Differentiation gives
\[
F'_{R,w}(v)=w\frac{1-v}{(v+1)^3}+(1-w)\frac{R-v}{(v+R)^3}.
\]
It is strictly positive on \(0<v\le1\) and strictly negative on \(v\ge R\). Every stationary point therefore belongs to \((1,R)\), and \(F\) tends to zero at both ends \(v\downarrow0\) and \(v\to\infty\).

**2. An exact scalar crossing equation.** On \((1,R)\) put
\[
H_R(v)=\frac{(R-v)(v+1)^3}{(v-1)(v+R)^3},\qquad K=\frac{w}{1-w}.
\]
Then
\[
F'_{R,w}(v)=\frac{(1-w)(v-1)}{(v+1)^3}\bigl(H_R(v)-K\bigr).
\]
Thus all stationary points, and their type through the derivative sign, are crossings of \(H_R\) with the positive horizontal level \(K\). The endpoint values of \(H_R\) are respectively \(+\infty\) and \(0\).

**3. Exact number of turns.** Logarithmic differentiation, valid throughout \((1,R)\), yields
\[
\frac{H_R'(v)}{H_R(v)}
=-\frac{2(R-1)\,[2v^2-(R+1)v+2R]}{(R-v)(v-1)(v+1)(v+R)}.
\]
The bracket quadratic has discriminant \(\Delta=R^2-14R+1\). For \(1<R<7+4\sqrt3\), \(\Delta<0\), so \(H_R\) strictly decreases. At \(R=7+4\sqrt3\), its derivative vanishes only at the double root \(v_0=(R+1)/4\), and strict decrease persists. This gives one stationary point of \(F\), necessarily a strict maximum, for every \(w\in(0,1)\). At \(R=R_*\) and \(K=H_R(v_0)\), the derivative of \(F\) has a zero of multiplicity three, making the maximum quartically flat.

For \(R>7+4\sqrt3\), both roots
\[
v_-=\frac{R+1-\sqrt\Delta}{4},\qquad
v_+=\frac{R+1+\sqrt\Delta}{4}
\]
lie strictly in \((1,R)\). (For the left endpoint, \(\sqrt\Delta<R-3\) follows by squaring when \(R>R_*\); the right endpoint is immediate.) The sign of \(H_R'\) is negative on \((1,v_-)\), positive on \((v_-,v_+)\), and negative on \((v_+,R)\). Consequently
\[
0<K_-:=H_R(v_-)<K_+:=H_R(v_+)<+\infty.
\]
For \(K_-<K<K_+\), the level is crossed exactly once on each monotonicity interval. The signs of \(F'\) alternate \(+,-,+,-\), providing exactly two strict local maxima and one strict local minimum. Conversely, if \(K\notin(K_-,K_+)\), there cannot be three simple crossings; if \(K\notin[K_-,K_+]\), there is exactly one simple stationary maximum. At either weight boundary \(K=K_-\) or \(K=K_+\), the level has exactly one simple crossing and one tangency; the latter has no sign change in \(F'\), so it is not an extremum. These cases exhaust all positive parameters. Every individual component has exactly one strict maximum, at its own rate scale \(v=1\) or \(v=R\).

**4. Fully rational bimodal witness.** Set \(R=20\), \(w=1/20\). Then \(\Delta=121\), \(v_-=5/2\), \(v_+=8\), and
\[
K_-=\frac{2401}{54675}<\frac1{19}=K<\frac{2187}{38416}=K_+.
\]
Hence the strict two-peak regime holds. The first peak lies in \((1,2)\), the valley in \((5,8)\), and the second peak in \((8,12)\); exact rational endpoint derivative signs and uniqueness supply certified disjoint intervals. No numerical root finder is needed for the existence or completeness statements.

## Verification

Execute `python3 verify.py` with the Python standard library. It checks the *bivariate polynomial identity* underlying the logarithmic derivative, the rational weight inequalities, the exact stationarity identity on a rational test grid, three disjoint witness sign changes, and positive stationary mass balances. All declared universal assertions are justified analytically above; the finite grid is a diagnostic, not an infinite proof.

## Relationship to prior work

Cui et al. (2024) survey heterogeneous hydrologic controls, substrate availability, transport pathways, and nonmonotone wetland methane flux responses. That study describes and reviews broad biogeochemistry rather than specifying or proving this exact two-stratum rational flux classification. Chen et al. (2023) examine nonlinear hydrologic exchange versus methane emission using a microbial-explicit spatial model. The available description and supplementary topics do not establish the present closed two-peak criterion, but the complete article was not available for full-text comparison; the resulting priority risk is explicit. General mixture-mode and logistic-family mathematics may contain related unimodality criteria; the claim is only the stated precise model-specific all-parameter classification, and no assertion of an unprecedented mixture principle is made.

## Limitations

The two independent serial compartments share a constant first-order flushing coefficient and have equal within-stratum removal rates for precursor and methane, an important restrictive assumption. The rate ratio is the ratio of effective first-order losses, not directly a groundwater head difference or observed soil water-table elevation. The weights are fixed with flushing; oxygen, substrate production changes, inter-stratum exchange, ebullition and plant transport are excluded. These restrictions prevent inferring a two-peak field-emission curve or recommending a field intervention. Priority is limited to the inspected literature and the reported database results, not independently certified. The mathematical result concerns **strict local maxima** and does not assert they are equal-height global maxima.

## References

1. S. Cui et al., "Wetland hydrological dynamics and methane emissions," *Communications Earth & Environment* **5**, 470 (2024), first published 2024-08-29. DOI: https://doi.org/10.1038/s43247-024-01635-w . Full open text: https://zenodo.org/records/14917240/files/Wetland%20hydrological%20dynamics%20and%20methane%20emissions.pdf .
2. K. Chen et al., "Vertical Hydrologic Exchange Flows Control Methane Emissions from Riverbed Sediments," *Environmental Science & Technology* **57**, 4014–4026 (2023), published online 2023-02-22. DOI: https://doi.org/10.1021/acs.est.2c07676 .
3. H. Guo et al., "Unraveling Spatially Diverse and Interactive Regulatory Mechanisms of Wetland Methane Fluxes to Improve Emission Estimation," *Environmental Science & Technology* **58**, 15052–15065 (2024), published online 2024-08-12. DOI: https://doi.org/10.1021/acs.est.4c06057 .
