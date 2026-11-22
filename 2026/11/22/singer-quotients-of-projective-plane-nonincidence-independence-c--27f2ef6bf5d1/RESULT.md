# Singer quotients of projective-plane nonincidence independence complexes

## Finding

Let \(q\geq2\) be a prime power, \(\Pi=\operatorname{PG}(2,q)\) its projective plane, \(N=q^2+q+1\), and \(G=C_N\) a Singer cyclic group acting regularly on its points and lines. Form the bipartite **nonincidence graph** \(B_q\) with one vertex per point and one vertex per line, and an edge precisely when the corresponding point and line are *not incident*. Put \(X_q=|\operatorname{Ind}(B_q)|\). Then the ordinary geometric orbit space satisfies

\[
\boxed{X_q/G\simeq\bigvee^{q} S^2.}
\]

More precisely, the underlying complex has \(X_q\simeq\bigvee^{1+N(q-1)} S^2\), and its entire integral deck representation is

\[
\boxed{\widetilde H_2(X_q;\mathbb Z)\cong
\mathbb Z\oplus\mathbb Z[G]^{q-1}},
\]

where \(G\) acts trivially on the first summand and by left translation on each regular summand. All other reduced integral homology groups vanish. The orbit space is simply connected and has torsion-free second integral homology of rank \(q\).

## Assumptions and scope

The group action is the simultaneous Singer action on the two vertex shores, not point–line duality. Independence means no chosen point–line pair is *nonincident*. The quotient is the **topological** orbit space of the geometric realization, with all stabilizers retained; it is not a naive vertex-orbit simplicial quotient. No assertion is made for non-Desarguesian planes without a Singer group, nor for arbitrary subgroups of the collineation group. All equivalences are ordinary homotopy equivalences, with the equivariant equivalence used explicitly below.

Write \(P\) and \(L\) for the point and line sets. A point-only face of \(\operatorname{Ind}(B_q)\) is any subset of \(P\). A mixed face with point part \(S\subseteq P\) and nonempty line part \(T\subseteq L\) exists exactly when every point of \(S\) lies on every line in \(T\).

## Proof

**1. An equivariant suspension.** Let \(U=\Delta(P)\) be the full point simplex and let
\(V=\bigcup_{\ell\in L}\operatorname{st}_{\operatorname{Ind}(B_q)}(\ell)\), where stars are closed simplicial stars. Every face containing a line belongs to the corresponding closed star, so \(\operatorname{Ind}(B_q)=U\cup V\). Both \(U\) and \(V\) are invariant under \(G\). The barycenter of \(U\) is \(G\)-fixed, so \(U\) is \(G\)-contractible. All finite intersections of stars of lines are nonempty, because the lines themselves form a simplex; specifically, the intersection indexed by nonempty \(T\subseteq L\) equals the closed star of the simplex \(T\), and its stabilizer fixes the barycenter of \(T\). The equivariant nerve lemma for a finite invariant cover by subcomplexes with stabilizer-contractible intersections therefore gives \(V\simeq_G\Delta(L)\simeq_G *\), the latter contraction ending at its fixed barycenter.

The intersection \(K=U\cap V\) has precisely the point subsets lying on at least one projective line. Thus
\[
K=\bigcup_{\ell\in L}\Delta(P_\ell),
\]
where \(P_\ell\) is the \(q+1\)-point set incident to \(\ell\). The subcomplex inclusions are cofibrations. Replacing both equivariantly contractible pieces in the homotopy pushout by fixed points gives a natural \(G\)-homotopy equivalence
\[
X_q\simeq_G\Sigma |K|,
\]
with \(G\) acting on the equator and fixing the two suspension poles. Hence \(X_q/G\simeq\Sigma(|K|/G)\).

**2. An explicit equivariant graph spine.** Distinct projective lines meet in one point, so the line simplices \(\Delta(P_\ell)\) intersect only in vertices. Select an incident point \(c(\ell_0)\) of one line and transport this choice by the regular Singer action to each line. In each line simplex, match every face \(A\subseteq P_\ell\setminus\{c(\ell)\}\) with \(A\cup\{c(\ell)\}\) whenever \(|A|\ge2\). Remove matching pairs in decreasing order of \(|A|\). The first face is always free: its only possible unremoved coface is the paired face, since higher-dimensional cofaces have already been removed. No face of size at least two lies on two distinct projective lines. Thus these collapses are simultaneous and equivariant across all lines, and leave exactly the edges from \(c(\ell)\) to the other \(q\) points of each line. Call the resulting graph \(T\).

