# Scientific review

## Correctness — PASS

For a fresh local-time threshold on every reset, the no-reset absorption Laplace transform from each gate state factorizes into one gate-specific open-boundary hitting transform and the *same* reaction-threshold transform. The conditional gate-at-reset kernel follows from killing in the open gate and a two-state resolvent. Exact matrix reduction gives the claimed distribution-invariant delay with strict positivity. A standalone checker verifies the symbolic reduction and reproduces independent Robin backward-equation discretizations. Numerical checks do not prove the all-threshold-law result; the strong Markov factorization and matrix identity do.

## Originality — PASS, qualified

The **perfect open-gate absorption** comparison is fully covered by Mercado-Vásquez and Boyer (2021), Appendix B Eq. (49), and is not presented as new. Bressloff (2022) covers arbitrary open-gate surface-contact threshold laws when the *gate also refreshes* at resets; the different literature on local-time resetting versus retention does not compare the two gate-memory protocols under renewed threshold progress. The added claim is the **same exact delay across every independently refreshed threshold law**. The strongest identified coverage and the possibility of a dominating abstract renewal identity are expressly acknowledged; publication priority has not been independently audited.

## Mathematical value — PASS

A natural biochemical model separates conformational memory of a stochastic target from finite or nonexponential chemical-contact requirements. The established universality shows that the latter can change both mean reaction times arbitrarily while leaving the specific gate-memory penalty unchanged. It is a full, physically motivated independence principle over an infinite-dimensional family of reaction laws, not an arbitrary parameter evaluation.

## Boundaries and prior work

The theorem requires stationary two-state gate initialization, a half-line reflected diffusion, positive rates, Poisson resets, and *refreshing all contact progress at every reset* in both protocols. It does not compare systems that retain their local-time progress, general reset clocks, or full reaction-time laws. Closest inspected primary works are arXiv:2107.02148 (the already known instant-reaction delay), arXiv:2205.13985 (general reaction thresholds under complete renewal), arXiv:2203.04868 (threshold memory and resetting), and arXiv:2009.02739 (original renewed-gate protocol). Independent review remains needed.

Self-review: passed. Independent audit: not yet performed.
