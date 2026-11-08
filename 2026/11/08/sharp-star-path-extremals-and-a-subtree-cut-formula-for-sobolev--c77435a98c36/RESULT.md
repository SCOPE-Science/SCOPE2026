# Sharp star–path extremals and a subtree-cut formula for Sobolev evaluation on metric trees

## Finding

Let \(T\) be any finite tree with \(n\ge3\) edges, each realized as a unit interval. Equip it with unnormalized arclength \(ds\). Define the squared sharp embedding constant
\[
\mathcal K(T)=\sup_{\substack{0\ne f\in C(T),\ f|_e\in H^1(e)\\\int_T f\,ds=0}}
\frac{\|f\|_\infty^2}{\int_T|f'|^2\,ds}.
\]
For a vertex \(v\) and an edge \(e\), remove the *open* edge \(e^\circ\), and let \(s_e(v)\) be the number of complete edges in the resulting component that does **not** contain \(v\); this number excludes \(e\) itself. Define
\[
\mathcal Q_T(v)=\frac1{3n}+\frac1{n^2}\sum_{e\in E(T)}s_e(v)[s_e(v)+1].
\]
**Theorem.** Every point-evaluation functional has squared norm \(\mathcal Q_T(x)\), and the global maximum is attained exclusively at vertices of degree one:
\[
\mathcal K(T)=\max_{v\text{ a leaf}}\mathcal Q_T(v),\qquad
1-\frac{2}{3n}\le\mathcal K(T)\le\frac n3.
\]
The lower equality holds if and only if \(T\) is the \(n\)-arm star; the upper equality holds if and only if \(T\) is the \(n\)-edge path. For an edge \(uv\), parameterized by \(t\in[0,1]\) from \(u\) to \(v\), the complete continuum diagonal satisfies
\[
\mathcal Q_T(t)=(1-t)\mathcal Q_T(u)+t\mathcal Q_T(v)-\frac{t(1-t)}n.
\]
If deleting \(uv\) leaves \(a\) whole edges on the \(u\)-side and \(b\) on the \(v\)-side, then \(a+b=n-1\) and
\[
\mathcal Q_T(v)-\mathcal Q_T(u)=\frac{a-b}n.
\]
Thus the sharp constant, all norming points, and the exact loss away from any vertex are obtainable by subtree-size arithmetic. Every nonzero equality function is a real scalar multiple of the centered Green representer associated with a maximizing leaf.

## Assumptions and scope

The tree is finite, connected, acyclic, and has exactly \(n\ge3\) nonzero edges of length one, with no vertex masses. Functions are real, continuous at vertices, and \(H^1\) on every edge. The arclength integral is unnormalized. The mean-zero condition fixes the additive constant, and derivative energy is a Hilbert norm. This is a **continuum** metric-graph problem, not a problem on the discrete vertex set. All supremums are taken over nonzero functions; maxima are attained.

## Proof

**1. Exact evaluation on the tree.** Fix a vertex \(v\), orient every edge away from \(v\), and write \(h=f'\) in those orientations. Unique paths imply that every \(h\in L^2(T)\) integrates to a continuous edgewise-\(H^1\) function, unique modulo constants. The mean-zero condition therefore determines its root value. Denote by \(m_v(t)\) the arclength of the downstream component of the tree left after cutting it at an interior point \(t\). Fubini's theorem for the unique paths gives
\[
0=\int_T f(y)\,dy=n f(v)+\int_T m_v(t)h(t)\,dt,
\qquad f(v)=-\frac1n\int_Tm_v(t)h(t)\,dt.
\]
Cauchy–Schwarz is sharp because every derivative \(h\in L^2(T)\) is allowable, including the choice \(h=-c\,m_v\). Hence
\[
\mathcal Q_T(v)=\frac1{n^2}\int_Tm_v(t)^2\,dt.
\]
On the edge \(e\), parameterized away from \(v\), its downstream length is \(s_e(v)+1-t\). Direct integration gives
\[
\int_0^1[s_e(v)+1-t]^2dt
=s_e(v)[s_e(v)+1]+\frac13,
\]
which proves the subtree formula. Equality functions for evaluation at \(v\) arise by integrating derivatives proportional to \(-m_v\) and imposing zero mean.

**2. The continuum profile and leaf localization.** Let \(G(x,y)\) be the centered reproducing kernel for point evaluations in the derivative Hilbert space. On a metric tree, the squared norm of \(\delta_x-\delta_y\) equals the path distance \(d(x,y)\), since the unique path integral has this exact Cauchy–Schwarz norm. Thus
\[
d(x,y)=G(x,x)+G(y,y)-2G(x,y),\qquad
\int_TG(x,y)dy=0.
\]
Averaging first in \(y\) and then in \(x\) yields
\[
\mathcal Q_T(x)=\frac1n\int_Td(x,y)dy
-\frac1{2n^2}\int_T\int_Td(y,z)dy\,dz.
\]
On any unit edge, the contribution of that edge to \(\int_Td(x,y)dy\) is \(\int_0^1|t-s|ds=t^2-t+1/2\); the contributions from other edges are affine in \(t\). This proves the strict edge profile displayed in the theorem. For adjacent vertices \(u,v\), the distance integral changes by \(+1\) on the component of \(u\), by \(-1\) on the component of \(v\), and integrates to zero over the joining unit edge. Their arclengths are \(a\) and \(b\), giving the reroot identity. Every interior-edge point has smaller \(\mathcal Q\) than at least one endpoint. If a vertex has degree \(k\ge2\), let \(b_1,\dots,b_k\) count whole edges in its adjacent components after deleting their corresponding joining edges. Since \(\sum_i(b_i+1)=n\), some \(b_i<(n-1)/2\); the reroot identity gives a neighbor with strictly larger \(\mathcal Q\). Consequently **only leaves** can maximize.

**3. Sharp lower bound and rigidity.** Root at any leaf \(v\). Its unique incident edge contributes \(s_e(v)=n-1\); all other summands are nonnegative. Therefore
\[
\mathcal Q_T(v)\ge\frac1{3n}+\frac{n(n-1)}{n^2}
=1-\frac{2}{3n}.
\]
Equality at this leaf forces \(s_e(v)=0\) on every other edge. This occurs exactly when every remaining edge is another pendant edge incident with the neighbor of \(v\), that is, exactly for a star. Conversely every leaf of a star has this value, and every nonstar has a strict positive correction at each leaf.

**4. Sharp upper bound and rigidity.** For a tree rooted at \(v\), let \(F(T,v)=\sum_e s_e(v)[s_e(v)+1]\), and set \(H(j)=j(j-1)(j+1)/3\) for integers \(j\ge0\). We prove by induction on the number of edges that \(F(T,v)\le H(n)\), with equality only for a path rooted at an endpoint. Let the branches at \(v\) have \(m_1,\dots,m_k\) edges including their root-incident edges; then \(\sum_i m_i=n\) and
\[
F(T,v)=\sum_{i=1}^k\bigl[m_i(m_i-1)+F(T_i,w_i)\bigr],
\]
where \(T_i\) is the branch with the root-incident edge removed, and \(w_i\) is the attachment vertex. Induction and \(H(m)-H(m-1)=m(m-1)\) give \(F(T,v)\le\sum_iH(m_i)\). Finally,
\[
H(a+b)-H(a)-H(b)=ab(a+b)>0\quad(a,b>0).
\]
Therefore \(\sum_iH(m_i)\le H(n)\), strictly if \(k\ge2\). Equality forces precisely one branch at every step, hence the rooted path. Consequently
\[
\mathcal Q_T(v)\le\frac1{3n}+\frac{H(n)}{n^2}=\frac n3,
\]
and equality occurs exactly when \(T\) is a path and \(v\) is an endpoint. This proves both equality classifications for the sharp global norm.

**5. Equality functions.** The derivative Hilbert space is real and evaluations are continuous. Cauchy–Schwarz and the reproducing kernel show that equality in the global embedding occurs precisely for nonzero multiples of \(G(v,\cdot)\), where \(v\) is a maximizing leaf. No point in an open edge or at a branching vertex can produce equality by step 2.

## Verification

The accompanying standalone standard-library checker independently constructs exact rational Kirchhoff Green solutions on each test tree. It solves the vertex Poisson equations, reconstructs the quadratic edgewise Green function, integrates the derivative energy exactly, and compares this value to the combinatorial subtree formula. It then tests all leaf-localization and star–path equality cases for the checked finite trees. The executed checker reported:

```text
EXACT_INDEPENDENT_QUADRATIC_GREEN_COMPARISONS_PASSED 1870
TREE_EXTREMAL_BOUNDS_AND_EQUALITY_CASES_PASSED 325
ALL_UNIT_TREE_SOBOLEV_CHECKS_PASSED
```

These are finite rational diagnostics only. The universal proof is the Fubini evaluation identity, the reroot/edge-profile identities, and induction above; no enumeration is used to establish claims for arbitrary \(n\).

## Relationship to prior work

Classical Hardy integration on trees, metric-graph Sobolev approximation, electrical-resistance identities, and metric-tree heat kernels provide closely related tools; the component-volume representation and resistance identity are not claimed as new. Evans–Harris–Lang study approximation numbers of path-integration Hardy operators, rather than the maximum arclength-centered point-evaluation norm over **every topology** with fixed unit-edge count. Solomyak's graph-uniform approximation results do not supply the topologically sharp star-versus-path extremal classification. Baker–Faber develop resistance and metric-graph Green theory but do not evaluate these tree-shape sharp constants. Frank–Kovařík study heat kernels, primarily on infinite sparse symmetric trees. The present claim is the joint complete subtree-size evaluation formula, leaf-only extremizers, two sharp all-tree topology bounds with if-and-only-if equality, and the exact edge/reroot profiles. Classical identities might allow a retrospective alternative derivation, and a theorem implicit in less accessible tree-embedding literature remains a priority risk.

## Limitations

The topology bounds require all combinatorial edges to have unit length and the mean to be taken with unweighted continuous arclength. They are not asserted for arbitrary edge lengths, atomic vertex measures, mixed boundary conditions, graphs with cycles, higher-order energies, or complex-valued different normalizations. The originality assessment is a best-knowledge literature comparison, not a guarantee of mathematical priority. Independent external audit has not been performed.

## References

1. W. D. Evans, D. J. Harris and J. Lang, *The approximation numbers of Hardy-type operators on trees*, preprint dated 30 March 2000, arXiv:math/0003215v1, https://arxiv.org/abs/math/0003215 (especially Sections 1–3).
2. M. Solomyak, *On approximation of functions from Sobolev spaces on metric graphs*, preprint dated 23 June 2002, arXiv:math/0206235v1, https://arxiv.org/abs/math/0206235 (especially Sections 1–2 and the tree appendix).
3. M. Baker and X. Faber, *Metrized graphs, electrical networks, and Fourier analysis*, preprint dated 25 July 2004, arXiv:math/0407428v1, https://arxiv.org/abs/math/0407428 (especially Sections 3 and 6).
4. R. L. Frank and H. Kovařík, *Heat kernels of metric trees and applications*, preprint dated 31 August 2011, arXiv:1108.6145v1, https://arxiv.org/abs/1108.6145 (especially Sections 1–2).
