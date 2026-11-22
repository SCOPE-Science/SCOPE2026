# Visibility-polynomial separation and optimal-set symmetry of the Shrikhande–rook pair

## Finding

Let \(R=K_4\square K_4\) be the four-by-four rook graph and let \(S\) be the Shrikhande graph, the Cayley graph on \(\mathbb Z_4^2\) with connection set \(\{(\pm1,0),(0,\pm1),(1,1),(-1,-1)\}\). Write \(v_k(G)\) for the number of vertex subsets \(X\subseteq V(G)\) of size \(k\) such that every two vertices in \(X\) have a shortest path whose interior avoids \(X\). Define the **ordinary** visibility polynomial by \(V_G(z)=\sum_{k=0}^{16}v_k(G)z^k\).

The exact polynomials are

\[
\begin{aligned}
V_R(z)={}&1+16z+120z^2+560z^3+1784z^4+3936z^5\\
 &+5728z^6+4768z^7+1512z^8+96z^9,\\
V_S(z)={}&1+16z+120z^2+560z^3+1760z^4+3744z^5\\
 &+5216z^6+4432z^7+2004z^8+384z^9+32z^{10}.
\end{aligned}
\]

In particular, \(\mu(R)=9\), attained by exactly \(96\) vertex subsets, while \(\mu(S)=10\), attained by exactly \(32\) subsets. In **each** graph, all optimum subsets form one orbit under graph automorphisms. Moreover, replacing any single vertex of an optimum subset by any unselected vertex never yields another optimum subset; hence the minimum-basis token-jumping reconfiguration graph has no edges in either case.

Although \(R\) and \(S\) have the same strongly regular parameters \((16,6,2,2)\) and spectrum, ordinary visibility separates them, with the first coefficient disagreement already at size four. Specifically there are \(36\) and \(60\), respectively, distinct four-point minimal obstructions to mutual visibility.

## Assumptions and scope

All graphs are finite, simple, undirected, and labelled by the sixteen ordered pairs \((i,j)\) with \(i,j\in\{0,1,2,3\}\). In \(R\), two distinct vertices are adjacent if they share one coordinate. In \(S\), they are adjacent precisely when their coordinatewise difference modulo four lies in the connection set given above. The polynomial counts *ordinary* mutual-visibility sets, not total, outer, dual or lower maximal visibility sets. Subsets are distinct as vertex subsets, without quotienting by symmetry; only the separate orbit statement uses graph automorphisms. The empty subset is counted.

## Proof

**Exact forbidden-quartet lemma.** Every vertex of either graph has six neighbors. For every pair \(u,v\) of distinct vertices, the intersection \(N(u)\cap N(v)\) has precisely two elements, by the respective explicit adjacency rules (and the strongly regular parameters). Both graphs have diameter two. If \(u,v\) are adjacent, they are automatically mutually visible. If not, every shortest \(u,v\)-path has length two and is obtained by choosing one of their two common neighbors, say \(a\) or \(b\). Thus the pair ceases to be visible inside a chosen subset \(X\) exactly when \(\{u,v,a,b\}\subseteq X\). Consequently, letting

\[
\mathscr F_G=\big\{\{u,v\}\cup(N(u)\cap N(v)):u\ne v,\ uv\notin E(G)\big\},
\]

with duplicate sets identified, **a subset \(X\) is mutually visible if and only if it contains no member of \(\mathscr F_G\)**. This equivalence covers every possible subset without approximation. There are \(72\) unordered nonadjacent vertex pairs in each graph; their quartets reduce to \(36\) distinct obstructions in \(R\) and \(60\) in \(S\). In particular \(\binom{16}{4}-36=1784\) and \(\binom{16}{4}-60=1760\), explaining the first coefficient difference.

