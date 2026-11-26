# Independent mathematical audit

## correctness

PASS

Count distinct parents of each length-four receipt, not deletion positions. The 15 first-occurrence equality patterns exhaust all receipts up to relabeling; direct deletion in each verifies at most two adjacent-repeat parents. Counting the union of the two adjacent equalities gives |A_q|=2q^2-q. An independent replay, branches/ebd6a027-7d8f-488c-b1c9-3832938cb61c/independent-reproduction.js, constructs the forbidden triples of distinct parents as a hypergraph and recursively tests target sizes, pruning only sets already containing a forbidden triple. At cardinalities 6,7 for q=2 and 15,16 for q=3 it gives respectively 1,0 and 1,0, with both singletons of the feasible layers equal to A_q as labeled sets. The combinatorial layer sizes are 28,8 and 17383860,13037895; downward closure excludes every larger size. The independently generated four-letter receipt histogram for the displayed 29-word code is (29,77,150,0,0) for list sizes 0 through 4. In a mixed receipt with three symbols in one full block and one outside, the only possible replaced in-block parent is obtained by removing the outside symbol. Among remaining mixed parents an equal pair must come from the three in-block positions. If exactly two are equal, the third is the only possible deletion making the equal pair; if all three are equal, an adjacent-repeat triple must leave the outside symbol at an end, with at most one possible such end (the count of in-block symbols on each side sums to three). Thus at most one mixed parent survives, and the three cases of the lift give the claimed bound for every q>=4. The frozen C++ checker and output were inspected, not executed; it prints the visited layer counts, but contrary to the prose does not separately assert their expected totals. The successor proof, observed counts and independent replay suffice. No exact optimum for q>=4 is inferred.

## originality

PASS

The inspected exact and broader matches treat a different receipt length, a different objective, or asymptotic rates. They do not cover the length-three integral list-two insertion rigidity and the first alphabet size at which it breaks. Full-text access limits are named below; the verdict is a bounded statement comparison, not a priority guarantee.

## value

PASS

The length is a natural smallest setting with nonadjacent repetitions and all-distinct parents. The work establishes a genuine rigidity cutoff of the simple adjacency construction: exact labeled optima in the first two alphabets, a finite minimal failure witness at four, and a repeatable improvement in every larger alphabet. The uniform block mechanism makes this more than an isolated one-code improvement or an unsupported search output, while preserving the stated lower-bound scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
