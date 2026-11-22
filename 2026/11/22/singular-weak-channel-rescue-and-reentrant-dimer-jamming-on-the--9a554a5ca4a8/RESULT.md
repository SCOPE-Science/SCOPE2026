# Singular weak-channel rescue and reentrant dimer jamming on the four-cube

## Finding

Let \(Q_4\) be the Cartesian product of four copies of \(K_2\), with vertices \(\{0,1\}^4\). At each edge, attempt irreversible adsorption of one dimer according to an independent exponential clock. The eight edges parallel to the first coordinate have rate \(r\ge0\); the other twenty-four edges have rate one. A dimer is accepted exactly when both endpoint vertices are still vacant. All accepted dimers remain permanently fixed. Write \(K_r\) for the number eventually accepted and \(p(r)=\Pr(K_r=8)\).

The probability of perfect coverage is discontinuous when the distinguished rate vanishes:
\[
 p(0)=\frac{289}{441},\qquad \lim_{r\downarrow0}p(r)=\frac{293}{441},\qquad
 p(r)=\frac{293}{441}-\frac{225653011}{290332350}r+O(r^2)\quad(r\downarrow0,\ r>0).
\]
The jump \(4/441\) is the probability that an arbitrarily late weak-coordinate deposition repairs two independently jammed three-cubes with matching antipodal vacancy pairs. Among binary hypercubes of dimension at least two, dimension four is the first to exhibit this weak-coordinate perfect-coverage discontinuity.

At the opposite extreme, the failure probability is quadratic in inverse rate:
\[
 p(r)=1-\frac{36}{r^2}+O(r^{-3})\qquad(r\to\infty).
\]
At equal edge rates, the complete terminal distribution is
\[
\begin{aligned}
\Pr(K_1=6)&=\frac{1416949}{56019600},\\
\Pr(K_1=7)&=\frac{389239200251}{735257250000},\\
\Pr(K_1=8)&=\frac{6296549887}{14139562500}.
\end{aligned}
\]
There are no other possible terminal counts. In addition,
\[
 p(1/2)=\frac{570855820090139614856593}{1201811705012081012850000}
 >p(1),\quad
 p(2)=\frac{12973948988785984681}{26501736736290816000}>p(1).
\]
Since \(p\) is continuous for strictly positive rates, it has a strict interior *comparison dip*: at least one local minimum in \((1/2,2)\), and a global minimum at some finite positive rate. No uniqueness or explicit minimizing rate is asserted.

## Assumptions and scope

Vertices are binary words \(x=(x_0,x_1,x_2,x_3)\), and edges connect words differing in exactly one coordinate. The chosen coordinate is \(x_0\). The clocks are independent, with distinct almost-sure arrival times. The observation is after *all* successful adsorptions, with no fixed time cutoff, diffusion, desorption, or repeated productive arrivals. At \(r=0\), edges parallel to \(x_0\) are absent; at every \(r>0\) those edges may arrive arbitrarily late. The claims concern this finite sixteen-site network, not a thermodynamic-limit transition.

## Proof

**Exact finite-state recursion.** Represent the occupied vertices by a subset \(S\subseteq\{0,1\}^4\), initially empty. Let \(A(S)\) be the edges whose two endpoints avoid \(S\). For \(e\in A(S)\), put \(w_e(r)=r\) if \(e\) is parallel to \(x_0\), and \(w_e(r)=1\) otherwise. Given \(S\), the next accepted edge is \(e\) with probability \(w_e(r)/W(S,r)\), where \(W(S,r)=\sum_{e\in A(S)}w_e(r)\). Rejected arrivals do not affect this competition, by independence and memorylessness. Hence the probability \(h_S(r)\) of eventual full coverage satisfies
\[
 h_S(r)=\frac{\sum_{e\in A(S)}w_e(r)h_{S\cup e}(r)}{W(S,r)}
\]
when \(W(S,r)>0\), and the boundary condition is \(h_S(r)=1\) if \(S\) is the entire vertex set, and \(0\) otherwise if no edge remains. Every transition adds two vertices, so backward induction makes this a finite, uniquely solvable system; for \(r>0\), every probability is a rational function of \(r\). The analogous vector-valued recurrence with terminal indicator \(\mathbf1_{\{|S|/2=k\}}\) determines the entire distribution of \(K_r\). Exhaustive rational evaluation gives the three fractions at \(r=1\), and the two displayed strictly positive-rate comparison fractions. The executable exact-arithmetic certificate `verify_q4.py` supplies both a backward recursion and an independent forward mass-propagation calculation, including explicit assertions for every reported rational value.

**Weak-coordinate discontinuity.** With \(r=0\), the graph is two disjoint three-cubes, and their deposition processes are independent. On one \(Q_3\), the dimer process ends with four dimers with probability \(17/21\), and otherwise ends with three dimers, leaving one of four antipodal vertex pairs vacant, each with probability \(1/21\). These facts follow by the same eight-vertex finite exact recursion and are independently enumerated in the certificate. Thus \(p(0)=(17/21)^2\). As \(r\downarrow0\) through positive rates, with probability tending to one every unit-rate productive arrival precedes any distinguished-coordinate productive arrival. The resulting residual sets consist of the two independently jammed three-cubes. If both halves have the *same* antipodal vacant pair, the two remaining distinguished-coordinate edges can fill all four vacancies; in every other defective case, full coverage is impossible. The event has probability \(4(1/21)^2=4/441\), establishing the right limit and the jump. For dimensions two and three, removing one coordinate yields two copies of \(Q_1\) or \(Q_2\), respectively, on which every maximal dimer matching is perfect. Therefore no corresponding positive right-limit jump is possible in those dimensions.

