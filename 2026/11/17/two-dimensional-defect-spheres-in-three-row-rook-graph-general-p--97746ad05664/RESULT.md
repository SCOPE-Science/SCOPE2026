# Two-dimensional defect spheres in three-row rook-graph general-position complexes

## Finding
For each integer \(n\ge3\), let \(R_n=K_3\square K_n\) be the rook graph with vertex set \([3]\times[n]\). Let \(X_n\) be its **ordinary graph-geodesic general-position complex**: its faces are all subsets containing no three distinct vertices on a common shortest graph path. Then
\[
\boxed{|X_n|\simeq\left(\bigvee^{2^n}S^{n-1}\right)\vee\left(\bigvee^nS^2\right).}
\]
The summands occupy the same dimension when \(n=3\); in particular, \(|X_3|\simeq\bigvee^{11}S^2\). When \(n\ge4\), the only nonzero reduced integral homology groups are
\[
\widetilde H_2(X_n;\mathbb Z)\cong\mathbb Z^n,\qquad
\widetilde H_{n-1}(X_n;\mathbb Z)\cong\mathbb Z^{2^n}.
\]
Let \(A_n\subseteq X_n\) be the column-thin subcomplex (at most one chosen cell in each column). The natural inclusion \(A_n\hookrightarrow X_n\) is split injective on reduced integral homology; its relative cofiber has homotopy type \(\bigvee^n S^2\). In particular, the \(2^n\) top-dimensional sphere classes already come from column-thin configurations.

For \(n\ge4\), there is also an integral symmetry statement. Under row permutations \(\mathfrak S_3\) and column permutations \(\mathfrak S_n\), the degree-two group is the tensor product of the row-sign module with the column-permutation lattice \(\mathbb Z^{[n]}\). The top-degree group is \(I_3^{\otimes n}\) with the natural diagonal row action and column permutation of tensor factors, twisted by the sign of the column permutation, where \(I_3=\ker(\mathbb Z^3\xrightarrow{\sum}\mathbb Z)\). When \(n=3\), there is instead a natural integral short exact sequence
\[
0\longrightarrow I_3^{\otimes3}\otimes\operatorname{sgn}_{\mathfrak S_3,\mathrm{columns}}
\longrightarrow\widetilde H_2(X_3;\mathbb Z)
\longrightarrow \operatorname{sgn}_{\mathfrak S_3,\mathrm{rows}}\otimes\mathbb Z^{[3]}
\longrightarrow0.
\]
No equivariant splitting of this last sequence is asserted.

## Assumptions and scope
All graphs are finite, simple and undirected. Cartesian-product adjacency means equal row or equal column with different remaining coordinate. A graph-geodesic general-position set avoids a triple of vertices on *any* shortest path between two of them; the triple itself need not span an induced path. The complex includes the empty face. Throughout the main theorem \(n\ge3\); the lower boundary \(n=2\) is treated separately below. The group actions preserve rows and columns, and no factor-exchange symmetry is asserted at \(n=3\).

## Proof
**1. Exact face condition.** A pair of rook-graph vertices is adjacent exactly when it shares a row or a column; otherwise its distance is two. A third vertex lies internally on a geodesic between two cells in different rows and columns exactly when it occupies one of their two rectangle corners. Identify cell \((r,j)\) with edge \(rj\) of \(K_{3,n}\). Such a rectangle-corner triple corresponds precisely to a path with three edges in the selected-edge graph. Hence the general-position faces are exactly the bipartite **star forests**, a face characterization already established in the relevant counting literature. A connected bipartite graph containing no three-edge path must be a star (including an isolated edge), so the converse holds as well.

**2. The column-thin core.** Write \(v_{rj}\) for the cell in row \(r\), column \(j\). Let \(D_j=\{v_{1j},v_{2j},v_{3j}\}\) be a discrete three-vertex complex, with no edge. The faces using at most one cell of each column form the join
\[
A_n=D_1*\cdots*D_n.
\]
Each \(D_j\simeq S^0\vee S^0\), and the join identity gives
\[
A_n\simeq\bigvee^{2^n}S^{n-1}.
\]
In particular, \(A_n\) is simply connected for \(n\ge3\). Its top reduced integral homology is the tensor product of the three-point augmentation lattices, with the usual join-orientation sign under permutations of the factors.

**3. All non-thin faces form isolated thick-column pieces.** For each column \(j\), set \(C_j=\Delta\{v_{1j},v_{2j},v_{3j}\}\), the filled triangle. For each row \(r\), write \(W_{rj}=\{v_{rk}:k\ne j\}\). Let \(T_{rj}\) be the simplex on the union of \(W_{rj}\) and the two column-\(j\) vertices outside row \(r\). Define
\[
B_j=C_j\cup T_{1j}\cup T_{2j}\cup T_{3j}.
\]
If a general-position face selects at least two vertices in column \(j\), it selects none in any other column in those two rows. If it selects all three vertices in column \(j\), it selects nothing elsewhere. Therefore every face of \(X_n\) lies in \(A_n\) or one of the \(B_j\). Moreover, a face cannot have two thick columns with only three available rows, so
\[
B_j\cap B_k\subseteq A_n\quad(j\ne k).
\]
The complex \(B_j\) is contractible: the three simplices \(T_{rj}\) meet the filled triangle \(C_j\) along their respective column edges, and intersections of distinct \(T_{rj}\) are contained in \(C_j\). Each \(T_{rj}\) deformation retracts onto its column edge, fixing that edge; these retractions agree on overlaps, yielding a deformation retraction \(|B_j|\to|C_j|\).

