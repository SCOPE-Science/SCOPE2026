# Sharp parity cost for delayed unary modular languages in bipartite cactus automata

## Finding

Let \(n\ge2\) and \(t\ge1\) be integers. For the unary language
\[
L_{n,t}=\{a^{kn}:k\in\mathbb Z,\ k\ge t\},
\]
let \(b(n,t)\) denote the minimum state count of an epsilon-free NFA recognizing \(L_{n,t}\) which admits a proper two-coloring of **every actual transition** and whose simple undirected transition graph is a cactus. Then
\[
\boxed{b(n,t)=\begin{cases}tn+1,&n\text{ even},\\(t+1)n+1,&n\text{ odd}.\end{cases}}
\]
These minima are already attained by complete, unary **deterministic** automata whose undirected transition graph is a path with at most one added edge. The same minima hold when the cactus restriction is dropped but transition-compatible bipartiteness is retained. Unrestricted unary DFAs and NFAs require exactly \(tn+1\) states. Thus odd moduli impose an exact additional \(n\) states, whereas even moduli impose none.

## Assumptions and scope

An epsilon-free NFA has states \(Q\), a single initial state \(s\), a transition relation \(\Delta\subseteq Q\times\{a\}\times Q\), and a final-state set \(F\). Nondeterminism and partial transition relations are allowed. It is *transition bipartite* when some map \(\chi:Q\to\{0,1\}\) obeys \(\chi(p)\ne\chi(q)\) for every \((p,a,q)\in\Delta\). In particular no self-loop is permitted. The simple undirected graph has vertices \(Q\) and an edge \(\{p,q\}\) whenever a transition goes between distinct states; it is a cactus when every edge belongs to at most one simple cycle. The permitted automata here have a connected underlying graph; lower bounds also hold without connectedness. The state count includes the initial and all final states, and there are no epsilon transitions.

The transition-compatible coloring is essential. Merely asking that the simple undirected graph be bipartite *after erasing self-loops* is weaker and does **not** imply this theorem: the latter permits a one-step closed walk that violates the parity argument. The hypotheses match the loopless, transition-compatible constructions in Grobler–Koziel–Siebertz (2026).

## Proof

**1. A parity-simple-run lemma.** In any epsilon-free NFA with a transition-compatible two-coloring, consider the least accepted length of a specified parity, say \(\ell\). Every accepting run
\(q_0,q_1,\dots,q_\ell\) has pairwise distinct states. Indeed, if \(q_i=q_j\) for \(i<j\), then \(j-i\) is even because each transition flips the coloring. Delete the closed subrun from \(i\) to \(j\); the remaining sequence is an accepting run of length \(\ell-(j-i)\), strictly shorter and of the same parity, a contradiction. Therefore an automaton accepting a word whose length is smallest among its accepted lengths of that parity needs at least \(\ell+1\) states. Independently, without a bipartiteness hypothesis, an accepting run of globally minimum accepted length is simple: deleting any repetition yields a shorter accepted word.

**2. Lower bounds.** The globally shortest word in \(L_{n,t}\) has length \(tn\), yielding the general lower bound \(tn+1\). If \(n\) is odd, the consecutive accepted lengths \(tn\) and \((t+1)n\) have opposite parities; moreover \((t+1)n\) is the *first accepted length of its parity*. By Step 1, any transition-bipartite recognizing NFA therefore has at least \((t+1)n+1\) states. This argument does not use the cactus property and applies to arbitrarily nondeterministic automata.

**3. Sharp construction for even \(n\).** Take \(tn+1\) states \(v_0,v_1,\ldots,v_{tn}\), initial state \(v_0\), sole final state \(v_{tn}\), and deterministic transitions \(v_i\xrightarrow a v_{i+1}\) for \(0\le i<tn\), together with
\[
v_{tn}\xrightarrow a v_{(t-1)n+1}.
\]
The unique run first reaches the final state at length \(tn\), then every \(n\) steps, and at no other lengths. Every edge changes the parity of the state index because the returning directed cycle has even length \(n\). The undirected graph is a lollipop (a path joined to a single cycle) for \(n\ge4\), or a tree for \(n=2\). Both are bipartite cacti. Thus \(b(n,t)\le tn+1\) for even \(n\).

