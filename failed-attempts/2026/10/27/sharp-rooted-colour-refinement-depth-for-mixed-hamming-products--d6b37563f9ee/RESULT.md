# Sharp rooted colour-refinement depth for mixed Hamming products

## Finding

Let \(k\ge 1\), let integers \(q_1,\ldots,q_k\ge 2\), and set
\[
G=K_{q_1}\square\cdots\square K_{q_k}.
\]
Choose any root \(o\). Give \(o\) one initial colour and all remaining vertices another. Perform *synchronous counting colour refinement*: in round \(t+1\), the colour of a vertex is the pair consisting of its round-\(t\) colour and the multiset of its neighbours' round-\(t\) colours. Count round zero as the initial partition; stabilization means that the partition stops splitting.

**Theorem.** The least stabilization round is exactly
\[
\tau(G,o)=\begin{cases}
k-1,&q_1=\cdots=q_k,\\
k,&\text{at least two distinct alphabet sizes occur}.
\end{cases}
\]
At that round, the colours coincide exactly with the orbits of automorphisms fixing \(o\).

For each distinct size \(q\), let \(m_q\) be the number of coordinates of that size, and let \(j_q\in\{0,\ldots,m_q\}\) count the coordinates in which a vertex differs from \(o\). The stable classes are exactly the profiles \((j_q)_q\), so their number and sizes are, respectively,
\[
\prod_q(m_q+1),\qquad
\prod_q\binom{m_q}{j_q}(q-1)^{j_q}.
\]
The orbit-profile enumeration itself is established in earlier Cartesian-product literature; the asserted new contribution is that ordinary *rooted* colour refinement reaches that partition in the **sharp, alphabet-size-independent number of rounds** above, including every mixed product of dimension at least three.

## Assumptions and scope

All graphs are finite, simple and unweighted. Each factor has at least two vertices. The root is *the only* individualized vertex; colours of all other vertices initially coincide. A round counts one simultaneous refinement update, not a sequential split. Stabilization refers to a partition, not to numeric labels used to encode colours. Coordinates of equal size are interchangeable; alphabet symbols themselves have no intrinsic labels beyond the named root symbol.

## Proof

Write \(d(v)\) for the graph distance of \(v\) from \(o\). This is the number of non-root coordinates of \(v\); its maximum is \(k\). Write \(\mathbf j(v)=(j_q(v))_q\) for the profile and \(|\mathbf j|=\sum_qj_q=d(v)\). Every vertex has the same degree \(\Delta=\sum_i(q_i-1)\). From a vertex at distance \(h\), exactly \(h\) neighbours have distance \(h-1\): each is obtained by resetting one non-root coordinate to the corresponding root symbol. All remaining neighbours have distance \(h\) or \(h+1\).

**Frontier lemma.** At round \(t\), provided those distance layers exist, all vertices with \(d(v)=t\) have one common colour, and all vertices with \(d(v)\ge t+1\) have another common colour. The two colours are distinct. Moreover, all distance layers \(0,\ldots,t\) are mutually colour-distinguished from one another and from the remaining layers.

At round zero the root is a singleton colour and all positive-distance vertices share the other colour. Inductively, at round \(t-1\), the vertices at distance \(t-1\) share a colour different from the one shared by all vertices at distance at least \(t\). Each vertex at distance \(t\) has exactly \(t\) neighbours of the former colour and \(\Delta-t\) of the latter. Each vertex at distance at least \(t+1\) has zero neighbours of the former colour and all \(\Delta\) neighbours of the latter. Their old colours agree, hence the new two colours are distinct and constant on the specified sets. Previously separated distance layers cannot merge because the old colour is part of the refinement key. This proves the lemma for every applicable round.

**First nontrivial profile step.** If \(k\ge2\), the frontier lemma separates the root, distance one, and distances at least two at round one. For a distance-one vertex whose unique changed coordinate has alphabet size \(q\), the number of neighbours *also at distance one* equals \(q-2\). Thus, at round two, the colours of distance-one vertices distinguish exactly their sizes \(q\), hence their entire profiles.

**Induction on distance.** Suppose \(2\le h\le k-1\) and profiles at distance \(h-1\) are already distinguished by round \(h\). The frontier lemma ensures that round-\(h\) colours also distinguish the distance-\(h-1\) layer from every other distance layer. For a distance-\(h\) vertex with profile \(\mathbf j\), the multiset of profiles of its \(h\) neighbours in the previous layer contains \(j_q\) copies of \(\mathbf j-\mathbf e_q\) for each size \(q\). Summing these \(h\) profile vectors gives
\[
\sum_q j_q(\mathbf j-\mathbf e_q)=(h-1)\mathbf j.
\]
Since \(h-1>0\), this multiset uniquely recovers \(\mathbf j\). The round-\((h+1)\) neighbourhood-colour multiset therefore distinguishes all profiles at distance \(h\). Induction begins at \(h=2\) by the preceding paragraph. The top layer \(h=k\) has the unique profile \(j_q=m_q\) for every \(q\). Consequently all profiles are separated by round \(k\) (and by round zero if \(k=1\)).

