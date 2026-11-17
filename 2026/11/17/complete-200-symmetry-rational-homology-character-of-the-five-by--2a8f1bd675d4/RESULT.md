# Complete 200-symmetry rational homology character of the five-by-five toroidal hard-square complex

## Finding
Let \(G=C_5\square C_5\) be the Cartesian product of two five-cycles, with vertices \((a,b)\in(\mathbb Z/5\mathbb Z)^2\) and edges at cyclic coordinate distance one. Set \(X=\operatorname{Ind}(G)\), the independence simplicial complex. The natural toroidal symmetry group \(H=(D_5\times D_5)\rtimes C_2\) (two coordinate dihedral actions and interchange of coordinates) has order \(200\). Every element can be uniquely written
\[
g(a,b)=\begin{cases}(s a+u,t b+v)&\text{if }e=0,\\(s b+u,t a+v)&\text{if }e=1,\end{cases}
\]
where \(e\in\{0,1\}\), \(s,t\in\{-1,1\}\), and \(u,v\in\mathbb Z/5\mathbb Z\). Its complete rational fourth-homology character \(\chi(g)=\operatorname{tr}(g\mid\widetilde H_4(X;\mathbb Q))\) is the following explicit finite formula:
\[
\boxed{\chi(g)=-\sum_{T\in\mathcal I(g)}(-1)^{|T|}.}
\]
Here \(\mathcal I(g)\) consists of collections \(T\) of vertex orbits of \(\langle g\rangle\), including the empty collection, whose entire union is independent in \(G\). This prescription determines the character at every group element without any homology matrix computation. The exact distribution on all \(200\) elements is
\[
\boxed{\#\chi^{-1}(9)=1,\quad\#\chi^{-1}(4)=8,\quad\#\chi^{-1}(1)=75,\quad\#\chi^{-1}(-1)=116.}
\]
Moreover the \(25\)-element translation subgroup has traces \(9\) at the identity, \(4\) on the eight nonzero translations whose displacement lies on one of the two lines of slope \(\pm2\), and \(-1\) on the other sixteen nonzero translations. Therefore
\[
\dim_\mathbb Q\widetilde H_4(X;\mathbb Q)^H=0,\qquad
\dim_\mathbb Q\widetilde H_4(X;\mathbb Q)^{(\mathbb Z/5)^2}=1.
\]
In particular the ordinary quotient \(|X|/H\) has no positive-degree rational homology. This calculation refines the previously published, and explicitly credited, homotopy equivalence \(X\simeq\bigvee^9S^4\).

## Assumptions and scope
The graph is the *fully periodic square grid* with five rows and five columns, **not** the open square grid, a cylindrical grid, the graph Rips complex, or a diagonal-neighbor variant. An independent subset contains no two vertices at toroidal Manhattan distance one. The \(H\)-action is by relabeling vertices and acts simplicially on \(X\). The character is a representation over \(\mathbb Q\) only, not an integral module classification. The already established homotopy type of \(X\) is used to pass from a Lefschetz alternating trace to a single homology degree; the character computation itself is new to the inspected literature.

## Proof
**Group action.** The formula for \(g\) permutes coordinates, changes their cyclic orientations, and translates them. Such maps preserve each elementary toroidal edge. The parameters give \(2\cdot2\cdot2\cdot5\cdot5=200\) distinct permutations. These transformations generate \((D_5\times D_5)\rtimes C_2\). In fact this is the complete graph automorphism group by uniqueness of prime Cartesian factors, though only the explicit group action is needed below.

**The fixed-face trace formula.** Write \(C_j(X;\mathbb Q)\) for oriented simplicial chains, including degree \(-1\). For a simplex \(F\) preserved setwise by \(g\), suppose its vertices are the disjoint union of \(c\) cycles of the vertex permutation. The induced orientation sign on \(F\) is \((-1)^{|F|-c}\). Its contribution to the reduced alternating chain trace is therefore \((-1)^{|F|-1}(-1)^{|F|-c}=(-1)^{c+1}\). Nonfixed simplices contribute zero. A setwise invariant independent face is precisely a union of vertex orbits, and admissible unions are the collections \(\mathcal I(g)\) appearing above. The empty simplex contributes \(-1\) to the reduced alternating trace. Summing proves \(\widetilde L(g;X)=-\sum_{T\in\mathcal I(g)}(-1)^{|T|}\), without approximation.

**Passage to homology.** The published integral discrete-Morse computation for exactly \(C_5\square C_5\) gives \(\widetilde H_4(X;\mathbb Q)\cong\mathbb Q^9\) and zero reduced homology in all other degrees. The Hopf trace theorem applied to the finite simplicial chain complex implies \(\chi(g)=\widetilde L(g;X)\). Thus the orbit-sum formula calculates the full fourth-homology character. This use of a prior nonequivariant result is essential and is not claimed as a new proof of its homotopy type.

**Exact 200-element evaluation.** The accompanying `torus_character_verify.py` constructs the graph's 25 adjacency masks, enumerates all 25,531 independent faces, generates the 200 distinct vertex permutations, decomposes each into cycles, discards orbit blocks that already contain an edge, builds the incompatibility graph on remaining orbit blocks, and evaluates its independent-set polynomial at \(-1\) by the exact deletion recurrence. No truncated search, floating-point operations, heuristic identification, or random choices are used. The resulting character values appear individually in `torus_character_data.json` and have the stated histogram. A separate signed-oriented-simplex implementation checks four selected elements, including the identity, nontrivial translation, reflection, and a nonidentity translated half-turn.

**Invariant dimensions.** Since \(H\) is finite over characteristic zero, averaging the character gives the dimension of its invariant subspace. The complete sum is \(9+8\cdot4+75-116=0\), hence the full-group fixed dimension is zero. For translations, the sum is \(9+8\cdot4-16=25\); dividing by \(25\) gives one invariant class. The rational homology of a finite group quotient agrees with invariant rational homology under this action, so the full quotient is rationally acyclic in positive degrees.

## Verification
Run `python3 torus_character_verify.py` in a directory containing this script; it creates `torus_character_data.json`. Compare the generated JSON byte-for-byte with the supplied data file, and standard output with `torus_character_output.txt`. Independent faces, all \(200\) permutations, the histogram, both averaging sums, and four direct signed oriented-chain traces are asserted by the program. No assertion is made that finite numerical experiments establish the previously published ordinary homotopy theorem; the current calculation is a complete finite enumeration of a specified 200-element representation.

## Relationship to prior work
Jonsson (2006) determined the signed independent-set enumeration for toroidal hard-square grids, i.e. their reduced Euler characteristic, not a graded automorphism character. Bousquet-Mélou, Linusson, and Nevo (2007) treated the homotopy of *open and cylindrical* grids. The accessible published note *Nine integral four-spheres in the fully periodic five-by-five hard-square complex* established precisely \(X\simeq\bigvee^9S^4\) using a complete acyclic matching, but expressly did not determine a symmetry representation. A separate published result on the scale-three Vietoris–Rips complex of the same underlying toroidal graph gives a nine-dimensional translation homology character with the same translation trace pattern; it concerns a **different simplicial complex** (pairs have distance at most three, instead of being nonadjacent), and determines only translations. Neither statement determines the complete \(200\)-element character for \(X\), particularly its reflection and coordinate-swap traces. The agreement of the translation trace patterns is noted as a potential comparison direction, not an asserted canonical equivalence.

## Limitations
The result applies only to the five-by-five graph and the indicated group. It describes the rational character and rational quotient homology, not an integral symmetry lattice, an equivariant homotopy model, or a larger-grid formula. An undiscovered identification with the related scale-three Rips complex might provide an alternative derivation of the translation restriction, but no identified source supplies the remaining full-group comparison. Independent audit has not been performed.

## References
1. J. Jonsson, *Hard Squares with Negative Activity and Rhombus Tilings of the Plane*, Electronic Journal of Combinatorics 13 (2006), R67, published 2006-08-07, DOI:10.37236/1093, https://www.combinatorics.org/ojs/index.php/eljc/article/view/v13i1r67.
2. P. Fendley, K. Schoutens, H. van Eerten, *Hard squares with negative activity*, arXiv:cond-mat/0408497 (2004).
3. M. Bousquet-Mélou, S. Linusson, E. Nevo, *On the independence complex of square grids*, arXiv:math/0701890 (2007).
4. *Nine integral four-spheres in the fully periodic five-by-five hard-square complex* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-nine-integral-four-spheres-in-the-fully-periodic-five-by-five-ha--374b6b4d37f7.
5. *Translation-fixed spaces of the five-by-five torus-grid Rips complex at scale three* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-translation-fixed-spaces-of-the-5-times5-torus-grid-rips-complex--84079f5fd0c0.
6. The Hopf trace formula for finite simplicial chain complexes (standard).
