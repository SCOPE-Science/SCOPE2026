# The first non-real-rooted random greedy matching laws on trees occur at thirteen vertices

## Finding

Let \(T\) be a finite simple unweighted tree. Repeatedly select an edge uniformly from those whose endpoints are still unmatched, add it to a matching, and delete its endpoints. Write \(M_T\) for the terminal matching size and \(P_T(z)=\mathbb E[z^{M_T}]\).

**Sharp classification.** Every tree on at most twelve vertices has a real-rooted polynomial \(P_T\). Among the \(1301\) unlabeled trees on thirteen vertices, exactly six have a non-real-rooted polynomial \(P_T\): four with a cubic nonzero factor and two with a quadratic nonzero factor. All other thirteen-vertex trees have real-rooted \(P_T\). Thus thirteen is the minimum order of a tree whose random greedy matching-size law is not real-rooted.

A particularly symmetric witness \(T_*\) consists of a central vertex joined to three hubs, each of which has both a pendant leaf and a path of length two ending in a leaf. Its exact law is

\[
P_{T_*}(z)=\frac{z^3}{11520}(180+1852z+5149z^2+4339z^3).
\]

The cubic factor has discriminant \(-12323232144\), hence has one real root and two nonreal conjugate roots. The nonreal-rootedness is **not** a failure of log-concavity: the four displayed positive coefficients are strictly log-concave.

## Assumptions and scope

All graphs are finite, undirected, simple and unweighted. The terminal matching is obtained by uniform selection **among currently feasible edges**, not by uniform sampling among all maximal matchings or all matchings. For the finite classification, graph order ranges over integers \(1\le n\le13\); real-rootedness includes any zero root created by the factor \(z^m\). Identical graph types under vertex relabeling count once. No assertion is made about all larger trees or weighted versions.

For the witness, use vertices \(\{0,1,\ldots,12\}\). For \(j\in\{0,1,2\}\), put \(h_j=1+4j\), and include the four edges \(\{0,h_j\}\), \(\{h_j,h_j+1\}\), \(\{h_j,h_j+2\}\), and \(\{h_j+2,h_j+3\}\). These twelve edges specify \(T_*\) completely.

## Proof

**Exact recursion.** For any finite graph \(G\), define \(P_G(z)=\mathbb E[z^{M_G}]\). When \(G\) has no edges, \(P_G(z)=1\). Otherwise the first chosen edge is uniform on \(E(G)\), and conditioning on it yields the exact identity

\[
P_G(z)=\frac{z}{|E(G)|}\sum_{uv\in E(G)}P_{G-\{u,v\}}(z).
\tag{1}
\]

The recursion terminates because two vertices disappear at each nontrivial step. It uses rational arithmetic throughout. Conditional distribution of the remaining process is exactly the same as a new greedy process on the remaining induced graph. This establishes the recursion, including normalization, for arbitrary finite graphs; in particular it applies to all forests arising during tree evaluation.

**Witness.** Applying (1) to the displayed twelve-edge tree gives, in increasing order of selected matching size, probabilities

\[
\Pr(M_{T_*}=3)=\frac{180}{11520},\quad
\Pr(M_{T_*}=4)=\frac{1852}{11520},\quad
\Pr(M_{T_*}=5)=\frac{5149}{11520},\quad
\Pr(M_{T_*}=6)=\frac{4339}{11520}.
\]

These four numerators sum to \(11520\). The discriminant of \(az^3+bz^2+cz+d\) is

\[
\Delta=b^2c^2-4ac^3-4b^3d-27a^2d^2+18abcd.
\]

Using \((a,b,c,d)=(4339,5149,1852,180)\) gives \(\Delta=-12323232144<0\). A real cubic with negative discriminant has exactly one real zero and two conjugate nonreal zeros. Multiplication by \(z^3\) cannot remove these zeros. This proves the thirteen-vertex failure.

**Exhaustive lower bound and exact count at thirteen.** The accompanying executable certificate enumerates the nonisomorphic unrooted trees of each order using the exhaustive `networkx.nonisomorphic_trees` generator. Its order-by-order counts are \(1,1,1,2,3,6,11,23,47,106,235,551,1301\). These agree with the classical unlabeled-tree count sequence and total \(2288\) tree types through order thirteen. For each generated tree the certificate evaluates (1) on every reachable induced vertex subset with exact rational coefficients. After factoring out the lowest power of \(z\), it verifies strictly positive contiguous coefficients and degree at most three; for degree two it evaluates the exact quadratic discriminant, and for degree three the exact cubic discriminant. Nonnegative discriminants are necessary and sufficient for all roots of these degree-at-most-three real polynomials to be real. All \(987\) trees through twelve vertices pass. Among the \(1301\) trees of order thirteen, exactly six have negative discriminant.

