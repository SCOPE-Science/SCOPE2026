# A divisor-sum census of every three-point cyclic Fourier minor

## Finding
Let \(N\ge3\) be an arbitrary integer. For the unnormalized complex character table
\[
F_N=(\exp(2\pi i rc/N))_{r,c\in\mathbb Z_N},
\]
choose any *unordered* three-point row set \(R\) and *unordered* three-point column set \(C\), with the ordered pair \((R,C)\) retaining the row/column distinction. Put \(T=\binom N3\), and use the convention \(\binom m3=0\) for \(m<3\). Define the following integers by finite arithmetic divisor sums:
\[
\begin{aligned}
P_N&=\frac{N^2(N-2)}2\sum_{\substack{a\mid N\\a<N}}\frac{\varphi(N/a)}a\binom a3,\\
Q_N&=\frac{N^2}4\sum_{\substack{a,b\mid N\\a,b<N\\N\mid ab}}\varphi(N/a)\varphi(N/b)(a-2)(b-2),\\
M_h&=\sum_{\substack{k\mid N\\h\mid k}}\mu(k/h)\,k\binom{N/k}3\quad(h\mid N),\\
L_N&=\sum_{h\mid N}M_h\frac Nh\binom h3.
\end{aligned}
\]
Here \(\varphi\) is Euler's totient and \(\mu\) is the classical Möbius function. The **complete complex rank incidence** of all \(T^2\) restrictions is
\[
\boxed{\begin{aligned}
\#\{(R,C):\operatorname{rank}F_N[R,C]=1\}&=L_N,\\
\#\{(R,C):\operatorname{rank}F_N[R,C]=2\}&=2P_N-Q_N+3L_N,\\
\#\{(R,C):\operatorname{rank}F_N[R,C]=3\}&=T^2-2P_N+Q_N-4L_N.
\end{aligned}}
\]
There are no other ranks. These expressions apply without any restriction on the number, multiplicity, or parity of prime factors of \(N\).

In particular, for the first cyclic order having three distinct prime factors, \(N=30\), the exact counts are
\[
\boxed{(R_1,R_2,R_3)=(18{,}000,\ 1{,}519{,}200,\ 14{,}946{,}400)}
\]
among \(\binom{30}{3}^2=16{,}483{,}600\) row/column pairs.

## Assumptions and scope
All ranks are computed over \(\mathbb C\); row and column indices are distinct residues modulo \(N\). The Fourier transform is unnormalized, though multiplying every entry by the same nonzero normalization would not change ranks. The arithmetic sums above are exact, with no floating-point or genericity assumptions. Each selected row/column set is unordered, but the two sets are chosen separately. This is a census of all third-order minors, not of arbitrary larger Fourier minors. The elementary three-by-three unit-modulus determinant rigidity used below is preexisting and is not asserted as new.

## Proof
**1. Rigidity of a unit-modulus three-by-three matrix.** We recall the elementary fact that a singular complex three-by-three matrix whose entries all have modulus one must have two proportional rows or two proportional columns. Multiplying rows and columns by nonzero constants puts the matrix in the form
\[
B=\begin{pmatrix}1&1&1\\1&u&v\\1&w&t\end{pmatrix},\qquad |u|=|v|=|w|=|t|=1.
\]
The determinant vanishes precisely when \((u-1)(t-1)=(v-1)(w-1)\). If both products are nonzero, conjugate and use \(\overline{z-1}=-(z-1)/z\) for \(|z|=1\), obtaining \(ut=vw\). Expanding the original equation then gives \(u+t=v+w\). Equal sums and products force the unordered pairs \(\{u,t\}\) and \(\{v,w\}\) to coincide. The two possibilities make either the last two rows equal or the last two columns equal. If both products are zero, checking the four choices of zero factors gives the same conclusion. The converse is immediate. This also shows that a singular Fourier minor of size three has no rank-deficiency mechanism besides proportional selected row/column pairs.

