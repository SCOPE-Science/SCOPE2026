# Two-Ferrers edge partitions, complement convexity, and cyclic deletions

## Finding
Let \(G=(U,V,E)\) be a finite bipartite graph with *pairwise incomparable* row neighborhoods \(N_G(u)\), \(u\in U\): for distinct \(u,w\), neither neighborhood contains the other. Let \(H=(U,V,(U\times V)\setminus E)\) be the bipartite complement. Then
\[
\operatorname{fp}(G)\le 2\quad\Longleftrightarrow\quad
\text{some ordering }u_1,\ldots,u_m\text{ of }U\text{ makes every }N_H(v)\text{ an interval.}
\]
Here \(\operatorname{fp}\) is the least number of pairwise edge-disjoint Ferrers (induced-\(2K_2\)-free) spanning bipartite subgraphs whose union is \(G\), and an interval may be empty. The forward direction assumes neighborhood incomparability; the reverse direction holds for every bipartite graph. The right-hand condition is the column consecutive-ones property of the complementary incidence matrix and is testable by standard consecutive-ones recognition.

For every integer \(n\ge3\), let \(G_n=K_{n,n}\setminus C_{2n}\), where the removed Hamiltonian cycle has edges \((u_i,v_i)\) and \((u_i,v_{i+1})\), with indices modulo \(n\). Then
\[
\operatorname{fp}(G_n)=3\quad(n\ge3).
\]
Furthermore \(\nu_{\mathrm{ind}}(G_n)=2\) for every \(n\ge4\); thus these dense, connected bipartite graphs give an infinite family with \(\operatorname{fp}(G_n)>\nu_{\mathrm{ind}}(G_n)\). For \(n=3\), the graph is a three-edge matching and \(\nu_{\mathrm{ind}}(G_3)=3\).

## Assumptions and scope
Graphs are finite, simple and bipartite with fixed sides \(U,V\). Parts in an edge partition span the same vertex bipartition, may have isolated vertices, and are allowed to be empty; the minimum for an edgeless graph can be taken as zero. A Ferrers graph means that its row neighborhoods form a chain under inclusion. A neighborhood antichain means every *distinct* pair is incomparable, including equality being excluded. The cyclic-deletion statement uses labels fixed as specified; its proof does not depend on equivalence under graph isomorphisms. No general characterization of \(\operatorname{fp}(G)\le2\) outside the antichain class is asserted.

## Proof
**Necessary interval condition.** Suppose \(E=R\,\dot\cup\,B\) and both the red and blue spanning subgraphs are Ferrers. Their row neighborhoods \(R(u)\) and \(B(u)\) each form chains. If two distinct rows have \(R(u)=R(w)\), the blue rows are comparable, so their unions \(N_G(u)=R(u)\cup B(u)\) and \(N_G(w)=R(w)\cup B(w)\) are comparable, contradicting the antichain assumption. Thus all red row sets are distinct; similarly all blue row sets are distinct. Order the rows so that
\[
R(u_1)\supsetneq R(u_2)\supsetneq\cdots\supsetneq R(u_m).
\]
For any \(a<b\), necessarily \(B(u_a)\subsetneq B(u_b)\): if the inclusion were reversed, both colors' neighborhoods at \(u_a\) would contain those at \(u_b\), again contradicting the host antichain. Fix a column \(v\). If its nonedge positions were not consecutive, we could choose \(a<b<c\) with \(u_av,u_cv\notin E\) and \(u_bv\in E\). If the middle edge is red, \(v\in R(u_b)\subseteq R(u_a)\), impossible. If it is blue, \(v\in B(u_b)\subseteq B(u_c)\), also impossible. Hence all complement-column neighborhoods are intervals. When \(|U|\le1\) the conclusion is immediate; the chain argument covers every larger antichain.

**Sufficient edge partition.** Conversely, fix an order of \(U\) for which each column's nonedge set is an interval \([a_v,b_v]\) in the ordered row positions (the interval may be empty). For a column with a nonempty nonedge interval, assign every present edge in rows \(i<a_v\) to red and every present edge in rows \(i>b_v\) to blue. For a column with no nonedges assign all its edges to red. Each column's red edges form an initial segment of the row order; each column's blue edges form a terminal segment. Therefore the red row neighborhoods decrease under inclusion and the blue ones increase. Both parts are Ferrers, and the assignment partitions all edges. This implication requires no antichain hypothesis.

**Cyclic-complement lower bound.** For \(G_n\), each row has exactly two missing columns, \(v_i,v_{i+1}\). These two-element forbidden sets are distinct for \(n\ge3\), so the host row neighborhoods are pairwise incomparable. Each complement column has missing rows \(\{u_j,u_{j-1}\}\), indices modulo \(n\). If \(\operatorname{fp}(G_n)\le2\), the theorem would force all \(n\) distinct pairs of this cyclic system to be consecutive in one linear ordering of the \(n\) rows. But any such ordering has only \(n-1\) distinct consecutive pairs. This is impossible, proving \(\operatorname{fp}(G_n)\ge3\).

