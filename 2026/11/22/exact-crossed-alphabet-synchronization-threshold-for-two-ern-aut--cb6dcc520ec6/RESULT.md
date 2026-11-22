# Exact crossed-alphabet synchronization threshold for two Černý automata

## Finding
For every integer \(n\ge2\), let \(C_n\) be the complete deterministic automaton on \(Q=\mathbb Z/n\mathbb Z\) with alphabet \(\{a,b\}\): letter \(a\) adds one modulo \(n\), and \(b\) fixes every state except that it maps \(n-1\) to \(0\). Let \(C_n^{\mathrm{op}}\) be the same automaton with the roles of the two input letters exchanged. Their ordinary synchronous direct product has exact reset threshold
\[
\boxed{\operatorname{rt}(C_n\times C_n^{\mathrm{op}})=2(n^2-3n+3)}.
\]
Equivalently, the shortest binary word that resets both the original and letter-exchanged Černý automata has this length. For \(n\ge3\) this is exactly \(2n-4\) less than the sum of their individual shortest-reset lengths \(2(n-1)^2\), and exactly \(n^2-4n+5\) more than either individual threshold. For \(n=2\), the threshold is \(2\).

## Assumptions and scope
Words are read from left to right. A reset word sends the **entire** state set to a singleton; the two target states need not coincide. The first factor has transitions
\[
 a(i)=i+1\pmod n,\qquad
 b(i)=\begin{cases}0&i=n-1,\\i&0\le i\le n-2.\end{cases}
\]
In the second factor, input \(b\) rotates by one and input \(a\) has the same defect-one transition as the first factor's \(b\). Both factors share the *same* literal input word. This is the coordinatewise direct product, not the asynchronous or two-tape product. All assertions concern every integer \(n\ge2\), with no probabilistic or heuristic assumptions.

## Proof
**1. A mandatory scattered subsequence.** Put
\[
 R_n=b(a^{n-1}b)^{n-2},\qquad |R_n|=(n-1)^2.
\]
Every reset word of \(C_n\) contains \(R_n\) as a scattered subsequence. Here is a direct proof. For each initial state \(i\), follow its trajectory under an arbitrary reset word \(w\). Write \(A\) for the total number of input \(a\)'s, and \(B_i\) for the number of occurrences of input \(b\) encountered while this particular trajectory is at state \(n-1\). Both an \(a\) and a counted \(b\) advance that trajectory by one modulo \(n\); an uncounted \(b\) fixes it. Therefore its terminal state equals \(i+A+B_i\pmod n\). Since the \(n\) terminal states are equal, the \(B_i\) have all \(n\) distinct residues modulo \(n\). One trajectory consequently has at least \(n-1\) counted \(b\)'s. Just after each such \(b\) it lies at \(0\). To reach \(n-1\) for the next counted \(b\), it must read at least \(n-1\) input \(a\)'s; all intervening \(b\)'s are uncounted and leave this trajectory fixed. Selecting \(n-1\) of those counted \(b\)'s and \(n-1\) intervening \(a\)'s between consecutive ones exhibits \(R_n\). By exchanging the two input letters, any reset word of \(C_n^{\mathrm{op}}\) contains
\[
 R_n^{\mathrm{op}}=a(b^{n-1}a)^{n-2}
\]
as a scattered subsequence. Thus every common reset word is a common supersequence of these two fixed words. This argument also proves the needed nonstandard subsequence lemma independently of finite computations.

**2. Their exact longest common subsequence.** We show
\[
\operatorname{LCS}(R_n,R_n^{\mathrm{op}})=2(n-2).
\]
Let \(x\) be a common scattered subsequence, with \(\alpha\) occurrences of \(a\), \(\beta\) of \(b\), and \(r_a,r_b\) maximal nonempty runs of the respective letters. In \(R_n\), there are exactly \(n-2\) runs of \(a\), and each \(b\) is isolated. Each of the \(\beta-r_b\) pairs of adjacent \(b\)'s within a run of \(x\) forces at least one **distinct** intervening \(a\)-run of \(R_n\) to be completely skipped. The \(r_a\) runs of \(x\) require at least \(r_a\) unskipped source \(a\)-runs. Hence
\[
 r_a+\beta-r_b\le n-2.
\]
Likewise, \(R_n^{\mathrm{op}}\) has \(n-2\) runs of \(b\), with singleton \(a\)'s, so
\[
 r_b+\alpha-r_a\le n-2.
\]
The two inequalities add to \(|x|=\alpha+\beta\le2(n-2)\). The word \((ab)^{n-2}\) is a scattered subsequence of each source, proving equality. The case \(n=2\) is included: the sources are the different one-letter words \(b\) and \(a\), whose LCS is empty. Therefore the shortest common supersequence of the mandatory patterns has length
\[
 2(n-1)^2-2(n-2)=2(n^2-3n+3).
\]
This is a lower bound for any common reset word; notably, containing a reset word as a scattered subsequence is **not** in general sufficient to reset an automaton.

**3. A matching common reset word.** For \(n=2,3,4\), respectively, take the literal words
\[
 ab,\qquad abbaab,\qquad abbaaabaaabbba.
\]
Their lengths are \(2,6,14\), and direct application of the specified transition tables sends both complete state sets to singletons.

