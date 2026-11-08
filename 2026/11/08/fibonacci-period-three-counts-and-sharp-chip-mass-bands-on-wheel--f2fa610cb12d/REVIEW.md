# Scientific review: Fibonacci period-three census on wheel graphs

## Correctness — PASS

The stated result has a complete algebraic proof. The Laplacian argument forces a common three-step firing number, the local predecessor-neighbor inequalities enumerate all once-firing states, and the bounded coordinatewise complement enumerates all twice-firing states. The local chip-mass identity \(|E|+m(c)+\sum_v s_v\) and the independent slack intervals establish the exact support and endpoint multiplicities. A nine-state symbolic determinant is explicitly specified and checked, yielding the Fibonacci/modulo-three formula rather than extrapolating from finite data. A second finite determinant gives the inner endpoint recurrence. Independent direct update enumeration checked 649,296 bounded states for rim sizes three through six. The complete initial-state mass counts agree with separate color-word enumeration. The test at rim size three is supplementary; the claim is for rim sizes at least four.

## Originality — PASS, with specific historical-access risk

The directly relevant literature introduces parallel chip-firing, establishes general periodic firing and complementation lemmas, and proves bounds for excluded chip masses, but the inspected material does not give the exact wheel mass polynomial, its sharp parity support, or the Fibonacci count. The 2010 full preprint by Jiang treats complete bipartite/multipartite graphs, not wheels. The 2012 full preprint by Jiang, Scully and Zhang classifies possible firing *patterns* but does not count wheel initial *states*. The 2024 full preprint by Ji, Li and Wang proves a general chip-mass exclusion for period three; it does not resolve equality cases or their multiplicities. Related mass-census findings for period two, a single three-resonant cycle, and friendship graphs do not imply the wheel statements, because a wheel has many overlapping cycles and a different local constraint structure. Searches for wheel, Fibonacci and exact three-cycle counts revealed no covering source. The 1992 Bitar–Goles publisher abstract was inspected, but full text was not accessible; an equivalent formulation there or in unindexed literature remains a real priority risk. Lack of a search result is not claimed as proof of novelty.

## Mathematical value — PASS

This resolves the complete *mass-resolved* primitive-three recurrence invariant for an infinite, natural noncactus graph family with highly overlapping short cycles. The exact count is a Fibonacci expression with a genuine mod-three correction, while the minimal recurrent mass and its multiplicity undergo a sharp parity transition. An explicit nine-state transfer formula gives every coefficient, and the inner endpoints attain the general period-three excluded interval boundary with computable positive populations. The result is not a renamed special case of a known family classification and does not rest on an arbitrary finite cutoff.

## Scope and remaining risks

The result concerns initial configurations *already* of least period three, not their basins or all periods. The algebraic determinant identities are reproducible and finitely checkable; brute-force enumeration does not prove the infinite statement. The inaccessible 1992 full text and potentially unindexed wheel-specific accounts remain novelty risks. There is no independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
