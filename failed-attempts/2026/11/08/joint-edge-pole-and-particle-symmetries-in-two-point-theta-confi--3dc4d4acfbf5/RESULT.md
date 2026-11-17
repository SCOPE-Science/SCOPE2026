# Joint edge, pole, and particle symmetries in two-point theta configurations

## Finding

For every integer \(m\geq3\), let \(\Theta_m\) be the graph formed by \(m\) internally disjoint arcs with the same endpoints \(A,B\), regarded as a metric graph with all arms parametrized by \([0,1]\). Put
\[
F_m=\{(x_1,x_2)\in\Theta_m^2:x_1\neq x_2\}.
\]
The commuting actions of arm permutations, simultaneous pole reversal, and particle exchange form \(G_m=S_m\times C_2^{\mathrm{pole}}\times C_2^{\mathrm{part}}\). The induced integral pole-reversal operator is exactly minus the identity on \(H_1(F_m;\mathbb Z)\).

The integral homology is torsion free:
\[
H_0(F_m;\mathbb Z)=\mathbb Z,\qquad
H_1(F_m;\mathbb Z)=\mathbb Z^{m^2-m-1},\qquad
H_k(F_m;\mathbb Z)=0\quad(k\geq2).
\]
For \(\sigma\in S_m\), let \(f(\sigma)\) be its number of fixed arms and \(c_2(\sigma)\) its number of two-cycles. Write \(p,t\in\{0,1\}\) for powers of pole and particle exchange. The complete first rational homology character is
\[
\operatorname{tr}\bigl((\sigma,p,t)\mid H_1(F_m;\mathbb Q)\bigr)
=(-1)^p\begin{cases}
f(\sigma)^2-f(\sigma)-1,&t=0,\\
1-2c_2(\sigma),&t=1.
\end{cases}
\]

There is a structural description of the **entire joint rational representation**. Let \(\mathbb Q[E_m]\) have basis \(e_{ij}\) for ordered distinct arms \(1\leq i\neq j\leq m\); set \(s=\sum_{i\neq j}e_{ij}\). On this space define the actions
\[
\sigma e_{ij}=e_{\sigma(i),\sigma(j)},\qquad
p e_{ij}=-e_{ij},\qquad
t e_{ij}=-e_{ji}.
\]
The line \(\mathbb Qs\) is stable under all three actions, and
\[
\boxed{H_1(F_m;\mathbb Q)\cong\mathbb Q[E_m]/\mathbb Qs}
\]
as a \(G_m\)-module. This is a **rational** isomorphism; no integral identification with this quotient lattice is claimed.

For \(m\geq4\), the eigenspace of particle exchange with eigenvalue \(+1\) is, as an \(S_m\times C_2^{\mathrm{pole}}\)-module, the pole-sign twist of \(S^{(m-1,1)}\oplus S^{(m-2,1,1)}\). The eigenvalue \(-1\) space is the pole-sign twist of \(S^{(m-1,1)}\oplus S^{(m-2,2)}\). For \(m=3\), these reduce respectively to \(S^{(2,1)}\oplus S^{(1,1,1)}\) and \(S^{(2,1)}\), each pole-sign twisted. Their dimensions are \(m(m-1)/2\) and \(m(m-1)/2-1\). In particular \(H_1(F_m;\mathbb Q)^{S_m}=0\).

## Assumptions and scope

The graph \(\Theta_m\) has two vertices of valence \(m\) and \(m\) topological edges. The two particles are **ordered** and never collide, including at the poles. Pole reversal changes a point at fractional coordinate \(u\) on arm \(i\) to coordinate \(1-u\) on that same arm. Particle exchange interchanges \(x_1\) and \(x_2\). All three actions commute. No statement concerns sink configurations, unordered configuration spaces, or numbers of particles other than two.

For cellular computations subdivide each arm into exactly three oriented edges, from \(A\) through \(u_i,v_i\) to \(B\). The finite deleted-product subcomplex \(D_m\) consists of ordered pairs of closed cells of this subdivision with disjoint supports. Its inclusion in \(F_m\) induces a \(G_m\)-equivariant isomorphism on homology: the inclusion is natural and the underlying homotopy equivalence is the classical deleted-product retraction [1, Section 1].

