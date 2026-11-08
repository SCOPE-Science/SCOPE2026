# Induced-matching edge-pivot mobility in squared cycles

## Finding

**Theorem.** Let \(n\ge5\) be an integer, and let \(G_n=C_n^2\) be the simple graph on \(\mathbb Z/n\mathbb Z\) in which vertices at cyclic separation one or two are adjacent. Let \(\nu_s(G_n)\) denote the largest cardinality of an induced matching (a collection of edges whose endpoints induce precisely those edges). Define \(\mathcal P_n\) to have as vertices all induced matchings of cardinality \(\nu_s(G_n)\), with two configurations adjacent when exactly one selected edge is replaced by a distinct graph edge sharing exactly one endpoint with the deleted edge and the result remains an induced matching.

Write \(n=4k+r\), where \(k\ge1\) and \(0\le r\le3\). Then
\[
\nu_s(G_n)=k,
\qquad
|V(\mathcal P_n)|=
\begin{cases}
4,&r=0,\\
2n,&r=1,\\
2kn,&r=2,\\
\dfrac{n(4k^2+2)}{3},&r=3.
\end{cases}
\]
The \(r=0\) case here necessarily has \(k\ge2\). Moreover,
\[
\mathcal P_n\cong4K_1 \quad\text{if }r=0;
\qquad
\mathcal P_n\text{ is connected if }r\in\{1,2,3\}.
\]
In particular, the four maximum strong matchings in a squared cycle of order divisible by four are entirely edge-pivot frozen, while at every other admissible order every maximum strong matching can reach every other through maximum strong matchings by incident-edge replacements.

The connectivity theorem and complete optimum-state count are the proposed new claims. The general definition of an induced matching, its conflict-graph representation, and prior results on ordinary independent-set reconfiguration are not new claims.

## Assumptions and scope

All graphs are finite, simple, undirected and vertex-labelled. The cycle-square edge set consists of all unordered pairs \(\{i,i+1\}\) and \(\{i,i+2\}\) modulo \(n\). Since \(n\ge5\), every edge has one unique clockwise representation \((i,i+a)\) with \(a\in\{1,2\}\). The induced-matching rule requires any endpoint of one selected edge to have cyclic distance at least three from any endpoint of any other selected edge. The move is **whole-edge pivoting** at a common original-graph endpoint, not arbitrary one-edge replacement and not token sliding on the conflict graph \(L(G_n)^2\).

No claim about the reconfiguration diameter, edge counts, or higher powers of cycles is made.

## Proof

**1. Cyclic block encoding.** Consider an induced matching \(M\) with \(m\ge2\) edges. For every selected edge \(e=\{u,u+a\}\) with clockwise length \(a\in\{1,2\}\), no other selected edge has an endpoint strictly inside the clockwise arc from \(u\) to \(u+a\), because an interior vertex (when it exists) is adjacent to both endpoints of \(e\). Thus the two endpoints of each selected edge form a consecutive block in the cyclic ordering of all chosen endpoints. Enumerate the matching edges clockwise as \(e_i=\{s_i,s_i+a_i\}\), with \(a_i\in\{1,2\}\) and cyclic index \(i\in\{1,\dots,m\}\). Distinct blocks cannot have endpoints at cyclic distance one or two, so the next start is \(s_{i+1}=s_i+a_i+3+g_i\) along the clockwise cycle, for a uniquely determined integer \(g_i\ge0\). Summing the increments gives
\[
n=\sum_{i=1}^{m}(a_i+3+g_i)\ge4m.
\]
For \(m=1\), the upper bound \(m\le\lfloor n/4\rfloor\) is immediate from \(n\ge5\). Conversely, \(k=\lfloor n/4\rfloor\) short edges at positions \(\{4j,4j+1\}\), for \(0\le j<k\), form an induced matching. Hence \(\nu_s(G_n)=k\).

**2. Complete optimum enumeration.** For a maximum matching, set \(b_i=a_i-1\in\{0,1\}\). The gap equation becomes
\[
\sum_{i=1}^{k}(b_i+g_i)=r,\qquad b_i\in\{0,1\},\quad g_i\in\mathbb Z_{\ge0}.
\]
Conversely, every solution to this equation, together with a chosen first start \(s_1\in\mathbb Z/n\mathbb Z\), builds one valid maximum matching by the increments \(4+b_i+g_i\). The construction wraps around exactly once and its original edges have mutual endpoint separation at least three. Each unrooted maximum matching arises exactly \(k\) times, once for each choice of its distinguished first edge. The number of solutions for fixed first start is the coefficient \([x^r]((1+x)/(1-x))^k\); therefore
\[
|V(\mathcal P_n)|=\frac nk[x^r]\left(\frac{1+x}{1-x}\right)^k.
\]
The coefficients through degree three are respectively \(1\), \(2k\), \(2k^2\), and \((4k^3+2k)/3\). This proves all four stated formulas, including the \(k=1\) cases \(n=5,6,7\).

**3. Frozen case.** If \(r=0\), every \(b_i=g_i=0\): the \(k\) selected edges are consecutive short edges spaced exactly four steps apart. Exactly four phase choices exist. Any distinct edge sharing one endpoint with a selected short edge either changes its position or makes it long; each such change requires at least one unused unit in an adjacent gap, but none exists. Thus no pivot is legal, and \(\mathcal P_n\cong4K_1\).

