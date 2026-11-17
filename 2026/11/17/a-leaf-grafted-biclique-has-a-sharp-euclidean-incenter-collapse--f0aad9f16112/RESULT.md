# A leaf-grafted biclique has a sharp Euclidean incenter-collapse threshold

## Finding
Let \(p\ge5\) and \(q\ge2\) be integers. Form the graph \(G_{p,q}^{+}\) by taking the complete bipartite graph with vertex parts \(A=\{a_0,\ldots,a_{p-1}\}\) and \(B=\{b_1,\ldots,b_q\}\), and adjoining one pendant vertex \(z\) joined only to \(a_0\). Equip its \(N=p+q+1\) vertices with graph shortest-path distance. Realize its real Lipschitz-free unit ball as the symmetric edge polytope
\[
K_{p,q}^{+}=\operatorname{conv}\{\pm(e_u-e_v):\{u,v\}\in E(G_{p,q}^{+})\}
\subset H=\{x\in\mathbb R^N:\sum_vx_v=0\}
\]
with Euclidean metric inherited from \(\mathbb R^N\). Set \(\varepsilon_p=p\bmod2\) and \(\eta_q=(q+1)\bmod2\). The exact global Euclidean inradius is
\[
\boxed{\rho_{p,q}^{-2}=\max\left\{q+1-\frac{\eta_q}{N},\ p+4-\frac{\varepsilon_p}{N}\right\}.}
\]
The origin is an optimal center. The first expression dominates when \(q>p+3\), the second when \(q<p+3\), and they are equal exactly when \(q=p+3\).

Define the positive integers
\[
A_q=\begin{cases}\binom{q+1}{(q+1)/2},&q\text{ odd},\\2\binom{q+1}{q/2},&q\text{ even},\end{cases}
\quad
B_p=\begin{cases}2\binom{p-1}{(p-4)/2},&p\text{ even},\\2\binom{p}{(p-3)/2},&p\text{ odd}.\end{cases}
\]
Then the number of distinct facets tangent to the largest **origin-centered** Euclidean ball is
\[
\boxed{T_{p,q}=\begin{cases}
B_p,&q<p+3,\\A_q+B_p,&q=p+3,\\A_q,&q>p+3.
\end{cases}}
\]
Let \(\mathcal I_{p,q}\) be the set of centers of **all** largest inscribed Euclidean balls. Its affine dimension is
\[
\boxed{\dim\operatorname{aff}\mathcal I_{p,q}=\begin{cases}
q+1,&q<p+3,\ p\text{ even},\\
q,&q<p+3,\ p\text{ odd},\\
1,&q=p+3,\ p\text{ even},\\
0,&q=p+3,\ p\text{ odd},\\
p,&q>p+3,\ q\text{ odd},\\
p-1,&q>p+3,\ q\text{ even}.
\end{cases}}
\]
In particular, at the sharp threshold the maximal-ball center is **unique for odd \(p\)** but lies in a **nondegenerate line segment for even \(p\)**. For \((p,q)=(5,8)\), one gets \(\rho=\sqrt{14/125}\), \(T=262\), and a unique center. For \((p,q)=(6,9)\), one gets \(\rho=1/\sqrt{10}\), \(T=262\), and a one-dimensional center family.

## Assumptions and scope
All edges have length one, all shortest-path distances are induced by the graph, \(p\ge5\), and \(q\ge2\). The Euclidean norm is the **canonical zero-sum-coordinate norm**; the assertion is not invariant under arbitrary linear isomorphisms of Lipschitz-free spaces. The center-locus dimension is the affine dimension of the set of centers of maximum-radius inscribed balls, not a count of all facet normals or a Banach–Mazur invariant. The bound \(p\ge5\) avoids low-dimensional exceptions in the strict maximizing-pattern and rank classifications.

