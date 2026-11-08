# Scientific assessment: exact collision moments for cyclic Rule 4

## Correctness — PASS

The statement concerns ordered pairs of labelled cyclic inputs, each of which is mapped once by the explicitly defined local Rule 4 map. The paired-symbol transfer matrix counts collisions by exact closed walks. Its characteristic polynomial is obtained by exact polynomial arithmetic. Independently, output one-sites fix neighboring input bits; free disjoint segments then consist of no-singleton-one words, giving a cyclic marked-composition formula. The squared-segment rational generating function yields a positive renewal singularity with leading coefficient one, while the all-zero-output fibre has strictly lower exponential order. Both independent computational implementations passed their stated checks. The infinite statement is proved by the transfer/renewal arguments rather than by extrapolating tested sizes.

## Originality — PASS, qualified

Jen's 1987 and 1989 papers establish general preimage counting, with the 1989 appendix explicitly treating Rule 4; no claim is made to rediscover those formulae. The 1989 text studies Shannon block entropy and general probabilities, not the cyclic-ring second moment with a degree-six exact exponential constant. Fukś's preimage-sequence work and Koller–Hudcová's transfer-matrix trajectory counts are related methods or different statistics; neither inspected result explicitly subsumes the specified pair-collision moment theorem. Searches using equivalent second-moment, collision-probability, Rényi-two, pair synchrony, cyclic basin-size and transfer-operator terminology yielded no covering stated result. An inaccessible, relevant 1988 article on cylindrical cellular automata and possible unindexed literature remain residual priority risks.

## Mathematical value — PASS

The distribution of basin sizes is a central quantitative characteristic of an idempotent but highly noninjective cellular automaton; the collision probability measures whether independently sampled inputs become exactly indistinguishable after one update. The exact algebraic exponential rate, sharp leading constant, and two independent exact all-size descriptions distinguish this from ordinary image counts, fixed-state counts, or a table of finite examples. This is a rule-specific calculation, not a universal law for all cellular automata.

Self-review: passed. Independent audit: not yet performed.
