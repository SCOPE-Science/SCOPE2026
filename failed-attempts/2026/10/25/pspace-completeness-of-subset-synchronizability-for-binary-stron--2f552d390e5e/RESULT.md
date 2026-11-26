# PSPACE-completeness of subset synchronizability for binary strongly connected automata

## Finding

For finite complete deterministic automata \(A=(Q,\{0,1\},\delta)\) whose transition graph is strongly connected, deciding whether a given subset \(S\subseteq Q\) can be synchronized—whether there exists \(w\in\{0,1\}^*\) with \(|\delta(S,w)|=1\)—is PSPACE-complete under polynomial-time many-one reductions.

## Assumptions and scope

A complete deterministic finite automaton is \(A=(Q,\{0,1\},\delta)\), where \(Q\) is finite and \(\delta:Q\times\{0,1\}\to Q\) is total. Extend \(\delta\) to words by composition and to a subset by
\[
\delta(S,w)=\{\delta(s,w):s\in S\}.
\]
The input explicitly gives the transition table and \(S\subseteq Q\). The transition graph is strongly connected when, for every \(p,q\in Q\), some word \(u\in\{0,1\}^*\) satisfies \(\delta(p,u)=q\). The decision question is whether there exists a word mapping every state in \(S\) to one common state. The theorem concerns decision complexity, not the length of a shortest such word for each individual instance.

## Proof

**Membership in PSPACE.** The subset transition graph has at most \(2^{|Q|}\) vertices, one for each subset of \(Q\), and an edge \(T\to\delta(T,a)\) for each letter \(a\in\{0,1\}\). A singleton is reachable from \(S\) if and only if \(S\) is synchronizable. If a singleton is reachable, a shortest path visits no subset twice, so it has fewer than \(2^{|Q|}\) edges. A nondeterministic algorithm stores the current subset and an \(|Q|\)-bit step counter, guesses at most \(2^{|Q|}-1\) letters, and accepts on reaching a singleton. This uses polynomial space; \(\mathrm{NPSPACE}=\mathrm{PSPACE}\).

**PSPACE-hardness.** The unrestricted subset-synchronizability problem is PSPACE-complete. Vorel's reduction restricts it to the stated class in two polynomial steps.

1. The first construction replaces each original state by a paired copy and adds two auxiliary states and a polynomial number of letters. The added transitions make the new transition graph strongly connected. A swap congruence pairs the copies and ensures that no successful subset-reset word can merge a paired pair. Consequently, a subset is synchronizable in the constructed automaton exactly when the original subset was synchronizable; the state and alphabet growth is polynomial.
2. For a \(k\)-letter strongly connected automaton, the alphabet-reduction construction uses states \(Q\times\Sigma\) and two letters \(\alpha,\beta\). The letter \(\beta\) advances the alphabet pointer; \(\alpha\) applies the pointed-to original transition and resets the pointer. An original letter \(a_i\) is encoded by \(\beta^i\alpha\), so a word \(a_{i_1}\cdots a_{i_t}\) is represented by \(\beta^{i_1}\alpha\cdots\beta^{i_t}\alpha\). Starting from \(S\times\{a_0\}\), subset synchronizability is preserved. The new automaton has \(k|Q|\) states, a binary alphabet, and remains strongly connected.

Both transformations are polynomial-time many-one reductions. Thus the restricted problem is PSPACE-hard; together with membership, it is PSPACE-complete.

## Verification

The definitions, state-set action, and reduction hypotheses were checked against the full primary text of Vorel's paper, including the strong-connectivity reduction, the alphabet-reduction lemma, and the theorem on computational complexity. The proof uses an exponential-size implicit subset graph only for a polynomial-space decision procedure; it does not claim a polynomial-time algorithm or infer impossibility from a finite search. The hardness argument is an analytical reduction, so no computational experiment is needed for the claim.

The earliest verified public version is arXiv:1403.3972v1, dated 16 March 2014. The journal version appeared later. The primary MSC classification is 68Q45.

## Relationship to prior work

The unrestricted subset-synchronizability problem was already known to be PSPACE-complete, with reductions connected to the common-word problem for finite acceptors. That result alone does not establish hardness after imposing both a binary alphabet and strong connectivity: a restriction can reduce complexity. Vorel's two polynomial reductions are the substantive step that transfers hardness to this constrained class. A later paper on synchronization problems in automata without non-trivial cycles also states the same restricted complexity result; that later source corroborates the statement but postdates the earliest public version.

## Limitations

The theorem is a worst-case decision-complexity classification. It does not say that every binary strongly connected automaton has a synchronizable subset, does not provide a polynomial-time method for finding a synchronizing word, and does not by itself give a lower bound on the shortest word for any fixed automaton. The foundational unrestricted PSPACE-completeness is cited in Vorel's paper to earlier literature; the restriction-preserving reductions are reconstructed here from Vorel's full text.

## References

1. Vojtěch Vorel, “Subset Synchronization and Careful Synchronization of Binary Finite Automata,” arXiv:1403.3972, first submitted 16 March 2014; *International Journal of Foundations of Computer Science* 27(5) (2016), 557–577, DOI 10.1142/S0129054116500167.
2. B. K. Natarajan, “An algorithmic approach to the automated design of parts orienters,” *Proceedings of the 27th Annual Symposium on Foundations of Computer Science* (1986), 132–142.
3. S. Sandberg, “Homing and synchronizing sequences,” in *Model-Based Testing of Reactive Systems*, Lecture Notes in Computer Science 3472 (2005), 5–33.
4. “Synchronization Problems in Automata without Non-trivial Cycles,” *Theoretical Computer Science*, DOI 10.1016/j.tcs.2018.12.026 (later corroboration).
