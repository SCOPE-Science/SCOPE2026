# Mathematical review: exact repeated-proposal adsorption on cycles

## Correctness

**PASS.** The first accepted deposition on a ring reduces the process to an interval with equal occupied endpoint species. With a nonempty interval of length at least two, accepted rates are \(1/2\) at each edge site and \(1\) at each strictly interior site. This leads to the exact two-boundary recurrences, the factorial difference between opposite- and equal-boundary expectations, and a solvable first-order generating-function equation. Algebraic coefficient extraction reproduces the stated finite-ring expectation, monotonicity difference, and limit. The boundary argument using strict local minima of first proposal times proves the infinite-line identification. Independent exact continuous-time state recursions and coefficient tests passed 324 rational comparisons. The finite checks are supplementary to, not replacements for, the proof.

## Originality

**PASS, qualified by historical-priority risks.** Martins, Dickman and Ziff (arXiv:2211.04622, Section V) conjectured the same finite-ring formula from numerical evidence, so the formula itself is prior. The result here proves that conjecture for every \(L\ge3\), and derives explicit generating functions for the two boundary classes and a strict factorial convergence law. Do Amaral and dos Santos (arXiv:2306.09786) treat the explicitly different one-attempt-per-site model. Penrose and Sudbury (arXiv:math/0503519) study monomer/dimer exclusion and annihilation models, not the stated two-species repeated rule at the level of their abstract. The closest prior exact repeated-adsorption results on complete multipartite graphs cover only small ring examples (not all cycles with at least five vertices). The announced, unlocated follow-up on one-dimensional adsorption remains a historical-priority risk, not proof of an earlier solution.

## Value

**PASS.** The theorem resolves a particular published analytic gap about the saturation of antagonistic adsorption on finite periodic one-dimensional lattices. The interval decomposition provides an explanatory structural reason for the unexpected alternating-factorial expression, not simply a numerical rederivation. The derived monotone, factorially rapid finite-size approach provides additional experimentally and computationally relevant information.

## Limits

Equal species proposal rates, initially empty periodic simple rings, repeated Poisson attempts and terminal coverage are required. There is no biased-rate exact formula, finite-time density formula, full blocked-site-count distribution, or independent mathematical validation in this package. The 2022 conjectural expression is acknowledged as previous literature, not advertised as a newly discovered formula.

Self-review: passed. Independent audit: not yet performed.
