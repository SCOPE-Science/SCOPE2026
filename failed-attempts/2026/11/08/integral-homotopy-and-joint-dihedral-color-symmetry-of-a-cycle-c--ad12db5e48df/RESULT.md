# Integral homotopy and joint dihedral–color symmetry of a cycle–complete graph product

## Finding
Let \(G=C_8\times K_3\) be the *categorical* (not Cartesian) product of the eight-cycle with the complete graph on three colors. For its ordinary independence complex \(X=\operatorname{Ind}(G)\), there is an integral homotopy equivalence
\[
X\simeq S^4\vee\bigvee^{3}S^5.
\]
Under the natural action of \(D_8\times S_3\), where \(D_8=\langle r,t\mid r^8=t^2=1,\,trt=r^{-1}\rangle\) acts on the eight cycle positions, the complete rational homology modules are
\[
\widetilde H_4(X;\mathbb Q)\cong\alpha\otimes\beta\otimes\operatorname{sgn}_{S_3},\qquad
\widetilde H_5(X;\mathbb Q)\cong\alpha\otimes\bigl(\operatorname{sgn}_{S_3}\oplus\operatorname{Std}_{S_3}\bigr).
\]
Here \(\alpha(r)=-1,\alpha(t)=+1\), \(\beta(r)=+1,\beta(t)=-1\), and \(\operatorname{Std}_{S_3}\) denotes the two-dimensional standard representation. Consequently, no positive-degree rational homology class is invariant under the full natural symmetry group.

## Assumptions and scope
The vertex set of \(G\) is \(\{(i,c):i\in\mathbb Z/8\mathbb Z,\ c\in\{0,1,2\}\}\). Distinct vertices \((i,c)\) and \((j,d)\) are adjacent precisely when \(j=i\pm1\pmod{8}\) and \(c\ne d\). A face of \(X\) is any set of mutually nonadjacent vertices. All integral homology uses ordinary orientations from ascending vertex labels \(v=3i+c\); rational homology is obtained by extending scalars. The homotopy statement is nonequivariant; the representation statement is a statement about the induced action on rational homology, not an equivariant splitting.

## Proof
**Exhaustive simplicial model and discrete Morse matching.** Enumerate all independent subsets as 24-bit integers, including the empty subset. A direct recursive vertex-extension enumeration produces exactly \(18{,}721\) nonempty faces, distributed in dimensions \(0\) through \(11\) as
\[
(24,228,1112,3042,4848,4652,2880,1305,472,132,24,2).
\]
Starting with the set of nonempty faces, process the bit positions \(v=0,1,\ldots,23\) in order. For each unpaired face \(a\) without bit \(v\), if \(b=a\cup\{v\}\) is unpaired, pair \(a\) with \(b\) and remove both. This precisely specified matching contains \(9{,}353\) pairs and has critical cells in dimensions \(0,4,5\) with multiplicities \(1,6,8\) respectively. Its acyclicity is proved by orienting *every* face-poset covering relation downward except matched relations, which point upward: a complete topological sort visits all \(18{,}721\) faces (the verifier computes the graph without sampling), excluding directed cycles. Therefore Forman's discrete Morse theory supplies a CW model with one point, six four-cells, and eight five-cells.

**Integral attaching degrees.** For a face \(s\) with vertices in ascending order, define its oriented boundary by deleting the \(j\)-th vertex with coefficient \((-1)^j\). Project to critical faces recursively by replacing a matched *lower* face using the other terms of the oriented boundary of its matched upper face, divided by the unit pivot \(\pm1\); a matched upper face projects to zero. Because the matching is acyclic, this recursion terminates. With critical cells in increasing bit-mask order, the resulting \(6\)-by-\(8\) integer Morse differential from degree five to degree four is
\[
D=\begin{pmatrix}
0&-1&0&0&0&-1&0&0\\
0&0&-1&0&0&0&-1&0\\
0&-1&0&-1&0&0&0&0\\
0&0&-1&-1&0&0&0&0\\
0&0&0&0&-1&0&-1&0\\
0&0&0&0&-1&-1&0&0
\end{pmatrix}.
\]
Exact rational Gaussian elimination finds rank five. Rows numbered \(0,1,2,3,4\) and columns numbered \(1,2,3,4,5\) form a square minor of determinant \(+1\). All nonzero Smith invariants are therefore units. Elementary changes of four- and five-cell bases and cancellation of five \(4\)-/\(5\)-cell pairs leave one four-cell and three five-cells. Since the CW complex has no cells in dimensions one to three, the attaching maps of the remaining five-cells to the one four-sphere are classified by their integral degrees, all zero after the reduction. Each such map is null-homotopic by \(\pi_4(S^4)\cong\mathbb Z\). Thus \(X\simeq S^4\vee\bigvee^3 S^5\), without relying on finite-field extrapolation.

