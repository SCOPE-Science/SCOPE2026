# Three-one privileged binary words: a complete gap classification and partition law

## Finding
A finite word is *privileged* if it has length at most one, or if it is a complete first return to a shorter privileged word: it begins and ends with that word, which occurs exactly twice, including possible overlapping occurrences. Fix the binary alphabet \(\{0,1\}\), and write any word with exactly three \(1\)s uniquely as
\[
w=0^a1\,0^b1\,0^c1\,0^d,\qquad a,b,c,d\in\mathbb Z_{\ge0}.
\]
**Classification.** Such a word is privileged if and only if
\[
a=d\quad\text{and}\quad\bigl(a>\max\{b,c\}\ \text{or}\ b=c\ge a\bigr). \tag{1}
\]
In particular, every binary palindrome with exactly three \(1\)s is privileged. A privileged word in this family is not a palindrome precisely when \(a=d>\max\{b,c\}\) and \(b\ne c\).

Let \(Q_n\) count nonpalindromic privileged binary words of length \(n\) with exactly three \(1\)s, and let \(P_n\) count all privileged words with that length and content. Then, for all \(n\ge3\),
\[
Q_n=2\#\{(r,s,t)\in\mathbb Z_{\ge0}^3:2r+3s+4t=n-8\}, \tag{2}
\]
where the count is zero for negative right-hand sides. Equivalently,
\[
\sum_{n\ge3}Q_nz^n=\frac{2z^8}{(1-z^2)(1-z^3)(1-z^4)},\qquad
P_n=Q_n+\begin{cases}(n-1)/2,&n\text{ odd},\\0,&n\text{ even}.\end{cases} \tag{3}
\]
Consequently \(P_n\sim n^2/24\), and the proportion of all length-\(n\), weight-three binary words that are privileged is asymptotic to \(1/(4n)\). Nonpalindromic examples first occur at \(n=8\), in one reversal pair; their existence at that length was already recorded in the literature and is not claimed as novel.

## Assumptions and scope
All words are finite, indexed, and binary. An occurrence is a starting position of a contiguous factor; overlapping occurrences are counted separately. A border is nonempty and proper when used in the recursive privileged-word definition. Zero-run lengths in (1) are arbitrary nonnegative integers, including the cases of adjacent \(1\)s and empty endpoint runs. Reversal is **not** quotiented in the word counts; hence the factor of two in (2). The statement is restricted to exactly three occurrences of the symbol \(1\).

## Proof
**Auxiliary border facts.** Every zero power \(0^k\), \(k\ge1\), is privileged: for \(k>1\) it is a complete first return to \(0^{k-1}\), while \(0\) is privileged by definition. Also, for all \(a,b,c\ge0\), a two-one word \(0^a1 0^b1 0^c\) is privileged if and only if \(a=c\). Necessity follows from the general privileged-prefix/suffix lemma described below (or by a direct induction on a privileged border). For sufficiency put \(a=c\). If \(a=0\), the word is a complete first return to \(1\). If \(a\ge1\) and \(b<a\), it is a complete first return to \(0^a\). If \(a\ge1\) and \(b\ge a\), it is a complete first return to the privileged one-one word \(0^a1 0^a\); that border occurs exactly twice, once around each \(1\).

A standard elementary privileged-prefix lemma says that every privileged prefix of a privileged word is also its suffix, and conversely under reversal. Its short induction examines the shorter privileged border defining the complete first return: a shorter privileged prefix must also border that shorter word or else would create a third occurrence. Consequently a privileged word beginning with \(0^a\) and ending with \(0^d\) must have \(a=d\), including the zero-run endpoint cases; if just one endpoint has no zeros, the first and last letters differ, which is impossible for a word of length at least two with a nonempty border. This lemma and the run-equality consequence are explicit in Forsyth–Jayakumar–Shallit (2013, Theorem 1 and Corollary 2); the preceding reasoning explains their use here.

**Necessity of (1).** Let \(w\) be privileged. By endpoint-run equality, \(a=d\). Let \(u\) be a privileged proper border appearing exactly twice. It cannot contain all three \(1\)s: the initial and terminal occurrences would give the same nonempty finite set of one-positions translated by the positive shift \(|w|-|u|\). The remaining cases are exhaustive.

If \(u\) has no \(1\), then it is \(0^k\) with \(1\le k\le a\). If \(k<a\), the two endpoint zero runs already contain at least four occurrences. Hence \(k=a\), and exactly two occurrences require \(b,c<a\), giving \(a>\max\{b,c\}\).

If \(u\) has one \(1\), the two-one-free privileged-border classification reduces it to \(u=0^a1 0^a\). (The one-one case follows directly from endpoint-run equality.) When \(a=0\), the candidate \(u=1\) occurs three times. When \(a>0\), for it to be both a prefix around the first \(1\) and a suffix around the last \(1\), both \(b,c\ge a\) are required; then it also occurs around the middle \(1\), giving at least three occurrences. This case is impossible.

