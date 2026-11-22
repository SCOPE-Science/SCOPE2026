# Review of the continuous spectral-order book-network theorem

## Correctness — PASS

The complete positive spectrum is established from three invariant subspaces: page fluctuations \(2x\) of multiplicity \(m-1\), the hub-symmetric contrast \((m+2)x\), and the hub-antisymmetric contrast \(mx+2y\). The strictly convex spectral trace objective and injective edge-weight Laplacian map establish unrestricted global uniqueness, rather than merely orbitwise stationarity. The full scalar derivative simplifies to an increasing sign test for \(0<c<4\), giving the exact support cutoff and optimizer; the \(p=0\) log-determinant derivative agrees with the positive-order limit. A strictly positive logarithmic lower bound proves the page-dependent direction change, and a strictly decreasing auxiliary derivative establishes the unique two-page expenditure peak. Standalone finite verification passed 13,679 assertions. Risks: the assumptions include shared spoke prices and the combinatorial Laplacian; the finite tests cannot replace the analytic quantifiers.

## Originality — PASS on examined sources, qualified

The closest published book-graph endpoint results were inspected in their full RESULT texts. The D-optimal record (2026-11-02) gives the known determinant cutoff \(4/(m+1)\); the resistance-optimal record (2026-11-02) gives the known first-order cutoff \(8(m+2)/(m^3+m^2+2m+4)\). Their claims and proofs concern those fixed objectives, not arbitrary real spectral order. Ghosh–Boyd–Saberi provides the underlying convex resistance framework, and Patterson–Bamieh provides first/second-order coherence interpretations; neither inspected primary source states the opposite page-count monotonicities or unique order-dependent two-page spending peak. This theorem does not claim its endpoint special cases as new. The main residual risk is a broader, unindexed, equivalent spectral-moment allocation result; priority requires independent assessment.

## Value — PASS

The book spine is a natural optional shortcut between two highly connected hubs. Whether a link is present at the optimum is an interpretable network-design decision. The derived continuous-order threshold shows a *direction reversal* between two pages and all larger books, while the two-page spine's expenditure share attains exactly one interior maximum at explicit prices despite declining again at high order. These are complete, sharp structural properties of a natural infinite family, not a numerical parameter slice. The formulas also quantify the page-count decay of the price threshold. Limits: this is a specific edge-cost model, not a universal principle for arbitrary network topologies.

## Closest evidence and publication limitations

References and direct full-material comparisons are in `RESULT.md`. Bibliographic searches and the known mathematical-record comparisons did not reveal an identical continuous-order theorem, but search failure is not a priority certificate. The separate observed endpoint results are credited, and an unindexed equivalent remains possible.

Self-review: passed. Independent audit: not yet performed.
