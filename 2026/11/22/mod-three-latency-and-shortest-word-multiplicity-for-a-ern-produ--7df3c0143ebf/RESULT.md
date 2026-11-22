# Mod-three latency and shortest-word multiplicity for a Černý product with three states

## Finding
For every integer \(n\ge3\), let \(C_n\) and \(C_3\) be the explicitly specified Černý automata below. The minimum length \(L_n\) of a single word resetting both, and the number \(N_n\) of distinct common reset words at that minimum length, satisfy
\[
L_n=(n-1)^2+\mathbf1_{3\nmid n},\qquad
N_n=\begin{cases}
1,& n\equiv0\pmod3,\\
\frac{2(n-1)(n-3)}3,&n\equiv1\pmod3,\\
\frac{(n-2)(n-3)}3,&n\equiv2\pmod3.
\end{cases}
\]
These formulas hold for **all** integers \(n\ge3\). In particular, the extra common-control delay is never more than one letter. The exact optimal-word classification in the nondivisible cases is given below; it yields an unbounded quadratic number of shortest words, contrasting with the unique optimum in the divisible case.

## Assumptions and scope
For any integer \(k\ge2\), let \(C_k\) have states \(Q_k=\{0,1,\ldots,k-1\}\) and a common ordered input alphabet \(\{a,b\}\). Define transitions by \(a(i)=i+1\pmod k\) and \(b(0)=1\), with \(b(i)=i\) for \(i\ne0\). The action of words is read left to right; \(w\) resets \(C_k\) if \(Q_kw\) has cardinality one. A word resets the direct product precisely when it resets each factor. Targets need not coincide. \(N_n\) counts distinct **literal** shortest words, not equivalence classes under rotations of letters or states. The case \(n=3\) is included: it is the product of two identical three-state machines. Our \(b\)-action is conjugate by cyclic state relabeling to the classical convention \(b(k-1)=0\), leaving the reset-word language identical.

Write
\[
W_n=b(a^{n-1}b)^{n-2},\qquad
V_{n,j,t}=b(a^{n-1}b)^{j-1}a^tba^{n-1-t}b(a^{n-1}b)^{n-2-j}.
\]
For \(n\equiv0\pmod3\), the only shortest common word is \(W_n\). For \(n\equiv1\pmod3\), all shortest common words are the \(V_{n,j,t}\) with \(1\le j\le n-2\), \(0\le t\le n-2\), \(t\ne j\) and \(t\not\equiv0\pmod3\). For \(n\equiv2\pmod3\), they are the same family restricted to \(t\equiv2\pmod3\).

## Proof
**1. The single-machine threshold and rigidity.** The standard inverse-preimage argument gives that \(W_n\) is the *unique* shortest reset word for \(C_n\), of length \((n-1)^2\). Here is a reconstruction in our normalization. For subsets of \(Q_n\), inverse \(a\) rotates by one step backward; inverse \(b\) adds \(0\) only if the set contains \(1\) but not \(0\), is the identity if it contains both or neither, and removes \(0\) otherwise. Starting from a singleton target and applying a word's inverse letters in reverse order must end at \(Q_n\). Omitting any inverse \(b\) which does not increase the maintained preimage cannot hurt final coverage, by monotonicity of inverse-image operations. After its first successful expansion the maintained set is the circular interval \(\{0,1\}\); after the next successful expansion it is \(\{0,1,2\}\), and so on. Between consecutive expansions, the unique orientation permitting growth is the interval starting at \(1\), requiring at least \(n-1\) inverse rotations. Thus at least \(n-1\) productive \(b\)'s and \((n-2)(n-1)\) copies of \(a\) are necessary. Equality forces the reverse preimage sequence, and hence the word, to be exactly \(W_n\). Conversely, direct action gives \(Q_n W_n=\{1\}\).

**2. The one-letter boundary for \(C_n\).** The established one-letter-slack classification [3] says that the complete set of resetting words of length \((n-1)^2+1\) is \(\{aW_n,W_na,W_nb\}\) together with the \(V_{n,j,t}\) indexed by \(1\le j\le n-2\), \(0\le t\le n-2\), \(t\ne j\). It also states these words are pairwise distinct. The classification can be checked from the same reverse-preimage argument: the extra letter is either an \(a\) at a boundary, or one unproductive \(b\) inserted in an \(a^{n-1}\) run of the unique shortest path. At the \(j\)-th run the allowable split offsets are precisely \(0\le t\le n-2\) except \(t=j\), where the reverse \(b\) would shrink its interval instead of fixing it. The two extensions \(W_na,W_nb\) reset before their final letter, and \(aW_n\) is the remaining extra-\(a\) word. The cited all-length classification supplies the exact boundary list; the computation below independently checks it at all lengths for which it is used in finite testing.

**3. The three-state modular filter.** After the first \(b\), the full three-state set becomes \(\{1,2\}\). If \(n\equiv0\pmod3\), then \(a^{n-1}\) acts as \(a^2\) on \(C_3\); the next \(b\) collapses \(\{0,1\}\), so \(W_n\) also resets \(C_3\). Its uniqueness for \(C_n\) therefore gives \(L_n=(n-1)^2\) and \(N_n=1\).

