# Sharp survival-horizon reversal for one large reserve versus two equal-area reserves

## Finding

Fix a total protected area \(A>0\), a reference extinction rate \(e>0\), an area exponent \(\gamma>0\), and a recolonization rate \(c\geq0\). One reserve of area \(A\) is initially occupied and is locally extinguished at rate \(e\). The alternative has two initially occupied, equal-area reserves of size \(A/2\), each undergoing independently a local extinction event at rate \(d=2^\gamma e\). Whenever exactly one smaller reserve is occupied, it recolonizes the empty one at rate \(c\). Complete extinction is absorbing; there is no immigration from outside either configuration. All clocks are exponential and independent conditional on the state.

Set \(\delta=2^\gamma>1\), \(d=\delta e\), and
\[
\alpha=\frac{c+3d-\sqrt{(c+3d)^2-8d^2}}2,
\qquad
\beta=\frac{c+3d+\sqrt{(c+3d)^2-8d^2}}2.
\]
Then \(0<\alpha<\beta\) and the respective global-extinction survival functions are exactly
\[
S_1(t)=e^{-et},\qquad
S_2(t)=\frac{\beta e^{-\alpha t}-\alpha e^{-\beta t}}{\beta-\alpha},\quad t\ge0.
\]
Define the two sharp recolonization thresholds
\[
c_{\mathrm{tail}}=e(\delta-1)(2\delta-1),
\qquad
c_{\mathrm{mean}}=e(2\delta^2-3\delta).
\]
**All-deadline classification.** If \(c\ge c_{\mathrm{tail}}\), then \(S_2(t)>S_1(t)\) for every \(t>0\). If \(0\le c<c_{\mathrm{tail}}\), exactly one positive time \(T_*\) satisfies \(S_2(T_*)=S_1(T_*)\); moreover \(S_2(t)>S_1(t)\) for \(0<t<T_*\), while \(S_2(t)<S_1(t)\) for \(t>T_*\).

**Mean classification and disagreement.** The means are
\[
\mathbb E\tau_1=\frac1e,\qquad
\mathbb E\tau_2=\frac{c+3d}{2d^2}.
\]
Thus \(\mathbb E\tau_2>\mathbb E\tau_1\) exactly when \(c>c_{\mathrm{mean}}\). The identity
\[
\boxed{c_{\mathrm{tail}}-c_{\mathrm{mean}}=e}
\]
shows that for **every** \(\gamma>0\) the nonempty physical parameter interval
\[
\max\{0,c_{\mathrm{mean}}\}<c<c_{\mathrm{tail}}
\]
contains configurations in which splitting improves *mean* persistence but is worse at every sufficiently distant fixed deadline. A strictly positive \(c\) can always be selected in this interval.

For example \(\delta=2\) and \(c=5e/2\) give \(\mathbb E\tau_2=17/(16e)>1/e\) and \(\alpha=(17-\sqrt{161})e/4>e\); the unique survival-curve crossover occurs at \(eT_*\approx2.0154308462756489\). This is a distributional rather than just a mean-persistence statement.

## Assumptions and scope

The one-reserve design has one occupied patch and independent exponential extinction with rate \(e\); the split design has two equivalent occupied patches, each with local extinction rate \(d=2^\gamma e\). The exponent \(\gamma>0\) is a *hypothesized* area-rate relation, not inferred empirically. Recolonization occurs only from an extant occupied patch to its empty counterpart at fixed total transition rate \(c\). No landscape restoration, correlated shock, background immigration, outside colonization, local population count, or simultaneous extinction catastrophe is modeled. In particular, after both patches become empty no revival is possible. Probabilities refer to persistence of at least one occupied patch, not occupancy of both.

All strict inequalities above refer to every real time \(t>0\); all rate assertions concern \(e>0\), \(\gamma>0\), and \(c\ge0\). The scaling by area is used only in comparing the two different numbers of reserves, and total protected area is identical across designs.

## Proof

