# Three-torsion in the minimum-domination shattering complexes of square rook graphs

## Finding
For integers \(2\le m\le n\), let \(R_{m,n}=K_m\square K_n\) be the rook graph on \([m]\times[n]\): two distinct cells are adjacent if they share a row or a column. Let \(\mathcal D_{m,n}\) be the family of **minimum-cardinality ordinary dominating vertex sets**. Querying a cell \(v\) returns the membership bit \(\mathbf1_{v\in D}\) of an unknown \(D\in\mathcal D_{m,n}\). The *shattered-support complex* \(\Delta_{m,n}\) consists of those finite sets \(S\subseteq[m]\times[n]\) on which all \(2^{|S|}\) membership traces occur.

**Theorem.** The following statements hold.

1. When \(m<n\), \(S\in\Delta_{m,n}\) if and only if it contains no repeated row. Thus \(\Phi_{m,n}(z)=\sum_{k=0}^{m}\binom mk n^kz^k=(1+nz)^m\), and \(|\Delta_{m,n}|\simeq\bigvee^{(n-1)^m}S^{m-1}\).
2. When \(m=n\), \(S\in\Delta_{n,n}\) if and only if its cells have **distinct rows or distinct columns** (the alternative may depend on \(S\), but not on the requested trace). Consequently
\[
\Phi_{n,n}(z)=\sum_{k=0}^{n}\left(2\binom nk n^k-\binom nk^2k!\right)z^k,
\qquad \operatorname{VCdim}(\mathcal D_{n,n})=n.
\]
The complex \(\Delta_{n,n}\) is pure of dimension \(n-1\), and for \(n\ge3\) it is not a matroid independence complex.
3. Let \(M_{n,n}\) denote the classical \(n\)-by-\(n\) chessboard (bipartite matching) complex. For \(1\le i\le n-2\) there are canonical isomorphisms
\[
\widetilde H_i(\Delta_{n,n};\mathbb Z)\cong\widetilde H_{i-1}(M_{n,n};\mathbb Z).
\]
In particular, for the \(5\times5\) rook graph,
\[
\Phi_{5,5}(z)=1+25z+300z^2+1900z^3+5650z^4+6130z^5,
\]
\[
\widetilde H_i(\Delta_{5,5};\mathbb Z)\cong
\begin{cases}\mathbb Z/3\mathbb Z&i=3,\\\mathbb Z^{2104}&i=4,\\0&\text{otherwise}.\end{cases}
\]
Furthermore, for **every integer \(n\ge8\)**, \(\widetilde H_{n-3}(\Delta_{n,n};\mathbb Z)\) has nonzero \(3\)-torsion. Hence \(\Delta_{5,5}\) and every \(\Delta_{n,n}\) with \(n\ge8\) are pure, nonshellable simplicial complexes that arise naturally as VC-shattering complexes of minimum dominating sets.

The exact integral \(3\)-torsion facts about chessboard complexes are *previously established results of Jonsson and his predecessors*. The finding here is the domination-shattering identification and the homological transfer, not a new computation of chessboard torsion.

## Assumptions and scope
All graphs are finite, simple and undirected. Domination means every unselected vertex is adjacent to at least one selected vertex; equivalently, the closed neighborhood of the selected set covers the graph. It is *ordinary* domination, not total, independent, paired or accurate domination. The ground-set elements of the Boolean concept class are individual board cells, not edges or open-neighborhood predicates. Every row and column is nonempty, and \(2\le m\le n\). Homology is reduced integral simplicial homology of the geometric realization; \(\Phi_{m,n}(z)=\sum_{S\in\Delta_{m,n}}z^{|S|}\).

## Proof
**Step 1: classify optimizers.** A set \(D\) fails to dominate if and only if there is an empty row \(i\) and an empty column \(j\), for then the cell \((i,j)\) is neither selected nor adjacent to a selected cell. Conversely, any such pair witnesses failure. Thus domination is equivalent to meeting all rows or meeting all columns. Every dominating set has size at least \(m\), and the family of size-\(m\) optimizers is exactly the family of one-cell-per-row placements if \(m<n\). When \(m=n\), it is the union of the one-cell-per-row and one-cell-per-column placements (their overlap being the permutation placements). These facts are also recorded in Mertens [1, Section 1, equations (2)--(3)].

**Step 2: trace criterion.** If a support \(S\) is shattered, its all-one trace must be contained in some size-minimum dominating set; by Step 1, the cells of \(S\) have distinct rows, or (in the square case) distinct columns. Conversely, suppose \(S\) has distinct rows. Fix any requested positive subset \(T\subseteq S\). In each row queried by a positive cell, choose that cell. In each row queried by a negative cell, choose a different column (possible as \(n\ge2\)); choose an arbitrary cell in each row unqueried by \(S\). This constructs a minimum dominating set with trace \(T\). The distinct-column case is symmetric on a square. This proves the if-and-only-if criteria, without supposing that any single optimizer realizes all traces.

**Step 3: count supports.** There are \(\binom mk n^k\) row-distinct supports of size \(k\). In a square there are equally many column-distinct supports, and \(\binom nk^2 k!\) in both families, as they are partial permutations. Inclusion-exclusion yields the displayed polynomials. The degree of the square polynomial is \(n\), since a full row-based transversal is shattered. Every square support of size below \(n\) extends to a size-\(n\) row- or column-distinct support, proving purity. For \(n\ge3\), matroid basis exchange fails: take \(S=\{(i,1):i\in[n]\}\) and \(T=\{(1,j):j\in[n]\}\). On deleting \((2,1)\) from \(S\), any \((1,j)\in T\setminus S\) creates repeated row \(1\) and repeated column \(1\), hence cannot be added while remaining a face. This establishes the claimed matroid boundary.

