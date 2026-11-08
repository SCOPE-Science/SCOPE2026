# Review of the sunlet fastest-mixing theorem

## Correctness (PASS)
The theorem treats every integer \(m\ge3\) and every real symmetric nonnegative stochastic matrix supported on the sunlet. The objective is the spectral norm of \(P-J\), so automorphism averaging is globally valid. Fourier blocks provide a complete spectrum for invariant candidates. Strict minimization of the first positive Fourier mode supplies a universal lower bound. The proposed chain attains it because the other nontrivial eigenvalues satisfy the separate explicit inequalities in the proof. Seven exact symbolic identities, 41 full-matrix spectra, 3,280 invariant perturbations, and 770 noninvariant sampled matrices are reproduced by `verify.py`; finite calculations are supporting checks only.

## Originality (PASS, with risk)
The original general semidefinite framework [1], the full cyclic/wheel/symmetry treatment [2], the cyclic multipartite families [3], and the clique-lift treatment [4] were compared for object definitions and implication. The sunlet has two vertex orbits and one distinct leaf attached to each rim vertex; it is neither the wheel's common-hub graph nor a uniform adjacent-layer multipartite graph nor a clique lift with complete fiber-edge connection. None of the inspected treatments gives the stated sharp sunlet formula or an explicit stronger classification that directly subsumes it. Searching an indexed mathematical findings collection did not recover an equivalent assertion. An unindexed publication might still cover the formula; bibliographic priority is not independently certified.

## Mathematical value (PASS)
This solves a natural infinite family of fastest-mixing design problems in closed form rather than just describing a generic semidefinite program. The triangular core \(m=3\) coincides with a previously obtained clique-with-leaves boundary case; the new family of nonclique cycle cores is \(m\ge4\). The nonregular graph has two genuinely distinct edge classes, and the optimal rim has zero holding while the leaf transition shrinks like the inverse number of core vertices. Both the exact value and the negative-mode domination argument are necessary to prove global—not merely orbit-restricted—optimality. The asymptotic \(m^{-2}\) spectral-gap law quantifies the effect of attaching leaves.

## Closest literature and remaining scope
[1] https://doi.org/10.1137/S0036144503423264 ; [2] https://arxiv.org/abs/0709.0955 ; [3] https://arxiv.org/abs/1008.2588 ; [4] https://arxiv.org/abs/2501.02421 . The result does not address asymmetric chains, unequal stationary masses, multiple leaves, or uniqueness outside the automorphism-invariant subclass. Specialist priority uncertainty remains.

Self-review: passed. Independent audit: not yet performed.
