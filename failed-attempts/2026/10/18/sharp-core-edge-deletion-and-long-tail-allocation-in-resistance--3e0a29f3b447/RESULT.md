# Sharp core-edge deletion and long-tail allocation in resistance-optimal lollipop networks

## Finding

**Theorem.** Fix integers \(m\ge3\) and \(\ell\ge1\), a budget \(B>0\), and a relative price \(t>0\). Form a graph by attaching a path of \(\ell\) *new vertices* to a distinguished root vertex of the complete graph \(K_m\). Thus there are \(N=m+\ell\) vertices. Each root-to-nonroot clique edge and each path edge has unit price per unit conductance; each edge between two nonroot clique vertices has price \(t\). All conductances are independently chosen and nonnegative, with total expenditure \(B\).

Define
\[
 k=m-1,\qquad A=\ell+1,\qquad C=N(m-2),\qquad
 S=\sum_{j=1}^{\ell}\sqrt{j(N-j)},
\]
and
\[
 t_*=\frac{2N(m-1)}{A+C}
 =2+\frac{2(m-1)}{A+C}>2.
\]
Number path edges *from the free tip toward the clique*: edge \(j=1\) is incident to the tip, and edge \(j=\ell\) joins the clique root to the nearest new path vertex. Put \(c_j=j(N-j)\).

**Mixed-core phase.** If \(0<t<t_*\), set
\[
 \alpha=k-\frac{(m-2)t}{2},\qquad
 \beta=\frac{(m-2)t}{2},\qquad
 h=\sqrt{A\alpha}+\sqrt{C\beta}.
\]
The unique minimizer assigns each root-to-nonroot clique edge conductance
\[
 x=\frac{B}{S+h}\sqrt{\frac{A}{\alpha}},
\]
each nonroot-to-nonroot clique edge conductance
\[
 y=\frac{B}{k(S+h)}
 \left(\sqrt{\frac{C}{\beta}}-\sqrt{\frac{A}{\alpha}}\right)>0,
\]
and path edge \(j\) conductance
\[
 z_j=\frac{B\sqrt{c_j}}{S+h}\quad(1\le j\le\ell).
\]
Here \(\alpha>0\) follows from \(t<t_*\).

**Deleted-core phase.** If \(t\ge t_*\), set
\[
 h=\sqrt{k(A+C)},\qquad
 x=\frac{B}{S+h}\sqrt{\frac{A+C}{k}},\qquad
 y=0,\qquad
 z_j=\frac{B\sqrt{c_j}}{S+h}.
\]
The optimizer is globally unique even at the boundary \(t=t_*\). In either phase, the exact minimum total effective resistance, summing over every unordered vertex pair, is
\[
 \boxed{\mathcal K_{\min}=\frac{(S+h)^2}{B}}.
\]

**Long-tail law.** Hold \(m\ge3\) and \(t>0\) fixed and send \(\ell\) to infinity. The threshold decreases to \(2\). The optimal fraction \(\phi_\ell\) of expenditure on *all clique edges* obeys
\[
 \phi_\ell\sim\frac{8q_t}{\pi}\ell^{-3/2},\qquad
 q_t=\begin{cases}
 \sqrt{m-1-\frac{(m-2)t}{2}}+(m-2)\sqrt{t/2},&0<t\le2,\\
 m-1,&t\ge2.
 \end{cases}
\]
The two branches agree at \(t=2\); in all cases \(\mathcal K_{\min}\sim\pi^2\ell^4/(64B)\).

## Assumptions and scope

The graph is simple, finite, undirected, and has precisely one attached path, whose length counts its new vertices/edges, not the number of path vertices including the root. Conductances are nonnegative, and a disconnected positive-weight subgraph has infinite total effective resistance. The given minimizer has all root and path edges positive, hence stays connected even when \(y=0\). The theorem permits arbitrary independent conductances, rather than assuming symmetry. It concerns conductance-weighted electrical effective resistance; it is not a discrete-time Markov chain mixing statement.

## Proof

**1. Unrestricted strict convexity and symmetry.** Let \(L(w)\) denote the weighted graph Laplacian, and \(J=\mathbf1\mathbf1^\top/N\). For a connected positive-conductance subgraph,
\[
 \mathcal K(w)=N\operatorname{tr}\bigl((L(w)+J)^{-1}\bigr)-N.
\]
The inverse-trace function is strictly convex on positive-definite symmetric matrices: its second directional derivative is \(2\operatorname{tr}(X^{-1}HX^{-1}HX^{-1})>0\) for every nonzero symmetric \(H\). Distinct vectors of edge conductances on a simple graph yield distinct Laplacians (their off-diagonal entries recover each weight). Therefore \(\mathcal K\) is strictly convex on its connected feasible domain. Averaging over permutations of the \(m-1\) nonroot clique vertices preserves both price and objective. Strict convexity forces every optimizer to be invariant under these permutations. It thus suffices to solve for common root-edge weight \(x\), common nonroot-core weight \(y\), and individual path weights \(z_j\); the solution will be unique even against asymmetric competitors.

**2. Exact resistance decomposition.** Put \(v=x+ky\). The clique Laplacian has nonzero eigenvalue \(mx\) once and \(v\) with multiplicity \(m-2\). Consequently its own pair-resistance sum is \(1/x+m(m-2)/v\), and the sum of clique-root resistances over nonroot vertices equals \(1/x+(m-2)/v\). Because each path edge is a bridge, attaching the path leaves clique-to-clique resistances unchanged. It adds \(\ell\) copies of each root-to-core resistance and contributes \(c_j/z_j\) from bridge edge \(j\), which separates \(j\) distal vertices from the other \(N-j\) vertices. Hence, exactly,
\[
 \mathcal K=\frac{A}{x}+\frac{C}{x+ky}
            +\sum_{j=1}^{\ell}\frac{c_j}{z_j},
 \quad B=kx+\frac{tk(m-2)}2y+\sum_{j=1}^{\ell}z_j.
\]

