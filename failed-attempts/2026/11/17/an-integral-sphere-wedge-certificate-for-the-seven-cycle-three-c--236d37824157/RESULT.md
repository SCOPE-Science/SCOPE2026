# An integral sphere-wedge certificate for the seven-cycle three-color product

## Finding
Let \(G=C_7\times K_3\) be the **categorical** (direct, tensor) product: its vertices are \((i,c)\), where \(i\in\mathbb Z/7\mathbb Z\) and \(c\in\{0,1,2\}\), and two distinct vertices are adjacent exactly when their cycle positions are adjacent and their colors differ. Let \(X=\operatorname{Ind}(G)\), the simplicial complex of independent vertex sets. Then
\[
\boxed{X\simeq S^3\vee S^4\vee S^4\vee S^4.}
\]
Consequently, \(\widetilde H_3(X;\mathbb Z)\cong\mathbb Z\), \(\widetilde H_4(X;\mathbb Z)\cong\mathbb Z^3\), and all other reduced integral homology groups vanish. There is no torsion. This resolves the three-color, seven-cycle instance of the open integral-torsion question stated in [1, Question 24].

## Assumptions and scope
The result concerns exactly the 21-vertex graph \(C_7\times K_3\), not the Cartesian, strong, or lexicographic product, and not products with other cycle lengths or color numbers. The complex includes all independent sets (including the empty face in the augmented chain model). The conclusion is an ordinary nonequivariant integral homotopy equivalence; no equivariant or persistent statement is asserted.

## Proof
Label \((i,c)\) by the integer \(3i+c\in\{0,\ldots,20\}\) and encode each face by its 21-bit mask. Define the ordered vertex-toggle matching as follows. Start with every independent-set face, including the empty face, unpaired. For \(v=0,1,\ldots,20\), simultaneously match each currently unpaired face \(\sigma\) not containing \(v\) to \(\sigma\cup\{v\}\) whenever both are currently unpaired. Remove every matched pair before advancing to \(v+1\). This rule is deterministic because its pairs at any fixed vertex are disjoint.

The exhaustive finite certificate in `verify.py` enumerates **all** \(5282\) faces (with dimensions \(-1,0,\ldots,8\) and counts \(1,21,168,658,1365,1554,1022,402,84,7\)). The matching has \(2636\) pairs and ten unmatched faces: four of dimension three and six of dimension four. The critical dimension-three masks, in increasing order, are
\[
(12312,12328,20504,20520),
\]
and the dimension-four masks are
\[
(299152,299296,598088,598304,1196104,1196176).
\]
To certify acyclicity rather than assuming it from the toggle rule, the verifier constructs the **entire** directed Hasse diagram: every unmatched cover relation is directed from the larger face to the smaller, and every matched cover relation is reversed. It checks by topological sorting that all \(5282\) vertices of the diagram can be removed; there are \(25242\) cover relations. Thus the matching is acyclic. Forgetting the empty face and its partner leaves an ordinary acyclic matching with one critical vertex, four critical three-cells and six critical four-cells.

For exact signed Morse incidence, orient every face by increasing vertex labels. Write \(\partial\tau=\sum_j(-1)^j(\tau\setminus\{v_j\})\). When a lower face \(\alpha\) is paired with an upper face \(\beta\), its projection to the Morse complex is defined recursively by the integral identity
\[
P(\alpha)=-[\beta:\alpha]\sum_{\gamma\subset\beta,\,\gamma\ne\alpha\atop |\gamma|=|\alpha|}
[\beta:\gamma]P(\gamma).
\]
Critical faces project to themselves; upper partners project to zero. Acyclicity ensures that this recursion terminates and agrees with algebraic elimination of the unit boundary entries. The verifier computes the resulting boundary \(\partial_4^{\mathrm M}\) from the six four-cells to the four three-cells. With each four-cell as a **row** and the three-cells as columns, it is exactly
\[
B=\begin{pmatrix}
-1&0&0&0\\
0&0&0&-1\\
-1&0&0&0\\
-1&1&1&-1\\
0&0&0&-1\\
-1&1&1&-1
\end{pmatrix}.
\]
The second and third columns are identical, so \(\operatorname{rank}B\le3\). The submatrix on rows \(1,2,4\) and columns \(1,2,4\) (one-based indices) has determinant \(-1\), hence \(\operatorname{rank}B=3\) and its Smith normal form has precisely three unit invariant factors. In the ordinary Morse CW complex, there are no cells in dimensions one or two. The only nonzero cellular boundary is this map. Thus its homology is torsion-free, with \(H_3\cong\mathbb Z\) and \(H_4\cong\mathbb Z^3\).

Finally, the Morse CW complex has one zero-cell, four three-cells, and six four-cells, so its three-skeleton is \(\bigvee^4 S^3\). Attaching maps of the four-cells lie in \(\pi_3(\bigvee^4S^3)\cong\mathbb Z^4\), and are therefore determined by the matrix \(B\). Integral changes of cellular bases, realized by homotopy equivalences of sphere wedges and changes among attaching maps, put this matrix into Smith form \(\operatorname{diag}(1,1,1,0)\). Three unit-degree attaching maps cancel three three-cells; the remaining one three-cell and three four-cells attach trivially. This proves the claimed wedge homotopy type.

## Verification
Run `python3 verify.py` using Python 3.10 or later. It uses only the standard library. It independently reconstructs the graph and its entire face set, checks the full oriented Hasse graph is acyclic, calculates the signed reduced Morse boundary from face incidences, verifies a unit \(3\)-minor and the matrix rank bound, and calculates all mod-two Betti numbers directly from full simplicial boundary matrices. `verification_output.txt` records a successful run ending in `VERIFY_OK`. The integer boundary and acyclicity checks, not the mod-two experiment alone, establish the integral conclusion.

## Relationship to prior work
Antolín Camarena and Carnero Bravo [1, Theorem 23 and Question 24] proved simple connectivity and restriction of nonzero homology to degrees three and four for this case and explicitly asked if the integral homology of these cycle–complete-graph products is always torsion-free. They reported nonzero free homology in both degrees for this example; that observation does not exclude torsion or specify the integral homotopy type. Their 2022 article [2] gives a general route from torsion-free consecutive-dimensional homology to a sphere wedge; here the required torsion-free determination and exact ranks come from a new explicit integer Morse certificate. A later paper [3] studies products with a path factor, not the present odd-cycle × complete-graph instance. A separate earlier computation concerns \(C_7\times K_4\) (four colors), which neither contains a homotopy retract statement for the three-color case nor implies its integral homology. The search comparison therefore concerns implications, not just titles.

## Limitations
This is a finite, fully enumerated exact result for one canonical graph. It does **not** answer Question 24 in general, prove torsion-freeness for every \(C_k\times K_n\), or classify the action of graph automorphisms. The originality conclusion is relative to the inspected primary literature, available mathematical-index searches, and retrievable prior research records; unpublished or unindexed equivalent work remains possible. No independent external audit has been conducted.

## References
[1] O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401v2 (first public arXiv version 2023-07-23), especially Theorem 23 and Question 24. https://arxiv.org/html/2307.12401v2

[2] O. Antolín Camarena and A. Carnero Bravo, *Homotopy type through homology groups*, arXiv:2212.07509 (2022), Theorem 2. https://arxiv.org/abs/2212.07509

[3] A. Carnero Bravo, *On independence complexes of graph products*, arXiv:2505.06457 (2025), sections 1–3. https://arxiv.org/abs/2505.06457
