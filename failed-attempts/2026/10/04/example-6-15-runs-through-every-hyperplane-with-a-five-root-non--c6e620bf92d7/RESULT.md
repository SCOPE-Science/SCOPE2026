# Example 6.15 runs through every hyperplane, with a five-root non-LCD locus
## Finding

Consider the family from Bartoli--Grimaldi--Stănică Example 6.15,
\[
\phi_\rho(x)=\rho x+x^4,
\qquad
C_\rho=\operatorname{im}\phi_\rho\subseteq\mathbb F_{64},
\]
viewed as an \(\mathbb F_4\)-linear code in the three-dimensional trace space
\[
V=\mathbb F_{64}
\]
with pairing
\[
\langle x,y\rangle=\operatorname{Tr}_{\mathbb F_{64}/\mathbb F_4}(xy).
\]

The source proves that \(\phi_\rho\) is singular exactly when
\[
\rho^{21}=1.
\]
For these \(21\) singular parameters, the corresponding image codes are not merely \(21\) rank-two examples: they are exactly all \(21\) hyperplanes of \(V\), each occurring once.

More precisely, if \(0\ne y\in\ker\phi_\rho^\dagger\), then
\[
\rho=y^{15},
\qquad
C_\rho=y^\perp.
\]
The projective map
\[
[y]\longmapsto y^{15}
\]
is a bijection from \(\operatorname{PG}(2,4)\) to the subgroup
\[
\{\rho\in\mathbb F_{64}^{\times}:\rho^{21}=1\}.
\]

Under this bijection, \(C_\rho\) is non-LCD exactly when
\[
\operatorname{Tr}_{\mathbb F_{64}/\mathbb F_4}(y)=0.
\]
Hence the non-LCD hyperplanes are the five points of the projective trace-zero line, and the five non-LCD parameters are exactly the roots of
\[
\rho^5+\rho^4+1=0.
\]
Over \(\mathbb F_2\),
\[
\rho^5+\rho^4+1
=
(\rho^2+\rho+1)(\rho^3+\rho+1).
\]
Thus two of the five parameters are the nontrivial elements of \(\mathbb F_4^\times\), while the other three form one Frobenius orbit of order-\(7\) elements.

## Assumptions and scope

The result concerns exactly the normalized one-parameter family
\[
\phi_\rho(x)=\rho x+x^4
\]
from Example 6.15, with \(q=4\), \(m=3\), and \(k=1\). The point at infinity in the full parameter line corresponds to a nonzero scalar multiple of the identity and is LCD.

The trace pairing is the relative trace pairing over \(\mathbb F_4\). The argument uses the source's adjoint identity
\[
\phi_\rho^\dagger(y)=\rho y+y^{16}
\]
and its identity
\[
(\operatorname{im}\phi_\rho)^\perp=\ker\phi_\rho^\dagger.
\]

The statement that the \(21\) singular images exhaust all hyperplanes is about labeled \(\mathbb F_4\)-subspaces of \(V\), not equivalence classes under an ambient semilinear group.

## Proof

For a singular parameter, the source gives
\[
\rho^{21}=1
\]
and
\[
\dim_{\mathbb F_4}\ker\phi_\rho^\dagger=1.
\]
A nonzero \(y\) lies in the adjoint kernel exactly when
\[
\rho y+y^{16}=0,
\]
which in characteristic two is equivalent to
\[
y^{15}=\rho.
\]

Multiplication by an element \(a\in\mathbb F_4^\times\) does not change \(y^{15}\), because
\[
a^{15}=(a^3)^5=1.
\]
Conversely, if \(y^{15}=z^{15}\), then
\[
(y/z)^{15}=1.
\]
Since \(\mathbb F_{64}^\times\) has order \(63\),
\[
\gcd(15,63)=3,
\]
so the kernel of the fifteenth-power map has exactly three elements. Those are precisely \(\mathbb F_4^\times\). Therefore \(y^{15}\) depends only on the projective point \([y]\), and distinct projective points give distinct parameters.

There are
\[
\frac{4^3-1}{4-1}=21
\]
points of \(\operatorname{PG}(2,4)\), matching the \(21\) singular parameters. Hence
\[
[y]\longmapsto \rho=y^{15}
\]
is a bijection.

By the source's adjoint theorem,
\[
(\operatorname{im}\phi_\rho)^\perp
=
\ker\phi_\rho^\dagger
=
\langle y\rangle_{\mathbb F_4}.
\]
Nondegeneracy of the trace pairing then gives
\[
C_\rho=\operatorname{im}\phi_\rho=y^\perp.
\]
As \([y]\) runs through all projective points, \(y^\perp\) runs through all hyperplanes exactly once.

