# Parity-perfect quadratic-character cancellation and sharp fluctuations in Stern’s sequence modulo five

## Finding

Let \(s(n)\) be Stern’s diatomic sequence, and let \(\chi_5\) be the quadratic character modulo five, equal to \(1\) on \(\{1,4\}\), to \(-1\) on \(\{2,3\}\), and to \(0\) on \(0\). Define, for every integer \(L\geq0\),

\[
B_L=\sum_{2^L\leq n<2^{L+1}}\chi_5(s(n)).
\]

Then the exact ordinary generating function is

\[
\boxed{\sum_{L\geq0}B_L z^L=\frac{1-3z^2}{1-z^2+4z^4}.}
\]

In particular, \(B_{2j+1}=0\) for every integer \(j\geq0\), while \(B_{2j}\ne0\) for every \(j\geq0\). The even-level values satisfy

\[
B_0=1,\quad B_2=-2,\qquad B_{2j+4}=B_{2j+2}-4B_{2j},
\]

and, for every integer \(j\geq1\), \(B_{2j}\equiv2\pmod4\). If

\[
\alpha=\frac{1+i\sqrt{15}}2,\qquad c=\frac{3+i\sqrt{15}}6,
\]

then the exact closed form and sharp normalized oscillation are

\[
\boxed{B_{2j}=2\operatorname{Re}(c\alpha^j),\qquad
\limsup_{L\to\infty}\frac{B_L}{2^{L/2}}=\sqrt{\frac83},\qquad
\liminf_{L\to\infty}\frac{B_L}{2^{L/2}}=-\sqrt{\frac83}.}
\]

Thus square and nonsquare nonzero residues of \(s(n)\) modulo five have exactly equal counts on every odd-depth dyadic row, but a provably nonzero, oscillating discrepancy of sharp square-root scale on the even-depth rows. Divisible-by-five values contribute zero to both sides.

## Assumptions and scope

Stern’s sequence is specified by \(s(0)=0\), \(s(1)=1\), \(s(2n)=s(n)\) for \(n\geq1\), and \(s(2n+1)=s(n)+s(n+1)\) for \(n\geq1\). The theorem holds over the integers for **every** \(L\geq0\); it concerns the full half-open block of indices from \(2^L\) inclusive to \(2^{L+1}\) exclusive. No probabilistic averaging, presumed random residue behavior, or numerical approximation is part of the theorem.

## Proof

**Finite-state reduction.** Let \(\mathcal U=(\mathbb F_5)^2\setminus\{(0,0)\}\), a set of \(24\) ordered pairs. The coprimality of consecutive Stern values ensures their reductions lie in \(\mathcal U\); alternatively, both child maps below are invertible, so they preserve \(\mathcal U\) starting at \((1,1)\). Every pair of consecutive Stern values \((a,b)=(s(n),s(n+1))\) at a dyadic level has two children with residues

\[
\ell(a,b)=(a,a+b),\qquad r(a,b)=(a+b,b)\pmod5.
\]

Let \(T\) be the \(24\times24\) integer matrix with entry \(T_{u,v}=\mathbf1_{u=\ell(v)}+\mathbf1_{u=r(v)}\) using any fixed common order of \(\mathcal U\). Set \(e\) to be the column unit vector at \((1,1)\), and \(h_u=\chi_5(a)\) for \(u=(a,b)\). Exact propagation of the dyadic Stern blocks yields

\[
B_L=h^{\mathsf T}T^Le\qquad(L\geq0).
\]

**Finite exact certificate and infinite extension.** Define the scalar sequence

\[
D_j=h^{\mathsf T}(T^4-T^2+4I)T^je
=B_{j+4}-B_{j+2}+4B_j.
\]

The standalone standard-library integer checker `verify.py` explicitly constructs all \(24\) states and both child maps, and checks by exact integer arithmetic that \(D_j=0\) for each of the **24 integers** \(0\leq j<24\). It independently checks initial values \(B_0=1\), \(B_1=0\), \(B_2=-2\), \(B_3=0\). The sequence \(D_j\) is a fixed linear functional of powers of the *same* \(24\times24\) matrix \(T\); the Cayley–Hamilton theorem therefore gives a monic linear recurrence of order at most \(24\) for \(D_j\). Twenty-four consecutive vanishing initial values force \(D_j=0\) for **all** \(j\geq0\). This proves the recurrence without extrapolating experimental values.

The recurrence and four initial values give

