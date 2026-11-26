# Independent mathematical audit

## correctness

PASS

Writing K for the number of ones, substitution gives K_(m+1)=2^m−K_m and K_0=0. Each one comes from a disjoint 01 image, so (01)^K embeds; this realizes every length-K word and every length-(K+1) word with an adjacent 01, by packing that pair into one block. The all-ones word of length K+1 is impossible and the all-zero word occurs since 2^m−2K≥1 for m≥2. Among all other length-(K+1) words avoiding 01, the earliest r ones maximize the zeros available for 1^r0^(K+1−r). The mandatory gaps give K−r zeros. For even m the final zero supplies the missing zero; for odd m the suffix 1000101 gives no trailing zero, a one-zero final gap, and a three-zero penultimate gap. The suffix follows from φ²(01)=01000101 and its invariant final 01, with base m=3. Thus exactly r=K,K−1 fail in the odd case, in addition to the all-ones word. This exhausts the finite-word scattered-subsequence claim. Independent greedy enumeration of every length-K and length-(K+1) binary word for m=2,3,4,5 agreed (counts 1,3,1,3); the frozen verifier was inspected, not executed. The recorded 2≤m≤13 check is finite.

## originality

FAIL

A distinct indexed record proves exactly the same full list and index for the same substitution and a superset of the levels. This establishes equivalent coverage at audit time, not who obtained it first. The catalogue dates alone do not establish priority.

## value

FAIL

The shortest missing patterns of a canonical morphic family and their parity dependence are a meaningful exact invariant. But the frozen range and every pattern are already covered by the distinct indexed theorem; relative to the available result there is no surviving exact invariant, stronger boundary, or other incremental mathematical result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
