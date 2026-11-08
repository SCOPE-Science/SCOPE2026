# Homotopy classification of the two thirteen-point Steiner line-avoiding complexes

## Finding
There are precisely two isomorphism classes of Steiner triple systems on thirteen points. Their **line-avoiding simplicial complexes** have different integral homotopy types:

\[
\operatorname{Ind}(\mathcal C)\simeq\bigvee^{12}S^4,
\qquad
\operatorname{Ind}(\mathcal N)\simeq\bigvee^{17}S^4.
\]

Here \(\mathcal C\) is the cyclic system and \(\mathcal N\) the noncyclic system. The first complex has 39 independent six-point faces and the second has 34; these enumerative counts and their Euler characteristics are not the novelty claim. The claim is the complete **integral homotopy type in both isomorphism classes**, including the vanishing of every lower homotopy group below degree four and the absence of nontrivial attaching maps in the final Morse models.

## Assumptions and scope
A Steiner triple system on \(V\) is a set \(\mathcal B\) of three-element subsets (blocks) such that every unordered pair of distinct points belongs to exactly one block. Its line-avoiding complex is
\[
\operatorname{Ind}(V,\mathcal B)=\{U\subseteq V:\text{no block }B\in\mathcal B\text{ is contained in }U\}.
\]
Its geometric realization is understood. All groups, chain boundaries, and homotopy equivalences below are integral, not just rational or mod two.

Use \(V=\mathbb Z/13\mathbb Z\), represented by integers 0 through 12. The cyclic block set is
\[
\mathcal B_C=\big\{\{t,t+1,t+4\},\{t,t+2,t+7\}:t\in\mathbb Z/13\mathbb Z\big\},
\]
with arithmetic modulo thirteen. The second block set is obtained by deleting
\[
\{014,027,179,249\}
\]
and inserting
\[
\{017,024,149,279\},
\]
where a three-digit string represents an unordered triple of one-digit vertices. This is a Pasch trade: the deleted and inserted triples contain exactly the same twelve unordered pairs. The resulting system is nonisomorphic to the cyclic system, as their independent six-set counts differ. The 2003 classification of Grannell, Griggs and Knor identifies these as the two exhaustive isomorphism classes.

## Proof
**1. Verification of the two designs and face sets.** The two cyclic base triples have pair differences representing the six nonzero difference classes modulo sign. Their thirteen translates each cover all 78 unordered pairs exactly once. The Pasch exchange preserves every pair multiplicity, so the second family is likewise a 26-block Steiner triple system. Two independent enumeration procedures (direct testing of all 8,192 bitmasks and recursive allowable-set extension) agree on the following face counts, with the initial entry denoting the empty face:

| Complex | Empty | Vertices | Edges | Triangles | Tetrahedra | Five-vertex faces | Six-vertex faces |
|---|---:|---:|---:|---:|---:|---:|---:|
| \(\operatorname{Ind}(\mathcal C)\) | 1 | 13 | 78 | 260 | 455 | 312 | 39 |
| \(\operatorname{Ind}(\mathcal N)\) | 1 | 13 | 78 | 260 | 455 | 312 | 34 |

There are no larger faces. Among the five-vertex faces, respectively 117 and 132 are maximal rather than faces of six-vertex simplices, so **both complexes are nonpure**. Thus purity-based shellability arguments cannot supply these homotopy conclusions directly.

**2. A reproducible acyclic matching.** Encode a face as the sum of powers of two corresponding to its points. Starting with all allowed faces (including the empty face), for \(i=0,1,\ldots,12\), pair each still-unpaired face \(F\) not containing \(i\) with \(F\cup\{i\}\), when both remain unpaired. Process eligible bitmasks in increasing order. Remove the augmented pair (empty face, vertex 0) and regard vertex 0 as the distinguished critical zero-cell. In the ordinary face poset, direct enumeration and topological sorting of all incidence arrows, oriented **up** along pairs and **down** along all other coverings, proves that neither matching contains a directed cycle.

The cyclic complex has 1,157 nonempty faces, 4,550 ordinary Hasse coverings, and 566 matched pairs, leaving one critical zero-cell, six critical three-cells and eighteen critical four-cells. The switched complex has 1,152 nonempty faces, 4,520 Hasse coverings, and 563 matched pairs, leaving one critical zero-cell, four critical three-cells and twenty-one critical four-cells. All numbers are recomputed from the definitions by `verify.py`.

By Forman's discrete Morse theorem each complex has a homotopy-equivalent CW model with exactly the corresponding critical cells. Since there are no critical one- or two-cells, the three-skeleton of each model is a wedge of three-spheres.

