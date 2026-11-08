# The full sixth-homology symmetry of pairwise-intersecting triples on seven labels

## Finding

Let \(X\) be the finite simplicial complex whose vertices are the \(35\) three-element subsets of \([7]=\{1,\ldots,7\}\) and whose simplices are **pairwise-intersecting** collections of those triples. Equivalently, \(X=\operatorname{Ind}(\operatorname{KG}(3,1))\), or the inclusive radius-four symmetric-difference Vietoris–Rips complex on all triples of a seven-element set. The natural action of \(\mathfrak S_7\) on labels induces, over \(\mathbb Q\),

\[
\boxed{\widetilde H_6(X;\mathbb Q)\cong_{\mathbb Q[\mathfrak S_7]} S^{(7)}\oplus S^{(4,3)}\oplus S^{(2,2,2,1)}.}
\]

Each irreducible appears once, with dimensions \(1,14,14\), respectively. Thus the sixth homology has precisely one globally invariant rational line and no sign subrepresentation. Writing \(\varepsilon(g)\) for the sign of a permutation and \(f_j(g)\) for the number of its invariant \(j\)-element subsets of \([7]\), its character is

\[
\boxed{\chi_6(g)=1+(1+\varepsilon(g))(f_3(g)-f_2(g)).}
\]

In particular, every odd permutation has sixth-homology trace exactly \(1\). The theorem concerns the rational representation, not integral torsion or the entire homotopy type.

## Assumptions and scope

The graph \(\operatorname{KG}(3,1)\) has as vertices all triples from a seven-element set and connects two triples when they are disjoint. The complex \(X\) is its **ordinary independence complex**. Group actions are the actual geometric simplicial actions induced by permutations of the ground set. Specht notation \(S^\lambda\) is over \(\mathbb Q\). All homology is reduced unless explicitly noted. The first public version of the motivating rational-homology theorem appeared on 2026-10-12 (arXiv:2610.17394), and its primary classification is in topological homology, MSC 55N31.

## Proof

**Step 1: known rational homology dimensions only.** Feng's Theorem 18 (arXiv:2610.17394) establishes, for this exact complex, that the only nonzero reduced rational homology groups have degrees \(6\) and \(9\), of dimensions \(29\) and \(7\). We do **not** assume any previously computed equivariant homology representation. The two individual group characters will both be recovered from the new fixed-point calculation and the dimensions by a saturation argument in Step 4.

**Step 2: a finite fixed-simplex model.** Fix \(g\in\mathfrak S_7\). It permutes the \(35\) triple vertices. A point of the geometric complex is fixed precisely when its barycentric coefficients are constant on every \(g\)-orbit of triple vertices; an orbit is admissible only if its union is a face of \(X\). Two such admissible orbits may coexist if all cross-orbit triple pairs intersect. Hence \(|X|^{\langle g\rangle}\) is PL-homeomorphic to the independence complex of the finite **orbit incompatibility graph** \(B_g\): its vertices are internally pairwise-intersecting triple orbits, and two vertices are adjacent if any triple in one orbit is disjoint from a triple in the other. This is an exact model, not a quotient-space heuristic.

Let \(P_g(z)=\sum_I z^{|I|}\), where the sum ranges over independent vertex sets \(I\) in \(B_g\), including the empty set. Then

\[
\widetilde\chi\bigl(|X|^{\langle g\rangle}\bigr)=-P_g(-1).
\]

For an induced incompatibility graph \(B\) and any vertex \(v\), the exact polynomial recursion is

\[
P_B(-1)=P_{B-v}(-1)-P_{B-N[v]}(-1),\qquad P_{\varnothing}(-1)=1.
\]

**Step 3: all conjugacy classes, with exact integer arithmetic.** Conjugacy classes of \(\mathfrak S_7\) correspond to the fifteen integer partitions of seven. For each cycle type, construct one representative, enumerate all triple orbits, exclude internally incompatible ones, build all pairwise incompatibilities, and evaluate the recursion above. The exhaustive resulting table is below. The column \(p\) is \(P_g(-1)\); the last two columns are the ordinary rational homology traces **deduced below**, not presumed as input.

| Cycle type | \(p\) | \(\chi_9\) | \(\chi_6\) |
|---|---:|---:|---:|
| \((7)\) | -1 | 0 | 1 |
| \((6,1)\) | -2 | -1 | 1 |
| \((5,2)\) | -1 | 0 | 1 |
| \((5,1,1)\) | 3 | 2 | -1 |
| \((4,3)\) | -1 | 0 | 1 |
| \((4,2,1)\) | 0 | 1 | 1 |
| \((4,1,1,1)\) | -4 | -3 | 1 |
| \((3,3,1)\) | -4 | 1 | 5 |
| \((3,2,2)\) | 1 | 0 | -1 |
| \((3,2,1,1)\) | -3 | -2 | 1 |
| \((3,1,1,1,1)\) | 5 | 4 | -1 |
| \((2,2,2,1)\) | -2 | -1 | 1 |
| \((2,2,1,1,1)\) | -2 | 3 | 5 |
| \((2,1,1,1,1,1)\) | -6 | -5 | 1 |
| \((1,1,1,1,1,1,1)\) | -22 | 7 | 29 |

