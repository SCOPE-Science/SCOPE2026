# Sharp quartic-shell extrema of the Newman rarefied Thue–Morse sum

## Finding
Let \(s_2(t)\) be the number of ones in the binary expansion of an integer \(t\ge0\), put \(\tau(t)=(-1)^{s_2(t)}\), and define the Newman rarefied sum \(F(N)=\sum_{0\le j<N}\tau(3j)\) for \(N\ge0\). For each integer \(k\ge1\),
\[
\min_{4^k\le N<4^{k+1}}F(N)=4\cdot3^{k-1},\qquad
\max_{4^k\le N<4^{k+1}}F(N)=4\cdot3^k.
\]
The minimum is attained only at \(N=4^k\), and the next possible value, \(4\cdot3^{k-1}+1\), is attained only at \(N=4^k+1\). The maximum is attained at the explicit integer
\[
N_k=\frac{10\cdot4^k+2}{3},
\]
with base-four expansion consisting of a leading 3, then \(k-1\) digits 1, then a final 2. Other maxima may occur; no complete classification of maxima is claimed.

## Assumptions and scope
Indices \(N,k,m\) are integers; \(k\ge1\), \(N\ge0\), and the shells include their left endpoint but exclude their right endpoint. The binary digit sum of zero is zero. There is no limiting process in the asserted equalities.

## Proof
**A four-block recurrence.** Write \(a=\tau(3m)\), \(b=\tau(3m+1)\), and \(S(m)=\sum_{0\le u<3m}\tau(u)\). Cancellation of the pairs \(\tau(2u)+\tau(2u+1)=0\) gives
\[
S(m)=\begin{cases}0,&m\text{ even},\\\tau((3m-1)/2),&m\text{ odd}.
\end{cases}
\]
The identities \(\tau(4x)=\tau(x)\), \(\tau(4x+1)=-\tau(x)\), \(\tau(4x+2)=-\tau(x)\), \(\tau(4x+3)=\tau(x)\) imply
\[
F(4m)=3F(m)-S(m),
\]
and, for \(r=0,1,2,3\),
\[
F(4m+r)=3F(m)+\delta_r(m),\quad
(\delta_0,\delta_1,\delta_2,\delta_3)=(-S,-S+a,-S+2a,-S+2a-b).
\]
Indeed, the four summands indexed by \(4j,4j+1,4j+2,4j+3\) in \(F(4m)\) are respectively \(\tau(3j),\tau(3j),-\tau(3j+1),-\tau(3j+2)\), so their total is \(3\tau(3j)-[\tau(3j)+\tau(3j+1)+\tau(3j+2)]\). If \(m\) is even, \(b=-a\) and
\[
(\delta_0,\delta_1,\delta_2,\delta_3)=(0,a,2a,3a).
\]
If \(m\) is odd, \(a=-S\), so
\[
(\delta_0,\delta_1,\delta_2,\delta_3)=(-S,-2S,-3S,-3S-b).
\]
In particular \(-4\le\delta_r(m)\le4\) for all \(m,r\), and \(F(m)\equiv m\pmod2\).

**Simultaneous induction for the two smallest values and the maximum.** For \(k=1\), direct summation on the twelve indices \(4\le N<16\) establishes minimum 4 only at 4, next value 5 only at 5, and maximum 12 at 14. Suppose the assertions, including uniqueness of the first two levels, hold on \(4^k\le m<4^{k+1}\). Put \(L=4\cdot3^{k-1}\), \(U=4\cdot3^k\), and \(A=4^k\). On the next shell \(4^{k+1}\le N<4^{k+2}\), write uniquely \(N=4m+r\) with \(A\le m<4A\) and \(0\le r\le3\).

For \(m\notin\{A,A+1\}\), the inductive uniqueness assertions give \(F(m)\ge L+2\), hence \(F(4m+r)\ge3L+2\). For \(m=A\), which is even, \(a=\tau(3A)=+1\), giving four values \(3L,3L+1,3L+2,3L+3\). For \(m=A+1\), which is odd, \(a=\tau(3A+3)=+1\) and \(S=-1\); the four corrections are \(1,2,3,3-b\), with \(3-b\ge2\). Its four values are therefore at least \(3(L+1)+1=3L+4\). Thus the next shell has minimum \(3L\) uniquely at \(4A\), and value \(3L+1\) uniquely at \(4A+1\).

