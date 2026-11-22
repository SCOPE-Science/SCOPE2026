# The full symmetric-group action on sixth homology of the seven-point Kneser triple complex

## Finding
Let \(X=\operatorname{Ind}(\operatorname{KG}(3,1))\), the simplicial complex whose vertices are the \(35\) three-element subsets of \([7]\) and whose faces are families of pairwise-intersecting triples. The natural \(\mathfrak S_7\) action induces the following **complete rational sixth-homology representation**:
\[
\boxed{\widetilde H_6(X;\mathbb Q)\cong S^{(7)}\oplus S^{(4,3)}\oplus S^{(2,2,2,1)}}.
\]
Here \(S^\lambda\) is the rational Specht representation indexed by a partition \(\lambda\) of seven. The three summands have dimensions \(1,14,14\); the last two are sign twists of one another. In particular the invariant subspace is one-dimensional. Moreover, the geometric quotient \(|X|/\mathfrak S_7\) has the reduced rational homology of \(S^6\). This is a statement about rational homology, not the homotopy type of the quotient.

## Assumptions and scope
The graph \(\operatorname{KG}(3,1)\) has triples of \([7]\) as vertices and disjoint triples as edges. Hence its independence complex consists precisely of pairwise-intersecting collections. All homology actions in this theorem are induced by permuting \([7]\), and all representation decompositions are over \(\mathbb Q\). The theorem concerns the first nontrivial seven-point case, not all \(\operatorname{KG}(3,k)\).

## Proof
**1. Rational homology inputs.** Feng (2026, Theorem 18) proves that \(\widetilde H_j(X;\mathbb Q)\) vanishes except for \(j=6,9\), with dimensions \(29\) and \(7\), respectively. For each six-element \(S\subset[7]\), the induced complex on the triples in \(S\) is the boundary of a ten-dimensional cross-polytope. Feng–Wang (2024, Lemma 9 and Theorem 10) prove that these seven embedded sphere cycles are independent. Combining that result with the published ninth Betti number makes them a rational basis of \(\widetilde H_9(X;\mathbb Q)\). The six-point stabilizer acts on each sphere's orientation by its sign: keeping one point fixed identifies the ten complementary triple-pairs with two-subsets of the other five points; a transposition of two of those five swaps exactly three pairs, reversing orientation. By conjugacy, every transposition reverses the orientation. Thus the known ninth-homology action is
\[
\widetilde H_9(X;\mathbb Q)\cong\bigwedge^6\mathbb Q^7,
\qquad \chi_9(g)=[t^6]\prod_{c\in\mathrm{Cycles}(g)}(1-(-t)^{|c|}).
\]
This ninth-degree representation is a previously available input, **not** the newly claimed result.

**2. Exact equivariant Lefschetz calculation.** Fix a permutation \(g\in\mathfrak S_7\). Partition the 35 triples into \(g\)-orbits. Discard an orbit if it contains two disjoint triples. On the surviving orbits construct the incompatibility graph \(F_g\): two orbits are joined if some triple in one is disjoint from a triple in the other. A face of \(X\) is setwise fixed by \(g\) exactly when it is a nonempty union of a set of pairwise compatible surviving orbits. An orbit of length \(d\) contributes \((-1)^{d-1}\) to the orientation sign, while the chain-degree factor is \((-1)^{d}\). Consequently the reduced Lefschetz number is
\[
\widetilde L(g)=-I(F_g;-1),\qquad
I(F_g;z)=\sum_{J\text{ independent in }F_g}z^{|J|}.
\]
The reduced Hopf trace formula and the known rational homology concentration therefore give
\[
\chi_6(g)=\widetilde L(g)+\chi_9(g)=-I(F_g;-1)+\chi_9(g).
\]
The identity also satisfies this equation, giving \(\chi_6(1)=29\).

**3. Finite class computation.** The fifteen conjugacy classes of \(\mathfrak S_7\), displayed by cycle type, yield the following exact character values. The two middle columns can be independently reconstructed from the public checker.

| Cycle type | \(I(F_g;-1)\) | \(\chi_9\) | \(\chi_6\) |
| --- | ---: | ---: | ---: |
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

For the incompatibility graph, the integer recurrence \(I(F;-1)=I(F-v;-1)-I(F-N[v];-1)\) with \(I(\varnothing;-1)=1\) computes every entry without approximations. Independently enumerating the compatible subsets of the orbit graph gives the same numbers. The Murnaghan–Nakayama rule yields inner products of \(\chi_6\) with all 15 irreducible characters equal to one for partitions \((7)\), \((4,3)\), \((2,2,2,1)\) and zero for the others. Since rational Specht characters exhaust the irreducible rational representations, this proves the displayed decomposition.

**4. Quotient consequence.** For a finite group action on a finite complex, barycentric subdivision gives a simplicial action for which rational homology of the quotient is the invariant part. The decomposition above gives one invariant line in degree six. The known \(\bigwedge^6\mathbb Q^7\) ninth-homology representation has no invariant line, and the other reduced rational homology groups vanish. Hence \(|X|/\mathfrak S_7\) is a rational homology six-sphere.

## Verification
Run \(\texttt{python3 verify_kg7_character.py}\) with Python's standard library. For each conjugacy class the checker independently builds the triple orbits and their incompatibility graph, computes the independence polynomial at negative one by (a) vertex deletion and (b) direct compatible-orbit enumeration, and computes all 15 Specht inner products using an explicit rim-hook implementation of Murnaghan–Nakayama. Both methods agree on every class; the verified character decomposition is exactly the claim. The checker uses Feng's published rational Betti numbers as external mathematical premises; it does not recompute the full 35-vertex complex's chain homology independently.

## Relationship to prior work
Feng and Wang (2024) proved independence of the embedded cross-polytopal sphere cycles, hence a lower bound for ninth homology, but did not determine the sixth-homology representation. Feng (first posted October 12, 2026) computed the rational sixth and ninth Betti numbers but did not determine their full symmetry actions and explicitly identified the degree-six generator problem as open. A previous calculation of the exterior-power representation in ninth homology covers only that known input. The new contribution here is the exact **sixth-degree** \(\mathfrak S_7\)-character, its multiplicity-free three-summand decomposition, and the rational quotient-homology consequence.

## Limitations
The result is rational and specific to seven ground elements. It does not identify an explicit integral or combinatorial basis in degree six, settle possible torsion, determine the integral representation or the homotopy type of \(X\), or give an all-parameter equivariant classification. A literature search cannot exclude unindexed equivalent work; an independent mathematical audit has not been performed.

## References
1. Z. Feng, *The rational homology of independence complexes of Kneser graphs on triples*, arXiv:2610.17394 (first posted 2026-10-12), Theorem 18 and Section 7. https://arxiv.org/abs/2610.17394
2. Z. Feng and G. Wang, *Exploring Homological Properties of Independent Complexes of Kneser Graphs*, arXiv:2404.10566 (first posted 2024-04-16), Lemma 9 and Theorem 10. https://arxiv.org/abs/2404.10566
3. Standard Hopf trace formula, simplicial Lefschetz theory, and the Murnaghan–Nakayama character rule.
