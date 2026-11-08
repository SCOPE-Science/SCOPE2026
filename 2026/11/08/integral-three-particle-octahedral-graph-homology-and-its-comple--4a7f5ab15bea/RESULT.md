# Integral three-particle octahedral graph homology and its complete symmetry character

## Finding

Let \(O=K_{2,2,2}\) be the octahedral graph, whose six vertices are labelled \(0,\ldots,5\), with antipodal nonedges \(\{0,1\},\{2,3\},\{4,5\}\). Its edges are exactly the twelve pairs joining different antipodal blocks. Write \(B_3(O)\) for the unordered configuration space of three distinct points of its geometric realization. Then, integrally,

\[
H_i(B_3(O);\mathbb Z)\cong
\begin{cases}
\mathbb Z & i=0,\\
\mathbb Z^8 & i=1,\\
\mathbb Z^{47} & i=2,\\
0 & i\ge3.
\end{cases}
\]

In particular, all its integral homology is torsion-free. The full group \(G=\operatorname{Aut}(O)\cong C_2\wr S_3\) has order \(48\). Its rational representations on \(H_1\) and \(H_2\) are determined by the following character table. Each representative is the displayed image tuple \((g(0),\ldots,g(5))\); this fixes the class order and removes any reliance on unlabeled class conventions.

| Representative | Class size | \(\chi_1\) | \(\chi_2\) |
| --- | ---: | ---: | ---: |
| (0,1,2,3,4,5) | 1 | 8 | 47 |
| (0,1,2,3,5,4) | 3 | 0 | -1 |
| (0,1,3,2,5,4) | 3 | 0 | -1 |
| (0,1,4,5,2,3) | 6 | -4 | 3 |
| (0,1,4,5,3,2) | 6 | 0 | -1 |
| (1,0,3,2,5,4) | 1 | 0 | -1 |
| (1,0,4,5,2,3) | 6 | 0 | -5 |
| (1,0,4,5,3,2) | 6 | 0 | -1 |
| (2,3,4,5,0,1) | 8 | 2 | -1 |
| (2,3,4,5,1,0) | 8 | 0 | -1 |

For a bipartition \((\lambda,\mu)\) of three, let \(\rho_{\lambda,\mu}\) be the rational irreducible of \(C_2\wr S_3\) induced from the Specht representations on the positive and negative coordinates, where negative coordinates carry the product of their \(C_2\) sign characters. Write \(\varnothing\) for the empty partition. Then

\[
H_1(B_3(O);\mathbb Q)\cong
\rho_{(1,1,1),\varnothing}\oplus
\rho_{(1,1),(1)}\oplus
\rho_{(1),(1,1)}\oplus
\rho_{\varnothing,(1,1,1)},
\]

\[
\begin{aligned}
H_2(B_3(O);\mathbb Q)\cong{}&2\rho_{(2,1),\varnothing}
\oplus\rho_{(1,1,1),\varnothing}
\oplus4\rho_{(2),(1)}
\oplus2\rho_{(1,1),(1)}\\
&\oplus3\rho_{(1),(2)}
\oplus3\rho_{(1),(1,1)}
\oplus2\rho_{\varnothing,(3)}
\oplus2\rho_{\varnothing,(2,1)}.
\end{aligned}
\]

Neither positive-degree homology representation has a nonzero \(G\)-fixed vector. Central inversion, the automorphism \((1,0,3,2,5,4)\), acts on \(H_2\) with a positive eigenspace of dimension \(23\) and negative eigenspace of dimension \(24\).

## Assumptions and scope

The graph is a one-dimensional CW complex with all twelve edges present. Configurations are **unordered, collision-free triples of points anywhere on the geometric edges**, not triples of graph vertices, graph matchings, or sink configurations. Homology is singular homology; the symmetry group acts by permuting antipodal vertex pairs and interchanging vertices within each pair. The representation formulas concern rational homology, although the ranks and torsion assertions are integral. No assertion is made about a particular equivariant splitting or the integral representation lattice.

## Proof

**Step 1: integral cellular model.** We use the reduced Świątkowski chain model for graph configuration spaces, justified by the graph configuration-space chain-model theorem of An, Drummond-Cole and Knudsen [2]. For a vertex \(v\), order its four incident edges by the global lexicographic edge order, choose the first as reference \(e_v\), and introduce three local degree-one differences \(h_{v,e}-h_{v,e_v}\). Their differential is \(e-e_v\), where each edge is a polynomial variable of weight one and each local difference has weight one. The degree-one differences anticommute between vertices. Work in total weight three, with monomials ordered nondecreasingly and local vertex differences in ascending vertex order. This fixes all integral signs and coefficients. With \(E(O)=12\) and all six vertices four-valent, the chain groups in degrees \(0,1,2,3\) have ranks

\[(364,1404,1620,540).\]

The complete integral boundary matrices are defined by `oct3.py`, which generates every monomial/local-state basis and its signed boundary. Direct substitution verifies every composition of consecutive boundaries is zero.

**Step 2: integral ranks and torsion.** Exact integer column reduction of the boundary maps produces image ranks

\[\operatorname{rank}(\partial_1,\partial_2,\partial_3)=(363,1033,540).\]

