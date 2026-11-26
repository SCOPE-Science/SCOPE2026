# Singer quotients of projective-plane nonincidence independence complexes

## Finding

Let \(q\geq2\) be a prime power, \(\Pi=\operatorname{PG}(2,q)\) its projective plane, \(N=q^2+q+1\), and \(G=C_N\) a Singer cyclic group acting regularly on its points and lines. Form the bipartite **nonincidence graph** \(B_q\) with one vertex per point and one vertex per line, and an edge precisely when the corresponding point and line are *not incident*. Put \(X_q=|\operatorname{Ind}(B_q)|\). Then the ordinary geometric orbit space satisfies

\[
\boxed{X_q/G\simeq\bigvee^{q} S^2.}
\]

The unquotiented space satisfies \(X_q\simeq\bigvee^{1+N(q-1)} S^2\). The integral Singer action on its second homology is

\[
\boxed{\widetilde H_2(X_q;\mathbb Z)\cong
\mathbb Z\oplus\mathbb Z[G]^{q-1}},
\]

where \(G\) acts trivially on the first summand and by left translation on each regular summand. All other reduced integral homology groups of \(X_q\) vanish. The orbit space is simply connected and has torsion-free second integral homology of rank \(q\).

## Assumptions and scope

The group action is the simultaneous Singer action on the two vertex shores, not point–line duality. Independence means no chosen point–line pair is *nonincident*. The quotient is the **topological** orbit space of the geometric realization, with all stabilizers retained; it is not a naive vertex-orbit simplicial quotient. The quotient map of \(X_q\) is not assumed to be a covering: the Singer action fixes the shore barycenters. No assertion is made for non-Desarguesian planes without a Singer group, nor for arbitrary subgroups of the collineation group. Equivariant equivalences are indicated explicitly below.

Write \(P\) and \(L\) for the point and line sets. A point-only face is any subset of \(P\). A mixed face with point part \(S\subseteq P\) and nonempty line part \(T\subseteq L\) exists exactly when every point of \(S\) lies on every line in \(T\).

## Proof

**1. An equivariant suspension.** Let \(U=\Delta(P)\) and \(V=\bigcup_{\ell\in L}\operatorname{st}_{\operatorname{Ind}(B_q)}(\ell)\), with closed simplicial stars. Every face containing a line belongs to the corresponding closed star, so \(\operatorname{Ind}(B_q)=U\cup V\). Both pieces are invariant under \(G\); \(|U|\) contracts equivariantly to its barycenter. For a nonempty face \(\sigma\) of \(V\), let \(A(\sigma)\) be the set of all lines incident to all points of \(\sigma\) (all lines when \(\sigma\) has no points). This set is nonempty by the definition of \(V\). The union \(\sigma\cup A(\sigma)\) is itself a face of \(V\). Inclusions of faces reverse inclusions of the sets \(A(\sigma)\).

An explicit equivariant homotopy sends the barycenter of each \(\sigma\) in the barycentric subdivision of \(V\) to the barycenter of \(A(\sigma)\). For a chain \(\sigma_0\subset\cdots\subset\sigma_k\), triangulate its prism with each simplex having bottom vertices of indices \(0,\ldots,i\) and top vertices of indices \(i,\ldots,k\) for some \(i\). Map the bottom vertices to the original face barycenters and the top vertices to the line-set barycenters. All their supports lie in the single face \(\sigma_i\cup A(\sigma_i)\), so affine interpolation maps to \(|V|\). The constructions restrict to the faces of each prism and respect the action. At the top the image is in \(\Delta(L)\), which contracts equivariantly to its fixed barycenter. Thus \(|V|\) is equivariantly contractible.

The intersection \(K=U\cap V\) is exactly the complex of point subsets lying on a projective line:
\[
 K=\bigcup_{\ell\in L}\Delta(P_\ell),
\]
where \(P_\ell\) consists of the \(q+1\) points on \(\ell\). The invariant subcomplex inclusions are equivariant cofibrations. The union is modeled by the equivariant homotopy pushout of \(|U|\leftarrow |K|\to |V|\). Replacing the outer terms by points gives an equivariant homotopy equivalence
\[
 X_q\simeq_G\Sigma |K|,
\]
where the suspension is unreduced, with two fixed poles. Passing to ordinary orbit spaces gives \(X_q/G\simeq\Sigma(|K|/G)\).

**2. An explicit equivariant graph spine.** Distinct projective lines meet at one point, so the line simplices \(\Delta(P_\ell)\) intersect only in vertices. Select a center \(c(\ell_0)\) in one line and transport this choice to each line by the regular Singer action. In each line simplex, pair every face \(A\subseteq P_\ell\setminus\{c(\ell)\}\) of size at least two with \(A\cup\{c(\ell)\}\). Remove pairs in decreasing order of \(|A|\). At each stage the only remaining strict coface of \(A\) is its paired coface, since other cofaces are removed at larger sizes and no face with at least two vertices lies on two different lines. Thus these are relative simplicial collapses; the matching of free faces and cofaces is equivariant. Collapsing each orbit of free pairs simultaneously gives an equivariant deformation retraction onto the graph \(T\) consisting of the edges from each center \(c(\ell)\) to the other \(q\) points of its line.

