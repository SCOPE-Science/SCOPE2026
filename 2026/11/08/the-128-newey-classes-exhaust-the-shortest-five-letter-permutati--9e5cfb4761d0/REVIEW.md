# Independent mathematical audit

## correctness

PASS

The finite census has a complete justified search domain. Repeated adjacent letters may be deleted without losing a distinct-letter permutation subsequence; canonical first-appearance renaming is unique and has free S5 action. For any t-distinct-letter pattern p, its earliest greedy completion in a length-L universal word leaves a suffix universal for the 5-t complementary symbols; hence the deadline L-m_{5-t} with verified m_1..m_4=1,3,7,12 is necessary. Actual C++17 enum_greedy and enum_subseq source blobs were fetched and Git hashes checked; one maintains greedy progress in 120 target permutations, the other explicit bitsets of all distinct-letter subsequences. Both independently compiled and searched the complete normalized, adjacent-repeat-free trees: zero canonical solutions at 18 and an identical list of precisely 128 at 19. Independent Python checks confirmed all 120 patterns in each 19-word, proper normalization and 16 fixed/56 paired reversal orbits; rank-five lower bound follows from empty 18 and extension argument. A full finite exhaustive proof is warranted because every branch and pruning rule is justified; a mere log or numerical sample would not be.

## originality

PASS

Best-of-knowledge statement/implication comparison: Compared alphabets relabeling and reversal as distinct group quotients; the new assertion is the upper bound of 128, not the previously known construction count. An optimal construction lower bound and minimal length theorem do not imply the number of all shortest words. The upper bound is provided by complete independent finite searches. An example list is not global enumeration unless soundly exhaustive. The two independently implemented pruning traversals provide that missing closed-world certificate; unindexed later lists remain possible priority overlap. The prior lower bound plus a new exact upper bound implies equality, while no inspected previous construction, length bound or OEIS entry entails that upper bound.

## value

PASS

This answers Newey’s explicit March 1973 question whether his 128 constructible five-letter shortest universal words exhaust the equality cases. A sharp exhaustive classification at the first unsettled alphabet size is a natural useful combinatorial invariant; it determines exact labeled and reversal spectra and structural occurrence constraints. It is not presented as a general alphabet theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
