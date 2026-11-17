# The remanent language of the seven-cycle has exactly \(102\) deterministic states

## Finding
Let \(C_7\) be the undirected simple cycle on vertices \(\{0,1,\ldots,6\}\), with edges between consecutive vertices modulo seven. Give each of its seven edges one of the two possible orientations, independently. An oriented walk is recorded by a word over \(\{-,+\}\), with \(+\) for traversing an edge in its assigned direction and \(-\) for traversing against that direction. For an orientation \(O\), let \(L(O)\) be the set of words that label some walk in \(O\), with arbitrary start and finish vertices. Define the *remanent language* by

\[
R(C_7)=\bigcap_{O\text{ an orientation of }C_7}L(O).
\]

**Theorem.** The minimal complete deterministic finite automaton recognizing \(R(C_7)\) has exactly \(102\) states, including its rejecting sink. The simultaneous-subset determinization of all \(128\) orientations, **after merging every tuple with an empty component into one rejecting sink**, has exactly \(230\) reachable states (\(229\) accepting states and one rejecting sink). Thus an exact Myhill–Nerode quotient removes \(128\) reachable redundancies.

## Assumptions and scope
The underlying graph is the loopless undirected seven-cycle, each unoriented edge receives exactly one direction, and all seven vertices are simultaneously initial and final in each oriented-walk automaton. The alphabet has precisely the two edge-traversal signs; words may revisit graph vertices and edges. The empty word is accepted. The state count uses a **complete** DFA with both signs defined at every state and includes its rejecting sink. The claim is finite and exact for this one graph, not a formula for arbitrary cycles.

## Proof
For each mask \(m\in\{0,\ldots,127\}\), orient edge \(\{i,i+1\}\) (indices modulo seven) as \(i\to i+1\) when bit \(i\) of \(m\) is one, and oppositely otherwise. Let \(T_{m,+}(v)\) be all vertices reached from \(v\) along an edge in its oriented direction, and \(T_{m,-}(v)\) the analogous reverse-edge set. There are no other transitions. For every word \(w\), define \(S_m(w)\) as the possible terminal vertices of a walk labeled \(w\), starting at any of the seven vertices. Induction on the word length gives

\[
S_m(\varepsilon)=V(C_7),\qquad
S_m(wc)=\bigcup_{v\in S_m(w)}T_{m,c}(v)
\quad(c\in\{-,+\}).
\]

Consequently, \(w\in R(C_7)\) if and only if \(S_m(w)\ne\varnothing\) for all \(128\) masks. The tuple \((S_m(w))_{m=0}^{127}\) is therefore a deterministic recognition state; any tuple having an empty component can be replaced by one common absorbing rejecting state, since no extension can revive an empty component. Breadth-first enumeration from the tuple with all components equal to \(V(C_7)\), applying both transitions and suppressing duplicate tuples, is exhaustive by induction on word length.

The attached `checker.py` implements exactly these set updates with bitsets. The attached `automaton_certificate.json` contains the entire reached transition table and shortest access word for every enumerated state. Regeneration gives **\(230\)** distinct reachable states, **\(229\)** of them accepting. Thus this table is a complete reachable DFA for the language, providing an upper bound of \(230\).

To determine its minimal quotient, start by partitioning these states into accepting and rejecting states. At each refinement round, split according to the triple consisting of the current block and the current blocks reached on \(-\) and on \(+\). The successive nontrivial partition sizes, beginning at the acceptance partition, are

\[
2,4,7,9,11,13,15,17,24,34,38,42,46,50,58,68,74,78,80,82,84,86,88,94,102.
\]

The next round makes no split. Inductively, the blocks at refinement depth \(r\) identify states accepting precisely the same continuations of length at most \(r\): the induction step follows by prefixing either sign. Thus distinct final blocks are separated by some finite continuation, and equal final blocks are indistinguishable by *all* continuations because the partition is stable. By the Myhill–Nerode theorem, precisely \(102\) states are necessary and sufficient. The certificate and the executable checker reproduce every finite step of this sink-collapsed construction; their algorithm is exhaustive, not statistical evidence.

## Verification
Place `checker.py` and `automaton_certificate.json` in the same directory and run:

```sh
python3 checker.py automaton_certificate.json
```

The checker regenerates all \(128\) orientations directly, performs the complete subset-product breadth-first search, and compares the resulting transition table, accepting-state counts, shortest access words, complete Moore refinement, and quotient labels byte-independently against the decoded certificate. An additional graph-edge implementation independently verifies membership for every binary sign word of length at most \(10\). The auxiliary cycle-size computations for \(3\) and \(5\) vertices give \(6\) and \(18\) states, respectively. These smaller values are context, not separate novelty claims. The finite enumeration and stable-partition argument together constitute a complete finite proof of the seven-cycle theorem.

## Relationship to prior work
Pujol's *Graph-based automata* (first public September 8, 2026), Section 5.2, defines remanent languages, connects their directed-path membership to chromatic number, and illustrates the five-cycle's remanent graph (Figure 11). It does not give a minimal complete DFA for \(R(C_7)\) or the exact \(102\)-state count. Guzmán-Pro and Hernández-Cruz (2020) establish oriented-path/odd-cycle homomorphism dualities, including the \(Q_n\) path family. Their structural results help explain the existence of cycle-sensitive path witnesses but do not imply this exact minimal-DFA count without the distinct deterministic-state calculation performed here. General NFA determinization and Moore/Myhill–Nerode minimization are standard tools; the new content is their verified exact outcome on this newly introduced seven-cycle language.

## Limitations
This proof establishes only the exact number of minimal complete DFA states for the seven-cycle's remanent language. It does not supply a closed formula or asymptotic growth for other odd cycles, a minimal graph-based NFA, or a classification of all orientations up to graph isomorphism. The exact computation is independently reproducible from the included certificate and checker but has not undergone independent external audit. Priority may be affected by an unindexed explicit table or an implicit earlier derivation.

## References
1. Cyril Pujol, *Graph-based automata*, arXiv:2609.08843v1, first posted September 8, 2026, https://arxiv.org/html/2609.08843 (especially Section 5.2, Proposition 33 and Figure 11).
2. Santiago Guzmán-Pro and César Hernández-Cruz, *Duality pairs and homomorphisms to oriented and unoriented cycles*, arXiv:2003.05605, first posted March 12, 2020, https://arxiv.org/abs/2003.05605 (Section 3).
3. J. Myhill, *Finite automata and the representation of events*, 1957; A. Nerode, *Linear automaton transformations*, 1958 (classical state-minimization theorem).
