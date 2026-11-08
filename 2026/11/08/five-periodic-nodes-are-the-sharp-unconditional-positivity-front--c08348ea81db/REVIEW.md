# Scientific review

## Correctness — PASS

The rational \([2/2]\) stability map is nonsingular for every nonnegative step on the positive-semidefinite cycle Laplacian. Direct matrix multiplication proves all listed entry formulas for cycle sizes three through five, whose numerators and denominators have the claimed signs. The cycle Green kernel has zero mean and solves the projected Poisson equation; spectral decomposition then proves the universal negative adjacent-entry asymptotic for every size at least six. The exact six-node witness and 16,391 symbolic/rational assertions corroborate but do not replace the all-size proof. The scope is uniform periodic nearest-neighbor diffusion and endpoint positivity only.

## Originality — PASS (best-knowledge, qualified)

Targeted literature and mathematical-record comparisons covered the equivalent fourth-order Gauss–Legendre/diagonal Padé formulation, general positivity and absolute-monotonicity coverage, exact graph/cycle tables, and implication by stronger schemes. The closest fully inspected general positive-system paper establishes failure mechanisms for diagonal Padé, not this positive-for-all-steps classification of periodic heat cycles. The fully inspected eight-state conservative example treats arbitrarily-small-step failure of a nonreversible pure-birth chain, not this large-step failure on symmetric cycles. The fully inspected backward-Euler-filtered Crank–Nicolson result changes the integrator. The scalar Gauss–Legendre positivity statement does not imply matrix entrywise positivity. The 2005 Padé smoothing paper and a 2026 Fokker–Planck rational-map preprint have not been ruled out by complete theorem-level full-text inspection and remain publication-priority risks. Absence of a search result is not a proof of novelty.

## Value — PASS

The result is a natural exact classification of a physical numerical maximum-principle question, not an arbitrary finite example. It identifies the last periodic grid size on which an A-stable fourth-order implicit integrator is unconditionally endpoint-positive, and proves why a strictly positive scalar stability factor is insufficient. The Green-function coefficient provides the precise geometric mechanism behind the transition and a sharp all-larger-grid negative asymptotic. This is useful as a reproducible benchmark for high-order heat-equation solvers and positivity-preserving modifications.

## Literature and limits

Relevant inspected sources include Gottlieb–Grant–Hu–Shu (2021), Zappavigna–Colaneri–Kirkland–Shorten (2012), Torlo–Öffner–Ranocha (2022), and two related published mathematical records for the Padé map and filtered Crank–Nicolson. Relevant material not fully inspectable includes the full Wade–Khaliq–Siddique–Yousuf (2005) paper and some newer Fokker–Planck rational-map results. No claim concerns internal Runge–Kutta stages, nonperiodic or nonuniform meshes, or uniform-in-grid asymptotics.

Self-review: passed. Independent audit: not yet performed.
