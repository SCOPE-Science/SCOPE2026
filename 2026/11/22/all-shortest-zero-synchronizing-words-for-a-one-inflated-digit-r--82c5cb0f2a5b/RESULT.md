# All shortest zero-synchronizing words for a one-inflated-digit radix family

## Finding

Let \(b\ge3\) and \(k\ge2\) be integers, and put
\[
D_{b,k}=\{0,1,\ldots,b-2,b^k-1\},\quad
M=\frac{b^k-1}{b-1},\quad H=\frac{b^{k-1}-1}{b-1},\quad B=b^k.
\]
For the canonical finite carry automaton associated with \(D_{b,k}\), **the shortest input word taking every carry to zero has length exactly \(2k-1\)**. Moreover, **all** shortest words are given by the following disjoint intervals of their ordinary radix values \(A\):
\[
BV-H+M\le A\le BV+(b-2)M,
\qquad V=\sum_{j=0}^{k-2}v_jb^j,\quad v_j\in\{1,\ldots,b-2\}.
\tag{1}
\]
Input words are read least-significant-digit first; a value \(A\) has a unique standard length-\(2k-1\) input with zero padding. In particular, the **exact number of shortest synchronizing words** is
\[
\boxed{(b-2)^{k-1}\left((b-1)b^{k-1}-\frac{b^k-1}{b-1}\right)}.
\tag{2}
\]
For \(b=3\), this gives precisely \((3^{k-1}+1)/2\) minimum words. The shortest-length statement in that ternary case was previously known, but its complete minimum-word classification was not established in the cited predecessor.

## Assumptions and scope

For each residue \(r\in\{0,\ldots,b-1\}\), set \(d_r=r\) if \(r\le b-2\), and \(d_{b-1}=b^k-1\). The state set is \(K=\{-M,-M+1,\ldots,0\}\). For an input digit \(a\in\{0,\ldots,b-1\}\), the carry transition is
\[
h_a(c)=\frac{a+c-d_{(a+c)\bmod b}}b.
\]
The specified transitions leave \(K\) invariant: their minimum is at least \(-M\), and their maximum is at most zero. A word \(a_0a_1\cdots a_{m-1}\), processed with \(a_0\) first, is zero-synchronizing if the final state is zero for **every** \(c\in K\). Only integer bases \(b\ge3\) and orders \(k\ge2\) are asserted in the theorem. The ordinary-digit case \(k=1\) is not part of the classification.

## Proof

**1. Exact interval criterion.** Define the length-\(m\) nonstandard representation set
\[
T_m=\left\{\sum_{j=0}^{m-1}\delta_jb^j:\delta_j\in D_{b,k}\right\}.
\]
Because \(D_{b,k}\) contains exactly one representative of every residue modulo \(b\), the \(b^m\) elements of \(T_m\) represent distinct residue classes modulo \(b^m\). Iteration of the transition identity yields
\[
A+c=\sum_{j=0}^{m-1}d_{(a_j+c_j)\bmod b}b^j+b^m c_m,
\quad A=\sum_{j=0}^{m-1}a_jb^j.
\]
Consequently the final carry from \(c\) is zero exactly when \(A+c\in T_m\). Therefore the word of value \(A\) is zero-synchronizing exactly when
\[
[A-M,A]\cap\mathbb Z\subseteq T_m.\tag{3}
\]

**2. No words of length below \(2k-1\).** First suppose \(k\ge3\). Set
\[
Q=(B-1)(b^{k-2}+b^{k-3}).
\]
Then \(Q>b^{2k-2}\). The residue of \(Q\) modulo \(b^{k-1}\) uniquely prescribes the first \(k-1\) nonstandard digits of any representation: they are \(B-1\) at positions \(k-2,k-3\), and zero elsewhere. Hence every nonnegative representable integer in this residue class is at least \(Q\). None lies in \([0,b^{2k-2})\). A putative synchronizing word of length at most \(2k-2\) has \(A<b^{2k-2}\) but, by (3), needs all \(M+1>b^{k-1}\) consecutive integers of \([A-M,A]\) to be nonnegative and represented. That interval necessarily meets the forbidden residue class, a contradiction.

If \(k=2\), the elements of \(T_2\) below \(b^2\) are precisely those ordinary base-\(b\) two-digit numbers whose digits both belong to \(\{0,\ldots,b-2\}\), together with \(b^2-1\). No consecutive run of these numbers has length \(M+1=b+2\). By (3) no length-two word resets, and the inclusion \(T_1\subseteq T_2\) excludes length one. Thus, for all \(k\ge2\), the reset length is at least \(2k-1\).

**3. Structure of the length-\(2k-1\) represented integers.** We inspect representations \(0\le n<b^{2k-1}\). At positions \(i\ge k\), the exceptional digit contributes at least \((B-1)b^k>b^{2k-1}\), so such positions must use ordinary digits \(0,\ldots,b-2\). In each of the lower \(k\) places, replace an exceptional digit \(B-1\) by the signed digit \(-1\), recording an extra \(B\). Thus every representation is
\[
n=e+B(E+U),\quad
 e=\sum_{i=0}^{k-1}t_i b^i,\quad
 E=\sum_{i:t_i=-1}b^i,\quad
 U=\sum_{j=0}^{k-2}u_jb^j,
\]
with \(t_i\in\{-1,0,\ldots,b-2\}\) and \(u_j\in\{0,\ldots,b-2\}\). Every integer \(e\) in the **complete consecutive interval** \([-M,(b-2)M]\), of exactly \(B\) integers, has exactly one such signed expansion: the signed digit set is a full set of residues modulo \(b\), and the interval has \(b^k\) members. Thus the decomposition \(n=BV+e\), with \(-M\le e\le(b-2)M\), is unique.

