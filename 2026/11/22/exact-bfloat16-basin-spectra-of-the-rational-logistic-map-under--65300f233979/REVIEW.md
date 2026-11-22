# Scientific review

## Correctness
PASS. Every state code is decoded as an exact rational; both successor semantics are explicit and all outputs are in the enumerated domain. Two mathematically distinct exact rounding implementations agree on the full set of inputs and midpoints and on all successor evaluations. Independent path-following and indegree-peeling algorithms agree on the complete graph decomposition, cycle codes, basin totals and transients. The attached executable reproduces all entries. The exact finite-graph claims make no extrapolation to a continuum orbit.

## Originality
PASS on inspected literature, not an independent priority certification. The originating Kumar et al. article supplies the recurrence and specifically uses control 5.5 in its chaotic plot, but its available full paper does not present bfloat16 state graphs. Klöwer et al. address low-precision periodicity for logistic and Bernoulli maps, not this rational family. Other published rational-map results classify real periodic orbits and do not determine rounded graph basins. Search comparisons of equation aliases, evaluation orders and exact period/basin counts found no statement implying this particular census. An unindexed equivalent computation remains possible.

## Value
PASS. The parameter is the originating paper's canonical chaotic example and the invariant finite-state census is a natural diagnostic of numerical fidelity and periodic-orbit diversity. A change from one nonzero recurrent component to three despite only 1,371 changed edges is a substantive state-space phenomenon, not a random partial trajectory or a generic inevitability of finite precision.

## Residual limitations
The finding is about two explicitly defined ideal rounding semantics, not all possible bfloat16 execution orders or actual microarchitecture. Cycle lengths do not establish information-theoretic security. Independent audit is pending.

Self-review: passed. Independent audit: not yet performed.
