# Scientific assessment

## Correctness — PASS

The proof reduces nonlinear two-input variation to path variation of selector images of single jumps, using the finite piecewise-linear structure of order statistics. In a window crossing a fixed input cut, the number of right-side observations among the lowest \(q\) cannot decrease. For each fixed count, an opposing pair of monotone order-statistic thresholds permits at most one downward color switch. This gives the \(2q-1\) bound and its upper-rank dual; the fully explicit integer permutation witnesses exactly \(2\min\{q-1,w-q\}+1\) changes. The proof covers every stated radius, rank, length and real input. The executable checks match this analysis; they are not substituted for proof.

## Originality — PASS, qualified

Maragos–Schafer (1987) provides the general morphological max–min representation and threshold compatibility; the material inspected describes representations and median roots, not a sharp two-signal path-variation coefficient. Restrepo–Chacón (1994) establishes one-signal variation diminution for median smoothing rather than variation of output differences; its publicly available manuscript PDF could not be fetched reliably in full. Published mathematical records of the central median and the two endpoint ranks imply particular cases but not all intermediate ranks, including their width-independent constants. Statement-level comparison, not a title match, supports a provisional originality judgment. Unindexed early filter-stability literature remains a priority risk.

## Mathematical value — PASS

The complete rank formula distinguishes two-input robustness of every sliding quantile, rather than a single median or an arbitrarily selected filter. It reveals a sharp ladder with the perhaps counterintuitive result that the second-smallest rank always has coefficient three for arbitrarily wide odd windows, while the middle rank has coefficient equal to the full window width. Explicit finite witnesses and a uniform endpoint-clamped length guarantee make the classification useful for interpreting nonlinear filtering stability.

## Closest literature and limits

The original order-statistic morphology framework and the older one-input median-variation result are essential context; neither supplies the all-rank two-input theorem in the material accessible here. The claimed domain is restricted to real scalar data, odd symmetric fixed windows, clamped endpoints, unweighted path variation, and paths of at least one more sample than the window width. No claim is made for shorter paths or more general filters.

Self-review: passed. Independent audit: not yet performed.
