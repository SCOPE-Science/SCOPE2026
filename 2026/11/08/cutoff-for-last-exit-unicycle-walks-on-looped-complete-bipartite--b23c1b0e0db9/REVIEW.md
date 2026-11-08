# Scientific review: looped complete bipartite unicycle cutoff

## Correctness

**PASS.** The theorem concerns the rooted-unicycle state space and uniform neighbor-plus-self transition. Changing the current root arrow preserves the one-cycle property. Strong connectivity with strictly positive local transitions supplies finite irreducibility, and a self-loop state supplies aperiodicity. The predecessor counting proof independently shows the invariant counting measure. Maximal coupling of the position chains coalesces in \(O_{\mathbb P}(M)\) steps, after which a uniform two-step vertex-hitting bound erases the remaining differences in the arrows by time \((1+\varepsilon)2M\log M\). Conversely, before \((1-\varepsilon)2M\log M\), a coupon-collector lower bound leaves polynomially many arrows pointing at a fixed opposite-part vertex, which is incompatible with the stationary \(O(1)\) expectation. Exact checks confirm 12,430 finite assertions; the infinite-size conclusion follows from the proof, not from those checks.

## Originality

**PASS on inspected evidence; residual historical-priority risk.** Kaiser--Levine--Sava-Huss, arXiv:2412.13766 (first posted 2024-12-18), proves cutoff on complete graphs and explicitly asks for other graph sequences in Section 5. Its full accessible preprint (including the construction and mixing section) and corresponding journal article were compared; neither gives the looped biclique cutoff or its larger-side time constant. The earlier Anantharam--Tsoucas tree-theorem work concerns a related stationary construction, not an identified cutoff theorem; only the accessible abstract was inspected. Miller--Peres lamplighter work concerns a different memory chain and is not a direct implication. Searches of an indexed mathematical-results collection and the accessible claims of an earlier research ledger identified no matching unicycle-biclique statement. Those searches do not prove historical uniqueness; further old tree-walk and memory-chain literature could contain an equivalent general theorem.

## Value

**PASS.** The motivating paper's Section 5 explicitly asks for non-complete graph families showing unicycle cutoff. The theorem supplies one natural infinite family, including all fixed positive bipartition ratios, and calculates the precise first-order cutoff location using the larger side rather than total vertex count alone. The bipartite position chain is nearly period-two, so the proof also distinguishes rapid resolution of a slow parity mode from the much later erasure of locally stored arrows. This is a natural structural mixing result, not an arbitrary isolated finite instance or a restatement of the complete-graph case.

## Limits and literature risks

The claim assumes uniform neighbor choices, one self-loop per vertex, and a positive asymptotic lower bound on the aspect ratio. No second-order profile, periodic loop-free result, or unrestricted-graph criterion is proved. The early tree-walk primary article was available only as metadata/abstract in the current inspection; any undiscovered general cutoff theorem remains a risk. Scientific proof has not been independently verified.

Self-review: passed. Independent audit: not yet performed.