**Complete finite certificate.** Encode \((i,j)\) by \(4i+j\) and each subset \(X\) by \(m_X=\sum_{v\in X}2^v\). For each integer \(m\) from zero through \(65535\) inclusive, the certificate tests whether \((m\mathbin{\&}q)\ne q\) for every distinct 4-bit obstruction mask \(q\) derived above. It increments the coefficient indexed by the number of set bits of \(m\). This loop is exhaustive because the vertex set has exactly sixteen members. The self-contained implementation in `visibility_polynomial.py` runs the enumeration, checks all coefficients, and prints an exact SHA-256 digest of the membership bitstring in increasing mask order. In addition `visibility_direct.cpp` independently enumerates every subset and, for each chosen pair, directly compares the ordinary shortest-path distance to its distance after deleting all other chosen vertices; this uses no obstruction hypergraph. Both finite algorithms return the displayed polynomials.

**Symmetry classification and exchange isolation.** The certificate explicitly constructs \(1152\) automorphisms of \(R\): independent permutations of its two coordinate alphabets, optionally followed by coordinate interchange. For \(S\) it constructs \(192\) affine automorphisms: translations on \(\mathbb Z_4^2\) composed with all \(2\)-by-\(2\) matrices modulo four that preserve its six-element connection set. Every constructed map is independently checked to preserve graph adjacency. Acting on one enumerated optimum subset gives respectively \(96\) and \(32\) distinct optimum subsets, equal to the complete enumerated numbers of optimum subsets; thus every optimum lies in the same orbit. Finally, the certificate checks every ordered removal–insertion pair for each optimum and finds no other optimum, proving the claimed exchange isolation. This is an exhaustive finite proof, not inference from a sample or search timeout.

## Verification

With Python 3 (standard library only), run `python3 visibility_polynomial.py`. Independently compile and run `g++ -std=c++17 -O2 visibility_direct.cpp -o visibility_direct && ./visibility_direct`. The expected terminal lines end in `VISIBILITY_EXACT_PY_OK` and `VISIBILITY_DIRECT_CPP_OK` respectively. The first program also checks that each optimum belongs to the single constructed symmetry orbit and that there are no single-vertex exchanges among optima. Both programs process every one of the \(2^{16}=65536\) labelled subsets of each graph. The complete recorded outputs and executable source are supplied separately. No external package or database supplies the coefficient values.

## Relationship to prior work

Brešar and Yero (2023) formalized lower ordinary mutual visibility in graphs. Cicerone, Di Stefano, Klavžar and Yero (2024) already establish the connection between the *maximum cardinality* of ordinary mutual-visibility sets in Cartesian products of complete graphs and Zarankiewicz's extremal problem. Hence the rook-graph maximum alone is not asserted novel. Bujtás, Klavžar and Tian (first preprint December 2024), and Tonny and Shikhi (2025), introduced and developed general visibility polynomials; their inspected texts do not state these graph-specific polynomials or the Shrikhande–rook comparison. Earlier related calculations for three-row rook graphs, for lower inclusion-maximal configurations, and for other invariants of the Shrikhande–rook pair do not imply the present full coefficient tables or symmetry classifications. Novelty remains subject to external priority checking.

## Limitations

This is an exact **finite**, sixteen-vertex classification, not an infinite-family result. The comparison does not classify all nonmaximum sets geometrically, or extend to arbitrary strongly regular graphs. The proof rests on complete finite enumeration after a proved quartet reduction; its two independent exhaustive implementations and transcript are provided for reproducibility. The automorphism argument uses an explicitly validated subgroup large enough to be transitive; it makes no unverified assertion about all automorphisms. Independent expert verification and exhaustive historical-priority determination have not been performed.

## References

- B. Brešar and I. G. Yero, *Lower (total) mutual visibility in graphs*, arXiv:2307.02951 (first public 2023-07-06), https://arxiv.org/abs/2307.02951.
- S. Cicerone, G. Di Stefano, S. Klavžar and I. G. Yero, *Mutual-visibility problems on graphs of diameter two*, arXiv:2401.02373 (first public 2024-01-04), https://arxiv.org/abs/2401.02373.
- Cs. Bujtás, S. Klavžar and J. Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, arXiv:2412.03066 (first public 2024-12-04), https://arxiv.org/abs/2412.03066.
- T. K. B. and M. Shikhi, *On the visibility polynomial of graphs*, arXiv:2507.01851 (2025), https://arxiv.org/abs/2507.01851.
