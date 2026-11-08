# Integral homotopy classification of four-row \((1,1,1,2)\) multiple chessboard complexes

## Finding
For each integer \(m\geq 1\), let \(X_m=\Delta_{[m]}^{(1,1,1,2)}\). Its integral homotopy type is
\[
|X_m|\simeq
\begin{cases}
\bigvee^{3}S^{0},&m=1,\\
\bigvee^{6}S^{1},&m=2,\\
\bigvee^{5}S^{2},&m=3,\\
\bigvee^{9}S^{2},&m=4,\\
\bigvee^{21}S^{3},&m=5,\\
\bigvee^{53}S^{3}\vee S^{4},&m=6,\\
\bigvee^{21}S^{3}\vee\bigvee^{90}S^{4},&m=7,\\
\bigvee^{b(m)}S^{4},&m\geq8,
\end{cases}
\]
where
\[
b(m)=\frac{m^5-15m^4+76m^3-151m^2+97m-2}{2}.
\]
The homotopy classifications not implied by the cited primary literature are the three intermediate cases \(4\leq m\leq6\), including the mixed-dimensional wedge at six columns. The seven-column case follows from a combination of existing top-homology, connectivity and wedge-of-spheres theorems, although a second, constructive certificate is supplied here. The small and stable ranges are also credited.

## Assumptions and scope
The vertices are squares \((i,j)\) with \(1\leq i\leq4\) and \(1\leq j\leq m\). A face may contain at most one square from each column, at most one square in each of rows 1, 2 and 3, and at most two squares in row 4. Every bound includes the empty face. No identification of equal row labels or quotient by column permutations is imposed. Here \(\bigvee^t S^d\) is the wedge of \(t\) copies of the ordinary unpointed sphere with a basepoint; \(\bigvee^3 S^0\) denotes four discrete points.

## Proof
**Finite middle range and cross-check.** The attached `verify.py` gives explicit finite certificates for the new cases \(m=4,5,6\) and, as a check on the literature-implied classification, \(m=7\). Its algorithms use integer bit masks \(\sum 2^{(i-1)m+j}\), with zero-based bit indices, to represent simplices. A first enumerator independently selects at most one row per column and enforces the four row capacities; a second chooses pairwise disjoint column subsets row by row and enforces the capacities. Equality of the two complete face sets is checked in each case. This double construction also verifies that no admissible simplex is omitted by the matching procedure.

For each \(m\), `ORDERS[m]` is an explicit permutation of all \(4m\) vertex bit indices. Process these vertices in that order. At vertex \(v\), pair every still-active simplex \(\sigma\) omitting \(v\) with \(\sigma\cup\{v\}\) whenever both are still active. A pair has codimension one. The program enumerates **every** cover relation \(\tau\subset\sigma\) between nonempty faces; it orients a matched cover relation from lower to upper and every other cover relation from upper to lower. Kahn's topological-sort algorithm visits the entire face poset, proving the resulting directed Hasse graph is acyclic. Thus every declared matching is a valid discrete Morse matching on the finite simplicial complex, not just a collection of locally legal pairs. Vertices unmatched by this process are the critical cells.

The exact certificates are:

| \(m\) | Nonempty simplices | Matched pairs | Critical cells | Directed cover relations |
|---|---:|---:|---|---:|
| 4 | 286 | 138 | one 0-cell, nine 2-cells | 792 |
| 5 | 840 | 409 | one 0-cell, twenty-one 3-cells | 2,750 |
| 6 | 2,139 | 1,042 | one 0-cell, fifty-three 3-cells, one 4-cell | 7,770 |
| 7 | 4,816 | 2,350 | one 0-cell, twenty-three 3-cells, ninety-two 4-cells | 18,711 |

For \(m=4,5\), this critical-cell structure itself proves the asserted wedge: the Morse CW complex has a point and cells only in one positive dimension.

For \(m=6,7\), the integer Morse boundary is computed by exact signed gradient-path cancellation, not by numerical ranks or by a finite-field proxy. Orient each simplex by its increasing vertex bit indices. For an oriented upper simplex \(u\) and codimension-one face \(f\), write \([u:f]\in\{+1,-1\}\) for the incidence sign. Project each lower-dimensional face \(f\) to the free abelian group on critical lower-dimensional cells by the recursion
\[
P(f)=\begin{cases}
 e_f,&f\text{ critical},\\
 0,&f\text{ is the upper member of a matched pair},\\
 -[u:f]^{-1}\sum_{g\subset u,\ g\ne f}[u:g]P(g),&f\leftrightarrow u\text{ is a matched pair}.
\end{cases}
\]
Every recursive call follows an edge of the acyclic gradient digraph, so it terminates. A critical upper cell \(u\) has Morse boundary \(\sum_{f\subset u}[u:f]P(f)\). This is the standard algebraic Morse cancellation formula and uses exact integers throughout.

