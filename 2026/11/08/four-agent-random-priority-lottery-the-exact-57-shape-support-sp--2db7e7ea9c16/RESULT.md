# Four-agent random-priority lottery: the exact 57-shape support spectrum

## Finding

For every strict complete preference profile in the square house-allocation model with four labeled agents and four labeled objects, choose an agent priority uniformly from the \(4!=24\) orders, then assign each agent her favorite currently available object in that order (random serial dictatorship, also called random priority).

For a profile \(P\), let \(\mu_\sigma(P)\) be the deterministic matching produced by the priority order \(\sigma\). For any matching \(\mu\), define its *priority multiplicity* and the *matching-support size* by
\[
c_P(\mu)=\#\{\sigma\in S_4:\mu_\sigma(P)=\mu\},\qquad
s(P)=\#\{\mu:c_P(\mu)>0\}.
\]
The uniform lottery assigns each matching \(\mu\) probability \(c_P(\mu)/24\). The sorted list of positive multiplicities is its *outcome-multiplicity shape*; this is a partition of \(24\), but not every partition of \(24\) is feasible.

**Complete support-size census.** Among all \((4!)^4=331{,}776\) labeled preference profiles, exactly the following numbers have each support size:

| Support size \(s\) | Number of profiles \(N_s\) |
|---:|---:|
| 1 | 31,104 |
| 2 | 20,736 |
| 3 | 20,736 |
| 4 | 53,856 |
| 5 | 48,384 |
| 6 | 40,032 |
| 7 | 45,504 |
| 8 | 26,568 |
| 9 | 12,672 |
| 10 | 15,120 |
| 11 | 6,336 |
| 12 | 5,880 |
| 14 | 4,032 |
| 16 | 216 |
| 18 | 576 |
| 24 | 24 |

All other support sizes from \(1\) through \(24\) are impossible. In particular, the forbidden sizes are
\[
13,15,17,19,20,21,22,23.
\]
Across all profiles, the sorted positive priority-multiplicity list assumes **exactly 57 different shapes**. The accompanying `SPECTRA.csv` gives every one of those 57 shapes and its exact labeled-profile frequency; `SUPPORT_HISTOGRAM.csv` is the 16-row marginal table. For every row of `SPECTRA.csv`, its multiplicities sum to \(24\), and grouping by the number of listed positive multiplicities yields the table above.

Consequently the exact mean number of supported deterministic matchings under uniformly and independently sampled strict preference rankings is
\[
\mathbb E[s(P)]=\frac{1{,}839{,}744}{331{,}776}=\boxed{\frac{1597}{288}},
\]
and the probability of at least fourteen supported matchings is
\[
\Pr(s(P)\ge14)=\frac{4{,}848}{331{,}776}=\frac{101}{6912}.
\]
Exactly 24 profiles achieve full 24-matching support, namely the profiles in which all four agents report one and the same ranking (the 24 choices of common ranking). This is part of the census, not an assertion of a new all-market support theorem.

## Assumptions and scope

There are precisely four labeled agents and four labeled indivisible objects, each agent receives exactly one object, and each agent's complete preference order is strict. The primitive priority distribution is uniform over the 24 permutations of the four agents. The object assignments are deterministic after an order is chosen; no preference ties or mechanism tie-breaking arise.

The support here is the support of the **specific RSD lottery over complete deterministic matchings**, not the number of positive entries in its four-by-four matrix of agent/object marginal probabilities. The full distribution over deterministic matchings matters: different lotteries can have the same marginal random assignment.

A profile is labeled. No quotient by names is applied when reporting the frequencies. Quotients by agent and object relabeling are used only as an independent counting method with exact orbit weights.

## Proof

The numerical theorem has a finite exhaustive proof, supported by two independently written checkers and complete census data. Both checkers enumerate *all* profiles, one directly and one through disjoint symmetry classes. Their source files, input tables, loop bounds, integer assertions, and replay instructions are included. No extrapolation from a partial finite sample is involved.

**Direct labeled enumeration.** There are \(24\) distinct strict rankings of the four objects. `rsd4.cpp` runs four nested loops, each from index \(0\) to index \(23\), and so visits each of the \(24^4\) labeled profiles exactly once. For a given profile, it loops over all \(24\) agent permutations. For each priority order, it allocates the top available object to each agent, maintaining a four-bit used-object mask, and encodes the resulting four-entry matching in the table of all 24 object permutations. Thus each priority contributes exactly one count to exactly one matching, and the 24 matching counts sum to 24. Counting positive entries yields \(s(P)\); sorting the nonzero counts yields its shape. Integer accumulators tally all profiles by support size and shape. Assertions check the full histogram, the 57-shape total, the domain size and the sum of support sizes.

**Independent symmetry-weighted enumeration.** `verify_rsd4_support.py` begins instead with the \(\binom{27}{4}=17{,}550\) nondecreasing four-multisets of the 24 possible rankings. It identifies two such multisets exactly when a common permutation of the four object names transforms one into the other. This produces 762 canonical classes. A multiset with ranking multiplicities \(d_1,\ldots,d_j\) represents exactly
\[
\frac{4!}{d_1!\cdots d_j!}
\]
labeled agent profiles, and all preference multisets in a given object-renaming class have the same outcome shape. The program sums these exact multiplicities for each canonical class. Its total reconstructed labeled weight is \(331{,}776\). Independently of the bit-mask implementation, this program implements serial allocation by repeatedly choosing the first preferred element of a mutable `set` of available objects, records a counter of four-tuples of assigned objects, and then weights the resulting shape. It checks all 16 reported histogram entries, every missing support size, 57 distinct shapes, the 24 full-support profiles, the exact mean, and both shipped CSV tables.

