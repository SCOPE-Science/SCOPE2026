# Common logarithmic gaps for finitely many Romanoff bases
## Finding
Let \(\mathcal A\subset\{2,3,\ldots\}\) be any fixed finite nonempty set. Define
\[
\mathcal R_{\mathcal A}=\{p+a^n:p\in\mathbb P,\ a\in\mathcal A,\ n\ge1\}.
\]
If \(G_{\mathcal A}(X)\) denotes the maximum length of a consecutive interval contained in \([1,X]\) and disjoint from \(\mathcal R_{\mathcal A}\), then
\[
G_{\mathcal A}(X)\gg_{\mathcal A}\log\log X.
\]
This is a simultaneous finite-base extension of the recent theorem for one fixed base.

## Assumptions and scope
The set \(\mathcal A\) is fixed as \(X\to\infty\); the implied constant may depend on \(\mathcal A\). Primes are positive rational primes and exponents satisfy \(n\ge1\). No assertion is made uniformly when the number or size of the bases is allowed to grow with \(X\).

The proof uses Radomskii's translate lemma for \(O(\log X)\) distinct integer shifts of absolute value at most \(X\). In the notation of that lemma, for sufficiently large \(x\), if \(Q=\prod_{p\le x}p\), \(k\le\eta x\), and \(|s_i|\le e^{3x}\), then for every integer \(b\) there is \(1\le t\le e^x\) such that each \(b+Qt+s_i\) is divisible by a prime in
\[
\left(x^6,\exp\!\left(\frac{x}{(\log x)^5}\right)\right].
\]

## Proof
Write
\[
x=\frac13\log X,\qquad Q=\prod_{p\le x}p,
\]
and put \(H=\lfloor c_{\mathcal A}\log x\rfloor\), where the positive constant \(c_{\mathcal A}\) will be chosen small enough. Let
\[
\mathcal P_{\mathcal A}(X)=\{a^n:a\in\mathcal A,\ n\ge1,\ a^n\le X\}.
\]
After duplicate values are removed,
\[
M:=|\mathcal P_{\mathcal A}(X)|\le \left(\sum_{a\in\mathcal A}\frac1{\log a}\right)\log X+O_{\mathcal A}(1)=O_{\mathcal A}(x).
\]

Consider the distinct shifts
\[
\mathcal S_0=\{j-w:1\le j\le H,\ w\in\mathcal P_{\mathcal A}(X)\}.
\]
Averaging over \(b_0\pmod Q\) gives some residue class \(b_0\) for which the subset
\[
\mathcal S=\{s\in\mathcal S_0:(b_0+s,Q)=1\}
\]
satisfies
\[
|\mathcal S|\le |\mathcal S_0|\frac{\varphi(Q)}Q
 \le HM\frac{\varphi(Q)}Q.
\]
By Mertens' product theorem,
\[
\frac{\varphi(Q)}Q=\frac{e^{-\gamma}+o(1)}{\log x},
\]
so
\[
|\mathcal S|\le\left(3e^{-\gamma}c_{\mathcal A}\sum_{a\in\mathcal A}\frac1{\log a}+o_{\mathcal A}(1)\right)x.
\]
Choose \(c_{\mathcal A}>0\) so that the displayed leading coefficient is less than the constant \(\eta\) from the translate lemma. Then \(|\mathcal S|\le\eta x\) for all sufficiently large \(X\). Also every \(s\in\mathcal S_0\) satisfies \(|s|\le X=e^{3x}\).

It remains to place the translated block away from every relevant power. The points of \(\mathcal P_{\mathcal A}(X)\) lying in \([X/4,3X/4]\) cut that interval into at most \(M+1\) power-free gaps. Hence one such gap \((L,R)\) has length
\[
D=R-L\ge\frac{X}{2(M+1)}\gg_{\mathcal A}\frac X{\log X}.
\]
The prime number theorem gives
\[
Qe^x=\exp((2+o(1))x)=X^{2/3+o(1)}=o(D),
\]
and also \(Q+H=o(D)\). Moreover, with
\[
y=\exp\!\left(\frac{x}{(\log x)^5}\right),
\]
one has \(y=o(D)\).

