# Scientific review

## Correctness — PASS

The theorem covers all even orders \(n=2m\ge4\), all budgets \(B>0\), all matching-price premiums \(r>1\), and all observation horizons \(t>0\). Strict convexity of \(\operatorname{tr}e^{-tL}\) as a function of the independent conductance variables gives unrestricted uniqueness; this is stronger than simply averaging over the cost-preserving automorphism group. The pair-antisymmetric and pair-constant subspaces give the complete exact spectrum. Substitution into the trace, positive scalar second derivative, and exact endpoint derivative identify the price-two permanent-deletion barrier and the single activation time, including equality at the boundary. The closed conductance formula and elementary rescaling establish the asymptotic ratio; no finite-grid extrapolation is used in the proof. The standalone verifier independently reconstructs exact finite characteristic polynomials and checks the formulas against matrix exponentials, sampled asymmetric budgets, and the large-network scaling. It passed 17,202 finite checks; sampled inequalities are corroboration only.

## Originality — PASS on inspected evidence

The closest published antecedents are the general linear-cost continuous-time fastest-mixing formulation by Sun, Boyd, Xiao and Diaconis (2006), the general convex Laplacian spectral design/symmetry treatment by Boyd (2006), and four full-text findings on priced matching edges in complete graphs: spectral-gap price-two optimizer faces, matching-size gap transitions, total-resistance deletion and worst-pair-resistance allocation. These use \(\lambda_2\) or inverse-Laplacian trace rather than finite-time heat trace. The present theorem supplies the missing exact finite-horizon optimizer, strictly unique selection among possible spectral-gap optimizer faces, the logarithmic observation-horizon threshold and its macroscopic scaling. Earlier eigenvalue formulas and the price-two spectral-gap boundary are explicitly excluded from novelty claims. Exact content, including all cost parameters and matching support, was compared rather than relying on title matches. published-finding corpus semantic searches and web primary-literature searches found no covering statement. Searching is not exhaustive; unindexed equivalent work remains a priority risk.

## Value — PASS

The problem models choosing conductance under two meaningful costs when performance is measured at a prescribed diffusion horizon instead of only asymptotically. The critical price two divides permanent deletion from eventual activation, while the active regime starts on a sharp time scale proportional to the square of network size. In the latter regime, expensive connections recover positive conductance even when they are omitted at shorter horizons, and they can absorb a vanishing fraction of total spending while remaining a positive fraction of ordinary per-edge conductance. This is a motivated design phase diagram, not a special numerical sample or a mere change of notation.

## Closest literature and limitations

1. Sun, Boyd, Xiao and Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699, https://stanford.edu/~boyd/papers/pdf/fmmp.pdf. Its objective maximizes the slowest-mode rate, not the entire finite-time heat trace.
2. Boyd, *Convex Optimization of Graph Laplacian Eigenvalues*, ICM 2006, https://www-leland.stanford.edu/~boyd/papers/pdf/cvx_opt_graph_lapl_eigs.pdf. Provides convex spectral and symmetry methods, not the priced-matching activation classification.
3. *The price-two rigidity transition and full optimizer faces for matched complete networks*, https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-the-price-two-rigidity-transition-and-full-optimizer-faces-for-m--2e1277c4e435/RESULT.md. Establishes the spectral-gap endpoint but not finite-time optimum.
4. *A sharp matching-price transition in resistance-optimized complete networks*, https://github.com/published-finding corpus/2026/blob/main/2026/10/13/SCOPE-a-sharp-matching-price-transition-in-resistance-optimized-comple--cf3b1355b128/RESULT.md. Covers inverse spectral moment, with a different critical price.
5. *A single-pair versus multi-pair price threshold for spectral-gap design of complete graphs*, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-a-single-pair-versus-multi-pair-price-threshold-for-spectral-gap--c0a7ce2499f8/RESULT.md. Stronger scope for spectral-gap design, but does not imply this time-dependent heat-trace law.

6. *Sharp worst-pair resistance design for complete graphs with priced matching links*, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-sharp-worst-pair-resistance-design-for-complete-graphs-with-pric--78a63c5af6f2/RESULT.md. It optimizes maximum effective resistance and does not determine heat-trace choices at finite horizons.

Limits: fixed even-size complete networks, a single cost-premium perfect matching, independent nonnegative conductances, fixed budget and unnormalized continuous-time diffusion. No arbitrary prices, discrete-time stochastic design, or independent external audit is asserted. The originality judgment remains qualified by possible unindexed equivalents.

Self-review: passed. Independent audit: not yet performed.
