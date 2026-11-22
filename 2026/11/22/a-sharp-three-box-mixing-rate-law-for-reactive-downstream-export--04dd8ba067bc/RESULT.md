# A sharp three-box mixing-rate law for reactive downstream export

## Finding

A chain of three equally sized, continuously mixed water compartments can have a **unique interior worst-case or best-case dispersive exchange rate for downstream discharge**, even with entirely linear first-order removal. No one- or two-compartment chain of the same kind can have such an interior optimum. The three-box outcome is governed by sharp inequalities involving the three local removal rates, and depends on which compartment receives the pollutant loading.

For a unitless throughflow of one, let \(a,b,c>0\) be the first-order removal rates in the upstream, middle, and downstream compartments, respectively. Let \(m\ge0\) be the common symmetric exchange rate between adjacent compartments, and let a constant mass input be added to the **middle** compartment. The fraction of that input ultimately leaving through the downstream outlet is
\[
E_2(m)=\frac{(1+m)(1+a+m)}{P_0+P_1m+P_2m^2},
\]
where
\[
P_0=(1+a)(1+b)(1+c),\quad
P_1=ab+bc+2ac+2(a+b+c+1),\quad P_2=1+a+b+c.
\]
Define
\[
T_A=\frac{a(a+1-c)}c,\qquad
T_C=\frac{a(c+1)}{c(a+1)}.
\]
For all positive \(a,b,c\) and all \(m>0\):

- If \(a>c\), then \(T_C<T_A\). The function \(E_2\) has exactly one strict interior **maximum** if and only if \(T_C<b<T_A\). Otherwise it is strictly monotone: decreasing for \(b\le T_C\) and increasing for \(b\ge T_A\).
- If \(a<c\), then \(T_A<T_C\). The function \(E_2\) has exactly one strict interior **minimum** if and only if \(T_A<b<T_C\). Otherwise it is strictly monotone: decreasing for \(b\le T_A\) (when this positive-parameter regime exists) and increasing for \(b\ge T_C\).
- If \(a=c\), then \(E_2\) increases for \(b>1\), decreases for \(b<1\), and is constant for \(b=1\).

Equalities at a threshold never produce a positive interior extremum. With the same three-box geometry, loading into compartment 1 makes the export fraction **strictly increasing** in \(m\), while loading into compartment 3 makes it **strictly decreasing** for every positive \(a,b,c\). Thus the middle loading location is essential to a nonmonotone response.

For the exact physically admissible example \((a,b,c)=(3,3,1)\),
\[
E_2(m)=\frac{(m+1)(m+4)}{2(4m^2+17m+16)},\qquad
E_2'(m)=\frac{3(4-m^2)}{2(4m^2+17m+16)^2}.
\]
Consequently \(m=2\) is the unique global maximizer, with \(E_2(2)=3/22\), whereas \(E_2(0)=\lim_{m\to\infty}E_2(m)=1/8\). The worst-case export is \(12/11\) times either limiting export. A more strongly heterogeneous example \((a,b,c)=(20,20,1)\) attains its unique maximum at \(m=\sqrt{21}\), approximately \(40.9\%\) above either limiting export, demonstrating that the intermediate mixing regime can have an appreciable effect.

## Assumptions and scope

Three well-mixed equal-volume compartments are connected in series by a fixed water throughflow \(Q>0\) from compartment 1 to 2 to 3, with downstream outlet \(Q\). Adjacent compartments additionally exchange water symmetrically at a common rate \(D\ge0\); these symmetric exchanges cause no net volume change. Clean water enters compartment 1, and pollutant mass is supplied at a constant rate \(J>0\) to exactly one chosen compartment, without adding appreciable water volume. Pollutant is removed irreversibly within compartment \(i\) at first-order rate \(k_i C_i\), with \(k_i>0\) expressed in the same volumetric-flow units as \(Q,D\). The result is about the unique steady state, not transient peak transport, sediment resuspension, nonlinear kinetics, or a fully spatially resolved estuary.

Divide all flow parameters by \(Q\): \(a=k_1/Q\), \(b=k_2/Q\), \(c=k_3/Q\), \(m=D/Q\). At steady state, in units of \(J/Q\), the concentration vector solves
\[
M(m)\mathbf z=\mathbf e_j,\quad
M(m)=\begin{pmatrix}
1+a+m&-m&0\\
-(1+m)&1+b+2m&-m\\
0&-(1+m)&1+c+m
\end{pmatrix}.
\]
The dimensionless exported fraction is \(E_j(m)=z_3\). The matrix is a nonsingular compartmental \(M\)-matrix: its diagonal exceeds the sum of the magnitudes of the off-diagonal entries in each column by \(a\), \(b\), and \(1+c\), respectively. Hence the unique nonnegative steady state exists and is globally attractive for nonnegative initial stocks.

## Proof

Direct cofactor evaluation yields \(\det M(m)=P(m)=P_0+P_1m+P_2m^2>0\), with the displayed positive coefficients, and
\[
E_1(m)=\frac{(1+m)^2}{P(m)},\quad
E_2(m)=\frac{(1+m)(1+a+m)}{P(m)},\quad
E_3(m)=\frac{(1+a)(1+b)+(2a+b+2)m+m^2}{P(m)}.
\]

