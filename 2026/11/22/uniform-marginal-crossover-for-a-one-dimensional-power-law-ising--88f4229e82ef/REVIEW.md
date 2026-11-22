# Scientific review

## Correctness — PASS

The claim is restricted to the energy maximum along finite contiguous intervals in the infinite one-dimensional Ising chain. Exact broken-bond counting gives the energy; strictly decreasing differences determine the maximizing length to \(O(1)\) uniformly near the marginal exponent. Uniform Euler--Maclaurin expansion and stationary-point cancellation reduce the optimum to \(\zeta(\sigma)-x_*^{1-\sigma}/(\sigma-1)\). The Laurent pole and exponent-dependent term cancel uniformly through \(\sigma=1\), leaving both \(\ell\Phi(\lambda)\) and the finite part \(\gamma-\lambda e^{-\lambda}\). The packaged reproducibility checker passed 159 finite consistency assertions. Numerical checks alone do not certify an infinite limit.

## Originality — PASS (qualified)

The strongest direct literature is the 2019 one-dimensional long-range Ising nucleation analysis and the 2026 work of Batini, Pagni and Defenu, which provides the exact one-droplet energy and fixed-exponent barrier scaling. The 2025 apparent-bistability paper motivates the near-marginal interaction physics. None of the inspected material states the compact-window \((\sigma-1)\log(2J/h)\) energy-barrier expansion with the bounded \(\gamma-\lambda e^{-\lambda}\) correction and uniform error. The already known exact finite-droplet energy is an essential input; a different classical analysis may implicitly contain the evaluated two-parameter limit. This is a live priority risk, not a proof that a literature search establishes novelty.

## Value — PASS

The interaction-decay threshold is physically significant because the fixed-exponent barrier changes between diverging, logarithmic, and finite behavior. Individual fixed-exponent expansions are not uniform when the exponent is tuned toward the boundary as the field decreases. The explicit crossover and order-one correction resolve this singular parameter layer at the energy level, allowing consistent comparison near the boundary without extrapolating invalid fixed-exponent formulas. The result is not a dynamical exit-time theorem or an entropic nucleation prefactor.

## Sources and limitations

Primary motivating source: Lazarides and Pizzi (2025), arXiv:2506.10068, initial version dated 11 June 2025. Related sources: van Enter et al. (2019), DOI 10.1007/s10955-019-02238-y; Batini et al. (2026), arXiv:2611.25764 (19 November 2026). See RESULT.md for exact hypotheses and references. The main residual risks are implicit asymptotic coverage of the evaluated marginal limit and physical use outside the infinitely extended, contiguous-droplet setting. The analytical and finite-check evidence is same-model only.

Self-review: passed. Independent audit: not yet performed.
