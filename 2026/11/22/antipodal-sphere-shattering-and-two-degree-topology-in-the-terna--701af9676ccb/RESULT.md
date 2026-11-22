# Antipodal-sphere shattering and two-degree topology in the ternary three-cube

## Finding
Let \(X=\{0,1,2\}^3\) with Hamming metric \(d_H\), and for each \(c\in X\) let \(R_c=\{x\in X:d_H(c,x)=3\}\). The 27 sets \(R_c\), each of size eight, are the Boolean concept class. All 27 singleton supports and all \(\binom{27}{2}=351\) distinct pairs are shattered. Exactly 216 triples are shattered: these are the triples \(S=\{a,b,c\}\) satisfying both (i) every coordinate assumes exactly two symbols on \(S\) and (ii) each of the three points is the unique holder of one of those two symbols in a distinct coordinate. Equivalently, the three pairwise Hamming distances are all two and the triple lies in an axis-aligned binary subcube of \(X\). No support of four or more points is shattered. Hence
\[
\Phi(z)=1+27z+351z^2+216z^3,\qquad\operatorname{VCdim}=3.
\]
The shattered-support simplicial complex \(K\) has 189 maximal edges (precisely the pairs at Hamming distance one or three) and 216 maximal triangles; it is nonpure. Over \(\mathbb F_2\), its only nonzero reduced homology is
\[
\widetilde H_1(K;\mathbb F_2)\cong\mathbb F_2^{192},\qquad
\widetilde H_2(K;\mathbb F_2)\cong\mathbb F_2^{83}.
\]

## Assumptions and scope
All centers and all queries range over the entire 27-point set \(X\); a center may be one of the queried points. A trace on \(S\subseteq X\) is \(R_c\cap S\). Shattering requires all \(2^{|S|}\) traces, including the empty and full trace. The rank computations and homology claims are over the two-element field; no integral homotopy-type or torsion claim is made. This is the exact-distance-three relation, not the usual distance-one adjacency of the Hamming graph.

## Proof
**Support criterion.** The full trace \(S\) can be realized if and only if each coordinate of \(S\) uses at most two of the three symbols: choose the missing symbol as the corresponding center coordinate. For a support \(S\) of size at least three, a trace \(S\setminus\{p\}\) requires a coordinate at which \(p\) has a symbol that none of the other members have. Call such a coordinate *private* for \(p\). Conversely, suppose every point \(p\in S\) has a private coordinate and every coordinate uses at most two symbols. For any excluded subset \(T\subseteq S\), choose at a private coordinate of each \(p\in T\) the center symbol \(p_i\), excluding \(p\) and retaining all other members of \(S\). The private coordinates for distinct members are distinct when \(|S|\ge3\). At remaining coordinates choose a symbol absent from \(S\). This produces trace \(S\setminus T\) and proves the criterion.

**Sizes and classification.** For a support with at least three points, no coordinate can be private for two different points. Thus a shattered support has at most three points. Every distinct pair is shattered: for the empty trace, either exclude both in one shared coordinate, or, if they differ in all coordinates, exclude them separately in two coordinates; singleton and full traces are immediate. A shattered triple must have a private coordinate for each of its three points; hence every coordinate uses two symbols, with each point uniquely different in one coordinate. Such a triple has all three pairwise Hamming distances equal to two. Each triple lies in a unique binary \(2\times2\times2\) box \(B\subset X\), as the omitted third symbol in each coordinate is unique. There are \(3^3=27\) boxes; each has precisely eight such triples (the three-point subsets of either parity tetrahedron, four per tetrahedron). This gives 216 triples and proves the polynomial.

**Facets.** Among 351 pairs, exactly \(\frac{27\cdot12}{2}=162\) have Hamming distance two. Each such pair extends to exactly four shattered triples: choose the third point by matching one endpoint at one differing coordinate, the other endpoint at the other, and using either of the two alternative symbols at the common coordinate. No pair of Hamming distance one or three can belong to a shattered triple. Therefore precisely \(351-162=189\) edges are maximal, alongside the 216 triangles.

**Homology.** The complex has 27 vertices, all 351 edges, 216 triangular faces, and no higher faces. Its first simplicial boundary map over \(\mathbb F_2\) has rank \(27-1=26\). The boundary map from triangles to edges, with a column for every three-element shattered support and three ones at its edge rows, has exact binary rank 133. Two independently implemented exhaustive exact row-reduction programs in the verification files construct this full \(351\times216\) matrix and independently return rank 133. Thus the reduced Betti ranks in dimensions one and two are respectively \(351-26-133=192\) and \(216-133=83\). Connectedness gives reduced zeroth homology zero, and absence of higher faces excludes other homology.

## Verification
Execute \(\texttt{python3 verify_python.py}\), then compile with \(\texttt{c++ -std=c++17 -O2 -Wall -Wextra verify_cpp.cpp -o verify_cpp}\) and execute \(\texttt{./verify_cpp}\). Both enumerate all \(\binom{27}{k}\) supports for \(0\le k\le4\), directly derive every trace from Hamming distance three, check the 216-triple geometric criterion and 189 maximal edges, and compute the exact binary rank 133 using separate implementations. Since shattering is hereditary, excluding every four-point support excludes every larger one. No statistical or numerical-rank approximation enters the proof.

## Relationship to prior work
Adler, Benediktsson and Macpherson (2020) determine VC dimension and VC density for **distance-one open neighborhoods** on Hamming and Johnson graphs; their Hamming section does not state a complete shattering-complex or homology classification for the distinct exact-distance-three relation. Related published finite Hamming studies also examine radius-one neighborhoods, Rips complexes, and antipodal incidence closures. A radius-two Rips complex, a three-cut complex, and the family of all proper Cartesian boxes are not the shattering complex of the fixed-width, exact-distance-three concept class analyzed here. The general private-coordinate support observation is a conjunction-class argument; the specific 216-face structure, nonpurity and binary homology numbers are the finite structural claims of interest.

## Limitations
The homology ranks are certified by full finite binary matrix elimination, not by a uniform closed-form formula for all dimensions. The generalization to arbitrary ternary word lengths and alphabet sizes is not claimed as an original theorem. This work does not establish integral homology, homotopy equivalence, or an adaptive Littlestone dimension. Some related published research records were available only as searchable summaries; an unindexed equivalent classification remains a priority risk. No independent validation has been performed.

## References
1. I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042v1, publicly posted 31 July 2020, especially Section 4, https://arxiv.org/pdf/2007.16042 .
2. Published published-finding corpus research record, *Coefficientwise VC-shattering census of open neighborhoods in Hamming graphs*, accessed 16 November 2026 (distance-one comparator; searchable title and abstract).
3. Published published-finding corpus research record, *Antipodal Hamming concepts: box polarity, symmetry collapse, and sharp Horn arity*, accessed 16 November 2026 (closure-system comparator; searchable title and abstract).
4. Published published-finding corpus research record, *Complete ternary translation character of the radius-two Hamming Rips complex*, accessed 16 November 2026 (different complex; searchable title and abstract).