## Proof

**Homology and connectivity.** Lütgehetmann and Recio-Mitter [2, Proposition 5.4 and proof] show, for \(m\geq3\), that the ordered two-point banana-graph configuration space is homotopy equivalent to a connected graph: in their cubical model every two-cell has a free one-face that permits a collapse. In particular \(H_1\) is integral free and all \(H_k\) for \(k\geq2\) vanish. Independently, the planar-graph theorem of Barnett and Farber [1, Theorem 6.1] gives zero second homology, since all faces of a theta graph have closures containing both poles, so no two face closures are disjoint.

The deleted-product cell counts can be obtained directly. There are \(V=2+2m\) subdivided graph vertices and \(E=3m\) oriented graph edges. Therefore \(C_0(D_m)\) has \(V(V-1)=4m^2+6m+2\) cells; \(C_1(D_m)\) has \(2E(V-2)=12m^2\) cells; and \(C_2(D_m)\) has \(7m^2-5m\) cells. The latter counts ordered pairs of edges with no common endpoint, or equivalently \(E^2+E-\sum_v\deg(v)^2\). Thus \(\chi(D_m)=2+m-m^2\); connectivity and absence of higher homology imply \(\operatorname{rank}H_1=m^2-m-1\).

**Signed Lefschetz character.** Orient the three edges of each arm from \(A\) to \(B\), and order product-cell coordinates by particle label. Each pole reversal reverses the orientation of every graph edge. Particle exchange acts on an edge-times-edge cell with the additional Koszul sign \(-1\). Let \(f=f(\sigma)\), \(c=c_2(\sigma)\). Direct enumeration of the cells stabilized as oriented cells produces the following integer chain traces; the columns are \(\operatorname{tr}C_0,\operatorname{tr}C_1,\operatorname{tr}C_2\):

| Pole exchange \(p\) | Particle exchange \(t\) | \(\operatorname{tr}C_0\) | \(\operatorname{tr}C_1\) | \(\operatorname{tr}C_2\) |
| --- | --- | --- | --- | --- |
| \(0\) | \(0\) | \((2+2f)(1+2f)\) | \(12f^2\) | \(7f^2-5f\) |
| \(1\) | \(0\) | \(0\) | \(0\) | \(f(f-1)\) |
| \(0\) | \(1\) | \(4c\) | \(0\) | \(-2c\) |
| \(1\) | \(1\) | \(2+2f+4c\) | \(0\) | \(-2f-6c\) |

Here is a direct justification of every nonzero type. When neither involution acts, fixed vertices and edges occur precisely on fixed arms; there are \(2+2f\) fixed vertices and \(3f\) fixed edges. There are \(12f^2\) fixed product one-cells and \(7f^2-5f\) disjoint ordered fixed-edge pairs. With pole exchange only, no graph vertex is fixed and the only fixed edges are the \(f\) reversed middle edges, of which \(f(f-1)\) ordered pairs are disjoint; the two edge-orientation reversals cancel. With particle exchange only, fixed ordered vertex pairs arise from the \(2c\) transposed arms, giving \(4c\) pairs; the \(2c\) disjoint transposed-middle-edge pairs contribute negatively in degree two. With both exchanges, fixed vertex pairs consist of the two poles, \(2f\) inner-vertex pairs on fixed arms, and \(4c\) pairs on transposed arms. Fixed oriented degree-two pairs are the \(2f+4c\) outer-edge pairs and \(2c\) middle-edge pairs, all with negative product-swap sign. One-cells can only contribute when particle exchange is absent and both graph factors are individually fixed.

The alternating sums of the three chain traces are, in table order,
\[
2+f-f^2,\qquad f^2-f,\qquad 2c,\qquad 2-2c.
\]
Since \(H_0\) is the trivial representation and all other nonzero homology is in degree one, the Lefschetz formula gives \(\operatorname{tr}(g\mid H_1)=1-\sum_{k=0}^2(-1)^k\operatorname{tr}(g\mid C_k)\). This proves the stated character for all \(m\) and all group elements.

