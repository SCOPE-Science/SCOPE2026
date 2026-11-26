# Independent mathematical audit

## correctness

PASS

The frozen pair-cost reduction and finite optimization are mathematically sound: the star Schur complement gives hub–leaf and leaf–leaf Green entries in ratio 1+μ. Distinct unordered pairs of Rademacher coordinates have uncorrelated products, giving 4 times the sum of within-class squared off-diagonals. At fixed hub occupancy exchange balances other classes; the integer marginal leaf cost is floor((m−h−1)/(k−1)), making the differences in the frozen text strictly increasing. The all-singleton endpoint trivially satisfies the isolation criterion, and the multinomial division counts the balanced partitions including ties. For the repaired claim independently use actual class sizes s_i and normalized energy Σ binom(s_i,2)+(R−1)(s_0−1). Moving a leaf from largest to smallest changes the energy by at most R−(s_max−s_min); it is feasible whenever the gap exceeds R>1. Hence optimal class sizes for j=k and k+1 differ from (m+1)/j by at most R, uniformly. After a split, k−1 unchanged classes contribute (k−1)m²/(2k²)+O(m). A class of size s=m/k+O(1) has split binomial cost (s²/4−s/2)+(u−s/2)²; nearest-integer balance attains the leading minimum regardless of where the hub goes. The hub correction is nonnegative and O(m), so the optimal split cost is (k−1/2)m²/(2k²)+O(m) for every optimal parent. The unrestricted k+1 cost is m²/[2(k+1)]+O(m); the common variance factor cancels. This checks the repaired ratio and the stated uniform O(m⁻¹) error. The example 117/4 is attained by leaving one leaf with the hub and splitting off four leaves; enumerating the two possible class types to split confirms optimality.

## originality

PASS

PASS applies only to the repaired one-split cross-budget claim. The frozen two-part originality claim cannot pass as written: the distinct same-day 276450ab2e3f summary materially covers the fixed-budget k≥3 balancing/convexity/classification and gives exactly the singleton-hub threshold, and 1edc2b42b895 matches at least the k=2 threshold. The shared date neither determines precedence nor removes the coverage. This is a substantive narrowing, not a finding of mathematical error or a failure caused by unavailable text. The repaired result credits those fixed-budget statements, proves only the needed coarse size bound, and establishes a uniform, sharp variance loss comparing two constrained budgets. No examined prior statement gives that one-split loss.

## value

PASS

The remaining result is independently useful: even a best one-class subdivision of any globally optimal parent has a dimension-independent variance penalty at fixed k and μ. The 9/8 limiting two-to-three penalty and exact 39/34 finite witness quantify the cost of restricted reuse versus redesign in a standard estimator; these are not just restated symmetry or balancing properties. Uniformity excludes the possibility of evading the penalty by a specially chosen optimal parent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
