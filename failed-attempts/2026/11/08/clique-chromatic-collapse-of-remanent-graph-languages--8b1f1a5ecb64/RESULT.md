# Clique–chromatic collapse of remanent graph languages

## Finding
Let \(G\) be a finite nonempty simple undirected graph satisfying \(\omega(G)=\chi(G)=k\), with \(k\ge1\). For each orientation \(\vec G\), let \(L(\vec G)\subseteq\{+,-\}^*\) be the set of signed words read along walks in \(\vec G\): a \(+\) traverses an edge in its direction and a \(-\) traverses an edge against its direction. The starting vertex and ending vertex are unrestricted. Define the remanent language by \(R(G)=\bigcap_{\vec G}L(\vec G)\).

Then the **entire remanent language**, including arbitrary mixed-sign words, is
\[
R(G)=\{w\in\{+,-\}^*: w\text{ has neither }+^k\text{ nor }-^k\text{ as a contiguous factor}\}.
\]
Its minimum complete deterministic finite automaton has **exactly** \(2k\) states (including a rejecting sink). For each length \(m\ge0\), the number \(a_k(m)\) of remanent words has ordinary generating function
\[
\sum_{m\ge0}a_k(m)z^m=\frac{1+S_k(z)}{1-S_k(z)},\qquad S_k(z)=\sum_{j=1}^{k-1}z^j.
\]
For \(k=1\), \(S_k=0\), so the language consists only of the empty word.

This includes complete graphs, complete multipartite graphs, all nonempty perfect graphs, and more generally every graph whose clique and chromatic numbers agree. In particular, the language and its state complexity are independent of the graph's number of vertices and edges once the common clique/chromatic number is fixed.

## Assumptions and scope
All graphs here are finite, simple, undirected, and have at least one vertex. An orientation directs every existing edge exactly once; it neither introduces arcs nor loops. A walk may repeat vertices or edges. A signed word of length \(m\) describes \(m\) consecutive transitions; the empty word is realized by the length-zero walk. All states of the oriented-graph automaton are initial and accepting. The assertions hold for every such graph \(G\) with \(\chi(G)=\omega(G)\), and every word length \(m\ge0\); no asymptotic or genericity assumptions are needed.

## Proof
**1. The language of a tournament.** Denote by \(T_k\) a transitive orientation of the complete graph \(K_k\), with vertex set \(\{0,\ldots,k-1\}\) and arc \(i\to j\) whenever \(i<j\). A word containing \(k\) consecutive \(+\) symbols cannot be read in \(T_k\), since it requires \(k\) strict increases among only \(k\) levels. Similarly \(-^k\) is impossible.

Conversely, suppose a signed word \(w\) contains neither forbidden factor. Make a directed path with \(|w|+1\) indexed vertices, orienting its successive edges according to the signs of \(w\). The longest directed path in this oriented path has length equal to the longest contiguous constant-sign run in \(w\): a directed path in an oriented line cannot change its direction of index traversal. Let \(h(v)\) be the maximum length of a directed path ending at vertex \(v\). Then \(0\le h(v)\le k-1\), and every directed edge \(u\to v\) satisfies \(h(u)<h(v)\). Sending \(v\) to \(h(v)\) is therefore an orientation-preserving homomorphism of this signed path into \(T_k\). Hence
\[
L(T_k)=L_k:=\{w: +^k,-^k\text{ are not factors of }w\}.
\]

An arbitrary tournament on \(k\) vertices is either transitive or contains a directed triangle. Indeed a shortest directed cycle in a tournament must have length three: a chord in a longer directed cycle produces a shorter directed cycle. A directed triangle admits **every** signed word as a walk: follow its cyclic arcs for \(+\) and against them for \(-\). Thus every tournament orientation of \(K_k\) contains \(L_k\); for \(k=1,2\), all tournaments are transitive, and the same conclusion holds. In fact \(R(K_k)=L_k\).

**2. Sandwich by a clique and a coloring.** Since \(\omega(G)=k\), fix a clique with \(k\) vertices. Restrict an arbitrary orientation of \(G\) to this clique. By Step 1 it accepts every word of \(L_k\); the larger oriented graph does too. Consequently \(L_k\subseteq R(G)\).

