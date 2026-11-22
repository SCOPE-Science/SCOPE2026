# The exact 7,311-state complexity of dinucleotide secondary-structure avoidance

## Finding

Let \(\Sigma=\{A,T,C,G\}\) with Watson–Crick complementation \(\overline A=T\), \(\overline T=A\), \(\overline C=G\), and \(\overline G=C\). For a finite linear word \(w\in\Sigma^*\), define a forbidden pair to be two **disjoint** contiguous length-two factors \(ab\) and \(cd\), appearing in either temporal order, satisfying \(ab=\overline d\,\overline c\). Let \(L\) be the language of words without any forbidden pair (the stem-length-two secondary-structure-avoidance language).

**Theorem.** The minimal **complete, deterministic, one-pass** finite automaton recognizing \(L\), with every finite word accepted or rejected at its end, has exactly **7,311 states**, comprising 7,310 accepting states and one rejecting sink. Every pair of inequivalent reachable states is distinguished by an appended word of length at most five. Consequently any fixed-width binary representation of the automaton state requires at least 13 bits, and 13 bits suffice.

The exact pre-minimization reachable-state count is 22,986 including the sink. The successive numbers of inequivalent reachable states when test suffixes of length at most \(0,1,2,3,4,5,6\) are permitted are, respectively,
\[
2,\quad17,\quad2715,\quad6807,\quad7295,\quad7311,\quad7311.
\]

## Assumptions and scope

Words are linear and indexed, including the empty word. Two dinucleotides are disjoint if their position sets are disjoint; adjacent factors such as positions \(1,2\) and \(3,4\) count as disjoint, but overlapping factors such as positions \(1,2\) and \(2,3\) do not. No extra minimum loop separation is imposed. The DNA alphabet, involution, and disjointness rule are fixed as stated. We measure the exact number of states of a complete deterministic left-to-right automaton, not of a nondeterministic, two-way, probabilistic, or biochemical detector.

## Proof

**Exact recognizer.** Encode nucleotides as \(0=A,1=T,2=C,3=G\), with complement permutation \(\kappa=(1,0,3,2)\). Encode a dinucleotide \(ab\) by \(4a+b\) and define its reverse-complement index
\[
\rho(4a+b)=4\kappa(b)+\kappa(a).
\]
A nonrejecting state is a triple \((a,p,S)\), in which \(a\) is the last nucleotide (or a special absent value for the empty word), \(p\) is the most recent dinucleotide (or absent if the length is at most one), and \(S\subseteq\{0,\ldots,15\}\) is the set of all dinucleotides whose ending position is **strictly before the current last position**. Thus, for a prefix of length \(r\), \(S\) contains the factors ending at positions at most \(r-1\). The initial state has absent \(a,p\) and empty \(S\).

On reading a new nucleotide \(b\) from a nonempty prefix, the new factor is \(u=4a+b\). Reject exactly when \(\rho(u)\in S\); otherwise update to
\[
(b,u,S\cup\{p\}),
\]
ignoring the absent \(p\). When the prefix was empty, just store \(b\). A rejected word enters a permanent nonaccepting sink. The test compares the new factor ending at position \(r+1\) with exactly those earlier factors ending at positions at most \(r-1\); these, and only these, are disjoint from the new factor occupying positions \(r,r+1\). Induction on prefix length therefore proves that this complete automaton accepts precisely \(L\). Its theoretical state space is finite because the mask \(S\) has only 16 possible bits.

**Reachability and exact finite count.** Start at the empty state; visit all four input transitions of every newly discovered nonrejecting triple, assigning canonical IDs in breadth-first discovery order. This exhausts all reachable triples since every transition is explored and the triple domain is finite. The complete standalone checker `verify_ssa2.py` obtains exactly 22,985 reachable nonrejecting triples and a reachable rejecting sink, for a total of 22,986 reachable states. Unlike sampling input lengths, this is a full traversal of the finite state graph.

**Minimality.** Partition the 22,986 states first by whether the empty suffix is accepted. Repeatedly split any two states distinguished by appending one letter before a suffix already distinguished, using the transition signature consisting of its fixed acceptance bit and the four destination-class labels. By induction, partition \(k\) equates states if and only if they accept exactly the same test suffixes of length at most \(k\). The exact stable class counts at \(k=0,1,2,3,4,5,6\) are those displayed above. Equality between the counts at five and six implies the partition is right-invariant; hence no longer suffix can split a class. By the Myhill–Nerode theorem its 7,311 classes are exactly the distinct right languages of the reachable states, giving both the 7,311-state lower bound and the minimal quotient construction. Since there is one rejecting sink right language and all other states have an accepting empty suffix, precisely 7,310 minimal states are accepting. Since \(2^{12}<7311\le2^{13}\), fixed-width state storage needs exactly 13 bits.

## Verification

Run `python3 verify_ssa2.py` with Python 3 and no external packages. The checker independently applies inverse-transition Hopcroft partition splitting as well as forward Moore suffix refinement. It checks equality at 7,311 classes, verifies that all 22,986 constructed states are represented in the partitions, and directly tests the original disjoint-index definition against the automaton on all 349,525 words of lengths zero through nine. The direct finite-word tests provide a separate semantic check; the proof for arbitrary lengths comes from the induction and the fully explored finite transition graph, **not** from extrapolating those tests.

## Relationship to prior work

Nguyen et al. (first posted February 27, 2023) formulate secondary-structure avoidance with arbitrary stem length and construct high-rate codes. Chu, Wang, and Zhang (first posted April 22, 2023) obtain sharp asymptotic capacities for stem lengths two and three using generating sets and their transition digraphs. Their six-vertex example is a graph for a **restricted** admissible dinucleotide set, not a recognizer for the complete language containing all nonoverlap-avoiding words. Neither inspected presentation gives the minimum deterministic state count for the entire length-two avoidance language or a five-symbol bound on distinguishing suffixes. The result here addresses exact online recognition memory, not asymptotic code capacity. The related 2023 work of Zhang and Wu introduces a stricter minimum-loop-distance variant and sequence-replacement codes, without a comparable exact minimal DFA claim. The usual DFA-minimization theorem is acknowledged as classical; the specific 7,311-state invariant and its exhaustive certificate are the contribution.

## Limitations

The theorem is for stem length exactly two and does not impose a physical loop-length requirement. It does not give the minimal size of a nondeterministic machine, optimize DNA code rate, or predict thermodynamic folding. No claim is made for different alphabets, stem lengths, or circular words. The finite-state enumeration is small enough to reproduce exactly but still warrants independent review, and older unindexed automata formulations could affect historical priority. No independent mathematical audit has been conducted.

## References

1. T. T. Nguyen, K. Cai, H. M. Kiah, D. T. Dao, and K. A. S. Immink, *On the Design of Codes for DNA Computing: Secondary Structure Avoidance Codes*, arXiv:2302.13714, initially posted 2023-02-27. https://arxiv.org/abs/2302.13714
2. H. Chu, C. Wang, and Y. Zhang, *Improved constructions of secondary structure avoidance codes for DNA sequences*, arXiv:2304.11403, initially posted 2023-04-22. https://arxiv.org/abs/2304.11403
3. Myhill–Nerode theorem and classical DFA partition refinement, standard automata theory; used here only for the final exact minimality inference from the computed finite-state partition.
4. R. Zhang and H. Wu, *On secondary structure avoidance of codes for DNA storage*, Computational and Structural Biotechnology Journal (2023), doi:10.1016/j.csbj.2023.11.035. https://pmc.ncbi.nlm.nih.gov/articles/PMC10749251/
