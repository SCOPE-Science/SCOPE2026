# Exact bipartite-cactus state complexity of prime-power length predicates

## Finding
Let \(p\) be a prime, \(k\geq 1\), and \(m=p^k\geq4\). Let \(\Sigma\) be any finite nonempty alphabet. Fix a genuinely multiresidue set \(R\subseteq\mathbb Z/m\mathbb Z\), with \(2\leq|R|\leq m-2\), having *least translation period* \(m\):
\[
R+t=R\pmod m\quad\Longrightarrow\quad t\equiv0\pmod m.
\]
Define the length predicate
\[
L_{m,R}=\{w\in\Sigma^*:|w|\bmod m\in R\}.
\]
Write \(s_{\mathrm{NFA}}(L)\), \(s_{\mathrm{bip}}(L)\), and \(s_{\mathrm{bc}}(L)\) for the least state counts of epsilon-free NFAs with a single initial state recognizing \(L\), respectively with unrestricted underlying transition graph, a bipartite underlying transition graph, or a bipartite-cactus underlying transition graph. The underlying graph is simple and undirected: transition directions and labels are forgotten; self-loops and parallel edges are suppressed. NFAs may be incomplete and may have multiple final states.

**Theorem.** For every choice above,
\[
\boxed{s_{\mathrm{NFA}}(L_{m,R})=m,\qquad
s_{\mathrm{bip}}(L_{m,R})=s_{\mathrm{bc}}(L_{m,R})=\operatorname{lcm}(m,2).}
\]
Both upper bounds are attained by complete deterministic automata (hence also by unambiguous NFAs). In particular, the graph restriction forces exactly twice as many states for odd prime powers, and no extra states for powers of two. There are exactly
\[
\boxed{2^{p^k}-2^{p^{k-1}}-2p^k}
\]
residue sets that meet both the least-period and genuinely multiresidue conditions, so this is an exact classification of that many languages for each prime power \(m\geq4\).

## Assumptions and scope
All words are finite, including the empty word. The alphabet is nonempty and may have one or more letters. The hypothesis \(2\leq|R|\leq m-2\) excludes both singleton predicates and their complements, as well as the empty and full sets. The least-period assumption is separate and necessary. Acceptance uses the ordinary existence of an accepting run, with no epsilon transitions. All state counts include unreachable states, though an optimum cannot benefit from them. Bipartiteness concerns the underlying simple undirected graph; this definition does not disallow formal self-loop transitions, which are handled in the lower-bound argument. A cactus is a graph in which every edge lies on at most one simple undirected cycle.

## Proof
**Lemma (period extracted from accepting cycles).** Let an epsilon-free NFA with \(q\) states accept infinitely many words on a fixed unary alphabet \(\{a\}\). Let \(C\) be the nonempty finite set of lengths of directed simple cycles lying on some initial-to-final path, with loops counted as length-one directed cycles, and put \(P=\operatorname{lcm}(C)\). Then the set of accepted word lengths is eventually periodic with period \(P\).

For any accepted word \(a^N\) with \(N\geq q\), choose an accepting path of length \(N\). It repeats a vertex. By selecting a repeated-vertex interval of smallest positive length, one obtains a directed simple cycle of some length \(c\in C\) occurring within that accepting path. The segment can be traversed an additional \(P/c\) times, giving an accepting path of length \(N+P\). Thus for all \(N\geq q\), acceptance at \(N\) implies acceptance at \(N+P\).

In each of the finitely many congruence classes modulo \(P\), either no accepted length at least \(q\) exists, or the first such length exists and all subsequent lengths in that class are accepted. Taking a threshold exceeding every such first length establishes, for all sufficiently large \(N\), the two-way equivalence between acceptance at \(N\) and at \(N+P\). This proves the lemma. Notice that the one-sided pumping implication is not mistakenly assumed to be an equivalence without this per-residue argument.

**Lower bound.** Fix a letter \(a\in\Sigma\), and restrict all transitions to those labeled \(a\). The unary restriction recognizes exactly \(\{a^N:N\bmod m\in R\}\). Since \(R\) is nonempty, this language is infinite; the lemma provides an eventual period \(P\). Because the language is *already* periodic modulo \(m\), eventual periodicity by \(P\) implies \(R+P=R\) modulo \(m\): for each residue choose arbitrarily large lengths belonging to that residue and compare lengths separated by \(P\). The least-period assumption therefore gives \(m\mid P\).

As \(m=p^k\) is a prime power and \(P\) is a least common multiple of cycle lengths, some directed simple cycle on an accepting path has length \(c\) divisible by \(m\). That cycle contains \(c\) distinct states, so every epsilon-free NFA recognizing the language has at least \(m\) states.

