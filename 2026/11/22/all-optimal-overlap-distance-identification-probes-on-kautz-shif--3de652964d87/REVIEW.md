# Self-review

## Correctness — PASS
The proof derives the exact directed shift-and-append distance from suffix/prefix overlap. Distinct completions of one prefix have identical responses at every probe outside that pair, forcing all but one in each class. For different prefixes, their first differing position supplies two competing probes in one class; one necessarily belongs to the sample and separates their overlap lengths. The proof treats zero overlap, self-probes, all \(q\ge3\), and all \(n\ge2\). Independent BFS computations agree with the formula and check all minimum choices in five small parameter pairs. The polynomial and exact counts then follow from independent classes.

## Originality — PASS (qualified)
Rajan et al. (accepted version made public 2013-09-30, DOI:10.1080/00207160.2013.844335) already give the **minimum cardinality**, which is explicitly not newly claimed. Their complete manuscript Section 4.2 gives the Kautz bound and states it without proof; it does not classify all resolving sets or count optimum families. published-finding corpus searches for metric bases, Kautz identifiers, prefix classes and exact enumerators locate studies of different graphs and radius-one Kautz identifying codes, not the asserted complete directed-distance polynomial. The exact characterization and complete polynomial are logically strictly stronger than knowing one minimum dimension: they determine all subsets at all cardinalities. Priority remains qualified because terminology and unindexed complete classifications might exist.

## Mathematical value — PASS
The full feasible-set characterization solves a natural exact-distance probe-design problem on an infinite family of finite-state shift networks. It gives not just optimal number of sensors but the complete combinatorial design space, an exact reliability/cardinality enumerator, and a linear-output-time construction and uniform sampling of all optimal configurations. These are useful for designing and varying minimum resolving configurations, with an explicit limitation to exact measurements.

## Closest literature and limitations
The 2013/2014 metric-dimension result is the nearest antecedent and owns the known minimum-size assertion. Kautz radius-limited identifying codes have different signatures and are not interchangeable. This result assumes labeled words, exact directed distance and no sensor erasures. Remaining originality risk: unindexed earlier characterization of all metric bases under another name.

Self-review: passed. Independent audit: not yet performed.
