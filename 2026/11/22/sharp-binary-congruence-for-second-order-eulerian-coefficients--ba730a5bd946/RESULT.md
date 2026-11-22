# Sharp binary congruence for second-order Eulerian coefficients

## Finding

Write \(E(n,k)\) for the number of order-\(n\) Stirling permutations with precisely \(k\) *internal ascents*, where the two occurrences of each letter are separated only by larger letters. For every \(n\ge1\) and \(0\le k<n\), put \(c=\lceil k/2\rceil\). Then

\[
\boxed{\frac{E(n,k)}{2^c}\equiv\binom{n-c}{k}\pmod2.}
\]

The quotient is always an integer. For every fixed \(k\ge1\), the divisibility \(2^{\lceil k/2\rceil}\mid E(n,k)\) is sharp exactly when every set binary digit of \(k\) also occurs in \(n-\lceil k/2\rceil\). Consequently the first row achieving the minimum valuation is \(n=\lceil 3k/2\rceil\), the sharpness pattern has exact least eventual index period \(2^{1+\lfloor\log_2 k\rfloor}\), and its natural density is \(2^{-s_2(k)}\), where \(s_2(k)\) is the number of set binary digits of \(k\).

Equivalently, with coefficients reduced modulo two, for each \(k\ge0\),

\[
\boxed{\sum_{n\ge0}\Big(\frac{E(n,k)}{2^{\lceil k/2\rceil}}\bmod2\Big)z^n
=\frac{z^{\lceil3k/2\rceil}}{(1+z)^{k+1}}\in\mathbb F_2[[z]].}
\]

## Assumptions and scope

An order-\(n\) Stirling permutation is a word containing each of \(1,\ldots,n\) twice in which all letters strictly between two copies of \(i\) are greater than \(i\). An *internal ascent* is an adjacent pair in the word whose second entry exceeds the first; neither external sentinel contributes. At order zero the empty word gives \(E(0,0)=1\). We set \(E(n,k)=0\) for \(k<0\) and \(k\ge n\) when \(n\ge1\), and for \(k\ne0\) when \(n=0\). Binomial coefficients with nonnegative upper index smaller than the lower index are zero. All index, period, and density statements concern nonnegative integers; the fixed-column period concerns \(n\ge k+1\), and the density is with respect to row indices \(n\to\infty\).

Inserting the two adjacent copies of the new largest letter into the \(2n-1\) gaps of an order-\(n-1\) word gives the standard recurrence

\[
E(n,k)=(k+1)E(n-1,k)+(2n-k-1)E(n-1,k-1),\quad n\ge1.
\]

The internal-ascent convention places the single order-one word in column zero. The common convention counting the compulsory initial ascent has column index \(k+1\) instead; the normalization in this result refers to the internal-ascent index \(k\).

## Proof

**Integral normalization.** Put \(c_k=\lceil k/2\rceil\). Induct on \(n\), using the recurrence. If \(k=2j\), then \(c_{k-1}=c_k=j\), so each summand is divisible by \(2^j\). If \(k=2j+1\), then \(c_k=j+1\) and \(c_{k-1}=j\), while both multipliers \(k+1=2(j+1)\) and \(2n-k-1=2(n-j-1)\) are even. Thus both summands are divisible by \(2^{j+1}\). The zero and boundary cases cause no exception. This proves integrality for all coefficients.

**Parity recurrences.** Let \(a(n,k)=E(n,k)/2^{c_k}\) and reduce its values modulo two. For \(j\ge1\) and \(n\ge1\), the even-column recurrence becomes

\[
a(n,2j)\equiv a(n-1,2j)+a(n-1,2j-1)\pmod2.
\]

For \(j\ge0\) and \(n\ge1\), the odd-column recurrence becomes

\[
a(n,2j+1)\equiv(n-j-1)a(n-1,2j)\pmod2.
\]

Here the first odd-column summand is even after normalization, because it carries a factor \(2(j+1)\). These recurrences apply to all zero-extended coefficients as well.

**Exact generating functions.** Work in the formal power-series ring \(\mathbb F_2[[z]]\), and set \(F_k(z)=\sum_{n\ge0}(a(n,k)\bmod2)z^n\), \(H_j=F_{2j}\), \(J_j=F_{2j+1}\). From \(a(n,0)=1\) we have \(H_0=1/(1+z)\). Summing the two displayed recurrences gives