At \(m=6\) the entire \(53\)-by-\(1\) signed boundary is zero. At \(m=7\) the \(23\)-by-\(92\) boundary matrix has rank exactly two: the minor on zero-based rows \((1,3)\) and columns \((11,33)\) has determinant \(-1\), and **every** column is explicitly checked to be the corresponding integer linear combination of those two columns. Hence its Smith invariant factors are both one and all other invariant factors vanish. The finite matching has no positive-dimensional critical cells below dimension three, so its Morse CW complex is 2-connected. Attaching maps of 4-cells to a wedge of 3-spheres are classified by their integer degree vectors, since \(\pi_3(\bigvee^q S^3)\cong\mathbb Z^q\). Elementary unimodular row and column operations are realized by homotopy equivalences and handle changes; the two unit entries remove two pairs of adjacent cells and the remaining attaching maps are null. The resulting space is exactly \(\bigvee^{21}S^3\vee\bigvee^{90}S^4\). The zero boundary for \(m=6\) similarly gives \(\bigvee^{53}S^3\vee S^4\). Independently calculated full simplicial mod-two Betti numbers agree with all four homotopy classifications.

For \(m=7\), the 2026 *Column Law* Theorem 9.6 applies with total row capacity five and two empty columns. Its top Betti rank is \(6+3\cdot14+3\cdot14=90\), calculated from the three partitions \((5),(4,1),(3,2)\), whose Kostka factors are \(1,3,3\) and whose associated Specht dimensions are \(6,14,14\). The 2014 connectivity bound yields two-connectivity, and Theorem 9.6 makes degree-three integral homology free; Euler--Poincaré then gives rank 21 in degree three. The cited wedge-of-spheres lemma for simply connected complexes with free homology in two consecutive degrees therefore already implies the seven-column homotopy type. Our exact Morse certificate independently realizes this implication and is not the originality claim.

**Previously implied ranges.** The source cited below determines the \(m=3\) case explicitly (Example 4.4), and its full/nearly-full-row proposition covers \(m=2\). At \(m=1\), four isolated vertices give the displayed type. For \(m\geq8\), the 2014 shellability theorem applies because the capacity sum is five and the number of rows is four, so the complex is pure shellable of dimension four and is a wedge of 4-spheres. The face count for \(1\leq k\leq5\) is
\[
f_{k-1}=\sum_{s=\max(0,k-2)}^{\min(3,k)}\binom3s\frac{m!}{(m-s)!}\binom{m-s}{k-s},
\]
where \(s\) is the number of singleton rows occupied. Euler--Poincaré gives \(b(m)=\sum_{k=1}^{5}(-1)^{k-1}f_{k-1}-1\), whose expansion is the displayed polynomial. This calculation supplies the already-implied high-range multiplicity and does not constitute a new shellability proof.

## Verification
Run `python3 verify.py` using Python 3.10 or later; only the standard library is needed. The verifier checks independent face enumerations for every \(1\leq m\leq7\), exhaustively constructs all matched and critical cells, checks every Hasse cover and global acyclicity, independently computes mod-two Betti numbers of the full simplicial chain complex, and checks the exact signed Morse boundary and determinant/integer-span certificate for \(m=6,7\). It also verifies the Euler polynomial at \(m=8,9,10,11,12\). The recorded `verify_output.txt` terminates with `ALL_VERIFY_OK`. Computational verification handles finitely many cases; the unlimited range \(m\geq8\) relies on the cited published shellability theorem and the symbolic face count.

## Relationship to prior work
Limonchenko--Yu (2026), arXiv:2610.37827v1, introduces these conventions and explicitly gives \(X_3\simeq\bigvee^{5}S^2\) in Example 4.4; Proposition 3.4 also settles \(X_2\). Their general three-row classification does not apply to this nonuniform four-row family, and their four-row torsion theorem treats a different capacity pattern. Jojić--Vrećica--Živaljević (arXiv:1412.0386, Theorem 4.4) gives shellability once \(m\geq8\). The independent 2026 preprint *The Column Law and Torsion in Chessboard Complexes* (Theorem 9.6) gives top-homology field-independence and freeness one degree lower for row-bounded complexes, and in combination with connectivity, Euler counting and the earlier wedge lemma it already implies the seven-column homotopy type; it does not determine the lower-degree homotopy of the four-, five- and six-column cases. Thus the new homotopy content is the three finite cases \(4\leq m\leq6\) bridging the credited ranges, particularly the mixed-dimensional integral wedge at \(m=6\). The seven-column certificate is an independently verifiable construction for a literature-implied consequence.

## Limitations
The result is specific to four row capacities \((1,1,1,2)\) with unit column capacities. It does not classify all four-row multiple chessboard complexes or establish equivariant homotopy equivalences. Independent mathematical peer review is not claimed. The three new finite homotopy results rely on executable exhaustive certificates (and standard discrete Morse theory), not a compact uniform symbolic matching valid for all column counts. Unindexed equivalent earlier results remain possible.

## References
1. Ivan Limonchenko and Seonghyeon Yu, *Homotopy types and torsion in homology of generalized chessboard complexes*, arXiv:2610.37827v1 (first posted 2026-10-27). https://arxiv.org/html/2610.37827v1
2. Duško Jojić, Siniša Vrećica, Rade Živaljević, *Multiple chessboard complexes and the colored Tverberg problem*, arXiv:1412.0386 (2014), Theorem 4.4. https://arxiv.org/abs/1412.0386
3. *The Column Law and Torsion in Chessboard Complexes*, Preprints.org, manuscript 202610.0974 (2026), Theorem 9.6. https://www.preprints.org/manuscript/202610.0974
