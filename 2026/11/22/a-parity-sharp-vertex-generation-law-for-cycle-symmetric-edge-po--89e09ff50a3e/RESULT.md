# A parity-sharp vertex-generation law for cycle symmetric-edge polytopes

## Finding

For every integer \(n\ge3\), in the hyperplane \(H_n=\{x\in\mathbb R^n:\sum_{i=1}^n x_i=0\}\), let
\[
P_n=\operatorname{conv}\{\pm(e_i-e_{i+1}):i\in\mathbb Z/n\mathbb Z\}.
\]
Writing \(V(P)\) for the vertex set of a polytope, define its optimal vertex-generation weight by
\[
\lambda(P)=\max\{t\in[0,1]:P=(1-t)P+tV(P)\},
\]
where addition is Minkowski addition and the finite set \(V(P)\) is not replaced by its convex hull.

**Theorem (exact parity-sensitive index).** For all \(n\ge3\),
\[
\boxed{\lambda(P_n)=\begin{cases}
\dfrac1{n-1},&n\text{ odd},\\[3pt]
\dfrac1{n-2},&n\text{ even}.
\end{cases}}
\]
Equivalently, the Schneider convexification index of the vertex set is
\[
\boxed{c(V(P_n))=\begin{cases}n-2,&n\text{ odd},\\n-3,&n\text{ even},\end{cases}}
\qquad
c(A)=\inf\{t\ge0:A+t\operatorname{conv}(A)\text{ is convex}\}.
\]
The equalities are attained, and every strictly larger vertex weight fails to cover the polytope. In particular the thresholds for \(n=3,4,5,6,7,8\) are \(1/2,1/2,1/4,1/4,1/6,1/6\), respectively.

A structural lemma established in the proof is independently useful: the free sum of any two centered simplices having \(p\ge2\) and \(q\ge2\) vertices has vertex-generation weight exactly \(1/(p+q-2)\). For odd cycles every facet is a simplex; for even cycles every facet is a free sum of two simplices of equal vertex count. The distinction causes the displayed parity law.

## Assumptions and scope

All graph edges have unit weight, and the geometric realization uses the canonical type-A roots rather than an arbitrary Euclidean rescaling. The parameter \(\lambda\) and Schneider's index are invariant under invertible affine maps of the affine hull; thus their values here do not depend on the Euclidean inner product. Indices are computed in \(H_n\), where \(\dim P_n=n-1\). The cycle \(C_3\) is the triangle. Repeated edge orientations are not counted as distinct vertices: the vertex set consists of the \(2n\) displayed roots, since every root is exposed by the corresponding root direction.

For arbitrary compact \(A\), the convex hull of \(A+t\operatorname{conv}(A)\) equals \((1+t)\operatorname{conv}(A)\), so convexity of that sum is equivalent to equality with the displayed dilate. The exact relation between the two normalizations is \(c(V(P))=1/\lambda(P)-1\). The definition and the basic face-to-body covering principle are due to Artstein-Avidan, Falah and Slomka; they are used as prior theorems, not asserted as new.

## Proof

**1. A free-sum lemma.** For integers \(p,q\ge2\), put
\[
H_p=\{x\in\mathbb R^p:\sum_i x_i=0\},\quad
u_i=e_i-\mathbf 1/p\in H_p,
\]
and similarly \(\omega_j=e_j-\mathbf1/q\in H_q\). Let
\[
Q_{p,q}=\operatorname{conv}\{(\nu_i,0):1\le i\le p\}\cup
\{(0,\omega_j):1\le j\le q\}\subset H_p\oplus H_q.
\]
We prove \(\lambda(Q_{p,q})=1/(p+q-2)\). Any free sum of two simplices whose individual barycenters meet at the origin is affinely equivalent to this model, since the two simplex direction spaces are complementary and the common barycenter supplies the origin.

