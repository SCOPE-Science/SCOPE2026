# A binary-digit parity law and the mod-four Walsh spectrum of Catalan matroid bases

## Finding

For every integer \(n\geq1\), let \(\mathcal D_n\subseteq\mathbb F_2^{2n}\) be the up-step incidence vectors of all Dyck paths of semilength \(n\), with step positions indexed \(t=0,\ldots,2n-1\). Write \(C_n=\binom{2n}{n}/(n+1)\), \(s_2(m)\) for binary digit sum, \(N_{n,t}=|\{u\in\mathcal D_n:u_t=1\}|\), and
\[
W_n(b)=\sum_{u\in\mathcal D_n}(-1)^{\langle b,u\rangle},\qquad b\in\mathbb F_2^{2n}.
\]
Define the following explicit set of positions \(I_n\):

* If \(n+1=2^a\) for an integer \(a\geq1\), put \(I_n=\{0,\ldots,2^a-2\}\).
* If \(n+1=2^a+2^b\), with integers \(a>b\geq0\), put \(I_n=\{2^{b+1}-1,\ldots,2^{a+1}-2\}\).
* Otherwise, put \(I_n=\varnothing\).

Then \(N_{n,t}\) is odd **if and only if** \(t\in I_n\). In particular, **every** Walsh multiplier is determined modulo four by
\[
\boxed{W_n(b)\equiv C_n-2\sum_{t\in I_n}b_t\pmod4.}
\]
If \(s_2(n+1)=1\), all Walsh multipliers are odd, hence unnormalized convolution by \(\mathbf 1_{\mathcal D_n}\) on \(\mathbb F_2^{2n}\) is invertible. If \(s_2(n+1)=2\), exactly \(2^{2n-1}\) frequencies have multipliers congruent to two modulo four, and the other half have multipliers divisible by four; consequently the convolution rank is at least \(2^{2n-1}\). If \(s_2(n+1)\geq3\), all multipliers are divisible by four. More precisely, for \(s_2(n+1)=1,2,3\) the two-adic valuation of the gcd of the complete set of multipliers is, respectively, \(0,1,2\). No assertion is made about odd factors of that gcd or higher dyadic layers when \(s_2(n+1)\geq4\).

## Assumptions and scope

The group is \(\mathbb F_2^{2n}\) with coordinatewise addition and its standard character pairing. A Dyck path has \(n\) up-steps and \(n\) down-steps, never goes below height zero, and returns to zero. The Fourier transform and convolution are **unnormalized**. The statement is uniform in all \(n\geq1\) and all \(2^{2n}\) Walsh frequencies; no probabilistic approximation is involved. Position indices in the statement are zero-based.

## Proof

Work first in \(\mathbb F_2[[x,y]]\). Write
\[
C(z)=\sum_{m\geq0} C_m z^{2m},\qquad C(z)=1+z^2C(z)^2.
\]
The latter equation and uniqueness of the series solution with constant coefficient one give
\[
C(z)=\sum_{a\geq0}z^{2^{a+1}-2}\quad\text{in characteristic two}.
\]
Let \(F(x,y)\) count a Dyck path with one of its up-steps marked, with \(x\) recording the number of preceding steps and \(y\) the number of following steps. Explicitly,
\[
F(x,y)=\sum_{n\geq1}\sum_{t=0}^{2n-1}(N_{n,t}\bmod2)x^t y^{2n-1-t}.
\]
Use the unique first-return decomposition \(UADB\), where \(A\) and \(B\) are Dyck paths and \(D\) matches the initial up-step \(U\). If \(U\) is marked, the contribution is \(yC(y)^2\). If the mark lies in \(A\), the contribution is \(xyC(y)F(x,y)\); if in \(B\), it is \(x^2C(x)F(x,y)\). Therefore
\[
F(x,y)=\frac{yC(y)^2}{1+xyC(y)+x^2C(x)}.
\]
The denominator has constant coefficient one. From \(x^2C(x)^2=C(x)+1\) and \(y^2C(y)^2=C(y)+1\), direct multiplication gives the formal-series identity
\[
\boxed{(x+y)F(x,y)=xyC(x)C(y)+C(y)+1.}
\]
Indeed, upon multiplying its right-hand side by \(1+xyC(y)+x^2C(x)\), all terms cancel in pairs except \((x+y)yC(y)^2\); the two Catalan identities above are the only reductions used.

