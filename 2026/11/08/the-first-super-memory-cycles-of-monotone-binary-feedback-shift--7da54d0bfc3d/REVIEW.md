# Review of the monotone feedback-register period classification

## Correctness

PASS. The state update is order-preserving because shifting preserves the product order and its feedback coordinate is nondecreasing. Any two comparable states of a periodic orbit would, under repeated iteration by their cyclic index difference, form an increasing chain returning to its first member, which forces equality. Thus orbit states are an antichain. Conversely a cyclic word with antichain length-\(n\) windows admits a monotone positive-DNF extension that prescribes all successors; the orbit is therefore realized. The LYM chain-counting argument bounds its length by the middle binomial coefficient. The complete remaining finite range for memory one through six is exhaustively enumerated, with two differently structured implementations. For memory six they independently obtain 28 rooted period-seven words, 18 rooted period-nine words and no period-eight or period-ten-through-twenty word; the six rotational representatives agree. Positive feedback and an explicit period-nine trajectory witness attainment.

## Originality

PASS, with qualification. Çalık, Sönmez Turan and Özbudak (2010) analyze maximum-length nonlinear feedback shift registers, with full-length cycles and XOR-based necessary conditions; this is not a maximum-period calculation for monotone feedback. Just and Enciso (2013) present the more general cooperative-network antichain upper bound, whose six-dimensional value is 20 rather than the actual shift-register maximum of 9, and do not classify the shift-subclass cycles. Arratia, Canfield and Hales (2023) investigate the distinct noncoalescing feedback family. Relevant full-text material was examined and targeted scientific index and published-results searches found no exact previous statement of the six-stage 9-cycle maximum or all six rotation classes. Unindexed studies of monotone shift registers remain a residual historical priority risk; the search is not a proof of global novelty.

## Value

PASS. In a shift register with monotone Boolean feedback, the first possible orbit longer than the memory is a natural structural threshold, not an arbitrary word census. It distinguishes constrained one-feedback cooperative networks from general monotone Boolean systems: the latter permit periods as long as the width of the Boolean lattice, whereas at six stages the shift architecture reduces the maximum from 20 to 9. The exact absence of period eight and the complete classification of periods seven and nine provide meaningful rigidity information for small cooperative sequential circuits and cycle construction.

## Sources and limits

- Çalık, Sönmez Turan and Özbudak (2010), DOI: 10.1587/transfun.E93.A.1226. Examined the publicly accessible article and its feedback structure/results.
- Just and Enciso (2013), DOI: 10.1186/1687-1847-2013-313. Examined the open full text and its general cooperative-network cycle bounds.
- Arratia, Canfield and Hales (2023), DOI: 10.1017/S0963548323000020. Examined the article text and its noncoalescing feedback framework.

The exhaustive computation is limited to six memory cells but covers all relevant candidate periods by a mathematical cutoff; this gives an unconditional conclusion within the stated range. Independent historical and scientific confirmation is not yet available.

Self-review: passed. Independent audit: not yet performed.
