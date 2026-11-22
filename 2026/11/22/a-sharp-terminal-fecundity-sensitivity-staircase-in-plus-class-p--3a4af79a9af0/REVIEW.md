# Review of terminal-fertility sensitivity staircase

## Correctness
PASS. The proof uses a simple positive Perron eigenvalue and its perturbation formula. A ratio of consecutive coordinates of the right Perron vector yields the exact comparison for every age, including the terminal retention denominator. Strict monotonicity of the scalar characteristic relation and of each crossing function proves uniqueness, ordering, equality cases and sharp necessity/sufficiency for the complete staircase. The packaged standard-library checker independently evaluates finite differences and frontiers; it is diagnostic, not a proof.

## Originality
PASS on accessible comparisons, with residual priority risk. Carslake et al. (2009), Table 2, state a simulated partial ordering (S2), not a complete terminal sensitivity classification or sequential crossing budget. Giaimo and Traulsen (2021) prove elasticity-flow inequalities, a distinct derivative normalization, not these absolute sensitivity thresholds. Giaimo and Traulsen (2022) treat age-specific perturbations within stage-structured models; those do not state the finite-class terminal fertility budget staircase. Generic Perron sensitivity and stable-stage distribution formulas are well known, and may make the result accessible as a consequence without the explicit claim being named. This is a precise risk, not a claim of exhaustive historical priority.

## Value
PASS. The exact feasible boundary \(\prod_{i=1}^{n-1}s_i>1-t\) separates life histories in which terminal-class fertility can ever dominate all younger-class absolute fertility sensitivities while population growth exceeds replacement. The full ordered crossings supply a parameter-free ranking protocol for a natural type of age-class projection with terminal survival; they refine a published numerically identified sensitivity rule. The finding is not presented as an empirically calibrated management recommendation, and no downstream theorem is needed for this finite structural classification.

## Closest literature and scientific limits
The closest reported sensitivity claim is S2 in Carslake et al. (2009). A 2021 general theorem covers elasticity identities but not absolute sensitivity rankings, and the 2022 stage-age analysis describes a different perturbation axis. Older Leslie eigenvector and sensitivity references remain a historical-priority caveat. The linear projection, independent absolute perturbations, fixed positive survival, and terminal-only fertility family limit practical application.

Self-review: passed. Independent audit: not yet performed.
