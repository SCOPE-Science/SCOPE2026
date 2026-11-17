# Rigidity of shortest reset words in cyclic one-point automata

## Finding

**Theorem (unique optimal reset word).** Fix integers \(n\ge 2\) and \(1\le r<n\). On the state set \(Q=\mathbb Z/n\mathbb Z\), consider the complete deterministic automaton with alphabet \(\{a,b\}\), where \(a\) sends \(i\) to \(i+1\pmod n\), and \(b\) sends \(0\) to \(r\) and fixes every other state. If \(\gcd(n,r)>1\), no reset word exists. If \(\gcd(n,r)=1\), the **complete set of shortest reset words**, with their labels fixed, is the singleton

\[
\boxed{\mathcal R_{\min}(n,r)=\{(ba^{n-r})^{n-2}b\}.}
\]

The unique word sends every state to \(r\). Its length is

\[
L(n,r)=(n-1)+(n-2)(n-r).
\]

**Novelty boundary.** The coprimality criterion, this optimal length, and an explicit shortest word in equivalent labeling are already present in Martyugin (2009, Proposition 6.2, page 532). The finding here is **uniqueness of the shortest word for every coprime pair**, not rediscovery of the known threshold or construction. The earlier assertion that one displayed word is shortest does not in itself exclude other shortest words.

## Assumptions and scope

Words are finite strings read left to right, each acting on the current state; distinct label strings are counted separately. The empty word is not a reset word for \(n\ge2\). The reset threshold is the minimum number of letters in a word mapping all \(n\) starting states to one state. The statement concerns precisely the two given letter actions (not a larger alphabet or arbitrary relabelings), all positive pairs \((n,r)\) with \(n\ge2\) and \(1\le r<n\), including the smallest case \(n=2\). A \(b\)-step is called **effective** along a particular trajectory only when that trajectory is at state \(0\) immediately before the step, so the step jumps to \(r\).

## Proof

**1. Arithmetic obstruction.** Let \(w\) contain \(A\) letters \(a\). For any initial state \(i\), let \(h_i\ge0\) be the number of effective \(b\)-steps along the trajectory starting at \(i\). Its final state is

\[
\delta(i,w)\equiv i+A+r h_i\pmod n.
\]

If \(g=\gcd(n,r)>1\), the residue of the final state modulo \(g\) is \(i+A\), so trajectories with different initial residues modulo \(g\) can never meet. Consequently the automaton cannot synchronize.

**2. Sharp lower bound in the coprime case.** Suppose \(\gcd(n,r)=1\) and \(w\) synchronizes. For distinct initial states \(i,j\), equality of final states gives

\[
r(h_i-h_j)\equiv j-i\pmod n.
\]

Invertibility of \(r\) modulo \(n\) forces the \(n\) integers \(h_i\) to have **pairwise distinct residues modulo \(n\)**. Thus some trajectory has at least \(n-1\) effective \(b\)-steps. Write \(B\) for the total number of occurrences of \(b\) in \(w\); then \(B\ge n-1\). Immediately after any effective \(b\)-step the chosen trajectory is at \(r\). Before its next effective \(b\)-step it must return to \(0\), and the only intervening state-changing steps on this trajectory are applications of \(a\). Hence each of the at least \(n-2\) intervals between consecutive effective \(b\)-steps contains at least \(n-r\) occurrences of \(a\). Therefore

\[
A\ge(n-2)(n-r),\qquad |w|=A+B\ge(n-2)(n-r)+(n-1)=L(n,r).
\]

The argument does not assume that every \(b\) in a general word acts effectively, and it applies to arbitrary reset words, not only words of the displayed alternating form.

**3. A word attaining the bound.** Put \(u=(ba^{n-r})^{n-2}b\). For \(1\le j\le n-1\), after the \(j\)-th occurrence of \(b\) the set of states absent from the image of \(Q\) is exactly

\[
H_j=\{0,-r,-2r,\ldots,-(j-1)r\}\pmod n.
\]

For \(j=1\), applying \(b\) excludes exactly \(0\). Inductively, before the next \(b\), the intervening \(a^{n-r}\) rotates the current image by \(-r\), and therefore rotates the missing set to \(\{-r,-2r,\ldots,-jr\}\). Since \(\gcd(n,r)=1\) and \(j\le n-2\), neither \(0\) nor \(r\) belongs to this missing set. Thus the next \(b\) replaces the present state \(0\) by the already-present state \(r\), excluding one more state; the new missing set is \(H_{j+1}\). At \(j=n-1\), precisely \(n-1\) distinct states are absent and the unique remaining image state is \(r\). Hence \(u\) synchronizes, with \(|u|=L(n,r)\).

