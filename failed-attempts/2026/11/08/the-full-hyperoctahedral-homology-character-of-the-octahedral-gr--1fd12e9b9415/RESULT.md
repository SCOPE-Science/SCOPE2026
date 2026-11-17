# The full hyperoctahedral homology character of the octahedral-graph Morse complex

## Finding
Let \(O=K_{2,2,2}\) be the octahedral graph, with opposite vertex pairs \(\{0,1\}\), \(\{2,3\}\), \(\{4,5\}\). Let \(X=\mathcal M(O)\) denote its **ordinary discrete Morse complex**, not its ordinary edge-matching complex: vertices of \(X\) are incidence pairs \((v,vw)\), and a simplex is a compatible acyclic discrete vector field on the graph. Reversing the orientation of every selected edge identifies a simplex with a directed forest rooted at its components.

Write \(G=\operatorname{Aut}(O)\cong C_2\wr S_3=(C_2)^3\rtimes S_3\), of order 48. Its irreducible rational representations are indexed by bipartitions \((\lambda,\mu)\) of 3; denote them by \(V_{\lambda,\mu}\). The **complete rational homology module** is concentrated in degree four, and is
\[
\widetilde H_4(X;\mathbb Q)\cong\bigoplus_{|\lambda|+|\mu|=3}V_{\lambda,\mu}^{\oplus m_{\lambda,\mu}},
\qquad \widetilde H_j(X;\mathbb Q)=0\quad(j\ne4).
\]
The following table specifies all multiplicities, as well as the dimensions of the irreducibles. The bipartition labels in the table use ordinary partition notation, with `()` meaning the empty partition.

| Positive partition | Negative partition | Irreducible dimension | Multiplicity |
|---|---|---:|---:|
| `()` | `(1,1,1)` | 1 | 14 |
| `()` | `(2,1)` | 2 | 29 |
| `()` | `(3)` | 1 | 17 |
| `(1)` | `(1,1)` | 3 | 44 |
| `(1)` | `(2)` | 3 | 39 |
| `(1,1)` | `(1)` | 3 | 42 |
| `(1,1,1)` | `()` | 1 | 15 |
| `(2)` | `(1)` | 3 | 45 |
| `(2,1)` | `()` | 2 | 25 |
| `(3)` | `()` | 1 | 11 |

Equivalently, the complete homology character \(\chi(g)=\operatorname{tr}(g\mid\widetilde H_4(X;\mathbb Q))\) is as follows, with rows indexed by the **positive and negative signed cycle partitions** of the three paired blocks. A signed cycle is positive when the number of within-block flips along the cycle is even, and negative otherwise.

| Positive cycles | Negative cycles | Conjugacy-class size | Character |
|---|---|---:|---:|
| `()` | `(1,1,1)` | 1 | -25 |
| `()` | `(2,1)` | 6 | 1 |
| `()` | `(3)` | 8 | -1 |
| `(1)` | `(1,1)` | 3 | -5 |
| `(1)` | `(2)` | 6 | 1 |
| `(1,1)` | `(1)` | 3 | -9 |
| `(1,1,1)` | `()` | 1 | 675 |
| `(2)` | `(1)` | 6 | -15 |
| `(2,1)` | `()` | 6 | -3 |
| `(3)` | `()` | 8 | 3 |

The antipodal involution \(z\), which reverses each opposite pair, has trace \(-25\). Thus its positive and negative eigenspaces in fourth homology have respective dimensions \(325\) and \(350\). The fixed subspace under all of \(G\) has dimension \(11\). In particular, the full orbit-space **rational cohomology ring** is
\[
H^*(|X|/G;\mathbb Q)\cong
\mathbb Q[\alpha_1,\ldots,\alpha_{11}]/(\alpha_i\alpha_j:1\le i,j\le11),\qquad |\alpha_i|=4.
\]
This ring description asserts neither an integral cohomology calculation nor a homotopy equivalence between the orbit space and a wedge of spheres.

