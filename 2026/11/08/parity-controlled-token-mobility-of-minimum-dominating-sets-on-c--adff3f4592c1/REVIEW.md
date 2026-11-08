# Self-review

## Correctness — PASS

The four-vertex closed-neighborhood lower bound is attained by explicit word constructions, so the minimum sizes are established without assuming earlier enumerative theorems. For odd lengths, the excess-cover argument excludes any double-selected column, and the independent-set condition on empty columns proves that the sole surplus singleton pair is unique. Color forcing supplies exactly two configurations at each distinguished-pair position, with an explicit parity condition on the pair. A one-token change can only move a member of that pair to its neighboring empty column; the target row is uniquely forced by domination at the newly emptied column. The resulting permutation \((i,x)\mapsto(i-2,\bar x)\) has order \(2n\) and consists of one orbit. The parity of the source and target rows proves the slide dichotomy. The even divisible-by-four and length-three boundary arguments are separate. Two complete finite enumeration strategies, with attached code and outputs, agree in their shared ranges.

## Originality — PASS, with stated historical risk

The closest *same-host* work is Allagan (2026), arXiv:2601.03488, whose full text counts optimal dominating sets and introduces numerical flexibility indices, but does not classify edges of either reconfiguration graph. Suzuki–Mouawad–Nishimura (2014), arXiv:1401.5714, treats addition/removal adjacency among dominating sets up to a threshold, not fixed-size one-token moves. Bouchou–Blidia (2016), DOI:10.7494/OpMath.2016.36.5.563, treats criticality of a related domination invariant on cycles. Fricke et al. (2011) introduce the sliding \(\gamma\)-graph construction without this cyclic-prism family classification. Equivalence via two-row encodings and stronger prior-coverage possibilities were compared in statement form; none of the inspected results states or entails these specific connected-component isomorphisms. Bibliographic and research-record coverage is incomplete; an unindexed equivalent result remains possible.

## Value — PASS

Minimum dominating-set counts do not determine accessibility under single-monitor reassignment. The theorem gives a sharp infinite parity-controlled obstruction: for odd prism lengths, unrestricted one-token relocation always connects all \(2n\) optimum sets, but edge-constrained relocation changes from a full cycle to a completely edgeless graph as the length changes by two. The diameter \(n\) supplies an exact movement cost. The additional zero-defect regime of lengths divisible by four gives a natural comparison. This answers a well-motivated reconfiguration question on a standard cubic family, rather than an arbitrary finite slice or an algebraic restatement of counts.

## Limitations and closest literature

The two-defect class \(n\equiv2\pmod4\) is not addressed, nor are larger feasible sets. Finite verification does not establish the infinite theorem by itself. Priority has not been independently established against all unpublished or inaccessible sources. The model's distinction from addition/removal is essential.

Self-review: passed. Independent audit: not yet performed.
