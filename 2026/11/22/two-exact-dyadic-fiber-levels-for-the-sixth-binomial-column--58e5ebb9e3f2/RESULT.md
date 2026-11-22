# Two exact dyadic fiber levels for the sixth binomial column

## Finding
For integers \(k\geq1\) and residues \(y\in\mathbb Z/2^k\mathbb Z\), put
\[
F(n)=\binom n6,\qquad
N_k(y)=\#\{0\leq n<2^{k+2}:F(n)\equiv y\pmod{2^k}\}.
\]
The least period of \(F(n)\pmod{2^k}\) is \(2^{k+2}\). At the first level, \(N_1(0)=6\) and \(N_1(1)=2\). At every level \(k\geq2\), the entire fiber law is
\[
\boxed{N_k(y)=2+8\,\mathbf1_{y\equiv0\pmod4}.}
\]
In particular, every target occurs, precisely one quarter of targets have ten preimages per least period, and the other three quarters have two. The pushforward of normalized Haar measure on \(\mathbb Z_2\) by \(F\) is exactly the half-and-half mixture of normalized Haar measure on \(\mathbb Z_2\) and normalized Haar measure on \(4\mathbb Z_2\).

## Assumptions and scope
The binomial polynomial \(F(x)=x(x-1)\cdots(x-5)/720\) is regarded as an integer-valued continuous function on the two-adic integers. Ordinary binomial values at \(0\leq n<6\) are zero. All target counts are taken in a *single least period*, not in a growing Pascal triangle with both indices varying. No statement is made about binomial columns other than the sixth or about odd prime powers.

## Proof
**The twofold triangular map.** Set
\[
w(n)=\frac{(n-2)(n-3)}2.
\]
The two polynomial branches are
\[
w(2v)=(v-1)(2v-3),\qquad w(2v+1)=(v-1)(2v-1).
\]
Each is congruent to \(v+1\pmod2\), and its difference at \(v\) and \(v'\) is \((v-v')\) times an odd two-adic unit. Hence each is an isometry (and therefore a bijection) of \(\mathbb Z_2\), and induces a permutation modulo every power of two. Consequently the map from \(n\pmod{2^{k+2}}\) to \(w(n)\pmod{2^{k+1}}\) has exactly two preimages of every \(w\).

**Exact cubic factorization.** Direct multiplication gives
\[
w-1=\frac{(n-1)(n-4)}2,\qquad
w-3=\frac{n(n-5)}2,
\]
so
\[
F(n)=P(w(n)),\qquad P(w)=\frac{w(w-1)(w-3)}{90}.
\]
For every \(w\in\mathbb Z_2\), its numerator is even; thus \(P\) is two-adically integral. The denominator has two-adic valuation one, so \(P(w)\pmod{2^k}\) depends only on \(w\pmod{2^{k+1}}\).

**Even cubic branch.** For \(w=2u\),
\[
P(2u)=A(u):=\frac{u(2u-1)(2u-3)}{45}.
\]
The polynomial \(A(u)\) has an odd coefficient of \(u\), while all its higher-degree coefficients are even two-adic integers. Thus \(A(u)-A(v)=(u-v)\times\text{(odd two-adic unit)}\), and \(A\) induces a bijection modulo \(2^k\). For each \(y\), there is exactly one even \(w\pmod{2^{k+1}}\) satisfying \(P(w)\equiv y\pmod{2^k}\).

**Odd cubic branch.** For \(w=2u+1\),
\[
P(2u+1)=4B(u),\quad
B(u)=\frac{(2u+1)u(u-1)}{2\cdot45}.
\]
Splitting \(u\) into even and odd arguments gives the integral-polynomial branches
\[
B(2v)=C_0(v):=\frac{v(4v+1)(2v-1)}{45},\qquad
B(2v+1)=C_1(v):=\frac{v(4v+3)(2v+1)}{45}.
\]
As with \(A\), each \(C_i\) has an odd linear coefficient and even higher coefficients, so each is a two-adic isometry and a permutation at every finite level. For \(k\geq2\), there are no odd-\(w\) solutions if \(y\not\equiv0\pmod4\). If \(y\equiv0\pmod4\), the congruence reduces to \(B(u)\equiv y/4\pmod{2^{k-2}}\). There are two solutions \(v\pmod{2^{k-1}}\) in each of the two branches \(u=2v\) and \(u=2v+1\); this gives four odd-\(w\) solutions modulo \(2^{k+1}\). For \(k=1\), both odd-\(w\) residues modulo \(4\) map to zero.

Multiplying the total counts of \(w\)-solutions by the proved factor two for \(n\mapsto w\) yields exactly the stated fiber formulas. Passing to the compatible inverse-limit measures gives the displayed Haar-mixture identity.

**Least period.** Since \(w(n+2^{k+2})\equiv w(n)\pmod{2^{k+1}}\), the length \(2^{k+2}\) is a period. It cannot be shortened to \(2^{k+1}\): at \(n=2\), one has \(F(2)=0\) and
\[
w(2+2^{k+1})=2^k(2^{k+1}-1),
\quad \nu_2(P(w(2+2^{k+1})))=k-1,
\]
since \(w-1\) and \(w-3\) are odd. Any proper period would divide \(2^{k+1}\), so the least period is exactly \(2^{k+2}\).

## Verification
The standalone script `check.py` performs exact integer checks of the cubic factorization for 494 inputs, independently checks all three branch permutations at moduli \(2^j\) for \(1\leq j\leq9\), and exhaustively verifies all target multiplicities and the least-period obstruction for \(1\leq k\leq11\). These finite checks are supplementary; the proofs above establish the statements for all \(k\).

## Relationship to prior work
Fiorot, Gilblas, and Tonolo (first publicly posted 2023-07-05) establish the general connection between constant-sequence primitives and fixed binomial columns and derive their prime-power periods (Proposition 3.4); the period used here is therefore not claimed as new. Their subsequent algorithms primarily count zeros and valuation layers in specified digit patterns, rather than an all-target sixth-column fiber law. Nguyen's generating-polynomial treatment concerns residue classes modulo the maximal ideal (the prime level) and not every dyadic level. Barat and Grabner investigate asymptotic spatial distributions over variable pairs of binomial indices, not this single fixed column and its exact least-period multiplicities. The full dyadic fifth-column fiber law and the published ternary sixth-column image theorem concern genuinely different parameters and do not imply the present fixed-column dyadic theorem through their stated conclusions.

## Limitations
No optimality or universality across binomial columns is claimed. The statement is proved internally from elementary two-adic isometries; independent mathematical audit has not been performed. Equivalent unpublished or poorly indexed exact sixth-column fiber classifications could exist, and the accessible historical bibliography is not exhaustive.

## References
- L. Fiorot, R. Gilblas, A. Tonolo, *Modular binomials with an application to periodic sequences*, arXiv:2307.02366 (first posted 2023-07-05), especially §§3–5, https://arxiv.org/abs/2307.02366.
- D. Q. N. Nguyen, *On the generating polynomials for the distribution of generalized binomial coefficients in discrete valuation domains*, arXiv:2006.07423 (2020), especially Theorem 3.6, https://arxiv.org/abs/2006.07423.
- G. Barat and P. J. Grabner, *Spatial Equidistribution of Binomial Coefficients Modulo Prime Powers*, Uniform Distribution Theory **11** (2016), 151–161, https://doi.org/10.1515/udt-2016-0017.
- R. Garfield and H. S. Wilf, *The distribution of the binomial coefficients modulo \(p\)*, Journal of Number Theory **41** (1992), 1–5, https://doi.org/10.1016/0022-314X(92)90078-4.
