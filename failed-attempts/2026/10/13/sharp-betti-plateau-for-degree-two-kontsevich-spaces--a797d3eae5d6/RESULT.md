# Sharp Betti plateau for degree-two Kontsevich spaces
## Finding
For every integer
\[
n\ge2,
\]
let
\[
X_n=\overline{\mathcal M}_{0,0}(\mathbb P^{n-1},2)
\]
be the coarse Kontsevich space of unmarked genus-zero stable maps of degree two to \(\mathbb P^{n-1}\). Write
\[
b_{2k}(X_n)=\dim_{\mathbb Q}H^{2k}(X_n,\mathbb Q).
\]
Then all odd Betti numbers vanish, and the even Betti sequence is unimodal with exact height
\[
\boxed{
\max_k b_{2k}(X_n)=\left\lfloor\frac{3n^2}{8}\right\rfloor.
}
\]

The plateau is completely determined by \(n\bmod4\). If \(n\) is odd, the maximum occurs exactly at
\[
k=\frac{3n-5}{2},\qquad \frac{3n-3}{2}.
\]
If
\[
n\equiv0\pmod4,
\]
the maximum is unique and occurs at
\[
k=\frac{3n-4}{2}.
\]
If
\[
n\equiv2\pmod4,
\]
the maximum occurs at exactly three consecutive indices
\[
k=\frac{3n-6}{2},\qquad\frac{3n-4}{2},\qquad\frac{3n-2}{2}.
\]
Outside this plateau, the sequence is strictly increasing before it and strictly decreasing after it.

## Assumptions and scope
The ground field is \(\mathbb C\), and cohomology is rational singular cohomology. The source spaces are the projective coarse moduli spaces of degree-two stable maps. Their rational Poincare polynomial is the established formula
\[
P_n(q)=\sum_{k=0}^{3n-4}b_{2k}(X_n)q^k
=\frac{(1-q^{n+1})(1-q^n)(1-q^{n-1})}{(1-q)^2(1-q^2)},
\]
where \(q=t^2\). This formula is the sole non-elementary input.

## Proof
Put
\[
a_k=b_{2k}(X_n),\qquad a_{-1}=0,
\]
and define first differences
\[
d_k=a_k-a_{k-1}.
\]
Multiplying the known Poincare polynomial by \(1-q\) gives
\[
(1-q)P_n(q)=
\frac{(1-q^{n-1})(1-q^n)(1-q^{n+1})}{(1-q)(1-q^2)}.
\]
The coefficient of \(q^j\) in
\[
\frac1{(1-q)(1-q^2)}
\]
is
\[
c(j)=\left\lfloor\frac j2\right\rfloor+1
\]
for \(j\ge0\), and is zero for \(j<0\). Before degree \(2n-1\), no product of two numerator shifts can contribute, so
\[
d_k=c(k)-c(k-n+1)-c(k-n)-c(k-n-1).
\]
This range contains the entire increasing half of the palindromic polynomial.

For
\[
0\le k\le n-2,
\]
we have
\[
d_k=c(k)>0.
\]
Now write
\[
k=n-1+s.
\]
If \(n=2m+1\) is odd, direct substitution gives
\[
d_{n-1+s}=m-s.
\]
Thus there is exactly one zero first difference, at \(s=m\), which creates a two-term central plateau. Summing the positive differences to the plateau gives
\[
\max a_k
=m(m+1)+\frac{m(m+1)}2
=\frac{3m(m+1)}2
=\left\lfloor\frac{3(2m+1)^2}{8}\right\rfloor.
\]

If \(n=2m\) is even, substitution gives
\[
d_{n-1+s}=m-1-2\left\lfloor\frac s2\right\rfloor.
\]
When \(m\) is even, none of the central first differences is zero, so the maximum is unique. When \(m\) is odd, precisely two consecutive first differences vanish, producing a three-term plateau. The initial block contributes
\[
\sum_{k=0}^{2m-2}c(k)=m^2.
\]
Adding the remaining positive differences gives
\[
\max a_k=\left\lfloor\frac{3m^2}{2}\right\rfloor
=\left\lfloor\frac{3n^2}{8}\right\rfloor.
\]

Finally, the displayed Poincare polynomial is palindromic of degree \(3n-4\). Hence its first half determines the second half by symmetry, proving strict decrease after the stated plateau and completing the unimodality classification.

## Verification
The bundled checker expands the rational Poincare polynomial exactly for every
\[
2\le n\le300,
\]
using integer polynomial arithmetic. It verifies palindromicity, vanishing of odd cohomology in the source formula, the exact maximum \(\lfloor3n^2/8\rfloor\), the residue-class plateau locations, and strict monotonicity away from the plateau.

The checker also verifies the symbolic first-difference formulas throughout their stated range. These finite computations are regression evidence only; the all-\(n\) result is proved by the coefficient calculation above.

## Relationship to prior work
Getzler and Pandharipande calculate the Betti numbers of genus-zero stable-map spaces to projective space in all degrees by Serre-characteristic methods. Kiem and Moon give, for degree two, the explicit closed Poincare polynomial used here and identify it with the earlier Getzler--Pandharipande calculation. Their degree-two theorem also gives the rational cohomology ring and a blow-up description.

The inspected sources state the Poincare polynomial and Betti-number computation, but they do not state unimodality, the exact largest Betti number, or the residue-class classification of the central plateau. Targeted searches using the stable-map notation, largest-Betti terminology, unimodality, and the exact value \(\lfloor3n^2/8\rfloor\) did not locate an equivalent statement.

## Limitations
The theorem concerns only unmarked degree-two maps to projective space. It does not assert an analogous extremal law for marked spaces, higher degree, Grassmannian targets, integral cohomology, or ring multiplication.

The originality conclusion is relative to the inspected and searched literature. Since the coefficient analysis is elementary once the closed Poincare polynomial is known, an unindexed equivalent observation remains a residual bibliographic risk.

## References
E. Getzler and R. Pandharipande, *The Betti numbers of* \(\overline{\mathcal M}_{0,n}(r,d)\), arXiv:math/0502525, first submitted 24 February 2005; *Journal of Algebraic Geometry* 15 (2006), 709--732, DOI 10.1090/S1056-3911-06-00425-5.

Y.-H. Kiem and H.-B. Moon, *Moduli space of stable maps to projective space via GIT*, arXiv:0711.4929, first submitted 30 November 2007; *International Journal of Mathematics* 21 (2010), 639--664, DOI 10.1142/S0129167X10006264.
