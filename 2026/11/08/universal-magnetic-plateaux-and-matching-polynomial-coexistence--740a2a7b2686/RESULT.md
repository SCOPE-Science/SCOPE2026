# Universal magnetic plateaux and matching-polynomial coexistence for the three-state Potts antiferromagnet on cubic line graphs

## Finding
Let \(G\) be any finite simple cubic graph that admits a proper three-edge-coloring, let \(n=|V(G)|\), and let \(L(G)\) be its line graph. For three-state Potts spins on \(V(L(G))=E(G)\), antiferromagnetic bond coupling \(J>0\), and a field \(h\in\mathbb R\) favoring spin zero, write \(x=h/J\). The exact ground energy is
\[
\frac{E_0(x)}{J}=n\min\left\{1,-\frac{x}{2},1-x,3-\frac{3x}{2}\right\}.
\]
The only changes of ground-state favored-color occupancy occur at \(x=-2,2,4\). In the four open intervals, the favored-color occupancies are respectively \(0,n/2,n,3n/2\), with all configurations meeting that occupancy.

For \(-2<x<2\), the ground-state degeneracy equals \(c_3(G)\), the number of labeled proper three-edge-colorings of \(G\). For \(2<x<4\), it equals \(2^{n/2}m_{n/2}(G)\), where \(m_j(G)\) counts matchings of size \(j\). At \(x=4\), the degeneracy is precisely the matching generating polynomial
\[
M_G(2)=\sum_{j=0}^{n/2}2^j m_j(G).
\]
These identities hold even for disconnected cubic graphs, provided the entire graph is three-edge-colorable.

For the cuboctahedral graph \(L(Q_3)\), the line graph of the eight-vertex cube, the energy reduces to
\[
\frac{E_0}{J}=\min\{8,-4x,8-8x,24-12x\}.
\]
Its degeneracies on the four successive open intervals are \(450,24,144,1\), while the degeneracies at the three transitions \(x=-2,2,4\) are \(3054,2232,689\), respectively. The last equals \(M_{Q_3}(2)\), since the cube matching-size vector is \((1,12,42,44,9)\).

## Assumptions and scope
An edge \(e\in E(G)\) carries a spin \(\sigma_e\in\{0,1,2\}\). Distinct edges of \(G\) are adjacent in \(L(G)\) exactly when they meet at a vertex of \(G\). The Hamiltonian is
\[
H_{J,h}(\sigma)=J\sum_{\{e,f\}\in E(L(G))}\mathbf1_{\{\sigma_e=\sigma_f\}}-h\sum_{e\in E(G)}\mathbf1_{\{\sigma_e=0\}}.
\]
All bonds have the same positive \(J\), all field couplings refer to the same favored color zero, and no other interactions are included. A proper three-edge-coloring gives each vertex of the cubic graph one edge of each color; this hypothesis is essential for simultaneous saturation of all local inequalities. The graph \(G\) is finite, undirected, simple, and three-regular, so \(|E(G)|=3n/2\). Ground-state degeneracy always counts labeled Potts-spin assignments, with no quotient by spin permutations or graph automorphisms.

## Proof
For each original vertex \(v\), the three incident edges induce one triangle in \(L(G)\). Because \(G\) is simple, these triangles partition the edges of the line graph. Let \(t_v\in\{0,1,2,3\}\) be the number of incident original edges assigned spin zero, and let \(b_v\) count equal-spin pairs in its associated line-graph triangle. By the pigeonhole principle, the exact minima \(b_v\ge a_{t_v}\) are
\[
(a_0,a_1,a_2,a_3)=(1,0,1,3).
\]
Indeed, with zero favored spins, two of three spins from \(\{1,2\}\) must agree, and this is tight; with one favored spin, the other two can be different; with two favored spins there is one unavoidable equal pair; with three favored spins all three pairs agree. Each favored edge of \(G\) meets exactly two vertices, so \(\sum_v t_v=2k\), where \(k\) is its global favored-color occupancy. Consequently
\[
\frac{H_{J,h}(\sigma)}{J}=\sum_v\left(b_v-\frac{x}{2}t_v\right)
\ge\sum_v\left(a_{t_v}-\frac{x}{2}t_v\right)
\ge n\min_{t\in\{0,1,2,3\}}\left(a_t-\frac{x}{2}t\right).
\]
The four affine functions in the stated formula are precisely the four terms of this minimum.

For sharpness, fix any proper labeled three-edge-coloring \(\alpha:E(G)\to\{A,B,C\}\). It gives every vertex one incident \(A\), one \(B\), and one \(C\) edge. Construct four global assignments using, respectively, the maps \((A,B,C)\mapsto(1,1,2),(0,1,2),(0,0,1),(0,0,0)\). For all vertices these have \(t_v=0,1,2,3\) and attain \(b_v=a_{t_v}\) simultaneously. Thus every affine branch is globally realizable, and the lower bound is an equality for every real \(x\).

A direct comparison of the four affine terms yields the only breakpoints \(-2,2,4\). Away from those three values, the minimizing local \(t_v\) is unique: respectively \(0,1,2,3\). Hence the total favored-spin count is forced to \(k=nt_v/2\). When \(t_v=1\) at every vertex, equality in \(b_v\ge a_1=0\) forces all three incident spins distinct. Such assignments are precisely proper labeled three-edge-colorings, proving \(c_3(G)\).

