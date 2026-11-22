# Scientific review

## Correctness — PASS
For every open ladder with at least two rungs, the proof establishes that each independent dominating set has occupied endpoints, isolated vacant rungs, and alternating occupied layers. These structural conditions are both necessary and sufficient and yield unique sign/gap encodings. Every legal slide corresponds to swapping two neighboring unlike gap bits. The resulting two exclusion-token path graphs have exact vertex and edge counts; their geodesics and unique coordinatewise medians yield the distance and diameter formulas. The degenerate zero-particle and saturated-particle graphs have been addressed explicitly.

Three independent computational checks were reproduced from their supplied source and output files: original-graph bitmask exhaustion through ten rungs, independent ternary-word/gap comparison through eighteen rungs, and token-path BFS with unique median validation through eight positions. These checks do not substitute for the infinite combinatorial proof.

## Originality — PASS (with priority caveat)
Stevanović (2001) proves the total unweighted maximal-independent-set count for open ladders; this total is **not** claimed as original. Brewster, Mynhardt and Teshima (2023) develop i-graphs and classify path and cycle seed graphs but do not establish this all-cardinality two-row ladder result. The closely relevant published 2026 circular-ladder result uses related gap words for *minimum* configurations on *cyclic* prisms, and does not prove the open-ladder two-component, all-cardinality geodesic/median theorem. Hoang (2026) studies ladder graphs as *targets* of realizability, not as domination-constrained seed graphs. Searches for minimal-vertex-cover equivalences, path token swaps, broader grid theorems, and existing tables found no result entailing this exact claim. The possibility of unindexed equivalent work remains.

## Mathematical value — PASS
This solves a complete, natural family of reconfiguration graphs over *every* feasible independent-domination cardinality. The two-component invariant determines reachability; the exact distance formula gives optimal reconfiguration sequences; component medianity and the full generating functions give structural and enumerative information beyond the known scalar Fibonacci total. It extends a motivated line of research on i-graphs of paths and cycles, not an arbitrary small numerical example.

## Limitations and closest prior work
The result is restricted to open two-row Cartesian ladders, fixed-size slides preserving independence and domination. It is neither a proof about unrestricted independent-set token sliding nor an assertion about cyclic or twisted ladders. The exact unweighted total is credited to D. Stevanović, *Fibonacci Quarterly* (2001). Full relevant primary texts inspected include arXiv:2303.06299, arXiv:2303.08190, arXiv:2606.03765 and the published 2026 circular-ladder result. The originality finding is based on available scientific literature and recorded claims, not an exhaustive global priority certificate.

Self-review: passed. Independent audit: not yet performed.
