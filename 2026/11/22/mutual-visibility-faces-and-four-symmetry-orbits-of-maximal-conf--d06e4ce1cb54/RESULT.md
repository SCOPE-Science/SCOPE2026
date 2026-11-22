# Mutual-visibility faces and four symmetry orbits of maximal configurations in the Heawood graph

## Finding

Let \(H\) be the 14-vertex Heawood graph, represented as the incidence graph of the Fano projective plane. A mutual-visibility set \(S\) is a set of vertices such that for any two distinct \(u,v\in S\), at least one shortest \(u\)-\(v\) path has no internal vertex in \(S\).

All \(2^{14}\) subsets admit an exact classification by the point-line incidence test below. The complete size polynomial of mutual-visibility sets and the polynomial of inclusion-maximal mutual-visibility sets are, respectively,

\[
\mathcal V_H(z)=1+14z+91z^2+322z^3+651z^4+728z^5+392z^6+58z^7,
\]

\[
\mathcal F_H(z)=70z^6+58z^7.
\]

Therefore \(H\) has exactly \(2257\) mutual-visibility sets, including the empty set; exactly \(128\) inclusion-maximal ones; mutual-visibility number \(\mu(H)=7\); and lower mutual-visibility number \(\mu^-(H)=6\). The mutual-visibility simplicial complex is nonpure, with facets of exactly dimensions five and six.

The full automorphism group of \(H\), of order \(336\), acts on the \(128\) maximal sets in exactly four orbits. The pairs (set size, orbit size) are
\[
(6,28),\qquad(6,42),\qquad(7,2),\qquad(7,56).
\]

With vertex labels \(p_0,\ldots,p_6,\ell_0,\ldots,\ell_6\) as below, explicit representatives are:

| Set size | Orbit size | Representative |
| --- | ---: | --- |
| 6 | 28 | \(\{p_1,p_2,p_4,\ell_0,\ell_2,\ell_3\}\) |
| 6 | 42 | \(\{p_0,p_2,p_4,p_5,p_6,\ell_0\}\) |
| 7 | 2 | \(\{p_0,p_1,\ldots,p_6\}\) |
| 7 | 56 | \(\{p_0,p_4,p_5,p_6,\ell_0,\ell_1,\ell_2\}\) |

## Assumptions and scope

Vertices are seven points \(p_i\) and seven lines \(\ell_j\), with indices in \(\mathbb Z/7\mathbb Z\). The line \(\ell_j\) is incident with precisely the points \(p_j,p_{j+1},p_{j+3}\). Edges join incident point-line pairs. This is the simple, connected, cubic Fano-incidence Heawood graph, with graph diameter three. The graph, its labels, and the mutual-visibility convention are fixed throughout. Sets are **labelled vertex subsets**, not equivalence classes modulo symmetry. Inclusion-maximality is different from maximum cardinality.

## Proof

**1. A complete point-line geodesic criterion.** Write a candidate set as \(S=P\cup L\), with \(P\) a point subset and \(L\) a line subset, and let \(\ell(p,q)\) be the unique Fano line through distinct points \(p,q\). Let \(p(\ell,r)\) be the unique Fano point common to distinct lines \(\ell,r\). Then \(S\) is mutually visible **if and only if** all of the following hold:

1. For each two distinct selected points \(p,q\), their joining line \(\ell(p,q)\notin L\).
2. For each two distinct selected lines \(\ell,r\), their intersection point \(p(\ell,r)\notin P\).
3. For every selected nonincident point-line pair \((p,\ell)\), there is a line \(a\) through \(p\) such that \(a\notin L\) and the point \(p(a,\ell)\notin P\).

To prove necessity and sufficiency, note that point-point distances are two and have a **unique** shortest path through their joining line; line-line distances are two and have a **unique** shortest path through their common point. Incident point-line pairs are adjacent and need no check. A nonincident point-line pair has distance three, and its precisely three shortest paths have the form \(p-a-p(a,\ell)-\ell\), one for each of the three lines \(a\) through \(p\). One such path must have both internal vertices unselected. These are all possible pair types, proving equivalence with the given definition.