## Proof
**1. Polar reduction and actual facets.** The metric molecule for nonadjacent vertices is the convex combination of the oriented edge molecules along a shortest path, so the free unit ball equals the displayed edge polytope. Its intrinsic polar is
\[
L=\{f\in H:|f_u-f_v|\le1\text{ for every }\{u,v\}\in E(G_{p,q}^{+})\}.
\]
An affine potential modulo constants is an extreme point of \(L\) if and only if the graph of tight edges \(\{uv:|f_u-f_v|=1\}\) is connected and spanning. Indeed, its signed incidence constraints have rank \(N-1\) exactly under this condition. Every such extreme point corresponds to a distinct facet of \(K_{p,q}^{+}\). By central symmetry and polarity, the largest inscribed Euclidean ball is achievable at zero and
\[
\rho_{p,q}^{-2}=\max_{f\in L}\|f\|_2^2
=\max_f\left(\sum_{v} f_v^2-\frac{(\sum_v f_v)^2}{N}\right).
\]
The squared norm is strictly convex; its maximum is attained only at vertices.

**2. Complete-bipartite core types.** Since the edge incident with \(z\) is a bridge, it must be tight at an extreme potential, so \(f_z=f_{a_0}\pm1\). The restriction to the core must be an extreme potential of the complete-bipartite Lipschitz polytope. Connected tight-edge constraints on the core force, up to an additive constant, one of two forms: (I) \(f|_A=0\) and each \(f_b\in\{-1,1\}\), or (II) \(f|_B=0\) and each \(f_a\in\{-1,1\}\). For completeness, if tightness touches all vertices of the bipartite core, each class must occupy a common value or two values distance \(2\) apart, and only one class can have two levels; the other then occupies their midpoint. This is the established complete-bipartite facet classification [2]. Adding a tight leaf edge preserves spanning connectedness; hence both families enumerate all polar vertices (with harmless duplication at constant-sign core boundaries).

**3. Norm extremization and the threshold.** In type I, both the \(q\) coordinates on \(B\) and \(f_z\) are independent signs, with all \(A\)-coordinates zero. The squared centered norm is \(q+1-S^2/N\), where \(S\) is the sum of \(q+1\) signs. Its maximum is
\[
M_A=q+1-\eta_q/N.
\]
In type II write \(s_0=f_{a_0}\in\{-1,1\}\). If the leaf returns to level zero, \(f_z=0\), then the centered squared norm is at most \(p\). The other leaf choice \(f_z=2s_0\) has squared norm
\[
p+4-\frac{\bigl(3s_0+\sum_{i=1}^{p-1}s_i\bigr)^2}{N}.
\]
For \(p\ge5\), one can choose the remaining \(p-1\) signs so that the absolute sum is precisely \(\varepsilon_p\); no smaller absolute sum is possible by parity. This gives \(M_B=p+4-\varepsilon_p/N>p\), so all returning-leaf patterns are strictly screened. Both \(M_A\) and \(M_B\) are attained. Their difference is
\[
M_A-M_B=q-p-3+\frac{\varepsilon_p-\eta_q}{N}.
\]
The absolute correction is less than one. At \(q=p+3\), the two parity bits agree, so equality holds, proving the exact threshold and radius formula.

**4. Contact counts.** For type I, maximality requires the \(q+1\) signs to have minimum possible imbalance. Their number is \(A_q\). For type II with \(p\) even, fixing \(s_0\) forces exactly \((p-4)/2\) of the remaining signs to agree with it (or, equivalently, determines \(B_p\) patterns as displayed); for odd \(p\), both imbalance signs occur and simple binomial addition gives \(B_p\). Maximizing patterns of the two types are disjoint for \(p\ge5\), because a type-I maximizer vanishes on \(A\) while a type-II maximizer has two signs on \(A\). The formula for \(T_{p,q}\) follows.

**5. The complete center locus.** A radius-\(\rho_{p,q}\) ball with center \(c\in H\) lies in \(K_{p,q}^{+}\) exactly when
\[
\langle c,f\rangle+\rho_{p,q}\|f\|_2\le1
\qquad\text{for each polar vertex }f.
\]
All polar vertices occur in opposite pairs. On the maximal-norm vertices equality at \(c=0\) implies that any admissible center must satisfy \(\langle c,f\rangle=0\). Every noncontact vertex has strictly positive slack at \(c=0\), and only finitely many exist, so a relative neighborhood of zero in this common kernel is feasible. Consequently the affine dimension of the full center locus is exactly the dimension of that kernel.

