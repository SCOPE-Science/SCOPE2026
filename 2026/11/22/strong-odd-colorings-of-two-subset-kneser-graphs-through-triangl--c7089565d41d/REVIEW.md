# Scientific review

## Correctness — PASS

The graph \(\mathrm{KG}(n,2)\) is identified with the edges of \(K_n\), and strong-odd color classes are characterized completely as singleton edges, full triangles, or (only for even \(n\)) full stars. The proof checks star sizes \(2\), proper stars of size at least \(3\), whole stars, and triangles by explicit parity counts; it proves no other color classes occur. At most one full star can occur. Coloring costs reduce to maximum edge-disjoint triangle packings, whose four leave cases and existence are credited to Schönheim's theorem; the three even-residue cost differences establish the unique exceptional tie at \(n=6\). Independent-code-path finite checks test the class lemma and solve color partitioning exhaustively through \(n=7\), and construct and verify optimizers through \(n=10\). Computation is corroboration, not the infinite proof.

## Originality — PASS, provisional

The verified earliest public motivating preprint is Kwon–Park (January 22, 2024), which defines the invariant but addresses sparse graph bounds; Caro et al. (October 3, 2024) addresses planar and product bounds. The later 2025 Caro et al. paper establishes the Petersen \(n=5\) special case and the maximum odd-independent-set size in general Kneser graphs. Both are acknowledged. Neither its maximum-class size alone nor the classical triangle-packing theorem specifies the permitted partition classes of \(\mathrm{KG}(n,2)\), the full-star optimality cutoff, or the general chromatic-number formula. Semantic published-record searches did not identify an equivalent or stronger result. Unindexed articles, unpublished designs-to-coloring reductions, and incomplete global priority clearance remain risks.

## Value — PASS

The claim solves a natural infinite family for a recently studied coloring invariant and completely classifies optimal color partitions, not merely their sizes. The sharp dichotomy between odd orders (only packing/leave classes) and even orders (a full-star class is forced for \(n\ge8\)), including the \(n=6\) tie, makes the reduction to classical partial Steiner triple systems useful. This structural identification is not a direct numerical substitution into a known packing count without the nontrivial parity classification.

## Closest literature and limitations

Kwon and Park, arXiv:2401.11653; Caro et al., arXiv:2410.02336 and arXiv:2509.20763 (Petersen and Kneser odd independence); Schönheim (1966), cited via the ETSU construction-based maximum-packing exposition. The result is specifically the \(2\)-subset Kneser family with open-neighborhood parity; the named-color enumerator and higher-rank generalization are not claimed. Priority remains provisional.

Self-review: passed. Independent audit: not yet performed.
