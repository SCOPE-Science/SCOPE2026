# Exact determinization and minimization overhead spectrum for three-state binary NFAs

## Finding

For every labeled, epsilon-free nondeterministic finite automaton on three states over an ordered two-letter alphabet, with exactly one initial state and exactly one final state, we determine the **complete joint distribution** of the number \(R\) of reachable powerset states and the number \(M\) of states of the equivalent minimal complete DFA. Each transition on each letter is an arbitrary subset of the three states, including the empty set. Initial and final states may coincide or differ. There are \(9\cdot 2^{18}=2{,}359{,}296\) such automata.

The complete population has \(1{,}828{,}224\) trim automata, meaning every one of the original three states is reachable from the initial state and can reach the final state. Among trim automata, the sharp maximum determinization-to-minimization **additive overhead** \(R-M\) is \(5\), attained by exactly \(1{,}716\) labeled automata; every extremizer has \((R,M)=(7,2)\). Further, among trim automata with all eight powerset states reachable, the minimal DFA has at least four states, sharply attained by \(1{,}272\) labeled automata.

For any fixed initial state, the normalized spectrum depends on the final state only through whether the endpoints coincide. The following table is for a fixed initial state \(0\) and final state \(0\) or \(2\). The columns headed *trim* count trim members of the same fixed-endpoint family. Cells not displayed are zero. The single complete 62-row machine-readable table appears in `data/joint_spectrum.csv`.

| \(R\) | \(M\) | Coincident: all | Coincident: trim | Distinct: all | Distinct: trim |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 4,096 | 0 | 4,096 | 0 |
| 2 | 1 | 15,360 | 7,872 | 16,128 | 0 |
| 2 | 2 | 14,256 | 147 | 13,488 | 9,088 |
| 3 | 1 | 34,560 | 29,712 | 5,760 | 0 |
| 3 | 2 | 9,145 | 2,730 | 32,714 | 29,094 |
| 3 | 3 | 19,995 | 11,889 | 25,226 | 20,188 |
| 4 | 1 | 11,520 | 9,936 | 2,688 | 0 |
| 4 | 2 | 9,084 | 3,092 | 20,417 | 18,979 |
| 4 | 3 | 28,128 | 24,554 | 21,749 | 18,843 |
| 4 | 4 | 19,848 | 15,972 | 23,726 | 21,682 |
| 5 | 2 | 5,520 | 2,092 | 6,926 | 6,644 |
| 5 | 3 | 15,912 | 13,180 | 12,870 | 11,028 |
| 5 | 4 | 15,142 | 14,058 | 15,843 | 15,307 |
| 5 | 5 | 15,274 | 15,274 | 16,209 | 16,209 |
| 6 | 2 | 2,500 | 900 | 1,500 | 1,444 |
| 6 | 3 | 3,130 | 2,102 | 3,702 | 3,014 |
| 6 | 4 | 6,692 | 5,616 | 8,109 | 7,493 |
| 6 | 5 | 7,436 | 7,436 | 7,325 | 7,325 |
| 6 | 6 | 11,034 | 11,034 | 10,156 | 10,156 |
| 7 | 2 | 648 | 216 | 178 | 178 |
| 7 | 3 | 388 | 248 | 344 | 284 |
| 7 | 4 | 1,112 | 760 | 1,852 | 1,622 |
| 7 | 5 | 1,972 | 1,972 | 2,340 | 2,340 |
| 7 | 6 | 1,952 | 1,952 | 2,036 | 2,036 |
| 7 | 7 | 5,700 | 5,700 | 5,022 | 5,022 |
| 8 | 3 | 44 | 0 | 6 | 0 |
| 8 | 4 | 252 | 192 | 162 | 116 |
| 8 | 5 | 160 | 160 | 166 | 166 |
| 8 | 6 | 332 | 332 | 366 | 366 |
| 8 | 7 | 80 | 80 | 102 | 102 |
| 8 | 8 | 872 | 872 | 938 | 938 |

