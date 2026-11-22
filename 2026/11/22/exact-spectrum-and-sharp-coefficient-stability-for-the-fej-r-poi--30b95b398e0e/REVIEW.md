# Mathematical review

## Correctness — PASS

The Fourier coefficient expansion gives the exact slack matrix \(H_n\). A direct second-difference calculation and the two reflection boundary conditions verify every eigenpair; counting \(n+1\) distinct modes proves completeness and gives the sharp smallest positive eigenvalue. This supplies a complete all-degree proof rather than extrapolation from finite tests. The included standard-library checker passed 421265 exact-rational and numerical supplementary assertions.

## Originality — PASS relative to checked sources

MacDonald, arXiv:2611.05363 (2026), proves the underlying pointwise inequality and a partial-sum squares identity, as inspected in the full paper; the proof does not state the entire slack spectrum, parity-dependent sharp coefficient-distance constant, or unique soft eigenmode. Ruzieh and Powers (1990) diagonalize the *unmodified* path distance matrix, whereas the current matrix has a noncommuting all-ones correction. Targeted published mathematical record searches found no equivalent or dominating coefficient-stability result. A disguised older discrete Green-kernel or Brownian-bridge formula remains a bibliographic priority risk.

## Value — PASS

The new quantitative lower bound turns a qualitative equality classification into sharp, all-degree stability in the natural Euclidean metric on Fejér–Riesz factors. Its exact soft modes reveal which coefficient perturbations are hardest to detect, with an even/odd switch and degree-dependent decay. This is a motivated stability invariant, not an arbitrarily chosen coefficient or finite test case.

## Limits

The result does not establish factor-independent function-space stability or solve the Krzyż conjecture. The standalone code is supplementary, not an infinite-degree certificate. Earlier equivalent formulas under another spectral terminology cannot be ruled out exhaustively.

Self-review: passed. Independent audit: not yet performed.
