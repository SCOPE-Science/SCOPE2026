# Independent mathematical audit

## correctness

PASS

For an edge ij of K_n, the exact closed-neighborhood count is m-d_i-d_j+2x_ij. Subtracting equations sharing one index forces uniform ground-set degree parity, and then m must be odd; the converse follows immediately. Size 1 is impossible. At size 3, the only even-degree support is a triangle (its selected vertices are independent in the disjointness graph); the only all-odd possibility for n>=5 is a perfect matching at n=6. At size 5, an even-degree simple graph decomposes into cycles and can only be a single 5-cycle. All-odd degrees require even n<=10; n=6 is already solved, n=8 forces degrees 3,1,1,1,1,1,1,1 giving the star and two disjoint edges, and n=10 forces a perfect matching. Disjointness gives a cycle, a connected star/matching join, or a clique, respectively. Counts are 12*binom(n,5), 8*binom(7,3)*3, and 10!/(2^5*5!) plus the separate 6!/(2^3*3!) case. For the exchange claim, four common edges determine a spanning path and a unique completion. The five nonadjacent two-edge cuts each admit one different cyclic reconnection, in each case reversing a block of length two or three not containing the distinguished element and reversing sign. This gives a 5-regular bipartite graph on 6+6 cycles; the omitted cross edges form a matching and each omitted pair has distance three. Independent replay: python3 /workspace/review_checks.py 3 uses XOR of actual closed-neighborhood masks and induced connectivity, checks all cardinalities up through the minimum at each n=5..10, verifies degree signatures, and constructs both exchange relations at n=5. Reproduced counts 12,15,252,1512,1512,3969. The PDF proof and finite replay are not interchangeable; the argument above exhausts all n. The frozen Python verifier intentionally stops at size 3 for n=6 despite the broader wording in the original Verification paragraph.

## originality

PASS

The supported distinct result is the connected closed-parity optimizer classification, including the exact additional branches at n=8 and n=10 and the specific optimum replacement relation. The record already disclaims priority for the Petersen weight-five count. The even/odd partition of Hamilton cycles is also known, but the closest inspected group-testing result does not identify the two-replacement exchange graph. The comparison is bounded, not a priority guarantee.

## value

PASS

The rank-two Kneser family is canonical. Closed parity on all ground-set pairs unexpectedly allows only three exceptional ground-set orders to change the minimum configuration types, and two of those change multiplicity without changing size. The exact labelled classification and the contrast between frozen one-replacement and connected two-replacement optima identify structure not visible in the known Petersen weight count or in ordinary domination.

The dated certificate retains the supplied scientific assessment, sources and limitations.
