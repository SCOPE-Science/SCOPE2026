# Scientific review: cyclic integer diffusion periodic-point census

## Correctness — PASS

The exact claim counts configurations already satisfying the two-step return equation, not states that merely enter an attractor. The edgewise sign-reversal lemma is proved for arbitrary finite graphs by a nonnegative dot-product identity, including ties and graphs with cycle space. On a simple ring, the local signed-gap intervals are both necessary and sufficient. Summing gaps to zero exactly enforces reconstruction of a unique integer configuration modulo translation. This proves the nine-state constant-term identity. The displayed quartic characteristic polynomial was confirmed by a symbolic exact determinant and is independently consistent with integer Newton-power-sum recurrence counts. A primitive Perron component and a strict unit-circle spectral-radius inequality give a unique Gaussian saddle with the stated coefficient, excluding spurious periodic contributions elsewhere on the unit circle. The known general period-at-most-two theorem supplies the last step from two-step-return points to *all* periodic points.

Direct exhaustive dynamics reproduced the counts for ring orders \(3\) through \(8\), restricting only to gaps within the **proved** bound of three. Independent transfer/Newton calculations agree for ring orders \(3\) through \(17\). These finite computations are checks, not an extrapolation to all ring sizes. There is no experimental substitute for the analytic asymptotic proof.

Risk: the symbolic determinant and asymptotic Perron argument remain subject to normal independent human proof scrutiny, which has not been performed.

## Originality — PASS, qualified

The foundational 2016 preprint [1] defines the rule and proves eventual periodicity on cycles, but does not enumerate the finite, translation-normalized set of configurations already periodic. The 2017 theorem [2] proves that all eventual periods are one or two and develops an edge-sign argument; its implication stops at period restriction, not the quartic enumerator or the asymptotic count. The present work makes no originality claim for the basic diffusion rule, cycle eventual-periodicity assertion, period-at-most-two theorem, or sign-reversal argument. The object-level contribution is the entire ring periodic-point count as an exact central Laurent coefficient, its two-quartic reduction, and its sharp growth constant.

Targeted literature and result-database searches used combinations of cyclic integer diffusion, two-step recurrent states, exact count sequences and spectral transfer. No accessible source giving these same formulas, or a stronger theorem implying them, was identified. The closest internal claim records on complete graphs and double-star trees do not imply the arbitrary-cycle result: one is a complete-graph enumeration (sharing only the triangle case), and the other concerns trees with two hubs. The comparisons are by graph family and invariant, not by titles alone.

Risks: absence of a search hit is not proof of priority; unindexed earlier transfer enumerations and database entries could exist. The 2017 paper provides an essential established periodicity theorem, not an independent validation of the new count.

## Mathematical value — PASS

The integer-diffusion model had a notable gap between its qualitative periodicity theorem and exact distributions of already-recurrent states. The ring is the fundamental non-tree one-dimensional family, and translation-normalized periodic-point growth is a natural invariant in dynamical systems. The result replaces an uncounted infinite family by an explicit finite transfer, an unexpected factorization into two quartics, exact primitive-two orbit counts and a universal \(n^{-1/2}\) prefactor. The square-root correction has structural meaning: cyclic gap integration imposes a zero-sum constraint on an otherwise exponentially growing local-sign language. No unrelated parameter slice or artificial finite cutoff is used.

Limitations of scope are stated in `RESULT.md`; the theorem does not enumerate transient basins, and no general-graph extension is claimed.

## Closest literature

[1] Duffy, Lidbetter, Messinger, Nowakowski, *A Variation on Chip-Firing: the diffusion game*, arXiv:1609.05792, first public September 19, 2016, especially Section 2.2 (cycle eventual periodicity).

[2] Long, Narayanan, *Diffusion on graphs is eventually periodic*, arXiv:1704.04295, first public April 13, 2017, Theorem 1.1 and its proof via a decreasing edge-sign potential.

Self-review: passed. Independent audit: not yet performed.
