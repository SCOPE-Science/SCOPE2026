# Sharp cut formula for total-variation sensitivity of tree slope-band regression

## Finding

**Theorem (exact, attained graph-cut modulus).** Let \(T=(V,E)\) be an arbitrary finite tree with \(|V|\ge2\), with a fixed arbitrary orientation \(e=(a_e,b_e)\) of its edges, positive observation masses \(m_v\), and finite edge-difference bounds \(\ell_e<r_e\). For each real input \(y\in\mathbb R^V\), define its slope-band least-squares fit \(Qy\) to be the unique minimizer
\[
\frac12\sum_{v\in V}m_v(u_v-y_v)^2
\quad\text{subject to}\quad
\ell_e\le u_{b_e}-u_{a_e}\le r_e\quad(e\in E).
\]
Measure *two-input* sensitivity in **unweighted edge total variation** \(J_T(z)=\sum_{ab\in E}|z_b-z_a|\), and put
\[
K(T,m;\ell,r)=\sup_{J_T(y-z)>0}\frac{J_T(Qy-Qz)}{J_T(y-z)}.
\]
For each connected vertex subset \(B\subseteq V\) containing an internal edge \(e\), let \(B=A\sqcup C\) be the two components obtained by deleting \(e\) from the induced subtree \(T[B]\). Write \(M_A=\sum_{v\in A}m_v\), \(M_C=\sum_{v\in C}m_v\), and let \(b_A\) and \(b_C\) be the counts of *original-tree* edges leading from \(A\) and \(C\), respectively, to \(V\setminus B\). Then
\[
\boxed{K(T,m;\ell,r)=\max\left\{1,\;\max_{\substack{B\subseteq V\text{ connected}\\ e\in E(T[B])}}
\frac{b_A M_C+b_C M_A}{M_A+M_C}\right\}.}
\]
Every term of this finite maximum is attainable as a variation ratio for arbitrarily close pairs of inputs; in particular, the sharp modulus is **independent of the positions and widths** of the nondegenerate edge bands.

**Nonlocal consequences.** For equal masses, paths and the three-leaf star have modulus exactly \(1\), while every other tree has modulus at least \(3/2\), a sharp gap attained on the four-leaf star. For a star with \(d\ge2\) leaves, center mass \(m_0\), and leaf masses \(m_i\), the full (not merely threshold) constant simplifies to
\[
K=\max\left\{1,\max_{1\le i\le d}\frac{(d-1)m_i}{m_0+m_i}\right\}.
\]
There are also nonlocal effects not captured by testing just one active edge: an unweighted six-vertex tree with edges \(01,03,04,12,25\) has \(K=5/3\), whereas every two-vertex active block has norm at most \(3/2\). On degree-three caterpillars with \(2q\) spine vertices and one pendant leaf on each internal spine vertex, \(q\ge2\), the sharp modulus is at least \(q-1\); hence amplification is unbounded even under a uniform degree bound of three.

## Assumptions and scope

The tree is finite, undirected, connected and cycle-free; edge orientation is only a device for writing constraints. Vertex masses are arbitrary positive reals, variation edges have weight one, and the lower/upper bounds are **strictly separated finite reals** on every edge. There is no restriction on the shape or sign of these bounds. The minimizer exists and is unique by strict convexity and feasibility (edge constraints can be realized recursively on a tree). The variation seminorm vanishes exactly on constant vectors, and \(Q(y+c\mathbf1)=Qy+c\mathbf1\). No uniformity across changing trees is assumed. The theorem gives an exact two-input Lipschitz seminorm, not a statement that \(J_T(Qy)\le J_T(y)\) for each fixed input.

## Proof

