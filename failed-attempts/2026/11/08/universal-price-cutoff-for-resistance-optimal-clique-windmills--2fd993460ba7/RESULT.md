# Universal price cutoff for resistance-optimal clique windmills

## Finding
Let \(m,r\ge2\) be integers and let \(W_{m,r}=K_1\vee(mK_r)\), a graph consisting of \(m\) disjoint peripheral cliques of order \(r\), each joined to one common hub. Put \(N=mr+1\). Every hub–periphery edge costs \(a>0\) per unit conductance; every within-clique edge costs \(b>0\). Under a total budget \(B>0\), minimize the Kirchhoff index \(\mathcal K=\sum_{u<v}R_{uv}\) over all **independently selectable, nonnegative** edge conductances with connected positive support. The optimizer is globally unique.

There is a sharp **universal support threshold**
\[
 b_c=\frac{2Na}{N-1},
\]
independent of how the \(N-1\) peripheral vertices are partitioned into cliques. If \(b\ge b_c\), the unique optimum has conductance \(x_*=B/[a(N-1)]\) on every hub edge and \(y_*=0\) on every within-clique edge; its optimal total resistance is \(\mathcal K_*=a(N-1)^3/B\). At equality, the clique-edge conductances are still exactly zero.

If \(0<b<b_c\), every clique edge is present at the unique optimum. Define
\[
 A=r(m-1)+1,\quad D=N(r-1),\quad
 \alpha=ra-\frac{(r-1)b}{2},\quad
 \beta=\frac{(r-1)b}{2},\quad
 S=\sqrt{A\alpha}+\sqrt{D\beta}.
\]
Then \(\alpha,\beta>0\), and the unique optimal hub-edge and clique-edge conductances are
\[
 x_* = \frac{B}{mS}\sqrt{\frac{A}{\alpha}},\qquad
 z_* = \frac{B}{mS}\sqrt{\frac{D}{\beta}},\qquad
 y_* = \frac{z_*-x_*}{r}>0.
\]
The optimal Kirchhoff index is
\[
 \boxed{\mathcal K_* = \frac{m^2}{B}
 \left(\sqrt{A\alpha}+\sqrt{D\beta}\right)^2.}
\]
The all-hub-edge-only (spoke-only) design always has resistance \(a(N-1)^3/B\). As \(b/a\downarrow0\), the ratio of that resistance to the true optimum tends to \(mr^2/[r(m-1)+1]\), which is unbounded as \(r\to\infty\) with \(m\ge2\) fixed. This shows the support transition can carry an arbitrarily large relative network-design penalty.

No hypothesis that conductances are symmetric within their edge classes is imposed: symmetry and global uniqueness are conclusions.

## Assumptions and scope
A hub, \(m\) separate cliques with \(r\) peripheral vertices each, and all possible edges from the hub to the peripheral vertices are present as candidate edges. Conductances may equal zero but the positive-weight network must remain connected; its disconnected limit has infinite objective. Prices are strictly positive and constant within the two edge classes. The budget is an upper bound, not an equality assumption; homogeneity shows the optimum exhausts it. Graphs are undirected; all pair resistances are counted once. Nothing is asserted about directed networks, unequal prices within an orbit, non-linear price schedules, or alternate objectives such as algebraic connectivity.

## Proof
**Step 1: existence, strict convexity, and orbit invariance.** Write the weighted Laplacian \(L(w)=\sum_e w_e b_e b_e^{\mathsf T}\), with each incidence vector \(b_e=e_u-e_v\), and put \(M(w)=L(w)+\mathbf1\mathbf1^{\mathsf T}/N\). Whenever the positive support is connected, \(M(w)\) is positive definite and
\[
 \mathcal K(w)=N\{\operatorname{tr}(M(w)^{-1})-1\}.
\]
The map \(M\mapsto\operatorname{tr}(M^{-1})\) is strictly convex on positive-definite matrices: along a nonzero symmetric perturbation \(H\), its second derivative is \(2\operatorname{tr}(M^{-1}HM^{-1}HM^{-1})>0\). The map from edge conductances to \(M\) is injective for a simple graph (an off-diagonal entry records its edge conductance). Consequently \(\mathcal K\) is strictly convex on the connected feasible region. The budget simplex is compact; approaching a disconnected limit sends a positive Laplacian eigenvalue to zero and \(\mathcal K\) to infinity, so an optimizer exists and is unique. Uniform positive rescaling decreases resistance, hence the budget is exhausted. Every graph automorphism preserving the two cost classes maps an optimizer to another; uniqueness therefore forces a common hub-edge conductance \(x>0\) and a common internal-clique conductance \(y\ge0\).

**Step 2: exact spectral reduction.** At conductances \((x,y)\), the nonzero Laplacian eigenvalues, counting multiplicities, are
\[
 \underbrace{x,\dots,x}_{m-1},\quad
 \underbrace{x+ry,\dots,x+ry}_{m(r-1)},\quad Nx.
\]
The \(x\) modes compare sums on the different cliques, the \(x+ry\) modes are mean-zero within a single clique, and the \(Nx\) mode contrasts the hub against all peripheral vertices. Therefore
\[
 \mathcal K(x,y)=N\left(\frac{m-1}{x}+\frac{m(r-1)}{x+ry}+\frac1{Nx}\right)
 =m\left(\frac A x+\frac D{x+ry}\right).
\]
The exact cost is \(mr a x+mr(r-1)b y/2\), so at optimum it equals \(B\).

