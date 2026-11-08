# Self-review

## Correctness — PASS

The exact counting proof is reconstructed from the tree count \((2n-3)!!\), contraction bijections for one and two disjoint prescribed fringe subtrees, and laminarity of descendant leaf sets. Every four-leaf fringe node contains precisely two cherries if balanced or one if asymmetric. The resulting first moments and mixed moments give both rational covariance formulas. The exceptional boundary \(n=4\) is checked directly, \(n=5\) has no disjoint pair, and strict signs for all greater sizes follow by elementary polynomial inequalities. Asymptotics and the increasing ratio follow from the exact formulas. A separate enumeration implementation passed 146650 exact assertions through eight leaves. These finite checks reinforce but do not replace the counting proof.

## Originality — PASS, with risk

Closest primary results inspected: Chang–Fuchs (2009/2010), a single-fringe-pattern framework; Wu–Choi (2015/2016), joint *rooted* cherry and pitchfork laws; Coronado et al. (2018/2019), *induced* rooted quartets; and Choi–Kaur–Thompson–Wu (2024), the complete four-subtree covariance vector for *unrooted* PDA trees. The last work is the closest comparison and is not being claimed new. The current statement is the explicit pair of mixed covariances under the **rooted** PDA law, including all finite sizes, strict signs and linear limits. The unrooted covariance vector alone cannot recover rooted four-leaf fringe counts; the five-leaf unrooted shape resulting from rooting four original leaves provides a counterexample to direct determination. Broad mixed-moment derivability from older pattern-count frameworks remains a priority risk. Searches do not certify uniqueness.

## Value — PASS

Four leaves are the first subtree size at which rooted binary trees have distinct balance shapes. The exact, opposite-sign mixed dependence with the ubiquitous cherry count therefore characterizes how balanced and asymmetric microscopic motifs couple to a global shape statistic under the neutral rooted PDA model. The covariance magnitudes stay of order \(n\), and the comparison is relevant to joint calibration of phylogenetic shape diagnostics. It is a natural first nontrivial shape classification rather than an arbitrary numeric slice.

## Limits

No independent audit has been performed; the claim is not an assertion about unrooted, induced-quartet, or non-PDA ensembles. The general single-pattern theory and newer unrooted four-pattern covariance results are nontrivial antecedents; implicit prior cross-moment specialization cannot be ruled out.

Self-review: passed. Independent audit: not yet performed.
