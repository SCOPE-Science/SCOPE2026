# Exact necklace and primitive-period census for shortest circular subsequence-universal words

## Finding
Fix an integer alphabet size \(q\ge2\) with \(q\) distinct labeled symbols and an integer \(k\ge1\). A word is \(k\)-subsequence universal if every word of length \(k\) over its alphabet occurs as a scattered subsequence. A word is *circularly* \(k\)-universal if at least one of its cyclic rotations is \(k\)-subsequence universal. Its shortest possible length is \(qk\).

Let \(P_q(k)\) be the number of marked-start, length-\(qk\) circularly \(k\)-universal words, let \(N_q(k)\) count their cyclic-rotation classes, and let \(R_q(k)\) count those classes of least period \(qk\). Then

\[
P_q(k)=q!\sum_{t=1}^{q}\frac{(-1)^{t+1}q}{t}
\sum_{\substack{g_1+\cdots+g_t=q\\g_1,\ldots,g_t\ge1}}
\left(\prod_{i=1}^{t}g_i!\right)^{k-1}.
\]

\[
N_q(k)=\frac1{qk}\sum_{e\mid k}\varphi(k/e)P_q(e),\qquad
R_q(k)=\frac1{qk}\sum_{e\mid k}\mu(k/e)P_q(e),
\]

where \(\varphi\) and \(\mu\) are Euler's totient and the Möbius function. Every least period is a multiple of \(q\); the formulas give the complete spectrum at every length. In particular,

\[
P_2(k)=2^{k+1}-2,\qquad
N_2(k)=\frac1k\sum_{e\mid k}\varphi(k/e)2^e-1,
\]

and for \(k\ge2\), \(R_2(k)=k^{-1}\sum_{e\mid k}\mu(k/e)2^e\), whereas \(R_2(1)=1\). For three symbols,
\[
P_3(k)=6\bigl(3\cdot6^{k-1}-3\cdot2^{k-1}+1\bigr).
\]
For every fixed \(q\ge2\), both \(N_q(k)\) and \(R_q(k)\) are asymptotic to \((q!)^k/k\) as \(k\to\infty\).

## Assumptions and scope
Positions and rotations are indexed modulo \(qk\), and the symbols are labeled. A necklace is an orbit under cyclic rotation alone, **not** reversal or alphabet relabeling. A marked word has a distinguished initial position, not a chosen universal cut. The formulas concern the minimal possible length \(qk\) and do not enumerate longer words. Only positive integers \(q\ge2\) and \(k\ge1\) are asserted.

## Proof
**1. Shortest linear universal words.** Scan a word greedily into consecutive *arches*: each arch ends at the first position where every one of the \(q\) letters has appeared since the last arch. A final remainder lacks at least one letter. If there are \(r\) arches, any length-\(r\) pattern is realized by taking its successive letters from successive arches, so the universality index is at least \(r\). Conversely let \(a_i\) be the letter which completes arch \(i\), and choose a letter \(b\) missing from the remainder. The shortest greedy embedding of \(a_1\cdots a_r b\) would put \(a_i\) at the end of its own arch, because no copy of \(a_i\) occurs earlier in that arch; it cannot then embed \(b\) in the remainder. Thus the index equals \(r\). Each arch has length at least \(q\), with equality precisely when it is a permutation of the alphabet. A word of length \(qk\) is therefore \(k\)-universal if and only if it is a concatenation of \(k\) length-\(q\) permutations. This proves minimality, and every such word has exactly \(k\) copies of each symbol.

**2. Overlaps between circular cut positions.** Let \(A_s\), for \(s\in\{0,\ldots,q-1\}\), consist of all marked words whose circular consecutive blocks of size \(q\), starting at residue phase \(s\), are alphabet permutations. Starting points differing by a multiple of \(q\) produce the same condition. The required marked-word set is exactly \(\bigcup_s A_s\).

For a nonempty subset of \(t\) phases, list them in cyclic order, with positive gaps \(g_1,\ldots,g_t\) summing to \(q\). Fix one phase as block boundary, and call its consecutive permutation blocks \(B_1,\ldots,B_k\), cyclically. An additional phase at offset \(r\) is valid if and only if the first \(r\) letters of every \(B_j\) have the same **set** of symbols: indeed the shifted length-\(q\) block is the suffix of \(B_j\) after \(r\) followed by the first \(r\) letters of \(B_{j+1}\), and is a permutation precisely when the two complementary symbol sets match. Applying this condition at every selected phase says that each of the \(t\) segments of sizes \(g_i\) has a common symbol set across all \(k\) blocks.