If \(n\equiv1\pmod3\), each full block \(a^{n-1}b\) acts as \(b\) on \(C_3\). If \(n\equiv2\pmod3\), its \(a\)-part acts as one rotation, which sends \(\{1,2\}\) to \(\{0,2\}\), and the subsequent \(b\) restores \(\{1,2\}\). Thus in both cases \(W_n\) leaves the non-singleton set \(\{1,2\}\), and a common reset word must be longer. Neither \(aW_n\), \(W_na\) nor \(W_nb\) resets \(C_3\) in these cases.

For the inserted words \(V_{n,j,t}\), the source image on \(C_3\) before the split is always \(\{1,2\}\). When \(n\equiv1\pmod3\), the two split rotation exponents sum to \(0\pmod3\). Starting from \(\{1,2\}\), the pair of \(b\)'s with an interior split resets exactly when \(t\equiv1\) or \(2\pmod3\); \(t\equiv0\) leaves \(\{1,2\}\). When \(n\equiv2\pmod3\), the two exponents sum to \(1\pmod3\); a reset occurs exactly when \(t\equiv2\pmod3\). These statements follow by applying \(a\) as the three-cycle and \(b(0)=1\) to the three possible subsets; after becoming a singleton, no later letter can increase the image size. This proves the classification displayed above and that at least one eligible split exists for every \(n\ge4\) not divisible by three (for instance \(j=n-2,t=n-3\)). The explicit common reset word \(b(a^{n-1}b)^{n-3}a^{n-3}ba^2b\) has length \((n-1)^2+1\), confirming sharpness independently of counting.

**4. Count the allowed split pairs.** If \(n=3k+1\), \(k\ge1\), the \(j\)-range has \(3k-1\) values. The \(t\)-range has \(2k\) values not congruent to zero modulo three, and exactly \(2k\) pairs have \(t=j\) among those. Hence \(N_n=(3k-1)2k-2k=2k(3k-2)=2(n-1)(n-3)/3\). If \(n=3k+2\), the \(j\)-range has \(3k\) values, the \(t\)-range has \(k\) values congruent to two, and exactly \(k\) forbidden diagonal pairs. Hence \(N_n=3k^2-k=(n-2)(n-3)/3\). The case \(3\mid n\) was counted in step 3. Every possible shortest common word has been included, establishing both formulas. \(\square\)

## Verification
From the directory containing `verify.py`, run `python3 verify.py`. The program independently builds the complete subset-pair automaton for \(C_n\times C_3\) and performs breadth-first search with shortest-path counting for every \(3\le n\le16\). A state is an ordered pair of nonempty subset masks, and the two outgoing transitions implement the defining letters. Every input word has one path, and breadth-first shortest-path counts therefore count all literal optimal input words, not only selected witnesses. For \(n\le13\), the script also replays every member of the stated one-letter-slack family when \(3\nmid n\). It separately replays \(W_n\) and the constructed one-letter-longer witness for \(3\le n\le200\). The recorded run in `verify_output.txt` ends with `CHECK_OK`. This finite computation checks implementation and edge cases; the proof above supplies the unbounded quantifiers.

## Relationship to prior work
The 6 November 2026 Fernau–Rystsov paper [1] treats reset thresholds of several automaton products, proving general bounds and motivating exact special-family analysis. Its accessible introduction and product definitions do not give this modular formula. A prior complete table for the standard Černý pairs \(2\le m<n\le11\) [2] includes the \(m=3\) values up to \(n=11\), and explicitly leaves all-size formulas outside the special divisibility cases open; those finite values are fully acknowledged, not reused as new results. The known all-length one-letter-slack classification for a *single* Černý automaton [3] supplies the essential input family in proof step 2, but does not impose synchronization of the second machine, determine the arithmetic condition on its resets, or count the resulting intersection. The new contribution is the all-length two-machine modular classification and exact multiplicity law. An unindexed equivalent or a specialization elsewhere remains a priority risk.

## Limitations
Only a **shared-input direct product of the particular machines** \(C_n\) and \(C_3\) is considered. This is not a formula for arbitrary synchronizing automata, for all pairs \(C_n\times C_m\), or for the product in which both coordinates choose independent letters. The proof uses an already published one-letter-slack classification; it does not claim that classification as new. No independent audit of the new product theorem has been performed. The complete later sections of [1] could not be reopened during bibliographic comparison; that access limitation leaves residual priority risk, although inspected statements concern general bounds rather than the exact modular count.

## References
1. H. Fernau and I. Rystsov, *Shortest Synchronizing Words on Product Automata*, arXiv:2611.09136v1, first public 6 November 2026. https://arxiv.org/abs/2611.09136
2. *Exact simultaneous reset thresholds for pairs of Černý automata through eleven states*, published research record, 13 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-exact-simultaneous-reset-thresholds-for-pairs-of-ern-automata-th--46765b03d598
3. *One-letter slack rigidity in the Černý reset language*, published research record, 2 November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-one-letter-slack-rigidity-in-the-ern-reset-language--61d8f6568fe8