Each fixed-endpoint family contains \(2^{18}=262{,}144\) transition tables. The coincident-endpoint family has \(190{,}080\) trim tables; the distinct-endpoint family has \(209{,}664\). Since there are three ordered coincident endpoint pairs and six ordered distinct pairs, multiply their respective table columns by three and six to obtain the all-endpoints population. In particular, \(15{,}660\) labeled automata reach all eight powerset states; of these, \(8{,}244\) already have minimal-DFA size eight. Among trim automata, \(15{,}036\) reach all eight powerset states.

## Assumptions and scope

Fix \(Q=\{0,1,2\}\), ordered input alphabet \(\{a,b\}\), no epsilon transitions, exactly one initial state and exactly one final state. For each state and each letter, the transition image may be any of the eight subsets of \(Q\); no completeness or nondeterminism requirement is imposed beyond this set-valued convention. The empty subset is included as a state of the *complete* powerset DFA whenever reached. The initial subset itself is counted, including the empty input word. \(R\) counts its reachable subsets. \(M\) counts distinguishable future accepted languages among those reachable subsets, including a rejecting sink if one is reachable. An original NFA is trim exactly when all original states are accessible and co-accessible.

## Proof

**Exhaustive finite domain.** Write the transition image of state \(i\) on each letter as a three-bit integer in \(\{0,\ldots,7\}\). Each letter is thus one base-eight number with three digits, in \(\{0,\ldots,511\}\). The ordered pair of letter codes ranges over all \(512^2=262{,}144\) possibilities, with no omissions or duplicates, for any prescribed pair of singleton endpoints. State relabeling is bijective on transition relations and preserves trim status, reachable powerset count and minimal-DFA size. It maps every coincident endpoint pair to every other such pair, and likewise all distinct endpoint pairs. Hence the two representatives \(I=F=\{0\}\) and \(I=\{0\},F=\{2\}\) suffice, with respective multiplicities three and six.

**Reachable subsets.** For a subset represented by mask \(s\), its successor on letter \(c\) is the bitwise union of all transition-row masks whose state bits occur in \(s\). Starting at mask \(1\), breadth-first closure under both letters returns exactly the collection \(\{\delta(I,w): w\in\{a,b\}^*\}\): induction on word length proves that every word image is reached, and every inserted mask is produced by a word. There are at most eight masks, so the closure terminates completely. Its size is \(R\).

**Language quotient.** A reachable subset accepts the empty word exactly when it contains the final state. Starting from this two-block partition, repeatedly refine a class by the ordered triple consisting of its current class and the classes of its two letter successors. The stable partition identifies exactly those subsets accepting the same continuation language. Indeed, after \(k\) rounds, any pair in different blocks is separated by an accepted/rejected continuation of length at most \(k\), and any pair in the same block agrees on all such continuations; stability implies agreement on all finite words by induction. Therefore the number of blocks is exactly the Myhill--Nerode state count \(M\). Alternatively, mark all pairs with different current acceptance and repeatedly mark pairs whose letter successors have already been marked. The fixed point is precisely the set of distinguishable pairs. At most \(\binom{8}{2}=28\) unordered pairs can be newly marked; neither method extrapolates from a partial search.

**Trim filter.** The union of all reachable subset masks is exactly the set of accessible original states. Starting with the final-state mask, repeatedly add any original state having a letter transition to the current set; this finite reverse closure is exactly the set of co-accessible states. The original NFA is trim if and only if both masks equal \(7\). The algorithms tally both the unrestricted and trim populations for every \((R,M)\).

**Certificate and extremal consequences.** The supplied CSV consists of the 62 nonzero fixed-endpoint cells, reproduced by two independent finite implementations: `verify/partition_enumeration.cpp` implements forward subset closure and stable class partitions, whereas `verify/distinguishability_enumeration.py` implements a separate reachable-subset procedure and reverse distinguishability propagation. Both independently enumerate the same complete finite domain and check every cell against the CSV. The row sums are \(262{,}144\) in each endpoint class. The maximum \(R-M\) among trim cells is \(5\), and it occurs only for \((R,M)=(7,2)\): \(3\cdot216+6\cdot178=1{,}716\). For \(R=8\), every trim cell has \(M\ge4\), and the \(M=4\) count is \(3\cdot192+6\cdot116=1{,}272\). These are exhaustive finite deductions from the certified table.

