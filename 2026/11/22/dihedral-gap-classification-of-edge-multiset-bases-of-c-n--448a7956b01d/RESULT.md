# Dihedral gap classification of edge-multiset bases of \(C_n\)

## Finding
Let \(C_n\) be the simple, unweighted cycle whose vertices are \(\mathbb Z/n\mathbb Z\), with \(n\ge7\). Let \(S\) be any three-element vertex subset, and let \((a,b,c)\) be its three positive clockwise gaps, so \(a+b+c=n\). A gap is the number of cycle edges between successive selected vertices, not the number of unselected vertices.

**Theorem.** The edge-distance multisets of all \(n\) cycle edges relative to \(S\) are pairwise distinct if and only if

1. \(a,b,c\) are pairwise distinct, and
2. it is **not** the case that \(n\equiv2\pmod4\) and one of \(a,b,c\) equals \(n/2\).

Every such triple is a minimum edge-multiset resolving set (an edge-multiset basis), since the established edge-multiset dimension of \(C_n\) is three for \(n\ge7\) [1, Theorem 12; 2, Theorem 6.4]. Thus this is a complete classification of all minimum sets, not only a construction of one set.

Writing \(B_n\) for the number of *labelled* bases (vertex subsets, with no ordering of landmarks), define

\[
U_n=\binom{n-1}{2}-3\left\lfloor\frac{n-1}{2}\right\rfloor+2\mathbf 1_{3\mid n}.
\]

Then

\[
\boxed{ B_n=\frac n3\left(U_n-\mathbf1_{n\equiv2\pmod4}\,3\left(\frac n2-1\right)\right). }
\]

Every basis has trivial stabilizer under the dihedral automorphism group of the cycle, so every orbit contains exactly \(2n\) labelled bases and there are exactly \(B_n/(2n)\) dihedral orbits.

| \(n\) | Labelled bases \(B_n\) | Dihedral orbits |
|---:|---:|---:|
| 7 | 14 | 1 |
| 8 | 32 | 2 |
| 9 | 54 | 3 |
| 10 | 40 | 2 |
| 11 | 110 | 5 |
| 12 | 168 | 7 |
| 13 | 208 | 8 |
| 14 | 196 | 7 |

The contrast between \(n\equiv0\pmod4\) and \(n\equiv2\pmod4\) is genuine: the former permits a distinct-gap triple containing an antipodal pair, while the latter does not.

## Assumptions and scope
The graph is the undirected, simple, unweighted cycle, with no repeated landmark vertex. If \(e_i=\{i,i+1\}\), the distance from vertex \(s\) to that edge is

\[
d(s,e_i)=\min\{d_{C_n}(s,i),d_{C_n}(s,i+1)\}.
\]

The *edge-multiset code* is \(M_S(e_i)=\{\!\{d(s,e_i):s\in S\}\!\}\), including multiplicities and forgetting the assignment of distances to landmarks. A set resolves when \(M_S(e_i)\ne M_S(e_j)\) for every pair of distinct edges. The graph order is any integer \(n\ge7\); the theorem is not an asymptotic or finite-experiment assertion.

## Proof
**1. A cycle-isometry matching lemma.** Put an edge centre at \(i+1/2\) on the circumference \(\mathbb R/n\mathbb Z\), and denote its shortest circular arc-length distance to a vertex \(s\) by \(\delta(i+1/2,s)\). Since edges have unit length,

\[
d(s,e_i)=\delta(i+1/2,s)-1/2.
\]

For distinct edges \(e_i,e_j\), set \(h=j-i\not\equiv0\pmod n\) and \(q=i+j+1\pmod n\). Equality \(d(s,e_i)=d(t,e_j)\) holds exactly when

\[
t\equiv s+h\pmod n\qquad\text{or}\qquad t\equiv q-s\pmod n.
\]

Indeed these are respectively the rotation carrying one edge centre to the other and the reflection carrying one centre to the other, and they exhaust the two points at a prescribed circular distance from a centre (allowing the two possibilities to coincide).

If the two edge codes agree for a three-element set \(S\), multiset matching gives a bijection \(\sigma:S\to S\) for which, at each \(s\in S\), either the rotation \(T(s)=s+h\) or reflection \(R(s)=q-s\) produces \(\sigma(s)\).

**2. Necessity.** The permutation \(\sigma\) cannot be the identity: because \(h\not\equiv0\), each fixed landmark would satisfy \(2s\equiv q\pmod n\), an equation with at most two solutions in \(\mathbb Z/n\mathbb Z\).

If \(\sigma\) is a transposition swapping \(u,v\) and fixing \(w\), then \(2w\equiv q\pmod n\). If either swapped point uses the reflection, then \(u+v\equiv q\equiv2w\pmod n\), so the triple is symmetric about \(w\) and has two equal clockwise gaps. Otherwise both swapped points use \(T\); hence \(T(u)=v\), \(T(v)=u\) and \(2h\equiv0\pmod n\). Thus \(n\) is even, \(h=n/2\), and \(u,v\) are antipodal. The fixed-point congruence becomes \(2w\equiv2i+n/2+1\pmod n\). Its right side must be even, so \(n/2\) is odd, equivalently \(n\equiv2\pmod4\).