**Joint symmetry.** Write an element of the natural \(D_8\times S_3\) action as \((r^at^b,\sigma)\) with \(0\le a<8\), \(b\in\{0,1\}\). Directly enumerate all \(96\) such permutations and verify that each preserves the graph's edges. To find its reduced Lefschetz trace, partition the 24 vertices into permutation orbits. An invariant independent set must be a union of orbits containing no internal graph edge; permissible orbits conflict if any cross-edge exists. For a selected family of \(k\) permissible, nonconflicting orbits, its oriented simplex has permutation sign \((-1)^{|S|-k}\), so its contribution to the reduced Lefschetz number is \((-1)^{k-1}\). The empty selection contributes \(-1\); hence the reduced Lefschetz number is minus the independence polynomial of the permissible-orbit conflict graph, evaluated at \(-1\). An exact deletion recursion computes these numbers for all 96 symmetries and gives
\[
L(r^at^b,\sigma)=(-1)^{a+b}\operatorname{sgn}(\sigma)
-(-1)^a\bigl(\operatorname{sgn}(\sigma)+\#\operatorname{Fix}(\sigma)-1\bigr).
\]
As the reduced homology is supported only in degrees four and five, \(L=\chi_4-\chi_5\). The one-dimensional \(H_4\)-character must be one of the eight sign characters of \(D_8\times S_3\). Subtracting the measured Lefschetz character gives candidate three-dimensional \(H_5\)-characters. The bound \(|\chi_5(g)|\le3\) removes six candidates. For one of the remaining two the squared character norm is \(4\); this is impossible for a three-dimensional representation of this group, since its possible complex irreducible dimensions are one and two, so a decomposition of total dimension three has character norm \(2,3,5\), or \(9\). The unique remaining candidate gives \(\chi_4=(-1)^{a+b}\operatorname{sgn}(\sigma)\) and \(\chi_5=(-1)^a(\operatorname{sgn}(\sigma)+\#\operatorname{Fix}(\sigma)-1)\), exactly the displayed module decomposition. It follows that the nontrivial rotation \(r\) acts by \(-1\) in both degrees and rules out full-group invariants.

## Verification
Run `python3 verify_c8_k3.py` from the directory containing the supplied standalone verifier. The program requires only Python's standard library, enumerates every face and every covering relation, recomputes the integer Morse differential and unit minor, and separately computes original-face mod-two boundary ranks and all 96 signed Lefschetz traces. Its recorded output appears in `verification_output.txt`; completion is signaled by `C8_K3_CATEGORICAL_PRODUCT_PASS`. The mod-two ranks are corroboration only: the integral homotopy equivalence uses the explicit acyclic Morse matching and integral unimodular attaching matrix.

## Relationship to prior work
Engström (2005) develops foundational methods for independence complexes and their homotopy types. Goyal–Shukla–Singh (2019) treat categorical products of *complete graphs* and related constructions, rather than this eight-cycle product. Most directly, Antolín Camarena–Carnero Bravo (2023 preprint; 2024 journal article) identify the independence complex of \(C_8\times K_3\) as an example with nonzero free homology in two adjacent dimensions and explicitly ask whether these cycle–complete product complexes always have torsion-free homology (Question 3.19, page 369). Their broader theorem permits Moore spaces and does not determine this example's integral homotopy decomposition or joint dihedral–color homology representations. The present calculation resolves that one named example; it does **not** answer their question for all cycle lengths and color counts. Related indexed results for \(C_7\times K_4\) concern different parameters and do not imply the result here.

## Limitations
This is an exact finite-instance classification, not a general theorem for all \(C_m\times K_n\). Its symmetry result is a rational module decomposition, not a classification of integral group-ring lattices or an equivariant homotopy equivalence. The executable proof is an exhaustive finite certificate contingent on the stated code and the standard discrete Morse framework; it is not a formally machine-checked proof or an independent mathematical audit. A definitive global publication-priority or equivalence search is not guaranteed.

## References
1. A. Engström, *Complexes of Directed Trees and Independence Complexes*, arXiv:math/0508148 (first public preprint 2005-08-08), https://arxiv.org/abs/math/0508148.
2. P. Goyal, A. Shukla, and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926 (2019), https://arxiv.org/abs/1905.06926.
3. O. Antolín Camarena and A. Carnero Bravo, *Homotopy Type of the Independence Complex of Some Categorical Products of Graphs*, *Homology, Homotopy and Applications* **26** (2024), no. 2, pp. 349–373; arXiv:2307.12401; DOI:10.4310/HHA.2024.v26.n2.a17. Specifically Theorem 3.18 and Question 3.19.
4. R. Forman, *Morse Theory for Cell Complexes*, *Advances in Mathematics* **134** (1998), 90–145.
