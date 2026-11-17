# Integral two-sphere loss under one missing Boolean-cube edge

## Finding

Let \(n\ge3\), let \(Q_n\) be the simple graph on \(\{0,1\}^n\) with edges at Hamming distance one, choose **any** graph edge \(e\), and set \(G=Q_n-e\). The **open neighborhood complex** \(\mathcal N(G)\) has a simplex on a nonempty vertex set \(A\) precisely when some graph vertex is adjacent to every vertex of \(A\). Put
\[
\mu_n=2^{n-3}(n^2-5n+8)-1,\qquad \lambda_n=\mu_n-(n-2).
\]
Then \(\mathcal N(G)\) has exactly two connected components, which are simplicially isomorphic and each have integral homotopy type
\[
\bigvee^{\lambda_n}S^2.
\]
The empty wedge is a point; thus both components are contractible for \(n=3\). For \(n=4,5,6,7,8\) their sphere multiplicities are respectively \(5,28,107,346,1017\). No reduced integral homology in any other degree occurs.

More precisely, let \(K'\subset K\) denote the inclusion of either parity component of \(\mathcal N(Q_n-e)\) into the corresponding component of \(\mathcal N(Q_n)\). The induced map
\[
H_2(K';\mathbb Z)\longrightarrow H_2(K;\mathbb Z)
\]
is a split injection with free cokernel \(\mathbb Z^{n-2}\). The edge-stabilizing group \(\mathfrak S_{n-1}\) that permutes the coordinates orthogonal to \(e\) acts on this cokernel as the **integral augmentation lattice**
\[
I_{n-1}=\ker\bigl(\mathbb Z^{n-1}\xrightarrow{\text{sum}}\mathbb Z\bigr).
\]
In particular, the \(n-2\) lost classes are represented by explicit four-vertex tetrahedral-boundary spheres in \(K\), described in the proof. Splitting is asserted as abelian groups, not equivariantly.

## Assumptions and scope

The graph has no loops, neighborhoods are open (not closed), and \(e\) is one deleted graph edge, not a deleted vertex or a change of metric. All assertions hold integrally for every integer \(n\ge3\). The two parity sheets have distinct vertex sets and are exchanged by a graph automorphism translating every binary vector by the direction of the missing edge. An empty wedge is interpreted as a contractible complex.

## Proof

**1. Parity reduction and unique large faces.** Translate/permute coordinates so the removed edge joins the even vertex \(u=0\) to the odd vertex \(v=e_1\), where \(e_i\) are unit vectors over \(\mathbb F_2\). Each open neighborhood lies wholly in the parity class opposite its center, so the neighborhood complex is the disjoint union of its even- and odd-vertex sheets. Both sheets are connected: their one-skeleton is the halved cube, joining two same-parity vertices at Hamming distance two, which is connected for \(n\ge3\). Translation by \(e_1\) exchanges the endpoints of the removed edge and consequently induces a simplicial isomorphism between the two sheets. Analyze the even sheet.

Let \(K\) be the intact even sheet and \(K'\) its edge-deleted counterpart. The facets generating \(K\) are \(F_w=N_{Q_n}(w)\), with \(w\) odd. Two distinct odd centers have at most two common even neighbors (exactly two when their Hamming distance is two, none otherwise). Consequently a face with three or more vertices lies in a *unique* generating facet. The sole changed facet is \(F_v\), replaced with \(F_v\setminus\{u\}\). Every old edge persists, because an even-even pair of Hamming distance two has exactly two odd common neighbors, and removal of one incidence cannot destroy both supports. Every larger face involving \(u\) and contained in \(F_v\) disappears; all other faces survive.

**2. Explicit collapse to dimension two.** For every unchanged generating facet \(F_w\), choose a vertex \(a_w\in F_w\). For each base face \(\sigma\subseteq F_w\setminus\{a_w\}\) having at least three vertices, pair \(\sigma\) with \(\sigma\cup\{a_w\}\), processing base faces in descending cardinality. The pair is an elementary free-face collapse: every other larger coface of \(\sigma\) was already removed, and no other generating facet contains \(\sigma\), by the two-common-neighbor observation. Repeat for the trimmed facet \(F_v\setminus\{u\}\), which can have only two vertices when \(n=3\). This removes every simplex of dimension at least three and leaves a two-dimensional CW (indeed simplicial) complex, without changing homotopy type. Hence \(H_j(K';\mathbb Z)=0\) for \(j\ge3\), and the same applies to \(K\).

**3. Simple connectivity of both sheets.** The intact sheet has one-skeleton the Cayley graph of the even-vector group with generating steps \(e_i+e_j\). Set \(t_i=e_1+e_i\) for \(2\le i\le n\); these form a basis for that group. Any edge of type \(e_i+e_j\), where \(i,j\ge2\), can be replaced homotopically by a two-edge path of types \(t_i,t_j\), since the corresponding triangular loop is supported by the odd center \(x+e_i\) at any even basepoint \(x\). The four-cycle for commuting steps \(t_i,t_j\) is the union of two neighborhood triangles, supported respectively by \(x+e_i\) and \(x+e_j\). All \(t_i\) are involutions. Commuting steps and deleting adjacent repeated steps therefore contract every closed walk, proving \(\pi_1(K)=0\).

For \(K'\), the only triangles missing from \(K\) are
\[
T_{ij}=\{0,e_1+e_i,e_1+e_j\}\qquad (2\le i<j\le n).
\]
Set \(z_{ij}=e_i+e_j\). The boundary of each missing triangle still bounds a *three-triangle disk* in \(K'\), on vertices \(\{0,e_1+e_i,e_1+e_j,z_{ij}\}\). The three surviving triangles are supported by odd centers \(e_i\), \(e_j\), and \(e_1+e_i+e_j\), respectively, all different from the damaged center \(e_1\). Thus every original triangular relator still holds in \(K'\). The one-skeleta of \(K'\) and \(K\) agree, so \(\pi_1(K')=0\).

**4. Exact Euler characteristic and integral homotopy.** Write \(V=2^{n-1}\). The even sheet has \(f_0=V\) vertices and \(f_1=2^{n-2}\binom n2\) edges. All faces of size \(k\ge3\) have unique odd centers, so their counts in the damaged sheet are
\[
f_{k-1}(K')=(V-1)\binom nk+\binom{n-1}k \qquad(3\le k\le n).
\]
For the intact sheet, replace the right-hand side by \(V\binom nk\). The alternating binomial identity \(\sum_{k=0}^n(-1)^k\binom nk=0\) gives
\[
\widetilde\chi(K)=\mu_n,\qquad \widetilde\chi(K')=\mu_n-(n-2)=\lambda_n.
\]
Both sheets are connected, simply connected, and homotopy equivalent to two-complexes. Therefore their only possible nonzero reduced integral homology is \(H_2\), necessarily free (as a subgroup of the free group of two-chains), with the displayed ranks. Integral Hurewicz and the homological Whitehead theorem give the asserted wedges of two-spheres (including the zero-rank contractible case).

**5. Inclusion and primitive local sphere classes.** Put \(F=F_v\). The intersection \(L=K'\cap 2^F\) is exactly the full simplex \(2^{F\setminus\{u\}}\), together with the \(n-1\) distinct edges from \(u\) to the other vertices of \(F\). Contracting the base simplex shows \(L\simeq\bigvee^{n-2}S^1\). Since \(K=K'\cup2^F\), excision for this simplicial pair yields
\[
H_j(K,K';\mathbb Z)\cong\widetilde H_{j-1}(L;\mathbb Z)
=\begin{cases}\mathbb Z^{n-2},&j=2,\\0,&j\ne2.\end{cases}
\]
As \(H_1(K')=0\), the long exact sequence yields a split short exact sequence
\[
0\longrightarrow H_2(K';\mathbb Z)\longrightarrow H_2(K;\mathbb Z)\longrightarrow\mathbb Z^{n-2}\longrightarrow0.
\]
For every \(2\le i<j\le n\), the four vertices \(\{0,e_1+e_i,e_1+e_j,e_i+e_j\}\) span exactly the **boundary** of a tetrahedron in \(K\): the four triples have the four distinct odd centers \(e_1,e_i,e_j,e_1+e_i+e_j\), while no single odd center supports all four vertices. Their oriented fundamental \(2\)-cycles map to the relative classes of \(T_{ij}\). Fixing \(i=2\) and allowing \(j=3,\ldots,n\) gives a primitive basis of the relative group: it is the usual rank-\(n-2\) edge-cycle quotient for a complete graph on \(n-1\) nodes, obtained by collapsing the common base simplex. Hence those explicit embedded sphere classes furnish an integral complement of \(H_2(K')\) in \(H_2(K)\).

Finally, \(\mathfrak S_{n-1}\) permutes the \(n-1\) vertices of \(F\setminus\{u\}\) and fixes \(u\). Consequently it permutes the corresponding \(n-1\) arcs in \(L\), and \(H_1(L;\mathbb Z)\) is precisely their sum-zero lattice \(I_{n-1}\). Excision identifies this naturally with the inclusion cokernel. The odd sheet obeys the identical argument by the translation symmetry.

## Verification

The standalone script `edge_check.py` constructs the open neighborhood complexes from *the graph neighborhoods themselves*, independently for both parity classes after deleting the edge \(\{0,e_1\}\). It enumerates every nonempty face for \(3\le n\le8\), verifies the full face-count formula and the parity-exchanging simplicial isomorphism, and computes the ranks of the first three simplicial boundary operators over \(\mathbb F_2\). Its observed \((\beta_0,\beta_1,\beta_2)\) are \((1,0,\lambda_n)\) in all twelve parity-sheet cases. There were 77,718 nonempty faces across these cases. See `edge_check.out` for the recorded output. These finite tests corroborate but do not establish the universal integral theorem or the equivariant lattice statement; those follow from the proof.

## Relationship to prior work

Arana and Stehlík (2025), *Quadrangulations and the Lovász complex*, study topological and equivariant aspects of neighborhood/Lovász complexes, predominantly for non-bipartite quadrangulations; their surface classification does not apply to these bipartite cubical edge defects. A publicly indexed 2026 result, *Neighborhood complexes of hypercubes collapse to explicit 2-sphere wedges*, gives the intact-cube count \(\mu_n\). The intact rank is recovered here by a self-contained argument; the **one-edge loss, primitive integral inclusion, and augmentation module** are separate deletion-specific statements. Prior classifications for *vertex*-punctured cubes concern deleting graph vertices and do not imply the edge-deletion behavior: deleting an edge keeps both vertices and all one-skeleton edges in the neighborhood complex. Index and literature searches found no covering claim, but cannot certify absence of unindexed work.

## Limitations

This theorem treats exactly one deleted edge, ordinary **open** neighborhood complexes, and the specified integral homology inclusion. The wedge equivalence is not claimed equivariant; no conclusion is made for arbitrary multiple-edge deletions, other graph families, or closed-neighborhood complexes. The closest indexed intact-cube result was available as an abstract/summary rather than material full text, leaving a limited novelty risk, and no independent mathematical audit has been performed.

## References

1. C. Arana and M. Stehlík, *Quadrangulations and the Lovász complex*, arXiv:2510.03698, first submitted 2025-10-04, https://arxiv.org/abs/2510.03698 (full online text inspected).
2. *Neighborhood complexes of hypercubes collapse to explicit 2-sphere wedges*, publicly indexed mathematical research record, 2026-10-11 (indexed theorem statement inspected; full manuscript not accessible).
3. L. Lovász, *Kneser's conjecture, chromatic number, and homotopy*, Journal of Combinatorial Theory, Series A **25** (1978), 319–324 (definition of the neighborhood complex).
4. A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002 (Hurewicz and Whitehead theorems).
