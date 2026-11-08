# Scientific review

## Correctness — PASS

The domain is the product of four three-element weak-order sets and sixteen ex ante refinement vectors. In each case the algorithm compares the DA matching to the **only** other perfect matching using all four agents' original preferences; any matching that leaves someone unmatched cannot Pareto improve a full matching. The two cross-pair argument proves that failures require two or three indifferent agents. Independent complete enumeration yields the three exact coefficient classes \((c_2,c_3)=(1,2),(2,3),(3,4)\), with respectively \(10,4,2\) vectors. Their profile probabilities imply the claimed polynomials. Because arbitrary report-independent randomized policies are convex mixtures, pointwise minimization over fixed vectors is conclusive. The standalone Python checker verifies all \(1296\) cases and the stability/worker-optimality of the DA result. The polynomial identity, not numerical tests, establishes the claim for all real parameters in scope.

## Originality — PASS, with residual risk

The closest inspected sources are Erdil and Ergin (2017), especially the initial two-by-two example and the treatment of single tie-breaking in Section 5; Domaniç, Lam and Plaxton (2017), an alternative strategyproof Pareto-stable mechanism; and Kawase and Sato (2026), who motivate the deficiency of arbitrary tie-breaking and give a generalized-DA solution. The earlier single-tie-breaking concept and the possibility of inefficiency are **not** claimed new. Neither the relevant full-text sections nor the additional accessible literature comparisons supplied the exact \(t\)-dependent risk polynomials or the ex ante minimization among all report-independent policies in the stated random model. Semantic claim searches also found only related strict-preference matching enumerations, not equivalent two-sided weak-order risk. A different or previously unindexed exact enumeration remains a genuine novelty risk, so this is not an independent priority certification.

## Mathematical value — PASS

The motivating practical issue is not just whether randomly refined deferred acceptance can fail, which is known, but how the **correlation in refinements** changes failure probability, while keeping every tied participant's refinement marginal fair and report independent. The result identifies the complete optimal policy class, a strictly positive risk gap for every interior tie propensity, and an exact canonical benchmark at equiprobable weak orders. It quantifies a substantive mechanism-design choice rather than merely restating a known two-by-two inefficiency witness. The small market is a controlled structural baseline; the result does not purport to solve larger matching markets.

## Limits and sources

Only fully acceptable, complete, one-to-one, two-by-two markets under independently drawn identically distributed weak preferences are covered. Deterministic reports can be correlated with labels, but the tie-refinement policy must be chosen independently of reports. Main comparisons: Kawase and Sato (2026), https://arxiv.org/html/2610.30807v1; Erdil and Ergin (2017), https://www.isid.ac.in/~dmishra/gmdoc/indiff_match.pdf, particularly Introduction and Section 5; Domaniç, Lam and Plaxton (2017), https://arxiv.org/html/1703.10598v1. Equivalent unindexed literature and extension to larger or heterogeneous markets remain unresolved.

Self-review: passed. Independent audit: not yet performed.
