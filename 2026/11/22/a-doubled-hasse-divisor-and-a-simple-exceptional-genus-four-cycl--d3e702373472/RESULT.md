# A doubled Hasse divisor and a simple exceptional genus-four cyclic-quintic Jacobian in characteristic \(31\)

## Finding

Let \(k=\overline{\mathbb F}_{31}\), let \((a,b)\in k^2\), and let \(C_{a,b}\) be the smooth projective curve associated to
\[
y^5=x^3+ax+b.
\]
Put \(\Delta=b^2-a^3\) and \(H=b^2-7a^3\). The smooth family is exactly \(\Delta\ne0\). On it, the Cartier--Manin coefficient matrix with respect to the basis given below satisfies
\[
\det M=14H^2\Delta^{12}\quad\text{in }\mathbb F_{31}[a,b].
\]
Its two-by-two trailing block has determinant \(-8\Delta^9\); its first two diagonal entries are \(4H\) and \(-14H\Delta^3\). Consequently the geometric Jacobian invariants are
\[
(31\text{-rank},a\text{-number})=\begin{cases}(4,0),&H\ne0,\\(2,2),&H=0,\end{cases}
\]
for every smooth geometric member. Scheme-theoretically the determinant divisor on the smooth parameter surface is \(2V(H)\), since \(H\) has no repeated irreducible factor.

The nonordinary locus is parametrized bijectively and scheme-theoretically by
\[
(a,b)=(u^2,10u^3),\qquad u\in k^{\times},
\]
since \(10^2=7\) in \(\mathbb F_{31}\), and \(H=\Delta=0\) only at \((a,b)=(0,0)\). In particular it has exactly \(q-1\) coefficient-marked smooth points over \(\mathbb F_q\) for each \(q=31^n\); the ordinary complement has \((q-1)^2\) points. Every exceptional curve becomes isomorphic over \(k\) to the distinguished rational model
\[
C:\quad y^5=x^3+x+10\quad\text{over }\mathbb F_{31}.
\]
For this specific rational model, and not necessarily every \(\mathbb F_{31}\)-twist, its zeta function is
\[
Z(C/\mathbb F_{31},T)=\frac{1+101T^2+4371T^4+97061T^6+923521T^8}{(1-T)(1-31T)}.
\]
The reciprocal Frobenius polynomial
\[
P(X)=X^8+101X^6+4371X^4+97061X^2+923521
\]
is irreducible over \(\mathbb Q\), and hence \(\operatorname{Jac}(C)\) is simple over \(\mathbb F_{31}\).

## Assumptions and scope

The ground field has characteristic \(31\), and \(C_{a,b}\) denotes the smooth projective normalization of its affine equation. All geometric invariants are over an algebraic closure. The stated finite-field counts count *marked affine coefficient pairs*, not geometric or arithmetic isomorphism classes. The cyclic cover has degree five over \(\mathbb P^1\) and four totally ramified geometric branch points (the three distinct roots of the cubic and infinity); the Riemann--Hurwitz formula gives genus four. In characteristic \(31\), the cubic discriminant is \(4(b^2-a^3)\), so precisely \(\Delta\ne0\) gives smooth curves of this type. The exact zeta function and simplicity are asserted for the displayed literal model over \(\mathbb F_{31}\); neither geometric simplicity nor identical zeta polynomials for its rational twists is asserted.

## Proof

**Cartier calculation.** A basis of regular differentials is
\[
\omega_1=dx/y^2,\quad\omega_2=dx/y^3,\quad\omega_3=dx/y^4,\quad\omega_4=x\,dx/y^4.
\]
At infinity the valuation of \(x^i dx/y^j\) is \(3j-5i-6\), nonnegative for these four forms. At a finite ramification point it is \(4-j\), also nonnegative. Four forms therefore give a full basis by genus. For a source form \(x^i dx/y^j\), the Cartier identity and \(31\equiv1\pmod5\) give the matrix entry in the target form \(x^k dx/y^j\) as the \(31\)-st root of
\[
[x^{31(k+1)-1-i}](x^3+ax+b)^{6j}.
\]
Entries between distinct \(j\) blocks vanish. Thus there are two scalar blocks for \(j=2,3\) and one two-dimensional block for \(j=4\). Direct exact multinomial coefficient expansion modulo \(31\) yields scalar coefficients \(4H\) and \(-14H\Delta^3\) and trailing block determinant \(-8\Delta^9\); the product is \(14H^2\Delta^{12}\). The accompanying `check_cartier.py` reconstructs all four by four entries as coefficient polynomials and checks every symbolic identity, without interpolating from finite samples.

Since \(\Delta\ne0\), the lower block and all of its Frobenius twists are invertible. When \(H=0\), the upper scalar blocks vanish identically, so the Cartier stable image has dimension two and the total Cartier rank is two; hence \(31\)-rank two and \(a\)-number two. When \(H\ne0\), every block is invertible, giving ordinary rank four and \(a\)-number zero. For \(H=0\), \(a\ne0\) on the smooth locus and \(u=b/(10a)\) is a two-sided inverse to the indicated parametrization, proving an isomorphism with \(\mathbb G_m\) and the counts. For \(a=u^2\), \(b=10u^3\), substitute \(x=uX\) and \(y=vY\) with \(v^5=u^3\) in \(k\), proving geometric isomorphism to \(C\).

