# A sharp tree-branching law for variation sensitivity of bounded-slope least squares

## Finding

Let \(T=(V,E)\) be any finite simple unweighted tree with \(n=|V|\ge2\), and let \(R>0\). Write
\[
\operatorname{TV}_T(x)=\sum_{\{u,v\}\in E}|x_u-x_v|,
\qquad
K_R(T)=\{z\in\mathbb R^V:|z_u-z_v|\le R\text{ for every }\{u,v\}\in E\}.
\]
Let \(P_R(x)\) uniquely minimize \(\sum_{v\in V}(z_v-x_v)^2\) over \(z\in K_R(T)\), and define its sharp two-input quotient-seminorm coefficient
\[
L(T)=\sup_{\operatorname{TV}_T(x-y)>0}
\frac{\operatorname{TV}_T(P_R(x)-P_R(y))}{\operatorname{TV}_T(x-y)}.
\]
The coefficient is independent of \(R>0\) and has the following exact connected-subtree formula. For every connected vertex subset \(S\subseteq V\) with \(|S|\ge2\), and every internal edge \(e\in E(S)\), removal of \(e\) splits \(S\) into nonempty parts \(A\) and \(B\). Let \(b_A\) and \(b_B\) be the numbers of edges from \(A\) and \(B\), respectively, to \(V\setminus S\). Then
\[
\boxed{L(T)=\max\left\{1,\max_{S\text{ connected},\ |S|\ge2}
\max_{e\in E(S)}\frac{|B|b_A+|A|b_B}{|S|}\right\}.}
\]
All terms attaining the maximum are realizable as sharp ratios of *distinct finite input pairs*, not merely as derivatives or limiting examples.

**Contractivity and gap.** One has \(L(T)=1\) exactly when \(T\) is a path or the four-vertex claw \(K_{1,3}\). Every other tree obeys \(L(T)\ge3/2\). The first possible amplification occurs on five vertices; a four-leaf star has coefficient \(3/2\). More generally, the \(k\)-leaf star has \(\max\{1,(k-1)/2\}\).

**Sharp fixed-order envelope.** For every integer \(n\ge2\),
\[
\boxed{\max_{|V(T)|=n}L(T)=
\max\left\{1,\max_{2\le s\le n-1}\frac{(s-1)(n-s)}s\right\},}
\]
where the inner maximum over an empty set is omitted. A tree made of an \(s\)-vertex path plus \(n-s\) leaves attached to one endpoint realizes each inner term. For \(n\ge5\), optimal \(s\) can be chosen as the first integer satisfying \(s(s+1)\ge n\), and the sharp envelope is
\[
 n-2\sqrt n+1+O(n^{-1/2})\qquad(n\to\infty).
\]
Thus bounded-slope least squares can exhibit variation sensitivity almost linear in the number of tree vertices, notwithstanding its Euclidean nonexpansivity.

## Assumptions and scope

All signals and projections are real, squared-error weights are equal, each tree edge contributes unit weight to graph total variation, and the same strictly positive slope cap \(R\) applies to every edge. The supremum concerns *two inputs* and uses the seminorm \(\operatorname{TV}_T\) on vectors modulo constants; this is distinct from Euclidean Lipschitz continuity of the projector and from a one-input variation inequality. Connectivity and acyclicity of \(T\) are essential to the cut-basis reduction below. No claim is made for \(R=0\), general connected graphs with cycles, unequal observation masses, or unequal edge variation weights.

## Proof

**1. Polyhedral active components.** For any active edge set \(F\subseteq E\) and either sign of its saturated difference, an ordinary differentiability cell of \(P_R\) has derivative \(Q_F\), the orthogonal projector onto the subspace of vectors constant on each component of the forest \((V,F)\). Thus \(Q_F\) replaces values by their arithmetic means within the components. Indeed, impose the active affine equalities \(z_v-z_u=\pm R\) and minimize squared error; its derivative is orthogonal projection onto the common nullspace of the active edge differences. Conversely, every \(F\subseteq E\) is realized on a full-dimensional cell: orient the tree from a root, choose a feasible \(z\) whose oriented edge differences are \(R\) on \(F\) and zero on \(E\setminus F\), and put \(x=z+\sum_{e\in F}\lambda_e d_e\), where \(d_e\) is the outward normal to the saturated inequality and every \(\lambda_e>0\). KKT stationarity, strict complementary slackness, and strict slackness off \(F\) give a neighborhood with this fixed active set. Tree independence guarantees the construction. Since Euclidean projection onto a finite polyhedron is continuous piecewise affine, integrating along an input segment gives
\[
L(T)=\max_{F\subseteq E}\|Q_F\|_{\operatorname{TV}_T\to\operatorname{TV}_T}.
\]
The reverse inequality is attained on two distinct points of the corresponding open affine cell by any norming direction.

**2. A complete cut basis.** Fix an arbitrary orientation of the tree. Every real signal modulo constants is the sum of its signed edge differences times the corresponding one-edge cut indicators. More precisely, for an edge \(e=\{u,v\}\), let \(U_e\) be either component of \(T\setminus\{e\}\) and let \(h_e=\mathbf1_{U_e}\). Because \(\operatorname{TV}_T(h_e)=1\) and tree edge gradients are independent coordinates, for any constant-preserving linear operator \(Q\),
\[
\|Q\|_{\operatorname{TV}_T\to\operatorname{TV}_T}
=\max_{e\in E}\operatorname{TV}_T(Qh_e).
\]
The upper bound follows by decomposing an arbitrary edge-gradient vector into this basis, and equality follows by using the maximizing indicator.

