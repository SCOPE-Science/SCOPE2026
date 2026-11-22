# Scientific review

## Correctness — PASS

The theorem is a fixed-finite-state assertion about the microscopic continuous-time Markov chain, not its diffusion approximation. The positive resource states form a killed finite generator. The pure-cooperator birth–death block has a positive, strictly increasing Perron right eigenvector, proved using order preservation and the eigenvalue equation. Comparing resource mortality and strategy exits to this eigenvector establishes strictly smaller spectral bounds for the all-defector and mixed blocks when the cooperative threshold exceeds the first integer resource stock. A positive path to the dominant class from each cooperator-containing initial state completes exponential conditional convergence. If the threshold is at most one, the positive-stock cooperator-increase rates vanish identically. Uniform finite-state death paths prove almost-sure depletion. The accompanying numerical program passed 90 finite parameter-family checks; these are corroboration rather than an infinite proof.

## Originality — PASS, qualified by available literature

The initiating article [1] gives the exact jump-rate model (Supplemental equations S1–S4), but treats diffusion/LNA quasi-cycles rather than the long-time conditional law or the sharp discrete threshold. The closest competing result found in primary literature, McAvoy et al. [2], explicitly discusses quasi-stationarity and longer persistence of all-cooperator populations, so qualitative noise-driven selection is **not** claimed as new. However, its discrete-generation variable-population branching process is not the resource-level continuous-time Markov chain in [1], and it has no cooperator-update gate at integer resource stock one. The multitype birth–death quasi-stationarity literature [3] supplies general techniques, but not this model-specific exact lattice boundary, eigenvalue domination, and conditional selection conclusion. Accessible published resource-feedback summaries concern other dynamical systems. Residual risk: unindexed work may already contain an equivalent spectral principle or a stronger model-specific result; the McAvoy PDF text was read, but page screenshots were not obtainable through the source interface.

## Value — PASS

The model includes a concrete finite-resource scarcity gate. The theorem identifies its *sharp minimum granularity* for strategy accessibility, then proves that an accessible all-cooperator class dominates the entire conditional survival tail rather than merely receiving occasional trajectories. This links a discrete ecological threshold, long-time survivorship selection, and the distinction between noisy quasi-cycles and true stationary dynamics. Both sides of the boundary are nonempty, including a directly checkable threshold-crossing example. The implication does not extrapolate to sustainable real fish stocks or typical observation windows.

## Limits and source comparison

The conclusion presupposes finite resource stock, no resource immigration, irreversible strategy-fixation boundaries, strictly positive extraction and switching parameters, and mixed-pair extraction rates not below all-cooperator extraction. It is not uniform as size grows and does not claim an asymptotic fixation probability or sharp extinction-time constant. Independent scientific audit is not available.

[1] Caruso, Menegazzo, Latora, Suweis, arXiv:2610.41830, https://arxiv.org/abs/2610.41830 .

[2] McAvoy, Fraiman, Hauert, Wakeley, Nowak, *Public goods games in populations with fluctuating size*, 2018, https://doi.org/10.1016/j.tpb.2018.01.004 .

[3] Chazottes, Collet, Méléard, *On time scales and quasi-stationary distributions for multitype birth-and-death processes*, 2017, https://arxiv.org/abs/1702.05369 .

Self-review: passed. Independent audit: not yet performed.
