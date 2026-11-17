# Translation characters of the quaternary Hamming three-cube Rips complex

## Finding

Let \(A=(\mathbb Z/4\mathbb Z)^3\) with the Hamming metric, and let \(K=\operatorname{VR}_{\le2}(A)\) be the simplicial complex of all subsets whose pairwise Hamming distances are at most two. Each \(a\in A\) acts on \(K\) by translation \(t_a(x)=x+a\). The sole nonzero reduced rational homology is \(\widetilde H_3(K;\mathbb Q)\cong\mathbb Q^{405}\), whose rank and integral homotopy type were determined previously. This result determines its **entire translation character**, all sixty-four complex character multiplicities, and the rational homology of two natural quotient spaces.

For a translation coordinate, call its *type* \(0\) when its residue is zero, \(1\) when it is odd (one or three), and \(2\) when it is the half-turn two. Sort the three coordinate types into a triple \(\tau(a)\). Let \(\chi(a)\) be the rational third-homology trace. For \(k\in A\), let \(\lambda_k(a)=i^{k\cdot a}\) be the complex character and let \(m(k)\) denote its multiplicity. The complete answer depends on the common type triple according to this table:

| Sorted type triple | Number of triples | \(\chi(a)\) | \(m(k)\) |
|:--|--:|--:|--:|
| (0,0,0) | 1 | 405 | 9 |
| (0,0,1) | 6 | 9 | 6 |
| (0,0,2) | 3 | 9 | 9 |
| (0,1,1) | 12 | -3 | 6 |
| (0,1,2) | 12 | -3 | 6 |
| (0,2,2) | 3 | 45 | 9 |
| (1,1,1) | 8 | 1 | 8 |
| (1,1,2) | 12 | 1 | 5 |
| (1,2,2) | 6 | 1 | 5 |
| (2,2,2) | 1 | 1 | 8 |

In the trace column, the type refers to \(a\); in the multiplicity column it refers to \(k\). In particular the multiplicity distribution is \(7\) characters of multiplicity \(9\), \(30\) of multiplicity \(6\), \(9\) of multiplicity \(8\), and \(18\) of multiplicity \(5\), totaling \(405\) dimensions. The representation is not multiplicity-free.

The translation-invariant subspace has dimension \(9\). Hence the orbit space has
\[
\widetilde H_j(|K|/A;\mathbb Q)\cong
\begin{cases}\mathbb Q^9,&j=3,\\0,&j\ne3.\end{cases}
\]
For the order-eight half-turn subgroup \(B=\{0,2\}^3\), the corresponding invariant rank is \(71\):
\[
\widetilde H_3(|K|/B;\mathbb Q)\cong\mathbb Q^{71},
\qquad \widetilde H_j(|K|/B;\mathbb Q)=0\quad(j\ne3).
\]

## Assumptions and scope

Every coordinate is in \(\mathbb Z/4\mathbb Z\), so the translations form \(A\cong C_4^3\) rather than the group of arbitrary permutations of four symbols. There are exactly sixty-four vertices. The Hamming threshold is inclusive and fixed at two. All characters and quotient-homology claims are over characteristic zero; no integral \(\mathbb Z[A]\)-lattice or torsion description of the quotient is asserted. A zero coordinate is distinct from a half-turn, and odd nonzero coordinates have order four. The source of the topological input has primary relevance in topological graph-metric homology (MSC2020 55U10).

## Proof

**1. Reconstruct the concentrated homology.** Two different words are forbidden to share a face precisely when they differ in all three coordinates. Therefore \(K=\operatorname{Ind}(K_4\times K_4\times K_4)\), where the product is categorical. The independently supplied verifier constructs the full pairwise-distance graph, enumerates all maximal cliques by a pivoted maximal-clique algorithm, then expands every face. It finds exactly \(508\) maximal faces: \(12\) coordinate planes with \(16\) vertices each, \(64\) radius-one Hamming balls with \(10\) vertices each, and \(432\) parity tetrahedra of size four. It independently checks that these are all maximal faces and that the simplicial complex, including its empty face, has exactly \(830101\) faces.

The verifier performs a deterministic staged face matching: for each vertex in lexicographic order, among remaining unmatched faces pair each face missing the vertex with its vertex-adjoined coface when both are available; remove each pair. There are \(414848\) augmented pairs and exactly \(405\) unmatched tetrahedra. After orienting every face-poset Hasse edge downward except matched edges upward, a full topological sort visits all \(830101\) augmented faces and finds no directed cycle. The empty face is matched with a vertex. Removing the empty face and this pair gives an ordinary acyclic matching leaving one critical vertex and \(405\) three-dimensional cells and no other critical faces. Forman's discrete-Morse theorem gives \(|K|\simeq\bigvee^{405}S^3\). This reconfirms a published input; it is not counted as an original nonequivariant result.

**2. Character from invariant simplices.** Fix \(a\in A\), and let \(d\in\{1,2,4\}\) be the order of its translation. All vertex orbits of \(t_a\) have size \(d\). Build a graph \(H_a\) with one vertex for every translation orbit whose complete collection is itself a face of \(K\); join two such orbits precisely when some cross-orbit pair differs in every coordinate. The complete \(t_a\)-invariant faces of \(K\) are then exactly the unions of \(j\) orbits corresponding to independent \(j\)-subsets of \(H_a\). This is an equality of sets, because \(K\) is flag and a face is fixed setwise if and only if it is a union of complete translation orbits.