Put \(e_a=2^{a+1}-1\), for \(a\geq0\). Substituting the lacunary series for \(C\) gives
\[
(x+y)F(x,y)=\sum_{a,b\geq0}x^{e_a}y^{e_b}+\sum_{a\geq0}y^{2e_a}.
\]
The diagonal term \(x^{e_a}y^{e_a}+y^{2e_a}\), divided by \(x+y\), equals \(y^{e_a}\sum_{t=0}^{e_a-1}x^t y^{e_a-1-t}\). Its total degree corresponds to \(n=e_a=2^{a+1}-1\), and gives precisely \(t=0,\ldots,n-1\). For distinct \(a>b\), the paired terms \(x^{e_a}y^{e_b}+x^{e_b}y^{e_a}\), divided by \(x+y\), equal
\[
\sum_{t=e_b}^{e_a-1}x^t y^{e_a+e_b-1-t}.
\]
Their total degree corresponds to \(n=2^a+2^b-1\), and the position interval is \(t=2^{b+1}-1,\ldots,2^{a+1}-2\). A positive integer has at most one representation as either a single binary power or a sum of two distinct binary powers. The displayed intervals therefore give **all** odd marginal counts without cancellation between cases. This proves \(N_{n,t}\equiv\mathbf1_{I_n}(t)\pmod2\).

For arbitrary \(b\), the integer identity \((-1)^j=(1-2)^j\) yields
\[
W_n(b)=\sum_{u\in\mathcal D_n}\prod_{t:b_t=1}(1-2u_t)
\equiv C_n-2\sum_{t:b_t=1}N_{n,t}\pmod4,
\]
which proves the complete mod-four formula. The known Catalan valuation \(\nu_2(C_n)=s_2(n+1)-1\) follows from the binomial formula and Legendre's factorial valuation formula. When \(s_2(n+1)=2\), \(I_n\ne\varnothing\), so precisely half the frequency vectors give even intersection parity; these multipliers are congruent to two modulo four and cannot vanish. The other cases follow from the valuation formula and the fact that \(W_n(0)=C_n\). In particular, the exact valuation of the gcd through three binary digits is inferred **only** from universal divisibility and this coefficient at zero, not from an unproved odd-part gcd claim.

## Verification

The standalone `verify_dyck_fourier.py` implements two independent finite tests. Integer dynamic programming checks the parity of every positional up-step count for semilengths one through one hundred. A separate explicit Dyck-path enumeration followed by an integer Walsh–Hadamard transform tests all frequencies for semilengths one through ten (1,398,100 Fourier coefficients in total), including their predicted residues modulo four. These checks completed with marker `DYCK_POSITION_PARITY_AND_MOD4_PASS`. The all-length claim rests on the formal-power-series proof above, not on extrapolating finite computations.

## Relationship to prior work

Ardila introduced the Catalan matroid using exactly these Dyck up-step sets and studied its bases, Tutte polynomial and representability [1]. Postnikov and Sagan established a more general Catalan two-adic valuation theorem for **height-dependent** ascent weights and recalled the classical identity \(\nu_2(C_n)=s_2(n+1)-1\) [2]. The present formula instead identifies the parity of every **position-dependent** single-step inclusion count and consequently the complete position-character Walsh transform **modulo four**. The proof explicitly uses the classical Catalan parity and valuation inputs; it does not claim these classical facts as new.

## Limitations

This theorem determines the full transform only modulo four; it does not determine which coefficients divisible by four vanish, their real magnitudes, or the exact convolution rank in the two-or-more-bit cases. It provides only a lower bound for the rank in the two-bit case. The exact odd part of the gcd, higher two-adic valuations, and independent mathematical validation are not addressed. Earlier equivalent marked-Dyck-path congruences in less searchable sources cannot be ruled out conclusively.

## References

1. Federico Ardila, *The Catalan matroid*, arXiv:math/0209354, first public submission September 25, 2002; https://arxiv.org/abs/math/0209354.
2. Alexander Postnikov and Bruce E. Sagan, *What power of two divides a weighted Catalan number?*, arXiv:math/0601339, first public submission January 13, 2006; https://arxiv.org/abs/math/0601339.
