# Review of the finite erasure-capacity theorem

## Correctness — PASS

The graph reduction is exact because a known-position erasure yields the same received word from two distinct inputs if and only if those two inputs differ only in that position. The source set is exactly the enumerated set of three-symbol words with no equal adjacent symbols. The claimed bounds do not rely on software-reported optimum values: each listed odd cycle contributes at most its floor-half vertex count to any independent set, and each paired edge at most one. Certificate files cover all admissible states without overlap. Separate explicit independent-word lists meet the upper bounds, establishing both equalities. `verify.py` and `alternate.py` were executed successfully against the same on-disk certificates, checking every critical edge, output, and set membership. Limit: neither verifier establishes a general odd-length formula.

## Originality — PASS, qualified

The closest inspected primary result is Choo–MacGillivray (2011), Theorem 5.5: the same three-coloring graph is Hamiltonian for all the relevant paths. This gives an upper bound of half the vertex count but neither its exact independence number nor the exhibited odd-cycle partition. The length-seven maximum \(92\) is strictly below their implied bound \(96\), and the analogous length-five maximum \(23\) below \(24\). Benerjee–Banerjee (2023) uses the exact homopolymer-free Hamming-code setting but provides broad analytic bounds rather than this sharp pair. Haas–MacGillivray (2018) studies canonical, color-quotiented reconfiguration graphs, not these fully labeled graph vertices. Targeted research-record searches and the accessible existing claims revealed no equal or stronger result. Novelty is qualified because undocumented prior finite computations or unindexed datasets might exist; searches alone cannot certify priority.

## Mathematical value — PASS

This is a natural exact finite capacity problem for a run-constrained source and a position-revealed erasure, as well as a finite independence-number problem in a well-studied recoloring graph. The length-seven result replaces a classical Hamiltonicity-derived 96-word upper bound by a sharp 92-word theorem and reveals a concrete odd-cycle obstruction. The 21-cycle partition gives an independently checkable combinatorial proof certificate that can benchmark future constrained-code optimization and recoloring-graph research. This is not offered as an asymptotic advance or as a solution to unknown-location synchronization.

## Sources and remaining scientific risks

Full text: Choo and MacGillivray, *Gray code numbers for graphs* (2011), Theorem 5.5 and the defining section of the three-coloring graph, https://scispace.com/pdf/gray-code-numbers-for-graphs-3yxrthhv40.pdf . Full text: Benerjee and Banerjee, *Bounds on Size of Homopolymer Free Codes* (2023), Definitions II.1 and the bound discussion, https://arxiv.org/abs/2305.10741 . Full text: Haas and MacGillivray (2018), the definition of canonical colorings and main objectives, https://www.mdpi.com/1999-4893/11/4/40 . The primary residual scientific risk is previously unindexed enumeration of the same small graph invariant. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
