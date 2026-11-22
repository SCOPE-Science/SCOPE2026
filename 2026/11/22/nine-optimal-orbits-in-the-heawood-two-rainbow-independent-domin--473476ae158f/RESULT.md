# Nine optimal orbits in the Heawood two-rainbow independent domination polynomial

## Finding

Let \(H\) be the fourteen-vertex Heawood graph, the incidence graph of the seven-point Fano plane. Write \(\mathcal R_H(t)=\sum_{k=0}^{14}r_k t^k\), where \(r_k\) counts functions \(f:V(H)\to\{0,1,2\}\) of weight \(k=|f^{-1}(\{1,2\})|\) such that each positive color class \(f^{-1}(1)\), \(f^{-1}(2)\) is independent and every zero-labeled vertex has a neighbor of each positive color. The colors \(1\) and \(2\) are named, so swapping them ordinarily gives a distinct function.

**Theorem.** The complete two-rainbow independent domination polynomial is
\[
\mathcal R_H(t)=868t^8+168t^9+42t^{10}+28t^{11}+2t^{14}.
\]
Thus \(\gamma_{\mathrm{ri}2}(H)=8\), exactly 868 minimum functions exist, and no feasible functions have weight \(12\) or \(13\). The 868 minima form exactly nine orbits under the full 336-element graph automorphism group, of sizes
\[
14,14,56,56,56,168,168,168,168.
\]
Among minima, the number having precisely \(j\) zero-labeled **point** vertices, for \(j=0,1,\ldots,6\), is respectively
\[
70,84,168,224,168,84,70.
\]
There are 1108 feasible labeled functions in total. An explicit representative of each optimum orbit is in `ORBIT_REPRESENTATIVES.tsv`.

## Assumptions and scope

All graphs are finite, simple, and undirected. Let the point vertices be \(p_0,\ldots,p_6\), and the line vertices \(\ell_0,\ldots,\ell_6\), indices modulo seven, with
\[
\ell_j=\{p_j,p_{j+1},p_{j+3}\}.
\]
The vertex order for each 14-digit representative word is \((p_0,\ldots,p_6,\ell_0,\ldots,\ell_6)\). An edge joins a point to an incident line. The theorem concerns **rainbow independent domination**, which requires each separate color class to be independent; it is not the differently defined independent rainbow domination with multi-color labels and globally independent positive support.

## Proof

**Component-coloring lemma.** For any bipartite graph \(G\) and any chosen zero set \(Z\subseteq V(G)\), let \(G-Z\) have nonempty connected components \(C_1,\ldots,C_c\). Every labeling with zero set exactly \(Z\) and with independent named positive classes restricts to a proper two-coloring on each \(C_i\). As \(C_i\) is connected and bipartite, it admits exactly two such colorings. Thus all possible positive colorings are indexed *bijectively* by \(\epsilon\in\{0,1\}^c\), independently flipping each component's bipartition colors. Such an assignment is feasible if and only if for each \(v\in Z\), its neighbors in \(G-Z\) include both named positive colors. There is no assumption that \(Z\) is independent. This condition is necessary and sufficient: it is exactly the uncolored-vertex requirement, while all positive-positive edges already join opposite colors.

Consequently, with \(m=|V(G)|\), the following exact finite identity holds (the product is over all vertices in \(Z\)):
\[
\mathcal R_G(t)=\sum_{Z\subseteq V(G)} t^{m-|Z|}
 \sum_{\epsilon\in\{0,1\}^{c(G-Z)}}
 \prod_{v\in Z}\mathbf 1\bigl[\{f_\epsilon(w):w\in N_G(v)\setminus Z\}=\{1,2\}\bigr].
\]
If \(G-Z\) is empty, it has zero components and one empty assignment, which fails all nontrivial zero-neighborhood conditions. Thus the formula includes every boundary case.

For \(H\), there are exactly \(2^{14}=16384\) zero sets. The standalone `component_enumerator.py` implements the identity without importing any graph library: it constructs all 21 incidences, performs connected-component breadth-first traversals for each zero set, loops through every component flip vector, tests all zero vertices, and accumulates the coefficients. The complete output is

| Positive weight | 8 | 9 | 10 | 11 | 14 |
|---|---:|---:|---:|---:|---:|
| Count | 868 | 168 | 42 | 28 | 2 |

It confirms zero counts at all other degrees, and among weight-eight assignments separately obtains the point-zero composition distribution \((70,84,168,224,168,84,70)\). This is an exhaustive finite proof because the lemma accounts for every function exactly once; no statistical sampling or unbounded inference is involved.

