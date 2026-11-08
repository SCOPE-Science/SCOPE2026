# A quarter-power jamming law for random three-site adsorption on complete bipartite networks

## Finding

On a complete bipartite graph, irreversibly deposit a three-site object on a uniformly selected available length-two path, occupying its three vertices. Let \(A_m,B_m\) be the initial numbers of sites in its two parts, let \(m=A_m+B_m\to\infty\), and let \(R_m\) be the total number of sites remaining unoccupied at jamming. Every distinct three-vertex path is assigned the same independent continuous exponential attempt clock; overlapping attempted objects are rejected.

**Critical window.** For every real \(\mu\), if
\[
\frac{A_m-B_m}{\sqrt m}\longrightarrow\mu,
\]
then, with \(Z\) standard normal,
\[
\boxed{\frac{R_m}{m^{1/4}}\ \xrightarrow{\mathrm d}\ |Z+\mu|^{3/2}.}
\]
In particular a balanced network has a nondegenerate quarter-power jamming vacancy law. The identity of the surviving part converges to the sign of \(Z+\mu\), interpreted as the part with excess initial sites when the sign is positive.

**Macroscopic imbalance.** If instead \((A_m-B_m)/m\to\delta\) for a fixed \(\delta\in(-1,0)\cup(0,1)\), then
\[
\boxed{\frac{R_m}{m}\ \xrightarrow{\mathbb P}\ |\delta|^{3/2}.}
\]
The first formula describes the critical boundary layer of the second. These are limits of a specified finite Markov adsorption model, not claims about spatially local two-dimensional substrates.

## Assumptions and scope

The substrate is the simple undirected complete bipartite graph \(K_{A_m,B_m}\), not a square lattice. An adsorbate occupies the three *vertices* of a path of two edges; a path and its reversal are the same object. Each distinct three-vertex path has independent rate-one exponential attempts. An attempt succeeds exactly when all its sites are vacant. The construction is equivalent to repeatedly choosing uniformly among currently available paths, because of exponential memorylessness. Both site populations diverge in each stated regime. The two-part critical asymmetry parameter \(\mu\) is finite and the macroscopic imbalance parameter satisfies \(0<|\delta|<1\).

Let \(a,b\) be current unoccupied counts, \(s=a+b\), and \(d=a-b\). If \(a,b\ge1\) and \(s\ge3\), there are \(a\binom b2\) paths with one site from the first part and \(b\binom a2\) with two sites from the first part. Thus their counts determine the entire embedded chain:
\[
\begin{split}
(a,b)&\mapsto(a-1,b-2)\quad\text{with probability }\frac{b-1}{s-2},\\
(a,b)&\mapsto(a-2,b-1)\quad\text{with probability }\frac{a-1}{s-2}.
\end{split}
\]
Zero-numerator moves are absent. The chain jams precisely when one part is empty or \(s<3\). Each successful adsorption decreases \(s\) by three.

## Proof

**Step 1: exact imbalance drift and normalization.** Write \(d_j\) for the imbalance after \(j\) successful adsorptions and \(s_j=m-3j\) for the deterministic total at that step. The increment \(\xi_j=d_{j+1}-d_j\) equals either \(1\) or \(-1\); the preceding transition law gives
\[
\mathbb E(\xi_j\mid\mathcal F_j)=-\frac{d_j}{s_j-2},\qquad
\operatorname{Var}(\xi_j\mid\mathcal F_j)=1-\frac{d_j^2}{(s_j-2)^2}.
\]
For deterministic levels at least four let \(h_0=1\) and
\[
h_{j+1}=h_j\frac{s_j-3}{s_j-2}.
\]
Stop the process upon jamming or on reaching a total of at most three, whichever comes first; this changes final occupancy by at most three. Before that stopping time, \(M_j=d_j/h_j\) is a martingale, and
\[
\Delta M_j=\frac{\xi_j+d_j/(s_j-2)}{h_{j+1}},\qquad
\mathbb E((\Delta M_j)^2\mid\mathcal F_j)
=\frac{1-d_j^2/(s_j-2)^2}{h_{j+1}^2}.
\]
The martingale is kept constant after stopping. As \(m\to\infty\), uniformly over levels \(s_j\to\infty\),
\[
 h_j=\left(\frac{s_j}{m}\right)^{1/3}
\left(1+O(s_j^{-1})\right).
\]
Indeed the logarithms of the products differ from one-third of the telescoping logarithm \(\log(s_j/m)\) by \(O(\sum_{s\ge s_j}s^{-2})=O(s_j^{-1})\), since the levels decrease in steps of three.