Since \(\chi(G)=k\), fix a proper coloring of \(G\) by colors \(0,\ldots,k-1\), and orient every edge toward the higher color. A \(+\) step strictly increases color, whereas a \(-\) step strictly decreases color. No directed walk in this orientation can read \(+^k\) or \(-^k\). Thus \(R(G)\subseteq L_k\). Combining the two containments proves \(R(G)=L_k\).

**3. Exact state count.** A complete DFA for \(L_k\) has an initial accepting state, \(k-1\) accepting states recording a trailing run of \(+\) of each possible positive length, \(k-1\) analogous accepting states for \(-\), and one rejecting absorbing sink. It therefore has \(2k\) states; this description also works for \(k=1\).

All these states have distinct right languages. The sink is distinguished from the accepting states by the empty suffix. Two trailing positive-run states of lengths \(i<j\) are distinguished by appending \(k-j\) positive symbols, which rejects from the longer run and accepts from the shorter; the same argument works for negative runs. A positive-run state of length \(j\) and any negative-run state are distinguished by appending \(k-j\) positives; this is forbidden from the former, allowed from the latter. A positive-run state of length \(i\) is distinguished from the initial state by appending \(k-i\) positives, and analogously for negative runs. Hence the stated DFA is minimal by Myhill–Nerode.

**4. Exact length generating function.** Each nonempty word in \(L_k\) has a unique factorization into \(r\ge1\) maximal same-sign runs. The first run has two sign choices; all subsequent signs alternate. Each run length belongs to \(\{1,\ldots,k-1\}\). Thus the generating series for nonempty words is \(2\sum_{r\ge1} S_k(z)^r=2S_k(z)/(1-S_k(z))\). Adding the empty word gives \((1+S_k(z))/(1-S_k(z))\).

## Verification
The included standalone `checker.py` performs exact bitset-reachability/product-automaton tests for all \(1{,}099\) labeled tournament orientations on at most five vertices. It checks their inclusion of \(L_k\) and confirms that the number with no directed triangle is \(k!\) at each order. It separately verifies all \(760\) orientations of weakly perfect graphs on at most four labeled vertices and \(400\) reproducibly generated orientations of larger complete multipartite graphs. The command is `python checker.py`; its expected final line begins `CHECKS_OK`. These finite tests independently check many boundary cases but are not substitutes for Steps 1–4, which prove the universal statement.

## Relationship to prior work
Pujol's September 2026 work introduces the remanent language of an undirected graph and proves its usefulness in detecting chromatic number. The result here addresses the stronger **full mixed-direction language** and exact minimal deterministic state count for every graph at clique–chromatic equality, not merely the existence of all-positive walks. The elementary tournament triangle/transitivity dichotomy provides the crucial additional ingredient. The general Gallai–Hasse–Roy–Vitaver relation between colorability and directed path length concerns monochromatic signed runs, not by itself all mixed-sign words or the complete DFA size.

The clique–chromatic equality hypothesis is meaningful: the five-cycle has \(\chi(C_5)=3\) but \(\omega(C_5)=2\). Orient its consecutive edges as \(1\to0\), \(1\to2\), \(3\to2\), \(3\to4\), \(4\to0\) (indices modulo five). In this orientation the word \(++-++\), which belongs to \(L_3\), is not realizable: the sole length-two directed walk is \(3\to4\to0\), and any backward step from its endpoint cannot be followed by two forward steps. Therefore the full-language collapse does not simply follow from the chromatic number for arbitrary graphs.

## Limitations
The theorem is a sufficient condition, not a converse characterization of all graphs having the language \(L_k\). It does not determine the remanent language for graphs with unequal clique and chromatic numbers, nor the minimum graph-based nondeterministic realization of the same language. The primary 2026 paper's complete remanent-language section could not be independently inspected during the literature comparison; an unstated or implicit earlier corollary remains a historical-priority risk. No independent mathematical audit has been performed.

## References
1. Cyril Pujol, *Graph-based automata*, arXiv:2609.08843v1, first publicly posted 2026-09-08. https://arxiv.org/abs/2609.08843
2. Pavol Hell, Huishan Zhou, Xuding Zhu, *On homomorphisms to acyclic local tournaments*, Journal of Graph Theory **20** (1995), 467–471. https://doi.org/10.1002/jgt.3190200410
3. Gallai–Hasse–Roy–Vitaver theorem on graph coloring and directed paths (classical background). https://en.wikipedia.org/wiki/Gallai%E2%80%93Hasse%E2%80%93Roy%E2%80%93Vitaver_theorem
