# A sharp all-temperature heat-rectification bound for a homogeneous three-spin Ising chain

## Finding
For a zero-field ferromagnetic open Ising path with three spins, identical positive exchange \(J\), and identical rate-one local heat-bath spin-flip clocks, attach the two outer spins to one heat reservoir and the central spin to another. Interchanging the two reservoir temperatures produces a genuine thermal diode even without unequal bonds or unequal clocks. For all \(0<\beta_{\mathrm h}<\beta_{\mathrm c}<\infty\), put \(a=\tanh(\beta_{\mathrm h}J)\) and \(b=\tanh(\beta_{\mathrm c}J)\). The ratio of magnitudes of stationary heat transferred per unit time from the hot reservoir to the chain, with the central site hot versus the two outer sites hot, is exactly
\[
R(a,b)=\frac{2+2b^2-ab}{2+2a^2-ab}>1.
\]
There is an exact, strict and globally sharp bound
\[
1<R(a,b)<1+\frac4{\sqrt{15}}.
\]
The supremum \(1+4/\sqrt{15}\) is approached only in the simultaneous limiting arrangement \(b\uparrow1\) and \(a\to4-\sqrt{15}\). It is not attained at any finite pair of unequal reservoir temperatures. In the corresponding two-spin homogeneous open chain, the heat-current magnitude is exactly invariant under swapping the two bath temperatures. Thus three spins are minimal within these homogeneous open-path single-site-bath models.

## Assumptions and scope
Let \(\sigma_i\in\{-1,1\}\) for \(i=1,2,3\), and let
\[
H(\sigma)=-J(\sigma_1\sigma_2+\sigma_2\sigma_3),\qquad J>0.
\]
The flip of spin \(i\) occurs at rate \(w_i(\sigma)=\tfrac12[1-\sigma_i\tanh(\beta_i J\sum_{j:\,|j-i|=1}\sigma_j)]\), with \(\beta_1=\beta_3=\beta_e\) and \(\beta_2=\beta_m\). This normalization means a rate-one heat-bath refresh at each spin; every flip obeys local detailed balance with its assigned reservoir. The finite chain is irreducible for \(0\le\beta_i<\infty\). For each site, heat current *into the chain* from the corresponding reservoir is the stationary mean of \(w_i(\sigma)[H(\sigma^{(i)})-H(\sigma)]\). The total heat from either thermal reservoir is summed over all sites coupled to it. \(\beta_{\mathrm h}\) and \(\beta_{\mathrm c}\) designate hot and cold inverse temperatures, respectively, so \(\beta_{\mathrm h}<\beta_{\mathrm c}\). No external field, particle exchange, additional edge or boundary bath is assumed.

## Proof
Write \(t=\tanh(\beta_eJ)\), \(u=\tanh(\beta_mJ)\), and \(v=\tanh(2\beta_mJ)=2u/(1+u^2)\). By reflection symmetry in the unique stationary law, set \(x=\langle\sigma_1\sigma_2\rangle=\langle\sigma_2\sigma_3\rangle\) and \(z=\langle\sigma_1\sigma_3\rangle\). The Markov generator applied to these two observables gives the exact closed stationary equations
\[
0=-2x+t+\frac{v}{2}(1+z),\qquad 0=-2z+2tx.
\]
These imply \(z=tx\) and \(x=(2t+v)/(4-vt)\). Since the central spin flip changes energy by \(2J\sigma_2(\sigma_1+\sigma_3)\), its exact stationary heat inflow is
\[
Q_m=J[2x-v(1+z)]=\frac{2J(t-u)(1-tu)}{2(1+u^2)-tu}.
\]
Energy stationarity and reflection symmetry give \(Q_1=Q_3=-Q_m/2\). For \(0\le t,u<1\), the denominator and \(1-tu\) are strictly positive, hence the heat flow direction follows \(t-u\), equivalently from hotter to colder. With center hot one has \((t,u)=(b,a)\); with outer sites hot one has \((t,u)=(a,b)\). Taking the positive hot-bath inflow magnitudes yields, respectively,
\[
I_{\mathrm{center}}=\frac{2J(b-a)(1-ab)}{2(1+a^2)-ab},\qquad
I_{\mathrm{outer}}=\frac{2J(b-a)(1-ab)}{2(1+b^2)-ab}.
\]
Dividing gives the stated \(R\), and \(R>1\) follows from \(b>a\).