**4. Equality forces a unique label string.** Suppose \(|w|=L(n,r)\). Equality in both bounds from step 2 gives \(B=n-1\), \(A=(n-2)(n-r)\). The chosen trajectory must have exactly \(n-1\) effective \(b\)-steps, so **every** occurrence of \(b\) in \(w\) acts effectively on it. There can be no \(a\) before the first \(b\), none after the last \(b\), and precisely \(n-r\) applications of \(a\) between each pair of successive \(b\)'s: the \(n-2\) return intervals already consume the entire \(a\)-budget. Thus \(w=(ba^{n-r})^{n-2}b=u\). For \(n=2\) this gives the lone letter \(b\), as required. This proves the unique-optimum assertion.

## Verification

The standalone standard-library program `verify.py` independently builds the subset automaton and performs breadth-first search with exact shortest-path counts. For every \(2\le n\le12\) and \(1\le r<n\), it checks the coprimality criterion, the previously known length, and **exactly one** shortest reset word in the coprime case. It also directly replays the symbolic witness and its target state for all coprime pairs with \(2\le n\le50\). Run `python3 verify.py`. These are finite corroborating tests, not a substitute for the argument for all \(n\).

## Relationship to prior work

P. Martyugin, *Complexity of Problems Concerning Reset Words for Some Partial Cases of Automata*, Acta Cybernetica 19 (2009), Proposition 6.2 and Figure 5, proves the synchronizability criterion and optimal length for this exact cyclic/simple-idempotent family and supplies an optimal word (with the cycle direction and label names exchanged). **These facts are acknowledged as known**. No assertion of uniqueness of the optimal word appears in the inspected proposition or surrounding proof. The present result isolates, states and proves the strictly stronger *one-element optimizer set*; its numerical length is cited as prior work, not claimed new.

H. Don (2016), Proposition 15, treats circular automata with a rank-deficient letter and proves synchronization and the general bound \((n-1)^2\) in the coprime-displacement case, but does not enumerate optimal words. Rystsov and Szykuła (2023) treat structural synchronizing criteria for automata with permutation and unitary letters; their later paper treats bounds on reset thresholds of transformation monoids, not this exact optimal-word count. General shortest-reset-word algorithms can compute this count for any fixed \(n\), but are not a uniform uniqueness theorem for this family. Related database records enumerate optimizers in other slowly synchronizing families; they neither include the present automaton nor logically imply uniqueness for it.

## Limitations

The proof concerns exactly two specified actions and counts label strings, not words modulo rotation, conjugacy or alphabet relabeling. It does not assert an analogous uniqueness result for arbitrary cyclic automata, other rank-deficient letters or larger alphabets. The reset threshold itself and existence of an optimal word are known, so they are not a novelty claim. The checked sources do not exclude an unindexed or differently phrased earlier proof of uniqueness. Independent scientific validation has not been performed.

## References

- P. Martyugin, “Complexity of Problems Concerning Reset Words for Some Partial Cases of Automata,” *Acta Cybernetica* **19** (2009), 517–536, Proposition 6.2, page 532. https://cyber.bibl.u-szeged.hu/index.php/actcybern/article/view/3780/3764
- H. Don, “The Černý Conjecture and 1-Contracting Automata,” *Electronic Journal of Combinatorics* **23** (2016), P3.12, Proposition 15. https://doi.org/10.37236/5616
- I. Rystsov and M. Szykuła, “Primitive Automata that are Synchronizing,” arXiv:2307.01302v1 (first public July 3, 2023), Section 4. https://arxiv.org/html/2307.01302v1
- I. Rystsov and M. Szykuła, “Reset Thresholds of Transformation Monoids,” arXiv:2309.08321v1 (2023), Sections 6–7. https://arxiv.org/pdf/2309.08321
- M. Szykuła and A. Zyzik, “An Improved Algorithm for Finding the Shortest Synchronizing Words,” ESA 2022. https://doi.org/10.4230/LIPIcs.ESA.2022.85
