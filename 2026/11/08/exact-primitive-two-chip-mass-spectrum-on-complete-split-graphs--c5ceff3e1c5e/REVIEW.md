# Scientific review

## Correctness — PASS

The result holds for all integers \(a\ge2\), \(b\ge2\) with the stated synchronous, loopless update. The two-update graph-Laplacian kernel forces each vertex to fire exactly once on a primitive two-cycle. The four vertex-type intervals follow directly from the threshold inequalities and are independent once the firing phases are fixed. Their shifted product gives the exact polynomial. Minimizing a convex integer quadratic gives the two-region lower endpoint; chip complementation gives the upper endpoint and reflection; one minimizing phase contribution has consecutive exponents across the full interval. Boundary multiplicities follow from all minimizing phase assignments. Two separate standard-library programs checked the new claim: \(3,178,320\) literal input states on ten graphs and 132 exact parameter pairs for the polynomial, support, symmetry, endpoint and parity formulas. The finite experiments do not establish the unrestricted theorem; Steps 1–5 of the proof do.

## Originality — PASS, qualified

Primary literature read includes Jiang's full-text sections on general firing count and multipartite period possibilities (arXiv:1003.0943), Jiang–Scully–Zhang on firing patterns (arXiv:1211.6786), Levine's complete-graph activity work (arXiv:0811.2800), and the two same-graph sink-based Abelian sandpile papers (arXiv:2006.08006 and arXiv:2402.15372). These do not give this mass-resolved primitive-two count: the same-graph papers employ a sink and asynchronous stabilization, while the others do not enumerate the relevant labelled split-graph configurations. Literature and published-result searches by aliases, finite-sum parameters and stronger-coverage concepts returned no exact or dominating split-graph theorem. The 1992 Bitar–Goles article was bibliographically verified but not read in full; its public abstract concerns period phenomena in general graphs. A historical-priority risk remains, but the unresolved access is not a decisive claim-level implication. General two-step firing equality and chip complementation are acknowledged as prior mathematics, not attributed to this result.

## Value — PASS

The conserved total chip mass is the physically natural energy for a closed, fixed-energy parallel chip-firing system. The complete split graph joins two extremal interaction structures—an all-to-all clique and a totally independent shore—and is a standard, structurally nontrivial graph family. The full initial-period-two population histogram, a gapless energy interval, a sharp transition when \(b\) crosses \(a\), and exact endpoint multiplicities make the classification useful beyond knowing only which periods exist or which chip band eventually has activity one half. The \(b<a\) regime has additional balanced-phase minimizers absent from the \(b\ge a\) regime. This is a natural complete classification rather than an arbitrary isolated coefficient.

## Closest literature and limitations

The nearest general dynamical comparison is Jiang, *On the Period Lengths of the Parallel Chip-Firing Game* (arXiv:1003.0943), especially Proposition 2.5 and Sections 3–4. The nearest exact-graph comparison is Dukes, *The sandpile model on the complete split graph* (arXiv:2006.08006), which uses a designated sink and a different update process. The original Bitar–Goles (1992) full text remains uninspected; only its public abstract and bibliographic information were available. The classification concerns only initially primitive period two, not all periods, basins, or sink-based recurrence. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