\[
(1-z^2+4z^4)\sum_{L\geq0}B_Lz^L=1-3z^2.
\]

The resulting generating function has only even powers; hence \(B_{2j+1}=0\). For \(j\geq1\), the even subsequence recurrence reduces modulo four to \(B_{2j+4}\equiv B_{2j+2}\pmod4\), and \(B_2=-2\equiv2\pmod4\). Thus no even-level sum vanishes; also \(B_0=1\ne0\).

**Sharpness.** The even subsequence \(b_j=B_{2j}\) obeys \(b_{j+2}=b_{j+1}-4b_j\), whose characteristic roots are \(\alpha=(1+i\sqrt{15})/2\) and its complex conjugate, each of modulus \(2\). Solving from \(b_0=1,b_1=-2\) gives \(b_j=c\alpha^j+\overline{c\alpha^j}\) for the stated \(c\), with \(2|c|=\sqrt{8/3}\). Write \(\alpha=2e^{i\theta}\), so \(\cos\theta=1/4\). The number \(\theta/\pi\) is irrational: otherwise \(e^{i\theta}\) is a root of unity, making \(2\cos\theta=1/2\) a rational algebraic integer, contrary to the fact that a rational algebraic integer is an integer. Therefore \(j\theta\pmod{2\pi}\) is dense, and \(b_j/2^j=2\operatorname{Re}(ce^{ij\theta})\) has limsup and liminf exactly \(\pm2|c|\). The odd levels contribute zero, so the same extrema hold when normalized over all \(L\).

## Verification

Run `python3 verify.py` in the directory containing the standalone file. It performs exact integer arithmetic only, constructs the \(24\)-state pair transition, checks the \(24\) matrix-scalar Cayley–Hamilton certificates required for the infinite proof, tests \(32\) state-propagated rows, and independently sums the recurrence-defined integer Stern values over \(14\) complete rows. The first sixteen exact sums are

\[
1,0,-2,0,-6,0,2,0,26,0,18,0,-86,0,-158,0.
\]

The finite certificate supports the infinite result **only in conjunction with** the stated Cayley–Hamilton argument; neither the direct enumeration nor the output log alone proves the theorem.

## Relationship to prior work

Reznick (2006, §§4–5) proved uniformity of consecutive Stern residue pairs modulo any integer, formulated the full finite-state matrix mechanism, and explicitly evaluated congruence examples modulo two and three. He also stated a recurrence for the divisibility-by-five marginal on dyadic prefixes. This theorem uses the same established mechanism and does **not** claim it as new. It instead evaluates the nonprincipal quadratic-character functional modulo five, giving exact odd-level cancellation, a nonvanishing even-level law, and the *sharp* oscillation constant. Reznick’s discussed difference of counts for residues one and four is a distinct functional from the present difference between residues \(\{1,4\}\) and \(\{2,3\}\).

Bettin, Drappeau and Spiegelhofer (first public 18 April 2017) studied the **real-valued logarithmic** statistical distribution of Stern values and its transfer operator. This motivates a complementary local, finite-field character statistic, rather than implying its finite-level values. Lansing (2013) studied size distributions of Stern values and binomial coefficients, not this quadratic-character block identity. The exact result also exceeds the asymptotic equidistribution conclusion alone: both the parity-perfect equality and the square-root oscillation constant require more information than an \(o(2^L)\) bound.

## Limitations

The theorem treats exactly the quadratic character modulo five on complete dyadic rows, not individual residue-frequency formulas, all characters, all moduli, or arbitrary non-dyadic prefixes. It is a self-reviewed proof with a transparent finite exact certificate; no independent audit has occurred. General finite-state techniques make related identities algorithmically derivable, and unpublished or implicit equivalent evaluations remain a priority risk, notably the class notes on Stern arithmetic mentioned in Reznick’s article. Numerical data are not treated as an independent infinite proof.

## References

1. B. Reznick, *Regularity properties of the Stern enumeration of the rationals*, arXiv:math/0610601 (first public 19 October 2006), §§4–5. https://arxiv.org/abs/math/0610601
2. S. Bettin, S. Drappeau, L. Spiegelhofer, *Statistical distribution of the Stern sequence*, arXiv:1704.05253 (first public 18 April 2017). https://arxiv.org/abs/1704.05253
3. J. Lansing, *Distribution of Values of the Binomial Coefficients and the Stern Sequence*, Journal of Integer Sequences 16 (2013). https://cs.uwaterloo.ca/journals/JIS/VOL16/Lansing/lansing3.pdf