For \(0\le V<b^{k-1}\), the top signed digit \(t_{k-1}=-1\) forces \(E\ge b^{k-1}>V\), making \(U=V-E<0\) impossible. The corresponding initial block \(-M\le e<-H\) is therefore absent. For every remaining \(e\in[-H,(b-2)M]\), its top signed digit belongs to \(\{0,\ldots,b-2\}\), and the lower signed digits determine a mask \(E\) whose base-\(b\) digits lie in \(\{0,1\}\) and whose length is \(k-1\). Such an integer \(BV+e\) is represented **if and only if** \(V-E\) has exactly \(k-1\) base-\(b\) digits in \(\{0,\ldots,b-2\}\), including leading zeros.

If all the digits of \(V\) belong to \(\{1,\ldots,b-2\}\), subtracting any permitted mask \(E\) causes no borrow and stays in \(\{0,\ldots,b-2\}\) digitwise. Thus every integer in
\[
I_V=[BV-H,BV+(b-2)M]\cap\mathbb Z
\tag{4}
\]
is represented. This run contains exactly
\[
|I_V|=H+(b-2)M+1=(b-1)b^{k-1}
\]
consecutive integers.

Conversely, if some digit of \(V\) equals \(b-1\), choose the mask \(E=0\). Then \(U=V\) is forbidden. If instead some digit of \(V\) equals zero, say at position \(j\), choose \(E=b^j\). Then \(V-E\) is either negative or has a forbidden digit \(b-1\) at position \(j\) after borrowing. In each case, every interval of \(b^{k-1}\) consecutive allowed values of \(e\) encounters a forbidden integer: its residues modulo \(b^{k-1}\) exhaust all lower signed-digit patterns, including the one specifying the chosen mask. Therefore **no** run in a non-interior \(V\)-block has length greater than \(b^{k-1}-1\), too short for (3).

Every regular block begins with an absent interval of length \(b^{k-1}\), so runs cannot join across blocks. At the upper boundary \(V=b^{k-1}\), only integers with \(-M\le e<0\) remain under \(b^{2k-1}\): at most \(M\) integers, hence no long run. Therefore the only runs of length at least \(M+1\) within the standard input range are precisely the intervals (4) for interior \(V\).

**4. All shortest words and their count.** By (3), a length-\(2k-1\) input of value \(A\) resets exactly when the interval \([A-M,A]\) is contained in some \(I_V\). This is equivalent to (1). All those intervals are nonempty because \((b-1)b^{k-1}>M\), and they are disjoint because they belong to separated blocks. There are \((b-2)^{k-1}\) interior choices of \(V\), each contributing \((b-1)b^{k-1}-M\) values of \(A\). This proves (2). The existence of such words also establishes the upper bound \(2k-1\), completing the proof. \(\square\)

## Verification

The accompanying `verify.py` computes full nonstandard representation sets and enumerates **every** legal zero-reset interval for a selection of bases and exponents, comparing the exact lists with (1) and (2). Separately, a subset-automaton breadth-first search derives shortest reset lengths directly from the carry maps. The two algorithms collectively pass 32 parameter checks, including \(b=3,\ldots,8\) and \(k=2,3\), plus four cases with \(k=4\), and smaller independent BFS checks. Run `python3 verify.py` using Python 3 and the standard library. Finite tests corroborate but do not replace the argument above.

## Relationship to prior work

Zhou's 2026 preprint proves a general qualitative carry-synchronization criterion for complete-residue digit systems, and explicitly asks for quantitative shortest-length bounds. A published 2026 result entitled *Sharp zero-synchronizing lengths for a ternary nonstandard digit family* already establishes the **ternary** shortest length in precisely the reparametrized case \(b=3\), with a lower bound of \((3^{k-1}+1)/2\) on the number of shortest words. Its statement explicitly does **not** assert an exhaustive count. The present contribution classifies every shortest word, proves that its ternary lower bound is exact, and treats **all higher bases** in one structural theorem. Neither the general qualitative criterion nor the published ternary-only length-and-lower-bound theorem implies the exact multi-base classification stated here. The 2025 two-dimensional expanding-rational-matrix addition-automata analysis is useful background but does not involve these scalar digit sets or determine their optimal reset-word families.

## Limitations

The classification concerns only the specified scalar complete-residue family and zero-target synchronization, not all digit sets or arbitrary synchronization targets. It does not claim priority for the already-known ternary minimal length. Possible unindexed equivalent classifications or general results on reset words remain an originality risk. The argument has not undergone independent mathematical audit; the finite checker alone is not a proof of the universal formula.

## References

1. N. H. Zhou, *Periodic counting, carry synchronization, and primes in nonstandard numeration systems*, arXiv:2611.07446v1, first posted 2026-11-05. https://arxiv.org/html/2611.07446v1 (Sections 4 and 6.3).
2. *Sharp zero-synchronizing lengths for a ternary nonstandard digit family*, published research result, 2026-11-08, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-zero-synchronizing-lengths-for-a-ternary-nonstandard-digit--fa7b02222afc/RESULT.md.
3. A. G. R. Cruz, M. J. C. Loquias, J. M. Thuswaldner, *Addition Automata and Attractors of Digit Systems Corresponding to Expanding Rational Matrices*, arXiv:2507.06158v1, first posted 2025-07-08. https://arxiv.org/html/2507.06158v1.
