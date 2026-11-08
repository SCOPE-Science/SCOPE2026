# Scientific review

## Correctness — PASS

For a finite irreducible positive-step Markov chain, equal sweep-start and sweep-end masses force a constant edge flux. The pre-edge mass is exactly the initial stationary mass plus the incoming flux if the predecessor was processed earlier. Solving that finite system proves the unique invariant distribution for all permutations, sizes, and positive steps. Its two-level structure gives exact total variation, and a one-variable derivative yields the sharp \(\tanh(h/4)\) envelope. Cyclic conjugacy proves exact stationarity under random rotations. Full-permutation exact rational tests through six vertices, partial seven-vertex tests, and larger envelope tests replay successfully. The finite checks are corroboration, not a substitute for the universal proof.

## Originality — PASS, with residual risk

The closest motivation is Bertazzi, Dobson and Monmarché (arXiv:2301.02537v1), with inspected full-text material on Markov splitting and invariant bias, including the introduction, Section 4 and one-dimensional explicit invariant treatment. That paper considers PDMP-based velocity-jump samplers, not directed-cycle single-edge ordered sweeps. The relevant open full text of Gourgoulias, Katsoulakis and Rey-Bellet (arXiv:1511.08240) develops long-time commutator and entropy-rate splitting analysis, not the claimed exact cyclic-ascent TV classification. Published update-schedule work identifies related ordering structures, but the accessible abstract does not resolve the exact probabilistic law. Searches for equivalent finite-state ordered-transfer formulas and dominating generic invariant formulas disclosed no decisive coverage. There remains a nonzero risk of an older specialized cyclic-update or exclusion-process result. An absence of search hits alone is not a proof of novelty.

## Value — PASS

Long-time discretization bias in Markov-chain and kinetic Monte Carlo splitting is mathematically motivated. Here all deterministic edge orders are completely classified, the uniform all-size error has a sharp closed form, and a same-cost randomized order removes that bias exactly. This gives a directly reproducible benchmark for generator splitting and a meaningful contrast between deterministic and symmetry-restored invariant sampling. The result makes no unsupported mixing-speed or arbitrary-generator claims.

## Limits and references

The conclusion is limited to unit-rate directed cycles and single-sweep edge exponentials; it does not cover unequal rates, nonlinear samplers, all finite-state Markov chains, or finite-time accuracy. The 2013 update-digraph paper is an incompletely inspected precedence risk. Core comparisons: Bertazzi, Dobson and Monmarché (2023/2025), https://arxiv.org/abs/2301.02537 ; Gourgoulias, Katsoulakis and Rey-Bellet (2015/2016), https://arxiv.org/abs/1511.08240 ; update-schedule paper https://doi.org/10.1016/j.dam.2012.12.018 .

Self-review: passed. Independent audit: not yet performed.