For type-I contacts, the balanced-sign equations imply that all \(c_b\) and \(c_z\) are equal when \(q\) is odd; when \(q\) is even, the minimally imbalanced sign vectors span the entire \((q+1)\)-coordinate block, forcing all \(c_b=c_z=0\). For type-II contacts, if \(p\) is even all \(c_{a_i}\), \(i\ge1\), have a common value \(\alpha\) and \(c_{a_0}+2c_z=3\alpha\); if \(p\) is odd, \(c_{a_i}=0\) for \(i\ge1\) and \(c_{a_0}+2c_z=0\). These equivalences follow by taking differences of balanced sign choices and then one original sign equation. Adding the zero-sum condition \(\sum_v c_v=0\) gives the six dimension cases displayed above.

At the tie \(q=p+3\), with odd \(p\) the type-I equations set the \(B\) and leaf coordinates to zero, and the type-II equations set all remaining coordinates to zero: uniqueness. With even \(p\), the common kernel is spanned by the zero-sum vector with coordinates \(-5\) at \(a_0\), \(-1\) at each other \(a_i\), and \(+1\) at every \(b\) and at \(z\), giving a nondegenerate interval of centers near zero. This proves the full theorem.

## Verification
Execute `python3 verify.py` using Python 3 without third-party packages. An independently implemented connected-tight-graph enumeration matches the two-type vertex classification in six small graphs (184 vertices). Exact integer centered norms, contact multiplicities, and rational contact-normal ranks match all formulas for 28 further graphs (66,224 polar vertices, 17,116 contact normals). A separate integer comparison checks the precise threshold over 9,044 parameter pairs. The computations are finite checks; the proof above, not the enumeration, establishes all unbounded cases.

## Relationship to prior work
Aliaga [1] establishes general extremal structure of Lipschitz-free unit balls over compact metric spaces, motivating the present intrinsic geometry; the paper does not compute the canonical Euclidean inradius or the center locus of these leaf-grafted biclique metrics. Higashitani–Jochemko–Michałek [2] establish the symmetric-edge-polytope facet description used in the proof and analyze the complete bipartite **core**. The graph-joining results of D'Alì–Delucchi–Michałek [3] concern combinatorial and enumerative behavior of symmetric edge polytopes under vertex identifications; a free-sum description does not preserve the present canonical zero-sum Euclidean norm. Chen–Davis–Korchevskaia [4] analyze tight-edge facet subgraphs, not optimal Euclidean center sets.

Closely related published results about the graph associahedron of \(K_{p,q}\), the one-skeleton Laplacian of the symmetric edge polytope of \(K_{p,q}\), and dense graphs obtained by deleting degree-two subgraphs from complete graphs address different polytopes, invariants, or graph families. None of those inspected results implies the pendant-biclique threshold or its alternating center-locus dimensions. The vertex classification [2] is used as a prior lemma and is not presented as novel.

## Limitations
This result is restricted to a single leaf joined to one vertex of a biclique with \(p\ge5\), \(q\ge2\), unit edge lengths, and the canonical intrinsic Euclidean realization. It does not claim weighted-edge results, several attached leaves, or a classification of other graph families. Prior graph-spread and variance formulations might express parts of the radius differently; exhaustive historical priority or independent review has not been established. The optimal-center *affine dimension*, rather than the exact endpoint positions of its positive-dimensional center polytope, is determined here.

## References
1. Ramón J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219 (first public 2021-02-01), primary MSC2020 46B20; Mediterranean Journal of Mathematics 19 (2022), article 32.
2. Akihiro Higashitani, Katharina Jochemko and Mateusz Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678 (first public 2018-07-20), especially complete-bipartite facet classification, Proposition 3.4.
3. Alessio D'Alì, Emanuele Delucchi and Mateusz Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193 (first public 2019-10-11), especially graph-joining discussion.
4. Tianran Chen, Robert Davis and Evgeniia Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315 (first public 2021-07-26), Theorem 3.