**3. Signed attaching degrees.** Orient each simplex by increasing vertex labels, so deleting the \(j\)-th vertex has coefficient \((-1)^j\), with \(j\) starting at zero. For each critical four-cell, take its signed simplicial boundary. Eliminate matched three-faces in the acyclic order: if a matched three-face \(\sigma\) has partner \(\tau\), subtract the current coefficient of \(\sigma\) times the signed boundary of \(\tau\), divided by the unit incidence \([\tau:\sigma]=\pm1\). The remaining coefficients on critical three-faces form the integer Morse boundary \(\partial_4^M\).

Two distinct implementations, an ordered sparse elimination and a memoized gradient recursion, agree entry by entry. In ascending critical-face bitmask order, the cyclic boundary has dimensions \(6\times18\) and its columns numbered \((0,1,3,4,5,8)\) form a determinant-\(+1\) minor. The switched boundary has dimensions \(4\times21\) and its columns \((0,1,2,7)\) form another determinant-\(+1\) minor. Thus each boundary is surjective over \(\mathbb Z\) and has kernel of ranks 12 and 17 respectively, with no torsion. Full unit minors are stronger certificates than ranks over fields.

**4. Passage from chains to homotopy.** Since each Morse three-skeleton is a wedge of three-spheres, its third Hurewicz homomorphism is an isomorphism. Consequently the attaching maps of the four-cells are determined by precisely the integral degree matrices above. Integral changes of bases in the third and fourth cellular groups (realized by homotopy equivalences and cellular handle-slides) reduce these surjective matrices to \([I\;0]\). Cancelling the corresponding three/four-cell pairs leaves exactly twelve, respectively seventeen, four-spheres. This proves the announced homotopy equivalences, not merely homology calculations.

## Verification
Run `python3 verify.py` with a Python 3 interpreter; only the standard library is required. This program reconstructs the two block systems and the Pasch-trade pair equality, checks all faces by two methods, exhaustively checks the incidence-oriented matching digraphs for acyclicity, constructs the signed critical-to-critical boundary by two algorithms, finds and checks the indicated unimodular maximal minors by exact integer Bareiss determinants, and independently computes the ordinary mod-two simplicial Betti numbers. The file `verification_output.txt` records the output from the included verifier, ending with `ALL_CHECKS_PASS`. The checking procedure is exhaustive for these two finite complexes; it does not enumerate or classify all Steiner triple systems independently, for which the cited established classification is used.

## Relationship to prior work
Grannell, Griggs and Knor (2003) establish that there are exactly two isomorphism classes at order thirteen, identify their cyclic and noncyclic forms and record the Pasch-switch relation. Forbes, Grannell and Griggs (2004) give formulas for the numbers of independent point subsets in arbitrary Steiner triple systems, thereby supplying strong existing enumerative information and in particular covering the type of face-count data used here. Neither of those inspected papers states the integral homotopy equivalences proved above or provides the required attaching-map calculations. Pavone (2023) gives a later geometric representation of the two order-thirteen systems, but an accessible abstract alone does not establish whether its full treatment contains any topological computation; no such content is claimed absent from its unread full text.

## Limitations
The conclusion concerns the line-avoiding simplicial complexes of the two thirteen-point systems only. It does not classify analogous complexes at orders fifteen or above, determine equivariant homotopy or the automorphism representations on homology, establish shellability, or independently validate the literature classification of Steiner triple systems. A finite exhaustive calculation proves only what its explicit domain covers. No independent mathematical review has been performed. A complete publication-priority guarantee is not available: equivalent unindexed work and inaccessible relevant material remain possible.

## References
1. M. J. Grannell, T. S. Griggs and M. Knor, *Face two-colourable triangulations of \(K_{13}\)*, Journal of Combinatorial Mathematics and Combinatorial Computing 47 (2003), 75–81. https://combinatorialpress.com/article/jcmcc/Volume%20047/vol-047-paper%205.pdf
2. A. D. Forbes, M. J. Grannell and T. S. Griggs, *Independent sets in Steiner triple systems*, Ars Combinatoria 72 (2004), 161–169. https://combinatorialpress.com/article/ars/Volume%20072/volume-72-paper-16.pdf
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. https://doi.org/10.1006/aima.1997.1650
4. M. Pavone, *A visual representation of the Steiner triple systems of order 13*, The Art of Discrete and Applied Mathematics 6 (2023), 1–22. https://doi.org/10.26493/2590-9770.1564.2b8
