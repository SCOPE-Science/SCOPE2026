# Exact two-cycle census for synchronous majority on wheel graphs

## Finding
For every integer \(n\ge3\), let \(W_n=K_1\vee C_n\) denote the simple wheel with **\(n\) labelled rim vertices** and one hub. In synchronous binary open-neighbor majority dynamics, vertices adopt the strict majority of their neighbors, retaining their present bit on a tie. The only fixed configurations are the two constant configurations, and the complete primitive two-cycle census is as follows.

For each integer \(m\ge2\), put
\[
R_m(z,w)=1+z^m w^m+\sum_{k=1}^{\lfloor m/3\rfloor}\;\sum_{j=2k}^{m-k}
\frac{m}{k}\binom{j-k-1}{k-1}\binom{m-j-1}{k-1}
 z^j w^{j-k}.
\]
Define \(B_n(z,w)=R_n(z,w)\) when \(n\) is odd and \(B_n(z,w)=R_{n/2}(z,w)^2\) when \(n\) is even. Then the **exact number of distinct labelled temporal two-cycles** is
\[
\boxed{\mathcal C_n(2)=2\mathbf 1_{\{2\mid n\}}+
\sum_{\substack{j,e\ge0\\2j>n,\;2e<n}}[z^j w^e]B_n(z,w).}
\]
There are exactly \(2\) fixed configurations; hence exactly \(2+2\mathcal C_n(2)\) configurations already on periodic orbits. By the general period-two theorem for symmetric threshold dynamics, no other least periods occur eventually. The formula concerns **already periodic** configurations and **distinct temporal orbits**, not their basins.

The two-cycle decomposition is sharp: for even \(n\), exactly two primitive cycles keep the hub fixed and the rest alternate the hub; for odd \(n\), every primitive two-cycle alternates the hub.

The fraction of initially uniformly sampled configurations **already periodic** is exponentially small in \(n\), despite the exponential growth of the absolute number of two-cycles along explicit infinite subsequences. More precisely, for odd \(n\) the fraction is at most \((7/8)^{\lfloor n/3\rfloor}+2^{-n}\), while for even \(n\) it is at most \((7/8)^{2\lfloor n/6\rfloor}+3\cdot2^{-n}\). For odd positive \(\ell\), \(\mathcal C_{7\ell}(2)\ge\binom{2\ell}{\ell}\); for every positive \(\ell\), \(\mathcal C_{14\ell}(2)\ge\binom{2\ell}{\ell}^2\).

## Assumptions and scope
Rim vertices are indexed \(i\in\mathbb Z/n\mathbb Z\), with edges to \(i-1\), \(i+1\), and the hub, and the hub is joined to all \(n\) rim vertices. All configurations are labelled binary assignments. Let the rim bits be \(x=(x_i)\in\{0,1\}^n\) and the hub bit be \(h\in\{0,1\}\). The update acts simultaneously at every vertex and ties retain the bit already held. All parameter ranges include the exceptional four-rim wheel; in the skip-two description below, a cycle of length two is a **two-edge multicycle for edge counting only**. All coefficients are exact integers. The convention \(\binom ab=0\) is used outside the usual integer range.

## Proof
**1. Local update and hub threshold.** At rim site \(i\), the three neighbors are the hub and the two cyclic rim neighbors. If the hub is zero, the updated rim is
\[
y_i=x_{i-1}x_{i+1}.
\]
If the hub is one, the updated rim is
\[
y_i=x_{i-1}\vee x_{i+1}.
\]
Writing \(j=\sum_i x_i\), the new hub is one if \(2j>n\), zero if \(2j<n\), and keeps \(h\) in case of equality.

**2. Alternating hub.** In a putative two-cycle whose first hub state is zero and whose second hub state is one, the first rim update is \(y_i=x_{i-1}x_{i+1}\) and the second must satisfy
\[
x_i=y_{i-1}\vee y_{i+1}=x_i(x_{i-2}\vee x_{i+2}).
\]
This holds precisely when every occupied rim site has another occupied site at distance two. Moreover, \(e=\sum_i y_i=\sum_i x_{i-1}x_{i+1}\), and both hub flips occur precisely when \(2j>n\) and \(2e<n\). Thus these three conditions are **necessary and sufficient**, with no appeal to numerical enumeration. Every such primitive cycle has a unique state with hub zero; hence counting these \(x\) counts the cycles once.

**3. Fixed hub.** If the hub remains zero throughout a two-step orbit, the rim equation becomes
\[
x_i=y_{i-1}y_{i+1}=x_{i-2}x_i x_{i+2}.
\]
Consequently every occupied site forces occupancy throughout its connected component of the step-two rim graph. When \(n\) is odd, that graph is connected; zero occupancy gives the all-zero fixed point, while full occupancy forces the hub to switch and is inadmissible. When \(n\) is even, there are exactly two components, the parity classes. Exactly one occupied parity class gives the alternating rim two-cycle (and the hub remains zero by the tie rule); neither gives the all-zero fixed point; both would force a hub switch. Thus hub-zero stationary cycles comprise one fixed point and, when \(n\) is even, one primitive two-cycle. Complementing all bits gives the hub-one cases and the all-one fixed point. This proves the fixed count and the additive \(2\mathbf 1_{\{2\mid n\}}\) term.

