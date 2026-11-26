# Uniform weighted-reset optimality in the Černý automata

## Finding
For every integer \(n\ge 2\), define the deterministic automaton \(C_n\) on \(Q=\{0,1,\ldots,n-1\}\) with letters
\[
a:i\longmapsto i+1\pmod n,\qquad b:n-1\longmapsto0,\quad b:i\longmapsto i\ (0\le i\le n-2).
\]
For any word \(w\), let \(\#_a(w)\) and \(\#_b(w)\) be its letter counts. Every reset word satisfies the **simultaneous coordinatewise lower bounds**
\[
\#_a(w)\ge(n-1)(n-2),\qquad \#_b(w)\ge n-1.
\]
Equality in both bounds occurs for exactly the word
\[
w_n=b(a^{n-1}b)^{n-2}.
\]
In particular, for every real pair \(\alpha,\beta>0\), the unique least-cost reset word, when the costs of \(a\) and \(b\) are respectively \(\alpha\) and \(\beta\), is \(w_n\), with optimal cost
\[
\boxed{\alpha(n-1)(n-2)+\beta(n-1)}.
\]
The optimal word is independent of the positive cost ratio. The assertion includes \(n=2\), for which the optimum is the single letter \(b\).

## Assumptions and scope
The automaton is complete and deterministic, acts on the right, and words are read from left to right. A reset word maps all of \(Q\) to the same state; the terminal state is not prescribed. Costs are **positive and additive by letter**, not state-transition-dependent or allowed to be zero. There is no upper bound imposed on the length of competitor words.

## Proof
Fix a reset word \(w\) with final state \(r\). Process its letters **backward**, starting with the singleton inverse-image set \(T=\{r\}\). Each backward \(a\) step replaces \(T\) by \(a^{-1}(T)\), and each backward \(b\) step replaces it by \(b^{-1}(T)\). After the whole word the inverse image is \(Q\).

Let \(t\) be the number of backward \(a\) steps already processed, and express the current inverse-image set in the rotating frame \(S=a^t(T)\). Thus \(S\) is initially \(\{r\}\). A backward \(a\) step increases \(t\) by one and leaves \(S\) unchanged. A backward \(b\) step at rotation time \(t\) acts exactly as
\[
S\longmapsto(S\setminus\{t-1\bmod n\})\cup
\begin{cases}
\{t-1\bmod n\},&t\bmod n\in S,\\
\varnothing,&t\bmod n\notin S.
\end{cases}
\]
Indeed, \(b^{-1}(T)=(T\setminus\{n-1\})\cup(\{n-1\}\text{ if }0\in T)\), and conjugating by \(a^t\) gives the display. Thus each inverse \(b\) can introduce **at most one** new position, and it can introduce the position \(x\) only when the cyclic successor \(x+1\pmod n\) is already present and \(t\equiv x+1\pmod n\).

For \(j=1,\ldots,n-1\), write \(x_j=r-j\pmod n\). Let \(t_j\) be the rotation count at the first introduction of \(x_j\). Such an introduction must occur because the final inverse-image set is all of \(Q\), and the predecessor-gate condition implies the first introductions occur in the order \(x_1,x_2,\ldots,x_{n-1}\). At the first introduction of \(x_1\), the only possible trigger is \(r\), so \(t_1\equiv r\pmod n\) and \(t_1\ge0\). For each \(j\ge2\), the introduction time satisfies \(t_j\equiv r-(j-1)\pmod n\). Because \(t_j\ge t_{j-1}\), and because the second residue is one **less** modulo \(n\),
\[
t_j-t_{j-1}\ge n-1\quad(2\le j\le n-1).
\]
Consequently the total number \(A\) of backward \(a\) steps, which equals \(\#_a(w)\), obeys
\[
A\ge t_{n-1}\ge t_1+(n-2)(n-1)\ge(n-2)(n-1).
\]
Starting with one element and ending with \(n\) elements, while each inverse \(b\) introduces at most one, separately forces \(\#_b(w)\ge n-1\).

To attain both bounds, one must have \(t_1=0\), hence \(r=0\), and \(t_j=(j-1)(n-1)\) for every \(j\). Exactly \(n-1\) backward \(b\) steps are available, so each introduces its required new predecessor; no deletion or redundant occurrence is possible. There can be no extra backward \(a\) steps either. The **only** possible backward sequence is therefore \(b,(a^{-1})^{n-1},b,\ldots,(a^{-1})^{n-1},b\), with \(n-1\) occurrences of \(b\). In forward order this is precisely \(b(a^{n-1}b)^{n-2}\). Conversely the inverse sequence really adds the positions \(-1,-2,\ldots,-(n-1)\pmod n\) successively, so the displayed word resets \(Q\) to \(0\).

Finally, a positive linear combination of the two coordinatewise lower bounds gives the stated weighted minimum; positivity ensures that equality of weighted costs requires equality in both counts, hence uniqueness.

## Verification
The independent `verify.py` enumerates subsets of the full-state power automaton. A zero-one shortest-path search computes the least possible number of rotation letters among all reset words, without any length bound. For \(n=2,\ldots,13\), it agrees with \((n-1)(n-2)\). For each of those twelve sizes and each of the five positive integer cost pairs \((1,1),(1,9),(9,1),(3,5),(17,2)\), an independent positive-weight Dijkstra search finds the stated optimum and counts exactly one optimal word. It also applies the explicit word to every state. Output: `VERIFY_OK: 12 state sizes, 60 positive-cost searches, unique weighted optimum in each`. These finite checks do not prove the infinite theorem; the inverse-preimage argument does.

To reproduce, run `python3 verify.py` with Python 3.9 or later. No external dependencies are used.

## Relationship to prior work
Ruszil [1] treats additive letter costs in weighted synchronizing automata and gives approximation algorithms; the paper also exhibits an automaton where minimum-length and minimum-cost words differ. Fominykh, Martyugin and Volkov [2] address weighted synchronization with general transition costs and algorithmic hardness. The familiar Černý bound concerns minimum **total** reset length, whereas the present claim separately bounds the number of each letter in **every**, possibly much longer, reset word. Known exact early-rank/avoidance thresholds and pair-merging distances do not supply the global positive-weight optimality statement. The all-cost rigidity rests on the predecessor-gate lemma proved above.

## Limitations
The claim is confined to this precisely labeled Černý family, to two letter-additive strictly positive real costs, and to exact reset synchronization. It does not cover weighted transitions, zero/negative letter costs, other cyclic one-defect automata, or arbitrary ranks. Independent expert verification has not been undertaken. An equivalent result expressed in alternate terminology in the wider literature remains possible.

## References
[1] J. Ruszil, *Approximation algorithm for finding short synchronizing words in weighted automata*, arXiv:2103.16185, first public version 2021-03-30. https://arxiv.org/abs/2103.16185

[2] I. Fominykh, P. Martyugin, M. Volkov, *P(l)aying for Synchronization*, arXiv:1205.2174, 2012. https://arxiv.org/abs/1205.2174

[3] P. Martyugin, *Complexity of Problems Concerning Reset Words for Some Partial Cases of Automata*, Acta Cybernetica 19 (2009), 517–536. https://acta.bibl.u-szeged.hu/12877/

[4] M. Ferens and M. Szykuła, *Completely reachable automata: a quadratic decision algorithm and a quadratic upper bound on reaching threshold*, arXiv:2208.05956. https://arxiv.org/abs/2208.05956
