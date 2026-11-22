# Sharp anisotropic variation amplification for isotonic regression on a four-point diamond

## Finding
Let \(Q:\mathbb R^4\to\mathbb R^4\) be the ordinary Euclidean least-squares isotonic projection for the four-point diamond \(0\prec1\prec3\) and \(0\prec2\prec3\). For every \(r>0\), define the weighted edge-variation seminorm
\[
 V_r(h)=r|h_1-h_0|+|h_2-h_0|+|h_3-h_1|+r|h_3-h_2|.
\]
Its **exact and attained two-input Lipschitz coefficient** is
\[
\boxed{\sup_{V_r(x-y)>0}\frac{V_r(Qx-Qy)}{V_r(x-y)}=\frac{1+\max\{r,r^{-1}\}}2.}
\]
Thus equal edge weights give sharp coefficient \(1\), while any anisotropy of this symmetric directional type produces strict amplification; the amplification grows without bound as \(r\to0\) or \(r\to\infty\).

## Assumptions and scope
The four inputs and outputs are arbitrary real vectors. The cone is
\[
\mathcal C=\{u\in\mathbb R^4:u_0\le u_1,\ u_0\le u_2,\ u_1\le u_3,\ u_2\le u_3\},
\quad Qx=\operatorname*{argmin}_{u\in\mathcal C}\sum_{i=0}^3(u_i-x_i)^2.
\]
The graph is the four-cycle formed by the undirected Hasse edges \((0,1),(0,2),(1,3),(2,3)\). The observation masses are all one. The two edges \((0,1),(2,3)\) have weight \(r\), while the other two have weight one. Variations count each undirected edge exactly once. This is the Lipschitz coefficient for **differences of two arbitrary projected signals**, not merely variation of a single projected signal.

## Proof
**1. Reduce the nonlinear projection to connected-block averaging.** The unique Euclidean metric projection onto the polyhedral cone \(\mathcal C\) is continuous and piecewise linear. On a full-dimensional active region, equality constraints pool some connected vertices; the derivative is the orthogonal averaging projection \(E_\mathcal B\) onto vectors constant on each resulting connected block \(B\), namely
\[
(E_\mathcal B h)_i=|B|^{-1}\sum_{j\in B}h_j\qquad(i\in B).
\]
An active partition is feasible with strict inequalities between distinct blocks exactly when contracting its equality edges leaves a directed acyclic graph; otherwise distinct connected blocks must also coincide. For the four-point diamond, enumerating the sixteen subsets of four Hasse edges and removing duplicate contractions yields precisely ten feasible connected-block partitions. For every one, a strict blockwise order assignment and small positive multipliers on a spanning forest of active edges produce a nonempty open projection region with the claimed derivative. The global difference \(Qx-Qy\) is an integral of such derivatives along the segment \([y,x]\). Therefore the global variation Lipschitz coefficient is at most the greatest \(V_r\)-operator norm over these ten averaging projections.

**2. Reduce every linear variation norm to binary cuts.** For any real \(h\), after subtracting its minimum and using the layer-cake identity,
\[
h=\min_i h_i\,\mathbf1+\int_{\min h}^{\max h}\mathbf1_{\{h>t\}}\,dt.
\]
Every block averaging projection fixes constants, and the triangle inequality for \(V_r\) gives
\[
V_r(E_\mathcal B h)\le\int V_r(E_\mathcal B\mathbf1_{\{h>t\}})\,dt.
\]
The graph coarea formula says \(V_r(h)=\int V_r(\mathbf1_{\{h>t\}})\,dt\). Consequently the exact norm of each averaging projection is the maximum of \(V_r(E_\mathcal B\mathbf1_S)/V_r(\mathbf1_S)\) over nonconstant zero-one vectors \(\mathbf1_S\).

