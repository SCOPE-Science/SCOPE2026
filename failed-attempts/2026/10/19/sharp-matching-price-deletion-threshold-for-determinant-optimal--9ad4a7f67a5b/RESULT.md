# Sharp matching-price deletion threshold for determinant-optimal bipartite conductances

## Finding
Let \(n\ge3\) be an integer, \(B>0\), and \(t>0\). In the complete bipartite graph \(K_{n,n}\), fix the perfect matching \(\{(i,i):1\le i\le n\}\). Match-edge conductances cost \(t\) units per conductance; each other edge costs one unit per conductance. Among **all independently chosen** nonnegative edge conductances \(w_{ij}\) obeying
\[
t\sum_{i=1}^n w_{ii}+\sum_{i\ne j}w_{ij}=B,
\]
maximize the weighted spanning-tree enumerator
\[
\tau(w)=\sum_{T\text{ spanning tree}}\prod_{e\in T}w_e
=\det L_{\mathrm{red}}(w).
\]
There is a **unique global optimizer**, with a common matching conductance \(a\ge0\) and a common nonmatching conductance \(b>0\). Define
\[
t_c(n)=\frac{n(2n-3)}{(2n-1)(n-2)}=1+\frac{2(n-1)}{(2n-1)(n-2)}.
\]
If \(t\ge t_c(n)\), then
\[
a=0,\qquad b=\frac{B}{n(n-1)}.
\]
Thus every edge of the distinguished perfect matching is optimally omitted, even though the remaining crown graph is connected. If \(0<t<t_c(n)\), the optimizer instead retains *all* edges. Its unique positive ratio \(y=a/b\) solves
\[
Q(y)=2ty^2+\bigl(4(n-1)t-2n\bigr)y+(2n-1)(n-2)t-n(2n-3)=0,
\]
and is explicitly
\[
y=\frac{-D+\sqrt{D^2-8tC}}{4t},\quad D=4(n-1)t-2n,\quad C=(2n-1)(n-2)t-n(2n-3)<0.
\]
Then \(b=B/[n(ty+n-1)]\) and \(a=yb\). With \(y=0\) in the deletion regime, the exact optimum across **all** conductance choices is
\[
\tau^*(n,B,t)=\frac{B^{2n-1}}{n^{n+1}}
\frac{(y+n-1)(2y+n-2)^{n-1}}{(ty+n-1)^{2n-1}}.
\]
In particular, for \(t\ge t_c(n)\), this equals
\[
\frac{B^{2n-1}(n-2)^{n-1}}{n^{n+1}(n-1)^{2n-2}}.
\]
The first thresholds are \(t_c(3)=9/5\) and \(t_c(4)=10/7\); as \(n\to\infty\), \(n(t_c(n)-1)\to1\). At equal prices \(t=1\), all edges receive \(B/n^2\). As \(t\downarrow0\), the optimal budget shares tend to \(n/(2n-1)\) on matching edges and \((n-1)/(2n-1)\) on the other edges.

## Assumptions and scope
The network is undirected and simple with two labeled parts of equal size \(n\ge3\); every possible cross-part edge is an admissible design variable. Edge conductances may be zero. The expense constraint is an equality, \(B>0\), and the only two possible prices are \(t>0\) on a prescribed perfect matching and one otherwise. No symmetry is assumed of competing allocations. The objective is weighted tree-product sum, **not** the count of trees in a selected unweighted graph, the minimum spanning-tree weight, the trace of an inverse Laplacian, or the Laplacian spectral gap.

## Proof
**1. Global existence, uniqueness, and symmetry.** Fix any vertex and form the reduced weighted Laplacian \(M(w)\). By the weighted matrix-tree theorem, \(\tau=\det M\). The nonnegative expense simplex is compact; \(\tau\) is continuous. A positive constant allocation is feasible, connected, and has positive determinant, so any maximizer has a positive-definite reduced Laplacian. Over the positive-definite locus, \(\log\det M\) is strictly concave as a function of the independent edge weights. Indeed for a nonzero feasible direction \(h\), let \(H=M(h)\); then
\[
\frac{d^2}{ds^2}\log\det(M+ sH)
=-\operatorname{tr}\bigl((M+sH)^{-1}H(M+sH)^{-1}H\bigr)<0.
\]
To see strictness, the reduced-Laplacian map is injective on the edge weights of a simple graph: non-root edge weights are minus their off-diagonal matrix entries, and weights incident to the deleted root are recovered from the diagonal after subtracting the other incident weights. Therefore \(h\ne0\) implies \(H\ne0\), and the trace above is a positive squared Frobenius norm. The intersection of the expense simplex with the positive-definite locus is convex, so the optimal weight vector is unique. The cost function and tree enumerator are invariant under simultaneously permuting the two vertex parts by the same permutation and under exchanging the parts. Those automorphisms act transitively on matching edges and on nonmatching edges. Uniqueness forces one common \(a\) and one common \(b\). Because \(n\ge3\), the graph left by deleting the matching is connected, but the graph with \(b=0\) is a union of isolated matched pairs. Hence at the optimizer \(b>0\).

