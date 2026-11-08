# Scientific assessment

## Correctness — PASS

The finite Markov process is specified by open-neighborhood majority and independent fair ties. Corner states are precisely the three closed recurrent classes (two singleton consensus states and one blinking pair); all remaining states hit these classes almost surely. The first-step recurrence separately treats the two single-tie cases and the double-tie case, including the zero-round boundary at corners. Explicit solution yields the exact expected time from each initial coloring. Exact-rational Bellman checks test all count states for sizes through eight. The global bound is not extrapolated from a finite search: a central-binomial inequality and an order-preserving Bellman supersolution control every size at least 42; exhaustive arithmetic certifies the remaining 400 even-by-even cases. The equality cases are checked exactly. The bound concerns expectation, not a pathwise cutoff.

## Originality — PASS (best-knowledge priority)

The closest directly relevant primary paper is Zehmakan (2023), arXiv:2302.06760v1, and its expanded 2024 journal article. Their general exponential stabilization example, cycle-specific bounds, and absorbing-component framework do not give the exact complete-bipartite formula or the sharp constant attained at \(K_{2,6}\). The published majority-dynamics results for dense random graphs concern a different graph ensemble and deterministic tie retention. Targeted mathematical-record and literature searches for equivalent formulations, global bounds, graph-specific tables, and broader theorems located no result implying the claimed constant. A less visible equivalent computation remains a priority risk.

## Value — PASS

The initiating literature shows exponential stabilization in general and polynomial behavior on cycles, prompting structural questions about which graph topologies stabilize rapidly. This theorem produces an exact all-initial-state law for an important two-community network family, a **size-independent sharp universal expectation**, and the nonmonotone extremizer \(K_{2,6}\), not the smallest balanced biclique. The interaction of tie-retention probability and immediate monochromatic absorption explains that unexpected finite-size optimum. This is a motivated structural boundary rather than an arbitrary example or a routine restatement of a general Markov-chain formula.

## Closest literature and limitations

Sources: Zehmakan (2023), arXiv:2302.06760v1 (Sections 1–4 and appendix context); Zehmakan (2024), DOI 10.1007/s10458-024-09651-y (full open-access article, especially Sections 2 and 4); Fountoulakis–Kang–Makai (2020), DOI 10.1002/rsa.20970 (different tie rule). No claim is made for other networks, other tie biases, or deterministic sample-path bounds. Independent external validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