**Exact asymptotic coefficients.** To obtain the near-zero and inverse-large-rate expansions without numerical extrapolation, classify available edges at \(S\) as *fast*, of rate one, or *slow*, of rate \(z\). For \(r\downarrow0\), take \(z=r\) with the three ordinary coordinate directions fast. For \(r\to\infty\), divide all rates by \(r\), take \(z=1/r\), and make the distinguished-direction edges fast. Let \(a_S,b_S\) count available fast and slow edges. The recursion is
\[
 (a_S+b_Sz)h_S(z)=\sum_{e\ \mathrm{fast}}h_{S\cup e}(z)+z\sum_{e\ \mathrm{slow}}h_{S\cup e}(z).
\]
Expand \(h_S(z)=\sum_{j\ge0}c_{S,j}z^j\). Whenever \(a_S>0\), coefficient comparison gives the finite exact recursion
\[
 c_{S,j}=\frac{\sum_{e\ \mathrm{fast}}c_{S\cup e,j}+\sum_{e\ \mathrm{slow}}c_{S\cup e,j-1}-b_Sc_{S,j-1}}{a_S},
\]
with negative-index coefficients zero; when \(a_S=0<b_S\), simply average the slow successor coefficients. Terminal coefficients are one or zero at order zero and zero at every higher order. Backward rational evaluation, independently repeated using forward formal-power-series propagation, yields respectively
\[
(c_{\varnothing,0},c_{\varnothing,1},c_{\varnothing,2})=
\left(\frac{293}{441},-\frac{225653011}{290332350},\frac{17759824852187387}{13252394315160000}\right)
\]
for \(z=r\), and \((1,0,-36)\) for \(z=1/r\). The finite rational function is analytic from the positive side at each singular endpoint after cancelling the common factor at states with \(a_S=0\). These exact coefficients prove both stated expansions, including the absence of an inverse-first-power failure term at large rate.

**Nonmonotonicity.** Exact rational comparisons show \(p(1/2)>p(1)\) and \(p(2)>p(1)\). Continuity and compactness ensure a minimum strictly inside \([1/2,2]\). Its interior location gives a local minimum. Moreover, the two endpoint limits \(293/441\) and \(1\) are strictly larger than \(p(1)\), so a global minimum is attained in a compact subinterval of \((0,\infty)\). This does not prove uniqueness.

## Verification

Run `python3 verify_q4.py` with a standard Python 3 interpreter. The script uses exact `fractions.Fraction` arithmetic throughout and no third-party libraries. Two differently organized algorithms—backward terminal recursion and forward propagation over increasing occupied masks—independently produce the three terminal fractions and the rate comparisons. The two independently organized formal-series recurrences agree on both Taylor certificates. The checker additionally verifies that each three-cube defective terminal set is an antipodal pair. The graph has sixteen vertices and thirty-two edges; the exact finite-state computation covers every reachable state, not a sample of random simulations. The mathematical argument for the formal-series coefficients is the finite recursion above, and the standalone script is the fully reproducible arithmetic certificate.

## Relationship to prior work

Pippenger (1989) studied graph random sequential adsorption, including the edge-occupation/greedy-matching version. Penrose and Sudbury (2005) rigorously formulated dimer adsorption on graphs and developed general evolution equations and formulas for tree-like geometries. Their process definition and edge-order principle are foundational here, not newly claimed. Koza and Kondrat (2020) proved a percolation statement applying to jammed configurations on finite hypercuboidal lattices, but it does not determine the terminal probabilities or the coordinate-rate response of this sixteen-site graph. Related published weak-bridge adsorption analyses on clique barbells already demonstrate that positive-rate limits can be singular; the specific four-cube rescue event, exact jamming distribution, initial negative slope and quadratic strong-channel asymptotic are not consequences of that model's clique parity formula. Research on static perfect matchings and resonance sectors of the four-cube concerns different probability laws. The claims of exact Q4 coefficients and nonmonotonic response remain provisional against incompletely indexed or inaccessible historical work.

## Limitations

The theorem is for a single finite hypercube, not an asymptotic result for arbitrary dimension. It describes the eventually jammed outcome rather than an experimentally bounded observation time; hence the discontinuity at exactly zero rate is not a finite-time discontinuity. The adsorbate has no relaxation, desorption, spatial diffusion or interaction beyond endpoint exclusion. The proof shows existence, but not uniqueness or exact location, of the optimal rate. Independent historical-priority confirmation and independent scientific validation have not been performed. Full text of Pippenger (1989) was unavailable in the comparison; only its abstract and bibliographic information were accessible.

## References

1. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM J. Discrete Math. **2** (1989), 393–401. DOI:10.1137/0402034, https://doi.org/10.1137/0402034.
2. M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, Ann. Appl. Probab. **15** (2005), 853–889; first arXiv posting 2005-03-24, https://arxiv.org/abs/math/0503519.
3. Z. Koza and G. Kondrat, *Jammed systems of oriented dimers always percolate on hypercubic lattices*, arXiv:2001.02008 (first posting 2020-01-07), https://arxiv.org/abs/2001.02008.
4. *A parity-sensitive weak-link law for irreversible dimers on clique barbells*, publicly available exact-science record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-parity-sensitive-weak-link-law-for-irreversible-dimers-on-cliq--430185f8b66b.