**Step 2: Gaussian imbalance at a mesoscopic level.** For the critical window choose the first level \(s_j\) no greater than \(m^{1/2}\), denoted \(s_c\). Early absorption before that level has probability tending to zero. To see this, the martingale second moment up to \(s_c\) is \(O(m)\), since
\[
\sum_{s_j\ge s_c}\frac1{h_{j+1}^2}=O(m).
\]
Absorption at a level \(s\ge s_c\) requires \(|d|=s\), hence \(|M|\ge c m^{1/3}s_c^{2/3}\); Doob's inequality bounds the probability of this event by \(O(m^{1/3}s_c^{-4/3})=o(1)\). The \(s<3\) stopping condition cannot occur this early.

The deterministic sum of reciprocal squared normalizers obeys
\[
\frac1m\sum_{s_j\ge s_c}\frac1{h_{j+1}^2}\longrightarrow1.
\]
The conditional-variance correction is negligible: \(\mathbb E(M_j^2)=O(m)\) uniformly up to the cutoff, and, since \(h_j/h_{j+1}\) is bounded there,
\[
\frac1m\sum_{s_j\ge s_c}
\mathbb E\left[\frac{d_j^2}{(s_j-2)^2h_{j+1}^2}\right]
\le C\sum_{s_j\ge s_c}s_j^{-2}=o(1).
\]
The martingale increments satisfy \(|\Delta M_j|\le2/h_{j+1}=o(\sqrt m)\) in this range, so the martingale central limit theorem gives
\[
\frac{M_{j_c}}{\sqrt m}\xrightarrow{\mathrm d}Z+\mu.
\]
A stopped-chain version makes the same conclusion valid without conditioning on survival to the cutoff, because that conditioning changes probability by \(o(1)\).

**Step 3: negligible late stochastic fluctuations.** Below \(s_c\) and down to level three, the predictable quadratic variation is bounded deterministically by
\[
\sum_{4\le s_j\le s_c,\,s_{j+1}\ge1}h_{j+1}^{-2}
=O(m^{2/3}s_c^{1/3})=o(m),
\]
with the final transition to zero omitted. Doob's inequality therefore shows that, uniformly through the stopped process, the further change of \(M/\sqrt m\) is \(o_{\mathbb P}(1)\). Let \(\widetilde R_m\) be the total at this stopping time. For any fixed \(0<\varepsilon<1/4\), \(\mathbb P(\widetilde R_m\le m^\varepsilon)\to0\): if the chain passed below that scale without earlier absorption, at that scale \(|d|\le s\), implying
\[
\frac{|M|}{\sqrt m}\le C\left(\frac{s}{m^{1/4}}\right)^{2/3}\longrightarrow0,
\]
which contradicts convergence of \(M/\sqrt m\) to the continuously distributed \(Z+\mu\), except on an event with vanishing probability. Thus with probability tending to one the actual terminal state occurs at \(R_m\to\infty\), is a one-part state, and satisfies \(|d|=R_m\). At that state, the martingale normalization gives
\[
\frac{M}{\sqrt m}
=\operatorname{sgn}(d)
\left(\frac{R_m}{m^{1/4}}\right)^{2/3}(1+o_{\mathbb P}(1)).
\]
Inverting this continuous signed relationship proves the asserted quarter-power limit and the survivor-side sign law. It also proves that the probability of exceptional terminal configurations with only two or fewer sites tends to zero.

