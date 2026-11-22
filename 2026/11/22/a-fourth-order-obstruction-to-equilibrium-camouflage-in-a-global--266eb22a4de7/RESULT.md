# A fourth-order obstruction to equilibrium camouflage in a globally reinitialized Glauber chain

## Finding
For a zero-temperature nearest-neighbor Glauber (voter) chain globally reinitialized to *fresh independent unbiased spins* at Poisson rate \(r>0\), the unique stationary law agrees with the zero-field nearest-neighbor Ising Gibbs law on **every marginal involving at most three spins**, yet differs on a four-spin marginal at every rate. This holds on every periodic ring of \(N\ge5\) sites and on \(\mathbb Z\). In fact there is an explicit strictly positive, local fourth-order witness, and four is the smallest spin-correlation order able to distinguish the laws.

Write \(C_j=\mathbb E_\mu[\sigma_0\sigma_j]\) and define
\[
U=\mathbb E_\mu[\sigma_0\sigma_1\sigma_2\sigma_3],\qquad V=\mathbb E_\mu[\sigma_{-1}\sigma_1\sigma_2\sigma_3].
\]
Let \(q\in(0,1)\) solve \(r=(1-q)^2/q\). Let \(\nu_q\) be the zero-field ferromagnetic Ising Gibbs law with bond coupling \(K=\operatorname{artanh}q\), on the same ring or line. Then \(U_{\nu_q}=C_2\), \(V_{\nu_q}=C_3\), and
\[
\boxed{(r+4)(U-C_2)-(V-C_3)=rC_2>0.}
\]
Consequently, the measured fourth-order discrepancy obeys the quantitative lower bound
\[
\boxed{\max\{|U-C_2|,|V-C_3|\}\ge\frac{rC_2}{r+5}>0.}
\]
For a ring, \(C_j=(q^j+q^{N-j})/(1+q^N)\); on the infinite line \(C_j=q^{|j|}\).

## Assumptions and scope
Sites carry \(\sigma_i\in\{-1,+1\}\). On the ring \(i\in\mathbb Z/N\mathbb Z\), \(N\ge5\), and on the infinite chain \(i\in\mathbb Z\). Each site independently rings at rate one and replaces its spin by either neighboring spin with probability one half. Independently, a *single global* clock rings at rate \(r>0\) and replaces **all** spins simultaneously with a new independent fair-sign configuration. New reset configurations are resampled at every reset; they are not a quenched original sample. There is no field and no other noise. All correlations are stationary expectations of finitely supported spin products. The Gibbs comparator has nearest-neighbor energy \(-K\sum_i\sigma_i\sigma_{i+1}\), with periodic boundary conditions on a ring and the unique infinite-volume zero-field Gibbs law on the line. The comparison concerns stationary *static* marginals, not equality of dynamics.

## Proof
**Existence, uniqueness, and symmetry.** Global reset regeneration gives a stationary distribution on the finite ring and stationary consistent finite-dimensional marginals on the line: sample a backward exponential age of rate \(r\), sample fresh independent fair spins at its start, and evolve the voter process for that age. Coupling two histories at the most recent global reset proves uniqueness for all local observables. The invariant law is translation-, reflection-, and global-sign invariant, so all odd spin products vanish.

**All two-point functions.** For distinct positions the voter generator applied to \(\sigma_i\sigma_j\) yields discrete nearest-neighbor hopping of either index. At stationary separation \(1\le j\le N-1\), the reset source vanishes because a fresh fair sample has zero distinct-site product. Translation invariance therefore gives
\[
(r+2)C_j=C_{j-1}+C_{j+1},\qquad C_0=C_N=1.
\]
The unique solution is \(C_j=(q^j+q^{N-j})/(1+q^N)\) with \(q+q^{-1}=r+2\), i.e. \(r=(1-q)^2/q\). On \(\mathbb Z\), boundedness and symmetry instead impose \(C_j=q^{|j|}\). Positive correlations follow from \(0<q<1\).

**The comparator has exactly the same two-point functions.** In zero-field one-dimensional Ising, the bond variables \(\eta_i=\sigma_i\sigma_{i+1}\) have weights proportional to \(e^{K\eta_i}\). On a ring their product must equal one, giving the two-point formula \((q^j+q^{N-j})/(1+q^N)\). On \(\mathbb Z\), independent bonds with mean \(q\) give \(q^{|j|}\). Zero means and vanishing odd products imply equality of *all* one-, two-, and three-site marginal distributions: for distinct sites \(a,b,c\), the Fourier expansion
\[
\mathbb P(\sigma_a=s_a,\sigma_b=s_b,\sigma_c=s_c)=\frac18\left[1+s_as_bC_{b-a}+s_as_cC_{c-a}+s_bs_cC_{c-b}\right]
\]
is shared by both laws. One- and two-site marginals follow similarly.

