# Exact all-length factor-frequency spectra of generalized period-doubling words

## Finding

For each integer \(q\ge 2\), consider the infinite word \(u^{(q)}\) on \(\{0,\ldots,q-1\}\) defined by \(u^{(q)}_i=\nu_2(i+1)\bmod q\) for \(i\ge0\). For a finite factor \(w\), write \(\operatorname{freq}(w)\) for the limiting proportion of starting positions at which \(w\) occurs. This limit exists. The following formulas determine *the multiplicity of every distinct factor frequency at every length*, not merely the number of factors.

Let \(F_{q,n}(\lambda)\) be the number of **distinct** factors \(w\) of length \(n\) satisfying \(\operatorname{freq}(w)=\lambda\). Only the displayed positive multiplicities occur.

For \(n=1\), the frequencies are \(2^j/(2^q-1)\), one factor at each level \(j=0,1,\ldots,q-1\).

For \(n=2\), three factors have frequency \(2/[2(2^q-1)]\), and for each \(j=2,\ldots,q-1\), two factors have frequency \(2^j/[2(2^q-1)]\).

For every \(n\ge3\), put
\[
L=2^{\lceil\log_2 n\rceil},\qquad M=L/4,\qquad
a=\max\{0,3M-n\},\quad c=\max\{0,n-3M\},\quad b=M-a-c,
\]
and put \(\lambda_j=2^j/[L(2^q-1)]\). For \(q=2\),
\[
F_{2,n}(\lambda_1)=4b+6c,\qquad
F_{2,n}(\lambda_2)=3a+b.
\]
For \(q\ge3\),
\[
\begin{aligned}
F_{q,n}(\lambda_1)&=4b+6c,\\
F_{q,n}(\lambda_2)&=3a+3b+4c,\\
F_{q,n}(\lambda_j)&=2a+3b+4c &&(3\le j\le q-1),\\
F_{q,n}(\lambda_q)&=2a+b.
\end{aligned}
\]
Empty index ranges and zero multiplicities are omitted. All other frequencies have multiplicity zero. In particular, for binary period doubling, every factor at a length \(n\ge2\) has the same frequency if and only if \(n\) is a power of two; at \(n=2^k\), all \(3\cdot2^{k-1}\) factors have frequency \(2/[3\cdot 2^k]\).

## Assumptions and scope

Here \(\nu_2(t)\) is the largest exponent \(e\ge0\) such that \(2^e\) divides the positive integer \(t\). A length-\(n\) factor is the contiguous word \(u^{(q)}_su^{(q)}_{s+1}\cdots u^{(q)}_{s+n-1}\) for some \(s\ge0\); a factor is counted once even if it occurs at many positions. The frequency uses the limit of the proportion of starts in \(\{0,\ldots,N-1\}\), not the number of embeddings of a scattered subsequence. The formulas apply to every integer \(q\ge2\) and every integer \(n\ge1\), with no truncation of the infinite word.

## Proof

**1. Complete phase representation and weights.** Fix \(n\ge1\), and let \(L=2^k\) be the smallest power of two at least \(n\). Each starting position determines exactly one offset \(j\) modulo \(L\) at which the corresponding positive integer is divisible by \(L\); the length-\(n\) interval contains *at most* one such multiple. For a starting position \(s\), set \(j\in\{0,\ldots,L-1\}\) by the condition \(s+j+1\equiv0\pmod L\). If \(j<n\), the letter at offset \(j\) is \(\nu_2(s+j+1)\bmod q\); for any other offset \(i\), the inequality \(0<|i-j|<L\) gives
\[
\nu_2(s+i+1)=\nu_2(|i-j|).
\]
If \(j\ge n\), every letter is thus fixed by the residue class \(j\). Otherwise there is exactly one variable center letter. All \(L\) phases occur with asymptotic density \(1/L\). Conditional on the phase, \((s+j+1)/L\) varies through positive integers; the probability that its two-adic valuation is \(e\) equals \(2^{-e-1}\). Consequently, a specified center letter has probability among \(2^0/(2^q-1),\ldots,2^{q-1}/(2^q-1)\), assigned cyclically according to \(k\bmod q\). The missing-center case has total integer mass \(D=2^q-1\) when all frequencies are multiplied by \(LD\). This proves existence and rationality of all limiting frequencies and defines an exhaustive finite weighted template model.