**2. Complete exact finite enumeration.** Encode each subset by a fourteen-bit integer \(m\) from \(0\) through \(2^{14}-1\); bits \(0,\ldots,6\) represent points and bits \(7,\ldots,13\) lines. For **every** such integer, evaluate the three conditions in step 1. Add one to the face coefficient indexed by its bit count if the conditions hold. For every admissible \(m\), test all missing bits \(i\); \(m\) is inclusion-maximal precisely when no single-bit extension \(m\cup\{i\}\) is admissible. This criterion is exact because the family is hereditary: any larger admissible superset would give an admissible one-bit extension. The resulting coefficient vectors (from sizes zero through seven) are
\[
(1,14,91,322,651,728,392,58),\qquad
(0,0,0,0,0,0,70,58).
\]
The executable `verify.py` supplies the entire terminating exhaustive implementation, with no pruning, search cutoffs, heuristic tests, or external data. The implementation independently rebuilds graph distances by breadth-first search, generates **all** shortest-path interior masks, and verifies the Fano incidence criterion against the graph-theoretic definition for **all** \(16384\) vertex subsets. In particular it asserts no admissible sets of size at least eight.

**3. Full symmetry and orbits.** A Fano line is a three-point set \(\{j,j+1,j+3\}\) modulo seven. Iterate over all \(7!\) point permutations and retain exactly those preserving the seven lines; there are precisely \(168\) such collineations, each inducing a part-preserving graph automorphism. The part-swapping involution \(p_i\mapsto\ell_{-i}\), \(\ell_j\mapsto p_{-j}\), sends incidence to incidence. Composing the \(168\) collineations with this polarity gives \(168\) additional automorphisms. Conversely every automorphism of the connected bipartite incidence graph either preserves the point/line parts, and is a collineation, or swaps them, after which polarity makes it part-preserving. Hence these \(336\) permutations constitute the entire graph automorphism group.

The script explicitly checks adjacency preservation for all \(336\) permutations and applies all of them to every facet, testing membership in the computed facet set. The four orbit sizes and representatives above are obtained by an exhaustive orbit partition, with total \(28+42+2+56=128\). This establishes the final assertion.

## Verification

From this file's directory, execute `python3 verify.py` using a standard Python installation. The program terminates after finite loops and asserts each critical equality. Successful execution prints `FANO_GEODESIC_CRITERION_OK`, the complete face and facet vectors, all four orbit counts and representatives, `AUTOMORPHISMS 336`, and `VERIFY_OK`. The calculation has been executed successfully from the packaged source. Each count is certified as **exhaustive over this fixed 14-vertex graph**, not extrapolated from sampling or from testing smaller instances.

## Relationship to prior work

Di Stefano's *Mutual Visibility in Graphs* (first public May 6, 2021) defines this shortest-path notion, establishes complexity and studies block graphs, trees, grids, tori, complete bipartite graphs, and cographs. Brešar and Yero's *Lower (total) mutual visibility in graphs* (first public July 6, 2023) defines the minimum size of an inclusion-maximal mutual-visibility set, the \(\mu^-\) parameter evaluated here. The 2023 *Variety of mutual-visibility problems in graphs* studies related, distinct outer/total/dual variants and grid-like graphs. Tonny and Shikhi's 2025 *On the visibility polynomial of graphs* provides the general size-enumerator terminology and algorithm, as well as examples for other graph families; a general exhaustive algorithm does not itself state the specific Heawood polynomial or symmetry-orbit classification. All four primary texts were read in their accessible full-text versions, and no Heawood enumeration or orbit result was found in them. Related indexed work on \(P_3\)-convexity of the Heawood graph and mutual visibility on other graphs does not imply these exact counts because it imposes different conditions or uses different graph families. This is a best-knowledge priority assessment, not a guarantee of uniqueness in all literature.

## Limitations

This is an exact theorem about one particular natural 14-vertex incidence graph, not a formula for the Levi graph of every projective plane. The proof involves a finite exhaustive certificate; its correctness depends on the plainly disclosed representation, definitions, loops, and executable checks. The face polynomial is not an independence polynomial or a general-position polynomial. Nothing here asserts publication priority over inaccessible, unindexed, or independently discovered work. The result has undergone self-review only; no independent mathematical audit has been performed.

## References

1. G. Di Stefano, *Mutual Visibility in Graphs*, arXiv:2105.02722, first public 2021-05-06. https://arxiv.org/abs/2105.02722
2. B. Brešar and I. G. Yero, *Lower (total) mutual visibility in graphs*, arXiv:2307.02951, first public 2023-07-06. https://arxiv.org/abs/2307.02951
3. S. Cicerone et al., *Variety of mutual-visibility problems in graphs*, arXiv:2304.00864, first public 2023-04-03. https://arxiv.org/abs/2304.00864
4. Tonny K B and Shikhi M, *On the visibility polynomial of graphs*, arXiv:2507.01851, 2025, subsequent background and comparison. https://arxiv.org/abs/2507.01851
5. E. W. Weisstein, *Mutual-Visibility Set*, MathWorld, terminology. https://mathworld.wolfram.com/Mutual-VisibilitySet.html