There are \(q!/(g_1!\cdots g_t!)\) ordered partitions of the alphabet into those sets and \((g_1!\cdots g_t!)^k\) ways to order the segments independently in the \(k\) blocks. Hence
\[
\left|\bigcap_{s\in T}A_s\right|
=q!\left(\prod_{i=1}^{t}g_i!\right)^{k-1}.
\]
For a fixed \(t\), summing the contributions over all phase subsets \(T\) is equivalent to summing over all positive \(t\)-compositions of \(q\), choosing one of the \(q\) possible rooted cut positions, and dividing by \(t\) possible roots of each subset. Inclusion–exclusion over the nonempty phase subsets yields the displayed formula for \(P_q(k)\).

**3. Cyclic orbits.** Since each member has exactly \(k\) occurrences of each letter, any least period \(d\) must satisfy \(q\mid d\): if it is \(m=qk/d\) repetitions of a primitive block, then \(m\mid k\) by equal letter counts. For a shift through \(j\) of the \(qk\) positions, the fixed strings are repetitions of a block of length \(d=\gcd(j,qk)\). If \(d\) is not a multiple of \(q\) there are none. For \(d=qe\) with \(e\mid k\), repetition maps the circularly \(e\)-universal length-\(qe\) words bijectively to the fixed members of the length-\(qk\) family; this holds because a phase partition into permutations repeats. There are \(\varphi(k/e)\) shifts with that gcd. Burnside's lemma gives \(N_q(k)\). Every necklace of least period \(qe\) contributes exactly \(qe\) distinct marked length-\(qk\) words on repetition, hence \(P_q(k)=\sum_{e\mid k}qeR_q(e)\). Möbius inversion proves the formula for \(R_q(k)\).

**4. Specialization and asymptotics.** At \(q=2\), the one-phase part of inclusion–exclusion is \(2^{k+1}\) and the two-phase intersection has size two, yielding \(P_2(k)=2^{k+1}-2\). Substituting into the orbit formulas yields the binary identities (including the \(k=1\) primitive exception). The analogous three-phase calculation yields the stated ternary expression. For fixed \(q\), the one-phase term is \(q(q!)^k\), while in any intersection with two or more selected phases the product of gap factorials is at most \((q-1)!\). Thus \(P_q(k)=q(q!)^k(1+O_q(q^{-k}))\). Contributions with proper divisor \(e\mid k\) have \(e\le k/2\) and are exponentially smaller than \((q!)^k\), proving both necklace asymptotics.

## Verification
The accompanying standalone Python 3 script `verify.py` implements the inclusion–exclusion and composition formulas independently, computes the totient/Möbius orbit counts, enumerates actual permutation-block words and their cyclic orbits, and directly tests subsequence universality on every binary word of lengths two, four, six, every ternary word of lengths three, six, nine, and every four-letter word of lengths four and eight. Its successful run checked 19 orbit instances, 138088 marked-word memberships and 35 further symbolic-integer formula identities. These finite tests check the implementation and small cases; the proof above establishes all \(q,k\) results.

For example the triples \((P_q(k),N_q(k),R_q(k))\) for \(q=3\) and \(k=1,2,3,4\) are \((6,2,2)\), \((78,14,12)\), \((582,66,64)\), \((3750,320,306)\).

## Relationship to prior work
Barker, Fleischmann, Harwardt, Manea and Nowotka (2020) introduced circular scattered-factor universality and established its basic structure and algorithms. Fleischmann, Germann and Nowotka (2021) investigated circular universality under repetition. Adamson (2023) counted and ranked *linear* universal words; Adamson and coauthors (2023) treated universality within regular languages. Their inspected primary texts establish the context but do not state the all-alphabet, minimum-length, marked-word/necklace/primitive orbit formulas here. The present argument uses a phase-overlap inclusion–exclusion and cyclic-period enumeration, beyond the linear permutation-block count. Distinct problems involving contiguous de Bruijn necklaces and perfect necklaces do not count scattered-subsequence universal rotations. This is a best-knowledge comparison, not a guarantee that no equivalent computation is recorded elsewhere.

## Limitations
The result concerns minimum length only, not general length or uniqueness of witnessing cuts. Computational tests stop at finite sizes and cannot certify the infinite formulas. The mathematical proof has not undergone independent validation. Searches and inspection of selected primary publications do not exclude every unpublished, unindexed or differently formulated equivalent result.

## References
1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, D. Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629v1, first public 2020-03-10. https://arxiv.org/html/2003.04629v1
2. P. Fleischmann, S. B. Germann, D. Nowotka, *Scattered Factor Universality -- The Power of the Remainder*, arXiv:2104.09063v1, first public 2021-04-19. https://arxiv.org/abs/2104.09063
3. D. Adamson, *Ranking and Unranking k-subsequence universal words*, arXiv:2304.04583v1, first public 2023-04-10. https://arxiv.org/html/2304.04583v1
4. D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea, D. Nowotka, *k-Universality of Regular Languages*, arXiv:2311.10658v1, first public 2023-11-17. https://arxiv.org/html/2311.10658v1