The numerator of \(E_2'(m)\) (the denominator is \(P(m)^2>0\)) is \(H(m)=Am^2+Bm+C\), where
\[
A=c(a+b)-a(a+1),\quad
B=2(a+1)(bc-a),\quad
C=(a+1)\bigl[bc(a+1)-a(c+1)\bigr].
\]
The signs of \(A,B,C\) are respectively the signs of \(b-T_A\), \(b-a/c\), and \(b-T_C\). If \(a>c\), then \(T_C<a/c<T_A\). For \(b\le T_C\), all three coefficients are nonpositive and \(H(m)<0\) for all \(m>0\); for \(b\ge T_A\), they are nonnegative and \(H(m)>0\). In between, \(C>0>A\), so \(H\) has exactly one positive zero (its two real roots have opposite signs), changing from positive to negative. If \(a<c\), the threshold inequalities reverse to \(T_A<a/c<T_C\). The identical argument gives negative-to-positive crossing and a unique strict minimum in that intervening band, with monotone behavior outside. For \(a=c\), all three coefficient signs coincide with \(\operatorname{sgn}(b-1)\); they all vanish only when \(b=1\). This proves the middle-input classification, including all boundaries.

For upstream input, \(P(m)^2 E_1'(m)\) equals
\[
(m+1)\bigl[(2abc+ab+bc)+(ab+2ac+bc)m\bigr],
\]
which is strictly positive. For downstream input, \(P(m)^2E_3'(m)\) is a quadratic with coefficients, in increasing order,
\[
-b(a+1)^2(b+1),\quad -2(a+1)(a+b)(b+1),\quad
-(2a^2+2ab+2a+b^2+b),
\]
all strictly negative.

For a two-compartment chain with removal rates \(a,b>0\), the common denominator is \(D_2(m)=(1+a)(1+b)+(1+a+b)m\). The exported fractions from upstream and downstream injection are respectively \((1+m)/D_2(m)\) and \((1+a+m)/D_2(m)\). Their derivative numerators are \(ab>0\) and \(-a(a+1)<0\). One compartment has no internal exchange. The three-box middle-input example therefore establishes the smallest chain length admitting a strict positive interior exchange optimum.

## Verification

The stand-alone Python 3 program `checker.py` uses only the standard library and exact rational arithmetic. Running `python3 checker.py` reports 25,248 assertions passed. It independently solves thousands of positive-parameter three-by-three linear systems for all three source locations, checks the closed export formulas and derivative identities, stress-tests all sign-order regimes, checks the two-box sign formulas, and verifies the exact rational example. The analytic coefficient factorization above—not these finite tests—establishes the theorem for all positive real parameters.

## Relationship to prior work

Single-box first-order nutrient retention and watershed attenuation are classical; Alexander et al. (2002) give a detailed reactive water-quality transport application. Soetaert and Herman (1995) employ longitudinal advective-dispersive box equations to infer estuarine residence time, but their focal substance is conservative and they do not classify reactive steady-state export as an exchange coefficient varies. Håkanson and Bryhn (2007) analyze a more detailed multi-compartment phosphorus model with variable internal exchanges, without deriving this three-box sharp source-location and loss-rate phase diagram. Gresch et al. (2009) use compartmental reactor models with backmixing to approximate CFD transport and reaction; the available material emphasizes model construction and validation, not the exact classification above. Related prior mathematical work on finite-time two-box tracer exchange optima, and on serial saturating nutrient-removal orderings, concerns different quantities and does not yield the present three-box steady-state response by a direct restriction. These comparisons support a provisional originality assessment; they do not establish historical priority or a general uniqueness result beyond this specified model.

## Limitations

The exchange coefficient is constrained to be equal across both interfaces, removal is linear and time independent, compartment volumes are equal, and loading occurs in exactly one cell. Real hydraulic dispersion is not necessarily tunable independently of throughflow, and a three-box approximation can introduce effective numerical dispersion. There is no claim about general spatial advection-diffusion-reaction equations, optimization with uncertain rates, real-world management efficacy, or transient peak exposure. The full 1984 paper on transport in lake water-quality models and the full 2009 reactor-compartment article were not completely available for comparison; further primary-source review could affect publication-priority assessment. Independent validation is not claimed.

## References

- R. B. Alexander, A. H. Elliott, U. Shankar, and G. B. McBride, “Estimating the sources and transport of nutrients in the Waikato River Basin, New Zealand,” *Water Resources Research* 38 (2002), DOI: https://doi.org/10.1029/2001WR000878 (first published 2002-12-04).
- K. Soetaert and P. M. J. Herman, “Estimating estuarine residence times in the Westerschelde (The Netherlands) using a box model with fixed dispersion coefficients,” *Hydrobiologia* 311 (1995), 215–224, DOI: https://doi.org/10.1007/BF00008582; lawful open manuscript at https://www.vliz.be/imisdocs/publications/ocrd/140774.pdf (only year and month independently established for the earliest public version).
- L. Håkanson and A. C. Bryhn, “A Dynamic Mass-balance Model for Phosphorus in Lakes with a Focus on Criteria for Applicability and Boundary Conditions,” *Water, Air, & Soil Pollution* 187 (2008), 119–147, DOI: https://doi.org/10.1007/s11270-007-9502-1 (first published 2007-09-28).
- M. Gresch, R. Brügger, A. Meyer, and W. Gujer, “Compartmental Models for Continuous Flow Reactors Derived from CFD Simulations,” *Environmental Science & Technology* 43 (2009), 2381–2387, DOI: https://doi.org/10.1021/es801651j (published online 2009-02-25).
- P. Shanahan and D. R. F. Harleman, “Transport in Lake Water Quality Modeling,” *Journal of Environmental Engineering* 110 (1984), 42–62, DOI: https://doi.org/10.1061/(ASCE)0733-9372(1984)110:1(42); only the abstract and bibliographic record were accessible.
