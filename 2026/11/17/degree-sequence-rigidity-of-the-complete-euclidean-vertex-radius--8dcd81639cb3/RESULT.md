# Degree-sequence rigidity of the complete Euclidean vertex-radius spectrum of tree zonotopes

## Finding

**Theorem (independent local vertex radii).** Let \(T=(V,E)\) be a finite, simple, unweighted tree on \(n\ge2\) vertices, with vertex degrees \(d_v\), and put \(m=n-1\). In the standard Euclidean zero-sum space define its **centered graphical zonotope** by
\[
 Z_T=\sum_{\{u,v\}\in E}\left[-\frac{e_u-e_v}{2},\frac{e_u-e_v}{2}\right]\subset\mathbf1^\perp\subset\mathbb R^n.
\]
Sample \(X\) uniformly from the \(2^m\) distinct vertices of \(Z_T\). Then the \(n\) absolute coordinate magnitudes \(\bigl(2|X_v|\bigr)_{v\in V}\) are **mutually independent**. Each has the distribution of \(\bigl|S_{d_v}\bigr|\), where \(S_d\) is the sum of \(d\) independent uniformly random signs.

In particular, the **complete squared-radius spectrum, including every multiplicity**, is the polynomial
\[
 \boxed{\displaystyle F_T(z)=\sum_{x\in\operatorname{Vert}(Z_T)}z^{4\|x\|_2^2}
 =\frac{1}{2^{n-1}}\prod_{v\in V}\left(\sum_{j=0}^{d_v}\binom{d_v}{j}z^{(d_v-2j)^2}\right).}
 \tag{1}
\]
Every coefficient on the right is a nonnegative integer. Thus **nonisomorphic trees with the same degree multiset have identical complete Euclidean vertex-radius spectra** in this canonical embedding.

Writing \(Q=\|X\|_2^2\), one obtains
\[
 \boxed{\mathbb E Q=\frac{n-1}{2},\qquad \operatorname{Var}(Q)=\frac14\sum_{v\in V}\binom{d_v}{2}.} \tag{2}
\]
The smallest and largest squared vertex radii are respectively
\[
 \boxed{\displaystyle Q_{\min}=\frac14\#\{v:d_v\text{ odd}\},\qquad
 Q_{\max}=\frac14\sum_v d_v^2.}\tag{3}
\]
The number of vertices on the inner shell is exactly
\[
 \boxed{\displaystyle N_{\min}=2^{-(n-1)}\prod_{v\in V}c(d_v),\qquad
 c(d)=\begin{cases}\binom d{d/2},&d\text{ even},\\2\binom d{(d-1)/2},&d\text{ odd} .\end{cases}}\tag{4}
\]
Exactly **two antipodal vertices** lie on the outermost sphere. For \(n=2\) the inner and outer shells coincide and both vertices belong to them.

For \(n\ge4\), the variance in (2) is uniquely minimized among all trees of order \(n\) by the path, with value \((n-2)/4\), and uniquely maximized by the star, with value \((n-1)(n-2)/8\). More sharply, the full distribution separates two growth regimes: for any sequence of trees of increasing order with uniformly bounded degrees,
\[
 \frac{Q-\mathbb EQ}{\sqrt{\operatorname{Var}(Q)}}\xrightarrow{\mathrm d}N(0,1),\tag{5}
\]
while for a sequence of stars the same standardized quantity converges in distribution to \((\chi_1^2-1)/\sqrt2\).

## Assumptions and scope

All trees are finite and simple, each edge has generator \(e_u-e_v\) of Euclidean length \(\sqrt2\), and the norm is inherited from \(\mathbb R^n\), rather than from an arbitrary affine-equivalent cube. Uniform vertex sampling assigns probability \(2^{-(n-1)}\) to each vertex. The radius origin is the center of symmetry of \(Z_T\), so all radius assertions concern this fixed canonical center. Exponents of \(z\) in (1) are integers since \(2X_v\) is an integer. Independent signs in the theorem statement refer to *independent auxiliary copies* for the one-vertex distributions; the original incident-edge signs are shared.

## Proof

**1. All independent signings are vertices.** Orient each edge arbitrarily and let \(b_e=e_u-e_v\) be its incidence column. Any vector \(\varepsilon=(\varepsilon_e)_{e\in E}\in\{-1,+1\}^m\) gives the point
\[
 x(\varepsilon)=\frac12\sum_{e\in E}\varepsilon_e b_e.
\]
The incidence columns of a tree are linearly independent: any dependence has a coefficient forced to zero at a leaf, after which leaf removal completes the induction. Thus their Minkowski sum is an injective linear image of a cube, and all its \(2^m\) sign corners are distinct vertices. Uniform vertex sampling is precisely independent fair signs on the edges.

