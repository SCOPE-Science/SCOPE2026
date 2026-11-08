# Exact minimal modular periods of the four-part elementary-symmetric partition sum

## Finding
For every integer \(n\ge0\), let \(a(n)\) be the sum of \(e_2(\lambda)=\sum_{1\le i<j\le4}\lambda_i\lambda_j\) over partitions \(\lambda_1\ge\lambda_2\ge\lambda_3\ge\lambda_4\ge1\) of \(n\) into **exactly four positive parts**. In particular \(a(n)=0\) for \(0\le n<4\). Let \(T(m)\) denote the least positive integer such that \(a(n+T(m))\equiv a(n)\pmod m\) for **all** \(n\ge0\).

For every positive integer \(m\), \(T(m)\) exists. Precisely, \(T(1)=1\), and if \(m=\prod_p p^{\alpha_p}\), then
\[
T(m)=\operatorname{lcm}_{p^{\alpha_p}\parallel m} T(p^{\alpha_p}),
\]
where for all positive \(r\),
\[
\begin{aligned}
T(2^r)&=3\cdot2^{r+3},\\
T(3)&=54,\\
T(3^r)&=4\cdot3^{r+2} \quad (r\ge2),\\
T(5^r)&=12\cdot5^{r+1},\\
T(p^r)&=12p^r \quad (p\ge7\text{ prime}).
\end{aligned}
\]
Moreover, the exact generating function is \(\sum_{n\ge0}a(n)q^n=N(q)/D(q)\) with
\[
\begin{aligned}
D(q)&=(q-1)^6(q+1)^4(q^2+1)^3(q^2+q+1)^3,\\
N(q)&=q^4(11q^{12}+25q^{11}+50q^{10}+72q^9+106q^8+126q^7\\
&\qquad+146q^6+121q^5+95q^4+57q^3+34q^2+15q+6).
\end{aligned}
\]
Thus \(a(n)\) satisfies the order-\(22\) recurrence given by \(D\) from its beginning. The complete period formula gives, in particular, \(T(10)=1200\) and \(T(18)=1296\), replacing the respective conjectural table entries \(1150\) and \(1246\) in the motivating paper. The predicted shifts already fail at \(n=0\): \(a(1150)\equiv2\pmod{10}\) and \(a(1246)\equiv6\pmod{18}\), whereas \(a(0)=0\).

## Assumptions and scope
All congruences are coefficientwise over integers. A period means an identity for every \(n\ge0\), not merely for sufficiently large \(n\). The modulus \(m\) is an arbitrary positive integer, and exponent \(r\) in prime powers is an arbitrary positive integer. The normalization counts partitions of **exactly four positive parts**, including equal parts, once each, weighted by the second elementary symmetric polynomial on those four parts.

## Proof
**1. Exact rational generating function.** Parametrize each four-part partition uniquely by \(a,b,c,e\ge0\) with its four parts
\[
(a+b+c+e+1,\ b+c+e+1,\ c+e+1,\ e+1).
\]
The total size is \(4+a+2b+3c+4e\). In these coordinates, direct expansion yields
\[
\begin{aligned}
 e_2={}&ab+2ac+3ae+3a+b^2+4bc+6be+6b\\
 &+3c^2+9ce+9c+6e^2+12e+6.
\end{aligned}
\]
Independently sum each monomial using, for \(x=q^w\), the three geometric moments \(\sum_{j\ge0}x^j=(1-x)^{-1}\), \(\sum jx^j=x(1-x)^{-2}\), and \(\sum j^2x^j=x(1+x)(1-x)^{-3}\), with weights \(w=1,2,3,4\). Integer-polynomial simplification gives exactly \(G=N/D\) as displayed. No cancellation remains over \(\mathbb Q[q]\), and \(\deg N=16<\deg D=22\). The file `artifacts/verify_periods.py` independently verifies this polynomial identity by multiplying all fourteen monomial rational expressions through a common denominator, without floating point.

