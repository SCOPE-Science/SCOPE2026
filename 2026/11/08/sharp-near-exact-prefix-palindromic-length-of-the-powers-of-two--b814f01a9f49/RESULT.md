# Sharp near-exact prefix palindromic length of the powers-of-two indicator word

## Finding

Let \(w=w_0w_1\cdots\) be the binary, \(2\)-automatic word with \(w_i=1\) exactly when \(i=2^j\) for some integer \(j\ge 0\), and \(w_i=0\) otherwise. Let \(P(n)\) be the minimum number of nonempty palindromes whose concatenation is the prefix \(w_0\cdots w_{n-1}\), with \(P(0)=0\). Set
\[
  k(n)=\#\{j\ge0:2^j<n\},\qquad h(n)=\left\lceil\frac{k(n)}2\right\rceil.
\]
For every integer \(n\ge0\), the following global two-value law holds:
\[
\boxed{h(n)\le P(n)\le h(n)+1.}
\]
For every integer \(r\ge2\), the upper endpoint is attained at the dyadic predecessor:
\[
\boxed{P(2^r-1)=\left\lceil\frac r2\right\rceil+1.}
\]
For every integer \(j\ge0\), the lower endpoint is attained at a constructive, unbounded sequence: put \(E_{-1}=0\) and
\[
 E_j=3\cdot4^j+1-E_{j-1}.
\]
Then \(P(E_j)=j+1=h(E_j)\). Consequently,
\[
 P(n)=\tfrac12\log_2n+O(1)\quad(n\to\infty),\qquad
 \lim_{n\to\infty}\frac{P(n)}{\log_2n}=\frac12.
\]
The bounds are uniform at every length, not estimates from finite experiments. The precise value at arbitrary non-extremal lengths may require further information.

## Assumptions and scope

All positions are nonnegative integers, the indexing starts at zero, and a factor \(w[a:b)\) includes positions \(a,a+1,\ldots,b-1\). A palindrome is a nonempty word equal to its reversal. An empty factor is never counted as a palindromic piece. Every finite binary word admits such a factorization by single letters. The number of nonzero symbols in \(w[0:n)\) is \(k(n)\). The characteristic word is \(2\)-automatic because its language of base-\(2\) indices carrying symbol \(1\) is \(10^*\), with leading zeros handled in the usual way. No assumption of a finite-palindrome language is made.

## Proof

**1. No palindrome contains three ones.** The positions of the ones of \(w\) are exactly the distinct powers \(2^j\). A palindromic factor reflects these positions around its center. If it contained an odd number at least three, its first, middle and last one positions would form a three-term arithmetic progression of distinct powers of two. This is impossible: \(2^a+2^c=2^{b+1}\) for \(a<b<c\) would give an odd sum after dividing by \(2^a\), while the right side is even. If it contained an even number at least four, its two outer symmetric pairs would give two distinct unordered pairs of powers of two with the same sum. That is impossible because the binary expansion of the sum of two distinct powers of two uniquely determines the pair. Thus each palindrome contains at most two ones, proving \(P(n)\ge\lceil k(n)/2\rceil\).

**2. Canonical paired palindromes.** Set \(E_{-1}=0\), \(E_j=3\cdot4^j+1-E_{j-1}\). We prove that \(w[E_{j-1}:E_j)\) is a palindrome with exactly two ones, at \(4^j\) and \(2\cdot4^j\). At \(j=0\), this is \(w[0:4)=0110\). At \(j=1\), \(E_0=4\) and \(E_1=9\), and \(w[4:9)=10001\). For \(j\ge1\), induction gives
\[
 2\cdot4^j<E_j<3\cdot4^j.
\]
Indeed the case \(j=1\) is direct. If it holds for \(j\), then \(E_{j+1}=3\cdot4^{j+1}+1-E_j\) lies strictly between \(2\cdot4^{j+1}\) and \(3\cdot4^{j+1}\). For \(j\ge2\), the preceding endpoint lies strictly between \(4^j/2\) and \(4^j\); for \(j=1\), it equals \(4^j\). Thus the factor starts after the preceding power of two, contains \(4^j\) and \(2\cdot4^j\), and ends before \(4^{j+1}\). Its endpoint sum equals the sum of these two one positions:
\[
 E_{j-1}+E_j-1=3\cdot4^j=4^j+2\cdot4^j.
\]
Reflection therefore interchanges its two ones and matches zeros everywhere else. The factors concatenate without gaps. After \(m\) such pieces, the prefix ends at \(E_{m-1}\), has exactly \(2m\) ones and satisfies \(P(E_{m-1})=m\) by the lower bound. Hence \(P(E_j)=j+1=h(E_j)\).

**3. All-length upper bound.** The cases \(n=0\) and \(n=1\) are immediate, so assume \(k=k(n)\ge1\). Write \(s=E_{-1}=0\) when no paired piece has been used.