For fixed \(a\), differentiation gives
\[
\frac{\partial R}{\partial b}=\frac{2(4b+4a^2b-a^3-ab^2)}{(2+2a^2-ab)^2}>0.
\]
Indeed \(a^3+ab^2\le2b^3<4b\) whenever \(0\le a<b<1\). Thus every ratio is strictly smaller than its \(b\uparrow1\) limit
\[
F(a)=\frac{4-a}{2+2a^2-a}.
\]
A second exact differentiation gives
\[
F'(a)=\frac{2(a^2-8a+1)}{(2+2a^2-a)^2}.
\]
The sole critical point within \([0,1]\) is \(a_*=4-\sqrt{15}\), and the derivative switches from positive to negative there. Therefore \(\max_{[0,1]}F=F(a_*)=1+4/\sqrt{15}\). Strictness at finite \(b<1\) and the unique limiting maximizing value of \(a\) establish the nonattainment and limiting rigidity.

For comparison, in the two-spin open path with the same exchange and independent rate-one local heat baths at inverse temperatures \(\beta_1,\beta_2\), the stationary bond correlation obeys \(\langle\sigma_1\sigma_2\rangle=[\tanh(\beta_1J)+\tanh(\beta_2J)]/2\). Thus the heat inflow at spin 1 is \(J[\tanh(\beta_2J)-\tanh(\beta_1J)]/2\). Its magnitude is unchanged by interchanging the baths. The one-spin system has no interaction or steady inter-bath heat flow. This proves minimality within the stated restricted family.

## Verification
The accompanying standalone \(\texttt{verify.py}\) solves the full eight-state stationary Markov generator over exact rational arithmetic for a \(10\times10\) grid of rational \((t,u)\) pairs; it independently computes all three heat currents and two correlations, matching the derived formulas in all 100 cases. It independently solves the full four-state two-spin Markov chain at the same 100 pairs and checks bath-swapping symmetry. Run \(\texttt{python3 verify.py}\) with Python 3 and no third-party dependencies. The infinite parameter-domain result follows from the analytic generator calculation and derivative inequalities, not from those finite checks.

## Relationship to prior work
The two-temperature Glauber chain and its stationary currents are well-established. Schmüser and Schmittmann (2002) analyze a periodic even-length chain with alternating baths; Schmittmann and Schmüser (2002) derive finite-ring stationary correlations. Lavrentovich and Zia (2010) analyze a junction of two semi-infinite thermal domains, and Bauer and Cornu (2017) solve an even periodic alternating-temperature chain and its heat-current fluctuations. These models differ in boundary topology from the finite open three-spin chain with one center bath and a two-site outer bath. In particular their current identities do not directly assert the exact orientation-dependent trimer formula or the global sharp ratio \(1+4/\sqrt{15}\). This comparison does not establish historical uniqueness, since related finite-chain calculations may have appeared elsewhere.

## Limitations
This is a finite-state, infinite-observation-time stationary-current result. The theorem assumes rate-one heat-bath clocks, ferromagnetic homogeneous nearest-neighbor coupling, zero field, and the specified central-versus-endpoint bath assignment. It does not assert the same universal ratio for longer chains, other update rules, unequal clocks, finite-time transport, or quantum chains. The boundary \(\beta_{\mathrm c}\to\infty\) is a limit through finite-temperature stationary systems and is not asserted to be an attained finite-temperature optimizer.

## References
1. F. Schmüser and B. Schmittmann, *Non-equilibrium stationary state of a two-temperature spin chain* (first public version 2002-06-18), https://arxiv.org/abs/cond-mat/0206345.
2. B. Schmittmann and F. Schmüser, *Stationary correlations for a far-from-equilibrium spin chain* (first public arXiv version 2002-12-27), https://arxiv.org/abs/cond-mat/0212616.
3. M. O. Lavrentovich and R. K. P. Zia, *Energy flux near the junction of two Ising chains at different temperatures* (first public version 2010-08-30), https://arxiv.org/abs/1008.5099.
4. M. Bauer and F. Cornu, *Thermal contact through a two-temperature kinetic Ising chain* (first public version 2017-12-06), https://arxiv.org/abs/1712.02273.
5. Z. Rácz and R. K. P. Zia, *Two-temperature kinetic Ising model in one dimension: Steady-state correlations in terms of energy and energy flux*, Phys. Rev. E 49 (1994), 139–144, https://doi.org/10.1103/PhysRevE.49.139.
