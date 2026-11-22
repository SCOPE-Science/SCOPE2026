# Scientific review

## Correctness: PASS

The mode composition has only two possibilities after the first step: repeated retention of the chosen coordinate yields a geometric series, while switching coordinates annihilates the state. This establishes \(J(x)=\|x\|_2^2+\beta\|x\|_\infty^2\). At each coordinate basis vector, an upper envelope must include a quadratic with diagonal coefficient at least \(1+\beta\). Pigeonhole forces \(r=\lceil n/m\rceil\) such coordinates into one piece; exact Rademacher averaging removes every off-diagonal entry and gives the sharp lower bound. Balanced coordinate blocks attain it, with the global ratio bounded by \(s\le\min(1,rt)\); graph Bellman LMIs hold because \(\rho^2(1+\beta)=\beta\). The proof covers all integers \(n,m\), all real states and all \(0<\rho<1\). The accompanying checker passed 132 rational parameter instances, 71,991 finite assignments and a non-diagonal sign-cancellation test. Finite checks do not substitute for the proof.

## Originality: PASS (best-knowledge, qualified)

Ninite et al., arXiv:2602.04310, provide the general path-complete graph framework, co-complete maximum rule, and SDP-based approximation guarantees. Their main result and Example 2 do not identify the coordinate-reset modes, the minimax relative factor \(\Gamma_{n,m}(\rho)\), or the piece-count lower bound against all off-diagonal quadratics. The 2026 robust-control extension arXiv:2607.15055 treats feedback synthesis and min-max certificates, not this exact autonomous error frontier. Ahmadi–Jungers arXiv:1504.03761 concerns nonexistence of bounded-complexity stability Lyapunov functions, not sharp value-overestimate for this fixed stable family. Exact and semantic records were searched for coordinate-reset, rank-one, graph complexity, max-quadratic approximation, equivalence to intersection-of-ellipsoids problems, and stronger covering results. No covering implication was identified. Search results cannot prove publication priority; an unindexed equivalent formulation remains possible.

## Value: PASS

Graph size is a genuine cost/accuracy design parameter in graph-based worst-case control certification. This theorem gives a complete finite-size Pareto frontier, identifies when increasing graph nodes can change the sharp guaranteed relative error, and supplies feasible LMIs attaining that frontier rather than just a geometric upper bound. It also quantifies the high-persistence cost of coarse grouping and proves off-diagonal quadratic freedom cannot circumvent it. A rank-one coordinate-reset benchmark is deliberately simple, and the theorem makes no claim about practical speedups or general noncommuting controls; these restrictions do not negate the exact structural tradeoff.

## Relevant literature and residual risks

The closest source is Ninite–Banse–Berger–Jungers (2026), *A Path-Complete Approach for Optimal Control of Switched Systems*, arXiv:2602.04310, especially its graph definitions, Theorem 1, and sections on quadratic LMIs and relative accuracy. The later controlled extension arXiv:2607.15055 and Ahmadi–Jungers (2015), arXiv:1504.03761, were checked for broader implications. The exact lower bound is not a corollary of the cited generic feasibility statements without a distinct covering argument. Historical completeness of literature retrieval and applications to less special systems remain open limitations.

Self-review: passed. Independent audit: not yet performed.