When \(t_v=2\) at every vertex, each original vertex is incident to exactly one nonzero spin; those nonzero edges form a perfect matching. Every matching edge can independently carry spin one or two, yielding \(2^{n/2}m_{n/2}(G)\) assignments. At \(x=4\), the minimizing local occupancies are exactly \(t_v=2\) or \(t_v=3\); thus every original vertex meets at most one nonzero edge. The nonzero edges consequently form an arbitrary matching, and every matching edge can independently carry spin one or two. Summation over all matching sizes gives \(M_G(2)\). These correspondences are bijective and establish all general degeneracy formulas.

For the cube \(Q_3\), index vertices by three-bit strings \(0,\ldots,7\), connect two vertices whenever their bitstrings differ in one coordinate, and take the resulting 12 edges as vertices of its line graph. Then \(n=8\), \(|V(L(Q_3))|=12\), \(|E(L(Q_3))|=24\), and the displayed cuboctahedral energy follows directly. A complete exact count of the configurations in each sector produces the following rows, each \((k,b_{\min},d_k)\), with \(b_{\min}\) the least monochromatic-bond count for exactly \(k\) favored spins and \(d_k\) its multiplicity:
\[
\begin{array}{c|rrrrrrrrrrrrr}
k&0&1&2&3&4&5&6&7&8&9&10&11&12\\\hline
b_{\min}&8&6&4&2&0&2&4&6&8&12&16&20&24\\
d_k&450&1248&1044&288&24&288&912&864&144&352&168&24&1
\end{array}
\]
The direct enumerator and an independent local-factor contraction evaluate all \(3^{12}=531441\) assignments; both produce the table. The phase counts follow from the unique active sectors, and each critical count is the sum of the multiplicities of the collinear active sectors. In particular, at \(x=-2\) sectors \(k=0,1,2,3,4\) sum to \(3054\); at \(x=2\) sectors \(k=4,5,6,7,8\) sum to \(2232\); at \(x=4\) sectors \(k=8,9,10,11,12\) sum to \(689\). An independent matching recursion gives \((m_0,m_1,m_2,m_3,m_4)=(1,12,42,44,9)\), so \(M_{Q_3}(2)=1+24+168+352+144=689\).

## Verification
The included Python 3.10+ standard-library programs `verify_direct.py` and `verify_transfer.py` require no external datasets. Run `python verify_direct.py` and `python verify_transfer.py`. The first exhaustively enumerates spin assignments on \(L(Q_3)\), independently computes the cube matching polynomial by recursion, and tests the general affine envelope and two degeneracy formulas on \(K_4\), \(K_{3,3}\), and the triangular prism. The second contracts eight three-spin vertex-local factors with memoized boundary states, independently generating all \(122\) nonzero energy/occupancy coefficients from \(531441\) assignments. They agree on all thirteen sector minima, the three critical degeneracies, and the matching counts. The proof above, not the finite checks, establishes the general theorem.

## Relationship to prior work
Rousochatzakis, Läuchli, and Mila (arXiv:0711.3231, initially public 2007-11-20) motivate the cuboctahedron as a spherical kagomé magnetic cluster; they study quantum/Ising-type antiferromagnetic magnetic spectra rather than this classical three-state Potts field classification. Shrock and Xu (arXiv:1009.1182) establish general field-dependent Potts partition-function and weighted-coloring formalism. Kotecký, Salas, and Sokal (arXiv:0802.2270) study the three-state Potts antiferromagnet on the diced lattice, a different thermodynamic graph. The present claim supplies the evaluated field-dependent ground energy and matching-polynomial degeneracy for every three-edge-colorable cubic line graph, with full cuboctahedral critical counts. General partition-function frameworks alone do not state these evaluated graph-family identities. Historical priority for unindexed equivalent specialized calculations remains uncertain.

## Limitations
The general theorem assumes a proper three-edge-coloring of the finite simple cubic base graph. A three-edge-uncolorable cubic graph need not attain the zero-frustration \(t=1\) branch; for example, this is a genuine structural boundary for snarks. The analysis is restricted to exactly three Potts states, uniform positive antiferromagnetic coupling, a single-color field and zero temperature. The finite cuboctahedral census is exhaustive only for the twelve-spin cluster, not for other line graphs; the general proof does not depend on it. Finite-cluster ground-state level crossings are not claims of thermodynamic bulk phase transitions, nonzero-temperature susceptibility or experimental observability. The counting results do not assert uniqueness relative to all unpublished or unindexed literature.

## References
1. I. Rousochatzakis, A. M. Läuchli, and F. Mila, “Highly Frustrated Magnetic Clusters: The kagomé on a sphere,” arXiv:0711.3231 (first posted 2007-11-20), https://arxiv.org/abs/0711.3231.
2. R. Shrock and Y. Xu, “Exact Results on Potts Model Partition Functions in a Generalized External Field and Weighted-Set Graph Colorings,” arXiv:1009.1182 (first posted 2010-09-07), https://arxiv.org/abs/1009.1182.
3. R. Kotecký, J. Salas, and A. D. Sokal, “Phase transition in the 3-state Potts antiferromagnet on the diced lattice,” arXiv:0802.2270 (first posted 2008-02-15), https://arxiv.org/abs/0802.2270.
