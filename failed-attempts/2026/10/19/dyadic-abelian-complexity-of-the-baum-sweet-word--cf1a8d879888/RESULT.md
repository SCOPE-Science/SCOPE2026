# Dyadic abelian complexity of the Baum–Sweet word

## Finding
Let \(b=b_0b_1b_2\cdots\) be the Baum–Sweet binary word, with \(b_0=1\) and, for \(j\ge1\), \(b_j=1\) if and only if every maximal run of zeros in the usual binary expansion of \(j\) has even length. Set \(F_0=0\), \(F_1=1\), and \(F_{t+2}=F_{t+1}+F_t\). For every integer \(m\ge0\), the maximum and minimum numbers of ones among length-\(2^m\) contiguous factors of \(b\) are respectively \(F_{m+2}\) and \(0\). Consequently the number \(\psi_b(2^m)\) of distinct Parikh vectors of such factors is
\[
\boxed{\psi_b(2^m)=F_{m+2}+1.}
\]
A stronger structural assertion underlies the maximum: for every \(m,q\ge0\) and \(0\le r<2^m\),
\[
b_{q2^m+r}\le b_r.
\]
Thus *each aligned dyadic block is coordinatewise dominated by the initial block of equal length*. This is a dyadic statement; it does not assert prefix normality at arbitrary lengths.

## Assumptions and scope
The usual finite binary expansion has no leading zeros. The zeroth symbol is the exceptional value \(1\). A factor is a contiguous substring indexed by any starting integer \(s\ge0\); its weight is its number of ones. Two binary factors of equal length have the same Parikh vector exactly when they have the same weight. All assertions apply to the infinite sequence, to all integers \(m\ge0\), without a finite-exponent cutoff.

## Proof
**Dyadic suffix dominance.** Fix \(m,q\ge0\) and \(0\le r<2^m\). If \(q=0\), the claim is equality. If \(r=0\), the claim holds because \(b_0=1\). Otherwise, the binary expansion of \(q2^m+r\) is the expansion of \(q\) followed by the exactly \(m\)-digit, zero-padded binary representation of \(r\). All zero runs occurring *after the first one of the unpadded expansion of* \(r\) are unaltered in this concatenation, including the terminal run. Therefore, if all zero runs of \(q2^m+r\) have even length, then all zero runs of \(r\) have even length. In indicator notation this is precisely \(b_{q2^m+r}\le b_r\). The possibility that padding joins a preceding run does not affect any run *after* the first significant one of \(r\).

**Maximal dyadic weight.** Put \(L=2^m\). Write an arbitrary starting position uniquely as \(s=qL+r\), with \(q\ge0\) and \(0\le r<L\). The length-\(L\) factor starting at \(s\) consists of offsets \(r,\ldots,L-1\) in block \(q\), followed by offsets \(0,\ldots,r-1\) in block \(q+1\). Applying the coordinatewise inequality separately to those two pieces gives
\[
\sum_{j=s}^{s+L-1}b_j\le
\sum_{i=r}^{L-1}b_i+\sum_{i=0}^{r-1}b_i
=\sum_{i=0}^{L-1}b_i.
\]
The initial length-\(L\) factor attains equality. Hence its weight is exactly the maximum over all factors of that length.

**Count of the initial block.** For a positive integer with exactly \(\ell\ge1\) binary digits, the first digit is \(1\). Its remaining \(\ell-1\) digits have even zero-run lengths if and only if they are uniquely tiled by the tokens `1` and `00`. There are \(F_\ell\) such tilings (the empty tiling for \(\ell=1\)); this is the standard length-one/length-two tiling recurrence. Thus among indices \(0\le j<2^m\), precisely
\[
1+\sum_{\ell=1}^{m}F_\ell=F_{m+2}
\]
have \(b_j=1\), where the initial \(1\) accounts for index zero.

**Minimum and all intermediate weights.** For any \(k\ge m\), every integer in \([5\cdot2^k,6\cdot2^k)\) begins in binary with `101`. That internal singleton zero run forces the corresponding Baum–Sweet symbols to be zero. The interval has length \(2^k\), at least \(L\), and therefore contains an all-zero length-\(L\) factor. When a length-\(L\) window shifts by one position, its weight changes by at most one. Moving from the initial window of weight \(F_{m+2}\) to an all-zero window therefore realizes *every* integer weight between these extremes. Since a binary Parikh vector at fixed length is determined by weight, there are exactly \(F_{m+2}+1\) distinct Parikh vectors. This completes the proof.

## Verification
The standalone `verify.py` independently generates \(2^{17}\) terms both from the binary-digit definition and from the four-state uniform morphism \(A\mapsto AB\), \(B\mapsto CB\), \(C\mapsto BD\), \(D\mapsto DD\), coded by \(A,B\mapsto1\) and \(C,D\mapsto0\). It checks equality of the generators; exhaustively scans every factor present in the generated prefix at dyadic lengths \(2^m\) for \(0\le m\le11\); checks the predicted extrema; and checks the coordinatewise block inequality over a finite sample of aligned blocks. The script prints `VERIFY_OK` if all checks pass. None of those finite checks replaces the universal proof above.

## Relationship to prior work
The Baum–Sweet sequence originates in the study of continued fractions of algebraic power series (Baum and Sweet, 1976), and its finite-automaton presentation is classical. Burcsi, Fici, Lipták, Ruskey and Sawada (2014) introduce computational methods and enumerative questions for prefix-normal words, while Parreau, Rigo, Rowland and Vandomme (2015) investigate higher abelian complexity of other automatic words. Cicalese, Lipták and Rossi (arXiv 2018, later published 2021) explain the general relation between maximum/minimum factor weights, prefix-normal forms and abelian complexity. The present result instead computes both extremal weights for the Baum–Sweet word at every dyadic length via a coordinatewise suffix-dominance lemma. The general framework alone does not yield the displayed Fibonacci specialization without that extra argument.

## Limitations
The result provides no exact formula for general, nondyadic factor lengths. It does not establish that every finite prefix of the Baum–Sweet word is prefix normal, and a finite verification cannot show an infinite statement. The bibliography comparison does not prove uniqueness of the result across unindexed literature.

## References
1. L. E. Baum and M. M. Sweet, *Continued fractions of algebraic power series in characteristic 2*, Annals of Mathematics 103 (1976), 593–610, DOI:10.2307/1970953.
2. P. Burcsi, G. Fici, Z. Lipták, F. Ruskey, J. Sawada, *Normal, Abby Normal, Prefix Normal*, arXiv:1404.2824, first submitted 2014-04-01.
3. A. Parreau, M. Rigo, E. Rowland, É. Vandomme, *A New Approach to the 2-Regularity of the ℓ-Abelian Complexity of 2-Automatic Sequences*, Electronic Journal of Combinatorics 22 (2015), P1.27, arXiv:1405.3532.
4. F. Cicalese, Z. Lipták, M. Rossi, *On Infinite Prefix Normal Words*, arXiv:1811.06273 (first submitted 2018; later journal version 2021).