**1. All local derivatives are connected-block averages.** Put \(M=\operatorname{diag}(m_v)\) and write \(D\) for the edge-by-vertex oriented incidence matrix. The feasible set \(\{u:\ell\le Du\le r\}\) is a polyhedron, so weighted metric projection \(Q\) is continuous and piecewise affine. On any full-dimensional data cell, the edges whose upper or lower constraints are active form a forest \(F\subseteq E\). The active equations fix the differences along each connected component \(B\) of \((V,F)\). Hence all feasible first-order increments on this face are constant on \(B\). Orthogonality to this tangent space shows that the linear part of \(Q\) is the weighted component-average operator
\[
(P_F h)_v=\frac{\sum_{w\in B}m_wh_w}{\sum_{w\in B}m_w},\quad v\in B.
\]
Continuity and piecewise affinity imply that the full two-input Lipschitz constant is at most the largest \(J_T\)-seminorm operator norm of these \(P_F\).

**2. Every forest derivative is realized, without relying on a genericity assumption.** Fix any \(F\subseteq E\). On each oriented edge of \(F\), prescribe \((Du)_e=r_e\); on every other edge take \((Du)_e\) strictly between \(\ell_e\) and \(r_e\). A tree admits this potential \(u\), uniquely up to a constant. Give each active upper constraint a strictly positive multiplier \(\lambda_e\), and set
\[
y=u+M^{-1}D_F^{\mathsf T}\lambda.
\]
Then the Karush–Kuhn–Tucker stationarity equation, strict complementarity, and strict slack on the remaining edges show that \(Qy=u\) and that, on an open neighborhood of \(y\), the derivative is exactly \(P_F\). Because the rows of \(D_F\) are independent, active multipliers persist positively under sufficiently small changes of \(y\). Thus the sharp global modulus is **equal** to \(\max_F\|P_F\|_{J_T\to J_T}\), and it is attained by arbitrarily small input perturbations inside such a neighborhood.

**3. Edge-cut basis and exact block formula.** For each edge \(e\), delete it from the entire tree, choose either of its two resulting sides \(S_e\), and write \(h_e=\mathbf1_{S_e}\). Every input vector is a constant plus a linear combination of \(h_e\), with coefficient magnitudes equal to its edge differences; in particular, \(J_T(h_e)=1\). The triangle inequality therefore gives the sharp identity
\[
\|P_F\|_{J_T\to J_T}=\max_{e\in E}J_T(P_Fh_e).
\]
If \(e\notin F\), the cut is constant on each active component and \(P_Fh_e=h_e\), giving \(1\). If \(e\in F\), its active component is some connected \(B\), split by \(e\) into \(A,C\). On \(B\), \(P_Fh_e\) equals \(M_A/(M_A+M_C)\) (up to interchanging sides); outside \(B\), it equals the original zero-one indicator. Consequently there are no variation contributions inside \(B\), and the boundary contributions are
\[
J_T(P_Fh_e)=b_A\frac{M_C}{M_A+M_C}+b_C\frac{M_A}{M_A+M_C}.
\]
Every connected set \(B\) and edge \(e\in E(T[B])\) are realized by the active forest \(F=E(T[B])\). Taking the maximum proves the theorem, including attainability and independence from the edge bounds.

**4. Tree rigidity and explicit examples.** For a path, each half of an active interval has at most one edge leaving the interval, so the cut formula is at most \(1\). The same direct check for the three-leaf star shows that its only potentially largest nontrivial term comes from a center-and-leaf block; with unit masses it equals \(1\). Every other nonpath tree contains an edge \(uv\) with \(\deg(u)+\deg(v)\ge5\): otherwise each degree-three vertex has only leaf neighbors, forcing the entire tree to be the three-leaf star. The block \(B=\{u,v\}\), with unit masses, yields
\[
\frac{(\deg(u)-1)+(\deg(v)-1)}2\ge\frac32.
\]
The four-leaf star has constant exactly \(3/2\), proving sharpness of the gap. For a \(d\)-leaf star every connected active block containing an edge is the center plus some leaf subset \(S\), and cutting the edge to leaf \(i\in S\) yields \((d-|S|)m_i/(m_0+\sum_{j\in S}m_j)\), maximized by \(S=\{i\}\). This proves the star formula.

