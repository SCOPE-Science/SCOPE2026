# Independent mathematical audit

## correctness

PASS

The original table, cycle codes and hash fingerprints are correct, but the Finding's literal 'all other nonzero states' includes 1, which maps to zero in both rules. The replacement RESULT.md states that the period-20 basin is exactly the representable open interval and corrects what the supplied verifier asserts versus prints. The real polynomial is the Paul et al. Table 2 logistic entry at C=1. Exact rounding was independently reconstructed in integer units of 2^−133: for consecutive scaled values u,v, compare the rational argument with (u+v)/2 and choose the even encoding at equality. The exact A argument is at most 3.98/4; the staged product is at most (255/64)(1/4). Both maps thus stay in the specified code interval. I generated all 16,257 successors for each rule and replayed every orbit to first repetition separately. For A the period/basin/max-depth triples are (1,2,1), (5,2026,77), (22,14229,87); for B they are (1,2,1), (20,16255,83). In both maps the zero-basin codes were 0000 and 3f80. The 2,205 edge differences, every cycle code and both digests matched the frozen certificate. The replacement preserves the correct finite census and does not rely on the asserted strength of the supplied verifier.

## originality

PASS

The distinct repaired claim is the complete graph invariant of a published state-dependent logistic polynomial at its maximal external control under the two specified rounding rules, not the polynomial itself or eventual periodicity. Close same-date bfloat16 censuses use materially different functions and rounding trees; neither states nor mechanically implies this comparison. No ordering is inferred from their common date.

## value

PASS

For a motivated real design at its documented control endpoint, the audit gives the exact collapse from two distinct nonzero recurrent basins to one under a specified arithmetic change. The depths, sizes, and changed-arrow count make this a reproducible benchmark for rounding sensitivity rather than just an example of eventual periodicity. The correction preserves that quantitative insight and distinguishes it from the unchanged {0,1} basin.

The dated certificate retains the supplied scientific assessment, sources and limitations.
