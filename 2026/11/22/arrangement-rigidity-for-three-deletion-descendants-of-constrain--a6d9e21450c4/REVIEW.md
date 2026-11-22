# Scientific review

## Correctness — PASS

The precise hypothesis is a linear binary word beginning `10`, length at least three, avoiding `00` and `111`. The proof starts from a distinct-subsequence last-occurrence recursion, works with run-length indicators, derives an exact two-deletion prefix count, and then telescopes the three-deletion increments. The terms at the final two runs are explicitly retained. The Fibonacci specialization follows from the substitution's final two/three symbols, its count of `11` factors, and Fibonacci-number identities. The standalone verifier checks 612 constrained words exhaustively and independently cross-checks 15 Fibonacci depths. The finite computations do not establish the infinite theorem by themselves; the stated algebraic proof does.

## Originality — PASS (qualified)

The closest primary source, Sloane (2002), gives a general exact **two**-deletion count in Section 5 and states that the analogous three-deletion problem does not simply follow from the same derivative statistics. This result supplies a specific arrangement-insensitive **three**-deletion law on a natural run-constrained class, plus a Fibonacci specialization. Bar-Lev–Etzion–Yaakobi (2023) give bounds and extremal deletion spheres and analyze radius-one fixed-length Levenshtein balls, not the stated fixed-source formula. Public-record similarity searches did not find the exact restricted identity. Earlier unindexed or differently formulated work remains possible, especially among older deletion-subsequence enumeration papers.

## Mathematical value — PASS

The count of distinct deletion outputs measures source-specific ambiguity; it is not the number of deletion-position triples. For unrestricted binary words a simple three-deletion derivative-statistic law is unavailable in the cited foundational account. In the explicit constrained language, a cubic count unexpectedly collapses to four run parameters, and the finite Fibonacci subfamily acquires a closed all-depth expression with asymptotic density. This is a structural simplification relevant to analyzing synchronization ambiguity for run-constrained sources, not a restatement of a universal bound.

## Boundaries and risks

The conclusion is not a code-packing optimum, not a random-source law, and not valid for all binary words. Search cannot exclude an earlier equivalent specialization, including inaccessible earlier literature. All cited mathematical premises and finite comparisons are reviewed here; no external independent mathematical audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