**Weil numerator.** Two different irreducible polynomial presentations of \(\mathbb F_{31^n}\) for each \(1\le n\le4\) were used to count affine solutions directly, with the unique point at infinity. For a given \(x\), the right-hand side has one fifth-root when zero, five when a nonzero fifth power, and zero otherwise. The exact counts are:

| \(n\) | \(\#C(\mathbb F_{31^n})\) |
|---|---:|
| 1 | 32 |
| 2 | 1164 |
| 3 | 29792 |
| 4 | 920604 |

These give power sums \(\sum_i\alpha_i^n=31^n+1-\#C(\mathbb F_{31^n})\), namely \(0,-202,0,2918\). Newton's identities give the first four coefficients \(1,0,101,0,4371\), and the genus-four Weil functional equation supplies the remaining coefficients \(0,97061,0,923521\). `count_points.cpp`, `count_points_independent.cpp` and `check_fields.py` reproduce the field and point-count certificates.

**Arithmetic simplicity.** Modulo seven the displayed degree-eight polynomial factors into two irreducible quartics
\[
(X^4+3X^3-X^2-2X+2)(X^4-3X^3-X^2+2X+2).
\]
The irreducibility of each quartic modulo seven is checked by Rabin's polynomial gcd criterion in `check_weil.py`. Thus a proper factor over the rationals, if any, must be a monic integer quartic. Since every complex Frobenius root has modulus \(\sqrt{31}\), each quartic has constant term \(d=\pm961\), with the same sign in both factors. Write their coefficients as
\[
A=X^4+aX^3+bX^2+cX+d,\qquad B=X^4-aX^3+fX^2-cX+d.
\]
Coefficient comparison in degrees six and two gives \(b+f=101+a^2\) and \(d(b+f)-c^2=97061\). The negative choice of \(d\) is impossible, so \(d=961\) and \(c^2=961a^2\). Comparing degrees five and three gives \(a(f-b)=c(f-b)=0\). If \(a=c=0\), the equations \(b+f=101\), \(bf=2449\) have non-square discriminant \(405\). Otherwise \(f=b\), \(b=(101+a^2)/2\), and \(bf-2ac=2449\). For \(c=31a\), setting \(z=a^2\) leads to \(z^2-46z+405=0\), with non-square discriminant \(496\); for \(c=-31a\), it gives \(z^2+450z+405=0\), impossible for \(z\ge0\). Thus \(P\) is irreducible over \(\mathbb Q\). The Tate--Honda description of finite-field isogeny factors implies that its Jacobian is simple over \(\mathbb F_{31}\).

## Verification

In Python 3 and a standard C++17 compiler, execute in the directory containing the accompanying standalone sources:

```
python3 check_cartier.py
python3 check_fields.py
g++ -O3 -std=c++17 count_points.cpp -o count_points && ./count_points
g++ -O3 -std=c++17 count_points_independent.cpp -o count_points_independent && ./count_points_independent
python3 check_weil.py
```

The Cartier checker evaluates exact symbolic identities in \(\mathbb F_{31}[a,b]\) and also checks all 930 smooth \(\mathbb F_{31}\)-pairs. Both point counters agree on all four extension-field counts. The second uses different irreducible defining polynomials; it is an independent field presentation but similar source code, not an independent algorithm. A finite computation cannot replace the Cartier identities or the algebraic irreducibility argument; those proofs are given above.

## Relationship to prior work

The cyclic family with branch inertia \((1,1,1,2)\) is equivalent by changing its cyclic generator to Moonen's genus-four degree-five branch family with inertia \((1,3,3,3)\), treated in Li--Mantovan--Pries--Tang (2018). Their characteristic-dependent generic Newton strata already establish much of the structural background. Cavalieri--Pries (2023) give mass formulas for the nonordinary locus of one-dimensional cyclic-cover families, including this Moonen family; their mass and nonordinary-type results must not be rebranded as a new discovery of nonordinary curves. Lin--Mantovan--Singhal (2024) give broader existence results. The specific characteristic-31 equation of the marked Hasse divisor, the rational distinguished exceptional model, the exact degree-eight zeta numerator, and the proof of finite-field Jacobian simplicity are the claimed new combined arithmetic calculation; they were not located in the inspected primary texts or the checked published-result database. In particular the mass formula may already imply the number of geometric exceptional classes, so that numerical uniqueness alone is not asserted to be novel.

## Limitations

The special-fiber zeta computation uses exact finite fields through extension degree four and the Weil functional equation; it does not calculate arbitrary rational twists, their isomorphism classes over \(\mathbb F_{31}\), or geometric absolute simplicity. The exact algebraic computations are intrinsic, but priority uncertainty remains about specialized finite-field tables or unindexed earlier calculations. The source comparison does not prove absolute novelty. No separate independent mathematical audit has been performed.

## References

- Wanlin Li, Elena Mantovan, Rachel Pries, and Yunqing Tang, *Newton polygons arising for special families of cyclic covers of the projective line*, 2018, https://arxiv.org/abs/1805.06914.
- Renzo Cavalieri and Rachel Pries, *Mass formula for non-ordinary curves in one dimensional families*, first public preprint 2023-08-28, https://arxiv.org/abs/2308.14891.
- Wanlin Lin, Elena Mantovan, and Deepesh Singhal, *Non-\(p\)-ordinary smooth abelian covers of \(\mathbb P^1\)*, first public preprint 2024-06-13, https://arxiv.org/abs/2406.09632.
