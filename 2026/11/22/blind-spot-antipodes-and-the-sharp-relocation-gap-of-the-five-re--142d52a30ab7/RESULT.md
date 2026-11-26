# Blind-spot antipodes and the sharp relocation gap of the five-regular Clebsch graph

## Finding

Let \(G\) be the five-regular Clebsch graph, with sixteen vertices. A power-dominating placement \(S\) observes its closed neighborhood \(N_G[S]\) at the first stage, then repeatedly observes any vertex that is the unique unobserved neighbor of an observed vertex. On minimum placements, let \(R_J\) permit one unrestricted vertex replacement and let \(R_S\) require that the replaced and inserted vertices be adjacent in \(G\). The minimum placements are the 160 independent triples and 160 induced paths on three vertices, as shown in [2]. The operation \(U(S)=V(G)\setminus N_G[S]\) is the same type-switching involution on these triples as in [3].

The additional result concerns **one-token slides and their distances**. The slide graph \(R_S\) is connected with 1,120 edges. Independent triples have degree 9 and path triples have degree 5. Every placement has eccentricity six; its **only** placement at slide distance six is the blind-spot triple \(U(S)\), at jump distance three. Among the 51,040 unordered pairs of distinct minimum placements, the nonnegative gap \(d_{R_S}-d_{R_J}\) has counts \((12{,}560,27{,}520,10{,}800,160)\) for gaps \(0,1,2,3\) respectively, and the 160 gap-three pairs are exactly \(\{S,U(S)\}\).

## Assumptions and scope

Write vertices as integers \(0,\ldots,15\), with adjacency when their bitwise XOR is in \(C=\{1,2,4,8,15\}\). This is the folded five-cube, not the ten-regular complement. Vertices are labeled; sensors are unlabelled, and there is no quotient of the placement graphs. Both moves maintain minimum cardinality and power domination at every step; they do not move multiple sensors simultaneously.

## Proof

The minimum-placement family \(\mathcal M\) and the jump eccentricity three are taken from [2]; they can also be obtained by the finite check below. For symmetry reduction, the generators in \(C\) sum to zero and any four are independent. Translations and permutations of the generators therefore act on \(G\). For a path, translate its center to zero and permute its two neighbors. For an independent triple, translate one vertex to zero; the other two are sums of distinct pairs of generators, with their two index pairs intersecting (disjoint pairs would yield adjacent vertices). Index permutations are transitive on such intersecting pairs. Consequently the two types of \(\mathcal M\) are single orbits, represented by \(\{0,3,5\}\) and \(\{0,1,2\}\), respectively. Their blind spots are \(\{6,9,14\}\) and \(\{7,11,12\}\); the reverse neighborhood complement recovers the input in both cases. This is also the involution of [3], independently of the placement interpretation.

Construct move adjacency as follows. For every \(S\in\mathcal M\), for each \(v\in S\) and \(w\in V(G)\setminus S\), let \(T=(S\setminus\{v\})\cup\{w\}\). If \(T\in\mathcal M\), add \(T\) to the jump adjacency list, and also to the slide list if \(v\oplus w\in C\). The numbers of same-type and opposite-type slide neighbors are \((6,3)\) for \(\{0,3,5\}\) and \((2,3)\) for \(\{0,1,2\}\). By transitivity the total is \((160\cdot9+160\cdot5)/2=1120\) undirected edges.

For either adjacency list \(A\), use the exact recurrence
\[
L_0(S)=\{S\},\qquad
L_{j+1}(S)=\bigcup_{X\in L_j(S)}A(X)\setminus\bigcup_{i=0}^{j} L_i(S),
\]
where the difference is taken after forming the union of neighbors. Each \(L_j\) is exactly the set of placements at distance \(j\): induction follows by deleting all earlier layers from the neighbors of the current one. Iteration until the frontier is empty gives these complete slide layers:

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | Layer 6 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| \(\{0,3,5\}\) | 1 | 9 | 45 | 122 | 118 | 24 | 1 | \(\{6,9,14\}\) |
| \(\{0,1,2\}\) | 1 | 5 | 28 | 108 | 141 | 36 | 1 | \(\{7,11,12\}\) |

Each row covers all 320 placements. As \(U\) commutes with graph automorphisms, the last layer is \(\{U(S)\}\) for every \(S\). Because \(S\) and \(U(S)\) are disjoint, at least three jumps are necessary; exactly three suffice by the jump eccentricity from [2].

To compute the gap distribution, enumerate all triples with zero or two induced edges and sort their increasing vertex lists lexicographically. Apply the recurrence to each source in each adjacency list, and for each larger-index target increment the bin indexed by the slide-layer index minus the jump-layer index. The resulting counts, together with the marginal distance counts, are:

| Distance | Jump pairs | Slide pairs |
| ---: | ---: | ---: |
| 1 | 3,360 | 1,120 |
| 2 | 20,160 | 5,840 |
| 3 | 27,520 | 18,400 |
| 4 | 0 | 20,720 |
| 5 | 0 | 4,800 |
| 6 | 0 | 160 |

| Gap | Pair count |
| ---: | ---: |
| 0 | 12,560 |
| 1 | 27,520 |
| 2 | 10,800 |
| 3 | 160 |

The recurrence covers all \(\binom{320}{2}\) pairs, and the blind-spot involution contributes 160 distinct pairs of gap three, exhausting that bin. For example, a shortest slide path is
\[
\{0,1,2\}\to\{1,2,4\}\to\{2,4,9\}\to\{3,4,9\}\to\{3,4,11\}\to\{3,11,12\}\to\{7,11,12\}.
\]

## Verification

The unchanged standard-library scripts `check_cayley.py` and `check_setmodel.py` perform the finite checks. The first directly computes propagation from all 696 nonempty seeds of sizes at most three using XOR adjacency; the second uses the empty set, singleton and pair model and forms placement adjacency by pairwise comparison. Both form the full distance matrices and check the unique farthest placements and the gap counts. The explicit recurrence and fixed vertex/edge definitions also suffice to reproduce the computations separately.

## Relationship to prior work and limitations

The minimum-placement classification and jump graph are background, not distinct contributions: [2] also proves a criterion for successful placements of all sizes. Further, the type-switching antineighborhood involution on the very same family of triples is established in [3], in the interpretation of two-rainbow domination. The simultaneous movement of two colored copies in [3] is not the adjacency-restricted movement of a single sensor here; its reported graph has 1,440 edges and diameter five. The result compared here is the one-token slide metric and its exact relationship to the known involution and to jumping. Records [2] and [3] are in the same dated catalogue as this result; no ordering within that date is inferred. Reference [1] gives the general reconfiguration framework. The result is confined to this explicit finite graph; it does not establish a family theorem or claims about actual power-grid sensor movement. Unidentified equivalent work remains possible.

## References

1. B. Bjorkman et al., *Power domination reconfiguration*, [arXiv:2201.01798v1](https://arxiv.org/html/2201.01798v1), §5.1; journal version [doi:10.1007/s44007-025-00187-5](https://doi.org/10.1007/s44007-025-00187-5).
2. *Induced-triple criterion and three-step exchange mobility for Clebsch power domination*, [Resultary record 99315adae8ca](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-induced-triple-criterion-and-three-step-exchange-mobility-for-cl--99315adae8ca/RESULT.md), Finding and Proof.
3. *Antineighborhood involution and sharp two-token mobility of minimum rainbow placements on the Clebsch graph*, [Resultary record c9e2c260f397](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-antineighborhood-involution-and-sharp-two-token-mobility-of-mini--c9e2c260f397/RESULT.md), Finding and Proof §§2–3.