Relabeling agents merely reindexes which agent receives each object and which priority order is used; renaming objects also induces a bijection of matching outcomes. Both operations preserve the multiset of positive priority multiplicities, justifying the symmetry weighting. Each multiset has exactly one canonical class, and each labeled profile has exactly one underlying ranking multiset, so there is neither omission nor double counting. The two enumerations therefore give exact independent exhaustive certificates for the same integer claims.

Grouping all recorded shape counts by their number of entries gives the 16 support-size frequencies. Direct summation gives \(\sum_P s(P)=1{,}839{,}744\), and the listed high-support cells total \(4{,}848\). The CSV shape table is exhaustive because the direct program generates a shape on every labeled profile, while the symmetry program checks the identical 57 shape-frequency pairs against that table.

## Verification

All computations use exact integer arithmetic; no floating-point approximation affects any count. In a directory containing the four accompanying source/data files, run:

```text
python3 verify_rsd4_support.py
g++ -O3 -std=c++17 rsd4.cpp -o rsd4
./rsd4
```

Both programs print `VERIFY_OK` when their checks pass. The Python verification independently reads and validates the two shipped CSV files, and its orbit-weighted counts were compared shape-by-shape with those from the direct labeled C++ computation.

The direct program performs \(331{,}776\cdot24=7{,}962{,}624\) serial-dictatorship evaluations. The independent program performs 17,550 canonicalizations under the 24 object permutations, then all 24 priority orders for each of the 762 canonical classes. Neither verifier assumes that any unexamined configurations behave similarly.

## Relationship to prior work

Abdulkadiroğlu and Sönmez (1998) define the random-serial-dictatorship lottery and prove that it coincides, profile by profile, with the core from uniformly random initial endowments. That identity and its all-market mechanism formulation are established prior results, not new claims here. Bade (2019/2020) obtains a broader lottery-equivalence theorem for randomized role assignments to deterministic matching rules. Thus the census also describes the matching-support shapes of those lottery-equivalent mechanisms where the hypotheses hold; it does not assert a new equivalence.

Shen, Wang, Zhu, Fain, and Munagala (arXiv version publicly released 31 January 2023) analyze assignments with uncertain priority and establish welfare and fairness properties of mechanisms including RSD. Their full accessible text motivates the effect of priority uncertainty but does not give the exact four-agent lottery-support census.

A prior complete three-agent RSD study has five multiplicity shapes and gives a labeled-profile table for three objects and three agents. Other published four-agent enumerations classify ordinal inefficiency of RSD and stochastic-dominance comparisons of random priority with probabilistic serial; those properties involve marginal assignment probabilities and do not determine the present distribution over complete deterministic matchings. The inspected literature on counting reachable *sets of houses* in Pareto-optimal matchings also studies a different invariant: in the square model, every complete matching uses all houses, even though the number of distinct Pareto-optimal matchings varies.

The numerical 57-shape census, its exact profile frequencies, and the complete list of feasible versus forbidden four-agent matching-support sizes are the contributions assessed here. The classical equivalence of RSD support with Pareto-efficient deterministic allocations is a different general fact and is not claimed as new.

## Limitations

This is a complete **four-agent finite census**, not a formula for arbitrary numbers of agents. The proof of the 57-shape numerical table is exhaustive computation with two independent enumeration methods, not a short closed-form combinatorial derivation of each entry. The results do not cover nonuniform priority, ties, quotas, extra unmatched objects, strategic preference reports, or marginal assignment-matrix support.

The accessible primary literature and available published-result comparisons did not reveal a table implying the 57 frequencies. Nonetheless, a thesis, supplementary computation, earlier unpublished table, or inaccessible article might contain equivalent numbers. A related 2019 matching-mechanism equivalence paper's author manuscript was inaccessible during the inspection; its abstract concerns lottery equivalence, but unreviewed supplementary material remains a residual priority risk. No independent external scientific validation has been performed.

## References

1. A. Abdulkadiroğlu and T. Sönmez, “Random Serial Dictatorship and the Core from Random Endowments in House Allocation Problems,” *Econometrica* 66 (1998), 689–701. DOI: 10.2307/2998580.
2. S. Bade, “Random Serial Dictatorship: The One and Only,” *Mathematics of Operations Research* 45 (2020), 353–368, first online 28 August 2019. DOI: 10.1287/moor.2019.0987.
3. Z. Shen, Z. Wang, X. Zhu, B. Fain and K. Munagala, “Fairness in the Assignment Problem with Uncertain Priorities,” *AAMAS* (2023), 188–196; first arXiv version posted 31 January 2023. arXiv:2301.13804v1.
4. A. Asinowski, B. Keszegh and T. Miltzow, “Counting Houses of Pareto Optimal Matchings in the House Allocation Problem,” *Fun with Algorithms* (2014), 301–312. DOI: 10.1007/978-3-319-07890-8_26.
