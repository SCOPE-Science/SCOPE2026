# Self-review

## Correctness — PASS

The claim has explicit parameter domain and a convergent Lyapunov Gramian. The Cauchy determinant identity and Kalman minor give the exact objective for all positive conductances and damping. The derivative numerator is a quadratic with a negative constant and positive leading coefficient, forcing exactly one interior positive root and a global maximum. Monotonicity and both damping asymptotics follow from explicit signed derivatives and nonsingular polynomial expansions. Symbolic Lyapunov elimination and exact identity checks were independently replayed within the same mathematical review, together with finite numerical diagnostics; the latter are not treated as proofs of universal claims.

## Originality — PASS on inspected evidence, qualified

The closest published frameworks optimize actuator selection or worst-case/average control energy, not the two continuous conductances under a fixed total-budget and D-volume objective. A relevant publicly available fixed-weight star result optimizes the sensor location instead of edges, so its implication runs neither to the quadratic optimum nor to the singular weak-edge asymptotic. The arXiv HTML of Pasqualetti–Zampieri–Bullo (2013) and Cortesi–Summers–Lygeros (2014) was materially reviewed, and the star sensor theorem full text was compared. Index coverage is not a uniqueness proof. Becker et al. (2019) is a relevant but differently targeted edge-optimization abstract; full-text comparison and other unindexed overlaps remain genuine publication-priority risks.

## Value — PASS

The objective is the standard volume of the reachable ellipsoid, and edge budget is a natural engineering constraint. A complete exact classification for the smallest nontrivial hub-controlled star demonstrates that the volume-optimal allocation is always asymmetric, with a non-obvious nearly disconnected weak-link scaling. The difference between fixed-conductance \\(O(\\mu^{-1})\\) and designed \\(O(\\mu^{-2})\\) determinant growth identifies a real tradeoff between energy-volume metrics and connectivity/robustness. It is not proposed as an arbitrary numerical example or as a general-star theorem.

## Closest literature and limitations

Pasqualetti et al. (2013), arXiv:1308.1201; Cortesi et al. (2014), arXiv:1403.6351; the 2026 public weighted-star D-optimal sensor classification; Becker et al. (2019), arXiv:1902.04195. The theorem does not extend to zero leakage, finite-time performance, or other metrics. Full publication priority and independent checking remain outstanding.

Self-review: passed. Independent audit: not yet performed.
