# Self-review

## Correctness — PASS

The statement is for a fixed capture level, a fixed nonzero adaptation rate and a fixed initial coupling. The original reduced phase equations agree with the originating work's equations (15a,b). The change of variable \(v=1+\cos\varphi\) gives the exact logistic-coupling ODE, whose invariant strip and bounded coupling imply convergence to the synchronized end state for every non-antipodal initial phase. The reciprocal integrating factor \(H=e^{-2\kappa/\epsilon}/v\) has exact derivative \(-(2-\kappa)e^{-2\kappa/\epsilon}\). Integrated logit and quadratic-coupling balances respectively give the sharp \(\tfrac12\log(1/v_0)\) term and a uniform bound on the squared-coupling integral. These identities control the Taylor remainder for a passage interval of diverging length and prove both asymptotic coefficients. The three symbolic identities and the event-driven integration checks in `check.py` passed. Finite numerical tests are ancillary, not infinite-time certification.

## Originality — PASS within inspected evidence

Jüttner–Martens (arXiv:2209.10514, *Chaos* 33, 053106) is the source of the adaptive oscillator equations. Its accessible full open-access text was read for the symmetric reduction, stability and bifurcation treatment, and the discussion of bistability. Those portions identify the locked-state structure but do not supply the asserted first-passage formula, the exponentially weighted initial-coupling amplitude, or the finite-rate logarithmic coefficient. Related adaptive-coupling synchronization papers (Ha–Noh–Park 2016; Ha–Lee–Li–Park 2018) concern alternative feedback rules and qualitative synchronization/singular limits, according to accessible abstracts; these are not sufficient to imply this exact formula. Published findings about discrete sine-map antiphase criticality are structurally different and do not imply the continuous adaptive two-dimensional law. The full texts of the two SIAM related papers were not verified, and mathematically equivalent unindexed treatments remain a residual priority risk; the present literature assessment is not a proof of uniqueness.

## Mathematical value — PASS

At the natural loss-of-antipodal-locking boundary, local linearization has a zero eigenvalue and does not determine how near-antipodal states cross to synchronization. An exact physically interpretable passage law establishes a universal critical exponent, an initial-coupling-dependent leading coefficient, and a nontrivial timescale-dependent logarithmic correction. This relates finite learning speed to long observed synchronization delays and distinguishes trajectories with the same arbitrarily small initial phase defect but different initially stored coupling. It is a motivated sharp dynamical invariant, not merely a computation of stability signs or a generic saddle-node normal form. The result is limited to the stated symmetric identical-frequency critical slice, with no claim for adaptive networks of arbitrary size.

## Closest literature and unresolved limitations

- Jüttner and Martens, https://doi.org/10.1063/5.0133190, open-access full-text equations (13)–(15), stability analysis, and discussion inspected.
- Ha, Noh and Park, https://doi.org/10.1137/15M101484X, and Ha, Lee, Li and Park, https://doi.org/10.1137/17M1124048, accessible abstracts checked; no whole-article negative-coverage assertion is made.
- Related indexed critical two-clock sine-map work concerns discrete nonadaptive maps; equal inverse-power scaling alone is not statement coverage.

Self-review: passed. Independent audit: not yet performed.
