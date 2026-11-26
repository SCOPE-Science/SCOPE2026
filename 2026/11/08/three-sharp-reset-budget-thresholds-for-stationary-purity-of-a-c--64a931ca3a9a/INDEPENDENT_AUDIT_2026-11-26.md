# Independent mathematical audit

## correctness

PASS

The equilibrium age is P(L>a)/μ at each a≥0. Summation and expectation can be exchanged because the absolute sum is μ. The cycle geometric series gives z=(1−E iᴸ)/(μ(1−i)); the diagonal entries are each 1/2, so the purity correction is |1−E iᴸ|²/(4μ²). Write w=1−E iᴸ. For u=2−μ in [1/2,1], the per-length linear support inequality gives Re w−u Im w≥1+u², tight at lengths 1 and 3, with length 4 also tight at u=1/2 but excluded by the required Re w=1. At μ between 3/2 and 4 the other linear support inequality gives 2 Re w−Im w≥4−μ, tight at 1,3,4; projecting to that line and applying the moment constraint gives precisely the stated weights. Zero norm forces residue 0 mod 4; at mean 4 this forces a point mass. For μ≤2, δ=E(i−iᴸ) has nonpositive real inner product with 1−i and norm at most √2(μ−1); the pointwise norm inequality is strict for every length over 2, so the unique optimizer has support in {1,2}. Above mean 2 the farthest point in the residue polygon is w=2, forcing residue 2 mod 4. Every real mean in a stated unbounded-support regime is attainable by mixing adjacent eligible lengths, and mixing extremizers yields all intermediate purity values at fixed mean. This reasoning does not assume synchronized convergence. An independent exact check computed the closest and farthest squared norms of the feasible residue polygon at 217 rational means, including all three thresholds. Replay: python3 /workspace/reproductions/frozen_checks.py 3. Finite polygon samples corroborate but do not certify the universal formulas or optimizer uniqueness.

## originality

PASS

The strongest distinct match treats the same fixed-mean extremal problem in continuous time. The half-turn and full-turn thresholds correspond to 2 and 4 ticks respectively, but its continuum envelope and equality cases do not give the discrete envelope or the additional optimizer transition at 3/2. The equilibrium age and renewal coherence reductions themselves are known. The pass is for the complete tick-constrained classification, not the general resetting model or the half-turn/full-turn mechanism.

## value

PASS

The quarter-turn phase is a canonical small finite-order gate, and fixed reset budget is the natural constraint. The exact cost of dephasing, the additional integrality-induced support transition below it, and the classification of every attaining law distinguish this from simply evaluating a steady state for a chosen clock. Equilibrium observation allows periodic optimizers without a false convergence interpretation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