**4. Sharp construction for odd \(n\).** Take \((t+1)n+1\) states \(v_0,v_1,\ldots,v_{(t+1)n}\), initial state \(v_0\), final states \(v_{tn}\) and \(v_{(t+1)n}\), transitions \(v_i\xrightarrow a v_{i+1}\) along the path, and
\[
v_{(t+1)n}\xrightarrow a v_{(t-1)n+1}.
\]
The unique directed cycle has length \(2n\) and hence is even. Every transition changes index parity, so the automaton is transition bipartite; its undirected graph is one lollipop cactus. The first two accepting lengths are \(tn\) and \((t+1)n\). Revisiting either final state increases the run length by \(2n\), so the set of all accepted lengths is exactly
\[
\{tn+2jn:j\ge0\}\ \cup\ \{(t+1)n+2jn:j\ge0\}=\{kn:k\ge t\}.
\]
Therefore \(b(n,t)\le(t+1)n+1\). Together with Step 2 this proves the exact formula for all allowed \(n,t\).

**5. Unrestricted optimum and comparison.** The even-case path-and-return construction from Step 3 recognizes \(L_{n,t}\) for *every* \(n\), even or odd, if the bipartiteness restriction is removed; the directed cycle has length \(n\). The general shortest-run lower bound still gives \(tn+1\), which is consequently the minimum among unrestricted DFAs and NFAs. This completes the comparison. \(\square\)

## Verification

The standalone `checker.py` constructs the deterministic witnesses and checks their state counts, exact acceptance behavior over an explicit finite test range, transition-compatible two-coloring, graph connectedness, and the cactus property. A separate mathematical proof establishes the result for every \(n\) and \(t\), independent of finite testing. Run `python3 checker.py`: the shipped implementation passes 600 construction checks spanning \(2\le n\le34\), \(1\le t\le18\), together with additional boundary instances. Enumeration of finite lengths does not substitute for the general path-and-cycle argument.

## Relationship to prior work

Grobler, Koziel and Siebertz (2026) prove that every regular language has an epsilon-free NFA whose transition graph is a bipartite cactus. Their main theorem is qualitative. Their Section 4 explicitly identifies sharp state-complexity blow-up as a remaining problem. The present result determines exact minimum state cost for a natural two-parameter family of delayed modular unary languages. The lower bound applies to the larger class of all transition-bipartite NFAs, and matching witnesses already lie inside the cactus class.

Classical unary automata state-complexity results such as Pighizzini and Shallit treat different restrictions and operations. Kutrib, Malcher and Schneider (2022) impose a genuinely symmetric transition relation, unlike the directed transitions considered here; their unary machine class does not imply this result. The classical simple-accepting-path observation and elementary parity of bipartite walks are used transparently, rather than asserted as new lemmas.

## Limitations

The result covers unary languages consisting of all multiples of one modulus above a multiple-of-modulus threshold, and automata whose **actual transitions** switch a two-coloring. It does not give a universal blow-up bound for arbitrary regular languages, nor extend as stated to NFAs with self-loops ignored by an underlying-graph convention. No independent verification has been performed. Historical priority remains provisional: it is possible that the parity-path argument was applied to this family in an earlier uncatalogued source.

## References

1. M. Grobler, T. Koziel and S. Siebertz, *Every Regular Language Has a Bipartite Cactus Automaton*, EPTCS 454 (2026), 117–129. First public version 2026-10-08. https://arxiv.org/abs/2610.11717 ; https://doi.org/10.4204/EPTCS.454.9 . Especially the transition-compatibility definition in Section 2 and the open state-complexity question in Section 4.
2. G. Pighizzini and J. Shallit, *Unary Language Operations, State Complexity and Jacobsthal's Function*, International Journal of Foundations of Computer Science (2002). https://doi.org/10.1142/S012905410200100X .
3. M. Kutrib, A. Malcher and C. Schneider, *Finite Automata with Undirected State Graphs*, Acta Informatica 59 (2022), 163–181. https://doi.org/10.1007/s00236-021-00402-0 . The graph class studied there requires symmetric transitions, unlike the directed automata here.