**3. Exact response of an active component.** Fix \(F\) and an edge \(e\). If \(e\notin F\), every connected averaging block lies on one side of the cut, hence \(Q_Fh_e=h_e\) and the response variation is exactly one. If \(e\in F\), let \(S\) be its active component. The cut splits \(S=A\sqcup B\) into sides of respective cardinalities \(a\) and \(b\). Within \(S\), \(Q_Fh_e\) has the common value \(a/(a+b)\), choosing \(h_e=1\) on the side containing \(A\). Every other active component is entirely on one side of the cut and retains the original zero or one value. Consequently the only output jumps are boundary edges of \(S\): those leaving \(A\) contribute \(b/(a+b)\) each, while those leaving \(B\) contribute \(a/(a+b)\) each. The exact gain is
\[
\operatorname{TV}_T(Q_Fh_e)=\frac{b b_A+a b_B}{a+b}.
\]
Conversely, each connected \(S\) and internal \(e\) is realized by taking \(F=E(S)\). Combining with steps 1–2 proves the exact formula, including finite-pair attainment.

**4. Contractivity threshold and strict gap.** On a path every connected \(S\) is an interval, so the two ends can contribute at most one boundary edge each; the ratio in step 3 is no larger than \((a+b)/(a+b)=1\). Direct inspection gives the same bound for \(K_{1,3}\). If a tree is neither a path nor \(K_{1,3}\), it contains an edge \(uv\) with \(\deg(u)+\deg(v)\ge5\): a vertex of degree at least four has such an incident edge, and any vertex of degree three either belongs to the four-vertex claw or has a neighbor of degree at least two. Taking \(S=\{u,v\}\) gives
\[
L(T)\ge\frac{\deg(u)+\deg(v)-2}{2}\ge\frac32.
\]
For a star with \(k\) leaves, connected subsets containing an edge consist of the hub and \(j\) leaves. For an edge to a leaf, all \(k-j\) boundary edges leave the hub side, giving \((k-j)/(j+1)\), maximized at \(j=1\). This proves the star formula and establishes the first five-vertex occurrence.

**5. Fixed-order envelope.** For a connected \(S\) of size \(s\ge2\), its total number of boundary edges is at most \(n-s\): each component of \(T\setminus S\) has exactly one edge into \(S\). Since both \(a\) and \(b\) are at most \(s-1\), step 3 yields
\[
\frac{b b_A+a b_B}{s}\le\frac{s-1}{s}(b_A+b_B)
\le\frac{(s-1)(n-s)}s.
\]
To attain equality for any \(2\le s\le n-1\), take an \(s\)-vertex path \(v_0,\ldots,v_{s-1}\), add \(n-s\) pendant leaves at \(v_0\), and choose \(S\) to be the path with internal edge \(v_0v_1\). All boundary edges attach to the one-vertex side of the internal cut, so its gain equals \((s-1)(n-s)/s\). The identity cell yields coefficient one when larger candidates are absent. Finally, the objective is \(n+1-s-n/s\); its discrete first difference is \(n/[s(s+1)]-1\), and its continuous maximum is \(n+1-2\sqrt n\) at \(s=\sqrt n\). The nearest integer choice loses \(O(n^{-1/2})\), completing the envelope and asymptotics.

## Verification

Run `python3 verify.py` using the adjacent source file. It reconstructs the graph cut response via two independent descriptions—componentwise averaging and boundary cardinalities—using exact rational numbers for every labeled tree through six vertices (1,441 trees and 43,614 active-set faces). It verifies the contractivity classification, exact fixed-order envelope, and integer optimizer for sizes through 500, and constructs distinct rational input pairs for five broom configurations with exact KKT multipliers, including the nine-vertex amplification factor four. Outputs are reproducible and require only the Python standard library. The finite computations independently test the formulas but are not used as proofs for arbitrary tree order; the unrestricted proof is above.

## Relationship to prior work

Yeganova–Wilbur (2009) examine a monotone, Lipschitz-constrained regression on an ordered line and prove an algorithmic convergence result. Agarwal–Phillips–Sadri (2009) develop fast least-squares Lipschitz-isotonic and unimodal regression algorithms on paths and trees; their tree results retain orientation/order constraints. Kyng–Rao–Sachdeva–Spielman (2015) study Lipschitz extensions from prescribed labels, including lexicographically optimal extensions, rather than global Euclidean nearest-point fitting to bounded differences. These works motivate constrained fitting but do not supply the two-input graph-variation norm, connected-active-subtree formula, contractivity characterization, or sharp fixed-order envelope derived here. Related results about graph gradient-space projections or predetermined descendant averages act on different spaces or use different averaging families and do not imply the present formula. This literature comparison does not establish absolute priority over all inaccessible or unindexed sources.

## Limitations

The result is restricted to finite unweighted trees, unweighted Euclidean least squares, a common positive symmetric edge-difference cap, and unit-weight undirected total variation. It does not determine stability for general graphs with cycles, asymmetric edge caps, vertex-dependent fitting weights, or arbitrary graph variation weights. It also does not claim a corresponding one-input variation inequality. Exact archival priority requires independent literature review.

## References

1. L. Yeganova and W. J. Wilbur, *Isotonic Regression under Lipschitz Constraint*, Journal of Optimization Theory and Applications **141** (2009), 429–443; first published online 2009-01-07. https://doi.org/10.1007/s10957-008-9477-0
2. P. K. Agarwal, J. M. Phillips, and B. Sadri, *Lipschitz Unimodal and Isotonic Regression on Paths and Trees*, first public arXiv version 2009-12-28. https://arxiv.org/abs/0912.5182
3. R. Kyng, A. Rao, S. Sachdeva, and D. A. Spielman, *Algorithms for Lipschitz Learning on Graphs*, first public arXiv version 2015-05-01. https://arxiv.org/abs/1505.00290
