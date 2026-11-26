# The three-flag fault census for the Fano incidence graph at Rips scale two

## Finding

Let \(H\) be the incidence graph of the Fano plane. Delete exactly three flags \(F\) and, if \(H-F\) is connected, form \(K_F=\operatorname{VR}_{\le2}(H-F)\) using the recomputed shortest-path metric. Then all reduced homology over \(\mathbb F_2\) vanishes except in degree two.

The degree-two rank is \(5\) unless the deleted flags form an induced matching in \(H\). For an induced matching, let \(a(F)\) indicate collinearity of the three point endpoints and \(b(F)\) indicate concurrency of the three line endpoints, in the original plane. Then the rank is \(5+a(F)+b(F)\). The 1330 triples give 14 disconnected graphs and 1316 connected cases; in the connected cases the ranks \(5,6,7\) occur \(1232,56,28\) times. The failure of the rank-five baseline occurs precisely on the 84 maximum induced matchings, including a two-class excess on the 28 with both endpoint conditions.

## Assumptions and scope

Points are \(0,\ldots,6\) and lines are \(L_j=\{j,j+1,j+3\}\) modulo seven. A flag is an incidence \((p,L_j)\), and an induced matching has six distinct endpoints with no cross-incidences other than the three selected flags. All fourteen vertices remain after deletion. Faces of \(K_F\) are the nonempty vertex sets with every pair at distance at most two. The claim is restricted to these triple deletions and to reduced homology over \(\mathbb F_2\).

## Proof

The seven cyclic triples form the Fano plane: each unordered pair of points occurs in exactly one triple (the six nonzero ordered differences in \(\{0,1,3\}\) are distinct modulo seven). The accompanying `verify.py` is a finite exhaustive calculation. Its triple-deletion loop enumerates each three-subset of the 21 flags exactly once and tests connectivity by graph traversal. For each connected case, breadth-first searches compute the surviving graph distances; the resulting distance-at-most-two adjacency is used to enumerate all cliques. The clique recursion adds vertices in increasing order and keeps precisely the later vertices adjacent to all chosen ones. Thus every clique occurs by its unique increasing sequence.

For each degree \(d\ge1\), columns of the simplicial boundary are represented by bitsets of their codimension-one faces. Successive cancellation by the highest nonzero bit gives a pivot basis, hence the exact rank over \(\mathbb F_2\). With augmentation rank one, the number of \(d\)-faces less the two adjacent boundary ranks is the reduced Betti number in every degree \(d\ge0\). Nonemptiness also gives vanishing in degree \(-1\).

The expected-rank test rejects repeated endpoints or any cross-incidence, then tests the selected point set against the seven lines and the selected line set against the seven point pencils. It checks the degree-two formula **separately at every connected triple**, not just on the final histogram, and asserts zero reduced ranks in all other degrees. The exact census gives \(14\) disconnected triples and the three stated connected counts. The separately classified 84 induced matchings are split into three classes of 28 with \((a,b)=(1,0),(0,1),(1,1)\), so no induced matching has zero excess. This proves the result.

## Verification

Run `python3 verify.py` and compare with `verification_output.txt`. The decisive data are the `deletions 3` histogram and the assertions for the other homological degrees and the endpoint predicate. The same script also checks the already covered cases of at most two flags as benchmarks. It uses only the Python standard library and exact arithmetic.

## Relationship to prior work

The [intact projective-plane classification](https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-scale-two-vietoris-rips-complexes-of-finite-projective-plane-inc--c3740b96b3c3) computes the undamaged rank. [Sharp arbitrary-incidence-fault stability of projective-plane Rips complexes](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-sharp-arbitrary-incidence-fault-stability-of-projective-plane-ri--3a3137e314b4) gives the stronger radius-two wedge-of-spheres result of rank \(q^3-t\) for every plane of order \(q\) under arbitrary \(t\le q\) flag deletions. It covers the Fano plane through two deletions, which are not claimed here as new, but its deletion budget does not cover any triple. The [Fano induced-matching exchange graph](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-the-fano-induced-matching-exchange-graph-tripartite-triangles-an--15f94095f8d3) already gives the 84 maximum matchings and their three geometric types. The contribution is their precise connection to homology changes beyond the uniform two-fault budget, not the matching classification itself.

The graph-power framework is treated by Adams and Coskunuzer ([arXiv:2103.06408](https://arxiv.org/abs/2103.06408)). Feng and Nukala ([arXiv:2302.14664](https://arxiv.org/abs/2302.14664)) treat scale two for specified subset-space metrics, not this deletion census.

## Limitations

No integral homology, homotopy type, persistence map or higher-order projective-plane census is asserted for the three-fault cases.
