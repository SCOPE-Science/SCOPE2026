# Independent mathematical audit

## correctness

PASS

Each element occupies a unique cell (E-class,F-class), so equality follows from the two coordinate equalities and shore names matter. The distinct-variable partition pairs number 5+3×3+1=15; exactly-two-equal triples give 3×3=9, and all-equal gives one. The six distinct-edge motifs, including both orientations of stars, are edge-selected and supply all repeated-variable cases as well. The opposite-shore three-stars occupy six edges if disjoint and cannot supply a three-matching; their shared five-edge double star also fails until an edge avoiding both centers is added. Such an edge leaves a spare leaf on each side for a matching and supplies both two-star-plus-disjoint-edge motifs by omitting at most one old leaf. The shared stars supply a three-edge path. The four choices of whether the extra endpoints are old/new are shore-size-distinguished. Commutation is equivalent to rectangular components by fourth-corner closure along alternating paths. Both stars in one rectangle cost ≥9 edges; in different rectangles they cost ≥3 each and a path requires either expanding one to ≥6 or using a third rectangle of ≥4. At equality the three listed rectangles/unions meet every motif; a disjoint singleton edge extends all larger sizes. An independent integer-mask enumeration found 25 profiles and the six-edge 4×4 labelled counts 576,288,288,144 by shore cardinalities (3,3),(3,4),(4,3),(4,4), and independently recovered exactly the three commuting nine-edge component multisets. The replay design and frozen replay path are `verify_profiles.py`, lines 10–80; the frozen script was inspected, not executed. The all-size proof does not rest on the bounded grid check.

## originality

PASS

The supported distinct result is the simultaneous realizability classification and sharp six-versus-nine comparison for named transverse equivalences. The incidence translation and rectangularity criterion are background mechanisms, not claims to novelty. Checked rank-one, nested, bipartite extension-rank and graph universality work neither matches the assumptions and objective nor entails the exact minima and named equality classes.

## value

PASS

Simultaneously realizing every permitted three-variable atomic configuration is a natural finite-model invariant. At this first arity where opposite-shore incidence and a path interact, permutability has an exact three-element cost and changes the entire minimum-host classification. Researchers can use the lists as small universal testing structures for the two named relations. The theorem is finite and quantifier-free, not a claim about general satisfiability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