Conversely, permutations of equal-sized coordinates and independent permutations of non-root symbols within each coordinate are root-preserving automorphisms and act transitively on the vertices of any one profile. Colour refinement is automorphism-invariant, hence it can never split a profile. The partition at round \(k\) is therefore exactly the profile/orbit partition and is stable. The number and size formulas follow by choosing, independently for each \(q\), exactly \(j_q\) of the \(m_q\) coordinates to differ, then choosing one of \(q-1\) symbols in each.

**Sharpness.** If all alphabet sizes are equal, profiles are just distances. The frontier lemma implies distance layers \(0,\ldots,k\) are separated by round \(k-1\), and for \(k\ge2\) the distinct layers \(k-1\) and \(k\) are still merged at round \(k-2\). Thus the least round is exactly \(k-1\), also valid for \(k=1\), where the initial root-versus-nonroot partition is already stable. If at least two alphabet sizes occur, then \(k\ge2\); at distance \(k-1\), vertices omitting a coordinate from different size groups have different profiles. The frontier lemma says all vertices in that layer have a common colour at round \(k-1\), whereas their profiles are separated at round \(k\). Thus the least stabilization round is exactly \(k\). This completes the proof.

## Verification

The included standard-library Python checker directly constructs Cartesian-product graphs, runs actual synchronous multiset refinement, compares the final partition pairwise with the predicted profile partition, and checks the **exact** first stabilization round. It covers 242 full-graph configurations with dimensions up to five and alphabet sizes two through six (subject to a finite vertex cutoff), plus seven higher-dimensional weighted equitable-quotient configurations, including products of ten and twelve factors. Run:

```sh
python verify_mixed_hamming.py
```

Expected final line: `ALL_TESTS_PASS`. The recorded output is in `verification_output.txt`. The verification is finite corroboration, not a replacement for the proof for arbitrary parameters.

## Relationship to prior work

Klavžar (2005) treats structural characterizations of Hamming graphs, understood as Cartesian products of complete graphs. Arvind, Köbler, Rattan and Verbitsky (2015), particularly their definition of refinable coloured graphs and exact counting-colour-refinement update, provide general finite-model-theoretic context but do not state the mixed-product round dichotomy.

Lu (2026), Proposition 7.1, gives a more general Cartesian-product root-stabilizer orbit formula, which already implies the profile *numbers*. Its Theorem 4.5 discusses the punctured adjacency–degree module for two distinct clique factors, and exhibits families where this linear module is smaller than the full orbit module. It does **not** assert that ordinary iterative counting colour refinement nevertheless reaches every orbit or determine its sharp round count. For example, its own \(K_2^{\square6}\square K_3^{\square4}\) case has a one-dimensional linear-module deficit; the theorem above shows that the rooted refinement partition is nevertheless orbit-exact after precisely ten rounds. Orbit enumeration or a linear-module rank formula alone does not imply the claimed refinement depth.

Previously recorded exact refinement statements for two-factor rook graphs and uniform-alphabet Hamming powers are also narrower than the mixed, arbitrarily many-factor assertion. The present claim does not present their special cases or the older orbit formula as independently new.

## Limitations

The theorem is only for one root initially individualized and all other vertices initially equal; it does not address additional marked vertices, arbitrary factor graphs, edge colours, or graph identification against arbitrary nonisomorphic inputs. Rounds are synchronous and use neighbour multiplicities. No claim is made about non-counting refinement, higher-dimensional Weisfeiler–Leman, canonical labeling, or complexity of arbitrary graphs. The checked sources and available prior records cannot rule out every unindexed or inaccessible equivalent formulation. Independent validation has not been performed.

## References

1. S. Klavžar, “Characterizing subgraphs of Hamming graphs,” *Journal of Graph Theory* 49 (2005), 302–312, doi:10.1002/jgt.20084. First online 2005-04-08, according to publisher metadata. https://doi.org/10.1002/jgt.20084
2. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, “Graph Isomorphism, Color Refinement, and Compactness,” arXiv:1502.01255v3 (2015), first public version 2015-02-04. https://arxiv.org/html/1502.01255v3
3. Z. Lu, “Punctured adjacency–degree algebras of Cartesian products,” arXiv:2609.06747v1 (2026), Proposition 7.1 and Theorem 4.5. https://arxiv.org/abs/2609.06747