For \((x,y)\in H_p\oplus H_q\), the gauge of \(Q_{p,q}\) is
\[
\gamma(x,y)=a+b,\qquad
 a=-p\min_i x_i,\quad b=-q\min_j y_j.
\]
Indeed the gauge of the centered standard simplex in \(H_p\) is \(-p\min_i x_i\), and the gauge of a free sum of convex bodies containing the origin is the sum of the two gauges on complementary subspaces. Consequently \((x,y)\in Q_{p,q}\) exactly when \(a+b\le1\). Define the nonnegative slack \(s=1-a-b\), and ranges
\[
R_x=\max_i x_i-\min_i x_i,\qquad R_y=\max_j y_j-\min_j y_j.
\]
For any \(0\le t<1\), the exact criterion for the vertex \((\nu_k,0)\) to supply a covering witness is
\[
(x,y)\in t(\nu_k,0)+(1-t)Q_{p,q}
\iff p t\le p(x_k-\min_i x_i)+s.
\]
To verify this, insert \((x-t\nu_k,y)\) into the gauge inequality \(\gamma\le1-t\). For coordinates other than \(k\), the minimum shifts upward by \(t/p\), automatically satisfying the bound because \(a+b\le1\). The \(k\)-coordinate produces exactly the displayed remaining inequality. The analogous criterion for \((0,\omega_j)\) is \(q t\le q(y_j-\min y)+s\).

As the coordinates in either block sum to zero, \(R_x\ge a/(p-1)\) and \(R_y\ge b/(q-1)\). Let \(d=p+q-2\). Since \(a+b=1-s\), at least one of
\[
 R_x\ge\frac{1-s}{d},\qquad R_y\ge\frac{1-s}{d}
\]
must hold. Moreover \(p,q\le d\) gives
\[
\frac{1-s}{d}\ge\frac1d-\frac{s}{p},\qquad
\frac{1-s}{d}\ge\frac1d-\frac{s}{q}.
\]
Therefore a coordinate achieving the larger range in at least one block supplies a covering vertex at \(t=1/d\). Every point of \(Q_{p,q}\) is covered, proving \(\lambda(Q_{p,q})\ge1/d\).

For sharpness take \(a=(p-1)/d\), \(b=(q-1)/d\). Choose \(x\in H_p\) with one coordinate \(-a/p\) and all other coordinates \(a/[p(p-1)]\); choose \(y\in H_q\) analogously with \(b\) in place of \(a\). Then \(a+b=1\), \(s=0\), and
\[
R_x=R_y=1/d.
\]
For any \(t>1/d\), both groups of covering criteria fail for all vertices. Hence \(\lambda(Q_{p,q})\le1/d\). This proves the free-sum lemma including the case \(p=q=2\).

**2. Complete facet structure of the cycle polytope.** Write \(b_i=e_i-e_{i+1}\). These \(n\) roots span \(H_n\) and have the unique (up to scaling) linear dependence \(\sum_i b_i=0\). The polar of \(P_n\), identified through the isomorphism \(u\mapsto(\langle u,b_i\rangle)_{i=1}^n\), is
\[
S_n=\{c\in[-1,1]^n:\sum_i c_i=0\}.
\]
At any vertex of this section at least \(n-1\) coordinate inequalities of the cube are active. If \(n=2m+1\) is odd, all vertices of \(S_n\) have exactly one zero coordinate and exactly \(m\) plus-ones and \(m\) minus-ones. If \(n=2m\) is even, all vertices have exactly \(m\) plus-ones and \(m\) minus-ones, with no zero coordinate. Conversely every such sign pattern is a vertex of \(S_n\), because \(n-1\) independent active bounds fix the point. These are all the polar vertices and hence all facets of \(P_n\).

For such a polar vertex \(c\), the associated facet is
\[
F_c=\operatorname{conv}\{c_i b_i:c_i\ne0\}.
\]
For odd \(n\), this consists of \(n-1\) affinely independent roots, hence is an \((n-2)\)-simplex. For even \(n=2m\), it has two sets \(A=\{b_i:c_i=1\}\) and \(B=\{-b_i:c_i=-1\}\), each of \(m\) affinely independent points. Their barycenters coincide because
\[
\sum_{c_i=1}b_i-\sum_{c_i=-1}(-b_i)=\sum_i b_i=0.
\]
After translation to that common barycenter, the linear direction spaces of the two simplices are complementary: their dimensions sum to \((m-1)+(m-1)=n-2\), the full facet dimension, and the unique dependence among the \(b_i\) supplies no further relations. Thus every even-cycle facet is affinely equivalent to \(Q_{m,m}\).

