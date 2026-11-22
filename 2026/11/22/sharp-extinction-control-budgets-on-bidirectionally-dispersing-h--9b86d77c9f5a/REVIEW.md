# Scientific review

## Correctness — PASS

For the conservative-migration logistic model, extinction from every nonnegative initial state is equivalent to nonpositivity of the Perron spectral abscissa of the irreducible Metzler linearization. Weighted Cauchy–Schwarz proves extinction even on the neutral boundary; a positive subsolution and bounded positive supersolution produce a positive equilibrium above threshold. Summing the Perron equations and applying edgewise AM–GM proves the claimed budget, and forces unique edge eigenvector ratios at equality. Consistency of these ratios is equivalent to cycle balance. The exact two-node active-set optimization and biased-three-cycle Jensen argument prove the remaining quantitative clauses. The included `check.py` independently verifies exact rational identities on specified representative networks; finite sampling is not used as a general proof.

## Originality — PASS (bounded comparison)

The 2026 initiating study [1] explicitly poses minimum total extinction control as a future problem. Its results instead optimize biomass and yield with *fixed* effort, so neither its two-patch results nor its large-growth asymptotics imply this exact minimum extinction cost. The 2013 paper [2] already provides general geometric programming for minimum-budget protective control on directed positive systems: numerical/computational tractability and the eigenvalue optimization principle are established prior art. The earlier network-control objective targets a strictly negative prescribed linear decay rate; the logistic crowding here also permits an attainable, globally extinct neutral Perron boundary. The assessed narrower novel finding is the exact closed-form edgewise lower bound with a necessary-and-sufficient equality boundary, all-bidirectional-tree optimizer and growth threshold, complete two-site active-set switch, and explicit directed-cycle no-savings obstruction for a logistic metapopulation. No absolute historical-priority claim is made; a specialization of older positive-system matrix balancing may conceivably contain equivalent formulas.

## Value — PASS

The initiating ecological study names the minimum extinction-control budget as a natural unresolved optimization target. For bidirectional trees, the result converts that optimization into explicit ecological migration rates and a sharp feasibility condition, making individual-patch intervention decisions and their directionally induced savings computable. The cycle obstruction prevents a potentially misleading extrapolation of separate edge savings to networks with circulation, and the two-patch low-growth branch identifies the sharp transition to a single active control patch. This has value as a mathematical boundary result rather than a practical policy recommendation.

## Closest literature and remaining limitations

[1] Nguyen, Shuai, Tang, Veprauskas, Wu and Zhou, *Optimal Harvesting in Stream Networks: Maximizing Biomass and Yield* (2026), arXiv:2602.05071; DOI:10.1007/s11538-026-01658-8, Introduction, model and Discussion's list of future optimization questions. [2] Preciado et al., *Optimal Resource Allocation for Network Protection Against Spreading Processes* (2013), arXiv:1309.6270, Sections II–III, generic minimum-budget geometric programming. Remaining risk: equivalent closed-form tree/detailed-balance specializations may appear elsewhere in the historical positive-network-control literature. The result assumes continuous-time deterministic logistic dynamics and constant nonnegative per-capita interventions, not stochastic or field-validated eradication.

Self-review: passed. Independent audit: not yet performed.
