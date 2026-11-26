# Shortest absent subsequences of period-doubling iterates

## Finding
Let \(\varphi(0)=01\), \(\varphi(1)=00\), and \(P_m=\varphi^m(0)\). For every integer \(m\geq 2\), put \(K_m=(2^m-(-1)^m)/3\). The shortest binary words absent as **scattered subsequences** of \(P_m\) have length exactly \(K_m+1\). If \(m\) is even, the entire set is
\[
\{1^{K_m+1}\}.
\]
If \(m\) is odd, the entire set is
\[
\{1^{K_m+1},\;1^{K_m}0,\;1^{K_m-1}00\}.
\]
Thus the number of shortest absent subsequences alternates exactly between one and three, although their lengths grow exponentially.

## Assumptions and scope
A binary word \(u=u_1\cdots u_t\) is a scattered subsequence of \(w\) when indices \(1\le i_1<\cdots<i_t\le |w|\) satisfy \(u_j=w_{i_j}\). Its *shortest absent subsequences* are all absent binary words of the smallest possible length. Both alphabet symbols are permitted. The theorem concerns the finite morphic prefixes \(P_m\), not arbitrary factors or infinite-word forbidden factors. The cases \(m=0,1\) are excluded.

## Proof
**One counts and structure.** Each substituted letter contributes exactly one zero, and contributes one one exactly when it was zero. If \(K_m\) counts ones, then \(K_0=0\) and \(K_{m+1}=2^m-K_m\). Consequently \(K_m=(2^m-(-1)^m)/3\). Every one in \(P_m\) is the second letter of an \(01\) image, and these images are disjoint. In particular there are no consecutive ones; taking the two characters of each image containing a one embeds \((01)^{K_m}\) as a scattered subsequence. Since every binary word of length \(K_m\) embeds into \((01)^{K_m}\) (select zero or one from each block), all binary words of length \(K_m\) occur. The word \(1^{K_m+1}\) is absent; hence the shortest absent length is precisely \(K_m+1\).

**Eliminating words with an \(01\) factor.** Any length-\(K_m+1\) word containing the adjacent pair \(01\) embeds into \((01)^{K_m}\): designate any one adjacent \(01\) pair to use both positions of one block and place its remaining \(K_m-1\) letters, in order, in the remaining blocks, selecting either the zero or the one in each. Thus a shortest absent word must avoid adjacent \(01\), equivalently it has the form \(1^r0^{K_m+1-r}\) for some \(0\le r\le K_m+1\).

**Zero/one extremes.** The all-one word is absent. The all-zero word occurs because the number \(Z_m=2^m-K_m\) of zeros satisfies \(Z_m\ge K_m+1\) for every \(m\ge2\).

**Intermediate counts.** Number the ones from left to right. For \(1\le r\le K_m\), the candidate \(1^r0^{K_m+1-r}\) is a subsequence if and only if there are at least \(K_m+1-r\) zeros after the \(r\)-th one: choosing the earliest \(r\) ones maximizes the number of following zeros. Because consecutive ones are separated by at least one zero, there are always at least \(K_m-r\) zeros after the \(r\)-th one. One additional zero suffices for occurrence.

**Parity-specific suffixes.** From \(P_2=0100\) and \(P_3=01000101\), and the two-step substitution identities \(\varphi^2(0)=0100\), \(\varphi^2(1)=0101\), it follows inductively that every even \(P_m\) with \(m\ge2\) ends in \(00\), while every odd \(P_m\) with \(m\ge3\) ends in \(1000101\). The induction for odd \(m\) uses the fact that the previous odd iterate ends in \(01\), whose two-step image is \(01000101\); the even case similarly uses the final \(00\).

For even \(m\), at least one zero trails the last one; hence every intermediate candidate occurs. For odd \(m\), no zero trails the last one, and exactly one zero separates the last two ones. Consequently the candidates at \(r=K_m\) and \(r=K_m-1\) are absent. The suffix \(1000101\) also exhibits three zeros between the third-from-last one and the second-from-last one. For every \(1\le r\le K_m-2\), that gap adds at least two zeros beyond the mandatory one-zero gaps, ensuring the needed extra zero and hence occurrence. This gives precisely the stated three words. All cases are exhausted. \(\square\)

## Verification
The standalone standard-library program `verify.py` independently constructs iterates for \(2\le m\le13\), counts absent subsequences by dynamic programming on the next-position automaton, and checks the claimed length and count. At small lengths it additionally enumerates all candidate absent words directly. Its output ends in `VERIFY_OK`. These finite checks supplement, but do not replace, the proof for all \(m\).

## Relationship to prior work
Classical work on the period-doubling word studies its factor and arithmetic-progression complexity; that does not count missing scattered subsequences of its finite iterates. General shortest-absent-subsequence theory supplies arch factorizations, structural characterizations, and algorithms for arbitrary strings, but the specific alternating one-versus-three classification of this morphic family is not among the inspected results. An analogous general upper bound or algorithm must not be mistaken for this explicit family-level statement.

## Limitations
The result classifies **shortest** absent subsequences only: it gives neither all longer missing subsequences nor minimal absent subsequences of nonminimum lengths. No claim is made about arbitrary substrings of the infinite period-doubling word. Priority relative to inaccessible or unindexed earlier literature remains subject to independent investigation.

## References
1. S. V. Avgustinovich, J. Cassaigne, and A. E. Frid, “Sequences of low arithmetical complexity,” *RAIRO Theoretical Informatics and Applications* 40 (2006), 569–582, doi:10.1051/ita:2006041 (first verified online availability 2006-11-08).
2. J. D. Currie, N. Rampersad, K. Saari, and L. Q. Zamboni, “Extremal words in morphic subshifts,” arXiv:1301.4972 (first version 2013-01-21), a source on the period-doubling morphic subshift.
3. M. Kosche, T. Koß, F. Manea, and S. Siemer, “Absent Subsequences in Words,” arXiv:2108.13968 (first version 2021-08-31), subsequently *Fundamenta Informaticae* (2023).
