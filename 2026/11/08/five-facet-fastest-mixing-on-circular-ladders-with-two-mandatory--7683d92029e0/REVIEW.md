# Scientific review: two-floor fastest mixing on circular ladders

## Correctness — PASS

The claim specifies every integer \(m\ge4\), all feasible individual rim and rung edge floors, symmetric stochastic matrices, and the SLEM objective. Dihedral-plus-layer symmetrization establishes that the global optimum is achieved within the two-weight class. Fourier decomposition then reduces the optimum to three inequalities. Five explicit necessary lower bounds coincide with a constructive feasible choice because \(a+b>4\). The proof also gives strict examples for each essential active bound and distinguishes the redundant even-cycle bound. The self-contained `verify.py` passed 1,323 exact-arithmetic feasible parameter pairs, 150 full-matrix spectral mode checks, and explicit facet witnesses. Finite tests are corroboration, not the proof of the all-size theorem.

## Originality — PASS on inspected evidence

Closest antecedents: Boyd, Diaconis and Xiao (2004), DOI 10.1137/S0036144503423264, supply the universal FMMC SDP; Boyd, Diaconis, Parrilo and Xiao (arxiv:0709.0955v1, 2007; journal 2009), §§2–3, supply automorphism averaging, product eigenvalues and unconstrained closed examples. The same-object spectrum paper by Raza et al. (DOI 10.3934/math.2023137) computes unweighted prism graph spectral invariants, not optimized transition probabilities. Jafarizadeh (arxiv:2501.02117) studies fixed probability tradeoffs on friendship graphs. The inspected sources do not state or imply the complete **two-pointwise-floor prism value function** and its parity-sensitive active facets without additional parametric optimization. Equivalent formulations and stronger general frameworks were compared, not merely titles. Residual risk: an unindexed thesis or other specialist paper may have independently classified this exact constrained product problem; independent priority assessment is unavailable.

## Mathematical value — PASS

Two floor constraints encode independently mandatory movement along circular layers and across the layer-connecting rungs. Exact sharp optimization for every network size and feasible pair gives an implementable mixing design rather than only a numerical SDP. The existence of five essential linear pieces on odd cycles, but only four on even cycles, exposes an interpretable spectral parity effect. The scope remains symmetric chains and asymptotic SLEM, not arbitrary chains or a guarantee on finite-time total variation.

## Limits and provenance

Verification used the embedded exact checker after reconstructing the analytic argument. No external independent mathematical review was performed, and the inspected-source originality comparison is not an exhaustive global literature certification.

Self-review: passed. Independent audit: not yet performed.
