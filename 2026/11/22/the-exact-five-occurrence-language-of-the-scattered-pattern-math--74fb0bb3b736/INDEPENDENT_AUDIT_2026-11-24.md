# Independent mathematical audit

## correctness

PASS

Independent all-length argument: call a one eligible if at least two zeros precede and at least two follow it. Every pair of eligible ones s<t contributes binom(L_s,2)binom(R_t,2) embeddings, where L_s counts zeros before s and R_t zeros after t, and no other pair contributes. At least four eligible ones would yield at least six embeddings. Two would give a single product of triangular numbers, which cannot be 5; fewer give zero. Thus there are three eligible ones. The contributions in order (1,2),(1,3),(2,3) are positive and must be a permutation of 3,1,1: the factors at most 5 are 1 or 3. The middle product is at most both others by monotonicity, so it is 1. If the first product is 3, the other two force L_1=L_2=2 and R_3=2, while R_2=3. Consequently there are five zeros, and the eligible interval between the second and fourth zero is 1101. If the last product is 3, reversal gives 1011. All other ones must be in the four ineligible runs, with no restriction on their lengths. Conversely both cores give 3+1+1; the parser is unique and the four exponents sum to n−8, giving the claimed count, GF and minimal words, including empty input. Separately inspected the frozen certificate by an independent cap-six DP × epsilon-NFA reconstruction: exact agreement with all 126 reachable states, 252 transitions and both accepting predicates. Saturation preserves the test for equality to five and reachable closure covers all lengths. Independent replay files: /workspace/branches/414a7688-ea4d-4ea1-ab01-41972d5ab13a/replay_record5.py and record5_replay.txt there. Unsaturated DP through length 16 was supplementary; the uploaded CHECKER.py was not executed.

## originality

PASS

The exact two-core description and all-length formula are distinct from the related exact two-run result and from general fixed-frequency structural theorems. Credit earlier eventual polynomiality, the degree bound, the primitive-word construction, and the already analyzed 0011 case. No exact coverage of the assigned three-run pattern and frequency was established in the inspected sources.

## value

PASS

This balanced three-run pattern lies outside the exact two-run results, and frequency five is the first beyond the cited small-frequency formulas. The case supplies an exact degree drop from the general bound and exactly identifies the two contributing cores. Those facts are useful as benchmarks for an eventual tightness criterion; this is more than a short-word count, and does not claim to solve that criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