**2. The modular period criterion.** Put \(R=\mathbb Z[q]/(D)\). Since \(D\) is monic of degree \(22\) with constant coefficient \(1\), its residue classes \(1,q,\ldots,q^{21}\) form an integral basis, and \(q\) is a unit. For any \(m,T\ge1\),
\[
 a(n+T)\equiv a(n)\ (\bmod\ m)\text{ for every }n\ge0
 \quad\Longleftrightarrow\quad N(q)(q^T-1)=0\text{ in }R/mR.
\]
Indeed, \((1-q^T)G\) is a polynomial of degree less than \(T\) exactly in the periodic case; division by monic \(D\) and \(\deg N<\deg D\) give equivalence with the quotient-ring condition. The criterion also shows the periods form a subgroup of \(\mathbb Z\), because \(q\) is invertible.

**3. Primes at least five.** The four resultants \(\operatorname{Res}(N,q-1)\), \(\operatorname{Res}(N,q+1)\), \(\operatorname{Res}(N,q^2+1)\), and \(\operatorname{Res}(N,q^2+q+1)\) are respectively \(864,32,144,36\). Thus \(N\) is invertible in \(R/p^rR\) for every prime \(p\ge5\). The criterion reduces to \(q^T=1\) in this ring. Modulo \(p\), roots of orders \(3\) and \(4\) force \(12\mid T\). The factor \((q-1)^6\) forces
\[
 p^r\mid\binom{T}{j}\qquad(1\le j\le5),
\]
by writing \(q=1+y\) and working modulo \(y^6\). Necessarily \(v_p(T)\ge r\). For \(p\ge7\), this is also sufficient, since \(v_p\binom{T}{j}\ge r\) for \(1\le j\le5<p\), yielding \(T=12p^r\). For \(p=5\), the \(j=5\) coefficient has \(v_5\binom{T}{5}=v_5(T)-1\) whenever \(5\mid T\), so necessity becomes \(v_5(T)\ge r+1\); this suffices for every \(j\le5\), giving \(T=12\cdot5^{r+1}\). To see sufficiency for the other three cyclotomic factors, note that for \(p\ge5\) these factors are pairwise comaximal modulo \(p\) and \(12\) is a unit modulo \(p\). In each factor's nilpotent neighborhood, \(q^{12}-1\) is its cyclotomic uniformizer times a unit. Hence the same binomial divisibility condition through the factor's multiplicity (at most \(6\)) makes \(q^T-1\) vanish modulo \(p^r\) in every component.

**4. The prime two.** Modulo \(2\), the denominator factors as \((q+1)^{16}(q^2+q+1)^3\), and the gcd of numerator with denominator is \((q+1)^4(q^2+q+1)\). The resulting reduced denominator is \((q+1)^{12}(q^2+q+1)^2\). The order of \(q\) in this quotient is \(\operatorname{lcm}(16,6)=48\). Consequently, \(T(2)=48\). Exact arithmetic in the integral rank-\(22\) quotient ring also gives
\[
q^{96}-1\in4R,\quad N(q^{96}-1)\in4R\setminus8R,
\]
where the coefficient of \(q^1\) in \(N(q^{96}-1)/4\), reduced modulo \(2\), is \(1\). Also \(N(q^{48}-1)\in2R\setminus4R\), with the same witness coordinate after division by \(2\). Write \(q^{96}=1+4C\). The valuation-two witness says \(NC\notin2R\). Repeated squaring \((1+4C)^{2^s}-1\) gives exactly \(2^{s+2}\) times an element congruent to \(C\) modulo \(2\); multiplication by any odd power does not change the valuation after multiplying by \(N\). Since every period modulo \(2^r\) is a multiple of \(48\), this proves \(T(2^r)=48\cdot2^{r-1}=3\cdot2^{r+3}\).