## Assumptions and scope
The graph \(O\) has vertices numbered \(0\) through \(5\); two distinct vertices are adjacent unless they belong to the same specified opposite pair. An incidence arrow \((u,v)\) means that vertex \(u\) is paired with edge \(\{u,v\}\), so a valid set of arrows has at most one arrow with any given tail, uses each underlying edge at most once, and contains no directed cycle. There are exactly 24 allowed arrows, hence \(X\) has 24 vertices.

The full automorphism group permutes the three opposite pairs and independently flips their ends. All (co)homology is over \(\mathbb Q\) unless the coefficient ring is explicitly stated. An irreducible \(V_{\lambda,\mu}\) is induced from the subgroup preserving a selected set of \(|\lambda|\) signed coordinate pairs, using the symmetric-group Specht module \(S^\lambda\) on that set, and the sign of flips times \(S^\mu\) on its complement. All ten resulting characters are rational-valued and afforded over \(\mathbb Q\).

The previously established nonequivariant homotopy type \(X\simeq\bigvee^{675}S^4\) is **background, not a new claim**. The claim here is the complete module decomposition, signed-cycle character, antipodal splitting, and full-symmetry orbit-space rational cohomology.

## Proof
**1. Identify the simplices and homology concentration.** The complex of acyclic incidence fields is the simplicial complex of directed forests of \(O\) with outdegree at most one at each vertex. Exhaustive enumeration by all \(5^6=15625\) possible choices of an outgoing neighbor or none gives the augmented face counts
\[
(f_{-1},f_0,f_1,f_2,f_3,f_4)=(1,24,228,1072,2496,2304).
\]
A separate enumeration by subsets of the 24 arrows produces exactly the same face set. Applying the deterministic matching in `verify_octahedral_morse_character.py` leaves one critical vertex and 675 critical four-simplices, after 2724 face pairs. The checker builds every one of the 25176 nonempty-face Hasse cover incidences, reverses the matched incidences, and proves acyclicity by exhausting a topological ordering. Forman's elementary acyclic-matching theorem therefore gives \(X\simeq\bigvee^{675}S^4\). This verifies the required rational homology concentration independently of published nonequivariant computations.

**2. Compute the complete character.** Represent \(g\in G\) by a permutation \(p\in S_3\) of opposite pairs and three binary flips \(f_0,f_1,f_2\). It permutes incidence arrows by \((u,v)\mapsto(g(u),g(v))\). For any face \(\sigma\) fixed as a set, this map acts on the oriented simplex by the sign of the induced permutation of its ordered arrow vertices. Let \(t_k(g)\) be the sum of these signs over the fixed \(k\)-element faces; set \(t_0(g)=1\) for the empty simplex. The reduced simplicial Lefschetz formula, and the fact that reduced homology is concentrated in even degree four, give the **exact integer**
\[
\chi(g)=\sum_{k=0}^5(-1)^{k-1}t_k(g)
=-1+\sum_{k=1}^5(-1)^{k-1}t_k(g).
\]
The checker enumerates all 48 elements, checks that they preserve every face, and evaluates every fixed-face orientation sign. Each of the ten signed-cycle classes has a constant trace, and its computed class size and trace are the ten rows above. This gives the character on every element, not merely selected generators.

**3. Decompose the character.** Irreducible characters of \(C_2\wr S_3\) are indexed by bipartitions \((\lambda,\mu)\) of 3. For each element \((p,f)\), their character is the induction sum
\[
\chi_{\lambda,\mu}(p,f)=
\sum_{A\subseteq\{0,1,2\},\,|A|=|\lambda|,\,pA=A}
(-1)^{\sum_{i\notin A}f_i}
\chi^\lambda_{S_{|A|}}(p|_A)
\chi^\mu_{S_{3-|A|}}(p|_{A^c}).
\]
For sizes at most three, the required Specht character values are obtained directly from trivial, sign, and standard representations of \(S_2,S_3\). The checker constructs these ten irreducible characters without importing a table, then evaluates each inner product
\[
m_{\lambda,\mu}=\frac1{48}\sum_{g\in G}\chi(g)\chi_{\lambda,\mu}(g).
\]
All ten are the nonnegative integers in the multiplicity table. As an independent consistency condition, the sum of multiplicity times dimension is 675, exactly the top-homology rank. Since these are all the irreducible rational characters of the signed-permutation group of rank three, the resulting decomposition is exhaustive.

