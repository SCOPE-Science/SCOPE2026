# Four-corner Poisson geometry and induced subgraphs of extremal permutation-graph degrees

## Finding
Let \(\pi\) be a uniformly chosen permutation of \(\{1,\ldots,n\}\). Its inversion graph \(G_n\) has vertices \(1,\ldots,n\) and an edge \(\{i,j\}\), \(i<j\), precisely when \(\pi(i)>\pi(j)\). Write \(d_i\) for its degrees. For fixed \(t>0\), define the low- and high-extremal vertex sets
\[
V_n^-(t)=\{i:d_i\le t\sqrt n\},\qquad
V_n^+(t)=\{i:n-1-d_i\le t\sqrt n\}.
\]
To each selected vertex attach its row tag \(L\) or \(R\), column tag \(B\) or \(T\), and coordinates
\[
x_i=\frac{\min\{i,n+1-i\}}{\sqrt n},\qquad
y_i=\frac{\min\{\pi(i),n+1-\pi(i)\}}{\sqrt n}.
\]
Tags are determined by whether the row or column lies in the lower or upper half of \(\{1,\ldots,n\}\). For any fixed \(t>0\), the entire *marked induced graph* on \(V_n^-(t)\cup V_n^+(t)\) converges in distribution to the following finite random marked graph:

Take four **independent**, unit-intensity planar Poisson processes, labelled \(LB,LT,RB,RT\), each restricted to the triangle
\[
\Delta_t=\{(x,y):x\ge0,\ y\ge0,\ x+y\le t\}.
\]
Points tagged \(LB\) and \(RT\) are low-degree vertices; points tagged \(LT\) and \(RB\) are high-degree vertices. For any two points, join them if and only if their row and column orderings disagree. The row ordering puts all \(L\) tags before all \(R\) tags, sorts \(L\)-points by increasing \(x\), and sorts \(R\)-points by decreasing \(x\). The column ordering puts all \(B\) tags before all \(T\) tags, sorts \(B\)-points by increasing \(y\), and sorts \(T\)-points by decreasing \(y\). Almost surely there are no ordering ties. Convergence is in the natural topology on finite tagged point configurations with their induced adjacency matrices, identifying configurations by their tag and coordinates.

In particular, the four tagged counts converge jointly to independent \(\operatorname{Poisson}(t^2/2)\) variables; the total number of low-degree and high-degree vertices converge to independent \(\operatorname{Poisson}(t^2)\) variables. Consequently the \(k\)-th smallest degree divided by \(\sqrt n\) and the \(k\)-th smallest complementary-degree deficit divided by \(\sqrt n\) converge jointly to independent \(\sqrt{\operatorname{Gamma}(k,1)}\) variables, for each fixed positive integer \(k\), and jointly across all finite selections of such ranks.

The induced graph is not a featureless Poisson vertex count: \(LB\)-to-\(RT\) edges are absent, \(LT\)-to-\(RB\) edges are complete, and the within-corner connection probabilities for two uniformly chosen triangle points are \(2/3\) in either low corner and \(1/3\) in either high corner. Hence, writing \(E_t^-\) and \(E_t^+\) for the numbers of induced low–low and high–high edges in the limiting graph,
\[
\mathbb E E_t^- = \frac{t^4}{6},\qquad
\mathbb E E_t^+=\frac{t^4}{3}.
\]
These are different despite identical limiting Poisson laws for the two extremal vertex counts.

## Assumptions and scope
The only randomness is uniform sampling from all \(n!\) permutations. Degree is the *ordinary* graph degree and high-degree deficit means \(n-1-d_i\). The parameter \(t\) and every compared rank \(k\) remain fixed as \(n\to\infty\). For sufficiently large \(n\), the low- and high-degree sets are disjoint. The statements are distributional, not almost-sure couplings and not quantitative total-variation error bounds. Points on any deterministic line \(x+y=t\) have limiting probability zero.

