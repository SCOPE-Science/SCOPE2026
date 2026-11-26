# Independent mathematical audit

## correctness

PASS

The scoped statement is about spanning the projection for the paper's two CSS sectors, not optimizing over all observables. Matsumoto arXiv v1 identifies this dimension in Theorem 4 (not Theorem 5 in v1), Proposition 10 and §5.3; Remark 9 distinguishes the smaller possible unrestricted count. Each erased primal edge imposes y_u+y_v=0 with missing/open vertices set to zero. The resulting relation space has one all-ones basis vector per completely retained component and none on grounded components. The binary face system is the same incidence system on faces after adding a grounded endpoint to each erased boundary edge. Thus the two ranks are the active row counts minus ungrounded component counts, including I empty, isolated dual faces, and erased edges with omitted endpoints. Removing one row per ungrounded component kills the full relation space, giving a basis of the projection and hence the exact minimum within this model. Each physical edge has at most two incident faces in the source and an erased one-face edge is closed; using local incidence with constant-time access and marking of active nodes, construction and traversal take O(1+|I|) time. The original checker was inspected, not executed; its synthetic inputs do not validate arbitrary cellulations. Independent replay python3 /workspace/branches/independent_probes.py 3: 115712 exact retained-row span comparisons on up to three edges on five labels with all omission masks, allowing parallel edges and loops interpreted as two cancelling incidences in that auxiliary graph test. This is bounded corroboration, not the proof.

## originality

FAIL

The closest decisive prior is not merely a fast decoder: Delfosse–Iyer–Poulin, arXiv:1606.07116, Proposition 4.1 proves exactly the open-vertex incidence rank by rank-nullity on any open graph, and Proposition 4.4's proof explicitly gives the closed-boundary face-row independence and any-one-omitted rule. Apply Prop. 4.1 to the erased primal graph, declaring omitted vertices open; for the dual graph attach a dummy open leaf to the unique face at each erased boundary edge. The open-graph incidence rows are exactly the two erased stabilizer matrices. Both minima then follow from Matsumoto's established rank objective. In a connected open graph the only possible dependency is the all-ones relation when unanchored, so retaining all rows on anchored components and deleting any one on others is direct. A local DFS/BFS implements the same component criterion in linear time. The measurement language and runtime are useful explicitizations but do not leave a distinct mathematical or algorithmic step under the originality standard.

## value

FAIL

Reducing the implementation cost of the paper's minimum-selection step is well motivated, but for this scoped claim the exact count and choice are given mechanically by the already available incidence results and ordinary traversal. No further structural, cost-model or algorithmic advance survives this comparison. The observation can be useful as an implementation note without qualifying as a distinct finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
