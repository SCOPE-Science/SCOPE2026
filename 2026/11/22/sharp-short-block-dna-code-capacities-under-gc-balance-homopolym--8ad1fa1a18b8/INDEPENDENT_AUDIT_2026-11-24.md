# Independent mathematical audit

## correctness

PASS

The incompatibility graph exactly describes the stated aligned Hamming and reverse-complement constraints after filtering for exact half-GC content, unequal adjacent symbols and self-separation. Reverse complementation is a Hamming isometry and preserves eligibility. Each eligible orientation class has two members, at most one of which can be selected; reversing either representative only interchanges the two cross distances being compared. Thus the unweighted compatibility clique number of the orientation classes equals capacity. Independently, n=2 is impossible by distance alone; n=4 has 40 eligible words, four size-four quotient cliques and no size-five clique, hence 4·2^4=64 labeled maxima. At n=6 there are 344 eligible words and 7804 incompatibility edges, yielding 172 orientation classes with 1908 cross-class conflicts. A separately written integer bitset search proved no clique of size 28: each candidate-prefix greedy coloring partitions into independent sets, bounding the extension by the number of colors; the recursion branches on inclusion and removes each candidate before considering later branches, and prunes only branches that cannot beat the independently checked size-27 incumbent. The complete run visited 5,237,256 search nodes. Direct read-only witness checks establish sizes 27 at six and 136 at eight for precisely the stated constraints. Since taking subsets preserves eligibility and separation, eight is the least positive even length for 32 or 128 messages.

## originality

PASS

The supported distinct claim is the exact six-symbol cutoff under the simultaneous fixed-composition, run-length-one and orientation-aware Hamming conditions, with the resulting first feasible message lengths. Credit ordinary constant-GC reverse-complement capacity, run-length-limited code concepts and the neighboring unrestricted four-symbol equality classifications; do not treat those as new. The available strongest comparisons do not give the exact restricted cutoff.

## value

PASS

The restrictions model a finite substitution code under composition and orientation constraints. Exact exclusion of 28 codewords at length six certifies that improving the search or construction cannot deliver a five-bit payload at that block length; the eight-symbol lower bound answers the corresponding five- and seven-bit feasibility questions. This is a concrete design boundary where asymptotic results and unrestricted-distance tables do not decide the answer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
