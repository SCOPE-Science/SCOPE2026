# Sharp two-input graph-variation sensitivity of mean-centered rectification on weighted trees

## Finding
Let \(T=(V,E)\) be a finite tree with \(n=|V|\ge 3\). Assign arbitrary strictly positive vertex masses \(\mu_v\) and strictly positive edge-variation weights \(w_e\). Write \(M=\sum_{v\in V}\mu_v\), and define the weighted mean and mean-centered positive-part map by
\[
\bar x_\mu=M^{-1}\sum_{v\in V}\mu_vx_v,\qquad
(F_\mu x)_v=\max\{x_v-\bar x_\mu,0\}.
\]
Equip real signals with the graph total-variation seminorm
\[
V_w(h)=\sum_{e=\{u,v\}\in E}w_e|h_u-h_v|.
\]
For any edge \(e\), deletion of \(e\) splits the tree into nonempty vertex classes \(U_e,W_e\). Let \(\mu(U)=\sum_{v\in U}\mu_v\) and \(w(E[U])=\sum_{f\in E(T[U])}w_f\), with an empty edge sum equal to zero. Then the **exact, attained two-input variation Lipschitz coefficient** is
\[
\boxed{\displaystyle
\sup_{V_w(x-y)>0}\frac{V_w(F_\mu x-F_\mu y)}{V_w(x-y)}
=\max_{e\in E}\left[1+
\frac{\mu(W_e)w(E[U_e])+\mu(U_e)w(E[W_e])}{M w_e}\right].}
\]
For every maximizing edge, a pair of signals with a difference supported on its cut step attains equality; the finite supremum is a maximum. The right-hand expression is independent of the orientation or naming of the two cut components.

The two-vertex case is different: for \(n=2\), the exact coefficient is \(\max\{\mu_1,\mu_2\}/(\mu_1+\mu_2)\). On an unweighted \(n\)-vertex tree with uniform vertex masses, the full formula collapses to
\[
\boxed{\displaystyle
\operatorname{Lip}_{V}(F)=\frac{2}{n}\max_{e\in E}|U_e|\,|W_e|,\quad n\ge3.}
\]
Consequently the sharp constant on a path is \(2\lfloor n^2/4\rfloor/n\), while that on a star is \(2(n-1)/n\). At each fixed order \(n\ge4\), stars uniquely minimize this coefficient among unlabeled trees; the maximum over trees equals the path value and occurs precisely in trees containing an edge with a most-balanced split. Although \(V_w(F_\mu x)\le V_w(x)\) for each individual signal, the two-input coefficient on paths is asymptotic to \(n/2\).

## Assumptions and scope
All inputs are real and vertex-indexed; vertex masses and edge weights are fixed, finite, and strictly positive. The underlying graph is a connected, finite, simple, undirected tree. No condition relates vertex masses to edge weights. We consider differences \(F_\mu x-F_\mu y\), not \(F_\mu(x-y)\). Because \(F_\mu(x+c\mathbf 1)=F_\mu(x)\), the map is well-defined on the quotient by constants, and \(V_w\) is a norm on that quotient. The definitions include arbitrary nonconstant input pairs, ties at the threshold, and nonuniform weights. For \(n=2\), the stated exceptional formula applies instead of the tree formula with leading term one.

## Proof
**1. Linear cells and realizable activation masks.** Let \(A\subset V\) be any nonempty proper subset and put \(D_A=\operatorname{diag}(\mathbf 1_A)\). The open set \(\{x:x_v-\bar x_\mu>0\text{ on }A,\ x_v-\bar x_\mu<0\text{ on }V\setminus A\}\) is nonempty: \(x=\mathbf 1_A\) belongs to it because all masses are positive. On this cell the Jacobian of the piecewise-affine map is the linear operator
\[
J_Ah=D_A(h-\bar h_\mu\mathbf 1).
\]
Only nonempty proper masks occur on open cells. A segment crosses finitely many such cells; by continuity, its total image increment is bounded by the maximum induced \(V_w\)-seminorm of these Jacobians. Conversely every Jacobian norm is achieved (in finite dimensions) by two sufficiently close points lying within its nonempty cell. Thus the global two-input modulus equals \(\max_{\varnothing\ne A\subsetneq V}\|J_A\|_{V_w\to V_w}\).

**2. Every direction decomposes into tree-cut steps.** Fix a root and direct each edge from the root toward its child. Let \(W_e\) denote the descendant component separated by edge \(e\). Every vector \(h\) admits the exact expansion
\[
h=h_{\rm root}\mathbf 1+\sum_{e\in E}d_e\mathbf 1_{W_e},
\qquad d_e=h_{\rm child(e)}-h_{\rm parent(e)},
\]
with \(V_w(h)=\sum_e w_e|d_e|\). As \(J_A\mathbf1=0\), the triangle inequality gives
\[
\|J_A\|_{V_w\to V_w}=\max_{e\in E}\frac{V_w(J_A\mathbf 1_{W_e})}{w_e}.
\]
The upper bound follows by decomposition and the reverse bound by testing a single step. This equality holds for each fixed mask, without an approximation argument.