As explicit trim witnesses, take initial \(\{0\}\), final \(\{2\}\), and the row masks (states in order \(0,1,2\)) for \(a\) and \(b\) equal respectively to \((2,1,1)\) and \((6,4,5)\); here \((R,M)=(7,2)\). For \((R,M)=(8,4)\), take row masks \((2,0,1)\) and \((6,4,5)\) with the same endpoints. A mask is interpreted in binary, so \(6\) represents states \(\{1,2\}\). Both witnesses are directly included in the exhaustive enumeration.

## Verification

Within the supplied artifact directory run:

```sh
g++ -std=c++17 -O2 verify/partition_enumeration.cpp -o /tmp/nfa_partition
/tmp/nfa_partition data/joint_spectrum.csv
python3 verify/distinguishability_enumeration.py data/joint_spectrum.csv
```

Both programs assert all 62 table cells, each complete fixed-endpoint population of \(262{,}144\), and trim totals \(190{,}080\) and \(209{,}664\). Both were executed against the supplied CSV with successful results. Their proof obligations are explicitly finite: all six labeled transition images range over all eight subsets of \(Q\), closure exhausts the eight-subset state space, and stable right-language equivalence is exact. No behavior for larger state sets, larger alphabets, epsilon moves, or arbitrary multisets of endpoint states is inferred.

## Relationship to prior work

Baburin and Cotterell, *Towards A Parametrized Complexity of Determinization* (first publicly posted 7 November 2026), study the difficulty of estimating determinization complexity and bounds through transition monoids and subset complexity, and explain that subset construction can be much larger than the minimal DFA. Their published results do not give the present fixed-size labeled joint distribution. Nicol and Frohme, *Deconstructing Subset Construction* (2026), develop intermediate minimization and evaluate practical and synthetic automata; their full accessible text motivates quantifying overhead but does not provide the exact three-state binary singleton-endpoint census. Jirásková (2006) studies attainable DFA blow-up sizes for minimal NFAs; existence or general upper bounds do not determine the number of labeled NFAs realizing each ordered pair \((R,M)\). The standard powerset construction and Myhill--Nerode minimization supply the algorithmic background, not the new counts.

## Limitations

This is a finite labeled classification for three states, two ordered letters, no epsilon moves and singleton endpoints; automata with unreachable or non-co-accessible states are included in the unrestricted column and excluded from the trim column. Fixed endpoint classes are counted separately before relabeling. The result does not provide an asymptotic distribution or optimal determinization algorithm for arbitrary input sizes. It is an exhaustive computer-assisted theorem supported by independently executable finite programs, not a formal proof-assistant certificate. Previously unindexed equivalent enumerations cannot be ruled out. Independent review has not been performed.

## References

1. Ivan Baburin and Ryan Cotterell, *Towards A Parametrized Complexity of Determinization*, arXiv:2611.10911v1, first public version 7 November 2026. https://arxiv.org/abs/2611.10911
2. John Nicol and Markus Frohme, *Deconstructing Subset Construction: Reducing While Determinizing*, TACAS 2026, pp. 394–415, DOI:10.1007/978-3-032-22749-2_20. https://link.springer.com/chapter/10.1007/978-3-032-22749-2_20
3. Galina Jirásková, *Deterministic blow-ups of minimal NFAs*, RAIRO Theoretical Informatics and Applications 40 (2006), 485–499, DOI:10.1051/ita:2006032. https://doi.org/10.1051/ita:2006032
4. Michael O. Rabin and Dana Scott, *Finite Automata and Their Decision Problems*, IBM Journal of Research and Development 3 (1959), 114–125, DOI:10.1147/rd.32.0114.
