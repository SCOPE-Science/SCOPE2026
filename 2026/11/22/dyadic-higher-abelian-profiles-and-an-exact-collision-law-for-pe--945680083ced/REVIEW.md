# Independent mathematical audit

## correctness

PASS

The two length-L substituted blocks share their first L−1 symbols and have opposite final bits by induction, so a factor starting at qL+r is exactly the r-rotation of U_(k,p_q). Both block types occur; their weights (L−δ)/3 and (L+2δ)/3, δ=(−1)^k, differ by one, separating their profiles. For h=ℓ−1, subtracting ∑_c occ(cu) or ∑_c occ(uc) from occ(u) for every h-word u recovers the initial or terminal h-word. Thus within one circular block equal profiles force equal cut bridges, and conversely a cut only deletes circular occurrences crossing it, all determined by the bridge. For m=2h≤2^j, any m-factor meets at most two aligned j-blocks; the common prefix makes it a cyclic m-factor in the first block. All cyclic possibilities occur via adjacent block types 00 and 10. Both pairs occur in each of the two blocks after three substitutions and in their longer iterates, since higher iterates begin with the appropriate expanded 0-block. Consequently for k≥j+3 each U_(k,a) has the whole bridge language, giving 2P_p(m). The frequency counts starts: type-a blocks have natural density π_a and contribute occ_cyc(v,U_(k,a)) cut offsets out of L, counted with multiplicity even for a circularly periodic block. For ℓ=3, 11 and 0000 are forbidden (even positions are zero, and adjoining odd zeros would require adjacent ones in the desubstituted word); circular four-factors are linear p-factors by the common-prefix argument. Ones are at odd positions, so each circular gap contains either one or three zeros. Each long gap contributes one instance to each A count and each short gap one to each B count, tallying 0010 by its preceding long gap and 0100 by its following long gap. If g₃,g₁ are the gap counts, g₃+g₁=block weight and 4g₃+2g₁=L; substituting the weights gives the tabulated positive frequencies for k≥4. In the sum of their squares with denominator 324L² the numerator is 16(L+2δ)²+12(L−4δ)²+2(L+8δ)²=30L²+384, giving 5/54+32/(27L²). Independent bounded enumeration at the minimum general thresholds for ℓ=2,…,6 and for explicit k=4,…,9 corroborated the counts and collision law. Replay: python3 /workspace/branches/da73aa29-1e4f-40f3-8cb3-c0c66db45c58/record5_recheck.py; adjacent record5_recheck_results.txt records the run. The two frozen scripts in verification/ were inspected, not executed. Enumeration is not the proof of the stated sufficient thresholds.

## originality

PASS

Cyclic complexity at dyadic lengths, order-two Abelian complexity, ordinary factor complexity, and even the dyadic whole-factor frequencies have substantive prior coverage. Credit those ingredients. The distinct content of the frozen result is the all-order dyadic partition by cut bridges with stabilization in each block, the resulting profile-frequency formula, and the earlier-threshold three-Abelian table and collision law. None of the inspected matching statements supplies that partition or the profile probabilities. Same-day dates do not establish priority, and the comparison is bounded.

## value

PASS

The problem asks how local pattern counts distinguish dyadic factors of a canonical substitution word, a stronger statistic than cyclic or ordinary factor complexity. The bridge partition explains the exact all-order count at a sufficient threshold. The nonuniform three-Abelian profile probabilities give an exact distribution of signatures of factor starts and a chance of agreement not determined by the mere fact that there are twelve classes. No sharp general threshold or coding capacity is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