**Three explicit Ferrers parts.** Index rows and columns from \(0\) to \(n-1\). Place every allowed edge \((i,j)\) in exactly one of the following sets:
\[
R=\{(i,j):j>i+1\},\qquad
B=\{(i,j):1\le j<i\},\qquad
S=\{(i,0):1\le i\le n-2\}.
\]
Here only pairs with indices in \(\{0,\ldots,n-1\}\) occur. The missing pairs are exactly \((i,i)\) and \((i,(i+1)\bmod n)\); every other pair belongs to precisely one of \(R,B,S\). Red row neighborhoods \(\{v_{i+2},\ldots,v_{n-1}\}\) decrease with \(i\). Blue row neighborhoods \(\{v_1,\ldots,v_{i-1}\}\) increase. The third part is a star centered at \(v_0\). All three are Ferrers, proving the reverse inequality.

**Induced matching separation.** For \(n\ge4\), edges \((0,2)\) and \((2,0)\) form an induced matching of size two: their two cross pairs \((0,0)\) and \((2,2)\) are removed. If three independent edges formed an induced matching, the three selected columns would have all their three unordered pairs among the forbidden pairs of rows: for each selected row, the other two selected columns must be its *two* forbidden columns. Every forbidden column pair in \(G_n\) consists of consecutive indices in \(C_n\). This would form a triangle in \(C_n\), impossible for \(n\ge4\). Thus the induced matching number is exactly two. When \(n=3\) every row contains one allowed edge, yielding the three-edge matching.

## Verification
Run `python3 artifacts/verify.py` using the included standalone Python 3 program; it requires only the standard library. It exhaustively compares the two criteria for every binary incidence matrix with incomparable rows of sizes \(3\times3\), \(3\times4\), and \(4\times4\) (respectively 12, 384, and 600 cases). The direct test for two Ferrers parts enumerates all binary assignments of the existing edges and checks the chain condition separately from the interval-order test. The script also verifies disjoint exhaustive coverage and Ferrers nesting of the explicit three-part construction for \(3\le n\le100\). These checks are finite corroborations; all-parameter claims rest on the preceding proofs.

## Relationship to prior work
London, *Edge partitions into induced-\(2K_2\)-free bipartite graphs* (first publicly available February 28, 2026), defines the edge-disjoint Ferrers partition invariant, proves induced-matching lower bounds and neighborhood-poset upper bounds, evaluates paths, cycles, and matching-deleted complete bipartite graphs, and lists the general two-part decision problem as open. The present antichain/consecutive-ones characterization resolves a natural restricted decision class not covered by those statements. For the cyclic-deletion family, \(G_3\) is a three-edge matching and \(G_4\) is an eight-cycle, so these two small cases are already covered by standard additivity or the known cycle computation; the genuinely new infinite family begins at \(n=5\), when the deleted structure is a spanning cycle in an increasingly dense biclique. Its exact partition number for these larger graphs is not implied by those earlier special cases. Earlier convex-bipartite chain-subgraph results of Ma–Spinrad, Brandstädt–Eschen–Sritharan, Takaoka, and Klemz–Rote concern edge *covers* permitting overlaps, a different invariant: removing overlaps can destroy the chain property. The construction and theorem do not assume cover-to-partition equivalence.

## Limitations
The forward implication requires that row neighborhoods form an antichain; it does not solve the unrestricted two-Ferrers partition decision problem. The cyclic construction proves an infinite separation of one unit but not an unbounded gap; the latter is already known for other graph families. Full-text comparison with the 1994 2-chain-cover article could not be completed, so historical priority remains provisional despite the distinct cover-versus-partition definitions. The argument is same-author-verified, not independently audited.

## References
1. A. London, *Edge partitions into induced-\(2K_2\)-free bipartite graphs*, 2026, arXiv:2603.00593; https://arxiv.org/abs/2603.00593; *Ars Combinatoria* **166** (2026), 15–26, DOI:10.61091/ars166-02.
2. S. Klemz and G. Rote, *Linear-Time Algorithms for Maximum-Weight Induced Matchings and Minimum Chain Covers in Convex Bipartite Graphs*, *Algorithmica* (2022), DOI:10.1007/s00453-021-00904-w.
3. A. Takaoka, *Recognizing Simple-Triangle Graphs by Restricted 2-Chain Subgraph Cover*, arXiv:1605.07322 (2016).
4. T. Ma and J. P. Spinrad, *On the 2-Chain Subgraph Cover and Related Problems*, *Journal of Algorithms* (1994), DOI:10.1006/jagm.1994.1034.
5. K. S. Booth and G. S. Lueker, *Testing for the consecutive ones property, interval graphs, and graph planarity using PQ-tree algorithms*, *Journal of Computer and System Sciences* **13** (1976), 335–379.