For the six-vertex example, take active block \(B=\{0,1,2\}\) and cut \(e=01\). The side containing vertex \(0\) has one vertex of \(B\) and two external edges \(03,04\), whereas the other side has two vertices and one external edge \(25\); the formula gives \((2\cdot2+1\cdot1)/3=5/3\). Checking all connected blocks gives no larger value. For the caterpillar with \(2q\) spine vertices, choose the full spine as \(B\) and its middle edge as \(e\); the two halves each have mass \(q\) and each has exactly \(q-1\) external leaf edges, giving \(q-1\).

## Verification

The ordinary standard-library program `check.py` uses exact rational arithmetic to compare the block-boundary formula with direct component averaging for every active mask, every cut and every labeled tree on two through five vertices (145 labeled trees altogether). It also tests heterogeneous observation masses on paths and stars, the exact six-vertex \(5/3\) value, and the caterpillar construction through \(q=8\). An independent algebraic KKT witness with a strictly active upper constraint and an exact finite perturbation reproduces a star amplification of \(20/11\). Execute `python check.py` after extracting the file. These finite checks validate computations and examples; the unrestricted theorem comes from Steps 1–4.

## Relationship to prior work

Yeganova and Wilbur's 2009 **Isotonic Regression under Lipschitz Constraint** treats an ordered path with constraints \(0\le u_{i+1}-u_i\le L_i\) and develops an algorithm for the weighted quadratic fit. Its full-text treatment of objective, knots, and algorithms does not state the exact two-input edge-variation modulus, a tree cut formula, or nonlocal amplification. Kolmogorov, Pock, and Rolinek's **Total variation on a tree** (first public preprint 2015) instead minimizes a sum of vertex losses and *penalties* proportional to edge absolute differences; hard edge-difference box constraints and their fit-map Lipschitz norm are different operators.

There is an especially close **existing tree-heat-flow theorem**: a published mathematical finding on the graph heat semigroup gives an edge-local criterion for contraction in weighted total variation. Its unit-edge-variation mass threshold on stars, and the corresponding path/three-leaf-star contractivity classification, coincide with consequences of the present formula. These **threshold consequences are not asserted as novel**; they can also be obtained using the heat criterion and limits of heat flows on active subforests. However, that result's infinitesimal generator criterion and contraction test do not state or determine the **sharp global magnitude** \(K(T,m;\ell,r)\) of this nonlinear hard-band fitting map, its connected-block cut formula, or the \(5/3\) and unbounded nonlocal amplification constructions. Likewise, a published cyclic-cover isotonic-regression theorem concerns order cones on cyclic Hasse graphs, not the tree edge-difference boxes here. The different operator families require a mathematical, not merely lexical, distinction.

## Limitations

This theorem uses real scalar data, finite trees, strictly positive vertex masses, nondegenerate finite edge bounds, unweighted edge variation and squared-error fidelity. It does not assert the formula on graphs with cycles, for zero-width/infinite bands, nonlinear losses, or for weighted edge-variation seminorms. The source comparisons cannot establish absolute historical priority; an implicit equivalent result in older shape-constrained regression or graph averaging work remains possible. Self-review is documented separately; no independent scientific audit has been performed.

## References

1. L. Yeganova and W. J. Wilbur, *Isotonic Regression under Lipschitz Constraint*, Journal of Optimization Theory and Applications 141 (2009), 429–443. First publicly available online 2009-01-07. DOI: https://doi.org/10.1007/s10957-008-9477-0. Open-access full text: https://link.springer.com/content/pdf/10.1007/s10957-008-9477-0.pdf.
2. V. Kolmogorov, T. Pock and M. Rolinek, *Total variation on a tree*, arXiv:1502.07770, first public submission 2015-02-26; SIAM Journal on Imaging Sciences 9 (2016), 605–636. https://arxiv.org/abs/1502.07770.
3. Published mathematical research record, *A conductance-independent contraction criterion for weighted tree heat flow in total variation*, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-conductance-independent-contraction-criterion-for-weighted-tre--9fedb9294a7c.
4. Published mathematical research record, *Cyclic-cover rigidity of weighted-variation stability for isotonic regression*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-cyclic-cover-rigidity-of-weighted-variation-stability-for-isoton--c6a0693fe803.
