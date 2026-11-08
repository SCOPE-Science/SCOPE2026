# Integral homotopy type of the eleven-cycle three-color categorical product

## Finding
Let \(G=C_{11}\times K_3\) denote the **categorical graph product**, and let \(\operatorname{Ind}(G)\) be its simplicial independence complex. Its complete integral homotopy type is
\[
\boxed{\operatorname{Ind}(C_{11}\times K_3)\simeq\bigvee^{3}S^{6}\vee S^{7}.}
\]
In particular, all its reduced integral homology groups are torsion-free, with \(\widetilde H_6\cong\mathbb Z^3\) and \(\widetilde H_7\cong\mathbb Z\), and every other reduced homology group zero. This treats an additional case of the integral-torsion question of Antolín Camarena and Carnero Bravo [1].

## Assumptions and scope
The vertex set is \(\mathbb Z/11\mathbb Z\times\{0,1,2\}\). Distinct vertices \((r,c)\) and \((s,d)\) are adjacent if and only if \(s-r\equiv\pm1\pmod{11}\) **and** \(d\ne c\). This is a 33-vertex, four-regular graph with 66 edges, not the Cartesian or strong graph product. A face of \(\operatorname{Ind}(G)\) is any set of mutually nonadjacent vertices. In the certificate, \((r,c)\) has zero-based bit index \(3r+c\), and the empty face is retained with dimension minus one.

## Proof
**1. Full finite face set.** Enumerate independent subsets by adding vertices in increasing bit order whenever none of the already selected vertices is adjacent. The resulting face set contains exactly 732,802 simplices **including the empty face**. An unrelated cyclic transfer calculation, with each cycle-position state a subset of the three colors, produces the identical face-count polynomial
\[
\begin{aligned}
F(z)={}&1+33z+462z^2+3608z^3+17424z^4+54681z^5\\
&+114620z^6+163746z^7+163218z^8+117260z^9\\
&+62832z^{10}+25479z^{11}+7645z^{12}+1584z^{13}\\
&+198z^{14}+11z^{15}.
\end{aligned}
\]
The transfer state rule is exact: two consecutive nonempty color subsets are compatible precisely if both are the same singleton. Closing the cycle enforces compatibility between the last and first positions. There is no reliance on partial sampling.

**2. Explicit full-poset Morse matchings.** Choose either ascending vertex order \(0,\ldots,32\) or descending order \(32,\ldots,0\). For each vertex in that order, greedily match each still-unmatched nonempty face \(\sigma\) not containing the vertex with its still-unmatched coface \(\sigma\cup\{v\}\), when that coface exists. Leave the empty face unmatched. Both matching orders yield exactly 366,383 pairs, one unmatched vertex, eighteen unmatched six-simplices, and sixteen unmatched seven-simplices. There are no other unmatched nonempty faces. In both cases, orient every face-cover relation downwards except matched relations, which are oriented upwards. A full topological sort visits **all 732,802 faces** across **5,573,766 Hasse incidences**, proving that the matchings are acyclic. By discrete Morse theory, the geometric realization is homotopy equivalent to a CW complex with one zero-cell, eighteen six-cells, and sixteen seven-cells.

**3. Exact signed attachment matrices.** The oriented simplicial boundary removes the \(j\)-th ordered vertex with sign \((-1)^j\). For every unmatched six-dimensional face \(t\), its projection is its basis vector. For a matched upper six-face its projection is zero. If \(t\) is a matched lower six-face with partner \(u\), define its projection recursively by eliminating \(t\) from \(\partial u\):
\[
P(t)=-[u:t]^{-1}\sum_{w\subset u,\,w\ne t}[u:w]P(w),
\]
where the incidence \([u:t]\) is \(+1\) or \(-1\). Acyclicity guarantees that this recursive elimination terminates. Applying these projections to the boundaries of all sixteen critical seven-simplices yields an integral \(18\times16\) Morse boundary matrix. Both matrices, their ordered critical face bitmasks, and their exact integer coefficients are in `morse_matrices.json`.

For each matrix, an independently executed **integer-only** sequence of elementary row swaps, column swaps, integer row and column additions, and row sign changes reduces it to fifteen diagonal unit entries and otherwise zero. These operations are unimodular, so its Smith invariant factors are exactly fifteen copies of one, and its rank is fifteen. Thus reduced integral homology is \(\mathbb Z^3\) in degree six and \(\mathbb Z\) in degree seven, with no torsion.

**4. Homotopy, not just homology.** The Morse CW complex is a point with only six- and seven-dimensional cells. Its six-skeleton is a bouquet of eighteen six-spheres. Since \(\pi_6(\bigvee^{18}S^6)\cong\mathbb Z^{18}\), each attaching map of a seven-cell is completely determined by its integer degree column; no higher attaching invariant appears in this dimension. The unimodular Smith reduction is implemented by homotopy self-equivalences of the six-sphere bouquet and integer changes among the seven-cell attachments. Fifteen degree-one cell pairs cancel, leaving three six-spheres and one trivially attached seven-cell. This proves the displayed integral homotopy type.

## Verification
Run `python3 verify_c11k3.py` using Python 3.10 or later, with `morse_matrices.json` alongside. No third-party Python packages are needed. The verifier independently counts faces by a cycle transfer, fully reconstructs both matchings, checks all reversed face-cover relations for acyclicity, independently regenerates both signed Morse matrices, compares their every entry and ordered basis with the embedded certificate, and exactly reduces both matrices by integer elementary operations. Its deterministic output is stored in `verification_output.txt`; success marker: `C11_K3_INDEPENDENCE_INTEGRAL_WEDGE_VERIFIED`.

## Relationship to prior work
Antolín Camarena and Carnero Bravo [1, Theorem 23(c) and Question 24 in the arXiv version] constrain the possible homology degrees of the cycle-product complexes and explicitly ask whether their integral homology is always torsion-free. Their exact homotopy results for cycle lengths divisible by three, and for lengths four and five, do not determine the present length eleven. The earlier small-cycle computations mentioned there concern other lengths. The subsequent graph-product study [2] treats products involving path factors rather than this cycle/complete-graph pair. The present computation does not settle the full family question. Other calculations at cycle lengths seven, eight, and ten do not imply the length-eleven result.

## Limitations
The homotopy equivalence is nonequivariant: the action of graph automorphisms on the homology is not classified. The proof is an exhaustive finite computation with complete explicit reproducible certificates, not a uniform formula for arbitrary cycle lengths or numbers of colors. It does not show the general cycle-product family is torsion-free; an equivalent independent unindexed computation could remain undiscovered. No external independent audit is represented.

## References
[1] O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401 (first public version July 23, 2023); *Homology, Homotopy and Applications* **26** (2024), no. 2, 349–373, DOI: 10.4310/HHA.2024.v26.n2.a17. https://arxiv.org/abs/2307.12401

[2] A. Carnero Bravo, *On independence complexes of graph products*, arXiv:2505.06457 (2025). https://arxiv.org/abs/2505.06457
