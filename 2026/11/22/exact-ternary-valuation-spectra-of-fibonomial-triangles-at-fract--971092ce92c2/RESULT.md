# Exact ternary valuation spectra of Fibonomial triangles at fractal scales

## Finding

Let \(F_0=0\), \(F_1=1\), and \(F_{n+2}=F_{n+1}+F_n\). Define the Fibonomial coefficient
\[
{m\brack k}_F=\frac{\prod_{j=1}^{m}F_j}{\bigl(\prod_{j=1}^{k}F_j\bigr)\bigl(\prod_{j=1}^{m-k}F_j\bigr)}
\qquad(0\le k\le m),
\]
where empty products equal one. For every integer \(L\ge0\), let
\[
H_L(u)=\sum_{m=0}^{4\cdot3^L-1}\ \sum_{k=0}^{m}u^{\nu_3({m\brack k}_F)}.
\]
The **complete three-adic valuation histogram** of these triangular blocks is given by
\[
\boxed{\sum_{L\ge0}H_L(u)z^L=\frac{10-42uz}{1-6(1+u)z+27uz^2}.}
\]
Equivalently, \(H_0(u)=10\), \(H_1(u)=60+18u\), and
\[
H_L(u)=6(1+u)H_{L-1}(u)-27uH_{L-2}(u)\quad(L\ge2).
\]
For every \(L\ge0\), exactly \(10\cdot6^L\) entries are prime to three. For every \(L\ge1\), the largest valuation is precisely \(L\), attained by exactly \(18\cdot6^{L-1}\) entries. The latter count is for individual triangle entries, including repeated numeric values at different positions.

## Assumptions and scope

All indices and counting multiplicities are integers. The outer sum includes every row from index zero through index \(4\cdot3^L-1\); the inner sum includes both boundaries of each row. We use the ordinary prime-adic valuation on positive integers. All equalities of generating functions are formal identities over the integer-polynomial ring in \(u\) (and hence also over rational functions). No limit interchange, unverified numeric interpolation, or assumption about higher-modulus Fibonomial congruences is needed.

## Proof

**1. Fibonacci factorial valuations.** Let
\[
Q=\begin{pmatrix}1&1\\1&0\end{pmatrix},\quad
C=\begin{pmatrix}-2&-1\\-1&-1\end{pmatrix}.
\]
The direct identity \(Q^4=-(I+3C)\) holds. Modulo three the matrix \(Q\) has order eight and its upper-right entry vanishes exactly for positive exponents divisible by four (equivalently, the successive pairs of Fibonacci residues have period eight, with zeros only at multiples of four). More precisely, for \(j=3^a v\) with \(3\nmid v\), binomial expansion and induction give
\[
(I+3C)^{3^a}=I+3^{a+1}C_a,\qquad C_a\equiv C\pmod3.
\]
For the inductive step cube \(I+3^{a+1}C_a\); the terms after the linear term are divisible by \(3^{a+3}\). Raising this identity to the power \(v\) gives a normalized upper-right matrix entry congruent to \(-v\pmod3\), hence nonzero. As \((Q^n)_{12}=F_n\), we obtain
\[
\nu_3(F_n)=\begin{cases}0,&4\nmid n,\\1+\nu_3(n/4),&4\mid n.\end{cases}
\]
Consequently, writing \(G(m)=\prod_{j=1}^mF_j\),
\[
\nu_3(G(m))=\left\lfloor\frac m4\right\rfloor+\nu_3\left(\left\lfloor\frac m4\right\rfloor!\right).
\]

**2. Four-residue reduction to ordinary binomials.** Write \(m=4Q+a\), \(k=4K+b\), where \(0\le a,b\le3\) and \(0\le k\le m\). From the factorial identity,
\[
\nu_3({m\brack k}_F)=
\begin{cases}
\nu_3\binom QK,&b\le a,\\
1+\nu_3\binom QK+\nu_3(Q-K),&b>a.
\end{cases}
\]
In the second case \(K<Q\), so the last valuation is defined; the formula follows because \(\lfloor(m-k)/4\rfloor=Q-K-1\). There are exactly ten choices of \((a,b)\) with \(b\le a\), and exactly six with \(b>a\), for each admissible \(K,Q\). Put \(R=Q-K\). For \(m<4\cdot3^L\), we have \(0\le Q<3^L\). Thus
\[
H_L(u)=10A_L(u)+6uB_L(u),
\]
where
\[
A_L(u)=\sum_{\substack{K,R\ge0\\K+R<3^L}}u^{\nu_3\binom{K+R}K},\quad
B_L(u)=\sum_{\substack{K\ge0,R\ge1\\K+R<3^L}}
 u^{\nu_3\binom{K+R}K+\nu_3(R)}.
\]