**2. Distinct center residues cannot collide.** Now \(n\ge3\), so \(L\ge4\) and \(n>L/2\). Consider two different potential centers \(j<j'\) and let \(t=\nu_2(j'-j)\). If \(t\le k-3\), select an offset \(i\in\{0,\ldots,n-1\}\) with \(i\equiv j+2^{t+1}\pmod{2^{t+2}}\). Such an offset exists because \(n>L/2\ge2^{t+2}\). It differs from both centers and has \(\nu_2(|i-j|)=t+1\) and \(\nu_2(|i-j'|)=t\). These letters differ modulo every \(q\ge2\), regardless of center values. Thus colliding templates can have centers only in the same residue class modulo \(M=L/4\); all comparisons reduce to the disjoint quartets \(r,r+M,r+2M,r+3M\), where \(0\le r<M\).

**3. Exact quartet collision census.** Fix a quartet. Define \(A=(k-2)\bmod q\) and \(B=(k-1)\bmod q\); they are distinct. Outside these four center offsets, the four templates agree: subtracting a multiple of \(M\) preserves the valuation of a nonmultiple of \(M\). At the four offsets, with the symbol \(*\) at the variable center, their signatures are exactly
\[
(*,A,B,A),\qquad (A,*,A,B),\qquad (B,A,*,A),\qquad (A,B,A,*).
\]
Truncate these signatures to the first \(h\) offsets actually inside the length-\(n\) window. Because \(L/2<n\le L\), we have \(h\in\{2,3,4\}\). For a variable center, insert each of the \(q\) symbols, giving that symbol its phase weight from part 1; for a center beyond the window, assign weight \(D\) to the unchanged truncated signature. Identical signatures are combined by *adding* their weights. Direct comparison of these four displayed signatures gives the following complete mass table; a missing row means zero occurrences:

| Mass after multiplying by \(LD\) | \(h=2\), \(q\ge3\) | \(h=3\), \(q\ge3\) | \(h=4\), \(q\ge3\) |
| --- | ---: | ---: | ---: |
| \(2\) | \(0\) | \(4\) | \(6\) |
| \(4\) | \(3\) | \(3\) | \(4\) |
| \(2^j\), each \(3\le j\le q-1\) | \(2\) | \(3\) | \(4\) |
| \(2^q\) | \(2\) | \(1\) | \(0\) |

For \(q=2\), the mass table is instead: at \(h=2\), three words have mass \(4\); at \(h=3\), four words have mass \(2\) and one has mass \(4\); at \(h=4\), six words have mass \(2\). The difference is the forced identification of the two non-center letter types when there are only two alphabet symbols; it is not legitimate simply to substitute \(q=2\) into the first table. In each case the total mass over a quartet is exactly \(4D\), independently checking that all starts have been counted.

The number of quartets with exactly two centers in the window is \(a=\max\{0,3M-n\}\); the number with all four is \(c=\max\{0,n-3M\}\); and the other \(b=M-a-c\) have three. Summing their mass tables proves the displayed spectrum for every \(n\ge3\).

**4. Lengths one and two.** At length one, the valuation distribution is geometric modulo \(q\), giving one letter at each weight \(2^j/(2^q-1)\). At length two, the two phase classes each have one visible center and their only shared factor has combined mass \(2\). The remaining center-letter weights produce exactly three factors of mass \(2\) and two factors at each mass \(2^j\) for \(2\le j\le q-1\), where the common denominator is \(2D\). This also follows by comparing the explicit length-two templates \((c,0)\) and \((0,c)\).

**5. Binary equifrequent criterion.** At length two the three frequencies are equal. If \(n=2^k\) with \(k\ge2\), then \(a=b=0\), \(c=M\), so \(F_{2,n}(\lambda_1)=6M=3L/2\) and no other level occurs. Conversely, for any non-power-of-two \(n\ge3\), the two nonnegative multiplicities \(4b+6c\) and \(3a+b\) are both positive: in the regime \(n<3M\), \(a>0\) and \(b>0\); in the regime \(3M\le n<L\), \(b>0\) and \(c\ge0\). Thus there are two different frequencies.

## Verification

The standard-library program `check_exact.py` independently enumerates every phase template and sums its exact integer mass, then compares the resulting multiset with the stated formulas for every \(2\le q\le10\) and \(1\le n\le129\), 1,161 parameter pairs. The separate program `check_prefix.py` generates literal length-\(131072\) prefixes and independently compares their factor supports and empirical frequencies with the exact phase spectrum for \(2\le q\le6\), \(1\le n\le28\), 140 parameter pairs. Both programs were executed successfully; see their captured output files. Numerical frequencies from finite prefixes are approximations, not proofs of existence or of the all-length identity. The proof above supplies the infinite conclusion.

## Relationship to prior work

Bell, Burnett and Schulz (2026) give general bounds on the *number of distinct frequency levels* for words of linear factor complexity, not an exact level-by-level multiplicity formula for this substitution family. Bognini and Ammar (2025) study generalized period-doubling kernel and gap factorizations, not this all-length frequency spectrum. The closest indexed dyadic factor result enumerates the number of distinct length-\(2^k\) factors and exact collisions among unweighted phase templates, but does not enumerate factor frequencies or non-dyadic lengths; those established dyadic counts are not claimed as new. The known reflection-complexity result concerns binary reversal classes rather than the weighted occurrence-frequency question. Balková's generalized Thue–Morse frequency work treats a different substitution family. The new theorem supplies the precise weighted spectrum and the sharp three-regime transition at \(n=3L/4\).

## Limitations

The theorem concerns stationary contiguous-factor frequencies in the explicitly defined infinite family, not arbitrary automatic sequences or finite-window output frequencies. It does not claim a full classification of individual occurrence sets, and general frequency bounds and dyadic unweighted factor counts predate it. Novelty remains subject to unindexed earlier explicit frequency formulas. The provided computational checks are finite, and independent mathematical validation has not been performed.

## References

1. J. Bell, L. Burnett, C. Schulz, *Frequencies of subwords in words of linear subword complexity*, arXiv:2607.28273, first posted 2026-07-30, https://arxiv.org/abs/2607.28273.
2. K. E. Bognini, H. Ammar, *A new factorization of the generalized period-doubling sequences through kernel words and gaps sequences*, arXiv:2511.20881, first posted 2025-11-25, https://arxiv.org/abs/2511.20881.
3. *Exact dyadic factor and reflection complexity of cyclic period-doubling words*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-dyadic-factor-and-reflection-complexity-of-cyclic-period-d--c8d7b40c0705.
4. J.-P. Allouche et al., *The reflection complexity of sequences over finite alphabets*, arXiv:2406.09302, https://arxiv.org/abs/2406.09302.
5. L. Balková, *Factor frequencies in generalized Thue-Morse words*, arXiv:1107.5033, https://arxiv.org/abs/1107.5033.