The reduced Lefschetz fixed-point formula, with only degrees \(6\) and \(9\) nonzero, gives the **virtual** character

\[
V(g)=\chi_6(g)-\chi_9(g)=-P_g(-1).
\]

**Step 4: irreducible decomposition and saturation.** Recover the irreducible characters of \(\mathfrak S_7\) from the Young-permutation characters \(M^\lambda\), using the integer-valued class inner product

\[
\langle a,b\rangle=\frac{1}{7!}\sum_{\mu\vdash 7}\frac{7!}{z_\mu}a(\mu)b(\mu).
\]

The character \(M^\lambda(\mu)\) counts assignments of the cycles of a permutation of type \(\mu\) to labeled rows of sizes \(\lambda\). Triangular subtraction yields the \(15\) irreducible Specht characters. Decomposing the independently computed virtual character gives exactly

\[
V = S^{(7)}+S^{(4,3)}+S^{(2,2,2,1)}-S^{(2,1,1,1,1,1)}-S^{(1,1,1,1,1,1,1)}
\]

in the rational representation ring. The sum of positive dimensions is \(1+14+14=29\), **exactly** Feng's degree-six Betti dimension, while the sum of negative dimensions is \(6+1=7\), **exactly** the degree-nine dimension. In a semisimple representation category, the two actual modules realizing a virtual difference can only add common irreducible summands to this positive/negative split. The two dimension equalities leave no room for any common summand. Thus the positive portion is precisely \(\widetilde H_6(X;\mathbb Q)\), and the negative portion is precisely \(\widetilde H_9(X;\mathbb Q)\). Both are determined **without assuming the previously published ninth-degree character**.

The negative portion equals the sign-twisted seven-dimensional permutation representation, providing an independent check against prior ninth-degree calculations. Its trace is \(\chi_9(g)=\varepsilon(g)f_1(g)\). By Young's rule the two-row Specht character \(S^{(4,3)}\) is \(f_3-f_2\), and sign twist conjugates its partition to \(S^{(2,2,2,1)}\). Accordingly \(\chi_6(g)=1+(1+\varepsilon(g))(f_3(g)-f_2(g))\), as claimed. Here \(f_j(g)=[u^j]\prod_{c\in\operatorname{Cyc}(g)}(1+u^{|c|})\). The fifteen-class table gives the exact traces in both homology degrees, including all signs and the empty-face correction. This proves the finding by Maschke's theorem.

## Verification

Run `python3 verify.py` with Python's standard library. The program enumerates all \(35\) triples, calculates all fifteen conjugacy-class orbit-graphs and their independent-set polynomials by memoized deletion–link recursion, verifies the closed character formula, and reconstructs all Specht characters by Young permutation modules and exact class-weighted inner products. The checker independently decomposes the virtual character, verifies its positive and negative dimension saturation, and asserts the two multiplicity-free homology decompositions and class-size totals. The supplied `verification_output.txt` is a recorded run, not a substitute for replay.

The identity case also admits a separate face-count cross-check: the number of independent triple-families by cardinality \(0\) through \(15\) is

`[1,35,525,4445,23555,81942,191170,300855,317730,221865,100296,29295,5950,910,105,7]`.

Its alternating sum is \(-22\), matching the independently computed fixed-orbit recurrence. This census is finite and exhaustive by the explicit recursion; it does not assert integral homology.

## Relationship to prior work

Feng (2026) gives rational Betti numbers and the two possible nonzero degrees for all triple Kneser independence complexes, but does not decompose the natural symmetric-group action. Feng and Wang (2024) establish explicit homology constructions and finite mod-two ranks. The existing six-support exterior-power result determines the **degree-nine** representation for all numbers of labels; it neither determines nor implies the **degree-six** representation without an additional equivariant Lefschetz calculation. The present classification supplies the complete, previously unspecified \(29\)-dimensional representation in the smallest nontrivial triple case, including a unique invariant line and the parity-sensitive trace law. Related symmetric-group calculations for neighborhood complexes of other Kneser graphs concern different simplicial complexes and cannot imply this result. No claim of uniqueness is made solely from failed searches.

## Limitations

Only \(X=\operatorname{Ind}(\operatorname{KG}(3,1))\) and rational homology are classified. Neither a concrete geometric basis in degree six, an integral torsion classification, a wedge-of-spheres homotopy type, nor the \(\mathfrak S_m\)-modules for all larger \(m\) follows. The independent ninth-degree literature result is used only as a consistency check; the new computation derives both equivariant characters from the two published Betti dimensions, with no input ninth-degree character.

## References

1. Ziqin Feng, *The rational homology of independence complexes of Kneser graphs on triples*, arXiv:2610.17394, first submitted 2026-10-12; full accessible primary HTML, especially Theorem 18 and Sections 6–7.
2. Ziqin Feng and Guanghui Wang, *Exploring Homological Properties of Independent Complexes of Kneser Graphs*, arXiv:2404.10566, first submitted 2024-04-16.
3. *Exterior sixth-power symmetry in ninth Kneser-complex homology*, published mathematical research record, October 2026; prior top-degree exterior-power representation theorem.
4. Standard finite-group representation theory: Young's rule for two-row Specht modules and the rational character classification of \(\mathfrak S_7\).