If \(u\) has two \(1\)s, it is necessarily the prefix containing the first two \(1\)s and the suffix containing the last two. The two-one classification forces its initial and terminal zero runs to be equal to \(a\), so the prefix has the form \(0^a1 0^b1 0^a\) and must have \(c\ge a\). The matching suffix has the form \(0^a1 0^c1 0^a\), requiring \(b\ge a\). Equality forces \(b=c\ge a\). Thus (1) is necessary.

**Sufficiency of (1).** If \(a=d>\max\{b,c\}\), then \(0^a\) is privileged and occurs exactly twice in \(w\), at the endpoints, so \(w\) is privileged. If \(a=d\) and \(b=c\ge a\), the two-one word \(u=0^a1 0^b1 0^a\) is privileged by the auxiliary fact, and it appears exactly twice in \(w\), once on each consecutive pair of \(1\)s. No other occurrence is possible because there are only three \(1\)s. Thus \(w\) is privileged.

**Exact enumeration.** A word with three \(1\)s is a palindrome exactly when \(a=d\) and \(b=c\). Every such word satisfies one of the alternatives in (1), so the number of privileged palindromes is \((n-1)/2\) when \(n\ge3\) is odd and zero otherwise. For a nonpalindromic privileged word, choose which of \(b,c\) is larger (two choices) and uniquely define
\[
t=\min(b,c),\qquad s=|b-c|-1,\qquad r=a-\max(b,c)-1.
\]
Each parameter is nonnegative. Conversely any \((r,s,t)\in\mathbb Z_{\ge0}^3\) and either orientation reconstructs exactly one eligible word by setting \(\min(b,c)=t\), \(\max(b,c)=t+s+1\), \(a=d=t+s+r+2\). Its length is \(8+2r+3s+4t\). This is the bijection in (2), and the geometric-series product gives (3). The rational generating function has a pole of order three at \(z=1\) with leading singular term \((1/12)(1-z)^{-3}\); all other unit-circle poles have smaller order. Thus \(Q_n=n^2/24+O(n)\), and the palindrome term is \(O(n)\). Since there are \(\binom n3\sim n^3/6\) binary words of weight three, the last asymptotic follows.

## Verification
The standalone Python 3 script `verify.py` computes privileged membership directly from the recursive border/occurrence definition, independently of the gap classification. It exhaustively compares the two predicates for all \(40{,}920\) binary words with three \(1\)s at lengths \(3\) through \(32\). It separately tests \(3000\) seeded long-gap examples, the required weight-two border classification through length \(24\), and generating-function coefficients through length \(700\) using two independent integer computations. Executing `python verify.py` prints `VERIFY_OK`. These are finite diagnostics; the unrestricted conclusion follows from the border-type proof, not the tests.

## Relationship to prior work
Peltomäki, *Introducing Privileged Words* (public arXiv v1, 2012), introduced the relevant structural framework and already recorded the nonpalindromic privileged word `00101100`; that small example is prior art. Forsyth–Jayakumar–Shallit, *Remarks on Privileged Words* (2013), proved the equal-leading-and-trailing-run lemma and a restricted three-one sublanguage of the form \(0^{a+1}1 0^{b+1}11 0^{c+1}\) used for non-context-freeness. The larger complete-return construction \(0^t1u10^t\) from that paper already supplies a sufficient condition corresponding to one branch of (1). Their paper and Peltomäki's 2016 dissertation do not state the full three-one classification, the weight-refined all-length generating function, or the partition bijection (2) in the inspected sections.

The entries OEIS A231208 and A235609 provide unrestricted length counts and lists of individual privileged words, respectively; those are not asserted new. Nicholson–Rampersad (2015) develops unrestricted counting bounds, not fixed-weight-three exact enumeration. The contribution claimed here is specifically the **complete gap criterion and exact count of nonpalindromic privileged words of weight three**, not the recursive definition, the recognition algorithm, or the first known example.

## Limitations
The classification says nothing about four or more occurrences of \(1\), nor about enumeration over arbitrary alphabets. The novelty comparison covers the inspected primary sources, indexed sequence entries, accessible historical claims, and the recorded related-index search; unindexed equivalent statements or a buried exercise may exist. The Peltomäki 2016 dissertation was inspected in accessible extracted sections, but image retrieval of its PDF returned an access error. No independent mathematical validation was performed.

## References
1. J. Peltomäki, *Introducing Privileged Words: Privileged Complexity of Sturmian Words*, arXiv:1210.3146v1 (first public 2012-10-11), https://arxiv.org/html/1210.3146v2 .
2. M. Forsyth, A. Jayakumar, J. Shallit, *Remarks on Privileged Words*, arXiv:1311.7403v1 (first public 2013-11-28), https://arxiv.org/abs/1311.7403 .
3. J. Peltomäki, *Privileged Words and Sturmian Words*, TUCS Dissertation 214 (2016), https://www.utupub.fi/items/3f47c1ce-a43c-4569-8fb7-9211bcd4e5c9 .
4. J. Nicholson, N. Rampersad, *Improved Estimates for the Number of Privileged Words*, arXiv:1506.07847v1 (2015-06-25), https://arxiv.org/abs/1506.07847 .
5. OEIS A231208, *Number of binary privileged words of length n*, https://oeis.org/A231208 ; OEIS A235609, *List of privileged words over the alphabet {1,2}*, https://oeis.org/A235609 .
