# Orthogonal cubical Thales tilings of every right simplex in all dimensions

## Finding

**Theorem.** Let \(d\ge 2\), let \(L_1,\ldots,L_d>0\), and let
\[
P=\operatorname{conv}\{0,L_1e_1,\ldots,L_de_d\}\subset\mathbb R^d.
\]
For **every** \(B=(b_1,\ldots,b_d)\in\operatorname{int}P\), every orthogonal projection of \(B\) onto the affine hull of every nonempty face of \(P\) lies in the relative interior of that face. Moreover, the convex hull \(C_v\) of the projections onto all faces containing a vertex \(v\) is a \(d\)-dimensional orthogonally bipolar polytope combinatorially equivalent to the \(d\)-cube, with antipodal poles \(v,B\). These \(d+1\) cutouts tile \(P\) face-to-face and agree **exactly** with the restricted normal-fan (Thales power-diagram) cells:
\[
 C_v=P\cap(B+N_P(v)),\qquad v\in\{0,L_1e_1,\ldots,L_de_d\}.
\]
In particular, the orthogonal-kernel condition is sufficient for orthogonally bipolar cutout tilings on this entire class in **every** dimension, including \(d\ge4\), a concrete case of the open higher-dimensional tiling question in Pavlík (2026).

## Assumptions and scope

A *right simplex* here means the convex hull of a point and \(d\) mutually orthogonal positive-length edges; Euclidean motion makes it the displayed \(P\). Write \(v_0=0\), \(v_i=L_ie_i\) for \(1\le i\le d\). The point \(B\) is arbitrary subject to
\[
 b_i>0,\qquad \sum_{i=1}^d b_i/L_i<1.
\]
For any nonempty face \(F\), its *orthogonal face point* is \(p_F=\operatorname{proj}_{\operatorname{aff}F}(B)\). For each vertex \(v\), \(C_v=\operatorname{conv}\{p_F:v\in F\}\). The normal cone \(N_P(v)\) consists of directions in which the linear functional is maximized on \(P\) at \(v\). Orthogonally bipolar means the geometric bipolar face-lattice property with distinguished poles and perpendicular interval faces as defined in [1]; it is not merely cubical combinatorics.

## Proof

**1. All face projections are interior.** Every nonempty face is indexed by a nonempty subset \(I\subseteq\{0,1,\ldots,d\}\). If \(0\in I\), the face is the coordinate simplex spanned by the origin and \(v_i\), \(i\in I\setminus\{0\}\), and the projection has coordinates \(b_i\) for \(i\in I\setminus\{0\}\) and zero otherwise. Strict positivity and \(\sum b_i/L_i<1\) put it in the face's relative interior. If \(0\notin I\), the affine hull has coordinates zero outside \(I\) and the equation \(\sum_{i\in I}x_i/L_i=1\). The orthogonal projection is
\[
 (p_I)_i=\begin{cases}
 b_i+\lambda_I/L_i,&i\in I,\\0,&i\notin I,
 \end{cases}\qquad
\lambda_I=\frac{1-\sum_{i\in I}b_i/L_i}{\sum_{i\in I}L_i^{-2}}>0.
\]
Thus it is a strictly positive convex combination of the indicated vertices. Every interior point \(B\) belongs to the orthogonal kernel.

**2. Explicit normal-fan cells.** At the origin, the restricted normal-fan cell is
\[
 D_0=P\cap\{x_i\le b_i\ (1\le i\le d)\}=\prod_{i=1}^d[0,b_i].
\]
The equality with the box follows from \(\sum b_i/L_i<1\). Its vertices are precisely the projections onto faces containing \(0\). For \(v_i\), the normal-cone inequalities \(\langle x-B,v_i-v_j\rangle\ge0\) give
\[
 D_i=\left\{x:\ x_j\ge0,\ \sum_{j=1}^d x_j/L_j\le1,\ t=L_i(x_i-b_i)\ge0,\ x_j\le b_j+t/L_j\ (j\ne i)\right\}.
\]
The inequality \(x_i=b_i+t/L_i\) is automatic by the definition of \(t\). The point \(B\) satisfies the strict simplex inequality, so the facets \(t=0\) and \(\sum x_j/L_j=1\) do not meet in \(D_i\). For each \(j\ne i\), the two constraints \(x_j=0\) and \(x_j=b_j+t/L_j\) are mutually exclusive. Every vertex must therefore have one active constraint from each of the \(d-1\) coordinate pairs and one from the bottom/top pair; conversely each such choice gives a feasible vertex.