**3. Exhaust the finite algebra symbolically.** For an arbitrary difference vector \(a\), write the variation as \(rA(a)+B(a)\), with
\[
A(a)=|a_1-a_0|+|a_3-a_2|,\qquad
B(a)=|a_2-a_0|+|a_3-a_1|.
\]
Across all ten feasible partitions and nonconstant Boolean cuts, the nonzero variation ratios, after exact rational simplification, belong to the following exhaustive nine functions:
\[
\frac1{r+1},\quad\frac13,\quad\frac r{r+1},\quad\frac{r+1}3,\quad\frac12,\quad1,\quad
\frac{r+1}2,\quad\frac{r+1}{3r},\quad\frac{r+1}{2r}.
\]
The complete enumeration is implemented in the accompanying standalone exact-rational program `verify.py`: it constructs all ten partitions from edge contractions, tests acyclicity, and computes every Boolean-cut numerator and denominator as a pair of rational coefficients of \(r\), identifying them by cross-multiplied polynomial identities. There are 118 nonzero output cases and no ratios outside the displayed set. For \(r\ge1\), each of the nine functions is bounded by \((r+1)/2\). This is an exhaustive finite algebraic certificate, not extrapolation from numerical samples. Thus
\[
V_r(Qx-Qy)\le\frac{r+1}{2}V_r(x-y)\qquad(r\ge1).
\]

**4. Attain the sharp coefficient with two genuine nonlinear inputs.** For \(r\ge1\) choose
\[
x=(1,1,-1,2),\qquad \delta=(0,0,1/4,1/4),\qquad y=x+\delta.
\]
The unique isotonic projections are
\[
Qx=(0,1,0,2),\qquad Qy=(1/8,1,1/8,9/4).
\]
Both project onto the same strict active face pooling exactly vertices \(0\) and \(2\); the active violation is strict and other cone inequalities are strict. Direct substitution yields \(V_r(\delta)=1/2\) and \(V_r(Qy-Qx)=(r+1)/4\). Their ratio equals \((r+1)/2\). For \(0<r<1\), interchanging the incomparable vertices \(1\) and \(2\) conjugates the cone and projection to themselves, while transforming \(V_r\) to \(rV_{1/r}\). Therefore the coefficient at \(r\) equals that at \(1/r\), establishing the asserted formula for all \(r>0\). At \(r=1\), the same pair witnesses coefficient one.

## Verification
Execute `python verify.py` using Python's standard library. The reproducible exact-rational checker generates all ten feasible active partitions, all 118 nonzero Boolean-cut output ratios and the complete nine-formula identity list, verifies the sharp expression at several exact positive rational weights, and checks explicit nonlinear witnesses at positive weights on both sides of one. It also performs 2200 deterministic exact-rational sample comparisons against independently reconstructed nonlinear projections. The continuum in \(r\) and the all-input upper bound follow from the symbolic ratio list, simple inequalities and the layer-cake proof; the random comparisons are only supplementary.

## Relationship to prior work
The nearest directly relevant existing result is *Cyclic-cover rigidity of weighted-variation stability for isotonic regression* (2026), which proves that isotonic regression on every cyclic Hasse cover graph is two-input variation nonexpansive precisely for uniform weights. That existing theorem already implies the qualitative fact that nonuniform weights permit amplification, so the present finding **does not claim that rigidity result**. Rather, for the first nontrivial cyclic Hasse graph and a natural one-parameter directional anisotropy, it determines the **exact global amplification magnitude and explicit sharp witnesses**, neither of which is stated or implied by the qualitative result alone.

Németh and Németh's 2012 study concerns order-monotonicity of metric projections onto monotone cones; Guyader and collaborators' 2012 work concerns iterative isotone and antitone regression. These papers do not calculate the stated diamond graph-variation Lipschitz coefficient. The numerical factor here is distinct from known coordinatewise isotonic contraction and from one-input variation bounds.

## Limitations
The formula is exact only for the specified four-point diamond, equal positive observation masses and paired edge weights \((r,1,1,r)\). It does not classify arbitrary independent edge weights, arbitrary observation masses or larger posets, nor does it claim independent verification of publication priority. The exhaustive finite calculation proves the algebraic cut list for four vertices; a different proof or computation would be needed beyond this finite order. Historical literature may be incompletely indexed.

## References
- A. B. Németh and S. Z. Németh, *Isotonicity of the projection onto the monotone cone*, arXiv:1201.4677, initially public January 23, 2012. https://arxiv.org/abs/1201.4677
- A. Guyader and collaborators, *A Geometrical Approach to Iterative Isotone Regression*, arXiv:1211.3930, initially public November 16, 2012. https://arxiv.org/abs/1211.3930
- *Cyclic-cover rigidity of weighted-variation stability for isotonic regression*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-cyclic-cover-rigidity-of-weighted-variation-stability-for-isoton--c6a0693fe803
