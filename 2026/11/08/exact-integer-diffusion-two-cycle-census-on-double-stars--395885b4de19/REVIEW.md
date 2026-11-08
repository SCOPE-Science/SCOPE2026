# Scientific review

## Correctness — PASS
The exact initial-periodic-state formula follows from the edgewise two-step reversal identity, independent integer gap choices on a tree, and the complete leaf-sign and hub-sign partition. The calculation covers every integer \(a,b\ge1\), including boundary cases \(a=1\), \(b=1\), and \(a=b\). Two independent verification routes matched the formula: direct diffusion on 31,946,794 bounded normalized chip configurations and all edge-sign patterns for 25 parameter pairs. The infinite theorem is supported by the written proof, not by the finite checks alone.

## Originality — PASS, qualified
Duffy et al. [1] study the same diffusion rule and prove eventual periodicity with a transient estimate on stars. Long and Narayanan [2] establish eventual period at most two on every finite graph. Their statements neither enumerate the already-periodic points on double stars nor imply the balanced-arm central-tie count. Targeted searches  yielded no exact equivalent. A separate complete-graph diffusion calculation concerns a different family, while a double-star zero-forcing result concerns a different invariant. Unindexed publications remain an acknowledged priority risk.

## Value — PASS
A complete two-parameter recurrent-state count on the smallest tree family with two branching hubs is a natural extension of the study of integer diffusion. The proof identifies and quantifies a distinct balanced-arm recurrence mechanism: \(2a^{2a}\) states have a permanently tied hub edge precisely when the branches have equal sizes. Counts of already-periodic states and their temporal orbit numbers can now be used without enumerating unbounded integer initial conditions.

## Limits and comparisons
The claim concerns initially periodic normalized states only, not transient basin cardinalities, eventual hitting times, or a formula for arbitrary trees. In particular, known general eventual-period-two results provide the permitted periods but not the new parameter-dependent state populations. The finite programs are cross-checks, not independent scientific certification. No claim of comprehensive historical priority is made.

Self-review: passed. Independent audit: not yet performed.

## References
[1] C. Duffy et al., *A Variation on Chip-Firing: the diffusion game*, arXiv:1609.05792, 2016.

[2] J. Long and B. Narayanan, *Diffusion on graphs is eventually periodic*, arXiv:1704.04295, 2017.