**2. A local indicator identity.** For a fixed selected restriction, let \(k_R\) be the number of unordered row pairs proportional on the selected columns, and let \(k_C\) be the number of proportional column pairs on the selected rows. Since proportionality is an equivalence relation, either value is \(0\), \(1\), or \(3\). A rank-one minor has \(k_R=k_C=3\). A rank-two minor has \(k_R,k_C\in\{0,1\}\), at least one equal to one by Step 1. A full-rank minor has \(k_R=k_C=0\). Thus, for every restriction,
\[
\mathbf1_{\{\operatorname{rank}\le2\}}
=k_R+k_C-k_Rk_C+4\mathbf1_{\{\operatorname{rank}=1\}}.
\]
Summing over all restrictions, put \(P=\sum k_R=\sum k_C\) (symmetry), \(Q=\sum k_Rk_C\), and \(L\) equal to the number of rank-one restrictions. Then
\[
R_1=L,\qquad R_2=2P-Q+3L,\qquad R_3=T^2-2P+Q-4L.
\]
It remains to calculate these three incidence statistics without enumerating minors.

**3. The one-pair incidence \(P\).** Two selected rows with nonzero difference \(d\in\mathbb Z_N\) restrict proportionally to a column triple exactly when all column differences \(c-c'\) satisfy \(d(c-c')\equiv0\pmod N\). Write \(a=\gcd(N,d)\). The annihilator subgroup \(H_d=\{c:dc\equiv0\pmod N\}\) has size \(a\). Thus such a column triple must lie in one of its \(N/a\) cosets, giving \((N/a)\binom a3\) possibilities. There are \(N\varphi(N/a)/2\) unordered row pairs whose difference has this greatest common divisor, and the third row can be any of \(N-2\) further points. Multiplication and summation over the proper divisors \(a\mid N\) gives exactly \(P_N\). By transposition the same count applies to proportional selected column pairs.

**4. The simultaneous-pair incidence \(Q\).** Choose an unordered row pair with difference \(d\), and an unordered column pair with difference \(e\). They can be simultaneously proportional on the completed triples only if \(de\equiv0\pmod N\). In that event the third row must belong to the annihilator coset of \(e\) already containing the selected row pair, leaving \(\gcd(N,e)-2\) choices; analogously there are \(\gcd(N,d)-2\) choices for the third column. For fixed \(a=\gcd(N,d)\), \(b=\gcd(N,e)\), the condition \(N\mid de\) is equivalent to \(N\mid ab\), prime power by prime power. Each row/column pair has \(N\varphi(N/a)/2\), respectively \(N\varphi(N/b)/2\), choices. Summing their product and the two completion factors yields exactly \(Q_N\). This counts all ordered choices of one proportional row pair and one proportional column pair, including the nine pair-of-pair incidences in each rank-one restriction.

**5. The rank-one incidence \(L\).** For a fixed row triple \(R=\{r_1,r_2,r_3\}\), set \(h=\gcd(N,r_2-r_1,r_3-r_1)\). All selected rows are proportional on a column triple precisely when its three columns lie in one coset of the common annihilator of the subgroup generated by the two differences. That annihilator has \(h\) members and \(N/h\) cosets, hence \((N/h)\binom h3\) admissible column triples. To count row triples with exact value \(h\), note that the number whose three points all coincide modulo any divisor \(k\mid N\) is \(k\binom{N/k}3\). Because that condition is equivalent to \(k\mid h\), Möbius inversion on the divisor lattice gives exactly \(M_h\) row triples of gcd \(h\). Summation over \(h\mid N\) gives \(L_N\). Substituting Steps 3–5 into Step 2 proves all three formulas for every \(N\ge3\).

## Verification
The standalone Python 3 standard-library checker `verify_census.py` computes the Möbius–totient formulas with integer arithmetic and independently counts all proportional-pair events for each \(N\in\{3,4,5,6,8,9,10,12\}\). It also checks the closed counts for \(N\in\{15,21,30\}\); all match.