At the bottom \(t=0\), for every subset \(J\subseteq\{1,\ldots,d\}\setminus\{i\}\), the vertex has coordinates \(b_j\) for \(j\in J\cup\{i\}\) and zero otherwise. It is the orthogonal projection onto the face \(\operatorname{conv}\{0,v_i,v_j:j\in J\}\). At the top \(\sum x_j/L_j=1\), write \(I=J\cup\{i\}\); the vertex has coordinates \(b_j+\lambda_I/L_j\) for \(j\in I\) and zero otherwise. It is the projection onto \(\operatorname{conv}\{v_j:j\in I\}\). All \(2^d\) choices yield distinct vertices because \(b_j>0\), \(\lambda_I>0\), and the active inequalities uniquely label them. Hence
\[
 C_{v_i}=D_i=P\cap(B+N_P(v_i)).
\]
In particular these are actual vertices, not merely contained face points.

**3. Cubical face lattice and orthogonal bipolarity.** The \(d\) pairs of opposite defining facets are (i) \(t=0\) versus \(\sum x_j/L_j=1\) and (ii) \(x_j=0\) versus \(x_j=b_j+t/L_j\) for \(j\ne i\). Each choice of one facet from every pair gives exactly one vertex, and every choice is realized; thus the full face lattice is that of the \(d\)-cube. The poles \(v_i\) (top, all lower choices) and \(B\) (bottom, all upper choices) are antipodal. The Boolean interval description of the cubical face lattice implies the required geometric bipolar incidence property. Every vertex is a face projection, so the orthogonality of the two interval faces follows from the projection identity and Proposition 4.2 of [1], applicable now that admissibility has been established. For \(C_0\), the same conclusion holds directly: its box facets meet at antipodal poles \(0,B\), and all directions are orthogonal.

**4. Face-to-face tiling.** At every \(x\in P\) some vertex \(v\) maximizes the linear functional \(y\mapsto\langle x-B,y\rangle\), so \(x-B\in N_P(v)\). The complete normal fan has disjoint full-dimensional cone interiors, and intersections of cones are faces. Therefore the \(D_v=C_v\) cover \(P\), have disjoint interiors, and meet face-to-face. Every \(C_v\) is contained in its Euclidean Thales ball with diameter \([v,B]\), because each projection lies on its boundary and the ball is convex. This completes the theorem for every finite dimension \(d\ge2\).

## Verification

The standalone script `check.py` uses exact rational arithmetic to reconstruct all \(2^d\) projections for each cell, compare them with the exhaustive active-constraint formula, and verify every normal-cone halfspace. It tests dimensions \(2\) through \(6\) and nonuniform leg lengths and interior points. It is corroborative: the unlimited-dimensional result follows from the analytic active-constraint proof above.

Run: `python3 check.py` (Python standard library only). A separate local test also matched the total of the Euclidean convex-hull cell volumes with \(\operatorname{vol}(P)=\prod_iL_i/d!\) in 16 nonuniform test cases in dimensions \(2\) through \(5\). No finite test is treated as an exhaustive proof.

## Relationship to prior work

Pavlík [1, Theorem 6.6] proves the equivalence between orthogonal-kernel membership and orthogonally bipolar cutout tilings for dimension three, and poses the higher-dimensional extension as Conjecture 6.8. The general Thales power diagram always partitions a polytope [1, Corollary 5.3]; in general the open question is whether these power cells are **the actual orthogonal-projection cutouts**. We prove this equality and the complete \(2^d\)-vertex cubical structure for all right simplices and every interior anchor. The companion paper [2, Proposition 5.6 and Remark 5.7] supplies an orthogonal cutout construction associated with *regular* simplices and recalls classical combinatorial cubical subdivisions; neither result supplies these metric identities for arbitrary right-simplex leg lengths and arbitrary interior anchor.

## Limitations

The result is confined to right simplices, not arbitrary simplices or polytopes. It does not prove the full higher-dimensional conjecture. The prior-work comparison is provisional, particularly for related classical cubical subdivisions and unpublished presentations of the orthogonal metric condition. The science is self-reviewed, not independently validated.

## References

[1] J. Pavlík, *Thales's theorem in higher dimensions*, arXiv:2611.14277v1 (first public 2026-11-10), https://arxiv.org/abs/2611.14277 . See §§4, 5, 6, 8.

[2] J. Pavlík, *Face lattices of polytopes and bipolar polytopes*, arXiv:2611.13896v1 (first public 2026-11-10), https://arxiv.org/abs/2611.13896 . See §§5–6, especially Proposition 5.6 and Remark 5.7.
