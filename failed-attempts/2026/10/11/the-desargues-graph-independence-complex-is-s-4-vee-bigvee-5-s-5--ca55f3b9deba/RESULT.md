# The Desargues graph independence complex is \(S^{4}\vee\bigvee^{5}S^{5}\)

## Finding

Let \(D\) be the twenty-vertex Desargues graph, equivalently the generalized Petersen graph \(GP(10,3)\), the bipartite Kneser graph \(H(5,2)\), or the point-line incidence graph of the Desargues configuration. Its ordinary independence complex satisfies the integral homotopy equivalence

\[
\operatorname{Ind}(D)\simeq S^{4}\vee\bigvee^{5}S^{5}.
\]

Thus \(\widetilde H_4(\operatorname{Ind}(D);\mathbb Z)\cong\mathbb Z\), \(\widetilde H_5(\operatorname{Ind}(D);\mathbb Z)\cong\mathbb Z^{5}\), and every other reduced integral homology group vanishes. In particular, the entire homotopy type is determined despite the simplicial complex having dimension nine.

## Assumptions and scope

Use the vertex set \(\{u_i,v_i:0\le i<10\}\), with indices modulo \(10\), and exactly the thirty undirected edges

\[
\{u_i,u_{i+1}\},\quad \{u_i,v_i\},\quad \{v_i,v_{i+3}\}\qquad(0\le i<10).
\]

Label \(u_i\) by the integer \(i\) and \(v_i\) by \(10+i\). A face is any subset of these twenty labels containing no edge. The empty face is included in the augmented enumeration but excluded from the ordinary discrete-Morse face poset. Orient each nonempty simplex by increasing label order. All homotopy equivalences in the claim are ordinary, non-equivariant, unpointed homotopy equivalences. There is no assertion about other generalized Petersen graphs or about the *matching* complex of \(D\).

## Proof

**Exhaustive face construction.** Traverse independent subsets in increasing-label order: when a vertex is selected, delete that vertex and its neighbors from the remaining extension set. This produces each independent subset exactly once. For cardinalities \(0,1,\ldots,10\), the respective counts are

```
1, 20, 160, 660, 1510, 1924, 1320, 480, 115, 20, 2
```

There are \(6212\) faces including the empty face and \(6211\) nonempty faces, with Euler characteristic \(-3\).

**Explicit matching and acyclicity.** On the augmented face poset, process labels in the following fixed order:

```
9, 2, 5, 17, 19, 3, 18, 6, 10, 11, 12, 4, 8, 16, 1, 15, 7, 13, 14, 0
```

At each stage with label \(w\), match every currently unmatched face \(\sigma\) omitting \(w\) to \(\sigma\cup\{w\}\), provided the latter is also currently unmatched, and remove both faces from later stages. The certificate checks all \(3103\) resulting pairs are disjoint. The six unmatched augmented faces, encoded as vertex-set bit masks, are

```
0x3891, 0x7141, 0x18512, 0x1c089, 0x80c48, 0x8e082
```

They consist of one face of dimension four (mask `0x80c48`) and five faces of dimension five. For each covering incidence of two faces, orient its arrow upward if matched and downward otherwise. The verifier constructs every one of the \(30380\) directed covering incidences among the \(6212\) augmented faces and removes all vertices in a topological sort. This establishes acyclicity, not merely the absence of short cycles. The empty face is matched to one vertex; on deleting the empty face from the ordinary complex, that vertex becomes the unique critical zero-cell. Hence Forman's theorem yields a CW model with exactly one zero-cell, one four-cell, and five five-cells, with no other cells.

**Integral attaching maps.** If \(\tau\) is a simplex and \(i\) is one of its vertices, use its signed boundary coefficient