**2. Exact tree polynomial.** For orbit-constant weights, write \(d=a+(n-1)b\). The full Laplacian is
\[
L=\begin{pmatrix}dI&-[(a-b)I+b\mathbf1\mathbf1^\top]\\-[(a-b)I+b\mathbf1\mathbf1^\top]&dI\end{pmatrix}.
\]
The constant bipartite direction gives eigenvalues \(0,2d\). On the \((n-1)\)-dimensional zero-sum subspaces the cross block acts as \((a-b)I\), giving eigenvalues \(nb\) and \(2a+(n-2)b\), each with multiplicity \(n-1\). Kirchhoff's eigenvalue product formula for a graph on \(2n\) vertices yields, exactly,
\[
\tau(a,b)=\frac{d}{n}(nb)^{n-1}(2a+(n-2)b)^{n-1}.
\]
This also holds at \(a=0\), since \(b>0\) and \(n\ge3\).

**3. One-variable maximization.** Write \(y=a/b\ge0\). The budget \(nt a+n(n-1)b=B\) forces
\[
b=\frac{B}{n(ty+n-1)},\qquad a=yb.
\]
Substitution into the preceding spectral product gives
\[
\tau(y)=\frac{B^{2n-1}}{n^{n+1}}
\frac{(y+n-1)(2y+n-2)^{n-1}}{(ty+n-1)^{2n-1}}.
\]
For every finite \(y\ge0\) this is positive, whereas \(\tau(y)\to0\) as \(y\to\infty\). Direct logarithmic differentiation gives
\[
\frac{\tau'(y)}{\tau(y)}=\frac1{y+n-1}+\frac{2(n-1)}{2y+n-2}-\frac{(2n-1)t}{ty+n-1}
=-\frac{(n-1)Q(y)}{(y+n-1)(2y+n-2)(ty+n-1)}.
\]
All denominator factors are positive. Let \(C=Q(0)=(2n-1)(n-2)t-n(2n-3)\), which is nonnegative exactly when \(t\ge t_c(n)\). In that regime, the linear coefficient \(D=4(n-1)t-2n\) is strictly positive because \(t_c(n)>1\) and \(n\ge3\). Thus \(Q(y)>0\) for every \(y>0\); the unique maximizer is \(y=0\). If \(0<t<t_c(n)\), then \(C<0\), while the leading coefficient \(2t\) is positive. Therefore the quadratic has exactly one positive root, with \(Q<0\) before it and \(Q>0\) afterwards; the derivative is positive then negative. This proves the explicit optimum for all \(t>0\), including equality and both boundaries.

**4. Consequences.** The stated closed-form optimum follows by substitution. At \(t=1\), the root is \(y=1\). The threshold identity implies \(n(t_c(n)-1)\to1\). From the quadratic with \(0<t\to0\), multiplying by \(t\) after setting \(z=ty\) shows its positive root has \(ty\to n\). Consequently \(nt a/B=ty/(ty+n-1)\to n/(2n-1)\) and \(n(n-1)b/B=(n-1)/(ty+n-1)\to(n-1)/(2n-1)\).

## Verification
The accompanying `verify.py` executes with Python 3 and no third-party dependencies. It reconstructs the grounded Laplacian and computes its determinant exactly over rational numbers for \(n=3,\ldots,8\), with zero and positive matching conductances. It independently enumerates weighted spanning trees at \(n=3,4\), checks the exact logarithmic derivative against \(Q\) in 450 rational cases, checks threshold coefficient signs in 90 cases, and checks boundary maxima algebraically for multiple sizes. The successful run reports `VERIFY_OK exact_cofactor_spectra=24 independent_tree_sums=6 exact_log_derivatives=450 threshold_sign_cases=90`. These are reproducibility and error-detection checks; the universal theorem is proved above, not inferred from finite experiments.

## Relationship to prior work
Khosoussi, Sukhatme, Huang, and Dissanayake [1] established the weighted spanning-tree count as a design objective, used weighted matrix-tree formulas, and studied discrete edge-selection under cardinality constraints together with convex relaxations. Their inspected problems and results do not provide the exact **uncapped per-edge conductance-budget** optimizer for a priced perfect matching in \(K_{n,n}\), or its sharp all-size deletion threshold. The present statement does **not** claim novelty for matrix-tree identities, log-determinant concavity, orbit symmetrization, or generic convex design. Earlier graph-optimization problems minimizing total effective resistance or maximizing algebraic connectivity use different spectral objectives; their optima do not logically determine this determinant-optimal allocation without an additional optimization. The related unweighted crown-graph spanning-tree calculation gives the tree count at \(a=0\) but not the globally optimal price boundary.

## Limitations
The price and geometry symmetry here are essential; no classification is asserted for arbitrary edge-price matrices, unequal part sizes, or directed graphs. The result is exact for weighted tree products rather than physical reliability probabilities under a specified stochastic failure model. The uniqueness claim uses that each admissible edge is independently controllable and the graph is simple. Broad optimal-design or specialized weighted enumeration literature might contain equivalent earlier derivations; the inspected literature and published-record searches do not constitute a proof of historical priority. No independent audit has been performed.

## References
[1] K. Khosoussi, G. S. Sukhatme, S. Huang, G. Dissanayake, *Maximizing the Weighted Number of Spanning Trees: Near-\(t\)-Optimal Graphs*, arXiv:1604.01116, initial public version 2016-04-05. https://arxiv.org/abs/1604.01116

[2] Weighted matrix-tree theorem (classical), formulated and used in [1, Sections 2.2 and 3].