Choose an integer \(b\equiv b_0\pmod Q\) with
\[
L+\frac D4\le b<L+\frac D4+Q.
\]
Apply the translate lemma to the distinct shifts in \(\mathcal S\). It yields \(1\le t\le e^x\). Put \(N=b+Qt\). For sufficiently large \(X\), the estimates above imply
\[
[N+1,N+H]\subset\left(L+\frac D4,L+\frac D2\right)\subset(L,R).
\]
Consequently every point of this block is at distance at least \(D/4+o(D)\) from every member of \(\mathcal P_{\mathcal A}(X)\); in particular, whenever \(w\in\mathcal P_{\mathcal A}(X)\) and \(w<N+j\),
\[
N+j-w>y
\]
for all sufficiently large \(X\).

Fix \(1\le j\le H\), \(a\in\mathcal A\), and \(n\ge1\), and write \(w=a^n\). If \(w>N+j\), then \(N+j-w<0\), so it cannot be a positive prime. If \(w\le X\) and \(w<N+j\), set \(s=j-w\). When \(s\notin\mathcal S\), the integer \(N+s=N+j-w\) has a prime divisor at most \(x\), because \((b_0+s,Q)>1\). When \(s\in\mathcal S\), the translate lemma gives a prime divisor at most \(y\). In either case \(N+j-w>y\), so this divisor is proper and \(N+j-w\) is composite. Finally, if \(w>X\), then \(w>N+j\) because the whole constructed block lies below \(X\) for large \(X\).

Thus none of \(N+1,\ldots,N+H\) belongs to \(\mathcal R_{\mathcal A}\). Since \(H\asymp_{\mathcal A}\log x\asymp\log\log X\), the claimed lower bound follows.

## Verification
The proof is symbolic and does not infer an infinite statement from finite computation. The nonstandard input is precisely the translate lemma stated above; its hypotheses are checked after duplicate shifts are removed. The two scale comparisons needed for block placement are \(Qe^x=X^{2/3+o(1)}=o(X/\log X)\) and \(y=X^{o(1)}=o(X/\log X)\).

The critical sign and proper-divisor cases are explicit: a power above the block gives a negative difference, while a power below the block gives a positive difference exceeding every auxiliary divisor supplied by the sieve. The macroscopic power-free gap prevents a zero difference and prevents an auxiliary divisor from being the whole difference.

## Relationship to prior work
Radomskii proves \(G_{\mathcal R}(X)\gg\log\log X\) for the classical base \(2\), and in Corollary 1.1 proves the same order for \(p+a^n\) for each single fixed integer \(a\ge2\). The present statement is not obtained by intersecting those individual gaps: individual long gaps for different bases need not coincide. Instead, the proof places one block inside a gap of the finite union of all relevant power sequences and feeds all surviving shifts from all bases into the same translate lemma.

The large-shift feature of Radomskii's lemma is essential here because the simultaneous shift set still has \(O_{\mathcal A}(\log X\log\log X)\) raw pairs but only \(O_{\mathcal A}(x)\) survivors after the preliminary sieve when \(H\asymp\log x\).

## Limitations
The family of bases must be fixed. The argument gives no uniform constant for growing families \(\mathcal A=\mathcal A(X)\), and it does not determine the optimal leading constant in front of \(\log\log X\). It also does not give an upper bound for the common-gap function.

## References
1. A. Radomskii, *Large gaps between Romanoff numbers*, arXiv:2609.38408v1, first public version 2026-09-29. Theorem 1.1, Corollary 1.1, Lemma 3.1, and Section 5.
2. A. Kalmynin and S. Konyagin, earlier lower bound for gaps between classical Romanoff numbers, as summarized and improved in the reference above.