\[
[\tau:\tau\setminus\{i\}]=(-1)^{\#\{j\in\tau:j<i\}}.
\]

For a matched pair of a four-face \(\sigma\) and a five-face \(\tau\), eliminate \(\sigma\) from the cellular boundary using the unit coefficient \([\tau:\sigma]\in\{\pm1\}\). Recursively following all such replacements to the sole critical four-face gives the integral Morse differential from the five critical five-faces to the critical four-face. In the order listed above it is the row vector

\[
\partial^{\mathrm{Morse}}_5=(0,0,0,0,0).
\]

The third and fourth entries each have two nonzero signed path contributions \(-1+1\); the other entries vanish termwise. The complete signed recursion and all critical masks appear in `verification/verify_integral_morse.py`, which checks these statements from the graph definition rather than trusting stored ranks or external logs.

The Morse four-skeleton is \(S^{4}\): the sole four-cell has only the zero-cell as its attaching target. Each five-cell is consequently attached by an element of \(\pi_4(S^{4})\cong\mathbb Z\), classified precisely by its integral degree. The five degrees are zero, so all attaching maps are nullhomotopic. It follows that the Morse CW complex, and hence \(\operatorname{Ind}(D)\), has the claimed wedge homotopy type.

## Verification

Run with Python 3 and no third-party dependencies:

```
python3 verification/verify_integral_morse.py
python3 verification/verify_independent_homology.py
```

The first program exhaustively enumerates the augmented face poset; verifies its face-count vector, all \(3103\) pairs, six critical faces and \(30380\) cover arrows; performs a complete acyclicity check; and evaluates all five *signed integer* Morse attaching degrees. It prints `DESARGUES_INTEGRAL_MORSE_OK` on success.

The second program independently builds the isomorphic bipartite Kneser graph \(H(5,2)\), validates an explicit vertex bijection from the generalized Petersen presentation, computes the independence polynomial by deletion recursion, and reconstructs every binary simplicial boundary rank. For dimensions \(0\) through \(9\), those ranks, with the augmented degree-zero-to-empty boundary included, are

```
1, 19, 141, 519, 991, 932, 383, 97, 18, 2
```

The resulting reduced mod-two Betti numbers are one in degree four and five in degree five, and zero elsewhere. It prints `DESARGUES_H52_HOMOLOGY_OK` on success. This second check alone does not establish the integral wedge result; the signed matching proof supplies the stronger conclusion.

## Relationship to prior work

Barmak's star-cluster theorem [1, Theorem 3.4] implies a suspension homotopy type for independence complexes of triangle-free graphs; it does not determine this particular mixed-dimensional wedge. Tsukuda's incidence-graph reduction [2, Corollary 5.3] also supplies a suspension description but no numerical homotopy classification for the Desargues configuration.

The bipartite Kneser graph \(H(5,2)\) is *exactly this graph*, not merely a nearby family member. Kumar, Singh, and Verma [3, Example 3.7, Theorem 3.6] calculate graded Betti numbers in the **linear strand of its edge ideal**. These syzygy invariants do not equal, and do not determine, the integral homotopy type of the whole independence complex. Nilakantan and Shukla's bipartite circulant family [4] has four-cycles in its three-regular cases with sufficiently many vertices; the Desargues graph has girth six and is not covered by those homotopy formulas.

A distinct computation concerns the ordinary **matching complex** of the Desargues graph. That is the independence complex of the *line graph*, with graph edges rather than graph vertices as the simplex vertices, and its result does not imply the present statement. Results about the dodecahedral graph \(GP(10,2)\), while closely named, concern a nonisomorphic graph and likewise do not settle the claim. Graph identity and aliases are recorded in [5].

## Limitations

The theorem concerns only the indicated twenty-vertex graph and the ordinary independence complex; no parameter-family theorem or equivariant decomposition is asserted. Exhaustive finite computation proves the stated finite case because all faces, directed incidences, and required signed attaching degrees are actually checked; experiments on a sample of faces would not suffice. A compatible calculation may exist in unindexed or unpublished literature, and bibliographic searches cannot establish absolute novelty. The verification programs and proof have not received independent scientific audit.

## References

1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1 (first public July 2, 2010), Theorem 3.4. https://arxiv.org/abs/1007.0418
2. S. Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics **12** (2017), 28–46, especially Corollary 5.3. https://cdm.ucalgary.ca/article/download/62277/46773/178118
3. A. Kumar, P. Singh, R. Verma, *Certain homological invariants of bipartite Kneser graphs*, arXiv:2105.06144v1 (2021), Theorem 3.6, Example 3.7. https://arxiv.org/abs/2105.06144
4. N. Nilakantan and S. Shukla, *Homotopy type of independence complexes of a family of regular bipartite graphs*, arXiv:1709.04789v1 (2017), Theorem 1.2. https://arxiv.org/abs/1709.04789
5. E. W. Weisstein, *Desargues Graph*, MathWorld, https://mathworld.wolfram.com/DesarguesGraph.html
