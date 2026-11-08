# Exact first two palindromic-gap excursions of stretched Thue–Morse words

## Finding
Let \(\mathbf t=\mu^\omega(0)\) be the Thue–Morse word, where \(\mu(0)=01\) and \(\mu(1)=10\). For an arbitrary integer \(M\ge1\), define the nonerasing morphism \(h_M(0)=a\), \(h_M(1)=a^M b\), and the infinite binary word \(\mathbf u_M=h_M(\mathbf t)\). Let \(p_M(n)\) be the number of its distinct length-\(n\) factors and \(P_M(n)\) the number of palindromic such factors, with \(p_M(0)=P_M(0)=1\). Write
\[
T_M(n)=p_M(n+1)-p_M(n)+2-P_M(n)-P_M(n+1).
\]
For every integer \(M\ge1\) and every integer \(0\le n\le5M+9\),
\[
\boxed{T_M(n)=\begin{cases}
0,&0\le n\le2M+2,\\
2,&2M+3\le n\le4M+6,\\
0,&4M+7\le n\le5M+8,\\
2,&n=5M+9.
\end{cases}}
\]
Thus the initial positive-gap block lasts exactly \(2M+4\) lengths. The following zero-gap block has length \(M+2\), and a new positive gap occurs immediately after it. The value at the first positive length was previously known; the interval structure and return boundary are the new assertion.

## Assumptions and scope
All factors are contiguous and counted as *distinct words*, not occurrences. Length zero means the empty factor. The parameter \(M\) is an arbitrary positive integer. The word \(\mathbf t\) is the standard one-sided Thue–Morse fixed point, and \(\mathbf u_M\) is its indicated nonuniform morphic image. No conclusion about later values \(n>5M+9\) is asserted.

## Proof
**Finite gap catalogue.** Each \(1\) in \(\mathbf t\) corresponds to a unique \(b\) in \(\mathbf u_M\). Let \(r_i\) be the number of zeros between consecutive ones in \(\mathbf t\); its values lie in \(\{0,1,2\}\). The distance between the corresponding consecutive \(b\)'s in \(\mathbf u_M\) is \(M+1+r_i\). To recover all possible contexts of up to six consecutive \(b\)'s, form the four finite blocks
\[
\mu^5(x)\mu^5(y),\qquad (x,y)\in\{00,01,10,11\}.
\]
Every pair \(xy\) occurs in \(\mathbf t\), and every factor of \(\mathbf t\) of length at most \(32\) lies in one of these four blocks: a factor of length at most one 32-block spans at most two adjacent blocks. The gap-context word from the preceding \(1\) through the following \(1\) around at most six displayed \(b\)'s has length at most \(3\cdot7+1=22\), so these four blocks give the *complete*, not sampled, catalogue. Let \(\mathcal C_k(u)\) be the set of pairs \((r_0,r_k)\) flanking an internal gap tuple \(u=(r_1,\ldots,r_{k-1})\) for \(k\) consecutive \(b\)'s. The catalogue has respectively \(1,3,6,10,12,16\) distinct internal tuples for \(k=1,2,3,4,5,6\), with \(6,10,12,16,20,22\) flank pairs. Its five-gap tuples have minimum sum \(4\). Consequently no length at most \(5M+9\) factor contains six \(b\)'s, since six \(b\)'s require at least \(5(M+1)+4+1=5M+10\) positions. Seven \(b\)'s are impossible even at length \(5M+10\): the six gaps have sum at least \(3\) (successive gap values are unequal), forcing length at least \(6(M+1)+3+1=6M+10>5M+10\). Thus \(k\le5\) suffices through \(5M+9\), and \(k\le6\) through \(5M+10\).

**Exact context count.** Fix \(k\ge1\), an internal gap tuple \(u\) with sum \(s\), and length \(n\). A factor containing exactly those \(k\) letters \(b\) has a unique representation
\[
a^L b a^{M+r_1}b\cdots b a^R,
\qquad L+R=d:=n-1-(k-1)(M+1)-s.
\]
It exists precisely when \(L,R\ge0\) and for some \((r_0,r_k)\in\mathcal C_k(u)\), \(L\le M+r_0\) and \(R\le M+r_k\). The separate no-\(b\) factor \(a^n\) exists exactly when \(1\le n\le M+2\). For one chosen endpoint pair \((a,b)\), the number of allowed nonnegative pairs \(L+R=d\) is
\[
H_{a,b}(M,d)=(d+1)_+-(d-M-a)_+-(d-M-b)_++(d-2M-a-b-1)_+,
\]
where \((x)_+=\max\{x,0\}\). The union over allowed endpoint pairs is counted by ordinary inclusion–exclusion. For a nonempty chosen subset \(E\subseteq\mathcal C_k(u)\), its intersection is \(H_{a_E,b_E}\) with \(a_E=\min_{(a,b)\in E}a\) and \(b_E=\min_{(a,b)\in E}b\), and sign \((-1)^{|E|+1}\). All factors have a unique internal tuple and left padding, so adding these exact counts gives \(p_M(n)\), with no overcounting.

**Factor growth.** Taking the difference at \(n+1\) and \(n\) turns each \(H_{a,b}\) into four integer threshold indicators. The complete signed threshold coefficients from \(k=1,\ldots,5\), represented by the pair \((\alpha,\beta)\) for \(\mathbf1_{n\ge\alpha(M+1)+\beta}\), are

| \((\alpha,\beta)\) | Coefficient |
|---|---:|
| \((0,0)\), \((1,0)\), \((1,1)\) | \(+1\) each |
| \((1,2)\) | \(-1\) |
| \((2,1)\), \((2,2)\) | \(+2,-1\) |
| \((3,1)\), \((3,2)\) | \(-1,+2\) |
| \((4,3)\) | \(-2\) |
| \((5,4)\), \((5,5)\), \((5,6)\) | \(-2,-8,-4\) |
| \((6,6)\), \((6,7)\) | \(+8,+4\) |