For reproducibility the six exceptional thirteen-vertex types, in graph6 notation without the optional header, are:

```
LpCPA?@?G?g??@
LpC`A?@?G?g??@
LpCa?C@?GAG??@
LpD?GC@O??_@?@
LpD?GCCO??_@?C
Lp`?GCCO??_@?C
```

The first three and last type have degree-three nonzero factors; the two types beginning with `LpD` have degree-two nonzero factors. The witness has the final graph6 type, and its explicit edge construction is independently checked for isomorphism with that encoding.

The finite conclusion relies on a complete isomorphism-class enumeration and exact discriminant signs, not a sampled collection or floating-point roots. The executable source and the complete expected counts are included with this report.

## Verification

Run `python -m pip install -r requirements.txt` followed by `python verify_greedy_matching_roots.py` using Python 3. The certificate checks every tree class of orders one through thirteen and asserts the complete exceptional-type list and witness polynomial. The verification completed successfully, with \(2288\) exact tree evaluations.

An independent integer-state calculation of the witness enumerates **all** \(12! = 479001600\) permutations of its twelve edges in aggregate, including rejected edges. It counts \(7484400\), \(77006160\), \(214095420\), and \(180415620\) permutations yielding matching sizes three, four, five, and six respectively. Dividing by \(12!\) reproduces the four probabilities above. This second recurrence processes *all* edges rather than choosing the first feasible edge at each stage.

## Relationship to prior work

The matching process here is the standard random feasible-edge greedy algorithm discussed in the matching-process literature; it can also be viewed as random-order greedy maximal independent set selection on the line graph. Krivelevich, Mészáros, Michaeli and Shikhelman analyze greedy independent sets through local limits and finite-tree expectations, but not the zero set of this terminal matching-size polynomial. Bal and Bennett analyze greedy matching on random graphs and hypergraphs using differential equations and limiting size, not this exact fixed-tree root classification.

The classical Heilmann–Lieb theorem says that the **ordinary matching enumerator**, which weights every matching of a given size equally, has only real nonpositive roots. It does not imply real-rootedness for \(P_T\), since greedy matching induces nonuniform, process-dependent weights on maximal matchings only. The example isolates a genuine distinction between these two measures. Earlier finite-graph greedy-matching analyses by Dyer and Frieze motivate the model but are not represented as having been completely checked for this zero-set question.

## Limitations

The threshold and count are exact but finite: no root classification is established beyond thirteen vertices. Non-real-rootedness by itself does not imply nonunimodality or failure of log-concavity. The result concerns unweighted edge-uniform choices, not vertex-first variants or independent edge fugacities. Historical-priority comparisons include fully accessible modern papers, but the complete original 1991 Dyer–Frieze article and the full 1989 Pippenger article were not accessible for a statement-by-statement inspection; independent priority verification is outstanding.

## References

1. M. Krivelevich, T. Mészáros, P. Michaeli, C. Shikhelman, *Greedy maximal independent sets via local limits*, arXiv:1907.07216 (first publicly posted July 16, 2019), https://arxiv.org/abs/1907.07216.
2. D. Bal, P. Bennett, *The Matching Process and Independent Process in Random Regular Graphs and Hypergraphs*, arXiv:1603.09232 (first posted March 30, 2016); *Electronic Journal of Combinatorics* 30 (2023), P1.11, https://doi.org/10.37236/10698.
3. M. Dyer, A. Frieze, *Randomized greedy matching*, *Random Structures & Algorithms* 2 (1991), 29–45, https://doi.org/10.1002/rsa.3240020104.
4. O. J. Heilmann, E. H. Lieb, *Theory of monomer-dimer systems*, *Communications in Mathematical Physics* 25 (1972), 190–232, https://doi.org/10.1007/BF01877590.
5. N. Pippenger, *Random Sequential Adsorption on Graphs*, *SIAM Journal on Discrete Mathematics* 2 (1989), 393–401, https://doi.org/10.1137/0402034.
6. NetworkX documentation, `nonisomorphic_trees`, https://networkx.org/documentation/stable/reference/generated/networkx.generators.nonisomorphic_trees.html.