**2. A bipartite gauge eliminates incidence signs.** Properly two-color the tree with signs \(c_v\in\{-1,+1\}\) such that \(c_u=-c_v\) across each edge. At each edge, the incidence entries satisfy \(b_{u,e}=-b_{v,e}\). Therefore the edge spin \(\zeta_e=c_u b_{u,e}\varepsilon_e=c_v b_{v,e}\varepsilon_e\) is well-defined and the spins \(\zeta_e\) remain mutually independent and fair. We have
\[
 2c_vX_v=\sum_{e\ni v}\zeta_e.
 \tag{6}
\]
This is a sum of \(d_v\) independent fair signs for each fixed \(v\), but different vertices share edge signs. The decisive fact is that their *absolute values* are nevertheless jointly independent on a tree.

**3. Exact joint independence by subtree elimination.** Root the tree at any vertex \(r\). For arbitrary bounded functions \(f_v\colon\{0,1,\ldots,d_v\}\to\mathbb R\), consider the product of \(f_v(|\sum_{e\ni v}\zeta_e|)\). For a vertex \(v\ne r\), fix its parent-edge spin \(s\in\{-1,+1\}\) and average this product over the entire descendant subtree, retaining the factor at \(v\). Call the conditional expectation \(H_v(s)\). We prove inductively, from the leaves toward the root, that
\[
 H_v(+1)=H_v(-1)=\prod_{u\text{ in the subtree at }v}\mathbb E f_u(|S_{d_u}|).\tag{7}
\]
If \(v\) is a leaf, the sum has absolute value one and the assertion is immediate. Otherwise condition first on the spins of all child edges. By induction, the product in each child subtree contributes a constant independent of its incoming spin. Hence \(H_v(s)\) equals the product of those constants times
\[
 \mathbb E_{\zeta_1,\ldots,\zeta_k}f_v(|s+\zeta_1+\cdots+\zeta_k|),\qquad k=d_v-1.
\]
Simultaneously reversing all the independent child signs shows that this expectation is the same for \(s=+1\) and \(s=-1\). Its common value is \(\mathbb E f_v(|S_{d_v}|)\), as obtained by also averaging a fair parent sign. This proves (7). At the root there is no parent spin; conditioning on child spins, applying (7), and averaging the root's local factor proves
\[
 \mathbb E\prod_{v\in V}f_v(2|X_v|)=\prod_{v\in V}\mathbb E f_v(|S_{d_v}|).\tag{8}
\]
Since this holds for arbitrary test functions, the claimed joint independence follows.

**4. Complete spectrum and shell contacts.** Put \(f_v(t)=z^{t^2}\) in (8). The elementary binomial law of \(S_d\) gives \(\mathbb E z^{S_d^2}=2^{-d}\sum_{j=0}^d\binom dj z^{(d-2j)^2}\). As \(\sum_v d_v=2m\), multiplying by the total vertex count \(2^m\) yields (1). The smallest possible square of \(S_d\) is zero for even \(d\) and one for odd \(d\), with respectively \(\binom d{d/2}\) or \(2\binom d{(d-1)/2}\) sign strings, giving (3)-(4). The largest possible value is \(d^2\), so the largest radius is (3). Simultaneous equality at all vertices forces all edges incident to each vertex to have the same gauged spin \(\zeta_e\); since the line graph of a nonempty tree is connected, **all** edge spins must agree. There are precisely two such global assignments, yielding two antipodal contacts. This proof remains valid for a one-edge tree.

**5. Moments and sharp tree extremizers.** Elementary independent-sign expansion gives \(\mathbb ES_d^2=d\) and \(\mathbb ES_d^4=3d^2-2d\). From (8),
\[
 \mathbb EQ=\frac14\sum_vd_v=\frac m2,\qquad
 \operatorname{Var}(Q)=\frac1{16}\sum_v2d_v(d_v-1)=\frac14\sum_v\binom{d_v}{2}.
\]
Set \(a_v=d_v-1\ge0\). For a tree, \(\sum_va_v=n-2\), hence
\[
 \frac12\sum_v(a_v^2+a_v)=\sum_v\binom{d_v}{2}
 \quad\text{lies between}\quad n-2\quad\text{and}\quad\binom{n-1}{2}.\tag{9}
\]
For \(n\ge4\), the lower equality requires all \(a_v\in\{0,1\}\), exactly the path degree pattern; the upper equality requires all excess degree at one vertex, exactly the star degree pattern. Substituting in (2) establishes the extremal variance and rigidity.

