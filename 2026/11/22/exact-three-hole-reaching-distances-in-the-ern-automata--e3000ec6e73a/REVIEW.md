# Scientific review: exact three-hole reaching distances

## Correctness — PASS

The result is a universal statement for the labeled cyclic Černý automaton and every omitted triple at every \(n\ge4\). The hole-action identity and the three-merge witness table independently supply the exact proposed upper bounds. The potential on zero-, one-, two-, and three-hole states is nonincreasing by more than one per transition. Because the omitted-set cardinality cannot decrease, every path to a three-hole image stays in the potential's domain and gives the lower bound. Disjoint adjacency cases exhaust all triples; their count gives the complete histogram. An independent BFS checks all 3,875 triples at sizes 4–18. The checker additionally tests 3,889,461 local potential transitions through size 95. Finite verification is supporting evidence, not an infinite proof.

## Originality — PASS, qualified

The closest primary papers by Ferens–Szykuła (2022), Casas–Volkov (2023/2024), and Zhu (2024) study complete reachability and Don-type estimates, rather than the exact target-wise codimension-three spectrum. Public results on the same automaton already settle the worst-case \(3n\), the minimum distance \(7\) for \(n\ge5\), and all individual *two-hole* distances. Those overlapping facts are fully credited and are excluded from the claimed new contribution. The new classification gives each prescribed triple's distance and a full triangular/plateau/singleton spectrum. An equivalent older theorem under a different indexing or avoiding-language formulation remains possible; independent literature audit has not been performed.

## Value — PASS

Prescribed-subset reaching cost is a natural invariant in automata synchronization and complete reachability. Upgrading a two-hole classification to three holes is not a mere renaming: two separate adjacency interactions, wraparound boundary cases, and a new constant-multiplicity plateau appear. The complete all-length metric and histogram provide immediately usable exact benchmarks for shortest-reaching algorithms and distinguish the distribution of costs from previously known extrema.

## Scientific limitations

No claim is made for higher codimension, arbitrary completely reachable automata, independent mathematical review, or priority beyond the checked published sources. The strongest extant worst-case and lower-envelope consequences are not presented as new results.

Self-review: passed. Independent audit: not yet performed.
