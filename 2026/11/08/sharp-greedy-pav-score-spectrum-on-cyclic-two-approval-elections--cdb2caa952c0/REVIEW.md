# Scientific review: sharp greedy-PAV scores on cyclic two-approval elections

## Correctness — PASS

The core identity \(F(W)=2|W|-A(W)/2\) follows directly from each two-approval voter's harmonic contribution. The cyclic bound \(A(W)\ge\max(0,2|W|-n)\) is attained by an independent set or the complement of one. Greedy's marginal is \(2-d_W(i)/2\). It therefore reaches a maximal independent set of size \(m\) in the full feasible interval \(\lceil n/3\rceil\le m\le\lfloor n/2\rfloor\), after which the \(n-2m\) two-empty-vertex gaps provide exactly that many one-neighbor moves before all remaining moves have two selected neighbors. This establishes the exact score spectrum, including all tie branches, and the sharp ratio \(11/12\). The standalone verifier directly recomputes every voter score and all tie paths and optimum committees for sizes \(3\le n\le15\), assessing 9766 reachable states. Infinite-order conclusions rest on the proof, not the test.

## Originality — PASS on available evidence, with residual risk

Janeczko–Faliszewski (arXiv:2305.01769v1) already use graph-edge candidates and endpoint voters and provide the graph-reduction setting. This underlying construction is known. Their full text develops tie counting and #P complexity, not the **exact cyclic PAV score spectrum** or the **sharp tie-breaking-sensitive \(11/12\) welfare guarantee**. The 2026 structured-election algorithm of Lassota–Sornat obtains optimum Thiele committees for candidates with at most two approving voters, which includes this class, but does not bound sequential greedy committees or enumerate possible greedy objective values. The classical independent domination number for cycles is also known. Mathematical-record searches for cyclic two-approval greedy PAV, exact score spectra, the \(11/12\) factor and graph-language reformulations returned no dominating claim. Distinct social-choice records on tournament rules or partitioned clone voters do not imply these assertions. An unindexed equivalent in greedy graph-dominating-set literature remains a real priority risk. The searches are not interpreted as a proof of uniqueness.

## Value — PASS

Sequential PAV is a natural and widely used procedure, and ties in its marginal choices matter substantially. Two approvals per voter on a cycle is a basic sparse structured election. An exact description of the **whole** tie-dependent welfare spectrum, not just its minimum, quantifies a sharp quality-of-outcome risk and improves the general monotone-submodular approximation guarantee for this nontrivial class. The ratio's equality family occurs at every size divisible by six, so it is not an isolated microexample. The formula also isolates the structural culprit: small maximal independent sets rather than arbitrary tie artifacts.

## Closest literature and limitations

Closest primary source: P. Janeczko and P. Faliszewski, *Ties in Multiwinner Approval Voting*, https://arxiv.org/abs/2305.01769 (definitions, graph-based reduction and tie count). Broader optimization source: T. Lassota and K. Sornat, *Algorithms for Structured Elections under Thiele Voting Rules*, https://arxiv.org/abs/2607.28575 (candidate approval degree at most two, polynomial optimization, not sequential score spectrum). General PAV setting: T. Masařík, G. Pierczyński and P. Skowron, https://arxiv.org/abs/2307.06077. Classical independent-domination facts are credited. Scope is limited to unit voter weights, a single cyclic two-approval incidence graph, fixed committee sizes, harmonic Thiele scores and possible greedy tie branches. The enumerator confirms only cycle sizes through 15. No external independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