Crucially, every new leading coefficient in the integer reduction is a unit, \(+1\) or \(-1\), not merely a nonzero rational number. In each column, reduction removes all larger pivot rows before selecting the new pivot; the normalized pivot column has zero entries at larger rows and has leading coefficient one. Ordering the pivot columns by decreasing pivot row therefore exposes a full-rank triangular minor of determinant \(\pm1\), so the corresponding image sublattice is primitive in the ambient free chain group. This is verified separately for each boundary by `oct3_sym.py`; no assumptions about small prime torsion are made. Each quotient of a kernel by the next boundary image is consequently torsion-free. The displayed chain dimensions and ranks give Betti numbers \((1,8,47,0)\), and there are no chain groups in higher degrees.

**Step 3: group action and exact traces.** The \(48\) automorphisms are the permutations of the three antipodal blocks, together with the independent sign flips within each block. Each sends a degree-one local difference to a signed integral linear combination of local differences; tensor factors are reordered with their Koszul signs. For each automorphism, `oct3_sym.py` verifies that the action commutes with every boundary on all four chain degrees. Write \(t_d(g)\) for the trace on the degree-\(d\) chain group, and \(b_2(g)\) for the exact trace on \(\operatorname{im}\partial_2\), computed in the integer-echelon basis. Since \(\partial_1\) has augmentation kernel and \(\partial_3\) is injective,

\[
\begin{aligned}
\chi_1(g)&=t_1(g)-t_0(g)+1-b_2(g),\\
\chi_2(g)&=t_2(g)-b_2(g)-t_3(g).
\end{aligned}
\]

The values in the table are obtained from these formulas. They are checked on every one of the \(48\) elements, grouped into exactly ten conjugacy classes. Orthogonality against the ten rational irreducible characters of \(C_2\wr S_3\), computed independently by inducing signed Specht characters, gives the two displayed decompositions. Averaging either complete character over the group yields zero invariants. The central inversion has trace \(-1\) and the second homology dimension is \(47\); the stated eigenspace dimensions follow.

**Step 4: independent finite topological calculation.** Subdivide every original edge once, obtaining a graph with eighteen vertices and twenty-four edges. It satisfies the standard three-particle sufficient-subdivision conditions: distinct essential vertices have paths of at least two edges, and every simple loop has length at least four. The resulting unordered Abrams cubical configuration complex is a deformation retract of \(B_3(O)\) [1]. Independently enumerating its cells gives counts \((816,2880,3192,1088)\) and boundary ranks \((815,2057,1088)\) over each of \(\mathbb F_2\), \(\mathbb F_3\) and \(\mathbb F_{1009}\), recovering Betti numbers \((1,8,47,0)\). The independent cubical action's signed Lefschetz numbers agree with \(1-\chi_1(g)+\chi_2(g)\) for all \(48\) automorphisms. This cross-check alone does not prove integral torsion-freeness; that conclusion relies on the unit-echelon calculation in Step 2.

## Verification

The four self-contained, standard-library Python programs `oct3.py`, `oct3_sym.py`, `oct3_abrams.py`, and `oct3_irreps.py` and their four outputs are included. Execute them in that order in the same directory; the symmetry program writes `oct3_chars.json`, which the latter two programs read. The first program checks all reduced Świątkowski boundary compositions, and its prime-field calculations are additional cross-checks, not the integral proof. The second performs exact integer unit-echelon reduction, verifies all 48 group actions are chain maps, computes their exact traces and checks conjugacy constancy. The third independently builds the sufficiently subdivided Abrams complex and tests cubical boundary ranks and signed Lefschetz numbers. The fourth determines the irreducible decomposition by exact class-function inner products. Successful runs terminate with `OCT3_SYMMETRY_CHARACTER_PASS`, `OCT3_INDEPENDENT_ABRAMS_CHECK_PASS`, and `DONE` respectively; the first program reports the full Betti table.

## Relationship to prior work

Ko and Park [1], publicly available January 13, 2011, calculate first homology of graph braid groups using graph-theoretic invariants and establish the relevant discrete-configurations convention. Their general first-homology result is compatible with rank eight here and is not part of the originality claim. The reduced Świątkowski chain model and its configuration-space equivalence are prior results [2]. An and Knudsen [3] determine generators for second homology of planar graph configuration spaces, not the explicit rank, complete relation calculation, or full symmetry character of this three-point octahedral case. Maciążek and Sawicki [4] develop integral homology results for wheel, complete-bipartite, and other specified graph families; the octahedral graph with six four-valent vertices is not among their resolved cases. The **new** claim is the explicit integral degree-two classification, the absence of all torsion for this configuration space, and its complete rational octahedral symmetry character. None follows merely from a general generating theorem or from a first-homology formula.

## Limitations

The calculation is specific to three particles on the octahedral graph. It does not classify general graph configuration spaces, the fundamental group, the cohomology ring, integral equivariant modules, or the homotopy type. The complete characterization of all possible prior appearances remains contingent on indexing and external scholarly verification. A reproducible exact computation does not constitute an independent mathematical audit.

## References

[1] K. H. Ko and H. W. Park, *Characteristics of graph braid groups*, first public arXiv version January 13, 2011, https://arxiv.org/abs/1101.2648.

[2] B. H. An, G. C. Drummond-Cole and B. Knudsen, *Subdivisional spaces and graph braid groups*, arXiv:1708.02351 (first public August 8, 2017), https://arxiv.org/abs/1708.02351.

[3] B. H. An and B. Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371 (first public August 24, 2020), https://arxiv.org/abs/2008.10371.

[4] T. Maciążek and A. Sawicki, *Non-abelian quantum statistics on graphs*, first public June 7, 2018, arXiv:1806.02846, https://arxiv.org/abs/1806.02846.