**3. Exact carry enumeration.** Kummer's carry identity states that \(\nu_3\binom{K+R}K\) equals the number of carries in adding \(K\) and \(R\) in base three. Each is written with exactly \(L\) digits, including leading zeros; \(K+R<3^L\) requires final carry zero. From incoming carry \(0\) or \(1\), there are respectively \((6,3)\) or \((3,6)\) digit-pair choices yielding outgoing carries \((0,1)\). Weight a transition by \(u\) if the outgoing carry is one. This gives
\[
T=\begin{pmatrix}6&3u\\3&6u\end{pmatrix},\qquad A_L(u)=(T^L)_{00}.
\]
For \(B_L\) also weight the consecutive low-order zero digits of \(R\) by \(u\); their number is \(\nu_3(R)\). Use states \(P\) (no nonzero digit of \(R\) has yet appeared, carry zero), \(C_0\) (it has appeared, carry zero), and \(C_1\) (it has appeared, carry one). Digits of \(R\) equal to zero keep \(P\) with weight \(3u\), while a first nonzero digit exits \(P\) with weights \(3,3u\); subsequent digits use \(T\). Hence
\[
M=\begin{pmatrix}3u&3&3u\\0&6&3u\\0&3&6u\end{pmatrix},
\qquad B_L(u)=(M^L)_{P,C_0}.
\]
The terminal condition \(C_0\) enforces both \(R\ne0\) and no overflow beyond the \(L\) digits. With \(\Delta(z,u)=1-6(1+u)z+27uz^2\), direct two-by-two inversion yields
\[
\sum_{L\ge0}A_L(u)z^L=\frac{1-6uz}{\Delta(z,u)}.
\]
A first-exit decomposition of the \(P\) state gives
\[
\sum_{L\ge0}B_L(u)z^L
=\frac{z(3,3u)(I-zT)^{-1}(1,0)^{\mathsf T}}{1-3uz}
=\frac{3z}{\Delta(z,u)}.
\]
Combining the two rational functions proves the displayed identity. Setting \(u=0\) gives \(10/(1-6z)\), so the valuation-zero count is \(10\cdot6^L\). The highest-degree term is read from the recurrence: \(\deg H_L=L\), with leading coefficient \(18\cdot6^{L-1}\) for every \(L\ge1\). Finally, substitution \(u=1\) gives \(H_L(1)=(4\cdot3^L)(4\cdot3^L+1)/2\), matching the total number of triangular entries.

## Verification

The self-contained Python 3 program `check.py` uses only the standard library. Run `python3 check.py` in the same directory. It constructs the digit-transition matrices independently from all nine base-three digit pairs, verifies the rational recurrence through level six, checks the exact total/zero/maximal counts, and separately calculates the Fibonacci integers and their factorial valuations to exhaust every coefficient in all triangular blocks through level five (\(472878\) entries at the last level). Its exhaustive test is independent of the carry transfer and passes. The mathematical proof establishes the formula for every \(L\), not merely the checked levels.

For illustration,
\[
H_2(u)=360+198u+108u^2,
\quad H_3(u)=2160+1728u+1350u^2+648u^3.
\]

## Relationship to prior work

Chen and Sagan [1, Section 5, Theorem 5.1] studied the Fibonomial triangle modulo three at precisely the side lengths \(4\cdot3^L\). Their congruence controls the zero/nonzero pattern, not the number of entries at each **higher valuation**. The valuation-zero specialization of the present formula is consistent with that pattern. Phunphayap and Pongsriiam [2] developed explicit prime-adic formulas for individual Fibonomial coefficients and [3] studied digital divisibility and asymptotics for the one-parameter subfamily \({pn\brack n}_F\). The present result instead sums the full valuation distribution over every two-index triangular block. Knuth and Wilf [4] established a general prime-power carry framework; ordinary Kummer carries serve as an input here, while the combined finite-state enumeration and exact rational histogram are separate contributions.

## Limitations

This result concerns only the prime three, ordinary Fibonacci numbers, and the specified triangular blocks. It does not determine the residues of Fibonomial coefficients modulo higher powers of three, only their valuations. Prior individual-valuation identities can in principle compute entries, but the explicit all-level histogram requires the counting argument above. A semantically equivalent finite-block enumeration in less readily searchable literature cannot be ruled out; independent scholarly review has not been performed.

## References

[1] Xi Chen and Bruce E. Sagan, “The fractal nature of the Fibonomial triangle,” arXiv:1306.2377 (2013), especially Section 5. https://arxiv.org/html/1306.2377v1

[2] Phakhinkon Phunphayap and Prapanpong Pongsriiam, “Explicit Formulas for the p-adic Valuations of Fibonomial Coefficients,” *Journal of Integer Sequences* 21 (2018), Article 18.3.1. https://cs.uwaterloo.ca/journals/JIS/VOL21/Pongsriiam/pong12.pdf

[3] Phakhinkon Napp Phunphayap and Prapanpong Pongsriiam, “Divisibility of Fibonomial coefficients in terms of their digital representations and applications,” *AIMS Mathematics* 7 (2022), 5314–5327, published 6 January 2022, DOI:10.3934/math.2022296. https://www.aimspress.com/aimspress-data/math/2022/4/PDF/math-07-04-296.pdf

[4] Donald E. Knuth and Herbert S. Wilf, “The power of a prime that divides a generalized binomial coefficient,” *Journal für die reine und angewandte Mathematik* 396 (1989), 212–219. DOI:10.1515/CRLL.1989.396.212. https://eudml.org/doc/153129