**The Gibbs four-spin identities.** For any four cyclically ordered distinct sites, expanding the two-spin-bond representation shows that the Gibbs four-spin expectation is the two-point correlation corresponding to the total length of the first and third cyclic gaps. In particular for sites \((0,1,2,3)\), the length equals two, hence \(U_{\nu_q}=C_2\); for sites \((-1,1,2,3)\) the length is three or its complement, hence \(V_{\nu_q}=C_3\). This holds on a ring with \(N\ge5\), and on the line.

**The four-spin stationarity identity.** Apply the voter generator to \(F=\sigma_0\sigma_1\sigma_2\sigma_3\). Updates at sites \(0\) and \(3\) provide the two outward four-spin terms, both equal by reflection to \(V\), and inward updates at the four sites reduce to pair products. Summing the eight neighbor choices gives
\[
\mathbb E_\mu L_{\rm voter}F=-4U+V+2C_1+C_3.
\]
The fresh independent reset has mean zero on every nonempty product of distinct spins, so stationarity gives \((r+4)U=V+2C_1+C_3\). The pair recurrence at separation two reads \(C_1+C_3=(r+2)C_2\). Subtracting the Gibbs four-spin values and using that recurrence yields
\[
(r+4)(U-C_2)-(V-C_3)=2C_1+2C_3-(r+4)C_2=rC_2.
\]
Because \(rC_2>0\), both deviations cannot vanish. The triangle inequality gives \(rC_2\le(r+4)|U-C_2|+|V-C_3|\le(r+5)\max\{|U-C_2|,|V-C_3|\}\). Combined with agreement at orders one through three, this proves minimality of order four.

A concrete ring instance is \(N=5\), \(q=1/2\), \(r=1/2\), \(C_2=4/11\), for which the strictly positive witness equals \(rC_2=2/11\). On the infinite line at these rates it equals \(1/8\). No limiting approximation is used.

## Verification
The accompanying standalone `checker.py` performs exact symbolic checks of ring recurrences and four-spin residuals for several ring sizes, and independently builds and solves the full \(2^N\)-state continuous-time Markov generator on rings of sizes five, six, and seven. The computed stationary probabilities are used to evaluate pair and four-spin expectations without assuming their formulas. The verified run returned `PASS 154 assertions`. Exact algebra and the stationary generator proof, rather than finite numerical samples, establish the general statements. Execute with `python checker.py` using NumPy, SymPy, and SciPy.

## Relationship to prior work
Glauber's original kinetic Ising analysis supplies the classical zero-temperature dynamics. Magoni, Majumdar, and Schehr (2020) analyze globally reset Glauber Ising magnetization, with resets to a fixed initial configuration, and develop its nonequilibrium stationary framework; their paths use a **fixed** initial configuration instead of a new iid draw at each reset. However, when that fixed configuration is itself sampled from the unbiased iid ensemble and the observations are averaged over it, its **single-time annealed stationary law coincides exactly** with the fresh-iid stationary law considered here: both are the same exponential-age mixture of Glauber evolution from unbiased iid spins. The present theorem therefore contributes a fourth-order static observable within this broader established renewal framework rather than claiming to introduce an unrelated stationary ensemble. Godrèche and Luck (2022) study correlation-based diagnostics for temperature protocols without the present global fresh-iid resetting. The new statement concerns a direct fourth-order obstruction despite complete agreement of low-order static marginals, not the known general renewal formula or the standard pair-correlation difference equation. Similar four-spin violations in spatially temperature-inhomogeneous kinetic chains use another mechanism and do not imply this reset theorem.

## Limitations
The comparison does not assert that the resetting law is a Gibbs law for an alternative non-nearest-neighbor interaction; it only rules out equality with the unique zero-field nearest-neighbor Gibbs law matching all pairs. It does not quantify experimental sample complexity, reset implementation costs, or entropy production. The displayed discrepancy lower bound need not be optimal. Every strictly positive reset rate is covered; the limits \(r\to0\) and \(r\to\infty\) are not included as strictly positive instances. The original model is invariant under global spin inversion, so no odd-order signature is possible. This theorem requires fully simultaneous fresh-iid resetting and does not extend by its proof to sitewise partial resets or quenched resets.

## References
1. R. J. Glauber, “Time-Dependent Statistics of the Ising Model,” *Journal of Mathematical Physics* **4**, 294–307 (1963), https://doi.org/10.1063/1.1703954.
2. M. Magoni, S. N. Majumdar, G. Schehr, “Ising model with stochastic resetting,” *Physical Review Research* **2**, 033182 (2020), https://arxiv.org/abs/2002.04867; https://doi.org/10.1103/PhysRevResearch.2.033182. First public arXiv posting: 2020-02-12.
3. C. Godrèche and J. M. Luck, “The Glauber-Ising chain under low-temperature protocols,” *Journal of Physics A* **55**, 495001 (2022), https://arxiv.org/abs/2208.12512.