An invariant face made of \(j\) orbits has dimension \(dj-1\), while translation on its vertices is a product of \(j\) cycles of length \(d\). Its contribution to the reduced alternating signed simplicial trace is therefore
\[
(-1)^{dj-1}(-1)^{j(d-1)}=(-1)^{j-1}.
\]
Including the conventional empty-face contribution \(-1\), the *reduced Lefschetz number* is \(-I(H_a;-1)\), where \(I(H;t)=\sum_{S\text{ independent}}t^{|S|}\) is the independence polynomial. Since the only nonzero reduced rational homology of \(K\) is in degree three, the reduced Lefschetz number also equals \(-\chi(a)\). Consequently,
\[
\boxed{\chi(a)=I(H_a;-1).}
\]
This includes identity translation: its orbit graph is the forbidden-distance categorical product, so the formula yields the alternating face sum \(405\).

**3. Exact finite evaluation for every translation.** Enumerate \(a\) over all \(64\) triples. The supplied `character.py` builds vertex orbits and the full graph \(H_a\) directly from the distance-three relation; it evaluates \(I(H_a;-1)\) with the integer recurrence
\[
I(H;-1)=I(H-v;-1)-I(H-N[v];-1),
\quad I(\varnothing;-1)=1,
\]
where \(N[v]\) is the closed neighborhood. Memoization avoids repeated induced subgraphs; the recurrence is exact, with no floating-point calculations. Coordinatewise symbol permutations conjugate all translations with the same triple of cycle types, explaining the ten rows of the table. The computed character values, in table order, are \(405,9,9,-3,-3,45,1,1,1,1\). As an independent cross-check, `direct_fixed_check.py` constructs all faces from the different maximal-face classification and, for a representative of each ten types, directly sums the signed action of the vertex permutation on **all invariant faces**. Each of those ten checks reproduces the trace.

**4. Exact Fourier inversion.** Every irreducible complex representation of \(A\) is one-dimensional and is one of the \(64\) characters \(\lambda_k(a)=i^{k\cdot a}\). Orthogonality gives
\[
m(k)=\frac1{64}\sum_{a\in A}\chi(a)i^{-k\cdot a}.
\]
The verifier evaluates all sums in \(\mathbb Z[i]\), checking vanishing imaginary parts, divisibility by \(64\), nonnegativity, and total dimension \(405\). The resulting multiplicities are precisely the ten listed rows. The trace sum is \(576\), giving \(m(0)=576/64=9\). Restricting to the eight half-turn translations gives a trace sum of \(568\), hence \(568/8=71\) invariant dimensions for \(B\).

**5. Rational orbit-space homology.** Barycentric subdivision eliminates inversions in the finite simplicial group action. The rational simplicial chain complex of the geometric quotient identifies with group-invariant chains of the subdivided original complex. Finite-group invariants are exact over \(\mathbb Q\). Therefore rational quotient homology is the corresponding invariant homology. Homology of \(K\) is reduced and supported only in degree three, proving both quotient assertions.

## Verification

The standalone standard-library-only programs `verify_full.py`, `character.py`, and `direct_fixed_check.py` rederive the necessary finite data directly from the stated words and metric. Executing them reproduces `PREMISE_Q4_WEDGE_405_VERIFIED`, `QUATERNARY_TRANSLATION_CHARACTER_PASS`, and `DIRECT_FACE_LEFSCHETZ_PASS`. The first checks every face and Hasse incidence for the known topological premise; the second independently uses translation-orbit quotient graphs and exact Fourier sums; the third cross-checks signed fixed-face Lefschetz numbers by direct enumeration. A complete 64-row table is in `translation_character.csv`; exact console output is in `verification_output.txt`. All computations have integer data and fixed deterministic input, with ordinary interpreter correctness as a reproducibility assumption. The finite checks are exhaustive for this fixed sixty-four-vertex complex; no arbitrary-alphabet theorem is inferred.

## Relationship to prior work

Galetto, Montaño and Wellner (first publicly available June 18, 2026) compute group-action homology representations of **binary** hypercube Rips complexes; their main theorems concern the hyperoctahedral group of a two-letter cube, not the four-letter three-cube. A previously published exact computation establishes \(\operatorname{VR}_{\le2}((\mathbb Z/4\mathbb Z)^3)\simeq\bigvee^{405}S^3\), but does not compute the translations' homology character or their quotient-space homology. Another published result computes the corresponding \(C_3^3\) translation character for the **three-letter** three-cube, not the composite-alphabet case here. Antolín Camarena and Carnero Bravo's three-factor categorical-product conjecture concerns nonequivariant homotopy, not these representation multiplicities. The binary and ternary cases do not imply the quaternary trace values, particularly the difference between order-two and order-four translations. The mathematical contribution here is precisely that equivariant refinement, **not** the previously established \(405\)-sphere decomposition.

## Limitations

The representation classification concerns only the translation subgroup \((\mathbb Z/4\mathbb Z)^3\), not all independent alphabet permutations or coordinate symmetries. Its statements are rational or complex, not an integral module classification. The quotient results assert rational homology groups and do not determine integral torsion or quotient homotopy types. An unindexed or implicit prior computation might give an equivalent character; this literature risk is not eliminated by search. Exact finite verification depends on successful execution of the included programs, and independent mathematical audit has not been performed.

## References

1. Federico Galetto, Jonathan Montaño and Zoe Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784, first public 2026-06-18, https://arxiv.org/abs/2606.20784 .
2. *Integral Rips homotopy of the quaternary Hamming three-cube*, public mathematical research record (2026-10-25), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-integral-rips-homotopy-of-the-quaternary-hamming-three-cube--05bd751a504e .
3. *Complete ternary translation character of the radius-two Hamming Rips complex*, public mathematical research record (2026-10-25), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-complete-ternary-translation-character-of-the-radius-two-hamming--f98167fe7255 .
4. Omar Antolín Camarena and Andrés Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401, https://arxiv.org/abs/2307.12401 .
5. Robin Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
