# Scientific review

## Correctness — PASS

The final theorem concerns the complete Krawtchouk sign interpolant on \(2m+1\) consecutive integers and the limit at points \(m-u\), including \(u=t/\log m\). The derivation reconstructs the paired Lagrange basis, the exact Gamma product, the alternating-sum normalization \(-1/4+O(m^{-1/2})\) and its uniformity via third finite differences. Uniform Gamma ratios then give the two moving-edge formulas. The lower bound follows from one admissible evaluation point; no global extremality is assumed. `checker.py` independently confirms finite exact interpolation formulas and the first alternating moment, with 202 successful tests. The central nonstandard step is the alternating-third-difference estimate in the proof, not numerical extrapolation.

## Originality — PASS relative to identified sources

The March 5, 2026 Cullinan–Young article proves the polynomial-interpolation identity and the derivative limit at the fixed origin; its reported overshoot data are on the first lobe. The most directly related published published-finding corpus result, *The exact limiting Gibbs overshoot for Krawtchouk interpolation of the sign function*, proves locally uniform convergence on fixed compact sets and its limiting profile, but explicitly does not study finite-degree maxima on growing intervals. Its full `RESULT.md` was read. The new claim is not a corollary: fixed-window convergence cannot bound, let alone calculate, a moving point \(m-t/\log m\). General classical Runge divergence and Lebesgue-constant estimates do not give the sharp asymptotic for these particular sign samples. Search comparisons also included aliases involving equispaced step interpolation, endpoint amplification and the logarithmic boundary layer. Residual priority risk: an older specialist treatment of the same step-interpolation boundary layer might have escaped discovery.

## Mathematical value — PASS

The source's near-origin Gibbs phenomenon is compatible with a vastly different response on the full interpolation interval. The theorem quantifies this contrast with a universal, positive and sharply maximized \(t e^{-t}\) edge profile and an explicit exponential lower bound. It is an infinite-family stability statement for an established Fourier-orthogonal polynomial construction, not an arbitrary sample count or a recomputed first-lobe table. The claim intentionally leaves the complete global supremum and uniqueness of its location unproved.

## Closest literature and limits

- J. Cullinan and E. Young, *The Gibbs phenomenon for the Krawtchouk polynomials*, https://arxiv.org/abs/2603.05408, especially its interpolation identification, fixed-origin derivative and overshoot table.
- *The exact limiting Gibbs overshoot for Krawtchouk interpolation of the sign function*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-exact-limiting-gibbs-overshoot-for-krawtchouk-interpolation--95d6218c0f0c. Its fixed-compact convergence and first-lobe maximum are prior work.
- NIST DLMF, §3.3, https://dlmf.nist.gov/3.3, for standard equispaced Lagrange cardinal weights.

The finite checker is not a proof of the asymptotic theorem. There is no independent mathematical audit, no global upper bound, and no global optimizer classification.

Self-review: passed. Independent audit: not yet performed.
