# Exact parity support and a full logarithmic counting expansion for 16-regular partitions

## Finding
Let \(b_{16}(n)\) be the number of partitions of \(n\) into positive parts not divisible by \(16\), with \(b_{16}(0)=1\). For every integer \(n\ge0\), the following are equivalent:

1. \(b_{16}(n)\) is odd.
2. There are a prime \(p\equiv5\pmod 8\), an integer \(a\ge0\), and a positive odd integer \(u\) with \(p\nmid u\), such that
\[
8n+5=p^{4a+1}u^2.
\]

The factorization in (2) is unique. Write
\[
N(X)=\#\{0\le n\le X:b_{16}(n)\equiv1\pmod 2\},\qquad Y=8\lfloor X\rfloor+5,\qquad L=\log Y,
\]
and define
\[
S(s)=(1-2^{-s})\zeta(s),\qquad C_j=\frac14\sum_{m=0}^{j}\frac{j!}{m!}2^m(-1)^m S^{(m)}(2)\quad(j\ge0).
\]
For **every fixed integer** \(J\ge1\), as real \(X\to\infty\),
\[
\boxed{N(X)=Y\sum_{j=0}^{J-1}\frac{C_j}{L^{j+1}}+O_J\!\left(\frac{Y}{L^{J+1}}\right).}
\]
In particular,
\[
\boxed{N(X)\sim\frac{\pi^2}{4}\frac{X}{\log X}.}
\]
The next term, in the natural variable \(Y\), is explicit:
\[
N(X)=\frac{\pi^2}{32}\frac{Y}{L}+
\left(\frac{\pi^2}{32}-\frac{\pi^2\log2}{48}-\frac{3\zeta'(2)}8\right)\frac{Y}{L^2}
+O\!\left(\frac{Y}{L^3}\right).
\]
All coefficients \(C_j\) are finite combinations of derivatives of the Riemann zeta function at \(2\).

## Assumptions and scope
The partition count is the ordinary, unrestricted-multiplicity \(16\)-regular partition function; no parity restriction is imposed on the number of parts. The classification holds for every \(n\ge0\), including \(n=0\). Asymptotic assertions concern \(X\to\infty\), with a fixed expansion order \(J\), and use the ordinary natural logarithm. The prime-number theorem in the fixed arithmetic progression \(5\pmod8\), the classical two-square representation formula, and Jacobi's triple-product identity are used as established theorems.

## Proof
**1. Binary reduction to two triangular sequences.** Put \(f_t(q)=\prod_{h\ge1}(1-q^{th})\). In \(\mathbb F_2[[q]]\), the Frobenius identity gives \(f_{16}=f_1^{16}\), so
\[
\sum_{n\ge0}b_{16}(n)q^n=\frac{f_{16}}{f_1}\equiv f_1^{15}=(f_1^3)(f_1^3)^4.
\]
Jacobi's identity \(f_1^3=\sum_{i\ge0}(-1)^i(2i+1)q^{i(i+1)/2}\) reduces modulo \(2\) to \(\sum_{i\ge0}q^{T_i}\), where \(T_i=i(i+1)/2\). Fourth powers substitute \(q^4\) over \(\mathbb F_2\). Consequently,
\[
b_{16}(n)\equiv\#\{(i,j)\in\mathbb Z_{\ge0}^2:T_i+4T_j=n\}\pmod2.
\]
Completing squares transforms every such pair bijectively into a pair of positive integers
\[
8n+5=(2i+1)^2+(4j+2)^2,
\]
with the first coordinate odd and the second congruent to \(2\pmod4\).

**2. Exactly one-eighth of the two-square representations.** For \(M=8n+5\), every integral solution \(M=x^2+y^2\) has one odd coordinate and one coordinate congruent to \(2\pmod4\), since the squares modulo \(8\) are \(0,1,4\). Neither coordinate can vanish (\(M\equiv5\pmod8\) is not a square). Each unordered pair of absolute values therefore creates exactly eight signed, ordered solutions. Precisely one has the odd coordinate first and both coordinates positive. Thus the number of triangular pairs in step 1 equals \(r_2(M)/8\), where \(r_2(M)=\#\{(x,y)\in\mathbb Z^2:x^2+y^2=M\}\).

By the classical sum-of-two-squares formula, \(r_2(M)=0\) if a prime congruent to \(3\pmod4\) divides \(M\) to odd order; otherwise
\[
r_2(M)=4\prod_{p\equiv1\pmod4}(v_p(M)+1).
\]
Therefore \(r_2(M)/8\) is odd precisely when every prime \(\equiv3\pmod4\) has even exponent and the product \(\prod_{p\equiv1\pmod4}(v_p(M)+1)\) has \(2\)-adic valuation exactly one. The latter holds exactly when one prime \(p\equiv1\pmod4\) has exponent \(v_p(M)\equiv1\pmod4\) and all other prime exponents are even. All square factors of an odd integer are \(1\pmod8\); since \(M\equiv5\pmod8\), this unique prime must satisfy \(p\equiv5\pmod8\). This proves the stated unique factorization and both implications.

**3. Exact counting reduction.** Denote \(\pi(t;8,5)=\#\{p\le t:p\text{ prime},\ p\equiv5\pmod8\}\). By step 2, the count up to \(Y\) is the number of triples \((p,a,u)\) satisfying \(p^{4a+1}u^2\le Y\), \(p\equiv5\pmod8\), \(a\ge0\), \(u\ge1\) odd, and \(p\nmid u\). The triples with \(a\ge1\) are \(O(\sqrt Y)\): sum the elementary estimate \(\#\{u:u^2\le Y/p^{4a+1}\}\le\sqrt Y/p^{2a+1/2}\), first over \(a\ge1\) and then over primes \(p\ge5\); the resulting double sum converges. In the remaining case \(a=0\), dropping \(p\nmid u\) introduces at most \(\sum_{u\le\sqrt Y}\omega(u)=O(\sqrt Y\log Y)\) extra pairs, where \(\omega(u)\) counts distinct prime divisors; for each fixed \(u\), an excluded prime must itself divide \(u\). Hence
\[
N(X)=\sum_{\substack{u\le\sqrt{Y/5}\\u\ \mathrm{odd}}}\pi(Y/u^2;8,5)+O(\sqrt Y\log Y).
\]

**4. Full logarithmic expansion.** Fix \(J\ge1\) and split the sum in step 3 at \(u=Y^{1/10}\). The upper tail is \(O(Y^{9/10})\), using \(\pi(t;8,5)\le t\) and \(\sum_{u>U}u^{-2}=O(U^{-1})\). In the lower range, \(Y/u^2\ge Y^{4/5}\), and the prime-number theorem for the fixed residue class gives uniformly
\[
\pi(Y/u^2;8,5)=\frac14\operatorname{Li}(Y/u^2)+O\left(\frac{Y}{u^2}\exp(-c\sqrt{\log Y})\right)
\]
for some absolute \(c>0\). Summing the errors yields \(O(Y\exp(-c\sqrt{\log Y}))\) after adjusting \(c\).

Uniformly for \(u\le Y^{1/10}\), expansion of the logarithmic integral gives
\[
\operatorname{Li}(Y/u^2)=\frac{Y}{u^2}\sum_{j=0}^{J-1}\frac1{L^{j+1}}\sum_{m=0}^j\frac{j!}{m!}(2\log u)^m
+O_J\left(\frac{Y}{u^2}\frac{(1+\log u)^J}{L^{J+1}}\right).
\]
The remainder is summable, because \(\sum_{u\text{ odd}}u^{-2}(1+\log u)^J<\infty\). In each main coefficient the truncated sum over \(u\le Y^{1/10}\) may be extended to all positive odd \(u\) at a cost \(O_J(Y^{9/10}(\log Y)^J)\), negligible compared with any fixed \(Y/L^K\). Finally,
\[
\sum_{u\text{ odd}}\frac{(\log u)^m}{u^2}=(-1)^m\left.\frac{d^m}{ds^m}\big[(1-2^{-s})\zeta(s)\big]\right|_{s=2}.
\]
Collecting all terms proves the expansion, including the constants. Since \(S(2)=\pi^2/8\), the leading term is \(\pi^2Y/(32\log Y)\sim\pi^2X/(4\log X)\). No unproved hypothesis is used.

## Verification
The companion executable `verify_parity.py` implements three distinct finite checks, which are fully reproducible with Python 3 and its standard library. It computes \(b_{16}(n)\pmod2\) directly by partition dynamic programming, independently counts triangular pairs modulo two, and tests the prime-exponent criterion using a smallest-prime-factor sieve. All three agree for every \(0\le n\le5000\), totaling \(5001\) indices. For \(0\le n\le400\), a fourth exact enumeration confirms \(r_2(8n+5)=8\#\{(i,j):T_i+4T_j=n\}\), totaling \(401\) indices. Exact counts include \(N(100)=49\), \(N(500)=194\), \(N(1000)=356\), \(N(2000)=648\), and \(N(5000)=1457\). The checker does not test the infinite asymptotic or the PNT; those follow by the proof.

## Relationship to prior work
Keith and Zanello (2023) study parity densities for even-regular partitions and explicitly use a triangular-number support condition for the \(f_1^{15}\) factor in a different identity (Section 3.2). Their paper proves the analogous prime-exponent criterion for \(8\)-regular partitions, based on \(x^2+3y^2\), but does not state an all-index prime-square criterion for \(16\)-regular partitions or this sharp full counting expansion. Cherubini and Mercuri (2023) independently prove an exact prime-exponent characterization for the \(8\)-regular partition function, but neither their theorem nor its modular-form argument addresses the \(16\)-regular function or counting expansion. Their 2020 preprint (published in 2022) records known density-zero and congruence results for \(16\)-regular partitions. Cui and Gu (2013) prove infinite families of congruences for regular partitions including \(16\), as described by their abstract and by the later literature. Cao, Jin, Yao and Zhou (2025) give congruences modulo four for \(16\)-regular partitions; the inspected text does not contain the counting expansion here. General lacunarity theorems imply only density zero, not the precise \(X/\log X\) scale or its full expansion. The prime-number-theorem calculation and the explicit constants are the distinguishing quantitative contribution. No claim of originality is made for Jacobi's identity, the two-square formula, the PNT in arithmetic progressions, or density-zero lacunarity itself.

## Limitations
The theorem concerns only the parity of the \(16\)-regular partition function, not parity of ordinary partitions or higher residue classes modulo four or eight. The expansion is asymptotic for each fixed truncation order; it is not an everywhere-convergent series and does not give a uniform error for growing \(J\). A similar method could conceivably have appeared in unindexed or inaccessible historical sources; the 2013 Cui–Gu full text could not be examined, so this remains a named originality risk. The computational checks validate only finite ranges. Independent external review has not been carried out.

## References
1. W. J. Keith and F. Zanello, *Parity of the coefficients of certain eta-quotients, II: The case of even-regular partitions*, arXiv:2302.00708 (first public 2023-02-01). Sections 1–3, especially Sections 3.2 and 3.5.
2. W. J. Keith and F. Zanello, *Parity of the coefficients of certain eta-quotients*, arXiv:2010.09881 (first public 2020-10-19); J. Number Theory **235** (2022), 275–304.
3. S. P. Cui and N. S. S. Gu, *Arithmetic properties of ℓ-regular partitions*, Adv. Appl. Math. **51** (2013), 507–523, doi:10.1016/j.aam.2013.06.002.
4. S. Cao, J. Jin, O. X. M. Yao, and X. Zhou, *Infinite families of congruences modulo 4 for 16-regular partitions*, Bull. Math. Soc. Sci. Math. Roumanie **68** (2025), 219–229, https://ssmr.ro/bulletin/pdf/68-2/articol_9.pdf.
5. G. Cherubini and P. Mercuri, *Parity of the 8-regular partition function*, Ramanujan J. **63** (2024), 715–722, first online 2023-10-16, doi:10.1007/s11139-023-00784-4.
6. G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers*, classical two-square representation formula and the prime number theorem in arithmetic progressions.
