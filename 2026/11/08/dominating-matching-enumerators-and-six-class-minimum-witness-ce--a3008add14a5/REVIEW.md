# Review of the dominating-matching enumerator for cycle prisms

## Correctness

**PASS.** The 34-state transfer is derived bijectively from actual matchings and domination, with 101 legal transitions. The bound of six dominated vertices per matched edge yields the minimum, and every third vertical rung attains it. Integer potential reweighting is checked on all transitions. The two zero-defect directed cycles of lengths three and six give denominator \((1-x^3)(1-x^6)\); adjugate degree bounds of 33, 67, and 101 make coefficient comparison through degree 103 a complete finite proof of the rational identities. The independent brute-force graph implementation verifies all minimum matching counts for \(3\le n\le12\). Neither brute force alone nor a plotted pattern is used as an infinite proof.

## Originality

**PASS, historical priority qualified.** Lu–Wu (2026) give upper bounds on paired domination in cubic bipartite graphs; Mynhardt–Schurch (2011) study paired domination in graph prisms; and Allagan and collaborators (2026) enumerate ordinary dominating vertex sets in a prism. The checked primary material does not give the enumerator of dominating matching witnesses or the six-class minimum coefficients. Published mathematical record searches under matching-domination and cycle-prism terminology found related results on other graph families, but no covering formula. Unindexed or inaccessible equivalent statements remain possible.

## Mathematical value

**PASS.** The formula solves a natural minimum-witness enumeration problem for all labelled circular ladders, reveals residue-six arithmetic and two different growth degrees, and provides the entire domination-by-a-matching polynomial, a substantial refinement of the scalar paired-domination number.

## Limits

The result concerns labelled prisms with \(n\ge3\), and counts **matching witnesses** rather than distinct minimum paired-dominating vertex sets. At \(n=4\), these numbers are respectively \(42\) and \(36\). No independent audit has occurred. Historical priority is provisional.

Self-review: passed. Independent audit: not yet performed.
