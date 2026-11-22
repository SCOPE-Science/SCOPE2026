# A duration-independent order law for reversible riverbed contaminant storage

## Finding

**Theorem (complete two-regime order comparison).** Fix two hydrological regimes \(i\in\{A,B\}\) with positive mobile-export, bed-attachment, and bed-release rates \(u_i,k_i,r_i>0\), and any positive durations \(t_A,t_B>0\). A source-free contaminant pulse has initial mobile and bed-stored masses \(M_0,B_0\geq0\), with \(M_0+B_0>0\). Let \(E_{AB}\) denote cumulative downstream export when regime A operates first for \(t_A\) and then B for \(t_B\), and let \(E_{BA}\) denote export under the reverse ordering of **the same two regime-duration pairs**. Define
\[
\begin{aligned}
\kappa_i&=\sqrt{(u_i+k_i-r_i)^2+4k_i r_i},\\
h_i&=\frac{2e^{-(u_i+k_i+r_i)t_i/2}}{\kappa_i}
 \sinh\left(\frac{\kappa_i t_i}{2}\right)>0,\\
\alpha&=u_Ak_B-u_Bk_A,\qquad
\beta=u_Br_A-u_Ar_B.
\end{aligned}
\]
Then the **exact finite-horizon export difference** is
\[
\boxed{E_{AB}-E_{BA}=h_Ah_B(\alpha M_0+\beta B_0).}
\]
Consequently its sign is **independent of both positive durations**, although its magnitude is not. The classification covers all parameters and all equality cases: A-first exports more exactly when \(\alpha M_0+\beta B_0>0\); B-first exports more exactly when this expression is negative; and they tie exactly when it vanishes. In particular, if \(\alpha\beta<0\), setting \(\eta=B_0/(M_0+B_0)\) yields exactly one interior loading threshold
\[
\boxed{\eta_* =\frac{\alpha}{\alpha-\beta}\in(0,1)}
\]
with a strict reversal of the preferred order on crossing \(\eta_*\), for **every** choice of positive durations. If \(\alpha\beta\geq0\), no strict reversal is possible between interior load compositions; if \(\alpha=\beta=0\), all orders tie for all loads. The boundary cases \(\alpha=0\) or \(\beta=0\) have only the directly specified pure-compartment ties.

A transparent exact example sets low-flow regime A to \((u_A,k_A,r_A)=(1,1,1)\) and high-flow regime B to \((u_B,k_B,r_B)=(3,2,2)\), in consistent inverse-time units. Here \(\alpha=-1\) and \(\beta=1\), giving
\[
E_{AB}-E_{BA}=h_Ah_B(B_0-M_0).
\]
For every pair of positive durations, high-flow-first exports more if the initial contaminant is predominantly mobile, low-flow-first exports more if it is predominantly bed-stored, and the two protocols tie at precisely one-half bed storage. Both exchange rates and the export rate increase in the high-flow regime; no extrapolation from field measurements is asserted.

## Assumptions and scope

The mobile mass \(M(t)\), reversible riverbed-stored mass \(B(t)\), and cumulative downstream exported mass \(E(t)\) evolve within regime \(i\) by
\[
\begin{aligned}
\dot M&=-(u_i+k_i)M+r_iB,\\
\dot B&=k_iM-r_iB,\\
\dot E&=u_iM,\qquad E(0)=0.
\end{aligned}
\]
Each regime is homogeneous, deterministic, perfectly mixed, and has fixed first-order rate constants. There is no new contaminant input during the two stages, no irreversible degradation or burial in the bed, no delayed transport beyond the downstream boundary, and no flow-rate feedback from particle concentration. All masses have the same units and all rates have dimensions inverse time. The downstream metric is **total exported mass by the end of the two intervals**, not maximum concentration, peak outflow, residence-time variance, or subsequent long-run export. Regime A and B can be distinct in all three rates. Changing their order swaps the chronological positions of both regimes while keeping each regime's associated duration unchanged.

## Proof