The hull of a hyperplane \(y^\perp\) is
\[
y^\perp\cap\langle y\rangle_{\mathbb F_4}.
\]
It is one-dimensional exactly when
\[
\langle y,y\rangle
=
\operatorname{Tr}_{64/4}(y^2)
=
0.
\]
In characteristic two,
\[
\operatorname{Tr}_{64/4}(y^2)
=
\operatorname{Tr}_{64/4}(y)^2,
\]
so this is equivalent to
\[
\operatorname{Tr}_{64/4}(y)=0.
\]
The trace-zero space has \(\mathbb F_4\)-dimension \(2\), hence contains exactly
\[
\frac{4^2-1}{4-1}=5
\]
projective points. This already explains the source's five non-LCD singular images.

It remains to eliminate \(y\). The trace-zero equation is
\[
y+y^4+y^{16}=0.
\]
For \(y\ne0\), division by \(y\) gives
\[
1+y^3+y^{15}=0.
\]
Put
\[
t=y^3.
\]
Then \(t^{21}=1\) and
\[
\rho=y^{15}=t^5.
\]
Because \(5^{-1}\equiv17\pmod{21}\),
\[
t=\rho^{17}=\rho^{-4}.
\]
Thus the trace-zero condition becomes
\[
1+\rho^{-4}+\rho=0,
\]
or equivalently
\[
\rho^5+\rho^4+1=0.
\]

Conversely, every root of this polynomial in \(\mathbb F_{64}\) is singular because
\[
\rho^5+\rho^4+1
=
(\rho^2+\rho+1)(\rho^3+\rho+1),
\]
whose roots have multiplicative order \(3\) or \(7\), hence satisfy \(\rho^{21}=1\). Reversing the preceding bijection shows that its corresponding normal point has trace zero. Therefore the polynomial cuts out exactly the five non-LCD parameters.

## Verification

`artifacts/verify.py` uses only the Python standard library and realizes
\[
\mathbb F_{64}=\mathbb F_2[a]/(a^6+a+1),
\]
where \(a\) has multiplicative order \(63\).

The verifier enumerates all \(64\) field elements and checks that:

- exactly \(21\) nonzero parameters satisfy \(\rho^{21}=1\);
- each singular image has \(16\) elements, hence \(\mathbb F_4\)-dimension \(2\);
- the \(21\) singular images are pairwise distinct;
- for every singular \(\rho\), the nonzero adjoint-kernel elements form one \(\mathbb F_4^\times\)-orbit and satisfy \(y^{15}=\rho\);
- each image equals the trace-orthogonal hyperplane \(y^\perp\);
- the \(21\) images equal the complete set of projective hyperplanes;
- exactly five have nonzero hull;
- those five parameters are exactly the roots of \(\rho^5+\rho^4+1\); and
- the full projective family has \(60\) LCD points and \(5\) non-LCD points.

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Bartoli, Grimaldi, and Stănică prove the general adjoint description of these hulls and, in Example 6.15, identify the \(21\) singular parameters by \(\rho^{21}=1\). Their exhaustive SageMath computation reports \(60\) LCD points and \(5\) non-LCD points, lists the five exceptional field elements in one primitive-element representation, and verifies total isotropy computationally for those five parameters.

The source does not identify the singular image family with the full projective dual plane, nor does it give the representation-independent equation
\[
\rho^5+\rho^4+1=0
\]
for the non-LCD locus. The projective-normal bijection explains why there are exactly \(21\) distinct singular image hyperplanes and why exactly five of them are non-LCD, without exhaustive parameter testing.

Focused searches using the source identifier, Example 6.15, the exact polynomial, the hyperplane interpretation, the trace-zero formulation, and equivalent parameter descriptions did not locate a prior statement of this same structural classification. The closest published hull results found concern different code families and do not imply the projective bijection or the five-root equation.

## Limitations

This result is a structural refinement of one finite worked example. It does not assert that an analogous projective-hyperplane bijection holds for arbitrary \(q\), \(m\), and \(k\).

The source already establishes the numerical count \(60\) LCD and \(5\) non-LCD points. The new contribution is the exact geometry and closed polynomial description of the exceptional locus, not a new count.

The factorization of the exceptional polynomial distinguishes one particular Frobenius orbit of three order-\(7\) elements; it does not include all six elements of order \(7\) in \(\mathbb F_{64}^{\times}\).

## References

1. Daniele Bartoli, Giovanni Giuseppe Grimaldi, and Pantelimon Stănică, *On the hull of linearized polynomial codes*, arXiv:2604.23097v1, first public version 25 April 2026; DOI 10.3934/amc.2026.101087.
2. Rudolf Lidl and Harald Niederreiter, *Finite Fields*, 2nd ed., Cambridge University Press, 1997.