If the underlying graph is bipartite, this selected cycle, since \(c\geq m\geq2\), is not a self-loop. A directed simple cycle of length two uses an undirected edge twice and has even length; a directed simple cycle of length at least three traces a simple undirected cycle, which must be even in a bipartite graph. In either case \(c\) is even. Since \(m\mid c\), we have \(\operatorname{lcm}(m,2)\mid c\); hence every bipartite-graph NFA has at least \(\operatorname{lcm}(m,2)\) states. This also applies to bipartite-cactus NFAs.

**Matching upper bounds.** For any positive integer \(d\) divisible by \(m\), take states \(\mathbb Z/d\mathbb Z\), initial state zero, and the deterministic transition \(j\overset{a}{\longrightarrow}j+1\pmod d\) for *every* input letter \(a\in\Sigma\). Mark precisely those states \(j\) with \(j\bmod m\in R\) as accepting. After any word of length \(N\), the state is \(N\bmod d\), so this complete DFA recognizes exactly \(L_{m,R}\). Choosing \(d=m\) proves the unrestricted upper bound. Choosing \(d=\operatorname{lcm}(m,2)\) gives an even directed cycle. Its simple underlying undirected graph is an even cycle if \(d\geq4\), and a single edge if \(d=2\). Both are bipartite cacti. This establishes all stated equalities.

**Count of predicates.** A residue set modulo \(p^k\) has a nontrivial translation period if and only if it is invariant under translation by \(p^{k-1}\). Indeed, every nonzero translation generates a subgroup containing that translation, and in a cyclic group of prime-power order every nontrivial subgroup contains the unique subgroup of order \(p\), generated by \(p^{k-1}\). The latter translation partitions the residue set into \(p^{k-1}\) disjoint orbits, each of size \(p\). There are \(2^{p^{k-1}}\) invariant subsets among the \(2^{p^k}\) subsets. The \(m\) singletons and \(m\) complements of singletons all have least period \(m\), and these two collections are disjoint for \(m\geq4\). Removing these \(2m\) boundary predicates gives the displayed count. This completes the proof.

## Verification
Run \(\texttt{python3 verify.py}\) from the directory containing this document and the accompanying script. It checks 935 primitive residue predicates, including previously known boundary controls, across eleven prime-power moduli, and 55,567 accepted/rejected word-length instances in the explicit even-cycle witnesses. A separate exhaustive enumeration tests 214,660 bipartite unary NFA configurations, including every labeled transition relation and final-state choice through four states, and finds no smaller witness for any nontrivial modulo-three residue predicate. For this finite exhaustive test, language comparison through the product of the subset automaton and the three-state residue counter uses the bound \(3\cdot2^q\) on the number of product states.

These finite checks test construction and boundary behavior; the lower bounds for all moduli and arbitrary state counts are established by the proof, not by the experiments. Expected output is preserved in \(\texttt{verification_output.txt}\).

## Relationship to prior work
Grobler, Koziel, and Siebertz (arXiv:2610.11717v1, 2026) proved that every regular language has an epsilon-free NFA whose underlying transition graph is a bipartite cactus. Their conclusion explicitly leaves the quantitative state overhead unresolved. The theorem here determines that overhead exactly for all primitive prime-power modular length predicates and shows that the weaker condition of bipartiteness costs precisely the same as the full bipartite-cactus requirement on this family.

Previously established exact results for a single accepted residue concern the languages \(\{w:|w|\equiv r\pmod m\}\), and do not by themselves imply the NFA minimum for residue sets with at least two accepted and two rejected residues. Those singleton predicates and their complements are not included in the present novelty claim. Czerwiński and collaborators (arXiv:2302.06435) analyze unary NFAs and UFAs but do not impose the bipartite underlying-graph restriction. Kutrib, Malcher, and Schneider (doi:10.1007/s00236-021-00402-0) study a different model, called an *undirected automaton*, in which each transition has a reverse transition with the same label. That symmetry restriction is stronger and is not equivalent to merely requiring an undirected underlying graph to be bipartite. The present theorem does not assert that their model recognizes the displayed modular languages.

## Limitations
The result is claimed here only for prime-power moduli \(m\geq4\) and residue sets with no nonzero translation symmetry and with at least two accepted and two rejected residues. It does not determine the minimum bipartite-cactus representation size for general composite moduli or nonprimitive residue sets, and does not settle the worst-case blow-up for arbitrary regular languages. Historical priority is limited by the coverage of examined literature; an equivalent characterization in unindexed work cannot be excluded. Independent verification beyond the accompanying checks has not been performed.

## References
1. M. Grobler, T. Koziel, S. Siebertz, *Every Regular Language Has a Bipartite Cactus Automaton*, arXiv:2610.11717v1 (first public version, 8 October 2026), EPTCS 454 (2026), 117–129, doi:10.4204/EPTCS.454.9.
2. W. Czerwiński et al., *Languages given by Finite Automata over the Unary Alphabet*, arXiv:2302.06435 (2023; later versions).
3. M. Kutrib, A. Malcher, C. Schneider, *Finite automata with undirected state graphs*, Acta Informatica 59 (2022), 163–181, doi:10.1007/s00236-021-00402-0.