**Step 3: constrained scalar minimization.** Set \(z=x+ry\), \(t=z/x\ge1\), \(\beta=(r-1)b/2>0\), and \(\alpha=ra-\beta\) (which may be negative). The budget is \(\alpha x+\beta z=B/m\), whence
\[
 x=\frac{B}{m(\alpha+\beta t)},\qquad
 \mathcal K=\frac{m^2}{B}
 \left(\alpha A+\beta D+\beta A t+\frac{\alpha D}{t}\right).
\]
The denominator \(\alpha+\beta t=ra+\beta(t-1)\) is positive for every \(t\ge1\). If \(\alpha\le0\), the derivative of the parenthesized expression, \(\beta A-\alpha D/t^2\), is positive for all \(t\ge1\). For \(\alpha>0\), this derivative is strictly increasing and has its only zero at
\[
 t_*=\sqrt{\frac{\alpha D}{\beta A}}.
\]
Thus \(t_*>1\) precisely when \(\alpha D>\beta A\). The key identity \(A+D=mr^2\) transforms this into
\[
 D(ra-\beta)>\beta A
 \quad\Longleftrightarrow\quad
 raN(r-1)>\frac{(r-1)b}{2}mr^2
 \quad\Longleftrightarrow\quad
 b<\frac{2Na}{mr}=\frac{2Na}{N-1}.
\]
Above or at that price, the scalar minimum is uniquely \(t=1\), hence \(y=0\) and \(x=B/[a(N-1)]\). Below that price, the unique scalar minimum is the stated \(t_*>1\). Applying the equality case of Cauchy–Schwarz to \(A/x+D/z\) subject to \(\alpha x+\beta z=B/m\) yields the stated formulas and value. Strict convexity from Step 1 establishes global uniqueness beyond symmetry-constrained designs. Finally, when \(b\downarrow0\), the optimal value approaches \(m^2 A r a/B\), whereas the optimal spoke-only design costs \(a(mr)^3/B\); dividing gives the stated ratio \(mr^2/A\).

## Verification
The file `verify.py`, supplied with this result, uses only Python's standard library and exact rational arithmetic. It computes the Kirchhoff index for arbitrary non-symmetric edge conductances by inverting the blocks of a Laplacian grounded at the hub: if \(Q\) is the grounded inverse, then \(\mathcal K=N\operatorname{tr}(Q)-\mathbf1^{\mathsf T}Q\mathbf1\). It checks exact spectral expressions on \(81\) uniform configurations, constructs exact rational interior optima with \(z/x=2\), tests all nine combinations \(2\le m,r\le4\), verifies both threshold regimes, and compares the bound against \(360\) randomly generated non-symmetric, exactly budget-normalized feasible designs. Running `python3 verify.py` prints `VERIFY_OK 522`.

As a rational example, take \(m=2,r=3,a=1,b=7/5,B=44/5\). Then \(N=7\) and \(b<b_c=7/3\); the optimal hub conductance is \(x_*=1\), the within-clique conductance is \(y_*=1/3\), and \(\mathcal K_*=22\). The best all-hub-edge-only allocation has \(\mathcal K=270/11>22\). The computations are checks of an analytic theorem, not substitutes for the infinite-family proof.

## Relationship to prior work
Ghosh, Boyd, and Saberi established the general convex effective-resistance allocation problem and uniqueness, and evaluated trees, wheels, and barbells. The same convexity and symmetry mechanisms are used here, but their inspected analytical examples do not give the clique-windmill weighted-price optimum, the exact support cutoff, or its surprising dependence only on total vertex count. Sardar and Xu investigate resistance distances and Kirchhoff indices of unit-resistance windmill graphs, a different, fixed-weight question. The current statement concerns an optimal allocation over all independent conductances with two positive cost classes; the formula and price threshold are not consequences of a fixed-weight index table without a further optimization argument.

## Limitations
The model assumes uniform prices inside each of two cost orbits and strictly positive linear prices. It does not classify general heterogeneous prices, discrete edge-installation costs, or budgets with lower bounds on individual edges. General convex optimization of effective resistance predates this result; only the explicit complete windmill evaluation and universal threshold are asserted as contributions. A later windmill-index paper was available by its abstract but not full publisher text, so unindexed equivalent weighted formulae remain a literature risk. Verification is internal to the analytical computation and does not constitute independent audit. A 2006 proceedings version of the foundational optimization paper is documented, while the 2008 journal paper supplies the earliest exact day-resolved verified public date used in metadata; the earlier proceedings upload day was not established.

## References
1. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of MTNS 2006, Kyoto, July 24–28, 2006, pp. 1185–1196, https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf.
2. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50(1), 37–66 (2008); online February 1, 2008, https://doi.org/10.1137/050645452; lawful author-hosted text https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf.
3. M. S. Sardar and S.-J. Xu, *Resistance Distance and Kirchhoff Index in Windmill Graphs*, Current Organic Synthesis 22(2), 159–168; first online July 4, 2024, https://doi.org/10.2174/0115701794299562240606054510 (abstract available; full text not inspected).