If \(\sigma\) is a three-cycle, there cannot be two reflection steps in its cyclic mapping, because two consecutive applications of the involution \(R\) would return to the starting vertex rather than reach the third distinct vertex. If there is one reflection step, the two consecutive translation steps show that the three vertices are an arithmetic progression modulo \(n\). Such a triple has two equal clockwise gaps (inspect the cases where the translation distance is respectively below or above \(n/2\)). If there are no reflection steps, \(T\) cyclically permutes the three points; they are equally spaced and again have repeated gaps. Hence any collision forces one of the two stated obstructions.

**3. Sufficiency of the obstructions.** If two gaps are equal, the three landmarks are preserved as a set by a reflection \(R(x)=2w-x\) around the remaining landmark \(w\). This reflection permutes the cycle edges and takes at least one edge to a distinct edge. Those two edges have equal edge-distance multisets because the reflection permutes the landmarks.

Now suppose \(n=2h\) with \(h\) odd and the landmark set contains antipodal vertices \(u,v=u+h\) and a third vertex \(w\). Choose an edge \(e_i\) solving \(2i\equiv2w-h-1\pmod{2h}\), possible since the right side is even. Put \(j=i+h\). In matching the distances from \(e_i\) to those from \(e_j\), the rotation \(T(s)=s+h\) swaps \(u,v\), and the reflection \(R(s)=i+j+1-s\) fixes \(w\). The matching lemma therefore makes the two distinct edge codes equal. Both obstructions are sufficient.

**4. Enumeration and automorphisms.** Choosing a landmark as a designated start and recording its ordered clockwise gap triple produces exactly three records for each three-element landmark set. There are \(\binom{n-1}{2}\) positive ordered triples summing to \(n\). For a chosen pair of equal gaps there are \(\lfloor(n-1)/2\rfloor\) possibilities; inclusion-exclusion for the three equal-pair events adds back twice the all-equal triple when \(3\mid n\). Thus \(U_n\) counts ordered triples with pairwise distinct gaps.

When \(n\equiv2\pmod4\), write \(h=n/2\), which is odd. Ordered triples containing a gap \(h\) are obtained by choosing its position (three choices) and choosing a positive ordered pair summing to \(h\) (\(h-1\) choices). The other two gaps are automatically unequal because \(h\) is odd, so precisely \(3(h-1)\) admissible gap triples must be removed. Multiplying by \(n/3\) gives the displayed formula. Finally, pairwise distinct clockwise gaps prohibit any nonidentity rotation or reflection from stabilizing the landmark set; the dihedral orbit-stabilizer theorem gives orbit size \(2n\) and the stated orbit count. \(\square\)

## Verification
The standalone Python 3 checker `verify_cycle_edge_multiset.py` constructs each cycle as an adjacency-list graph, obtains all distances by breadth-first search, computes every edge-distance multiset, and checks every vertex triple against the structural criterion and counting formula for each \(3\le n\le28\). It also checks orbit divisibility for \(n\ge7\). The program prints `EDGE_MULTISET_CYCLE_BASIS_VERIFY_OK 3<=n<=28` and a sample table; a captured output is supplied in `CHECK_OUTPUT.txt`. These finite tests corroborate but do not replace the all-order proof above.

## Relationship to prior work
Ikhlaq, Ismail, Siddiqui and Nadeem [1] introduced the edge-multiset dimension and proved \(\operatorname{edim}_{m}(C_n)=3\) for \(n\ge7\), supplying the particular triple \(\{0,1,3\}\). Their stated result determines the minimum cardinality, not the structure and number of **every** minimum triple or the parity-dependent antipodal obstruction. Farhan, Klavžar, Kuziak and Yero [2, Section 6.1] survey this same scalar value without a basis enumeration. The present classification is an exact refinement rather than a new proof of the scalar dimension.

Classical cycle multiset vertex-resolution, ordinary edge metric dimension, and edge-general-position configurations distinguish different objects or retain different information; no implication from their scalar values determines this basis census. The proof does explicitly account for possible edge/vertex midpoint dualities through the rotation/reflection matching lemma. A bounded literature and mathematical-record comparison did not identify a covering theorem, but does not establish exhaustive historical priority.

## Limitations
This theorem classifies minimum **three-vertex** edge-multiset resolving sets only. It makes no claim about four-vertex or larger sets, which cannot be inferred by adding vertices because multiset resolution need not be monotone under additions. The complete classification and formula are mathematical claims supported by the proof, while exhaustive publication priority and independent scholarly validation remain unperformed.

## References
[1] H. M. Ikhlaq, R. Ismail, H. M. A. Siddiqui, M. F. Nadeem, “A New Technique to Uniquely Identify the Edges of a Graph,” *Symmetry* **15** (2023), 762, published 20 March 2023, https://doi.org/10.3390/sym15030762. See Section 4.6, Theorem 12.

[2] M. Farhan, S. Klavžar, D. Kuziak, I. G. Yero, “Multiset resolvability parameters in graphs: A survey with new results and open problems,” arXiv:2607.10311 (2026), https://arxiv.org/abs/2607.10311. See Section 6.1, Theorem 6.4.