The graph \(T\) has \(N\) vertices and \(Nq\) edges. All point pairs lie on some line, whose chosen star contains a path joining them, so \(T\) is connected. The Singer group acts freely on its vertices and edges: a nonidentity element fixes neither a point nor a line, and every edge belongs to a unique line. Thus the quotient \(T/G\) has one vertex and exactly \(q\) edges, each a loop. Consequently
\[
|K|/G\simeq T/G\cong\bigvee^{q}S^1,
\qquad
X_q/G\simeq\Sigma(T/G)\simeq\bigvee^{q}S^2.
\]
The unreduced suspension of a connected wedge of circles has the stated based homotopy type. Similarly \(T\) is a connected graph of first Betti number \(Nq-N+1=1+N(q-1)\), so \(X_q\simeq\bigvee^{1+N(q-1)}S^2\).

**3. The integral Singer lattice.** Let \(R=\mathbb Z[G]=\mathbb Z[t]/(t^N-1)\). The graph \(T\to T/G\) is a regular covering. The quotient is the rose of \(q\) loops, so its equivariant cellular chain complex is \(R^q\xrightarrow{(t^{d_1}-1,\dots,t^{d_q}-1)}R\), with the differences \(d_i\) determined by the chosen star in a base line. Singer regularity produces a cyclic planar difference set \(D\subseteq\mathbb Z/N\mathbb Z\), representing one line; every nonzero difference appears exactly once. In particular there are \(a,b\in D\) with \(b-a\equiv1\pmod N\). Choose the center of that base line to be \(a\). Then one displayed boundary entry is exactly \(t-1\), and each other entry \(t^{d_i}-1\) is a multiple of \(t-1\) in \(R\). Elementary column operations over \(R\) transform the differential to \((t-1,0,\dots,0)\). Its kernel is
\[
\ker(t-1:R\to R)\oplus R^{q-1}
=\mathbb Z(1+t+\cdots+t^{N-1})\oplus R^{q-1}.
\]
Suspension transports this module exactly to \(\widetilde H_2(X_q;\mathbb Z)\). Its first summand is the trivial \(G\)-lattice, proving the assertion.

## Verification

The standalone Python 3 standard-library program `verify.py` exhaustively checks Singer cyclic difference sets and all pairs of line intersections for orders \(q=2,3,4\), and constructs equivariant line-star graphs. For \(q=2\), it separately constructs a stellar subdivision of the fourteen-vertex independence complex (subdividing the two full shore simplices to account for fixed barycenters), forms the **signed integral quotient cellular chain**, and checks all products of adjacent boundaries vanish. Its orbit-cell vector in dimensions zero through six is \((4,11,22,22,16,8,2)\). Exact unit-pivot cellular cancellations leave one zero-cell and two two-cells and no others, independently recovering \(S^2\vee S^2\) for the first case. These finite calculations test the model and algebra; the all-prime-power theorem follows from the geometric proof above, not extrapolation from computations. Reproduce using `python3 verify.py`.

## Relationship to prior work

The older star-cluster and bipartite independence-complex methods of Barmak motivate the suspension viewpoint; Tsukuda's later general incidence-graph/Alexander-duality theorem likewise supplies a broad nonequivariant comparison. Neither inspected source identifies the **nonincidence** projective-plane family's Singer orbit homotopy or its integral deck lattice. Published computations of the Heawood **incidence** independence complex concern the complementary bipartite adjacency convention, whose homotopy type and order-seven character are different. Published Fano cap-complex Moore quotients, projective-plane *matroid* independence quotients, and Lovász neighborhood complexes of nonincidence graphs use different simplicial constructions; their conclusions do not imply the present quotient formula. The new input is the line-simplex graph spine together with its regular cyclic covering and explicit integral group-ring boundary.

## Limitations

The theorem assumes a prime-power projective plane with a Singer cycle and does not address arbitrary finite projective planes. It determines homotopy types and the integral degree-two representation but not an equivariant simple-homotopy type under all collineations. Computational tests run only for orders two, three and four, with an additional exact quotient chain computation in order two. Mathematical review has been performed on the stated proof and checks, but no independent external audit has been performed. An equivalent theorem in differently indexed literature cannot be excluded solely by the searches recorded.

## References

1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first public 2010-07-02, https://arxiv.org/abs/1007.0418.
2. S. Tsukuda, *Independence complexes and incidence graphs*, *Contributions to Discrete Mathematics* 12 (2017), 28–46, https://doi.org/10.55016/ojs/cdm.v12i1.62277.
3. J. W. P. Hirschfeld, *Projective Geometries over Finite Fields*, Oxford University Press, 1998, for finite projective planes and Singer cycles (background only).
4. J. A. Barmak, *Algebraic Topology of Finite Topological Spaces and Applications*, Lecture Notes in Mathematics 2032, 2011, for simplicial collapses and finite-poset homotopy methods.
