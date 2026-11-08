# Review of the smallest-part two-leader theorem

## Correctness
PASS. The grounded-Laplacian block decomposition is exact for every complete multipartite graph. Sherman–Morrison gives the general inverse-trace formula. The same-part objective is increasing in part size, while the mixed-versus-same difference has an explicitly positive rational numerator with a five-term coefficient certificate. Exact-rational direct inverse tests (3,322 cases) and a 729-point rational-identity grid pass. The theorem is restricted to at least three parts, each of size at least two, and exactly two noise-free leaders.

## Originality
PASS on inspected evidence, subject to the stated literature risk. The 2013 algorithmic paper [1] formulates the same objective but gives neither the exact unequal multipartite placement nor its strict comparison formula. The 2014 joint-centrality paper [2] gives a graph-general equivalent optimization criterion but explicit examples concern paths/cycles rather than this unequal family. Accessible prior findings for complete bipartite and balanced complete multipartite networks have different quantified graph domains and do not imply the unequal at-least-three-part theorem. Indexed semantic results did not expose a stronger claim containing it. Unknown equivalent literature is a residual priority risk; this is not an independence or publication certification.

## Value
PASS. This is a complete classification of a natural two-input A-optimal control problem on heterogeneous dense-community networks. It has an exact optimizer count and closed objective, and proves the counterintuitive placement rule that both leaders are nonadjacent and lie in a *smallest* part rather than being spread over communities. The restriction to at least two vertices per part isolates a meaningful structural regime.

## Closest primary literature and limitations
[1] https://arxiv.org/abs/1302.0450 (noise-free inverse-trace objective and general algorithms). [2] https://arxiv.org/abs/1407.1569 (joint centrality and explicit path/cycle cases). [3] https://viterbi-web.usc.edu/~mihailo/papers/farlinjovCDC11.pdf (earlier convex-relaxation methodology). Unindexed equivalent statements cannot be excluded. The theorem does not cover singleton parts, larger budgets, or variable edge weights.

Self-review: passed. Independent audit: not yet performed.
