# Independent mathematical audit

## correctness

PASS

This PASS is for the replacement files under /workspace/repairs/3, not the original proof. Frozen RESULT.md Step 3 claims only certain overlapping C windows can coexist and that all other overlaps force incompatible partners; (1 4)(2 3) is a compatible joint B and C^- occurrence using the same transposition (2 3). It has positive probability in the finite fixed-count model, and its contribution to E[B_n C_n^-] cannot be dropped by incompatibility. In the corrected proof, an overlap of compatible matching motifs always shares an entire transposition. A connected cluster of matching motifs forms a connected graph of prescribed edges linked by C motifs; knowing one edge leaves at most finitely many choices for each successive edge along a spanning tree (endpoints differ in absolute value by one in the two intervals). Thus r-edge clusters have O(n²) placements, or O(n) if a B forces the root edge to be adjacent. Distinct C motifs cannot have exactly the same two transpositions, since the four ordered endpoints determine the only possible two disjoint adjacent intervals and the pairing. Hence overlapping C-only clusters have r≥3, and mixed B/C clusters have r≥2. Each is negligible by the O(n^-r) prescription bound; distinct B's cannot overlap compatibly. A-only connected sets of q≥3 consecutive fixed sites contribute O(n^(1−q/2)); A cannot coexist at a shared site with a matched vertex. For finitely many selection patterns multiply the placement bounds and apply the probability bound to the union, not an independence assumption. The disjoint leading counts are n^(a+b+2c+2d)/2^(c+d), with a one-power loss for the placements intersecting distinct intervals; the joint prescription probability (f)_s ∏_{j<r}(m−2j)/(n)_(s+2r) gives the required constants, including the α=0 cases. The factorial moments determine the independent Poisson limit. E has mean fm/[n(n−1)]=O(n^-1/2); the exact bond decomposition and integer continuity interval give the deficit and zero probabilities. The four exact means follow from the same prescription formula and candidate counts, with impossible small-n or empty-matching terms zero. The unrestricted ratio comparison traverses order √n ratios bounded away from one outside an inner band, and the conditional subsequence argument establishes mixing. Separate exact brute force over all permutations up to n=8 filtered by π²=id used deletion ranks v−1{v>π(i)}, independent direct bond classification, and rational sums by f; all 1,115 involutions matched the identity and mean. The nested four-site B/C^- overlap appeared at n=4 and in all tested n=4…8 (counts 1,2,6,16,49). Frozen verifier and logs were inspected, not executed; neither small check establishes joint asymptotic independence. The replacement REVIEW.md also removes the misleading suggestion of source reconstruction: the event is only distinct outputs for a given source.

## originality

PASS

Best-of-knowledge pass reassessed for the corrected four-way conditioned limit and the resulting compound-Poisson deletion deficit. Not an originality claim for general deletion/bond equivalence, separate perfect-matching marginals, or the standalone unrestricted adjacent-swap count.

## value

PASS

The corrected theorem addresses a natural restricted-source deletion question, and explains both why the deficit is compound Poisson (paired matching mechanisms) and how fixed sites add a separate contribution at the square-root scale. It separates a joint limit from known marginals and quantifies the probability of distinct deletion outputs under two natural sampling laws. It does not assert unique reconstruction from an output.

The dated certificate retains the supplied scientific assessment, sources and limitations.