Two further independent exact computations verify the most informative three-prime case \(N=30\). `verify_rank30_cyclotomic.py` reduces the six-term determinant of each of the \(\binom{29}{2}^2=164{,}836\) anchored pairs modulo \(\Phi_{30}(x)=x^8+x^7-x^5-x^4-x^3+x+1\). `checker_mod30.py` instead evaluates the same determinants at all eight primitive thirtieth roots modulo the prime \(1201\). As each power of a thirtieth root reduces to an integer polynomial with coefficient absolute value at most one in the degree-eight basis, the reduced determinant has coefficients of absolute value at most six. Consequently, zero at all eight distinct primitive roots modulo \(1201\) is equivalent to exact vanishing in the integer cyclotomic ring; no numerical tolerance is involved.

The two checks agree on anchored ranks \((180,15192,149464)\). Independent translation of row and column triples preserves the rank; for \(N=30\) each anchored incidence contributes the exact multiplicity \((30/3)^2=100\) to the global count. This reproduces the three boxed values. These finite checks independently corroborate the general formula but do not replace the universal proof in Steps 1–5. All programs can be run directly with Python 3 and need no external dependencies.

## Relationship to prior work
Krahmer, Pfander and Rashkov (2006) give numerical minor-rank tables for the cyclic groups of orders five and six, not an arbitrary-order rank census; our formulas reproduce their order-six third-minor counts \((0,48,352)\). Delvaux and Van Barel (2006, 2007/2008) analyze maximal rank-deficient blocks and subgroup tilings of Fourier matrices rather than the rank distribution across *all* third-order restrictions. Bonami and Ghobber (2010) study minimum Fourier-support equality cases for prime-square and semiprime groups; their results do not determine the present incidence distribution.

Previously published specialized exact censuses cover cyclic prime powers, products of two distinct primes, even semiprimes, and third-order principal minors. These coincide with arithmetic specializations or restrictions of this theorem but do not settle orders with arbitrarily many distinct and/or repeated prime factors. In particular, order thirty is outside those two-prime and prime-power statements. The preexisting unit-modulus rigidity lemma is shared with those works. This result adds the all-order three-rank divisor-sum law and an exact three-prime benchmark, not a new determinant-rigidity principle. A previously unindexed or differently formulated equivalent census remains a historical priority risk.

## Limitations
The theorem applies only to complex restrictions with precisely three distinct row indices and three distinct column indices; it makes no claim about fourth- or higher-order minors, optimal singular values, arbitrary finite abelian groups beyond the cyclic case, or uniqueness of prior publication. All computations are finite corroboration; the infinite theorem is justified by the provided combinatorial proof. The literature comparison is bounded, and independent mathematical validation has not been performed.

## References
1. F. Krahmer, G. E. Pfander and P. Rashkov, *Uncertainty in time–frequency representations on finite Abelian groups and applications*, arXiv:math/0611493v1, first posted 2006-11-16, https://arxiv.org/abs/math/0611493, Section 3 and Table 1.
2. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Fourier matrices*, KU Leuven Report TW470, September 2006; Linear Algebra and its Applications 429 (2008), 1587–1605, https://www.cs.kuleuven.be/publicaties/rapporten/tw/TW470.abs.html.
3. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, KU Leuven Report TW477, November 2006; Linear Algebra and its Applications 426 (2007), 349–367, https://doi.org/10.1016/j.laa.2007.05.009.
4. A. Bonami and S. Ghobber, *Equality cases for the uncertainty principle in finite Abelian groups*, arXiv:1003.5060v1, first posted 2010-03-26, https://arxiv.org/abs/1003.5060.
5. *Valuation-stratified rank census for three-point Fourier sampling on prime-power cycles*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-valuation-stratified-rank-census-for-three-point-fourier-samplin--0fc41b9fd0d2.
6. *Complete third-order Fourier-minor rank incidence for distinct-prime cyclic products*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-third-order-fourier-minor-rank-incidence-for-distinct-p--6a97dfb3d140.
7. *Exact singularity criterion for three-point principal Fourier minors*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-singularity-criterion-for-three-point-principal-fourier-mi--1482c28703d6.