## Proof
**1. Joint Poisson convergence at all four corners.** For each tag \(c\in\{LB,LT,RB,RT\}\), consider the point measure of *all* permutation matrix cells near that corner under the displayed rescaling. Fix finitely many disjoint bounded rectangles across the disjoint union of these four tagged quadrant planes. The eligible permutation-matrix cells in each rectangle number \(n\) times its Euclidean area, plus \(O(\sqrt n)\). Every row or column meets at most \(O(\sqrt n)\) eligible cells in their union. Thus, for any fixed total factorial order \(r\), among \(O(n^r)\) ordered \(r\)-tuples of candidate cells, only \(O_r(n^{r-1/2})\) have an invalid repeated row or column. Each valid prescribed \(r\)-tuple is present with exact probability \(1/(n)_{\underline r}\). Joint factorial moments of counts in disjoint rectangles therefore converge to products of their areas. Moment determinacy and local tightness prove convergence of the *four* tagged processes to independent intensity-one Poisson point processes. In particular, their restrictions to \(\Delta_t\) are finite almost surely.

**2. Degrees at prescribed permutation cells.** If \(\pi(i)=j\), put \(a=i-1\), \(b=j-1\), and \(N=n-1\). Let \(K\) count earlier rows whose column is less than \(j\). Conditioned on \(\pi(i)=j\), \(K\) is hypergeometric with population size \(N\), \(b\) successes and sample size \(a\), and the following exact identity holds:
\[
 d_i=a+b-2K. \tag{1}
\]
Indeed the left-neighbor contribution is \(a-K\); the right-neighbor contribution is \(b-K\). Simultaneously reversing the row and column orders preserves the inversion relation; complementing the column order changes inversion into non-inversion. Consequently the same identity, after one of these symmetries, holds for either \(d_i\) near the two diagonal corners or \(n-1-d_i\) near the two anti-diagonal corners, with nonnegative corner offsets \(a',b'\), corner score \(s=a'+b'\), and corresponding hypergeometric \(K'\):
\[
 D_i=s-2K',\qquad \mathbb E(D_i\mid\pi(i)=j)=s-\frac{2a'b'}N\ge\frac s2
 \quad(s\le N), \tag{2}
\]
where \(D_i\) denotes the appropriate degree or complementary deficit.

**3. No remote extreme vertices.** For each cell choose the relevant *nearest* diagonal corner (for ordinary degree) or nearest anti-diagonal corner (for complementary degree); its score satisfies \(s\le N\). If \(s>4t\sqrt n\), then \(D_i\le t\sqrt n\), together with (2), forces \(K'-\mathbb EK'\ge s/8\). Sampling-without-replacement Hoeffding bounds, with sample size at most \(s\), give
\[
\Pr(D_i\le t\sqrt n\mid\pi(i)=j)\le e^{-s/32}.
\]
(The bound is trivial when the sample size is zero.) A union bound over \(n\) sampled cells makes the chance of *any* remote extreme vertex at most \(n e^{-t\sqrt n/8}\), which tends to zero. Apply this to degrees and complementary deficits.

**4. Uniform corner approximation.** Every candidate extreme cell now lies, with probability tending to one, in a square of side \(O(\sqrt n)\) at a relevant corner. Within such a corner, all relevant \(K'\) in (2) are bounded by the *number of sampled permutation cells in that corner square*. Its expectation is \(O_t(1)\), so the maximum of these \(K'\) values is \(O_{\Pr}(1)\). Therefore, uniformly over all near-corner cells,
\[
 \left|D_i/\sqrt n-(x_i+y_i)\right|\xrightarrow{\Pr}0.
\]
Combining the four-corner point-process limit with the zero limiting mass on the boundary of \(\Delta_t\) proves that selection by extremal degree, rather than corner score, makes no difference to the limiting marked configuration.

**5. Exact recovery of the induced graph.** For any two selected rows, their original index order is *exactly* the row ordering specified by tags and coordinates; likewise their original permutation-value order is exactly the specified column ordering. A pair is an inversion precisely when those orders disagree. Adjacencies are therefore deterministic functions of the marked configuration at every finite \(n\). The limiting Poisson process almost surely has distinct ordering coordinates; the finite marked-graph mapping is continuous there. This proves full induced-graph convergence, including the cross-population edges, not merely the vertex-count marginals.

**6. Edge means and ranked-degree consequences.** Each triangle has area \(t^2/2\). In a single triangle, two independent uniformly chosen points have discordant \(x,y\) ordering with probability \(2/3\): in the unit triangle, the area integral for one of the two discordant orientations equals \(1/12\); doubling and dividing by the square of the triangle area \(1/4\) gives \(2/3\). Within an \(LT\) or \(RB\) corner, the column coordinate reverses orientation, giving probability \(1/3\). Cross-corner low edges are absent; cross-corner high edges are complete. Since two independent Poisson counts of mean \(\lambda=t^2/2\) have mean product \(\lambda^2\), and each corner has expected unordered pair count \(\lambda^2/2\), the two displayed mean edge counts follow. Uniform bounded moments of bounded-corner cell counts, together with exponentially small probability of remote extreme vertices, ensure uniform integrability of the finite induced-edge counts, so the corresponding finite-n expectations converge to these limiting means. Finally, a Poisson process of rate one in total *score-squared time* has ordered score thresholds whose squares have consecutive unit-exponential gaps. Independent low/high corner fields yield the joint rank conclusion.

## Verification
Execute `python3 verify.py` in the same folder; no external Python packages are required. The checker exhaustively enumerates the 46,232 permutations of orders two through eight; it checks 725,756 exact degree/complementary-degree identities, 60,548 exact corner-coordinate inversion identities, and 14 exact moment identities. The successful execution reports `PASS permutations=46232; degree_identities=725756; corner_edge_identities=60548; exact_moment_identities=14`. This finite verification supports critical identities and implementations but does **not** prove the Poisson process, concentration, or asymptotic assertions; those depend on the analytic arguments above.

## Relationship to prior work
Bhattacharya and Mukherjee [1] establish the classical Rayleigh limit for the *single* minimum degree of a uniform permutation graph and analyze degree distributions; their arXiv manuscript was publicly available in March 2015 and their revised published text [2] was examined as the same underlying work. Consequently the marginal minimum-degree law is not claimed as new. A published 2026 study [3] establishes *two* independent Poisson corner clouds at the **anti-diagonal** corners together with a Gaussian inversion statistic, and implies some high-deficit marginal consequences. It does not state joint four-corner geometry or the induced random graph joining the low and high extremes. The present claim requires the simultaneous four-corner point process, the uniform degree-to-corner-score approximation, and the exact reconstruction of all induced edges; it yields nontrivial, different low/high extremal edge intensities. A more general earlier permutation-point process theorem could subsume parts of the result; the originality assessment is qualified by that residual possibility.

## Limitations
Uniformity of the permutation is essential. No assertion is made for Mallows or general permuton models, growing \(t\), growing ranks, quantitative rates, or local weak limits outside the finite extreme-vertex graph. The independent corner Poisson processes do *not* mean that edges within each type are independent; their dependence is determined by the shared point coordinates. The theorem has received a self-review, not independent validation. Historical priority is subject to additional scholarly checking.

## References
[1] B. B. Bhattacharya and S. Mukherjee, *Degree Sequence of Random Permutation Graphs*, arXiv:1503.03582v1, first posted 2015-03-12, https://arxiv.org/abs/1503.03582 (especially the minimum-degree analysis).

[2] B. B. Bhattacharya and S. Mukherjee, *Degree Sequence of Random Permutation Graphs*, published revised full text, https://sites.stat.columbia.edu/sumitm/perm_deg.pdf (same work as [1]).

[3] *Independent corner Poisson clouds and Gaussian inversion fluctuations*, publicly available mathematical result (2026-10-12), https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-independent-corner-poisson-clouds-and-gaussian-inversion-fluctua--14fa62567e42.