**Orbit proof.** Every incidence-graph automorphism either preserves or interchanges the two bipartition classes, because the graph is connected. A side-preserving automorphism is determined by a permutation of the seven point vertices preserving the seven line triples. Of the \(7!=5040\) permutations, precisely 168 preserve these triples, checked in `component_enumerator.py`. The map \(p_i\mapsto\ell_{-i}\) and \(\ell_j\mapsto p_{-j}\) is an incidence-preserving duality because \(i-j\in\{0,1,3\}\) is unchanged by the corresponding incidence test. Composing this duality with the 168 side-preserving maps gives 168 additional distinct automorphisms. Hence the full group has exactly 336 elements.

The enumerator acts on every weight-eight labeled word with all 336 permutations. It takes the lexicographically least remaining word as orbit representative, deletes its orbit and repeats until none remain. It obtains nine orbits, with the representatives and sizes in `ORBIT_REPRESENTATIVES.tsv`; their sizes sum to 868. Exhaustive orbit membership and coverage assertions in the code show that these nine are disjoint and cover *all* optimum functions. Thus the orbit classification is exact.

## Verification

Two independent finite enumerations are supplied. `component_enumerator.py` derives all coefficients by enumerating zero sets and independent component flips, and also verifies all automorphisms and optimum orbits. `direct_label_enumerator.cpp` instead visits all \(3^{14}=4,782,969\) ternary assignments and directly checks the two independence conditions and every zero-vertex neighborhood. It neither constructs components nor invokes the first algorithm. Both assert the complete coefficient vector and the optimum point-zero distribution. The proof relies on these actual exhaustive algorithms and their stated 14-vertex finite bounds; a finite check is not claimed to prove a theorem for larger projective planes.

Run from the artifact directory with:

```sh
python3 component_enumerator.py
c++ -std=c++17 -O2 -Wall -Wextra -pedantic direct_label_enumerator.cpp -o verify_direct
./verify_direct
```

Expected terminal markers are `CERTIFICATE_OK` and `TERNARY_CERTIFICATE_OK`, respectively. The temporary executable is not needed to reproduce the source-based proof.

## Relationship to prior work

Kraner Šumenjak, Rall and Tepeh introduced the same rainbow-independent invariant and identified its relationship with independent domination of \(G\square K_k\); their original 2017 arXiv text gives bounds and graph-family examples, not this fourteen-vertex polynomial or the optimum-orbit census. Zhu and Liu's 2019 paper addresses complexity and Nordhaus–Gaddum bounds. Gabrovšek, Peperko and Žerovnik (2023) determine scalar minima for products of paths/cycles and generalized Petersen graphs \(P(n,2)\) using tropical matrix methods; their results do not specialize to the Heawood incidence graph or its complete weight enumerator. Their 2020 paper instead studies a *different* invariant, independent rainbow domination, so its \(P(n,3)\) formulas cannot substitute for the theorem above.

The polynomial also counts independent dominating sets of \(H\square K_2\), by the original graph-prism correspondence. Searches for that equivalent formulation, as well as for Fano-plane incidence labelings and all-set tables, revealed no prior polynomial or nine-orbit classification. Non-indexed prior computations remain possible.

## Limitations

This is a finite exact classification for the Heawood graph, not for arbitrary incidence graphs or generalized Petersen graphs. The coefficients, orbit sizes, and minimality are proved by exhaustive finite certificate-backed enumeration plus a structural bijection, not by a short hand enumeration of every orbit. The code assumes standard Python 3 and a C++17 compiler for its reproducibility checks. The literature comparison is best-knowledge rather than exhaustive priority certification, and no independent expert audit has been performed.

## References

1. T. Kraner Šumenjak, D. F. Rall, A. Tepeh, *On k-rainbow independent domination in graphs*, arXiv:1709.08966v1, publicly available 2017-09-26, https://arxiv.org/abs/1709.08966 .
2. E. Zhu, C. Liu, *Notes on k-rainbow independent domination in graphs*, arXiv:1908.01432v1, 2019-08-05, https://arxiv.org/abs/1908.01432 .
3. B. Gabrovšek, A. Peperko, J. Žerovnik, *On the 2-rainbow independent domination numbers of some graphs*, published online 2023-02-15, https://doi.org/10.1007/s10100-023-00840-w .
4. B. Gabrovšek, A. Peperko, J. Žerovnik, *Independent Rainbow Domination Numbers of Generalized Petersen Graphs P(n,2) and P(n,3)*, 2020-06-18, https://doi.org/10.3390/math8060996 .