**Step 4: macroscopic imbalance.** If \(d_0/m\to\delta\ne0\), for every fixed \(\epsilon>0\) the stopped martingale has \(M_j=d_0+O_{\mathbb P}(\sqrt m)\) uniformly over the levels \(s_j\ge\epsilon m\). Consequently \(d_j/m\) converges uniformly there to \(\delta(s_j/m)^{1/3}\). This deterministic curve first reaches the admissibility boundary \(|d_j|=s_j\) at the unique positive fraction \(s_j/m=|\delta|^{3/2}\). Sandwiching between levels just above and just below this crossing and using the uniform approximation yields \(R_m/m\to|\delta|^{3/2}\) in probability.

## Verification

The standalone Python standard-library program `verify.py` checks two independently implemented finite-state formulations: exact rational dynamic programming on all labeled subsets of \(K_{a,b}\) and exact rational dynamic programming on the pair of vacant counts. They agree on the full terminal-vacancy distribution for each \(1\le a,b\le4\) (16 separate comparisons). Exact conditional-drift and variance identities are additionally tested for 9,798 count states. Seeded simulations at larger sizes illustrate, but do not certify, convergence. Execute `python3 verify.py` from the same directory. The all-size limit relies on the argument above, not on simulation.

## Relationship to prior work

Lebovka, Karmazina, Tarasevich and Laptev (arXiv:1109.3271, submitted 2011-09-15) study partially oriented linear adsorbates on square lattices, with numerical finite-size effects and anisotropic jamming. Their substrate, paths and occupancy law are different; the present process instead has all length-two paths on a complete bipartite network, leading to an exact two-count chain. Bennett and Bohman (arXiv:1210.3581, submitted 2012-10-12) give general upper bounds for vacancies in random greedy matchings of regular uniform hypergraphs; their theorem does not identify the exact quarter-power law or its Gaussian-power limiting distribution for this particular regular three-uniform hypergraph. Penrose and Sudbury (arXiv:math/0503519, submitted 2005-03-24) give graph-adsorption results for monomers and dimers, not this three-site path model. General random greedy matching and stochastic approximation tools are prior mathematical machinery. No claim is made that those tools, or the complete bipartite graph, are new.

## Limitations

The theorem applies to independent equal-rate path clocks and to the specified complete bipartite substrates; it is not an assertion about orientation-biased rates, planar lattice geometry or unequal path weights. For a critical initial bias the theorem gives convergence in distribution, not a pointwise or total-variation error rate and not an expectation asymptotic. The proof controls the infinite-size limiting process but does not enumerate every finite labeled jamming state in closed form. Searches did not find an explicit previously published identical distributional law, but this cannot establish absolute priority. Historical articles on bent-trimer adsorption and general random greedy hypergraph matchings may contain overlooked specializations.

## References

1. N. I. Lebovka, N. N. Karmazina, Y. Y. Tarasevich, V. V. Laptev, *Random sequential adsorption of partially oriented linear k-mers on square lattice*, arXiv:1109.3271v1, 2011-09-15, https://arxiv.org/html/1109.3271v1.
2. P. Bennett and T. Bohman, *A natural barrier in random greedy hypergraph matching*, arXiv:1210.3581, 2012-10-12, https://arxiv.org/abs/1210.3581.
3. M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, arXiv:math/0503519, 2005-03-24, https://arxiv.org/abs/math/0503519.
4. J. Cortés and E. Valencia, *Random sequential adsorption kinetics of dimers and trimers on geometrically disordered substrates*, Journal of Colloid and Interface Science 252 (2002), 256–258, https://doi.org/10.1006/jcis.2002.8443.
