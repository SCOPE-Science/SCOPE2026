# The complete palindromic language and maximal factors of geometric-marker automatic words

## Finding
For an arbitrary integer base \(b\ge2\), put \(w_b(i)=1\) if \(i=b^j\) for some integer \(j\ge0\), and \(w_b(i)=0\) otherwise, for every integer \(i\ge0\). Define
\[
g_t=(b-1)b^t,\qquad H_0=1,\qquad H_t=(b-1)b^{t-1}-1\quad(t\ge1).
\]
The **complete set of nonempty palindromic factors** of this infinite word is
\[
\{0^n:n\ge1\}\;\cup\;\{0^h10^h:h\ge0\}\;\cup\;
\left\{0^h10^{g_t-1}10^h:t\ge0,\ 0\le h\le H_t\right\}.
\]
Here all exponents denote nonnegative integral repetition counts. In particular, no palindrome has three or more occurrences of the symbol \(1\).

A palindromic factor is called **globally maximal** if neither \(0u0\) nor \(1u1\) occurs as a factor of the infinite word. All globally maximal palindromic factors, without exception, are
\[
M_{b,t}=0^{H_t}10^{g_t-1}10^{H_t}\qquad(t\ge0).
\]
They have distinct lengths
\[
|M_{b,0}|=b+2,\qquad
|M_{b,t}|=(b-1)(b+2)b^{t-1}-1\quad(t\ge1).
\]
If \(P_b(n)\) denotes the number of distinct palindromic length-\(n\) factors, then, for each integer \(n\ge1\),
\[
P_b(n)=1+\mathbf 1_{\{n\text{ odd}\}}+
\sum_{t\ge0}\mathbf1_{\{g_t+1+2h:\,0\le h\le H_t\}}(n).
\]
The sum has at most one nonzero term. Thus \(P_b(n)\in\{1,2,3\}\) and, more strongly, \(P_b(n)\le3\). For the binary base this simplifies to
\[
P_2(1)=2,\quad P_2(2)=P_2(4)=2,\quad
P_2(n)=3\text{ for odd }n\ge3,\quad
P_2(n)=1\text{ for even }n\ge6.
\]
In bases \(b\ge3\), the two-symbol palindromes of a fixed level \(t\ge1\) occur at precisely the lengths of the appropriate parity in the interval
\[
(b-1)b^t+1\le n\le (b-1)(b+2)b^{t-1}-1.
\]
These intervals are pairwise disjoint.

## Assumptions and scope
Only one-sided, zero-indexed factors with starting position at least zero are considered; a factor must occur at least once, not necessarily with positive frequency. The base \(b\) is any integer at least two, without a primality hypothesis. Symmetric extension is an extension *somewhere* in the infinite factor language; failure of extension at one occurrence alone would not establish global maximality. The empty word is excluded.

## Proof
**1. Excluding three or more marked positions.** The positions with symbol \(1\) are exactly \(1,b,b^2,\ldots\). Consider any palindromic factor containing \(m\ge3\) such positions \(b^{a_1}<\cdots<b^{a_m}\). Since the factor is palindromic, the first and last marked positions, and the second and penultimate, have the same midpoint. When \(m\ge4\), this would force
\[
b^{a_1}+b^{a_m}=b^{a_2}+b^{a_{m-1}}.
\]
Both sides are sums of *two distinct* powers of \(b\). Such sums have two unit digits in base \(b\), and therefore uniquely determine the unordered pair of exponents, contradicting the strictly increasing order. When \(m=3\), symmetry forces
\[
b^{a_1}+b^{a_3}=2b^{a_2},
\]
with \(a_1<a_2<a_3\). Dividing by \(b^{a_1}\) gives \(1+b^{a_3-a_1}=2b^{a_2-a_1}\), impossible modulo \(b\). Thus at most two marked positions occur in any palindromic factor.

**2. Zero- and single-marked factors.** Every \(0^n\) occurs in the arbitrarily long gaps between successive powers. Every \(0^h10^h\) occurs around a sufficiently isolated power \(b^t\), since both neighboring marked-position gaps grow without bound. All palindromes having at most one marked position are exhausted by these two forms.

**3. The two-marked factors.** If a factor contains exactly two occurrences of \(1\), they must be at consecutive marked positions \(b^t\) and \(b^{t+1}\); otherwise a third marked position lies strictly between them. Their distance is \(g_t=(b-1)b^t\). A palindrome containing exactly these two markers must have equal numbers \(h\) of zeros outside them, hence must be \(0^h10^{g_t-1}10^h\). At \(t=0\) the left marker is at position \(1\), so \(h\le1\); the right marker has enough available zeros, including the base-two case. At every \(t\ge1\), the previous marker is at \(b^{t-1}\), at distance \(g_{t-1}\) to the left, so \(h\le g_{t-1}-1=H_t\). The distance from \(b^{t+1}\) to the following marker \(b^{t+2}\) exceeds this left allowance. Each allowed \(h\) therefore occurs, and no other two-marked palindrome exists.