For every \(n\ge5\), put
\[
\begin{aligned}
 U_n&=ab^2(a^{n-1}b)^{n-3},\\
 W_n&=U_n\,a^2\,(b^{n-1}a)^{n-5}\,b^{n-1}a^2b^{n-1}a.
\end{aligned}
\]
A count of its displayed blocks gives \(|W_n|=2(n^2-3n+3)\). To check its action exactly, write \(Q\cdot v\) for the image of all states after reading \(v\) in the first factor and \(Q\cdot_{\mathrm{op}}v\) for the second factor. In the first factor, \(ab^2\) leaves \(\{0,\ldots,n-2\}\); each subsequent \(a^{n-1}b\) removes its current largest state. Thus
\[
 Q\cdot U_n=\{0,1\}.
\]
In the second factor, \(ab^2\) gives \(\{0,2,\ldots,n-1\}\), and after \(j\) of the blocks \(a^{n-1}b\), for \(1\le j\le n-3\), its image is exactly
\[
 \{1,\ldots,j\}\cup\{j+2,\ldots,n-1\}.
\]
Indeed, here the input \(a\) maps \(n-1\) to \(0\) and input \(b\) rotates the resulting set by one. Consequently
\[
 Q\cdot_{\mathrm{op}}U_n=\{1,\ldots,n-3\}\cup\{n-1\}.
\]
After the next input \(a^2\), the two images are, respectively, \(\{2,3\}\) and \(\{0,\ldots,n-3\}\). In the first factor, every \(b^{n-1}\) in the following \((b^{n-1}a)^{n-5}\) is ineffective and each \(a\) rotates the pair, leaving \(\{n-3,n-2\}\). In the second factor, each \(b^{n-1}a\) turns \(\{0,\ldots,k\}\) into \(\{0,\ldots,k-1\}\), leaving \(\{0,1,2\}\). The final three blocks act as follows:

| Read block | First image | Second image |
|---|---|---|
| Before final three blocks | \(\{n-3,n-2\}\) | \(\{0,1,2\}\) |
| \(b^{n-1}\) | \(\{n-3,n-2\}\) | \(\{n-1,0,1\}\) |
| \(a^2\) | \(\{n-1,0\}\) | \(\{0,1\}\) |
| \(b^{n-1}a\) | \(\{1\}\) | \(\{0\}\) |

The singleton terminal images prove that \(W_n\) resets the synchronous product. Its length matches the lower bound, proving the theorem for every \(n\ge2\).

## Verification
Two self-contained Python 3 programs independently check the new all-size formula in finite ranges. `verify_bfs.py` performs complete breadth-first search on the product of the two subset automata for \(2\le n\le9\); the shortest distances are \(2,6,14,26,42,62,86,114\), matching the theorem. It also replays explicit witnesses. `verify_structure.py` uses separately implemented direct state transitions to verify the displayed construction and its intermediate invariants for \(2\le n\le50\), and an independent LCS dynamic program to check \(\operatorname{LCS}(R_n,R_n^{\mathrm{op}})=2(n-2)\) for \(2\le n\le30\). The actual recorded outputs are included. Run `python3 verify_bfs.py` and `python3 verify_structure.py` in the same directory; no dependencies beyond the Python standard library are needed. The all-integer proof above, not these finite experiments, establishes the theorem.

## Relationship to prior work
Fernau and Rystsov's *Shortest Synchronizing Words on Product Automata* (submitted 6 November 2026) proves the general synchronous-product bound \(\max\{\operatorname{rt}(A),\operatorname{rt}(B)\}\le\operatorname{rt}(A\times B)\le\operatorname{rt}(A)+\operatorname{rt}(B)\) (Proposition 3.4) and studies the standard Černý automaton in its Section 4. This does not determine the sharp value for two equally sized factors with **opposite** assignments of letters to permutation/defect maps. The exact crossed value lies strictly inside the generic interval for every \(n\ge3\).

The previously reported mandatory-subsequence lemma and letter-weight lower bound for one standard Černý automaton are compatible with Step 1 above, which gives a direct proof for the required normalization. A published finite investigation of simultaneous reset thresholds for differently sized, equally oriented Černý pairs treats \(2\le m<n\le11\); it excludes the present equal-size opposite-orientation all-\(n\) family. Maslennikova (2014) studies complexity of equality/inclusion of reset languages, rather than their shortest common word for this family. These comparisons concern statements and implications, not just similar titles.

## Limitations
The theorem does not classify **all** shortest common reset words, nor arbitrary products, unequal factor sizes, partial automata, independently controlled/two-tape products, or other letter permutations. The simple bound from common-supersequence length is special to the two rigid required patterns and must be combined with the explicit reset-word construction; it is not a general equivalence of common supersequences and synchronizing words. Earlier formulations of this exact special family may exist outside indexed literature, and independent expert audit has not been performed.

## References
1. H. Fernau and I. Rystsov, *Shortest Synchronizing Words on Product Automata*, arXiv:2611.09136, first public version 6 November 2026, https://arxiv.org/html/2611.09136 .
2. M. Maslennikova, *Complexity of checking whether two automata are synchronized by the same language*, arXiv:1405.3576, first submitted 14 May 2014, https://arxiv.org/html/1405.3576v1 .
3. A. Kisielewicz, J. Kowalski and M. Szykuła, *Computing the shortest reset words of synchronizing automata*, first online 17 November 2013, https://doi.org/10.1007/s10878-013-9682-0 .
4. *A mandatory reset subsequence and exact one-step multiplicity for the Černý automata*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-a-mandatory-reset-subsequence-and-exact-one-step-multiplicity-fo--8a725fd1702c .
5. *Exact simultaneous reset thresholds for pairs of Černý automata through eleven states*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-exact-simultaneous-reset-thresholds-for-pairs-of-ern-automata-th--46765b03d598 .
6. *Uniform weighted-reset optimality in the Černý automata*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-uniform-weighted-reset-optimality-in-the-ern-automata--6527a70965c4 .