**4. Every attachment intersection is a circle.** The intersection \(L_j=A_n\cap B_j\) is covered by the three subcomplexes
\[
L_{rj}=\Delta(W_{rj})*\{v_{sj}:s\in[3]\setminus\{r\}\},
\]
where the two displayed column vertices form a discrete complex and \(\Delta(W_{rj})\) is a full simplex. Since \(n\ge3\), each \(W_{rj}\) is nonempty, so \(L_{rj}\) is contractible. Every pair of these three pieces meets in exactly one column-\(j\) vertex; the triple intersection is empty. The simplicial nerve theorem therefore gives
\[
|L_j|\simeq S^1.
\]
The row-permutation action permutes the three nerve vertices, so it acts on \(H_1(L_j;\mathbb Z)\) by the sign character.

**5. Homotopy attachments.** Attach the contractible pieces \(B_1,\ldots,B_n\) to \(A_n\) in any order. By the intersections established above, the attaching intersection at stage \(j\) is always exactly \(L_j\), even after earlier pieces have been attached. The inclusion \(L_j\hookrightarrow A_n\) is nullhomotopic because \(L_j\simeq S^1\) and \(A_n\) is simply connected. Consequently the inclusion into any intermediate stage is also nullhomotopic. The homotopy pushout of a null map from \(S^1\) into a space with a contractible second piece is the wedge of that space with its suspension, \(S^2\). Iterating gives the asserted homotopy equivalence and the inclusion-compatible sphere splitting.

**6. Integral maps and symmetries.** The relative homology \(\widetilde H_\bullet(X_n,A_n;\mathbb Z)\) is concentrated in degree two and is \(\mathbb Z^n\), one summand from each \(L_j\). The relative long exact sequence, combined with \(H_1(A_n)=0\) and \(H_2(L_j)=0\), gives the stated split injection and free complementary classes. It is natural for the row and column symmetry actions. Row permutations act on each relative generator by the orientation of the triangle nerve, and column permutations permute the \(n\) thick-column generators. For \(n\ge4\), the degree-two group of \(A_n\) vanishes, proving the stated integral module. In top degree the inclusion is an isomorphism and the ordinary signed join-chain description gives \(I_3^{\otimes n}\) with a column-sign twist. When \(n=3\), the two degrees coincide and the relative exact sequence yields the displayed extension; no equivariant splitting is needed or claimed.

## Verification
The standalone `verify_rook_gp_homotopy.py` computes all face subsets directly from the two-step graph geodesics, separately from the bipartite star-forest condition and the explicit cover \(A_n\cup\bigcup B_j\). It compares these independent predicates for \(n=2,3,4,5\), builds each augmented boundary matrix over \(\mathbb F_2\), and checks the predicted Betti numbers. For \(n=3,4,5\), it also checks fifteen signed Lefschetz numbers of row and column permutations against the integral representation characters. The verifier examined 1,754 nonempty simplicial faces across the four complexes and returned `PASS`; run `python verify_rook_gp_homotopy.py` with standard Python 3. Exact integral homotopy for all \(n\ge3\) rests on the preceding gluing proof, not on these finite mod-two experiments.

The sharp boundary is visible at \(n=2\): direct complete computation gives \(\widetilde\beta_1=3\), \(\widetilde\beta_2=1\), unlike the \(n\ge3\) formula. The simply connected-core step is indeed unavailable there because \(A_2\) is a graph.

## Relationship to prior work
The general-position face condition and star-forest correspondence on rectangular rook graphs are known, together with complete counting and maximality formulas; they are *not* claimed as new. In particular, the publicly recorded October 18, 2026 mathematical result *General-position polynomials of rectangular rook graphs via bipartite star forests* gives the full polynomial, and the November 8, 2026 result *Complete general-position enumerators and gapped maximal spectra of rook graphs* gives maximal-set information. Neither inspected complete result states this homotopy splitting, the attached \(n\) two-sphere classes, or the integral row/column homology modules. The present argument uses the known face characterization as an input and gives new homotopy-pushout structure.

Cody and Detore (first public version January 7, 2026) develop a higher-order geodesic-independence framework, including the ordinary general-position specialization. The 2024 general-position polynomial paper and the 2023 lower-general-position work study counting or extremal parameters, not the present integral homotopy groups. An unpublished or differently phrased topological computation remains possible, and having the full face enumeration in prior work makes this a natural derivation rather than a new combinatorial characterization. No priority or external certification is asserted.

## Limitations
The classification requires exactly three rows and at least three columns. The \(n=2\) boundary is explicitly different. It does not determine the homotopy type for four or more rows or assert an equivariant wedge decomposition. The integral symmetry result concerns homology modules; at \(n=3\), only the natural short exact sequence is stated and not an integral equivariant splitting. No claim is made about generalized geodesic thresholds or arbitrary Cartesian products.

## References
1. B. Cody and R. Detore, *Metric general position extensions of classical graph invariants and perfection*, arXiv:2601.04351, first public version 2026-01-07, https://arxiv.org/abs/2601.04351 ; HTML https://arxiv.org/html/2601.04351 .
2. *General-position polynomials of rectangular rook graphs via bipartite star forests*, public mathematical result dated 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-general-position-polynomials-of-rectangular-rook-graphs-via-bipa--fc2af413d7b2 .
3. *Complete general-position enumerators and gapped maximal spectra of rook graphs*, public mathematical result dated 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-general-position-enumerators-and-gapped-maximal-spectra--809e96679882 .
4. V. Iršič, S. Klavžar, G. Rus and J. Tuite, *General position polynomials*, arXiv:2401.05696, first public 2024-01-11, https://arxiv.org/abs/2401.05696 .
5. G. Di Stefano, S. Klavžar, A. Krishnakumar, J. Tuite and I. Yero, *Lower General Position Sets in Graphs*, arXiv:2306.09965, first public 2023-06-16, https://arxiv.org/abs/2306.09965 .