**3. Sharp cut-column inequality.** For one cut \(V=U\sqcup W\) made by deleting \(e\), let \(a=\mu(U)/M\) and \(b=\mu(W)/M\), so \(a+b=1\). The centered cut step \(\mathbf1_W-\overline{\mathbf1_W}_\mu\mathbf1\) equals \(-b\) on \(U\) and \(a\) on \(W\). After multiplication by \(\mathbf1_A\), every internal \(U\)-edge contributes at most \(b w_f\), and every internal \(W\)-edge at most \(a w_f\); the cross-edge contributes at most \(w_e\), because its two possible nonzero endpoint values have opposite signs and absolute values summing to one. Therefore for every mask \(A\)
\[
V_w(J_A\mathbf1_W)\le w_e+b\,w(E[U])+a\,w(E[W]).
\]
For \(n\ge3\), equality is realized simultaneously on *every edge*: give each of \(T[U]\) and \(T[W]\) a bipartite checkerboard mask with the vertex incident to \(e\) active and every adjacent internal vertex inactive. The union \(A\) is nonempty, and since some component contains at least two vertices, at least one vertex is inactive, making \(A\) a realizable strict activation mask. Every internal edge then joins an active endpoint to an inactive endpoint, and both cross-edge endpoints are active. This saturates every bound.

**4. Exact global sharpness.** Maximize the sharp column value from Step 3 over edges, then over masks as justified in Steps 1–2. For a maximizing cut \(W\), use its checkerboard mask \(A\), choose \(x=\mathbf1_A\), and choose \(y=x+\varepsilon\mathbf1_W\) with \(\varepsilon>0\) small enough to preserve the strict signs defining the same mask. Then \(F_\mu y-F_\mu x=\varepsilon J_A\mathbf1_W\) and \(V_w(y-x)=\varepsilon w_e\). Hence the bound is achieved by actual input data, not merely a formal derivative. The same proof works for arbitrary positive masses and edge weights. At \(n=2\), the only permitted masks select exactly one vertex; the single cut-column output magnitudes are \(a\) and \(b\), proving the exceptional coefficient \(\max\{a,b\}\).

**5. Consequences for unweighted trees.** With \(\mu_v=w_e=1\), a cut with \(|U|=u\), \(|W|=n-u\) has exactly \(u-1\) and \(n-u-1\) internal edges. Its column value becomes
\[
1+\frac{(n-u)(u-1)+u(n-u-1)}{n}=\frac{2u(n-u)}n.
\]
The maximum over integer splits occurs at \(u=\lfloor n/2\rfloor\). A path has such a split. A star has only singleton splits. Every nonstar tree of order at least four has a nonpendant edge splitting it into two parts of sizes at least two, for which \(u(n-u)>n-1\); hence its coefficient strictly exceeds the star coefficient. The largest possible cut product is \(\lfloor n^2/4\rfloor\), so a tree is globally worst precisely if one edge realizes this balanced split.

**6. One-input variation contraction.** For each input \(x\), shifting by the constant \(\bar x_\mu\) leaves all edge differences unchanged; applying the scalar map \(t\mapsto\max(t,0)\) cannot increase any edge difference. Hence \(V_w(F_\mu x)\le V_w(x)\). This separate one-input inequality does not constrain the variation of the difference of two separately rectified signals.

## Verification
Run `python verification/check.py` with Python 3's standard library from the package root. Its exact rational-arithmetic tests compare the formula against every nonempty proper activation mask and every edge column on 210 sampled weighted trees with 2 through 8 vertices (90,600 mask/column comparisons); they also test 2,513 arbitrary input pairs, construct 180 exact attaining checkerboard pairs, and check the unweighted path and star formulas at every length 3 through 30. The program emits `ALL_CENTERED_RECTIFICATION_VARIATION_CHECKS_PASS` upon success. The tests are finite and sampled; the preceding proof establishes the result for every finite weighted tree.

## Relationship to prior work
Chambolle, Giacomini and Lussardi (publicly archived 2009) study graph-based discrete perimeter energies, coarea and continuum limits. They provide relevant variation background but do not study the global pairwise Lipschitz norm of a mass-centered positive-part map on finite trees. Glorot, Bordes and Bengio (2011) investigate coordinatewise rectification as an activation; their experiments and rectifier model do not provide graph-variation stability norms. The published result *Sharp weighted-degree bound and bipartite rigidity for graph-Sobolev truncation* studies uncentered positive-part truncation in a **quadratic graph-Sobolev norm**, whereas this theorem concerns a centered nonlinear map in a **weighted edge-\(\ell_1\) seminorm** and its sharp bridge-mass formula. The published three-point median two-input variation theorem uses a different order-statistic filter and a local three-edge selector bound rather than global mean subtraction. The exact implication comparisons appear in `AUDIT.json`; historical priority is not guaranteed by search alone.

## Limitations
The bridge-cut decomposition and exact formula require a tree. No analogous closed form is claimed for graphs with cycles. All masses and edge weights are positive, and the map uses precisely the global weighted arithmetic mean as threshold and coordinatewise positive part. Vector-valued data, alternative thresholds, and infinite trees are not covered. The published literature might contain a differently worded equivalent, especially in older nonlinear graph-processing or projection theory, and no independent historical review is represented.

## References
1. A. Chambolle, A. Giacomini and L. Lussardi, *Continuous limits of discrete perimeters*, publicly posted 2009-03-01, https://cvgmt.sns.it/paper/443/ ; full text https://cvgmt.sns.it/media/doc/paper/443/discreteperimetersfinal.pdf .
2. X. Glorot, A. Bordes and Y. Bengio, *Deep Sparse Rectifier Neural Networks*, PMLR 15 (2011), 315–323, public proceedings record 2011-06-14, https://proceedings.mlr.press/v15/glorot11a.html ; full text https://proceedings.mlr.press/v15/glorot11a/glorot11a.pdf .
3. *Sharp weighted-degree bound and bipartite rigidity for graph-Sobolev truncation*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-weighted-degree-bound-and-bipartite-rigidity-for-graph-sob--1700b3de04ff .
4. *Sharp two-input variation sensitivity of three-point median smoothing on finite paths*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-two-input-variation-sensitivity-of-three-point-median-smoo--5759b99f2a42 .
