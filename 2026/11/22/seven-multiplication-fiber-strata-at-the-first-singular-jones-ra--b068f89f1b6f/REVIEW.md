# Scientific review: seven Jones-monoid multiplication-fiber strata

## Correctness — PASS

The rank-\(n-2\) diagrams have exactly one adjacent cap and cup, with \(n-1\) choices each; product gluing splits by whether their middle cap indices have distance at most one. For distance at least two, the explicit upper-half and lower-half branch bijections give the four exact prescribed-fiber formulas. The four indicator coincidences for the disjoint/disjoint case obey a closure condition (any three force the fourth), so seven is impossible. The one-, two-, three-, four-, five-, six-, and eight-fiber multiplicities are obtained by a complete intersection count, and their weighted sum plus the \(3n-5\) rank-preserving fibers equals the total \((n-1)^4\) ordered pairs. The independent standard-library diagram-gluing checker confirms all individual fibers for \(3\le n\le10\), and all candidate factors against a complete Catalan diagram enumeration for \(3\le n\le8\). The general claim rests on the combinatorial bijection, not on finite enumeration.

## Originality — PASS, with historical-priority qualification

East and Gray, *Diagram monoids and Graham–Houghton graphs* (arXiv:1404.2359, first posted 2014-04-09), Section 9 and Lemma 9.7, provide the Jones class structure, rank-preserving adjacency and ideal-generation work. The present theorem credits that adjacency and contributes the full rank-decreasing prescribed target law and its multiplicity spectrum, which are not furnished by that Section 9 analysis. Dolinka et al., *Enumeration of idempotents in planar diagram monoids* (arXiv:1507.04838, first posted 2015-07-17), classify and count *idempotents*, whereas the current factors range over every rank-\(n-2\) diagram without an idempotency condition. Semantic searches of a published mathematical-record index returned nearest Jones results about power stabilization and commuting idempotents, not the unrestricted two-factor fibers; other published mathematical summaries did not exhibit this statement. These are implication comparisons, not a proof that no unindexed equivalent exists. The relevant research risk is an unindexed general diagram-product coefficient or an inaccessible document implying this precise spectrum.

## Value — PASS

The first singular Jones rank is the smallest nontrivial multiplication layer. Its exact prescribed multiplication structure constants are natural invariants of the entire Green class, rather than an arbitrary finite slice: for all \(n\ge4\) they distinguish two rank outcomes, resolve every target, and reveal a genuinely noninterval spectrum with forbidden fiber seven. Counting this spectrum is useful for multiplication operators and aggregate diagram-product statistics; the result does not claim a general theorem for all ranks or arbitrary-length products. The enumeration is parameter-uniform and not a known-table recomputation.

## Sources and scientific limits

- J. East and R. D. Gray, *Diagram monoids and Graham–Houghton graphs: idempotents and generating sets of ideals*, arXiv:1404.2359, first public 2014-04-09, especially Section 9 and Lemma 9.7 (full relevant HTML section inspected).
- I. Dolinka et al., *Enumeration of idempotents in planar diagram monoids*, arXiv:1507.04838, first public 2015-07-17, especially Sections 2–4 (relevant full PDF text and diagrams inspected).
- Supporting independent computation: `check_jones.py`, with captured `CHECK_OUTPUT.txt` ending in `ALL_CHECKS_PASS`.
- Residual risks: unknown older equivalent in the Temperley–Lieb structure-constant literature; computational checks stop at \(n=10\); independent mathematical audit not performed.

Self-review: passed. Independent audit: not yet performed.
