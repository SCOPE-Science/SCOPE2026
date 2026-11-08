# Review of the exact-EF capacity census

## Correctness

PASS. The source's Definition 1 reduces for unit size/disutility to \(\min(a_i,b_j)\le a_j\) for every source bundle, including the housekeeper, and genuine agent \(j\). Unsaturated agents are forced to be global load maxima; the resulting saturation/water-level dichotomy is both necessary and sufficient. Multinomial counting gives the complete labeled census. Adjacent workload bands differ by \(R(t+1)\), making the final missing workload exactly \(F(t_*)-1\); later bands touch. The entire argument covers \(m=0\), all-full instances and arbitrary positive integer capacities. Direct finite enumeration checked 6,066,226 labeled assignments with no discrepancy, and separate threshold tests covered 19,525 heterogeneous capacity vectors. Computation supports, but does not replace, the proof.

## Originality

PASS on available evidence, with residual priority risk. The 2024 source [1] was inspected through its accessible full-text HTML, including the precise EF definition, sections on indivisible EF1/EFX and divisible EF, and relevant theorem proofs. The 2022/2023 closely related budgeted-goods paper [2] was also inspected in its open version, particularly its definition and cardinality/equal-size cases. Both stop at relaxed fairness guarantees in indivisible settings: neither inspected result states the complete exact-EF load census or the strict-Durfee final-gap cutoff. The shared integer structure of the goods and chores models is recognized, not treated as a novelty escape. Searches for synonyms, capacity water-filling, exact census and saturation thresholds did not identify dominating published coverage. Unindexed or poorly retrieved equivalent work cannot be ruled out.

## Value

PASS. Exactly envy-free allocations need not exist even when chores have identical unit disutility, although weaker fairness is achievable. For this canonical homogeneous submodel, the result solves three intertwined natural questions for every budget vector: which precise allocations are EF, how many are there, and from which smallest workload onward is existence guaranteed for every larger workload? The sharp threshold depends on a strict Durfee-type index of the capacities and can be far below total capacity. For four agents of capacity five, eleven chores are impossible but every workload from twelve onward is possible; at twelve there are exactly 369600 fair assignments. These exact boundaries and counts are not supplied by the general EF1/EFX algorithms.

## Sources and scientific limits

[1] Elkind, Igarashi and Teh, *Fair Division of Chores with Budget Constraints*, first online 31 August 2024, https://doi.org/10.1007/978-3-031-71033-9_4 ; full text https://arxiv.org/html/2410.23979v1 .

[2] Barman, Khan, Shyam and Sreenivas, *Finding Fair Allocations under Budget Constraints*, https://arxiv.org/abs/2208.08168 .

The result requires distinct unit chores, identical additive disutility, positive integer capacities, the housekeeper, and the precise source-defined EF relation. It makes no claim about heterogeneous chores, all fairness variants, or independent external checking.

Self-review: passed. Independent audit: not yet performed.