**6. Distinct distributional limits.** Under a uniform bound \(d_v\le D\), the independent centered summands \((S_{d_v}^2-d_v)/4\) have uniformly bounded magnitude, while (9) gives \(\operatorname{Var}(Q)\ge(n-2)/4\to\infty\). Lindeberg's triangular-array central limit theorem therefore gives (5). For the \(n\)-vertex star with \(m=n-1\) leaves, the leaf contributions are deterministic, so
\[
 Q=\frac m4+\frac{S_m^2}{4},\qquad
 \operatorname{Var}(Q)=\frac{m(m-1)}8.
\]
The ordinary central limit theorem gives \(S_m/\sqrt m\Rightarrow N(0,1)\); the continuous mapping theorem then yields the asserted centered chi-square limit. This completes the proof.

## Verification

The complete exact-arithmetic diagnostic `CHECKER.py` uses only the Python standard library. Run `python3 CHECKER.py`. It directly enumerates all sign corners of **18,248 labeled trees** of orders two through seven (\(1{,}119{,}262\) signed vertices), compares the resulting exact squared-radius multiplicities against (1), and checks extrema and rational moments. It separately checks the full local-absolute-value joint distribution for an eight-vertex nonpath, and compares two nonisomorphic degree-equivalent six-vertex spiders. Observed marker:

`TREE_RADIAL_PASS labelled_trees=18248 orientations=1119262 joint_states=16 six_vertex_shells={4: 6, 8: 12, 12: 8, 16: 4, 20: 2}`

This exhaustive *finite-range* computation is diagnostic only; (1)-(5) for arbitrary trees and asymptotic sequences follow from the analytical proof.

## Relationship to prior work

Padrol, Pilaud and Poullot describe the graph-zonotope realization and acyclic-orientation vertex correspondence, as well as deformation cones; their paper provides the natural setting rather than a uniform-vertex Euclidean radial calculation. Winter classifies vertex-transitive and homogeneous zonotopes, whose cospherical properties concern a different question. Existing published work on tree graphical zonotopes determines **random directional-width variance**, **directional-width third moments**, and **third Steiner intrinsic volumes**, none of which states or implies the joint independence (8) or the full uniform-vertex shell polynomial (1). In particular, a published third-volume result distinguishes the two same-degree spiders whose entire vertex-radius spectra agree here. The point is not a new general probability central limit theorem but a complete, unexpectedly degree-rigid Euclidean polytope statistic.

## Limitations

The factorization requires a **tree**, equal unweighted incidence generators, the centered canonical Euclidean embedding, and **uniform sampling over vertices**. It does not concern uniform interior volume measure, Gaussian normal-cone-biased vertices, intrinsic spherical width, or arbitrary graph cycles. The law need not extend to weighted trees with arbitrary unequal edge weights; the subtree sign-reversal mechanism yields symmetry but not the claimed degree-only equal-weight factorization. The originality comparison cannot exclude unindexed earlier descriptions under random-orientation imbalance, tree Ising or graph-energy terminology. Independent mathematical audit has not been performed.

## References

1. A. Padrol, V. Pilaud and G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422, first publicly submitted 24 November 2021, §§1.3 and 2, https://arxiv.org/abs/2111.12422.
2. M. Winter, *Classification of Vertex-Transitive Zonotopes*, arXiv:1912.10469, first publicly submitted 22 December 2019, https://arxiv.org/abs/1912.10469.
3. *Sharp width-variance extremizers among tree graphical zonotopes*, publicly available 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-width-variance-extremizers-among-tree-graphical-zonotopes--482983ab9269.
4. *A cubic directional-width law detects degree assortativity in tree graphical zonotopes*, publicly available 18 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-cubic-directional-width-law-detects-degree-assortativity-in-tr--18a26979ef7a.
5. *Third intrinsic volumes of tree graphical zonotopes: an exact formula and sharp path–star bounds*, publicly available 8 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-third-intrinsic-volumes-of-tree-graphical-zonotopes-an-exact-for--17ffdb474fb3.
