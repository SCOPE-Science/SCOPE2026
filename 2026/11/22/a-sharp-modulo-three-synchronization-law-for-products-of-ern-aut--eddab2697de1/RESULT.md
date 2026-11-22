# A sharp modulo-three synchronization law for products of Černý automata

## Finding

Let \(C_k\) be the standard \(k\)-state Černý automaton, and let \(\operatorname{rt}\) denote the minimum length of a word resetting all states of a deterministic automaton. For **every integer \(n\ge4\)**, the two-letter direct product of the \(n\)-state and three-state automata satisfies

\[
\boxed{\operatorname{rt}(C_n\times C_3)=(n-1)^2+\begin{cases}0,&3\mid n,\\1,&3\nmid n.\end{cases}}
\]

Thus, the three-state factor costs either no additional input or precisely one letter beyond the optimal reset cost of the \(n\)-state factor. This is an all-length statement, not an extrapolation from small instances.

A shortest simultaneous reset word is

\[
W_n=b(a^{n-1}b)^{n-2}\quad\text{when }3\mid n,
\]

and, when \(3\nmid n\),

\[
V_n=b(a^{n-1}b)^{n-3}a^{n-3}ba^2b.
\]

The second word is obtained by inserting one extra \(b\) into the last \(a\)-block of \(W_n\); its length is exactly \((n-1)^2+1\).

## Assumptions and scope

For each \(k\ge2\), \(C_k\) has state set \(Q_k=\{0,1,\ldots,k-1\}\), common input alphabet \(\{a,b\}\), and transitions

\[
i\cdot a=i+1\pmod k,\qquad i\cdot b=\begin{cases}0,&i=k-1,\\i,&i<k-1.\end{cases}
\]

Words are read from left to right. A word resets \(C_k\) if the image of the whole state set under that word is a singleton. The direct product \(C_n\times C_3\) has state set \(Q_n\times Q_3\), each letter acting simultaneously in both coordinates. Its full-state image after any word is the Cartesian product of the two coordinate images. Thus it is reset exactly when **the same word** resets both factors; the target states may differ. The theorem is asserted for \(n\ge4\), so the two factors have different sizes.

## Proof

**1. The single-factor lower bound and rigidity.** Consider a reset word \(w\) of \(C_n\), write \(A\) and \(B\) for the numbers of \(a\)'s and \(b\)'s in it, and, for each starting state \(i\), let \(h_i\) be the number of occasions on which that trajectory uses a \(b\) **at state \(n-1\)**. Both \(a\) and an effective \(b\) increment the state by one modulo \(n\); an ineffective \(b\) fixes it. Therefore

\[
i\cdot w\equiv i+A+h_i\pmod n.\]

If \(w\) resets all \(n\) initial states, the \(n\) numbers \(h_i\) occupy distinct residues modulo \(n\). In particular, at least one trajectory has at least \(n-1\) effective \(b\)-steps, so \(B\ge n-1\). Between consecutive effective \(b\)-steps on that trajectory the state must travel from \(0\) back to \(n-1\); this requires at least \(n-1\) occurrences of \(a\). The trajectory therefore forces \(A\ge(n-2)(n-1)\), yielding

\[|w|\ge(n-1)^2.\]

Equality forces exactly \(n-1\) effective \(b\)-steps on that trajectory, using **every** \(b\) of the word, with precisely \(n-1\) copies of \(a\) between successive \(b\)'s and none before the first or after the last. Consequently, the **only** possible reset word of length \((n-1)^2\) is \(W_n=b(a^{n-1}b)^{n-2}\). The explicit image calculation in step 2 shows that it does reset \(C_n\); hence this lower bound and uniqueness are sharp.

**2. Image dynamics in the \(n\)-state factor.** Put \(g_n=a^{n-1}b\). After the first \(b\), the image of \(Q_n\) is \(\{0,1,\ldots,n-2\}\). An elementary induction gives, for every integer \(0\le j\le n-2\),

\[
Q_n\cdot bg_n^{j}=\{0,1,\ldots,n-j-2\}.
\]

Indeed, \(a^{n-1}\) rotates this interval backwards by one, introducing \(n-1\) and deleting its previous largest element; \(b\) then merges \(n-1\) into the already-present \(0\). At \(j=n-2\) the image is \(\{0\}\), establishing that \(W_n\) resets \(C_n\). At \(j=n-3\) the image is \(\{0,1\}\). Starting from this pair, the suffix \(a^{n-3}ba^2b\) maps it by \(a^{n-3}\) to \(\{n-3,n-2\}\), leaves it unchanged under \(b\), maps it under \(a^2\) to \(\{n-1,0\}\), and merges it to \(\{0\}\) under the final \(b\). Thus \(V_n\) also resets \(C_n\).

**3. The three-state factor.** After the initial \(b\), the image of \(Q_3\) is \(\{0,1\}\). On that pair, the block \(g_n=a^{n-1}b\) has the following effect, determined solely by \(n\pmod3\):