**4. Exact cyclic-run count.** Consider a cyclic binary word of length \(m\ge2\) with no isolated ones. Let \(j\) be its number of ones, and \(e\) its number of adjacent ordered one-one pairs, counting one pair per cyclic edge position (two positions when \(m=2\)). The all-zero and all-one words contribute \(1\) and \(z^mw^m\). Every other word has \(k\) maximal one-runs of lengths at least two, separated by \(k\) zero-runs of lengths at least one. Hence \(2k\le j\le m-k\), and \(e=j-k\). The positive compositions of the one-run lengths and zero-run lengths number \(\binom{j-k-1}{k-1}\) and \(\binom{m-j-1}{k-1}\). There are \(m\) locations for a distinguished run start; dividing by the \(k\) choices of distinguished run in each labelled word gives the coefficient \(\frac m k\binom{j-k-1}{k-1}\binom{m-j-1}{k-1}\). Thus \(R_m\) enumerates exactly these words by \((j,e)\), including \(m=2\).

The step-two rim graph has one cyclic component of length \(n\) if \(n\) is odd, and two of length \(n/2\) if \(n\) is even. Under these component orderings, the no-isolation criterion and the \((j,e)\) statistics in Step 2 are exactly those counted by \(B_n\). Extracting terms satisfying the two strict hub inequalities therefore counts precisely the hub-alternating cycles. Combining with Step 3 proves the boxed formula.

**5. Rarity and nontrivial growth.** Every admissible component word avoids the local length-three pattern \(010\). Partitioning an \(m\)-word into \(\lfloor m/3\rfloor\) disjoint triples and at most two remaining positions yields \(R_m(1,1)\le2^m(7/8)^{\lfloor m/3\rfloor}\). Use \(\mathcal C_n(2)\le B_n(1,1)+2\mathbf 1_{\{2\mid n\}}\) and the exact two-fixed-point count to obtain the two probability bounds. For a lower bound, take a cyclic component word composed of exactly \(\ell\) blocks \(110\) and \(\ell\) blocks \(1110\), in arbitrary fixed-start order. These \(\binom{2\ell}{\ell}\) distinct words have length \(7\ell\), exactly \(5\ell\) ones, and exactly \(3\ell\) adjacent one-one pairs; all one-runs have length at least two. For odd \(\ell\), the single skip-two component on \(W_{7\ell}\) gives the first lower bound. On \(W_{14\ell}\), choose such a word independently for the two skip-two components, proving the squared lower bound.

## Verification
The standalone scripts `code/wheel_majority_brute.py` and `code/wheel_run_census.py` use only the Python standard library. Run them as `python code/wheel_majority_brute.py` and `python code/wheel_run_census.py` from the package root. The first constructs graph neighbor lists and checks every state for rim lengths \(3\) through \(17\), totalling **524,272 labelled configurations**; the second evaluates the independent binomial run formula for rim lengths \(3\) through \(60\) and directly enumerates the component cyclic-word polynomial for lengths \(2\) through \(13\). Captured deterministic outputs are `reports/brute_output.txt` and `reports/run_output.txt`.

For \(n=3,4,5,6,7,8,9,10,11,12\), the counts of distinct primitive two-cycles are respectively \(3,2,5,11,21,34,66,77,220,227\). The two methods agree on every tested size, but the infinite claim rests on the structural proof in Steps 1–5.

## Relationship to prior work
The general eventual-period-at-most-two statement is the classical symmetric-threshold theorem of Goles and Olivos and is **not** a new assertion. Benjamini et al. describe this finite-graph theorem explicitly while studying unimodular and random graphs, rather than the wheel orbit count. Agur, Fraenkel, and Klein derive cyclic-word counts for one-dimensional self-inclusive majority; their article explicitly restricts its graph model to a simple ring and leaves general graphs open. This classical cyclic counting is not claimed new. Turau obtains structural classifications for trees, which wheels are not. Nakar and Ron study one-dimensional majority automata with fixed-radius neighborhoods and no globally updating hub. Aledo et al. count periods for MAX/MIN Boolean operators, not the nonlinear majority operator used here. The new statement is the exact wheel-specific labelled two-cycle census and its fixed-hub/alternating-hub decomposition, together with resulting rarity and exponential-subsequence consequences. These distinctions compare mathematical conclusions, not publication titles.

## Limitations
The theorem does not enumerate transient-entry times or attraction basin sizes. The source of the classical general period bound was accessible only through bibliographic and abstract material; its publisher full text was not obtained. A precise equivalent wheel enumeration in unpublished or unindexed literature cannot be definitively excluded. Finite computations corroborate, but do not establish, the all-size statement.

## References
- E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189. DOI: https://doi.org/10.1016/0012-365X(80)90121-1.
- I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, first arXiv version dated 2014-05-11: https://arxiv.org/abs/1405.2486.
- Z. Agur, A. S. Fraenkel, and S. T. Klein, *The number of fixed points of the majority rule*, Discrete Mathematics 70 (1988), 295–302: https://u.cs.biu.ac.il/~tomi/Postscripts/majority.pdf.
- V. Turau, *Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees*, 2022: https://arxiv.org/abs/2202.01580.
- Y. Nakar and D. Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata*, 2022: https://arxiv.org/abs/2205.08972.
- J. A. Aledo et al., *Counting Periodic Points in Parallel Graph Dynamical Systems*, Complexity (2020), article 9708347: https://doi.org/10.1155/2020/9708347.
