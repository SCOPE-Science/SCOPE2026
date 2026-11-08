# Scientific review

## Correctness — PASS

The exact symmetric-triplet decomposition places the reset vector in a dark eigenstate and a bright two-level sector. The bright high-energy leakage is at most order \(1/j\) uniformly over all evolution times, yielding an explicit stationary trace-norm bound independent of reset rate. The two-qubit Pauli tensor of the effective state has singular values \(1,h,h\), with \(h=\kappa/(1+\kappa^2)\). The Horodecki criterion, optimization of \(h\), and uniform gap separation establish the limiting Bell maximum and the rate of every maximizing sequence. A separate energy-dephasing computation establishes the fixed-finite-coupling zero-reset limit. The delivered script independently checks full spectral averaging against a direct stationary Liouville solve and executes 262 assertions. The analytic proof, not finite tests, supports the infinite limits.

## Originality — PASS (best-knowledge, priority risk)

Kulkarni–Majumdar, arXiv:2307.07485, already derive this exact stationary Ising-dimer model, investigate its strong-coupling/weak-reset scaling, and show an asymptotic concurrence peak of one-half. Neither the basic state formula, the crossover scale, nor that concurrence observation is new. The additional claim is a **uniform over all reset rates** Bell-CHSH error bound, its sharp limiting supremum \(\sqrt5\), and convergence of every maximizing reset rate to the avoided-crossing splitting. The general Horodecki criterion supplies the CHSH test but not this rate optimization. A 2026 related two-qubit study was accessible only in abstract form and remains a specific unresolved publication-priority risk; no independent novelty certification is asserted.

## Mathematical value — PASS

CHSH violation is strictly stronger than entanglement for generic mixed states. The singular regime \(r\sim\Omega^2/(2J)\) produces stationary Bell nonlocality even though the reset rate goes to zero, while the limit at fixed finite coupling is Bell-local. The forced location of every asymptotically optimal rate is a nontrivial design law for a physically motivated reset-entanglement model.

## Sources and limitations

Motivating primary: Kulkarni and Majumdar (2023), https://arxiv.org/abs/2307.07485 . Bell test: R. Horodecki, P. Horodecki and M. Horodecki (1995), https://doi.org/10.1016/0375-9601(95)00214-N . Related but incompletely inspected: Murauer et al. (2026), https://arxiv.org/abs/2610.40638 . The result concerns a two-qubit, pure-state jointly Poisson-reset steady state, ideal CHSH measurements and the strong-coupling supremum. No finite-coupling global \(\sqrt5\) bound is asserted.

Self-review: passed. Independent audit: not yet performed.