- If \(n\equiv0\pmod3\), then \(g_n=a^2b\) as an action on \(Q_3\), and sends \(\{0,1\}\) to the singleton \(\{0\}\).
- If \(n\equiv1\pmod3\), then \(g_n=b\) as an action on \(Q_3\), and fixes \(\{0,1\}\).
- If \(n\equiv2\pmod3\), then \(g_n=ab\) as an action on \(Q_3\), and also sends \(\{0,1\}\) back to itself.

Since \(n\ge4\), it follows that \(W_n\) resets \(C_3\) exactly when \(3\mid n\), and otherwise has final image \(\{0,1\}\).

For \(V_n\), the common prefix \(bg_n^{n-3}\) has a singleton image on \(C_3\) when \(3\mid n\) (then \(n\ge6\)). In the residue-one case it has image \(\{0,1\}\); the suffix \(a^{n-3}ba^2b\) acts as \(ab a^2b\), sending \(\{0,1\}\) first back to itself and then to \(\{0\}\). In the residue-two case the same suffix begins with \(a^2b\), which already merges \(\{0,1\}\) to \(\{0\}\). Hence \(V_n\) resets \(C_3\) for every \(n\ge4\).

**4. Sharpness for the product.** Every common reset word has length at least \((n-1)^2\) by step 1. When \(3\mid n\), the word \(W_n\) achieves that bound in both factors. When \(3\nmid n\), the unique word of that length resetting \(C_n\) is \(W_n\), but it does **not** reset \(C_3\); hence a common reset word must be at least one letter longer. Step 3 supplies the common reset word \(V_n\) of length \((n-1)^2+1\). These upper and lower bounds coincide, proving the theorem. \(\square\)

## Verification

Two standalone standard-library Python programs accompany this result. Run `python3 verify_bfs.py` for independent exhaustive subset-pair breadth-first searches over every \(4\le n\le16\); the script explores every reachable image pair in increasing word length and checks the exact shortest common reset distance against the formula. Run `python3 verify_direct.py` to independently apply both explicit witnesses to every individual state for every \(4\le n\le70\), check the intermediate image-pair identity, and verify the modular behavior in \(C_3\). Both programs completed successfully on the supplied files. The all-integer result rests on the proof above; finite tests are supplementary, not a substitute for it.

## Relationship to prior work

Fernau and Rystsov (arXiv:2611.09136v1, first public November 6, 2026) develop general direct-product synchronization bounds and ask when they can be sharp. Their Proposition 3.4 gives \(\max\{\operatorname{rt}(C_n),\operatorname{rt}(C_3)\}\le\operatorname{rt}(C_n\times C_3)\le\operatorname{rt}(C_n)+\operatorname{rt}(C_3)\), which confines this product to an interval of width four but does not specify the modulo-three formula. Their section on the Černý automaton treats a single factor and not the common-word intersection.

An accessible public exact census of simultaneous Černý thresholds (October 13, 2026) already gives every pair \(2\le m<n\le11\), including the instances of the present formula with \(m=3\) and \(4\le n\le11\). These **finite instances are prior work**, not original contributions here; the statement proved here applies to all \(n\ge4\). The same earlier census proves the zero-overhead baseline \(m\mid n\) in all sizes, which covers our divisible branch. The nondivisible branch and the uniform one-letter witness complete the fixed-three-state slice.

Other public results prove the uniqueness of the optimal single-factor Černý word and classify near-shortest single-factor reset words. Those results are used as comparison points: they do not classify whether a single word simultaneously resets the three-state factor. The present proof reconstructs the required single-factor lower bound and rigidity explicitly instead of assuming novelty for them.

## Limitations

The result is specific to the standard labeled Černý pair with one three-state factor; no corresponding formula is asserted for an arbitrary second factor \(C_m\), differently aligned input letters, or other synchronizing automata. The result establishes exact optimal lengths and explicit witnesses, not a count of **all** common shortest words. Previous work already determines the stated zero-overhead branch and the small finite examples. An unindexed equivalent all-length common-reset theorem cannot be ruled out from bibliographic searching alone.

## References

1. H. Fernau and I. Rystsov, *Shortest Synchronizing Words on Product Automata*, arXiv:2611.09136v1, first posted November 6, 2026, especially Proposition 3.4, Section 4.1 and Section 7. https://arxiv.org/html/2611.09136v1
2. *Exact simultaneous reset thresholds for pairs of Černý automata through eleven states*, publicly accessible research record (October 13, 2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-exact-simultaneous-reset-thresholds-for-pairs-of-ern-automata-th--46765b03d598
3. *One-letter slack rigidity in the Černý reset language*, publicly accessible research record (November 2, 2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-one-letter-slack-rigidity-in-the-ern-reset-language--61d8f6568fe8
4. *Rigidity of shortest reset words in cyclic one-point automata*, publicly accessible research record (November 8, 2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-rigidity-of-shortest-reset-words-in-cyclic-one-point-automata--34a9919c4680
5. J. Černý, “Poznámka k homogénnym experimentom s konečnými automatmi,” *Matematicko-fyzikálny časopis* 14 (1964), 208–216.