For the upper bound, first note that the integer parity of \(F(m)\) equals that of \(m\). If \(F(m)\le U-2\), the correction bound gives \(F(4m+r)\le3U-2\). If \(F(m)=U\), then \(m\) is even; the next index \(m+1\) remains inside the induction shell, and maximality forces \(a=\tau(3m)=-1\). Hence the four corrections are \(0,-1,-2,-3\), all nonpositive. Finally, suppose \(F(m)=U-1\), so \(m\) is odd. If \(a=-1\), all four corrections are nonpositive. If \(a=+1\), they equal \(1,2,3,3-b\); the only possible correction exceeding 3 would be \(b=-1\). This last sign pair is impossible unless \(m\) is the final integer of its shell: put \(z=(3m-1)/2\). Since \(m\) is odd, \(\tau(z)=-a=-1\) and \(\tau(z+1)=b=-1\). Were \(z\) even, \(\tau(z+1)=-\tau(z)\); thus \(z\) is odd. Consequently \(z+1\) is even and \(\tau(z+2)=-\tau(z+1)=+1\). But \(3m+3=2(z+2)\), so \(\tau(3m+3)=+1\), giving \(F(m+1)=U\) and \(F(m+2)=U+1\), in contradiction with the induction hypothesis provided \(m+2<4A\). The only odd \(m\) in the induction shell not satisfying that restriction is \(m=4A-1\). In this case \(3m+1=3\cdot4A-2\) has base-four expansion of a leading digit 2, followed by \(k\) digits 3 and a final digit 2, and consequently \(\tau(3m+1)=+1\). Thus \(b=-1\) is also impossible at the endpoint. We have shown \(F(N)\le3U\) on the next shell.

**Attaining every maximum.** Set \(N_k=(10\cdot4^k+2)/3\), an integer since \(4^k\equiv1\pmod3\). Each \(N_k\) belongs to its asserted shell, since \(1<10/3+2/(3\cdot4^k)<4\). The case \(k=1\) has \(N_1=14\) and \(F(14)=12\). For every \(k\), \(N_k\) is even and the integer \(3(N_k-1)=10\cdot4^k-1\) has base-four expansion \(2,1\), followed by \(k\) digits 3. Its \(\tau\)-value equals \(({-1})({-1})(+1)^k=+1\), so \(F(N_k-1)=F(N_k)-1\). Also \(N_{k+1}=4(N_k-1)+2\). Taking odd \(m=N_k-1\) with \(a=+1\), the recurrence has \(S=-1\) and \(\delta_2=3\); hence
\[
F(N_{k+1})=3(F(N_k)-1)+3=3F(N_k).
\]
By induction \(F(N_k)=4\cdot3^k\), proving sharpness of the upper bound and completing the proof.

## Verification
The accompanying standalone Python program `verify.py` directly computes \(F(N)\) from bit counts, independently checks every four-block recurrence on \(0\le m<4^7\), and exhaustively tests both extrema and their specified locations for shells \(1\le k\le6\). The verification log is reproduced in `verify_output.txt`. These finite tests corroborate, but do not replace, the preceding induction proof.

## Relationship to prior work
Newman established the positivity phenomenon for the rarefied Thue–Morse sum, and Coquet subsequently gave an exact asymptotic/fractal formula. Shallit's 2023 paper studies the identical \(F(N)\), proves pseudopower bounds, and gives explicit special values such as \(F(2\cdot4^i)=2\cdot3^i\) and \(F((85\cdot4^{i+1}+1)/3)=55\cdot3^i\). These statements are not the exact extremum on each whole quartic shell with the uniquely placed minimum and the explicit recurrent maximizing sequence proven here. Coquet's general formula is a potentially stronger descriptive framework; without analyzing its periodic fluctuation's extrema, it does not directly state or supply these scale-by-scale sharp values. The original Coquet and later weighted-variant full texts were not independently obtained for a line-by-line comparison; equivalent undocumented consequences remain a residual priority risk.

## Limitations
No assertion is made about a complete list of maximizing positions; there are generally several. The theorem is specific to multiples of three and classical binary digit parity; it is not a claim about all rarefied moduli or weighted variants. No independent scientific audit has been performed. Older sources with general explicit formulas may yield some consequences by further optimization and require expert priority checking.

## References
1. Jeffrey Shallit, *Rarefied Thue-Morse Sums Via Automata Theory and Logic*, first public version 18 February 2023, arXiv:2302.09436, https://arxiv.org/abs/2302.09436 ; full preprint https://arxiv.org/html/2302.09436v2 .
2. Jean Coquet, *A summation formula related to the binary digits*, Inventiones Mathematicae 73 (1983), 107–115, DOI:10.1007/BF01393827.
3. Roswitha Hofer, *Coquet-type formulas for the rarefied weighted Thue–Morse sequence*, Discrete Mathematics 311 (2011), 1724–1734, DOI:10.1016/j.disc.2011.04.008.
