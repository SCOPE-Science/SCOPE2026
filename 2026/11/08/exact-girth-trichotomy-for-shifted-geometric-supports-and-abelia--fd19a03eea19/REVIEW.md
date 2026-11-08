# Scientific review: shifted geometric support girth

## Correctness — PASS
The graph has weights \(b^j+c\). If \(c<b(b-2)\), all weights from the third onward exceed twice the previous weight, forbidding a highest-weight edge on any cycle; the two remaining matchings are acyclic. The proof constructs an explicit simple cycle of length \(2b+2\) for every \(c\ge b(b-2)\). In the intermediate band, larger weights are excluded, eligible third-weight edges occupy distinct modulo-\(b-1\) components, and the path between their endpoints through two lower matchings has exactly \(2b+1\) edges. Above \(c=b^2-b-1\), an explicit six-cycle exists. Sidon uniqueness for sums of two base powers excludes four-cycles. The finite verifiers independently corroborate the bounds, while the proof establishes all parameter values. The word-complexity corollary is conditional on the published incidence-forest characterization, whose statement was checked.

## Originality — PASS, with priority risk
The 2026 Zeng–Xue–Zeng paper supplies the forest characterization, but the accessible abstract and introductory material do not state the exact two-threshold shifted geometric-support girth law. The potentially relevant examples subsection was not completely retrievable; its contents remain a genuine priority risk, not a negative full-text finding. Earlier general three-marker forest-extension criteria and logarithmic support bounds do not give the girth of this designated infinite support. Public record and related-result searches showed no direct coverage. This is a bounded best-knowledge originality assessment, not a uniqueness certificate.

## Value — PASS
The main graph invariant is a natural complete classification across an infinite two-parameter lacunary family, rather than an arbitrary finite slice. The first transition exactly determines which characteristic words attain minimal Abelian maximal pattern complexity; for \(b\ge3\) the second identifies a genuine decrease in the shortest obstruction from length \(2b+2\) to six (the two finite cases coincide when \(b=2\)). The entire cyclic range is quantitatively distinguished by exact girth, beyond a yes/no forest condition.

## Sources and limitations
Primary structural source: Zeng, Xue and Zeng, *Abelian maximal pattern complexity and extremal words*, arXiv:2609.28059 (first public September 23, 2026). Background: Kamae, Widmer and Zamboni, *Abelian maximal pattern complexity of words*, arXiv:1301.5113. The graph proof is elementary and self-contained; classification outside integer bases and nonnegative shifts, nonminimal complexity values, and definitive historical priority are not claimed.

Self-review: passed. Independent audit: not yet performed.
