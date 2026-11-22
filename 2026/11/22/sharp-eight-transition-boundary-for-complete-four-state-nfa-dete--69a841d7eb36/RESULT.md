# Sharp eight-transition boundary for complete four-state NFA determinization

## Finding
Consider all labeled epsilon-free nondeterministic finite automata with state set \(Q=\{0,1,2,3\}\), fixed start \(\{0\}\), ordered binary alphabet \(\{a,b\}\), arbitrary transition relation, and arbitrary set \(F\subseteq Q\) of final states. There are \(32\) possible labeled transitions \((p,c,q)\). Let \(R\) be the number of subsets reachable from \(\{0\}\) in the completed subset construction (including \(\varnothing\) when reachable), and \(M\) the number of states of the minimal complete DFA for the language.

**Sharp sparsity cutoff.** Every transition relation with at most seven edges satisfies \(R<16\), hence \(M<16\). Among the \(\binom{32}{8}=10{,}518{,}300\) relations with exactly eight edges, exactly \(5{,}808\) have \(R=16\). Across these relations and the \(16\) choices of \(F\), exactly \(56{,}544\) labeled automata have \(M=16\). Thus precisely eight labeled edges are necessary and sufficient for the full sixteen-state minimal-determinization blow-up. No assertion is made for more than eight edges.

The counts by final-state mask \(f=\sum_{i\in F}2^i\), for \(f=1,\dots,15\), are: \(3900,4196,3660,4196,3660,3696,3612,4196,3660,3696,3612,3696,3612,3636,3516\); mask zero gives zero.

## Assumptions and scope
Edges are individually specified triples, not state-letter entries. Distinct ordered alphabets, labeled states, and accepting sets are counted separately; no quotient by relabeling is taken. Multiple outgoing destinations and absent transitions are allowed. The initial state is fixed to zero, no epsilon transitions are allowed, and untrimmed automata are included. The empty subset is a completed dead state. The recognized language accepts a word when its resulting subset meets \(F\).

## Proof
There are \(4\cdot2\cdot4=32\) eligible transition triples. Encode each relation by a unique 32-bit mask. For each mask with exactly \(e\) bits, \(0\le e\le8\), reconstruct both four-by-four Boolean adjacency matrices, then extend them to all sixteen subsets by union: \(\delta_c(S)=\bigcup_{p\in S}\delta_c(p)\). Starting from \(\{0\}\), breadth-first traversal through the two subset transitions computes all and only reachable subsets, since every word is a path in this finite directed graph and every discovered node is reached by a word.

The independent complete evaluations in the included standalone programs give, for edge counts \(e=0,1,\ldots,8\), respectively, \(0,0,0,0,0,0,0,0,5808\) relations with all sixteen subsets reachable. The numbers of enumerated masks at each edge count are the binomial coefficients \(\binom{32}{e}\), explicitly checked by the program. In particular the zero results for the first eight budgets establish the global lower bound for all relations with at most seven edges.

For each full-reach relation, label subset \(S\) initially accepting exactly if \(S\cap F\ne\varnothing\). The first program repeatedly refines the partition by the pair of successor-class labels until it stabilizes. By induction on distinguishing-suffix length, the stable classes are precisely the Myhill–Nerode classes. The second program independently marks a pair of subsets distinguishable if their acceptance differs, or if a letter sends them to a distinguishable pair, until the marking reaches a fixed point. There are sixteen minimal states precisely when all \(120\) unordered distinct pairs become distinguishable. Both methods return \(56{,}544\) full-minimal cases, with the final-mask counts stated above.

For an explicit sharp witness take \(F=\{1\}\) and transitions:

| Source state | \(a\) destinations | \(b\) destinations |
|:--|:--|:--|
| 0 | \(\{2,3\}\) | \(\{2\}\) |
| 1 | \(\{3\}\) | \(\{1\}\) |
| 2 | \(\{1\}\) | \(\{0\}\) |
| 3 | \(\{0\}\) | \(\varnothing\) |

There are exactly eight triples in this table. The first program identifies its transition mask as integer `19141260` and final mask as `2`; a direct traversal reaches all sixteen subsets and the pair-separation test distinguishes each pair. This supplies attainability without relying only on the aggregate counts.

## Verification
Compile and run `verify_sparse_4_full.cpp` and `verify_sparse_4_independent.cpp` using a C++17 compiler with optimization. The first enumerates every relation having at most eight edges, returns \(5{,}808\) full-reach relations and \(56{,}544\) fully minimal eight-edge automata; the second separately enumerates every eight-edge relation and uses reverse distinguishability closure instead of partition refinement. The independent agreement includes each of the fifteen nonzero final masks. The included output transcripts are diagnostic only; the executable exhaustive procedures are the finite proof certificates.

## Relationship to prior work
The full subset-construction bound \(2^n\), the distinction between reachable subset states and minimal-DFA states, and explicit worst-case exponential witnesses are classical. Baburin and Cotterell (2026) investigate determinization complexity and parameterized bounds, but do not report the exact minimal transition budget and complete eight-edge count for the labeled four-state binary family. Their earlier analysis of the subset construction (2025) provides general complexity bounds, not this finite census. A separate census for the three-state single-final family has different parameters and does not determine the four-state threshold.

## Limitations
This is an exhaustive finite theorem restricted to four labeled states, two ordered letters, singleton initial state, and at most eight transition edges. It is not a theorem asserting an eight-edge formula at other state sizes, or a complete distribution for higher budgets. The enumeration proofs are computer assisted, and no independent human audit has been performed. Similar numeric tables not indexed by the searched literature remain a priority risk.

## References
1. I. Baburin and R. Cotterell, *Towards A Parametrized Complexity of Determinization*, arXiv:2611.10911v1, first public 2026-11-07. https://arxiv.org/abs/2611.10911
2. I. Baburin and R. Cotterell, *A Close Analysis of the Subset Construction*, arXiv:2407.09891 (consulted v6). https://arxiv.org/abs/2407.09891
3. M. O. Rabin and D. Scott, *Finite Automata and Their Decision Problems*, IBM Journal of Research and Development 3 (1959), 114–125.