If \(k=2m\) is even, with \(m\ge1\), first use the \(m-1\) canonical paired palindromes for the first \(2m-2\) ones. Their endpoint is \(s=E_{m-2}\) for \(m\ge2\), and \(s=0\) for \(m=1\). The last two ones are at \(a=4^{m-1}\) and \(2a\), and \(2a<n\le4a\). Put \(H=3a-s+1\). If \(n\ge H\), the factor \(w[s:H)\) is a palindrome centered between these two ones, while \(w[H:n)\) (if nonempty) consists only of zeros. If \(n<H\), put \(t=3a-n+1\); then \(s<t\le a\), \(w[s:t)\) consists only of zeros and \(w[t:n)\) is the palindrome reflecting the two ones. When \(m\ge2\), the inequality \(s>a/2\) excludes any earlier one from these factors; when \(m=1\), the only preceding position is zero. Thus at most \((m-1)+2=m+1\) palindromes suffice.

If \(k=2m+1\) is odd, first use the \(m\) canonical paired pieces ending at \(s=E_{m-1}\) (or \(s=0\) if \(m=0\)). The last one is at \(a=4^m\), and \(a<n\le2a\). Put \(H=2a-s+1\). If \(n\ge H\), use the one-centered palindrome \(w[s:H)\), followed by the all-zero \(w[H:n)\) if nonempty. If \(n<H\), put \(t=2a-n+1\) and use \(w[s:t)\) (an all-zero prefix if nonempty) followed by the palindrome \(w[t:n)\) centered on the single one at \(a\). For \(m\ge1\), \(s>a/2\) excludes earlier ones. The total number of pieces is at most \(m+2=h(n)+1\). Zero-length pieces are omitted in both cases. This proves the global upper bound.

**4. Sharpness at dyadic predecessors.** Fix \(r\ge3\), let \(b=2^{r-1}\) and \(q=2b-2\), so \(q\) is the last index of \(w[0:2^r-1)\) and \(b\) its last one position. Suppose a palindrome \(w[s:q+1)\) ending at \(q\) contains the last one, i.e. \(s\le b\). The reflection of \(b\) is \(s+b-2\). If \(3\le s\le b\), this lies strictly between \(b\) and \(2b\), where there are no powers of two. If \(s=1\), the reflected point is \(b-1\), not a power of two for \(b\ge4\). If \(s=2\), the one at \(b/2\) must be reflected to \(3b/2\), not a power of two. If \(s=0\), reflection of \(b\) yields \(b-2\), not a power of two unless \(b=4\); for \(b=4\), reflection of the one at position \(1\) yields \(5\), which is not a one. Thus the final palindrome cannot contain any one: it must be a nonempty all-zero suffix. Every earlier palindrome contains at most two of the \(r\) ones, so at least \(\lceil r/2\rceil\) earlier palindromes are necessary, in addition to this final one. The global upper bound gives equality. At \(r=2\), the prefix \(w[0:3)=011\) has \(P(3)=2\), also the claimed value.

**5. Asymptotics.** For \(n\ge2\), \(k(n)=1+\lfloor\log_2(n-1)\rfloor\). Combining this identity with the global bounds yields \(P(n)=\frac12\log_2 n+O(1)\) and the asserted limit.

## Verification

Run `python3 verify.py` using Python 3 with no external dependencies. The independent center-expansion dynamic program computes exact prefix palindromic lengths through \(n=4096\); a second interval-based palindrome dynamic program checks \(n\le256\). The code reconstructs the proof's explicit factorizations at all tested lengths, verifies adjacency, palindrome validity and piece count, checks dyadic sharpness through exponent \(11\), and validates seven canonical paired blocks. The successful output is `VERIFY_OK prefixes= 4096 independent= 256 dyadic_scales= 10 claims_checked= 4113`. This is a finite check only; steps 1–5 above establish the infinite statement.

## Relationship to prior work

Frid, Laborde and Peltomäki study prefix palindromic length in automatic words, including other classical automatic words and structural regularity questions [1]. Li studies the ruler and period-doubling sequences [2]. Bulgakova, Frid and Scanvic study the ternary-base Sierpiński word [3]. The present word is the characteristic function of positions that are powers of two and is different from each of those sequences; its all-prefix one-unit bounds, sharp dyadic predecessor values and explicit optimal paired palindrome endpoints are not statements supplied by those papers. Earlier general work on unbounded palindromic length [4] motivates the invariant but does not supply this profile. A separately indexed result on string attractors of a shifted powers-of-two word concerns a distinct invariant, and its exact attractor counts do not imply palindromic factorization lengths.

## Limitations

The theorem gives the exact answer at two infinite families and a one-unit interval everywhere, but does not classify which of the two adjacent values occurs at each remaining prefix length. There is no independent scientific audit or formal proof-assistant certification. An equivalent result absent from searched bibliographic indexes remains possible.

## References

[1] A. E. Frid, E. Laborde and J. Peltomäki, *On prefix palindromic length of automatic words*, arXiv:2009.02934 (first public September 7, 2020), https://arxiv.org/abs/2009.02934.

[2] S. Li, *Palindromic length sequence of the ruler sequence and of the period-doubling sequence*, arXiv:2007.08317 (2020), https://arxiv.org/abs/2007.08317.

[3] Y. Bulgakova, A. E. Frid and E. Scanvic, *Prefix palindromic length of the Sierpinski word*, arXiv:2201.09556 (2022), https://arxiv.org/abs/2201.09556.

[4] A. E. Frid, S. Puzynina and L. Q. Zamboni, *On minimal factorizations of words as products of palindromes*, arXiv:1210.6179 (2012), https://arxiv.org/abs/1210.6179.