**Module and integral pole action.** The ordered-pair module \(\mathbb Q[E_m]\) has trace \(f(f-1)\) without particle exchange and \(-2c\) with it; the one-dimensional line \(\mathbb Qs\) has particle-exchange trace \(-1\). Pole exchange acts by \(-1\) on both. Thus its quotient has precisely the derived character. Complete reducibility over \(\mathbb Q\) proves the equivariant isomorphism. The \(+1\) particle-exchange eigenspace is \(\bigwedge^2\mathbb Q^m\), whereas the \(-1\) eigenspace is the two-subset permutation module modulo its constant line; standard symmetric-group decompositions yield the displayed Specht constituents. Finally the pole-only character is \(-(m^2-m-1)\). The pole operator is an involution on the rational \(H_1\), so all its eigenvalues are \(-1\); it is \(-I\) over \(\mathbb Q\), hence exactly \(-I\) on the torsion-free integral lattice.

## Verification

Run `python3 theta_character_verify.py` and `python3 theta_ranks_verify.py` in the directory containing both programs. The first program reconstructs all deleted-product cells, checks \(\partial_1\partial_2=0\) over the integers, checks chain equivariance on all one- and two-cells for four generating automorphisms, and independently compares the claimed formula with signed Lefschetz traces for every group element for \(m=3,4,5,6\), totaling 3,480 actions. The second computes full boundary ranks modulo each of \(2,3,5\) for \(m=3,4,5,6,7\). Their deterministic outputs are included as `character_output.txt` and `ranks_output.txt`. The finite tests check implementation and sign conventions; the all-parameter proof above is combinatorial and does not extrapolate these tests to infinitely many \(m\).

## Relationship to prior work

Barnett and Farber [1] established deleted-product methods, an Euler-characteristic formula, and planar second-homology generators. These methods determine the nonequivariant homology rank here but do **not** by themselves state the joint arm/pole/particle representation. Lütgehetmann and Recio-Mitter [2] proved the needed graph-homotopy type for \(F_2(\Theta_m)\), with a lower bound on its first Betti rank; they focused on topological complexity rather than the symmetry character. An and Maciążek [3] studied geometric graph-braid presentations including theta graphs, notably higher-particle examples, not the present all-parameter two-particle character.

The result also differs from calculations for sink configurations, where particle collision at designated vertices is allowed, and from higher-particle theta-class relations or metric Rips complexes on theta graphs. The new claim is the exact joint representation, with the integral pole-reversal conclusion, not the established underlying graph homotopy type. A hidden equivalent calculation in the broader graph-braid literature remains possible.

## Limitations

The displayed permutation-quotient description is proved over \(\mathbb Q\), not as an integral \(\mathbb Z[G_m]\)-lattice isomorphism. Only the integral scalar action of pole reversal and the integral Betti groups are asserted. No complete integral simultaneous eigensublattice or extension classification is given. Results apply only to two labeled collision-free particles on equal-arm generalized theta graphs and do not address higher-particle configuration spaces, equivariant homotopy, or metric dependence for unequal, non-symmetric arm lengths.

## References

[1] Kathryn Barnett and Michael Farber, *Topology of configuration space of two particles on a graph, I*, arXiv:0903.2180v1 (first public 2009-03-12), especially Lemma 1.1, Corollary 1.2 and Theorem 6.1. https://arxiv.org/abs/0903.2180

[2] Daniel Lütgehetmann and David Recio-Mitter, *Topological complexity of configuration spaces of fully articulated graphs and banana graphs*, arXiv:1806.00659 (first public 2018-06-02), especially Proposition 5.4 and its proof. https://arxiv.org/abs/1806.00659

[3] Byung Hee An and Tomasz Maciążek, *Geometric Presentations of Braid Groups for Particles on a Graph*, Communications in Mathematical Physics (2021), DOI:10.1007/s00220-021-04095-x, especially Sections 4–5. https://doi.org/10.1007/s00220-021-04095-x