These are finite signed integer sums, exactly reproduced by the standalone program. On \(2M+3\le n\le5M+8\), the last five thresholds are inactive, while the first four contribute a constant \(2\). Thus
\[
\Delta p_M(n)=2+2\mathbf1_{n\ge2M+3}-\mathbf1_{n\ge2M+4}-\mathbf1_{n\ge3M+4}+2\mathbf1_{n\ge3M+5}-2\mathbf1_{n\ge4M+7}.
\]
For \(1\le n\le M\), the same expression before range simplification gives \(\Delta p_M(n)=1\); for \(M+1\le n\le2M+2\), it gives \(2\), after accounting for the disappearance of the all-\(a\) factor at \(n=M+2\). At \(n=5M+9\), the first six-\(b\) factors enter at length \(5M+10\); including \(k=6\) changes the coefficient of the threshold \((5,4)\) from \(-2\) to \(+2\). Hence \(\Delta p_M(5M+9)=4\).

**Palindromic count.** The same factor with gap tuple \(u\) is a palindrome exactly when \(u\) reads the same forwards and backwards and \(L=R=d/2\). Put \(b_u=\max_{(a,b)\in\mathcal C_k(u)}\min(a,b)\). The factor is then present exactly when \(d\) is even and \(0\le d\le2(M+b_u)\). Up to five \(b\)'s the eight palindromic internal-tuple signatures \((k,s,b_u)\), with multiplicity one each, are
\[
(1,0,1),\ (2,0,2),\ (2,1,0),\ (2,2,1),\ (4,2,1),\ (4,2,2),\ (4,4,0),\ (4,4,1).
\]
The no-\(b\) palindrome \(a^n\) is added through \(n=M+2\). Each signature contributes whenever
\[
0\le n-1-(k-1)(M+1)-s\le2(M+b_u)
\]
and that middle quantity is even. Directly pairing adjacent lengths in these eight parity-restricted intervals gives the following *entire* range table; the first row also covers \(n=0\) by direct inspection:

| Length range | \(\Delta p_M(n)\) | \(P_M(n)+P_M(n+1)\) | \(T_M(n)\) |
|---|---:|---:|---:|
| \(0\le n\le M\) | 1 | 3 | 0 |
| \(M+1\le n\le2M+2\) | 2 | 4 | 0 |
| \(n=2M+3\) | 4 | 4 | 2 |
| \(2M+4\le n\le3M+3\) | 3 | 3 | 2 |
| \(n=3M+4\) | 2 | 2 | 2 |
| \(3M+5\le n\le4M+6\) | 4 | 4 | 2 |
| \(4M+7\le n\le5M+8\) | 2 | 4 | 0 |
| \(n=5M+9\) | 4 | 4 | 2 |

For the last row, two palindrome signatures with six \(b\)'s, \((6,4,1)\) and \((6,4,2)\), first enter at length \(5M+10\), replacing the two four-\(b\) palindromes that expire; the adjacent palindrome sum stays \(4\). The table and the definition of \(T_M\) prove the claim for every \(M\ge1\). \(\square\)

## Verification
The standalone file `stretched_tm_gap_verify.py` generates the complete context catalogue from the four length-\(64\) superblock pairs, derives the signed threshold coefficients by exact integer inclusion–exclusion, and reconstructs the eight palindrome signatures. It also constructs an independent long Thue–Morse prefix and counts *distinct* factors and their palindromes directly for \(M=1,\ldots,9\), covering all declared lengths, including both boundary transitions. Further arithmetic checks use parameters \(M=20,51,100,1000\). The symbolic reduction and interval-parity argument, not the finite direct tests, prove the infinite statement. Run `python3 stretched_tm_gap_verify.py`; expected terminal line begins with `STRETCHED_TM_GAP_VERIFY_OK`.

## Relationship to prior work
Kim and Kwon (arXiv:2609.16596v1, September 15, 2026), Section 4, introduced exactly this family in their sharpness argument and proved \(T_M(2M+3)=2\) through exact counts at one critical length. Their general low-complexity theorem and sharpness construction do not state the lengths of the subsequent positive interval, the intervening zero interval, or the next return; these require the fuller finite gap-context calculation above. The initial value is explicitly not claimed as new. Earlier Thue–Morse palindromic-complexity studies, including Frougny–Klouda (2013), concern different morphic images or the unmodified word, not the displayed stretched-image interval spectrum. This is a best-knowledge literature comparison, not a definitive global priority guarantee.

## Limitations
Only the local gap through length \(5M+9\) is determined; no complete all-length factor or palindrome complexity is claimed. The result depends on the particular stretching morphism and binary Thue–Morse source. The finite checker supports the exact derivation but is not an independent audit of the proof, and further related literature may exist outside the checked sources.

## References
1. D. H. Kim and S. Kwon, *On the number of palindromic factors of low complexity words*, arXiv:2609.16596v1, first posted 2026-09-15, Sections 2–4, especially Proposition 4.3, https://arxiv.org/abs/2609.16596.
2. C. Frougny and K. Klouda, *Factor and palindromic complexity of Thue–Morse's avatars*, Acta Polytechnica 53 (2013), 868–871, https://doi.org/10.14311/AP.2013.53.0868.
3. P. Baláži, Z. Masáková and E. Pelantová, *Factor versus palindromic complexity of uniformly recurrent infinite words*, Theoretical Computer Science 380 (2007), 266–275. (General inequality; not used for the enumeration.)
