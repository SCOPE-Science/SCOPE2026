# Six-vertex saturation of Euclidean vertex robustness in cycle symmetric-edge polytopes

## Finding
For each integer \(n\ge3\), let \(e_1,\ldots,e_n\) be the standard orthonormal basis of \(\mathbb R^n\), take indices cyclically, and define \(r_i=e_i-e_{i+1}\). Let
\[
P_n=\operatorname{conv}\{\pm r_i:1\le i\le n\},\qquad Q_n=\operatorname{conv}\bigl(\{-r_1\}\cup\{\pm r_i:2\le i\le n\}\bigr).
\]
The squared Euclidean distance from the deleted vertex to the remaining-vertex hull is exactly
\[
\boxed{\operatorname{dist}(r_1,Q_n)^2=\begin{cases}
\frac12&n=3,\\
\frac45&n=4,\\
\frac9{10}&n=5,\\
\frac{11}{12}&n\ge6.
\end{cases}}
\]
Every vertex of \(P_n\) has the same deletion distance. Moreover, the exposed face of \(Q_n\) containing the unique projection of \(r_1\) has precisely \(\min\{n-1,4\}\) vertices and affine dimension \(\min\{n-2,3\}\). For \(n\ge6\), those are the four oriented roots \(-r_2,-r_3,-r_{n-1},-r_n\), so both the squared distance and the dimension of the nearest face become independent of the cycle length. The directed Hausdorff distance from \(P_n\) to \(Q_n\) equals this same deletion distance.

## Assumptions and scope
The ambient Euclidean metric is the restriction of the standard coordinate metric on \(\mathbb R^n\) to the hyperplane \(\sum_i x_i=0\). Each root \(r_i\) has squared length \(2\); no alternative nonorthogonal coordinate quotient is being used. Every \(\pm r_i\) is an actual vertex of \(P_n\): the functional \(x\mapsto\langle r_i,x\rangle\) attains its strict maximum \(2\) at \(r_i\), whereas all other distinct signed edge roots have scalar product at most \(1\). The result is for all integers \(n\ge3\), without an upper cutoff, and concerns deletion of one oriented-root vertex, not deletion of an underlying graph edge together with both orientations.

## Proof
By the dihedral action on the cycle together with central inversion, all \(2n\) vertices are equivalent under Euclidean symmetries. It suffices to delete \(r_1\). Put \(m=n-1\) and \(b_j=r_{j+1}\) for \(1\le j\le m\). The cycle identity is \(r_1=-\sum_{j=1}^m b_j\). The Gram matrix of \((b_j)\) is the path tridiagonal matrix
\[
G_{jj}=2,\qquad G_{j,j+1}=G_{j+1,j}=-1,\qquad G_{jk}=0\text{ if }|j-k|>1.
\]
Define nonnegative weights \(s=(s_1,\ldots,s_m)\) of total mass one by
\[
s=\begin{cases}
(\frac12,\frac12), &n=3,\\
(\frac25,\frac15,\frac25), &n=4,\\
(\frac25,\frac1{10},\frac1{10},\frac25), &n=5,\\
(\frac5{12},\frac1{12},0,\ldots,0,\frac1{12},\frac5{12}),&n\ge6.
\end{cases}
\]
The last line has exactly \(n-5\) zeros, including one zero when \(n=6\). Set \(q=-\sum_{j=1}^m s_j b_j\in Q_n\), \(v_j=1-s_j\), and \(y=r_1-q=-\sum_{j=1}^m v_jb_j\). Let \(h_j=\langle y,-b_j\rangle=(Gv)_j\). Direct multiplication of the tridiagonal matrix gives the following complete certificate:

* If \(n=3\), all \(h_j=1/2\).
* If \(n=4\), all \(h_j=2/5\).
* If \(n=5\), all \(h_j=3/10\).
* If \(n=6\), the ordered vector \(h\) is \((1/4,1/4,1/6,1/4,1/4)\).
* If \(n\ge7\), \(h_1=h_2=h_{m-1}=h_m=1/4\), while the other entries are nonnegative and strictly smaller than \(1/4\). Explicitly, they are \(1/12\) immediately next to those pairs and zero elsewhere, with overlapping positions counted only once.

