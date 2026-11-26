# Independent mathematical audit

## correctness

PASS

The prefix automaton is minimal: the completion suffix for the longer prefix separates any two proper prefixes, as a shorter prefix followed by that suffix cannot contain the whole pattern. For a nonempty input, an initial 0^k with k≥r merges all live states; with k<r its first 1 starts a separate trajectory at B_1 from the high-zero suffix and resets the other class to A_0. Before the next zero, ones leave the latter class at A_0 and advance or kill the high class; the next zero merges the two if both survive. A high-class survivor before merging cannot be a fixed output, since every B-state belongs to the other input class. Starting with ones, the first zero already merges the survivors with killed domain K_k or K_*. Short pure runs are not idempotent; long ones give the already enumerated maps. Every listed kill-and-merge form is attained by the stated prefix and a suffix reaching the requested fixed output without acceptance. For s=1 the 1 kills the high class directly and the merged A_r state cannot leave without acceptance; for r=1 a live A_1 reached at the first zero cannot reach A_0 without acceptance. The (1,1) case has five elements and four idempotents. The identity, zero and disjoint rank-two form counts give the displayed formulas; division by the independently sourced total sizes gives the limits.

## originality

PASS

Pass for the composition-idempotent count and the explicit rank and killed-domain classification, not the previously known total size. No distinct equivalent was established in the inspected evidence.

## value

PASS

The idempotents describe all retract images and sink fibers in a natural benchmark family of factor-recognition monoids. The full classification, including both singular parameter axes, exposes rank collapse and determines asymptotic density while the known total syntactic complexity supplies neither. This is more informative than reproducing the total size or counting a few small instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
