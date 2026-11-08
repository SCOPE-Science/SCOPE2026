# Scientific review

## Correctness — PASS

Two complete sweeps are rank-one maps \(cvu^{\mathsf T}\) and \(cuv^{\mathsf T}\). Their repeated/switching squared-norm factors are exactly \(c^4\) and \(c^2\), respectively. Tracking the random last-sweep type produces a positive 2-by-2 transfer matrix. Its trace/determinant yield the claimed eigenvalues. Perron positivity proves the exact asymptotic rate for every nonzero deterministic initial error; row-sum symmetry yields the finite-horizon fair-mixing law. Boundary cases and finite verification are explicitly separated. Exact rational enumeration reproduced the stated transfer identities.

## Originality — PASS, with specialist precedence risk

The all-bias, complete-sweep permutation distribution differs from single-row independent random sampling in Steinerberger (2020) and from randomized block-averaged projection in Necoara (2019). Their accessible full texts were examined for definitions, theorems and implications; neither asserts the 2-by-2 complete-sweep transfer law. Bai–Wu's exact mean-square calculations concern the independently sampled Kaczmarz model, not full two-row permutations. Older two-projection random-product theory and inaccessible detailed row-reordering analyses remain residual risks; the result should not be treated as independently certified novelty.

## Value — PASS

It gives a complete sharp classification of a natural minimal random-reshuffling model: the same pair of equal-cost convergent sweeps is strictly slowed by any nontrivial mixing, with a unique worst bias and an unbounded relative slowdown near orthogonality. This provides a diagnostic counterexample to the assumption that repeated order randomization necessarily improves cyclic projection methods, without extrapolating to larger systems.

## Sources and limits

Necoara, https://arxiv.org/abs/1902.09946; Steinerberger, https://arxiv.org/abs/2007.02910; Bai–Wu, https://doi.org/10.1016/j.laa.2018.05.009; Kaczmarz anomaly in tomography, https://www.mdpi.com/2673-9909/2/2/12. Exact arithmetic only; no proof for more than two rows, independent per-row sampling, noisy equations, floating point, or almost-sure error rates.

Self-review: passed. Independent audit: not yet performed.