**1. Positivity and conservation.** Write \(z=(M,B)^\top\), \(\mathbf1=(1,1)^\top\), and let
\[
Q_i=\begin{pmatrix}-(u_i+k_i)&r_i\\ k_i&-r_i\end{pmatrix}.
\]
The off-diagonal entries are positive. Hence \(e^{tQ_i}\) is entrywise nonnegative for \(t\geq0\), and both masses remain nonnegative. Since \(\dot M+\dot B+\dot E=0\), for either ordering with final mass vector \(z_T\),
\[
E_T=M_0+B_0-\mathbf1^\top z_T.
\]

**2. A positive matrix-exponential coefficient.** Define \(\gamma_i=(u_i+k_i+r_i)/2\). Direct multiplication gives
\[
(Q_i+\gamma_i I)^2=(\kappa_i^2/4)I.
\]
Therefore, by separating even and odd powers in the absolutely convergent exponential series,
\[
e^{t_iQ_i}=e^{-\gamma_i t_i}\left[
\cosh(\kappa_i t_i/2)I+
\frac{2\sinh(\kappa_i t_i/2)}{\kappa_i}(Q_i+\gamma_i I)
\right]=a_iI+h_iQ_i,
\]
where \(a_i=e^{-\gamma_it_i}[\cosh(\kappa_it_i/2)+(2\gamma_i/\kappa_i)\sinh(\kappa_it_i/2)]\) and \(h_i\) is exactly the strictly positive coefficient in the Finding. The strict positivity uses \(t_i>0\) and \(\kappa_i>0\); no limiting or numerical inference is needed.

**3. Exact order gap.** For A then B, the final state is \(z_{AB}=e^{t_BQ_B}e^{t_AQ_A}z_0\); for B then A it is \(z_{BA}=e^{t_AQ_A}e^{t_BQ_B}z_0\). Thus, using conservation,
\[
\begin{aligned}
E_{AB}-E_{BA}
&=\mathbf1^\top(e^{t_AQ_A}e^{t_BQ_B}-e^{t_BQ_B}e^{t_AQ_A})z_0\\
&=h_Ah_B\mathbf1^\top(Q_AQ_B-Q_BQ_A)z_0.
\end{aligned}
\]
Direct multiplication of the two displayed \(2\times2\) generators gives
\[
\mathbf1^\top(Q_AQ_B-Q_BQ_A)
=(u_Ak_B-u_Bk_A,\ u_Br_A-u_Ar_B)
=(\alpha,\beta),
\]
proving the boxed identity. Note that \(h_Ah_B>0\) for all finite positive stage durations: **there cannot be a duration-driven change of sign**, even when the two intervals are of unequal lengths.

**4. Sharp reversals and boundaries.** With \(S=M_0+B_0>0\), write \(M_0=S(1-\eta)\) and \(B_0=S\eta\) for \(\eta\in[0,1]\). The order difference is \(S h_Ah_B[\alpha+(\beta-\alpha)\eta]\). This affine function has one strict interior zero if and only if the endpoint coefficients have opposite signs, namely \(\alpha\beta<0\), with zero at the displayed \(\eta_*\). Otherwise no strict interior reversal exists. Direct evaluation covers \(\alpha=0\), \(\beta=0\), and \(\alpha=\beta=0\). For the example, \(\alpha=-1\), \(\beta=1\), so the zero is \(\eta_*=1/2\) with strict opposite signs on each side. This proves all assertions.

## Verification

The standalone standard-library program `verify.py` verifies, by exact rational arithmetic over 900 parameter samples, both generator-commutator column sums and the derived linear-form identity; independently computes 240 pairs of matrix exponentials from their defining power series (not the hyperbolic formula); and compares their two-order cumulative exports with the claimed prefactor formula. It additionally tests both sign regimes and the exact equality boundary of the worked example at several unequal positive durations. Execute `python3 verify.py` in the directory containing this result; the tested program prints `VERIFY_OK assertions=3435`. These finite tests support reproducibility and do not replace the universal analytical proof in Steps 1–4.

For short stages, \(h_i=t_i+O(t_i^2)\), so the order effect is \(t_At_B(\alpha M_0+\beta B_0)+O(t_At_B(t_A+t_B))\); this is consistent with the matrix commutator and is not an extra assumption.

## Relationship to prior work

