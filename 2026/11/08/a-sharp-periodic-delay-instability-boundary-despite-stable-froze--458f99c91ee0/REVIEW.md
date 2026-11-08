# Scientific assessment

## Correctness — PASS

The exact stagewise recurrence is reconstructed from [1, Eq. (29) and Section 4.3]. Its five-dimensional period-three product has exact characteristic factor \(z^2p_\mu(z)/27000\), with the displayed cubic verified by standalone symbolic computation. Schur reduction gives five necessary-and-sufficient inequalities; all but the sign of \(-p_\mu(-1)\) hold uniformly for \(-1<\mu<1\). The critical point is an exact, simple \(-1\) eigenvalue; below it a real multiplier is strictly smaller than \(-1\). An independent Rouché argument proves the frozen-recurrence claim for every constant integer delay, and a Halanay comparison proves continuous-variable-delay stability. No finite experiment is promoted to an infinite proof.

## Originality — PASS (best-knowledge, priority qualified)

[1, Theorem 3.8] proves unconditional stability for a fixed delay; [1, Section 4.3] warns that nonautonomous products require stronger certificates, but provides no exact three-phase switching frontier. The present exact cubic, rational threshold and physical-versus-discrete stability separation are not a restatement of that warning. Koto [2] and Watanabe–Roth [3] address related IMEX and delay stability, but the accessible abstracts and source descriptions do not establish the specified stage-dependent periodic result. Relevant published mathematical-search matches concerned other periodic recurrences or delay-system crossings; no identified result directly implied the fixed coefficient cubic threshold. Historical-priority risk persists because some earlier papers' complete text was not accessible or inspected.

## Value — PASS

The natural three-phase delay pattern forces a repeated held sample followed by a three-step jump, making a minimal, directly reproducible stress test of the source's variable-delay caveat. It yields a sharp, nontrivial internal frontier where all frozen discrete problems and the exact continuous DDE are still exponentially stable, quantifying when product-level certification is indispensable. The result is a genuine parameter-complete structural boundary for the specified method, not a tiny numerical improvement or arbitrary table entry.

## Limits and closest literature

The theorem is not a claim of unconditional failure for all variable delays or all step sizes. The published general frozen-delay theorem remains valid. The exact classification is restricted to \(\beta_0=4/5\), \(h=1\), negative real coefficient \(-5\), and the periodic delay pattern. The main residual risk is an earlier general numerical-stability theorem that already implies this specialization. Source [1] was read in relevant full-text sections; [2] and [3] could be compared only from abstracts, so their full-text coverage is not certified.

Self-review: passed. Independent audit: not yet performed.