**4. Determine the quotient.** The central inversion has signed cycle type \((\varnothing,(1,1,1))\), hence trace \(-25\). The projections \((1\pm z)/2\) give dimensions \((675-25)/2=325\) and \((675+25)/2=350\). Averaging the class character over all 48 group elements gives \(11\) invariant fourth-homology classes. For a finite group acting simplicially, barycentric subdivision and rational transfer identify the orbit space's rational cohomology with the invariant subring of the original cohomology. Thus \(|X|/G\) has eleven classes in degree four and none in other positive degrees. Since degree-eight cohomology vanishes, all positive-degree products vanish, proving the stated ring.

## Verification
The standalone file `verify_octahedral_morse_character.py` requires only the Python 3 standard library. Running `python3 verify_octahedral_morse_character.py` prints the complete ten-class character and ten irreducible multiplicities, together with face enumeration, the Morse matching, group size, antipodal dimensions, and fixed-subspace dimension. `verification_output.txt` is the exact expected output. Two independent enumeration methods agree for all 6125 faces, including the empty face, and the complete acyclicity check operates on every one of the 25176 nonempty-face incidences. Irreducible multiplicities are obtained from group-character inner products and checked for integrality and total dimension; no approximate numerical linear algebra is used.

## Relationship to prior work
Chari and Joswig established the discrete Morse-complex construction and its connection to directed forests [1]. Crucially, Jojić [2, Theorem 3.2] already determines the homotopy type of directed-tree complexes of complete multipartite graphs. Reversing every edge arrow gives the present complex, and applying that theorem to \(K_{2,2,2}\) yields **exactly** the previously known 675-sphere wedge. The independently published octahedral graph Morse-complex calculation [5] provides the same nonequivariant homotopy type. These stronger earlier conclusions settle ordinary homology and are not restated as new results.

The precise gap addressed here is that the number and dimension of the spheres, even together with shellability, do not determine the ten conjugacy-class traces, the ten multiplicities, the central eigenspaces, or the orbit-space fixed classes. The inspected full texts of [1], [2], [3], and [4] do not supply these explicit \(C_2\wr S_3\) homology invariants for this graph. The published result [5] reports nonequivariant data only. A different result about the octahedral **edge-matching** complex, and a result about the \(K_{3,3}\) discrete Morse complex, concern distinct simplicial complexes. These comparisons concern mathematical implication, not just title matching.

## Limitations
The result is confined to the rational representation of this single octahedral-graph Morse complex. It does not determine the integral module lattice, torsion in orbit-space integral cohomology, an equivariant homotopy type, or a complete multipartite-family representation formula. Literature coverage is limited to the cited inspectable sources and searches: an unindexed same-graph symmetry calculation could affect publication priority. The exact proof and finite verification do not constitute an independent external mathematical audit.

## References
1. Manoj K. Chari and Michael Joswig, *Discrete Morse Complexes*, arXiv:math/0011234 (first publicly posted 2000-11-28).
2. Duško Jojić, *Complexes of directed trees of complete multipartite graphs*, Publications de l'Institut Mathématique 92(106) (2012), 43–51, DOI:10.2298/PIM1206043J, especially Theorem 3.2.
3. Connor Donovan, Maxwell Lin, and Nicholas A. Scoville, *On the homotopy and strong homotopy type of complexes of discrete Morse functions*, arXiv:1909.11440 (first posted 2019-09-25).
4. Connor Donovan and Nicholas A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780 (first posted 2022-07-27).
5. *The octahedral graph Morse complex is a wedge of 675 four-spheres*, public research record, `https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-octahedral-graph-morse-complex-is-a-wedge-of-675-four-sphere--5d292e60a1a7`.