\[
H_j=\frac{zJ_{j-1}}{1+z}\quad(j\ge1),\qquad
J_j=z\big(zH_j'(z)+jH_j(z)\big)\quad(j\ge0).
\]

The differentiation is formal. Assume \(H_j=z^{3j}/(1+z)^{2j+1}\). The formal logarithmic derivative, interpreted as the product rule without requiring division by \(z\), shows

\[
zH_j'+jH_j=\big((3j+j)+(2j+1)z/(1+z)\big)H_j
=\frac{z}{1+z}H_j
\]

in characteristic two, because \(3j+j\equiv0\pmod2\) and \(2j+1\equiv1\pmod2\). Therefore \(J_j=z^{3j+2}/(1+z)^{2j+2}\) and \(H_{j+1}=z^{3j+3}/(1+z)^{2j+3}\). Induction from \(H_0\) proves, for every \(k\ge0\),

\[
F_k(z)=\frac{z^{\lceil3k/2\rceil}}{(1+z)^{k+1}}.
\]

**Coefficient extraction.** In characteristic two, the coefficient of \(z^m\) in \((1+z)^{-k-1}\) equals \(\binom{m+k}{k}\bmod2\) for \(m\ge0\). Taking \(m=n-\lceil3k/2\rceil\), with a zero coefficient if this is negative, gives the stated formula \(\binom{n-\lceil k/2\rceil}{k}\bmod2\). In particular, \(m=0\) proves the first sharp row \(n=\lceil3k/2\rceil\).

**Digits, least period, and density.** Lucas's binomial congruence at two says \(\binom{u}{k}\) is odd exactly when all one-bits of \(k\) occur in \(u\). For \(k\ge1\), let \(r=1+\lfloor\log_2 k\rfloor\), so membership depends only on \(u\bmod2^r\). Exactly \(2^{r-s_2(k)}\) of these \(2^r\) residues contain the required set bits, giving density \(2^{-s_2(k)}\). Adding \(2^{r-1}\) to \(u=k\) flips its highest required bit, hence \(2^{r-1}\) is not a period. Any least period of a \(2^r\)-periodic binary word divides \(2^r\); since the proper divisors are at most \(2^{r-1}\), the least period is \(2^r\). Shifting from \(u\) to \(n=u+\lceil k/2\rceil\) leaves periods unchanged. This completes the proof.

## Verification

The accompanying standard-library Python program `check.py` independently enumerates the smallest Stirling permutations by insertion, checks the coefficient recurrence, exact integral normalization, binomial parity and Lucas digit criteria for all indices through row 360, and tests sharp starting rows and finite periodic patterns. It reports `PASS 195380 exact assertions; N= 360`. These finite diagnostics do not prove the unbounded statement; the formal power-series induction and Lucas theorem do.

## Relationship to prior work

Haglund and Visontai studied the second-order Eulerian/Stirling-permutation polynomials and proved multivariate stability and real-rootedness; their full text has a one-column shift because the initial ascent is counted. Chen, Hao and Yang (2012) studied related stable refinements and the transformed polynomials \(2^nC_n(z/2)\). Neither result supplies coefficientwise binary normalization or a sharpness classification. Castro, González and Medina (2015) study valuations of *ordinary Eulerian numbers*, not Stirling-permutation coefficients. Zhao, Hong and Zhao's 2012 preprint studies valuations of the *ordinary Stirling numbers of the second kind* \(S(n,k)\), not the second-order Eulerian triangle. The published flattened-Stirling-permutation descent-set count concerns another restricted statistic and has no implication that yields the present congruence. The recorded OEIS triangle supplies finite values, not an unrestricted parity theorem. The present result is thus a separate prime-adic arithmetic statement, not a corollary of real stability or an ordinary Stirling-number valuation law.

## Limitations

The result determines the *minimum attained* \(2\)-adic valuation in each fixed column and classifies equality. It does not give higher valuations when equality fails, nor does it assert a new distribution for general \(r\)-Stirling permutations. A prior equivalent formulation hidden in the older divisibility or digit-automata literature could affect historical priority; this is not a proof of global novelty. The review is non-independent, and finite checks do not certify the infinite claim.

## References

1. J. Haglund and M. Visontai, “Stable multivariate Eulerian polynomials and generalized Stirling permutations,” *European Journal of Combinatorics* 33 (2012), 477–487. DOI: https://doi.org/10.1016/j.ejc.2011.10.007; lawful accessible full text: https://sites.math.washington.edu/~billey/classes/561.fall.2021/past.articles/haglund.vis.2012.pdf (available online January 5, 2012).
2. W. Y. C. Chen, R. X. J. Hao, H. R. L. Yang, “Context-free Grammars and Multivariate Stable Polynomials over Stirling Permutations,” arXiv:1208.1420 (August 7, 2012), https://arxiv.org/abs/1208.1420; full text https://arxiv.org/html/1208.1420v2.
3. J. Zhao, S. Hong, W. Zhao, “Divisibility by 2 of Stirling numbers of the second kind and their differences,” arXiv:1209.6284 (September 27, 2012), https://arxiv.org/abs/1209.6284. This reference concerns a different triangle.
4. F. N. Castro, O. E. González and L. A. Medina, “The p-adic Valuation of Eulerian Numbers: Trees and Bernoulli Numbers,” *Experimental Mathematics* 24 (2015), 183–195, https://doi.org/10.1080/10586458.2014.981899. This study concerns ordinary Eulerian numbers.
5. E. W. Weisstein, “Second-Order Eulerian Triangle,” MathWorld, https://mathworld.wolfram.com/Second-OrderEulerianTriangle.html.
6. OEIS A201637, second-order Eulerian triangle, https://oeis.org/A201637.