**3. Optimality conditions and phase boundary.** On the positive variables, the Lagrangian derivatives with multiplier \(\lambda>0\) are
\[
 \frac{A}{x^2}+\frac{C}{v^2}=\lambda k,
 \quad\frac{C}{v^2}=\lambda\beta\ \text{when }y>0,
 \quad z_j=\sqrt{c_j/\lambda},
\]
where \(\alpha=k-\beta\) and \(\beta=t(m-2)/2\). For \(y>0\), these equations give
\[
 x=\frac1{\sqrt\lambda}\sqrt{A/\alpha},\quad
 v=\frac1{\sqrt\lambda}\sqrt{C/\beta},\quad
 B=\frac{\sqrt{A\alpha}+\sqrt{C\beta}+S}{\sqrt\lambda}.
\]
The positivity constraint \(y=(v-x)/k>0\) is equivalent to \(C\alpha>A\beta\), or \(t<t_*\). Since \(t_*<2k/(m-2)\), these parameters indeed satisfy \(\alpha>0\) throughout this phase.

At \(y=0\), the remaining stationarity equations instead give
\[
 x=\sqrt{\frac{A+C}{k\lambda}},\qquad
 B=\frac{\sqrt{k(A+C)}+S}{\sqrt\lambda}.
\]
The one-sided condition for the inactive variable \(y\) is
\[
 -\frac{Ck}{x^2}+\lambda\frac{tk(m-2)}2
 =\frac{-Ck+(A+C)t(m-2)/2}{x^2}\ge0,
\]
precisely when \(t\ge t_*\). All Karush–Kuhn–Tucker conditions are sufficient by convexity; strict convexity makes the optimizer unique. Equality \(t=t_*\) still gives only one minimizer, with \(y=0\), and the formulas from the two phases meet continuously. Homogeneity, or direct substitution, yields \(\mathcal K_{\min}=\lambda B=(S+h)^2/B\).

**4. Tail asymptotics.** For fixed \(m\), a Riemann sum gives
\[
 S=\sum_{j=1}^{\ell}\sqrt{j(m+\ell-j)}
 \sim\ell^2\int_0^1\sqrt{u(1-u)}\,du
 =\frac\pi8\ell^2.
\]
Since \(t_*\to2\), the displayed phase formulas give \(h\sim q_t\sqrt\ell\); the equality case \(t=2\) remains in the mixed phase but has the same limiting coefficient as the deleted phase. The total clique expenditure is \(B h/(S+h)\) in either phase, so its fraction is \(h/(S+h)\sim(8q_t/\pi)\ell^{-3/2}\). The asymptotic minimum follows from \((S+h)^2/B\).

## Verification

The supplied `verify.py` is a standalone finite-check program using Python 3, NumPy, and SymPy. Executing `python verify.py` runs 7,437 assertions, including symbolic threshold identities; phase and budget boundaries; agreement between the derived objective, an independently assembled full weighted Laplacian, and the claimed minimum; and randomly generated asymmetric feasible perturbations. Test ranges cover clique orders \(3\) through \(8\), path lengths \(1\) through \(7\), several prices on each side of the threshold including equality, and several budgets. These computations are corroboration, **not** a replacement for the proof over all integer orders and positive real parameters.

## Relationship to prior work

Ghosh, Boyd, and Saberi (2006) established convex effective-resistance weight allocation and solved the equal-price two-clique barbell, with tree examples. Their barbell has two dense cores connected by one bridge and does not yield the parameter-dependent clique-plus-path deletion threshold here. Yang (2014) identified an *unweighted* clique-plus-path graph as extremal for the Kirchhoff index subject to a clique-number constraint; that graph-theoretic extremum is not conductance-budget optimization. Bianchi, Cornaro, Palacios, and Torriero (2016) treated a *degree-weighted* Kirchhoff index on lollipops, again without optimizing their individual conductances. The present theorem supplies the full independently weighted, price-dependent minimizer and long-tail budget scaling. The general inverse-trace convexity principle and the bridge counting identity are not claimed as new.

## Limitations

Only one path is attached, all path and root-to-core edge prices are one, and nonroot-core edges share a common price; arbitrary prices on individual edges are outside the result. The objective is the unnormalized sum of electrical pair resistances. Equivalent closed forms or specializations may exist in nonindexed literature. The asymptotic statement fixes clique size and price while path length diverges; no simultaneous-growing-size regime is asserted. Independent external mathematical audit has not been performed.

## References

1. A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, 17th International Symposium on Mathematical Theory of Networks and Systems (July 24–28, 2006), pp. 1185–1196. Public full text: https://stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf . Expanded SIAM Review 50(1) (2008), 37–66, DOI:10.1137/050645452.
2. Y. Yang, *Some Bounds for the Kirchhoff Index of Graphs*, Abstract and Applied Analysis (2014), article 794781, DOI:10.1155/2014/794781. Full text: https://onlinelibrary.wiley.com/doi/10.1155/2014/794781 .
3. M. Bianchi, A. Cornaro, J. L. Palacios, A. Torriero, *Upper and Lower Bounds for the Mixed Degree-Kirchhoff Index*, Filomat 30(9) (2016), 2351–2358, DOI:10.2298/FIL1609351B. Full text: https://journal.pmf.ni.ac.rs/filomat/index.php/filomat/article/download/1354/1218 .
