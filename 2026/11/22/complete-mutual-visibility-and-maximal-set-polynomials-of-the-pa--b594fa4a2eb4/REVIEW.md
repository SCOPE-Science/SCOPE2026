# Scientific review

## Correctness (PASS)

The claim is a finite exact census. The incidence formula explicitly determines all 18 vertices and all 27 edges. The first exhaustive source enumerates every mask, all geodesics for every selected vertex pair, and therefore the exact visibility predicate. The downward-closure lemma makes one-vertex-extension tests equivalent to maximality. It gives 14,287 feasible sets, coefficients \((1,18,153,762,2340,4374,4605,1998,36)\), and facet counts \((63,1710,36)\) at sizes \((6,7,8)\). A separately written blocked-BFS algorithm agrees on every membership-state byte (same deterministic fingerprint). One computation constructs and edge-tests 216 automorphisms and partitions all facets into 15 orbits; a separate complete distance-preserving-bijection enumerator proves that there are no additional automorphisms. This is a rigorous finite certificate, not sampling; the included verifier is needed to reproduce the full exhaustive step. Remaining risk: a software implementation error shared by the independent methods or an environmental execution defect; no higher-order statement is claimed.

## Originality (PASS, best knowledge)

Brešar–Yero (arXiv:2307.02951v1) introduces the lower visibility invariant and studies general bounds and other graph families, without a Pappus enumeration. Boruzanlı Ekinci–Bujtás (arXiv:2403.15645v1) studies Kneser, bipartite Kneser and Johnson families; its total-visibility theorem and open ordinary-visibility question concern different objects/quantifiers. The graph-specific MathWorld entry does not display mutual-visibility coefficients. Querying published research records with the Pappus, incidence, polynomial, maximality and exact-count aliases located related but different problems; accessible earlier claims contain no implication of this census. Residual risks include unindexed Pappus computations, dynamically evaluable general-purpose graph databases, and literature unavailable in full text. Absence of search results alone is not evidence of global originality.

## Mathematical value (PASS)

The Pappus graph is a canonical cubic symmetric, distance-regular 18-vertex Levi graph of a highly structured incidence configuration. The established lower mutual-visibility invariant measures the worst outcome of greedy inclusion-maximal placement, and the novel exact answer \(6\), contrasted with optimum \(8\), gives a mathematically motivated nonpure visibility complex. The **complete** labeled face polynomial, facet cardinality polynomial, and 15 orbit census distinguish optimal from nonoptimal greedy placements and quantify the exact symmetry of all optimal placements; this has more purpose than an arbitrary induced-subgraph count. It is finite, but the natural graph and invariant were selected before computation rather than by a desired number. No downstream infinite theorem is asserted.

Self-review: passed. Independent audit: not yet performed.
