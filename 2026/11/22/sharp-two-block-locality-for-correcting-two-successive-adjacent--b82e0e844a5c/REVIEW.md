# Review of the two-block binary two-swap locality theorem

## Correctness — PASS
The proof applies to every positive block length and every nonempty binary block set. The metric identity \(d(x,z)=\sum_j|\Delta_j|\) is shown by lower and matching upper transport bounds. A shortest obstructing pair has distinct nonzero internal boundary imbalance levels. Its radius-four budget excludes levels of magnitude at least two, leaving exactly two opposite signed levels and a three-block collision; swapping the final blocks between the two words gives a forbidden two-block collision without increasing distance. The \(b=1\) case and sharp witness are explicit. Standalone finite checks agree with the infinite proof: 66,196 equal-weight word pairs for the metric, plus all nonempty block sets of lengths one through four at powers two through five.

## Originality — PASS against checked sources
Ataba–Zabokritskiy (arXiv:2611.02192v1, Sections 2, 3, 6, 7) define precisely this sequential-swap concatenation problem, state \(2\le D_2(2)\le4\), and leave its exact value open. The new claim proves \(D_2(2)=2\). Other inspected works (arXiv:2509.06692, arXiv:2606.26905, arXiv:2607.19566) study code size or a disjoint-swap limited-permutation channel; they do not entail a stronger all-length two-block criterion. Semantic-index hits on bounded-run swap graphs, one-sided single swaps, Ulam balls and mixed deletion/swap channels likewise do not imply the exact claim. Accessible own ledger history contains an earlier one-swap short-block capacity finding, but no previously recovered two-error binary two-block horizon statement. The actual comparisons and searches appear in AUDIT.json. Residual priority risk: an earlier unindexed equivalent might exist.

## Value — PASS
The result closes a specific natural open case of the concatenation-locality parameter, improves the binary two-error test from up to four blocks to exactly two, and proves sharpness. The distinguishing lemma is structural: opposite nonzero prefix imbalances can be cross-spliced to form a lower-power obstruction. It applies uniformly to all binary block sets and block lengths and can be reused to decide code-family correction without testing arbitrarily long powers.

## Limits
The theorem treats only two sequential adjacent swaps and the binary alphabet. It does not supply a decoder, code-size optimum, polynomial-time list algorithm or other-channel locality; the finite verification scripts are falsification checks, not a proof of the all-length assertion. Independent external audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