Order the transient states of the two-reserve system as \(2\) occupied, then \(1\) occupied. The transient Markov generator is
\[
Q=\begin{pmatrix}-2d&2d\\c&-(c+d)\end{pmatrix}.
\]
Starting from \(2\) occupied, its survival function is \(S_2(t)=(1,0)e^{Qt}(1,1)^{\mathsf T}\). Its Laplace transform is
\[
\int_0^\infty e^{-zt}S_2(t)\,dt
=(1,0)(zI-Q)^{-1}(1,1)^{\mathsf T}
=\frac{z+c+3d}{z^2+(c+3d)z+2d^2},\qquad z\ge0.
\]
The denominator has distinct positive decay roots \(\alpha,\beta\), since its discriminant is \(c^2+6cd+d^2>0\). Partial fractions, or \(S_2(0)=1\) and \(S'_2(0)=0\), yield the displayed two-exponential law. Its hazard rate is
\[
h_2(t)=-\frac{S'_2(t)}{S_2(t)}
=\frac{\alpha\beta(1-z_t)}{\beta-\alpha z_t},
\qquad z_t=e^{-(\beta-\alpha)t}.
\]
Since
\[
h'_2(t)=\frac{\alpha\beta(\beta-\alpha)^2z_t}{(\beta-\alpha z_t)^2}>0
\]
for finite \(t\ge0\), its hazard increases strictly from \(h_2(0)=0\) toward \(\lim_{t\to\infty}h_2(t)=\alpha\). The one-reserve hazard is constantly \(e\). Hence the logarithmic survival advantage \(H(t)=\log(S_2(t)/S_1(t))\) has \(H(0)=0\), \(H'(t)=e-h_2(t)\), and \(H'(0)=e>0\).

If \(\alpha\le e\), then \(H'(t)>0\) for every finite \(t>0\), proving universal strict split superiority. If \(\alpha>e\), the derivative \(H'\) decreases strictly from positive to negative and crosses zero exactly once. Because
\[
H(t)=(e-\alpha)t+\log\frac{\beta}{\beta-\alpha}+o(1)
\quad(t\to\infty),
\]
we have \(H(t)\to-\infty\); after its unique maximum, the continuous \(H\) therefore crosses zero exactly once on \((0,\infty)\), with the claimed sign order.

To convert \(\alpha\le e\) to a simple recolonization criterion, substitute \(d=\delta e\) and \(z=e\) into the characteristic polynomial \(z^2-(c+3d)z+2d^2\). The unique solution giving the *smaller* root \(\alpha=e\) is \(c=e(2\delta^2-3\delta+1)=c_{\mathrm{tail}}\); indeed the other root then equals \(2\delta^2e>e\). Since \(\alpha\) decreases continuously and strictly as \(c\) increases (by its explicit formula or the characteristic equation), the classification follows, including the equality case.

Finally \(\mathbb E\tau_2=\int_0^\infty S_2(t)\,dt=(c+3d)/(2d^2)\) by setting \(z=0\) in the Laplace transform. Comparing this with \(1/e\) gives exactly \(c>c_{\mathrm{mean}}\). Direct subtraction gives \(c_{\mathrm{tail}}-c_{\mathrm{mean}}=e\), and \(c_{\mathrm{tail}}>0\) for every \(\delta>1\); the stated disagreement interval is consequently nonempty. The example satisfies the two strict threshold inequalities \(2e<c<3e\), completing the proof.

## Verification

Execute `python verify.py` with `sympy` and `mpmath`. The standalone checker reconstructs the transient generator and survival resolvent symbolically, tests the exact mean and threshold identities, then compares the closed-form survival probability against an independently calculated matrix exponential for \(30\) rational parameter pairs and five times each. It also checks tail-rate inequalities, mean ranking, and the example's crossing numerically. At packaging, the script completed with **401** passing assertions. These computations supplement, but do not replace, the universal monotone-hazard proof above. No numerical integration or finite sample is asserted to prove the all-parameter theorem.

## Relationship to prior work

Etienne and Heesterbeek (2000) develop the fixed-total-area reserve fragmentation question and explicitly use the reproduction/colonization potential and *mean* metapopulation extinction time as their persistence criteria. Their open full text establishes this motivation but the inspected main mathematical argument does not give a comparison of the complete one-versus-two extinction-time survival distributions with a unique horizon crossover. The present simple model is not their lattice model and makes its assumptions independently.

Nicol and Possingham (2010) address restoration choices under finite- and infinite-horizon stochastic dynamic programming; Helmstedt and colleagues (2014) study the costs of a large versus two small fenced reserves. These substantially overlap the policy motivation but have different optimization objectives and mechanisms. Only their accessible abstracts and indexing text were inspected, not all results and appendices, so possible earlier algebraic coverage cannot be ruled out. Trouillier and colleagues (2023) report simulation-based comparisons between multiple population viability metrics, reinforcing why rank disagreement matters; this analysis is not a substitute for a complete priority check. Exact two-patch mean-lifetime and recolonization-allocation calculations are established techniques. The narrow proposed contribution here is the *sharp all-horizon two-design comparison together with the fixed, strictly positive gap between its tail and mean thresholds*, not the Markov generator, its elementary mean formula, or the general concept of horizon-dependent rankings.

## Limitations

The conclusion concerns the stated independent, homogeneous, closed, two-state local occupancy process and the stipulated area–extinction scaling. Real reserve design includes correlations, costs, different initial occupancy, possible rescue before a patch is fully empty, finite dispersal distance, external immigration, larger habitat graphs, and stochastic individual demography. No statement about those omitted mechanisms or direct management optimality follows. In the crossover regime \(T_*\) has a unique implicit definition but no elementary closed-form expression is claimed. Originality is qualified by incomplete access to related full texts, particularly Nicol and Possingham (2010) and Helmstedt et al. (2014); independent historical-priority validation has not been performed.

## References

- R. S. Etienne and J. A. P. Heesterbeek (2000), *On Optimal Size and Number of Reserves for Metapopulation Persistence*, Journal of Theoretical Biology 203, 33–50, [doi:10.1006/jtbi.1999.1060](https://doi.org/10.1006/jtbi.1999.1060); [lawful repository full text](https://dspace.library.uu.nl/bitstream/1874/8099/1/heesterbeek_00_optimal_metapopulation.pdf).
- S. C. Nicol and H. P. Possingham (2010), *Should metapopulation restoration strategies increase patch area or number of patches?*, Ecological Applications 20, 566–581, [doi:10.1890/08-2216.1](https://doi.org/10.1890/08-2216.1).
- K. J. Helmstedt, H. P. Possingham, K. E. C. Brennan, J. R. Rhodes and M. Bode (2014), *Cost-efficient fenced reserves for conservation: single large or two small?*, Ecological Applications 24, 1780–1792, [doi:10.1890/13-1579.1](https://doi.org/10.1890/13-1579.1).
- A. Trouillier et al. (2023), *A comparison of population viability measures*, Ecology and Evolution 13, [doi:10.1002/ece3.9752](https://doi.org/10.1002/ece3.9752).
