# Review of the sharp group-composition envelopes

## Correctness — PASS

The conditional two-state chain has unique marginal stationary probability \(h(p)=p^2/(1-p+p^2)\). The upper bound is the exact factorization \(p-h(p)=p(1-p)^2/(1-p+p^2)\). For the lower bound, \(1-p+p^2\) is minimized on the finite cooperator lattice at the one or two sites nearest half occupancy; this gives a supporting line to \((1,1)\). Strict convexity on \([0,1/2]\) and a derivative comparison at the lower nearest-half site produce the sharp polygonal envelope. Jensen's inequality and two-point supporting distributions prove both attainability and equality conditions. The attached exact checker passed; its finite enumeration is not a proof of unbounded group sizes.

## Originality — PASS, with residual risk

The primary source of the model is Wei et al., arXiv:2603.22967 (2026-03-24), whose full available article text was inspected, including the state-transition equations and simulation conclusions. It does not state a fixed-strategy stationary abundance convex-envelope theorem. Su et al. (2019) address evolutionary selection with game transitions, while Pi et al. (2026) optimize two-player variable game distributions for cooperation selection, rather than fixing a common cooperator mean and bounding state abundance for arbitrary higher-order group-composition distributions. The generic Markov-stationary formula and convex-hull method are not original. The new specificity is the exact lattice-dependent lower envelope, parity contact set, and sharp arrangement reversal for the named model. The full text of Pi et al. was not obtainable in this review; although the available model description identifies a different optimization objective, an unindexed implication cannot be fully ruled out. The literature and indexed record searches are evidence of noncoverage, not proof of uniqueness.

## Mathematical value — PASS

The exact envelope answers a natural structural question left open by environmental-state simulations: how much high-quality game availability can differ while aggregate cooperative participation is unchanged? The closed formula works at every group size, detects a group-size/parity-dependent optimizer transition, and gives both lower and upper attainable bounds. The four-person witness demonstrates that neither homogenizing nor arbitrary mixing has a universal sign effect on environmental abundance. The statement is explicitly restricted to frozen strategies and does not infer new global behavior of the full imitation process.

## Closest literature and limitations

The motivating transition kernel is in Wei et al. (2026), equations (6)–(7), arXiv:2603.22967. Relevant prior frameworks include Su et al. (2019), arXiv:1905.10269; Pi et al. (2026), arXiv:2603.20603; and Zhang et al. (2026), arXiv:2602.07877. Generic convexification remains background mathematics. Extrema over arbitrary composition distributions need not be exactly realizable at a prescribed finite edge count or under prescribed edge-overlap constraints; the main result therefore distinguishes universal bounds from topology-specific feasibility.

Self-review: passed. Independent audit: not yet performed.