**5. The prime three.** Modulo \(3\), the denominator becomes \((q-1)^{12}(q+1)^4(q^2+1)^3\); its gcd with \(N\) is \((q-1)^2(q^2+1)^3\). The reduced denominator is \((q-1)^{10}(q+1)^4\), so the least period modulo \(3\) is \(\operatorname{lcm}(27,18)=54\). Since \(N\equiv-12\pmod{q^2+1}\), for any multiple of \(54\) not divisible by \(4\), its product with \(q^T-1\) reduces to \(24\pmod{q^2+1}\), not divisible by \(9\). Thus every period modulo \(3^r\) for \(r\ge2\) is a multiple of \(108\). Exact arithmetic gives
\[
 q^{108}-1\in3R,\quad N(q^{108}-1)\in3R\setminus9R,
\]
where the constant coefficient of \(N(q^{108}-1)/3\) modulo \(3\) equals \(1\). Writing \(q^{108}=1+3C\) and cubing repeatedly proves that \(N(q^{108\cdot3^s}-1)\) is divisible by exactly \(3^{s+1}\) in the integral basis. Multiplication of the exponent by an integer prime to \(3\) preserves this valuation. Therefore \(T(3^r)=108\cdot3^{r-1}=4\cdot3^{r+2}\) for \(r\ge2\).

**6. Arbitrary moduli.** By the Chinese remainder theorem, \(T\) is a period modulo \(m=\prod p^{\alpha_p}\) exactly when it is a period modulo every prime power. Their least common multiple is therefore the least period modulo \(m\). The case \(m=1\) is immediate. This proves all claims.

## Verification
The file `artifacts/verify_periods.py` uses only Python's standard library. It derives \(N/D\) by an independent exact polynomial identity from the fourteen gap monomials; compares the resulting recurrence against direct four-part enumeration for every \(0\le n\le110\); verifies the requisite quotient-ring modular powers and primitive coefficients; and checks the claimed exact periods against every prime divisor for 29 test moduli. Its executed output is in `artifacts/verification_output.txt`. The computation certifies only the specific finite polynomial identities, ring residues, and test moduli it evaluates; the universal prime-power conclusions follow from the binomial and lifting arguments in the proof, not from extrapolation of sampled moduli.

## Relationship to prior work
Ballantine, Beck, and Merca introduced and investigated this weighted four-part statistic, gave numerical evidence for an order-\(22\) recurrence and a conjectural table of modular periods, and proved the three congruence periods \(48\), \(54\), and \(96\) modulo \(2\), \(3\), and \(4\), respectively. Their Theorem 2 does not establish the least periods globally. Their other formulas concern unrestricted part sets and related statistics; neither implies this all-modulus minimal-period formula. Classical results of Nijenhuis–Wilf and Kwong apply to the unweighted four-part partition count rather than the weighted sequence here. The companion work on elementary symmetric partition maps concerns images of a partition map rather than modular periods of the four-part weighted sum. The fully explicit generating function, prime-power formulas, and identification of two inaccurate conjectural table entries are the assertions assessed here; they are not asserted to be publication-priority certified.

## Limitations
The formula concerns exactly four positive parts and the weight \(e_2\); no generalization to other lengths, other symmetric polynomials, or arbitrary weights is claimed. Exhaustive computer tests are not proofs for all moduli. Search coverage cannot rule out an inaccessible or unindexed equivalent treatment, and the result has not undergone independent scientific validation.

## References
- C. Ballantine, G. Beck, and M. Merca, *Partitions and elementary symmetric polynomials: an experimental approach*, arXiv:2408.13346, first posted 23 August 2024; journal version in *The Ramanujan Journal* 66 (2025), article 34, DOI: 10.1007/s11139-024-01001-6. https://arxiv.org/abs/2408.13346
- A. Nijenhuis and H. S. Wilf, *Periodicities of partition functions and Stirling numbers modulo p*, 1987 (unweighted restricted-partition periods, cited in the preceding paper).
- Y. H. H. Kwong, *Minimum periods of partition functions modulo M*, 1989 (unweighted restricted-partition periods, cited in the preceding paper).
- C. Ballantine, G. Beck, M. Merca, and B. E. Sagan, *Elementary symmetric partitions*, arXiv:2409.11268, 2024 (distinct image-partition questions). https://arxiv.org/abs/2409.11268