**Step 4: topology.** Let \(A_n\) be the complex of row-distinct supports, \(B_n\) the complex of column-distinct supports. By Step 2, \(\Delta_{n,n}=A_n\cup B_n\). The intersection \(A_n\cap B_n\) is the chessboard matching complex \(M_{n,n}\). Each of \(A_n\) and \(B_n\) is the join of \(n\) discrete \(n\)-point spaces, so each has reduced integral homology \(\mathbb Z^{(n-1)^n}\) in degree \(n-1\), and zero in all other degrees. Indeed, each discrete \(n\)-point space is a wedge of \(n-1\) copies of \(S^0\), and joins of reduced integral chain complexes shift tensor products by one degree. Their connectivity and homology ensure that the reduced Mayer--Vietoris long exact sequence for \(A_n\cup B_n\) gives the displayed natural isomorphisms for \(1\le i\le n-2\).

**Step 5: integral torsion and the first explicit case.** Jonsson [2, Section 3] gives a computer-free proof that \(\widetilde H_2(M_{5,5};\mathbb Z)\cong\mathbb Z/3\mathbb Z\). Jonsson [2, Theorem 1.1, citing Björner et al.] gives connectivity below this degree, and [2, Theorem 3] implies that in this square case no homology occurs above degree \(3\). Thus the Mayer--Vietoris isomorphism gives \(\widetilde H_3(\Delta_{5,5};\mathbb Z)\cong\mathbb Z/3\mathbb Z\) and zero in degrees \(1,2\). The top homology in degree \(4\) is a subgroup of the free simplicial chain group, hence free abelian. The alternating face count from Step 3 yields
\[
\widetilde\chi(\Delta_{5,5})=-1+25-300+1900-5650+6130=2104,
\]
so its top Betti number is \(2104\) and other reduced homology vanishes. For general \(n\ge8\), [2, Theorem 2] establishes nonzero \(3\)-torsion in \(\widetilde H_{n-4}(M_{n,n};\mathbb Z)\), because \((2n-4)/3\le n-4\). Step 4 transports it to \(\widetilde H_{n-3}(\Delta_{n,n};\mathbb Z)\). A pure shellable complex has torsion-free integral homology, concentrated at the top reduced dimension, so all these torsion-bearing shattering complexes are nonshellable.

The proof uses known published integral chessboard-complex theorems as explicit mathematical premises. The finite checks below corroborate the new identification and do not substitute for Jonsson's integral results or the general argument.

## Verification
Three independent, bundled checkers provide finite corroboration. `VERIFY_PYTHON.py` exhausts all membership supports through square order four and directly tests ordinary domination for orders two and three. `VERIFY_CPP.cpp` exhausts every query support of size at most five for the \(5\times5\) square, independently enumerates all \(6130\) optimal concepts and reproduces the full polynomial, including all \(6130\) top faces. `VERIFY_CHESSBOARD.py` independently constructs chessboard-complex boundary maps and computes dimensions over the fields of two, three and five elements; the degree-two Betti number is one in characteristic three and zero in characteristics two and five, consistent with but not by itself proving integral \(3\)-torsion. Recorded verifier outputs accompany the standalone programs. The all-order proof and cited integral theorem, not extrapolation from small sizes, establish the infinite claim.

## Relationship to prior work
Mertens [1] proves the complete ordinary-domination polynomial and already states the minimum-optimum count \(2n^n-n!\) for the square rook graph. That is a premise, **not** a new claim here; it does not identify membership-shattered supports or their topology. Jonsson [2] proves the classical integral \(3\)-torsion statements about chessboard matching complexes independently of domination and learning. Those facts are likewise credited; our claimed contribution is that this torsion appears, one degree higher, in a particular natural family of Boolean shattering complexes. The published open-neighborhood VC-shattering profile of rectangular rook graphs uses the family of graph neighborhoods, not the family of minimum ordinary dominating sets [3]. The published analysis of rook-graph dominance complexes [4] concerns the simplicial complex of subsets whose complements dominate, not our learning-theoretic shattered-support complex. These distinctions are by predicate, inclusion and implication, not merely different names.

## Limitations
Historical uniqueness cannot be guaranteed from database searches; a publication about joins of partition-matroid complexes or matching-complex suspensions could contain an equivalent restatement. No value of the Littlestone dimension is claimed. The isomorphism in the middle homological degrees does not determine all equivariant structure. No proof of Jonsson's original chessboard torsion theorem is newly claimed. The \(5\times5\) finite calculations verify only that size and selected fields; the proof of the family for all \(n\) is structural and imports exact established integral topology.

## References
[1] S. Mertens, *Domination Polynomial of the Rook Graph*, arXiv:2401.00716 (first publicly posted January 1, 2024), Sections 1--3, especially equations (2)--(3). https://arxiv.org/abs/2401.00716

[2] J. Jonsson, *On the 3-Torsion Part of the Homology of the Chessboard Complex*, Annals of Combinatorics 14 (2010), 487--505; available arXiv preprint: arXiv:1203.5644 (March 26, 2012), Theorems 1.1, 2 and 3 and Section 3. https://arxiv.org/pdf/1203.5644

[3] *Exact open-neighborhood shattering polynomials of rectangular rook graphs*, published-finding corpus, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-open-neighborhood-shattering-polynomials-of-rectangular-ro--ffaa2f7a2b1d

[4] *Three-sphere homotopy types of rook-graph dominance complexes*, published-finding corpus, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-three-sphere-homotopy-types-of-rook-graph-dominance-complexes--89367a150c4b