**4. Connectivity with a defect.** Suppose \(r\ge1\). If a selected edge is long, replace \(\{s_i,s_i+2\}\) by the short edge \(\{s_i,s_i+1\}\). This is an allowed pivot. It changes \(b_i=1\) to \(b_i=0\) and increases the following gap variable \(g_i\) by one, without violating any separation condition. Repeating produces a matching of only short edges, with \(r\) units distributed among its \(k\) gaps.

For short edges, if the gap following \(e_i=\{s_i,s_i+1\}\) has \(g_i\ge1\), pivot to \(\{s_i+1,s_i+2\}\). This decreases \(g_i\) by one and increases \(g_{i-1}\) by one; the reverse move transfers a unit in the opposite direction. Accordingly, the gap units can be transferred between neighboring gaps on a cyclic \(k\)-tuple. For \(k\ge2\), such transfers connect every weak composition of \(r\) into the \(k\) gaps to one with all units in a single designated gap. The resulting short-edge matching is a rotation of the canonical matching
\[
M_t=\bigl\{\{t+4j,t+4j+1\}:0\le j<k\bigr\}.
\]
Because \(r\ge1\), starting with the last edge of \(M_t\) and then shifting the preceding edges one by one, moving each short edge clockwise by one, is a sequence of legal pivots. It changes \(M_t\) into \(M_{t+1}\). Thus all rotations \(M_t\) lie in one component. For \(k=1\), shortening every long edge and repeatedly shifting the sole short edge by one similarly connects all states. Every optimum can reach a canonical matching, proving the claimed connectivity.

## Verification

The self-contained program `check_direct.py` constructs the original graph and the exact compatibility relation on its \(2n\) edges, enumerates all maximal compatible cliques by Bron–Kerbosch recursion with pivoting, retains all maximum cliques, then traverses their incident-edge-pivot graph. All orders \(5\le n\le23\) passed the maximum-size, exact-count, and component-count assertions, without assuming the claimed optimum size in its search.

An independently structured program `check_gaps.py` generates every matching from the binary-length/weak-composition encoding, checks the actual induced-matching condition and explicitly traverses all incident-edge pivots. All orders \(5\le n\le47\) passed exact-count and component-count assertions. Outputs are in `direct_results.txt` and `gap_results.txt`. Run both scripts using Python 3 (standard library only). These finite checks corroborate but do not replace the proof for arbitrary \(n\).

## Relationship to prior work

Cameron, Sritharan and Tang study induced matching algorithms in weakly chordal graphs. Basavaraju and coauthors establish global extremal counting bounds for *maximal* induced matchings in triangle-free graphs; squared cycles are not triangle-free. Neither result, in the inspected material, derives this exact optimum-state pivot graph. Bousquet and coauthors study ordinary matching token jumps (with equivalence to slides for maximum ordinary matchings), not induced matchings under mandatory incident-edge pivots; those reconfiguration theorems do not transfer the stronger induced-matching feasibility or the present cyclic classification. Demaine and coauthors address token-sliding independent vertex sets on trees. Avis and Hoang analyze independent-set token-sliding reconfiguration graphs and their structure for various graph classes, including ordinary cycles. The present edges are whole original-graph edges, and the move requires those edges to meet; the corresponding conflict-graph vertex tokens would instead have a different adjacency relation. In particular, the existing result on maximum independent sets in \(C_n^2\) concerns selected *vertices*, not selected edges of \(C_n^2\), and does not imply the theorem.

The modular four obstruction has a natural interpretation: optimal induced matchings are hard rods with lengths four or five and nonnegative gaps. At multiples of four they have no slack. Off that lattice, the available slack becomes transferable, restoring connectivity despite retaining optimal size.

## Limitations

The claim addresses only edge pivots that share an endpoint in the original graph; arbitrary replacements and other reconfiguration models may behave differently. The exact graph diameters and complete degree distributions are not determined here. Literature searches cannot certify global historical novelty; unindexed earlier work or sources beyond the inspected material remain possible. The full text of some publisher-hosted algorithm papers was not accessible, and comparisons to those are bounded to their accessible claims. No independent scholarly audit has been conducted.

## References

1. M. Basavaraju, P. Heggernes, P. van 't Hof, R. Saei, and Y. Villanger, *Maximal induced matchings in triangle-free graphs*, arXiv:1312.5180, first posted 2013-12-18, https://arxiv.org/abs/1312.5180.
2. K. Cameron, R. Sritharan, and Y. Tang, *Finding a maximum induced matching in weakly chordal graphs*, Discrete Mathematics 266 (2003), 133–142, https://doi.org/10.1016/S0012-365X(02)00803-8.
3. E. D. Demaine and coauthors, *Linear-time algorithm for sliding tokens on trees*, Theoretical Computer Science 600 (2015), 132–142, https://erikdemaine.org/papers/TokenReconfigurationTrees_TCS2015/paper.pdf.
4. N. Bousquet, T. Hatanaka, T. Ito, and M. Mühlenthaler, *Shortest Reconfiguration of Matchings*, arXiv:1812.05419, https://arxiv.org/abs/1812.05419.
5. D. Avis and D. A. Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding*, arXiv:2203.16861, https://arxiv.org/abs/2203.16861.