The graph \(T\) has \(N\) vertices and \(Nq\) edges. Any two points lie on a line and are joined by a path through its center, so \(T\) is connected. The Singer action on vertices is free, and an element stabilizing an edge stabilizes its unique line, so the action on edges is free with no inversions. The quotient has one vertex and \(q\) loops. Therefore
\[
|K|/G\simeq T/G\cong\bigvee^{q}S^1,
\qquad
X_q/G\simeq\Sigma(T/G)\simeq\bigvee^{q}S^2.
\]
Similarly, \(T\) has first Betti number \(Nq-N+1\) and \(X_q\simeq\bigvee^{1+N(q-1)}S^2\). In both cases the ordinary reduced suspension of a based connected graph is homotopy equivalent to its unreduced suspension.

**3. The integral Singer lattice.** Let \(R=\mathbb Z[G]=\mathbb Z[t]/(t^N-1)\). It is the graph map \(T\to T/G\) that is a regular covering. With edges oriented away from their chosen line centers, the equivariant cellular boundary is \(R^q\to R\) with entries \(t^{d_i}-1\), where the \(d_i\) are the differences along star edges in the base line. There exists a point \(a\) in the base line with \(t a\) also in the base line: take a line through any point and its translate by \(t\), then translate that line to the base line. Equivalently, the Singer difference set has a pair of difference one. Choose \(a\) as the center. Then one boundary entry is \(t-1\), and each other entry is a multiple of \(t-1\) in \(R\). Elementary column operations over \(R\) transform the differential to \((t-1,0,\ldots,0)\). Its kernel is
\[
 \ker(t-1:R\to R)\oplus R^{q-1}
 =\mathbb Z(1+t+\cdots+t^{N-1})\oplus R^{q-1}.
\]
The first summand has trivial action. The equivariant unreduced suspension transports this lattice isomorphically from \(H_1(T;\mathbb Z)\) to \(\widetilde H_2(X_q;\mathbb Z)\).

## Verification

The Python 3 standard-library script `verify.py` checks all differences and point-pair incidences for specified cyclic models at \(q=2,3,4\) and constructs the corresponding equivariant line-star graphs. At \(q=2\), it separately constructs a stellar subdivision of the fourteen-vertex independence complex at the two full shore simplices and forms signed integral cellular boundary matrices of the geometric quotient. The orbit-cell vector in dimensions zero through six is \((4,11,22,22,16,8,2)\). The script checks that consecutive boundary products vanish. Integer unit-pivot **chain cancellations** reduce the chain complex to one copy of \(\mathbb Z\) in degree zero and two in degree two, with all other groups zero. This certifies the integral homology for that case, not a topological collapse, a fundamental-group computation, or a homotopy-type certificate. The wedge equivalences, including at \(q=2\), follow from the geometric proof. Reproduce the finite checks using `python3 verify.py` with the recorded checker.

## Relationship to prior work

Barmak's star-cluster and bipartite independence-complex methods motivate the suspension viewpoint; Tsukuda's general incidence-graph/Alexander-duality theorem provides a broader nonequivariant comparison. An underlying suspension alone does not compute the cyclic geometric quotient or its integral Singer lattice. Published computations of the Heawood **incidence** independence complex use the complementary bipartite adjacency convention. Fano cap complexes, projective-plane matroid independence complexes, and Lovász neighborhood complexes of nonincidence graphs also use different simplicial constructions. The claim concerns the projective-plane line-simplex graph spine, its cyclic quotient, and the integral module determined by its regular graph covering.

## Limitations

The theorem assumes a prime-power Desarguesian projective plane with a Singer cycle and does not address arbitrary finite projective planes. It determines ordinary homotopy types and the integral degree-two representation, not an equivariant simple-homotopy type under all collineations. Computational tests use only orders two, three and four, with an additional exact quotient-chain calculation at order two. Equivalent results in differently indexed literature cannot be excluded by the comparisons above.

## References

1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first public 2010-07-02, https://arxiv.org/abs/1007.0418.
2. S. Tsukuda, *Independence complexes and incidence graphs*, *Contributions to Discrete Mathematics* 12 (2017), 28–46, https://doi.org/10.55016/ojs/cdm.v12i1.62277.
3. J. W. P. Hirschfeld, *Projective Geometries over Finite Fields*, Oxford University Press, 1998, for finite projective planes and Singer cycles.
4. J. A. Barmak, *Algebraic Topology of Finite Topological Spaces and Applications*, Lecture Notes in Mathematics 2032, 2011, for simplicial collapses and finite-poset homotopy methods.
