# Review of uniform partial-derangement greedy matching

## Correctness

**PASS.** The exact transition probabilities partition all available edges. The identities for \(U_k\) and \(V_k\) are rational-algebra consequences of those probabilities. The bound \(0\le\eta_{k,t}\le6/[k(k-1)]\) controls accumulated potential loss uniformly over all possible surviving forbidden pairs. The comparison to \(1/k\) yields the stated universal \(36v_{n,r}\) bound. Independently implemented unmatched-subset computations verify exact small cases; they are supporting tests, not the proof of the infinite limit.

## Originality

**PASS, with historical priority risk.** The source's random-edge algorithm (Arnosti 2021) is known, as are general algorithmic comparisons and counts of perfect matchings avoiding a fixed diagonal (Johnston–Kayll–Palmer 2022). A previous first-order crown-graph analysis also includes the finite state recurrence; this review does not claim that recurrence as new. The claim assessed is the sharp \(4v_{n,r}\log n\) correction, complete with a uniform constant-order remainder across every deletion size. No inspected primary statement or mathematical-record result was shown to imply that coefficient. General older greedy-matching full texts were not completely accessible and remain a priority limitation.

## Value

**PASS.** A fixed-size nonindependent forbidden-pair constraint creates a failure probability of leading order \(r/n^2\); interactions of distinct constraints generate a smaller, logarithmically enhanced term of order \(r(r-1)\log n/n^4\). The precise term answers a natural random sequential matching question at both sparse and dense levels of forbidden pairs, while detecting the first nontrivial pair interaction. It provides more than an isolated finite table or an automatic restatement of a first-order asymptotic.

## Closest literature and limitations

Arnosti (2021), DOI 10.1287/stsy.2021.0082, gives algorithm definitions and performance comparisons on random bipartite graphs; Johnston, Kayll and Palmer (2022), arXiv:2209.11319, enumerate perfect matchings in graphs with deleted forbidden pairs. Dyer and Frieze (1991), DOI 10.1002/rsa.3240020104, and Miller and Pritikin (1997), DOI 10.1002/(SICI)1098-2418(199705)10:3<353::AID-RSA5>3.0.CO;2-V, study randomized greedy matching generally. Their full texts were not verified, so historical overlap is not excluded. This result concerns only disjoint edge deletions from balanced complete bipartite graphs, not arbitrary forbidden subgraphs or other greedy selection rules.

Self-review: passed. Independent audit: not yet performed.