**3. Lift sharp facet thresholds to the entire polytope.** A simplex with \(r\) vertices has vertex-generation weight \(1/r\). Its barycenter forces the upper bound (no simplex barycentric coordinate exceeds \(1/r\)); the lower bound follows from choosing a largest barycentric coordinate for every point. By Step 2 each odd-cycle facet has weight \(1/(n-1)\), while the free-sum lemma makes each even-cycle facet's weight \(1/(n-2)\).

The known face-inheritance theorem for vertex generation (Artstein-Avidan–Falah–Slomka, Lemma 2.2) implies that \(\lambda(P_n)\) is no larger than this common facet value. Conversely, each facet is covered by scaled copies centered at its own vertices at that value, so the entire boundary of \(P_n\) is covered. Since \(P_n=-P_n\) is centrally symmetric and the proposed weights lie in \([1/n,1/2]\), the known centrally symmetric boundary-to-body theorem (same paper, Lemma 5.1) implies that all of \(P_n\) is covered. Therefore \(\lambda(P_n)\) equals the common facet value, proving the theorem and the Schneider-index conversion.

## Verification

The standalone `CHECK.py` uses exact rational arithmetic and no third-party packages. It lists every vertex of the polar cube section for \(3\le n\le10\), verifies its facet rank and even-case common barycenter and complementary ranks, and checks the predicted number of facets. Independently, for \(2\le p,q\le5\) it verifies 4,120 convex combinations of free-sum vertices at the sharp threshold and an exact rational uncovered boundary witness above the threshold. Running `python CHECK.py` must print the status recorded in `CHECK_OUTPUT.txt`.

The code tests finitely many exact instances. It does not certify arbitrary dimension; the general result follows from Steps 1–3. No independent mathematical audit is asserted.

## Relationship to prior work

Higashitani, Jochemko and Michałek [1] introduced the present standard symmetric-edge-polytope notation and established general combinatorial facet descriptions. Chen, Davis and Korchevskaia [2] further classify facet subgraphs and affine dependence. The odd/even facet structures used here agree with these antecedents and are not claimed to be new. Artstein-Avidan, Falah and Slomka [3] introduced the normalized vertex-generation weight and proved the face-inheritance and centrally symmetric boundary-lifting lemmas used explicitly above. Their article does not give the cycle-graph weights or the two-simplex free-sum covering calculation.

Published comparison results give exact vertex-set convexification indices for cross-polytope skeleta [4], hypersimplices [5], and demihypercubes [6]. Their objects have different vertex realizations, face structures and coverage gauges. In particular, the full cross-polytope vertex case is not affinely equivalent to \(P_n\) when \(n\ge5\): a cross-polytope in dimension \(n-1\) has \(2n-2\) vertices, whereas \(P_n\) has \(2n\). The original articles' general bounds do not by themselves determine the new parity formula. The proof states which general ingredients are reused and supplies the specific missing calculation.

## Limitations

The theorem is restricted to unweighted simple cycles and vertex-generated coverings; it is not a result about arbitrary graphs, weighted symmetric-edge polytopes, Euclidean Hausdorff distances or vertex exposure probabilities. The result is a self-review, not an independently audited theorem. An equivalent formula in unindexed convexification literature remains possible, and a general closed formula for arbitrary symmetric-edge polytopes is not established.

## References

[1] A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678, first version 20 July 2018, https://arxiv.org/abs/1807.07678 .

[2] T. Chen, R. Davis, E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315, https://arxiv.org/abs/2107.12315 .

[3] S. Artstein-Avidan, T. Falah, B. A. Slomka, *Vertex generated polytopes*, arXiv:2407.20604, first version 30 July 2024, https://arxiv.org/abs/2407.20604 .

[4] *Sharp convexification thresholds for all cross-polytope skeleta*, published 8 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-convexification-thresholds-for-all-cross-polytope-skeleta--77eb9551cb3d .

[5] *Sharp rank–corank convexification of hypersimplex vertex sets*, published 8 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-rank-corank-convexification-of-hypersimplex-vertex-sets--c74758654390 .

[6] *A linear-time nearest-vertex covering certificate for every demihypercube*, published 8 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-linear-time-nearest-vertex-covering-certificate-for-every-demi--fa451ec084a1 .