Boos et al. (2024), in the full accessible article including Methods, Results, and Discussion, measured separate low- and high-flow flume responses, downstream breakthrough curves, and reversible riverbed retention. They found faster breakthrough and low residual sediment loads under higher flow, but did not compare reversed **two-stage** fixed-rate protocols or classify an initial mobile-versus-bed mass threshold. Munz et al. (2024), in the accessible complete experimental article, measured particle-retention profiles under differing flow and sediment conditions and modeled a flow-dependent filtration coefficient, not the exact temporal ordering of reversible two-compartment export. Drummond et al. (2022) developed a more detailed hyporheic residence-time model; its public abstract and accessible metadata support the need to model bed storage, but the full text was not obtainable here, so a whole-document noncoverage conclusion is not made about it.

Rasmussen et al. (2016) developed general nonautonomous compartmental transit-time theory, with full accessible exposition of time-dependent compartmental dynamics, but studied mean age and mean transit time rather than two-stage **total-export order** and its sharp initial-storage reversal. A published result on three-stage stormwater washoff with continuing supply studies a **scalar surface stock** and an integrated recipient exposure, not a reversible mobile/bed two-state model or terminal exported mass. A published two-box tracer-exchange result optimizes a single receiving-box concentration with **constant** rates, not ordering of two regimes. A published exact three-factor split for conservative two-state Markov generators concerns mass-preserving stochastic transitions and a constrained decomposition of a summed generator. It has no downstream absorbing export and does not compare the two orderings of killed generators for a prescribed initial mobile/bed loading. The standard matrix exponential and its Cayley–Hamilton identity are not claimed as new: the mathematical contribution assessed here is their sharp application to all initial compositions, arbitrary stage rates and arbitrary positive unequal durations, including the load-dependent reversal and universal equality boundary.

## Limitations

This is a mathematical result for an idealized two-state, first-order, source-free reversible-storage system. It does not quantify hydrodynamic flow, spatial bedforms, turbulent release, immobilized fractions, nonlinear sorption, further groundwater loss, particle-size distributions, fresh upstream delivery, measurement noise, or concentration-dependent filtration. The proof says only which of **two fixed regime-duration orderings** exports more mass by their shared endpoint. It neither identifies the optimal policy among unconstrained controls nor implies a general multi-stage ordering law. The regime rates in the example are illustrative, not fitted to any cited experiment. Historical mathematical priority is still subject to broader older matrix-semigroup literature and the inaccessible full Drummond text; no independent validation or field confirmation is claimed.

## References

1. J.-P. Boos, F. Dichgans, J. H. Fleckenstein, B. S. Gilfedder, and S. Frei (2024), *Assessing the Behavior of Microplastics in Fluvial Systems: Infiltration and Retention Dynamics in Streambed Sediments*, Water Resources Research 60, e2023WR035532. First published 23 February 2024. https://doi.org/10.1029/2023WR035532
2. M. Munz, C. Loui, D. Postler, M. Pittroff, and S. E. Oswald (2024), *Transport and retention of micro-polystyrene in coarse riverbed sediments: effects of flow velocity, particle and sediment sizes*, Microplastics and Nanoplastics 4, 2. Published 15 January 2024. https://doi.org/10.1186/s43591-023-00077-z
3. J. D. Drummond et al. (2022), *Microplastic accumulation in riverbed sediment via hyporheic exchange from headwaters to mainstems*, Science Advances 8, eabi9305. Electronic article date 12 January 2022. https://doi.org/10.1126/sciadv.abi9305
4. M. Rasmussen et al. (2016), *Transit times and mean ages for nonautonomous and autonomous compartmental systems*, Journal of Mathematical Biology 73, 1379–1398. https://doi.org/10.1007/s00285-016-0990-8
5. *Sharp three-stage stormwater exposure ordering with continued pollutant supply* (public mathematical result, 2026), available from published-finding corpus research records; mathematical comparison restricted to its scalar washoff model and its integrated-exposure metric.
6. *A sharp exchange-rate optimum for an unequal-loss two-box tracer* (public mathematical result, 2026), available from published-finding corpus research records; mathematical comparison restricted to its constant-rate two-box receiver-peak optimization.

7. *An exact positive three-factor split for two-state Markov generators* (public mathematical result, 2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-an-exact-positive-three-factor-split-for-two-state-markov-genera--9b0eeef7eade/RESULT.md .
