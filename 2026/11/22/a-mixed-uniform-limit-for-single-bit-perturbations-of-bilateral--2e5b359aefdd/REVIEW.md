# Scientific review

## Correctness (C) — PASS

The binary adjacent-change variables are independent Bernoulli variables, so toggling one interior bit produces either an unchanged run skeleton or a change of exactly two runs. In the unchanged-skeleton case only two run-pair tokens can change. In the changed-skeleton case, comparing the ordered runs from both ends shows that, away from bounded exceptional depths, the affected run indices differ by two and the other paired side is unchanged. The two-step run-length mismatch indicators are stationary and two-dependent with exact mean \(2/3\), giving the uniform interval strong law. The run count is asymptotically \(n/2\), and the randomly chosen run index is asymptotically one-half its source position. Together these independently establish the mixed limit and mean \(1/24\), with the bounded token count giving uniform integrability. An independent pair of token constructors matched for all 32,766 binary words through length 14. An exhaustive test of 360,456 directed interior flips verified the skeleton-preserving bound; finite Monte Carlo diagnostics support but do not establish the infinite theorem. The critical run-index shift and terminal exceptions are written explicitly in RESULT.md.

## Originality (O) — PASS, with residual historical-priority risk

The initial run-pair construction and run-preserving locality are in Konstantinovsky and Yaari, arXiv:2604.26190, original public submission on 2026-04-29, Sections 6.1 and 6.4. Their discussion allows realignment after changing the run skeleton but gives neither this depth-aligned random-edit statistic nor its mixed limiting law and mean constant. Checks for aliases such as bilateral run peeling, one-edit token mismatch, random bit flip, and edit sensitivity found no claim that covers the stochastic theorem; nearest indexed mathematics involves different deletion-channel statistics. The stochastic claim is not a renamed deterministic corollary: it requires a renewal comparison frequency, global interval control and random-location asymptotics. Nevertheless, an unindexed equivalent result or an unnoticed stronger version in related literature is possible, so historical uniqueness is not certified.

## Value (V) — PASS

The motivating reversible representation advertises strong locality when run symbols are preserved while acknowledging deeper realignment for a character edit. This theorem quantifies that substantive boundary: exactly half of uniformly selected interior flips are asymptotically negligible on the linear scale, while the other half produce a continuous macroscopic fraction of changed tokens. The compact law gives a meaningful stability benchmark for using the transform as a compressed mutable representation, and explicitly distinguishes rewrite sensitivity from token edit distance.

## Limits and closest literature

This is an i.i.d. fair-binary, one-interior-flip, depth-aligned result; extending it to arbitrary alphabets, nonuniform sources, optimal sequence alignment, multiple edits or worst-case bounds is unproved. The closest primary source is T. Konstantinovsky and G. Yaari, *Flashback: A Reversible Bilateral Run-Peeling Decomposition of Strings*, https://arxiv.org/abs/2604.26190, especially Sections 6.1 and 6.4. Finite exhaustive tests cannot substitute for the proof of asymptotic mixing. External expert validation and a definitive claim of publication priority have not been obtained.

Self-review: passed. Independent audit: not yet performed.