**4. Global maximality.** Pure-zero factors and single-marker palindromes can each be symmetrically extended with zeros by choosing a sufficiently large marker-free gap. For a two-marker palindrome at level \(t\), when \(h<H_t\), both ends can be extended by a zero at the same occurrence. When \(h=H_t\), the left neighbor is outside the one-sided word if \(t=0\), or is the preceding marked position (hence symbol \(1\)) if \(t\ge1\). For \(t\ge1\) the right neighbor is symbol \(0\); when \(t=0\) its value is irrelevant because the left boundary lies outside the word. Hence no symmetric extension is possible at this unique occurrence. Because the gap \(g_t\) uniquely determines \(t\) and there is exactly one consecutive pair of powers with that gap, the same factor has no other occurrence that could permit a symmetric extension. The displayed family is therefore precisely the family of globally maximal palindromic factors.

**5. Counting lengths.** The zero-only factor contributes one factor of every positive length. The single-marker factors contribute one more precisely at odd positive lengths. The two-marker factor at level \(t\) with padding \(h\) has length \(g_t+1+2h\), and the allowed values of \(h\) are distinct. For \(t\ge1\), their length intervals begin at \(g_t+1\) and end at \(g_t+1+2H_t=(b-1)(b+2)b^{t-1}-1\). The next interval begins at \((b-1)b^{t+1}+1\), which exceeds the preceding endpoint by \((b-1)(b-2)(b+1)b^{t-1}+2>0\). Level zero has lengths \(b\) and \(b+2\); the first later level begins at \((b-1)b+1\). For \(b\ge3\) this exceeds \(b+2\); for \(b=2\), it begins at \(3\) but comprises odd lengths whereas the level-zero lengths are even. No two levels contribute the same length, establishing the exact count and the bound \(P_b(n)\le3\).

In the base-two case, the later-level length intervals are exactly the odd numbers from \(2^t+1\) through \(2^{t+1}-1\), for \(t\ge1\). They partition all odd lengths at least three. Combining them with the level-zero exceptions proves the displayed binary-base simplification.

## Verification
The accompanying `verify.py` directly enumerates factors of a finite prefix of the defined word and compares their *actual strings*, not just their counts, against the complete predicted palindromic language. It also checks globally maximal factors using the two symmetric extension tests. Execute with `python verify.py`. The checked bases are \(2\) through \(10\), and factor lengths are \(1\) through \(110\), using a prefix of length \(13000\). The program reports `VERIFY_OK` on agreement. The unbounded theorem rests on the symbolic proof above; finite enumeration alone is not a proof for all bases and lengths.

## Relationship to prior work
The palindromic-complexity invariant is classical: Allouche, Baake, Cassaigne and Damanik investigate it for Rote words and particular primitive uniform morphic words, and prove general bounds. The geometric-marker words here have unbounded zero gaps and are not in the uniformly recurrent primitive family covered by that analysis. Dvořáková, Ochem and Opočenská classify binary words with *finitely many distinct palindromes* subject to critical-exponent constraints; the present words have infinitely many zero-only palindromes and unbounded powers, so those theorems do not imply this exact language. Frid, Laborde and Peltomäki treat *prefix palindromic length*, a different invariant. Related literature on sparse automatic words and previous power-marker factorization and reflection questions does not by itself identify these complete maximal factors or all the exact length counts. No claim of novelty is based solely on failing to find a title match.

## Limitations
These formulas do not provide the frequency of every palindromic factor or the usual subword complexity. Occurrence is existential in the one-sided word; almost all factor occurrences may be rare. The prior-art comparison was conducted against specific relevant accessible papers and mathematical-record searches and cannot rule out an unindexed equivalent result. Only self-review has been carried out; independent audit has not been performed.

## References
- L. Dvořáková, P. Ochem, D. Opočenská, *Critical exponent of binary words with few distinct palindromes*, arXiv:2311.13003 (first submitted 2023-11-21), https://arxiv.org/html/2311.13003v2 .
- J.-P. Allouche, M. Baake, J. Cassaigne, D. Damanik, *Palindrome complexity*, arXiv:math/0106121 (2001), https://arxiv.org/html/math/0106121v1 .
- A. E. Frid, E. Laborde, J. Peltomäki, *On prefix palindromic length of automatic words*, arXiv:2009.02934 (2020), https://arxiv.org/abs/2009.02934 .
