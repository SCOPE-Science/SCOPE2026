# Unique optimal pair-merging words and an explicit pair-distance labeling for the Černý automata

## Finding
For every integer \(n\ge 2\), let \(C_n\) be the two-letter deterministic automaton on \(Q=\{0,1,\ldots,n-1\}\) with \(a(i)=i+1\pmod n\) and \(b(n-1)=0\), while \(b(i)=i\) for \(i<n-1\). For a two-element subset \(P\subseteq Q\), let \(\tau(P)\) be the shortest length of an input word whose action identifies the two states in \(P\). Set \(N=\binom n2\), \(h=\lfloor n/2\rfloor\).

The already known fact that a pair requires \(N\) steps, together with the general upper bound of \(N\) on pair distances, implies the *unlabeled* spectrum \(\{1,2,\ldots,N\}\), each value once. The additional result here is an **explicit exact label for each pair and a unique optimal word for each pair**. Write a pair at its smaller circular separation \(k\). If \(2k<n\), there is a unique representation \(P=\{i,(i+k)\bmod n\}\) with \(0\le i<n\), and
\[
\tau(P)=kn-i.
\]
If \(2k=n\), necessarily \(n\) is even; use the unique representation \(P=\{i,i+k\}\) with \(0\le i<k\), and
\[
\tau(P)=(k-1)n+k-i.
\]
Furthermore, **each pair has exactly one shortest merging word**. All these words are suffixes of one master word \(U_n\), given by
\[
U_{2h+1}=(a^{2h}b)^h,\qquad
U_{2h}=a^{h-1}b(a^{2h-1}b)^{h-1}.
\]
The unique shortest word for \(P\) is precisely the suffix of \(U_n\) containing \(\tau(P)\) letters. Thus the reverse shortest-path tree on pair states is a single path visiting every pair exactly once.

## Assumptions and scope
Words act left to right, and an input letter is one unit of cost. A pair is unordered. The circular distance is the minimum number of clockwise or anticlockwise \(a\)-steps between its members. No restrictions on input words beyond using the two letters \(a,b\) are imposed. Every statement above concerns the standard automata \(C_n\) for *all* \(n\ge2\), not arbitrary synchronizing automata.

The use of the word "spectrum" means the multiset of optimal lengths over the \(\binom n2\) distinct unordered input pairs, not the length of a word resetting *all* states. The known all-state reset threshold \((n-1)^2\) is a different invariant.

## Proof
Put \(\rho(P)\) equal to the claimed explicit formula, and \(\rho(\{j\})=0\) for singleton images. We verify three properties:

1. The map \(\rho\) is a bijection from the unordered pairs onto \(\{1,\ldots,N\}\).
2. Under either input letter \(x\in\{a,b\}\), \(\rho(Px)\ge\rho(P)-1\).
3. For each pair there is **exactly one** input letter \(x\) for which \(\rho(Px)=\rho(P)-1\).

For \(2k<n\), the cyclic arcs of clockwise length \(k\) yield \(n\) different unordered pairs, indexed by \(i=n-1,n-2,\ldots,0\), with \(\rho=(k-1)n+1,(k-1)n+2,\ldots,kn\). When \(n=2h\) is even, the diametrical arcs at \(k=h\) give \(h\) pairs, indexed by \(i=h-1,\ldots,0\), with ranks \((h-1)n+1,\ldots,(h-1)n+h=N\). When \(n=2h+1\), the \(h\) ordinary layers each contain \(n\) pairs and \(hn=N\). This proves (1).

For (2) and (3), call the smallest-rank pair of each circular-distance layer its **layer head**. At an ordinary layer head, the representation starts at \(i=n-1\). At an even diametrical layer head, it starts at \(i=h-1\). Applying \(a\) increases the start index by one and therefore **decreases the rank by one** at every non-head pair. At a layer head, \(a\) wraps to a larger rank in the same layer (or fixes the sole pair when \(n=2\)); it cannot decrease the rank by one.

The letter \(b\) fixes any pair not containing \(n-1\). For a pair \(P=\{r,n-1\}\), \(0\le r\le n-2\), \(b\) replaces \(n-1\) by \(0\); when \(r=0\), the image is a singleton. Direct substitution in the formulas gives:

- If \(n=2h\), for \(0\le r\le h-1\) the rank falls by exactly one (the first case includes the singleton), while for \(h\le r\le 2h-2\) it rises by \(n\).
- If \(n=2h+1\), for \(0\le r\le h-1\) the rank falls by exactly one, for \(r=h\) it rises by \(h\), and for \(h+1\le r\le 2h-1\) it rises by \(n\).

The rank-decreasing \(b\)-cases are precisely the layer heads: \(\{n-1,k-1\}\) at ordinary gap \(k\) and \(\{n-1,h-1\}\) for the even diametrical gap. All other pairs are non-heads, so only \(a\) decreases their rank. This proves (2) and (3), including the boundary \(n=2\).

Every input word reducing a pair to a singleton must decrease \(\rho\) from \(\rho(P)\) to zero. Since each letter decreases it by at most one, its length is at least \(\rho(P)\). Repeatedly taking the unique rank-decreasing letter reaches the unique pair at each successive rank and ultimately a singleton in exactly \(\rho(P)\) steps; no other word of that length is possible. Hence \(\tau(P)=\rho(P)\), and the shortest word is unique.

Starting from the unique pair of rank \(N\), the successive optimal letters run backwards through the layers. In each complete layer of length \(n\), they form \(a^{n-1}b\). For even \(n=2h\), the top diametrical layer has \(h\) ranks and contributes \(a^{h-1}b\). These are exactly the displayed master words. Starting from the unique pair of any rank \(t\), its forced path follows the last \(t\) letters of the same master word. This proves the suffix statement and the theorem.

## Verification
The included stand-alone Python 3 program `verify.py` builds every unordered pair transition directly, independently obtains the shortest merging distance by a reverse breadth-first search from singleton images, and counts all shortest paths. It compares every computed distance with the displayed formula, checks that every shortest-path count equals one, checks transition rank inequalities, and verifies the master word for \(2\le n\le80\). Run:

```bash
python3 verify.py
```

Expected terminal line: `VERIFY_OK: all pair states, independent reverse BFS and path counts, n=2..80`.

The finite computation tests the theorem but is **not** the proof of the claims for unbounded \(n\); the preceding rank argument is the infinite-family proof.

## Relationship to prior work
Behague and Johnson [1] define the rendezvous weight of a subset and show that the Černý family realizes the universal upper bound \(\binom n2\) for the *maximum* two-state rendezvous time; their named witness supplies one hardest pair. Since a shortest path of this maximal length necessarily visits all \(\binom n2\) different pair vertices before merging, **the abstract spectrum of distinct values is already a corollary of that known maximum** and is not claimed as new. The new, strictly stronger information is the explicit pair-to-distance formula, the unique shortest word at every pair, and the common master-suffix ordering. Their work also discusses larger subsets, which are not classified here.

Eppstein [2] establishes a general pair-automaton breadth-first-search construction of shortest merging sequences, whereas the result above supplies closed formulas and an explicit unique path for this specific automaton family. Gonze and Jungers [3] investigate the triple rendezvous and synchronizing probability function, not the complete two-state spectrum. No claim is made that the basic Černý automaton, the pair-automaton method, or the known extremal maximum is new.

## Limitations
The theorem is specific to the labeled Černý family and its two specified transitions. The uniqueness conclusion is for minimum-length **pair-merging words** and does not imply uniqueness of all-state reset words. The known maximum already entails the bare multiplicity-one spectrum, so that spectrum by itself is not a novel contribution. The literature comparison does not rule out every unindexed equivalent formulation; in particular, a historical explicit pair-distance table or inverse-pair-path analysis might recover some or all formulas.

## References
[1] N. C. Behague and R. Johnson, "Synchronizing Times for \(k\)-sets in Automata," *Electronic Journal of Combinatorics* 29(3), P3.41 (2022), arXiv:2008.12166 (first posted 2020-08-27), DOI:10.37236/9819.

[2] D. Eppstein, "Reset Sequences for Monotonic Automata," *SIAM Journal on Computing* 19(3), 500–510 (1990), DOI:10.1137/0219033; author-hosted manuscript at https://www.ics.uci.edu/~eppstein/pubs/Epp-SJC-90.pdf.

[3] F. Gonze and R. M. Jungers, "On the Synchronizing Probability Function and the Triple Rendezvous Time for Synchronizing Automata," *SIAM Journal on Discrete Mathematics* 30(2), 995–1014 (2016), arXiv:1410.4034, DOI:10.1137/15M1024603.
