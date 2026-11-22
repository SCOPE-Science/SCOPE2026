# The first reversal savings in cyclic golden-mean word covers

## Finding

Let \(\mathcal G_n\) consist of binary words of length \(n\) containing no adjacent `11`. A cyclic binary word \(C\) *covers up to reversal* if it has no cyclic adjacent `11` and, for every \(w\in\mathcal G_n\), at least one of \(w\) and its reverse occurs as a cyclic length-\(n\) factor of \(C\). For orders \(n=2,3,4,5,6\), the exact shortest lengths are respectively
\[
L_n=(3,6,10,17,23).
\]
For \(n=6\), the explicit optimal circle `01000010001001010100000` has length \(23\). At orders \(2\) through \(5\), permitting reversal does not shorten the corresponding oriented golden-mean covering cycles. **Order six is the first reversal-saving order**: the shortest oriented cycle has length \(28\), so reversal saves exactly five symbols.

## Assumptions and scope

A cyclic length-\(n\) factor starts at any one of the circle's positions and continues cyclically, possibly traversing the circle more than once; a no-`11` circular host is a cyclic binary sequence with no adjacent ones including across the wrap. The position count is the circle's length, not its linearization plus a prefix. The theorem concerns \(2\le n\le6\), not arbitrary orders, and only identifies optimum *lengths*, not the counts of optimizers.

## Proof

Each permitted length-\(n\) word corresponds to a directed edge of the golden-mean order-\((n-1)\) overlap graph: an edge labeled \(w\) goes from its first \(n-1\) symbols to its final \(n-1\) symbols. Every cyclic no-`11` host is a closed directed walk in this graph, and every closed directed walk yields a cyclic no-`11` host. The vertex set consists exactly of admissible \((n-1)\)-words.

Partition the admissible \(n\)-words into reversal classes \([w]=\{w,w^R\}\). There are respectively \(2,4,5,9,12\) such classes for \(n=2,3,4,5,6\). Fix a starting vertex \(s\). Assign each reversal class a distinct bit. An exact breadth-first search has states \((v,M)\), with current overlap vertex \(v\) and bit mask \(M\) of reversal classes seen so far; the initial state is \((s,0)\). For each legal edge \(w:v\to v'\), transition to \((v',M\cup\{[w]\})\) at cost one. The shortest cyclic cover starting at \(s\) is the first positive-length transition arriving at \((s,\text{all-bits})\). Taking the minimum over *every* admissible starting vertex proves the global optimum, because every possible cyclic host determines a closed walk with some starting vertex, and no candidate is omitted. The finite algorithm is written in full in `verify_dp.py`, including exact integer state keys and exhaustive queue traversal; it yields the five lengths above and explicit witnesses.

Independently, `verify_bruteforce.py` directly enumerates **every** circular binary host of every length strictly below the claimed optimum for each of the five orders and checks the cyclic no-`11` and reversal-covering predicates literally. None qualifies. It independently checks explicit witnesses at every claimed length:

| Order | Optimal cycle |
| --- | --- |
| 2 | `010` |
| 3 | `010100` |
| 4 | `0100101000` |
| 5 | `01000100101010000` |
| 6 | `01000010001001010100000` |

Thus these lower bounds and matching constructions establish the exact finite theorem. For comparison, the known oriented golden-mean shortest-cover theorem gives \(F_{n+2}+F_n-1\) symbols, where \(F_0=0,F_1=1\). At the five stated orders its lengths are \(3,6,10,17,28\), proving the first strict savings at six.

## Verification

Run `python3 verify_dp.py` and `python3 verify_bruteforce.py`. The former exhaustively visits reachable directed overlap-graph states; the latter enumerates actual circular words without using that graph model. Both passed for every order two through six. The code is the complete finite proof's exhaustive certificate, not a sample or extrapolation to higher orders.

## Relationship to prior work

Burris, Motta and Shipman (2016) study unoriented de Bruijn sequences, supplying the reversal-quotient graph framework without this golden-mean source restriction. Published cyclic golden-mean covering results establish the corresponding **oriented** minima for all orders, but that stronger all-oriented-factor task does not determine the unoriented-reversal optimum. Previously published binary unoriented covering results address unrestricted source words, not the no-adjacent-one source. This theorem identifies the first natural point at which reversal gives a strict saving for the constrained source.

## Limitations

No general formula is claimed beyond order six. The optimum counts and uniqueness classes are not enumerated. Published general algorithms for unoriented graph Eulerization may subsume the finite search methodology; the exact restricted five-order boundary may have appeared in unindexed computations, and independent mathematical verification remains outstanding. The exhaustive programs check complete finite domains rather than representing an infinite-order proof.

## References

1. C. S. Burris, F. C. Motta, P. D. Shipman, *An Unoriented Variation on de Bruijn Sequences*, first public preprint August 30, 2016, https://arxiv.org/abs/1608.08480 .
2. *Sharp Fibonacci length for cyclic covers avoiding adjacent ones*, published result with oriented length formula, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-fibonacci-length-for-cyclic-covers-avoiding-adjacent-ones--115d2faf86fa .
3. *Shortest cyclic binary reversal covers through order five*, published unrestricted benchmark, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-shortest-cyclic-binary-reversal-covers-through-order-five--d2dd86a41c28 .
4. *Complete small-order census of minimum golden-mean cyclic covering words*, unrestricted-orientation benchmark, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-complete-small-order-census-of-minimum-golden-mean-cyclic-coveri--50305dee27be .