Thus every \(h_j\) lies between zero and a common bound \(\lambda\), equal to \(1/2,2/5,3/10,1/4\) in the four respective regimes. Equality \(h_j=\lambda\) holds exactly when \(s_j>0\). Consequently \(\langle y,q\rangle=\sum_j s_jh_j=\lambda\). For every other vertex \(z\) of \(Q_n\), either \(z=-b_j\) with \(\langle y,z\rangle=h_j\le\lambda\), or \(z=b_j\) with \(\langle y,z\rangle=-h_j\le\lambda\), or \(z=-r_1=\sum_j b_j\) with \(\langle y,z\rangle=-\sum_jh_j<\lambda\). Therefore
\[
\langle r_1-q,z-q\rangle\le0\qquad(z\in Q_n).
\]
This is the exact Euclidean nearest-point characterization, proving that \(q\) is the unique metric projection of \(r_1\) onto \(Q_n\). Computing \(\langle y,y\rangle=v^T Gv\) yields the four asserted squared distances. The inequalities above are strict except at the listed \(-b_j\) with \(s_j>0\); those vectors are affinely independent because the path roots \(b_1,\ldots,b_m\) are linearly independent. Their convex hull is therefore the precise exposed contact face and \(q\) is in its relative interior.

Finally, the map \(x\mapsto\operatorname{dist}(x,Q_n)\) is convex. Its maximum over \(P_n=\operatorname{conv}(Q_n\cup\{r_1\})\) is attained at one of these generating points; all points of \(Q_n\) have distance zero, so the directed Hausdorff distance is precisely \(\operatorname{dist}(r_1,Q_n)\). This also proves the single-vertex robustness statement by cycle symmetry.

## Verification
Run `python check_cycle_robustness.py` with Python 3, NumPy, and SciPy. The deterministic checker performs exact-fraction calculations of the candidate, squared norm, every supporting inequality, and the equality-face cardinality for \(3\le n\le160\); it independently minimizes the complete \((2n-1)\)-vertex quadratic program for \(3\le n\le18\). Successful output is:

`CYCLE_VERTEX_ROBUSTNESS_PASS exact_n=158 independent_qp_n=16 cutoff=6 plateau_squared=11/12`

The finite checker tests particular values only. The all-dimensional conclusion follows from the tridiagonal support inequalities proved above. No floating-point minimization is used to infer an infinite statement.

## Relationship to prior work
The general parameter measuring the distance from a vertex to the convex hull of the other vertices (and its use in vertex-enumeration stability) is established in Awasthi–Kalantari–Zhang (2018). The symmetric-edge-polytope construction, its connection to graph metrics, and the even-cycle face-vector theory are established in D'Alì–Delucchi–Michałek (2019/2022). Chen–Davis–Korchevskaia (2021/2022) give an explicit characterization of face and facet subgraphs. Those works are not claimed as new here. The assertion proved here is the exact **Euclidean** vertex-deletion robustness, its stable four-vertex projection face, and the sharp onset at \(n=6\). The cited face counts, projection algorithms, and facet-subgraph classifications do not state this exact metric value. Historical priority remains provisional.

## Limitations
The robustness and face profiles apply to the canonical orthonormal root realization of **unweighted simple cycles**. They are not asserted for arbitrary weighted cycles, other graphs, or nonorthogonal unimodular changes of coordinates; Euclidean lengths are not invariant under general unimodular maps. The finite numerical checks are corroborative, not independent mathematical certification. No independent mathematical audit has been performed, and unindexed earlier literature may contain an equivalent formula.

## References
1. P. Awasthi, B. Kalantari, Y. Zhang, *Robust Vertex Enumeration for Convex Hulls in High Dimensions*, first public preprint 2018-02-05, arXiv:1802.01515, https://arxiv.org/abs/1802.01515. In particular the introduction defines the minimum vertex-to-other-hull distance and explains its use.
2. A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, first public preprint 2019-10-11, arXiv:1910.05193, https://arxiv.org/html/1910.05193v1. Sections 2.1, 3.1 and 4.1 describe signed edge roots and cycle face enumerations.
3. T. Chen, R. Davis, E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, first public preprint 2021-07-26, arXiv:2107.12315, https://arxiv.org/html/2107.12315v2. Sections 3–5 study facet/face subgraphs and cycle constructions.
