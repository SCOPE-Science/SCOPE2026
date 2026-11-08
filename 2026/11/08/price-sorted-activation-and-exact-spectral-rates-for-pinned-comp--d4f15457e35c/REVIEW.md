# Self-review of priced complete-network pinning

## Correctness: PASS

For arbitrary integer \(n\ge2\), positive vertex costs \(p_i\) and budget \(B>0\), the rank-one identity \(L_{K_n}=nI-\mathbf 1\mathbf 1^{\mathsf T}\) reduces the spectral feasibility constraint to positive denominators and one reciprocal-sum inequality. The target-eigenvalue minimum-cost problem has a unique solution: its strict convex tangent certificate establishes global optimality without symmetry or local KKT assumptions. Solving the active reciprocal constraint yields the phase formulas; exact boundary algebra establishes monotone activation, continuous first derivatives, and eventual affine behavior. The standalone exact-rational and random numerical verifier reproduced 16,146 supplementary checks. The full-parameter theorem is not inferred from this finite sampling.

## Originality: PASS, with qualified priority

Zhou et al. (arXiv:1511.02012v1, 2015) already use a linearly weighted gain budget with importance-derived prices; this formulation is **not new**. Their full-text Results section gives a uniform-price analytic solution and numerical semidefinite optimization for nonuniform importance coefficients. Jafarizadeh (2022, DOI 10.1109/TSMC.2022.3151222) proves general uniform-total-gain SDP results and an equal-gain all-pinned complete-network special case, which is **already covered**. Jafarizadeh (2024, DOI 10.1109/TAC.2024.3376302) optimizes an eigenratio while varying graph-edge weights, not the present fixed-unit-edge, independent-priced rate budget. The assessed contribution is the all-positive-real-price **closed phase diagram, unique global allocations, exact entry costs and smooth/affine transition**. Published-priority overlap from unlocated diagonal-loading or heterogeneous-price specialist work remains possible. No novelty inference rests on an absence of title matches alone.

## Mathematical value: PASS

The question asks how to allocate a fixed, independently priced feedback budget to maximize a network's worst decay rate. Even on complete networks, heterogeneous actuator costs break vertex symmetry and allow the optimal support to change with the budget. An exact phase-by-phase allocation rule, a global uniqueness theorem and an explicit differentiability/affine law are structural optimization information rather than a restatement of general SDP feasibility or the equal-price formula. The result is scoped to its precise natural model and does not claim an arbitrary-network theorem.

## Sources and limitations

Primary sources: Zhou et al., arXiv:1511.02012v1 (first public on 2015-11-06); Jafarizadeh, DOI 10.1109/TSMC.2022.3151222; Jafarizadeh, DOI 10.1109/TAC.2024.3376302. Additional grounded-Laplacian selection literature: arXiv:1804.10818 (different ideal/infinite-pinning domain). The 2020 *Optimal Cost* proceedings paper, DOI 10.1109/LCN48667.2020.9314818, was accessible only as abstract; its full-text specialty priority remains a residual risk. All primary comparison statements refer to the actual material inspected. An independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
