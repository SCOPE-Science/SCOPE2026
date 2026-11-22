# Independent mathematical audit

## correctness

PASS

The turn-flip-move ant state space has 2^12*12*4=196608 states. Each transition has a unique inverse, found by backing up the final direction, recovering the preflip bit and old heading, so the finite full map is a permutation and every state is immediately periodic. Independent full-state enumeration rebuilt and traversed all 196608 states, obtaining 2480 cycles, 20 distinct periods, minimum 16 and maximum 312; all periods divisible by 8 and period-weighted total 196608. All 48 translations and axis-sign operations with color complement for reversing orientation commute with the rule. Classifying temporal cycles under these symmetries reproduced exactly 74 types and the complete 20-row count table, including 18 types among 564 period-72 cycles and two types among 96 longest cycles. This is exhaustive for the fixed finite torus, not for other dimensions.

## originality

PASS

First nonsquare nondegenerate 3-by-4 torus complete labelled-cycle and rule-symmetry quotient census is not supplied by earlier all-white period tables, 3-by-3/4-by-4 torus censuses, 2-by-n geometry, or infinite/twisted-torus complexity papers. Bounded risk of unindexed finite ant enumerations remains.

## value

PASS

A 3-by-4 torus is the first unequal-sided torus with at least three sites in both directions, making it a natural finite benchmark. The 20 temporal periods refine into 74 geometric cycle types; even a fixed period (72) splits into 18 distinct types. These are exact complete finite dynamical invariants, independent of claims about larger lattices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
