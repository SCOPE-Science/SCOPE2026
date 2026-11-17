# Triple-free boundary rigidity in nearly free smooth-conic arrangements

## Finding

Let \(\mathcal C\subset\mathbf P^2_{\mathbf C}\) be a nearly free reduced union of \(k\ge2\) distinct smooth conics, with no singularities other than nodes \(A_1\), tacnodes \(A_3\), transverse triple points \(D_4\), and two-branch contacts \(A_5,A_7\). Suppose **no transverse triple points occur**. Then \(k\le5\). If \(k=5\), its entire necessary singularity-count vector is
\[
(n_2,t_3,n_3,t_5,t_7)=(13,0,0,1,6).
\]
Moreover, the simple graph on the five conics whose edges represent \(A_7\)-contacts is necessarily \(K_{2,3}\), and the single \(A_5\)-contact pair is a nonedge of that graph. This is a **necessary** five-conic configuration: no geometric realization is asserted.

In the narrower class having only nodes and \(A_7\)-contacts, \(k\le4\), and this bound is attained by the four-conic nearly free example already known in the literature. The general upper bound \(k\le6\), without the triple-free assumption, was established previously and is *not* claimed as a new theorem here.

## Proof

Put \(K=k(k-1)\) and denote the numbers of \(A_1,A_3,D_4,A_5,A_7\) points by \(n_2,t_3,n_3,t_5,t_7\), respectively. Pairwise Bézout and local Tjurina numbers give
\[
2K=n_2+2t_3+3n_3+3t_5+4t_7,\qquad
\tau=n_2+3t_3+4n_3+5t_5+7t_7.
\]
The known Dimca–Sernesi/Pokora lower bound \(r=\operatorname{mdr}(f)\ge5k/4-2\), together with the near-free condition \(r\le k\), forces \(r=k\) for \(5\le k\le8\). The already-published general ceiling \(k\le6\) excludes larger \(k\); for the remaining \(k=5,6\), the nearly-free Tjurina formula thus yields \(\tau=3K\). Eliminating \(\tau\) gives
\[
K=t_3+n_3+2t_5+3t_7,\qquad n_2=t_5+2t_7-n_3.
\]
The published Zieliński orbifold inequality for exactly these singularity types reads
\[
560k+100n_2+75n_3\ge184t_3+404t_5+608t_7.
\]
Substituting yields
\[
159n_3+64t_5+144t_7\ge184K-560k.
\]
Since there are no triple points, \(n_3=0\), and
\[
64t_5+144t_7\le48(2t_5+3t_7)\le48K,
\]
so \(136k(k-1)\le560k\). This excludes \(k=6\). For \(k=5\), \(K=20\), hence
\[
2t_5+3t_7\le20,\qquad64t_5+144t_7\ge880.
\]
If \(t_7\le5\), the first bound implies \(64t_5+144t_7\le848\). If \(t_7=6\), it gives \(t_5\le1\), while the second requires \(t_5\ge1\). Larger \(t_7\) are impossible. Thus \(t_7=6,t_5=1\), and the preceding equalities yield \(t_3=0,n_2=13\). For \(k<5\), the asserted component bound is automatic.

The \(A_7\)-contact graph is triangle-free. Indeed, if two distinct conics \(Q_2,Q_3\) meet \(Q_1\) in order four at distinct points \(P,Q\) (distinctness follows from the excluded three-branch contacts), put \(Q_1=xz-y^2\), \(P=[1:0:0]\), \(Q=[0:0:1]\) by projective coordinates. After scaling their equations, the restrictions to \(Q_1\) having divisors \(4P,4Q\) imply
\[
Q_2=Q_1+\alpha z^2,\qquad Q_3=Q_1+\beta x^2,\quad\alpha\beta\ne0.
\]
Their difference \(\alpha z^2-\beta x^2\) is the product of two distinct lines. Those lines meet at \([0:1:0]\), which is not on \(Q_2\) or \(Q_3\), so their common intersection divisor with either conic has support at two or more distinct points. Consequently \(Q_2,Q_3\) cannot have a single order-four contact. Thus no three \(A_7\)-contact edges form a triangle. A triangle-free simple graph on five vertices with six edges is precisely \(K_{2,3}\) by the equality case of Mantel's theorem. The unique \(A_5\) pair cannot also be an \(A_7\) edge: such an edge already uses all four pairwise Bézout intersections.

If only nodes and \(A_7\) occur, the forced five-conic basket is impossible because it needs one \(A_5\); therefore \(k\le4\). For sharpness, an earlier published construction gives four smooth conics
\[
\begin{aligned}
Q_0&=x^2+y^2-z^2,&Q_1&=2x^2+y^2+2xz,\\
Q_2&=x^2+y^2+2xz,&Q_3&=4x^2+6y^2+4xz-8z^2.
\end{aligned}
\]
Their reduced union has eight nodes and four order-four two-branch contacts, with \(\tau=36\) and \(\operatorname{mdr}(Q_0Q_1Q_2Q_3)=3\). The standard near-free numerical criterion for degree eight gives \(36=(8-1)^2-3(8-3-1)-1\), so it is nearly free. The construction and its minimal-syzygy certificate are prior; it is included only to demonstrate sharpness.

## Motivation, comparison, and scope

Five and six smooth conics are the first component counts for which existence of nearly free unions with the specified ADE singularities remains open. The no-triples boundary is a natural incidence restriction; forcing an exact five-conic basket and a unique six-edge contact graph rules out almost all candidate configurations without assuming that the remaining one is realizable. This structural reduction is distinct from the earlier general \(k\le6\) theorem and its modulo-five exclusion of \(k=7,8\), which are **not** new here. The sharp four-conic witness and its full stratum were also established previously. The result makes no existence assertion at five or six conics, does not classify configurations with triple points, and does not settle projective realizability of the \(K_{2,3}\) five-conic contact graph.

The arithmetic necessary conditions can be checked by exhaustive integer enumeration for \(k=5,6\), but the theorem follows from the displayed elimination and Mantel argument; the finite census is not used as a proof of geometric nonexistence.

## References

1. P. Pokora, *On free and nearly free arrangements of conics admitting certain ADE singularities*, arXiv:2303.08584 (2023), notably the near-free criterion, syzygy lower bound, and four-conic example.
2. M. Zieliński, *On plane conic arrangements with A5 and A7 singularities*, Rendiconti del Circolo Matematico di Palermo (2023/2024), Theorem 1.1 (orbifold inequality), DOI:10.1007/s12215-023-00890-8.
3. *A six-component ceiling for nearly free smooth-conic arrangements with A1,A3,D4,A5,A7 singularities* (2026-11-02), https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-a-six-component-ceiling-for-nearly-free-smooth-conic-arrangement--c7898da4d723 . The previously published universal six-component ceiling.
4. *Singularity strata and the unique nearly-free member of an explicit four-conic family* (2026-10-13), https://github.com/Resultary/2026/tree/main/2026/10/13/SCOPE-singularity-strata-and-the-unique-nearly-free-member-of-an-expli--849decf44190 . The prior sharp four-conic example and its Jacobian certificate.
