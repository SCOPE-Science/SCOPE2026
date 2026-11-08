# Numerical index three quarters for the first noncyclic odd theta graph

## Finding
Let \(G\) be the simple unit-edge graph with vertices \(0,1,2,3,4,5\) and three internally disjoint paths between \(0\) and \(1\): \(0-2-1\), \(0-3-1\), and \(0-4-5-1\). Give its vertices the shortest-path metric. For the **real** Lipschitz-free space \(X=\mathcal F(G)\), the exact numerical index is
\[
\boxed{n(X)=\frac34.}
\]
Equivalently, every real linear operator \(T:X\to X\) satisfies \(v(T)\ge\frac34\|T\|\), and a rank-one operator attains equality. The graph is the theta graph with arm lengths \(2,2,3\), containing one four-cycle and two five-cycles, not a single cycle.

## Assumptions and scope
All Banach spaces and operators are real. Put \(\delta_0=0\); then \(X\) has basis \(\delta_1,\ldots,\delta_5\), and the seven unit edge molecules are
\[
m_{02}=\delta_0-\delta_2,\quad m_{21}=\delta_2-\delta_1,\quad m_{03}=\delta_0-\delta_3,\quad m_{31}=\delta_3-\delta_1,\quad m_{04}=\delta_0-\delta_4,\quad m_{45}=\delta_4-\delta_5,\quad m_{51}=\delta_5-\delta_1.
\]
By shortest-path decomposition, the closed unit ball is the convex hull of these seven molecules and their negatives. The dual unit ball is the Lipschitz polytope
\[
F=\{f=(f_0,\ldots,f_5): f_0=0,\ |f_a-f_b|\le1\text{ for each graph edge }ab\}.
\]
The numerical radius is \(v(T)=\sup\{|f(Tx)|:\|x\|=\|f\|=1,\ f(x)=1\}\), and \(n(X)=\inf_{\|T\|=1}v(T)\).

## Proof
**Reduction to finite vertices.** The edge-difference matrix is a graph incidence matrix and is totally unimodular. Hence all extreme points of \(F\) have integer coordinates. A feasible point \(f\) is extreme precisely when the edges satisfying \(|f_a-f_b|=1\) connect all six vertices: the active edge normals span the rooted five-dimensional dual space precisely under that connectivity condition. The shortest-path distance bounds give \(-d(0,j)\le f_j\le d(0,j)\) for each \(j\). Thus the explicit finite enumeration in `verify_theta.py` is exhaustive and yields exactly \(54\) dual extreme points.

For each oriented edge \(e=(a,b)\), let \(F_e\) be the extreme dual points satisfying \(f_a-f_b=1\). In the edge order displayed above their cardinalities are \(21,21,21,21,22,22,22\). The exact rational certificate `theta_certificate.json` proves the following **simultaneously for every** oriented edge and every dual extreme point \(f\):
\[
\frac34 f\ \in\ \operatorname{conv}(F_e\cup(-F_e)).\tag{1}
\]
Indeed, when \(f_a-f_b\) equals \(\pm1\), membership is immediate because \(\tfrac34 f\) is a convex combination of \(f\) and the origin; the origin belongs to the symmetric convex hull. When \(f_a-f_b=0\), the certificate explicitly lists a positive rational convex combination of signed points in \(F_e\) equal to \(\tfrac34 f\). The checker re-enumerates all extreme dual points independently of the certificate and verifies exact integer and rational equalities for all \(78\) such nontrivial cases, involving \(334\) rational summands. Since \(F\) is the convex hull of its extreme points, (1) holds for all \(f\in F\). Therefore, for any \(y\in X\) and every edge \(e\),
\[
\max_{f\in F_e}|f(y)|\ \ge\ \frac34\|y\|.\tag{2}
\]
A norm-one edge molecule is extreme in the unit ball: its endpoints are distance one, with no distinct vertex on their metric segment. For every operator \(T\), \(\|T\|=\max_e\|T m_e\|\). Each \(f\in F_e\) is norming for \(m_e\); hence (2) implies
\[
v(T)\ge \max_e\max_{f\in F_e}|f(Tm_e)|\ge\frac34\max_e\|Tm_e\|=\frac34\|T\|.
\]

**Sharp rank-one witness.** In the rooted coordinates \((\delta_1,\ldots,\delta_5)\), let \(y=(0,1,0,0,-2)\), and let the real functional \(\ell\) have coordinate values \((-1/4,-1,-3/4,3/4,0)\). It has \(\|\ell\|=1\) since the largest of its absolute edge differences is one. Set \(T(x)=\ell(x)y\). Exact dual enumeration gives \(\|y\|=4\). The seven face maxima \(\max_{f\in F_e}|f(y)|\) are \((3,4,4,4,4,4,4)\), while the edge values \(\ell(m_e)\) are \((1,-3/4,3/4,-1/2,-3/4,3/4,1/4)\). Hence \(\|T\|=4\) and \(v(T)=3\), so \(n(X)\le3/4\), completing the equality.

## Verification
Run `python verify_theta.py theta_certificate.json` with Python 3 standard library only. Expected output starts `THETA_INDEX_EXACT_OK`. The checker verifies the graph and the complete dual-vertex enumeration, every rational convex identity in (1), all face cardinalities, and the sharp rank-one witness with exact fractions. It outputs `dual_extremes 54 convex_certificates 78 rational_terms 334` and `norm 4 radius 3 index 3/4`. The convex-hull and operator reductions above are finite-dimensional theorems, so the exact certificate proves the universal inequality for **all** real operators, not only sampled matrices.

## Relationship to prior work
Pal, Roy and Sain (2026) characterize numerical index one for general Banach spaces and discuss extremal numerical-radius geometry; that theorem does not compute the nonunit value here. Cobollo, Guirao and Montesinos (2023) solve the numerical index for two-dimensional Lipschitz-free spaces, not this five-dimensional example. Published exact results for simple odd cycles include \(n(\mathcal F(C_5))=3/4\), while a recent universal graph inequality gives only \(n(\mathcal F(G))\ge1/2\); neither implies the present result for a theta graph with two independent cycles. The coincidence of this new theta index with the five-cycle index is a genuine comparison, not a claim that the cycle result was unknown.

## Limitations
The result concerns only the stated six-vertex unit-edge theta metric, over the real field. It does not classify all theta graphs, weighted graphs, or complex free spaces. The exact finite certificate is independently replayable but does not establish publication priority; more general historical theorems could potentially imply the particular value. Independent mathematical review has not been performed.

## References
1. S. Pal, S. Roy and D. Sain, *A characterization of Banach spaces with numerical index one*, arXiv:2604.03690v1 (first public 2026-04-04), https://arxiv.org/abs/2604.03690.
2. Ch. Cobollo, A. J. Guirao and V. Montesinos, *The numerical index of 2-dimensional Lipschitz-free spaces*, arXiv:2304.13183 (2023), https://arxiv.org/abs/2304.13183.
3. R. J. Smith, *A Choquet theory of Lipschitz-free spaces*, Proceedings of the London Mathematical Society (first published 2026-02-10), DOI: 10.1112/plms.70125.
4. Published mathematical result, *Numerical index three quarters for the five-cycle Lipschitz-free space* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-numerical-index-three-quarters-for-the-five-cycle-lipschitz-free--9240f2c24bdf.
5. Published mathematical result, *A sharp universal half bound for numerical indices of finite graph free spaces* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-universal-half-bound-for-numerical-indices-of-finite-gra--166e28e756ad.
