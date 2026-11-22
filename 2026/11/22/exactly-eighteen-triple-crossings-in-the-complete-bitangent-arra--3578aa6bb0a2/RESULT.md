# Exactly eighteen triple crossings in the complete bitangent arrangement of the order-nine quartic

## Finding
Consider the smooth canonical genus-three plane quartic over \(\mathbb Q\)
\[
 C:\quad X^4+XY^3+YZ^3=0.
\]
Let \(\mathcal B\) denote the reduced union of all its geometric bitangent lines in \(\mathbb P^2\). Then \(\mathcal B\) has exactly 28 distinct line components, and its complete geometric singularity basket consists of **324 ordinary nodes** and **18 ordinary triple points**, with no points of multiplicity four or higher. The 18 triple points have two explicit nine-point loci:
\[
\begin{split}
 T_\infty&=\{[1:m:0]:m^9-96m^6+48m^3+64=0\},\\
 T_{\rm aff}&=\{[-1/(3d^2):d:1]:27d^9-4=0\}.
\end{split}
\]
The singular support thus has 342 geometric points. The sum of local delta invariants equals 378, and the arithmetic genus of the degree-28 union is 351.

## Assumptions and scope
All assertions concern the indicated coefficientwise quartic over a field of characteristic zero, with intersection multiplicities over an algebraic closure. A bitangent means a line with even intersection divisor of degree four; an undulation line is included. An ordinary triple point is the transverse intersection of three distinct lines. The result concerns the **singularities of the union of bitangent lines**, not the bitangent contact points on the quartic.

The plane transformation \([x:y:z]=[X:Z:-Y]\) identifies this quartic with the classical order-nine model \(y^3z=x(x^3-z^3)\). Smoothness of the displayed plane quartic follows directly from its partial derivatives \(4X^3+Y^3\), \(3XY^2+Z^3\), and \(3YZ^2\), which cannot vanish simultaneously in projective space.

## Proof
**1. Exhaustive equations for the 28 bitangents.** The hyperflex is \(Y=0\), meeting the quartic in \(4[0:0:1]\). Consider another line \(Y=mX+bZ\). In the chart \(Z=1\), substitution gives
\[
(1+m^3)X^4+3m^2bX^3+3mb^2X^2+(b^3+m)X+b.
\]
If \(1+m^3\ne0\) and \(m b\ne0\), a repeated quadratic must be \((1+m^3)(X^2+uX+v)^2\), with
\[
 u=\frac{3m^2b}{2(1+m^3)},\qquad v=\frac{3m(4+m^3)b^2}{8(1+m^3)^2}.
\]
Comparing the linear and constant coefficients and eliminating \(b^3\) yields the necessary and sufficient relations
\[
 H(m):=m^9-96m^6+48m^3+64=0,
\qquad (m^6+20m^3-8)b^3=8m(1+m^3)^2. \tag{1}
\]
The displayed quadratic-coefficient calculation and elimination are checked exactly by the attached program. The polynomial \(H\) is separable and relatively prime to \(m\), \(1+m^3\), and \(m^6+20m^3-8\). Hence there are nine distinct slopes \(m\), each giving three distinct nonzero intercepts \(b\), and all 27 associated lines are distinct. Direct substitution excludes \(m=0\) except \(Y=0\); \(m^3=-1\) gives odd intersection multiplicity at infinity. Lines \(X=cZ\), including \(X=0\), and \(Z=0\) are not bitangent, by their intersection divisors. Thus equation (1), plus \(Y=0\), lists every bitangent.

**2. Nine triples at infinity.** For a given \(m\), the three different intercepts \(b\) yield three lines meeting at \([1:m:0]\). The nine roots of \(H\) give nine distinct points. No other line of the list meets any of these points because its slope would have to be the same, and \(Y=0\) meets none of them.

**3. Nine finite triples.** Let \(d\) run through the nine distinct roots of \(27d^9-4\). The three roots of
\[
 g_d(m)=m^3-9d^3m^2+4
\]
are distinct; this follows because the discriminant is \(432(3d^3-1)(9d^6+3d^3+1)\), which is nonzero on \(27d^9=4\). Exact polynomial reduction modulo the ideal \((g_d(m),27d^9-4)\) gives \(H(m)=0\) and
\[
(m^6+20m^3-8)(3d^3+m)^3=216d^6m(1+m^3)^2.
\]
Consequently, with \(b=d+m/(3d^2)\), all three lines \(Y=mX+bZ\) belong to equation (1), and all pass through \([-1/(3d^2):d:1]\). Different \(d\) give distinct points, none on the line at infinity. Thus at least 18 distinct triples exist.

**4. Modular upper bound that applies in characteristic zero.** Specialize the full, separable 28-line list at the prime \(433\). The nine slope roots, 27 slope-intercept pairs, and nine \(d\)-roots all become distinct \(\mathbb F_{433}\)-rational solutions, with all required denominators nonzero. The complete finite-field pair-intersection census (not a sample) gives exactly 342 distinct projective intersection points, of which 324 lie on two lines and 18 lie on three; it finds no higher multiplicities. The 18 triples constructed above specialize to 18 **distinct** modular triples. If any three other geometric characteristic-zero bitangent lines were concurrent, their determinant would also vanish after reduction modulo a prime above 433; since the 28 lines reduce bijectively to 28 distinct lines, that would create another modular triple. This contradicts the exhaustive census. Hence the 18 known triples exhaust all characteristic-zero triple intersections and no higher intersection exists. All remaining pairs meet at distinct nodes. Pair counting gives \(\binom{28}{2}=324+3\cdot18=378\).

Each ordinary node contributes local \(\delta=1\) and each ordinary triple point contributes \(\delta=3\). The union has 28 rational components, so its arithmetic genus is \(378-28+1=351\), agreeing with \((28-1)(28-2)/2\).

## Verification
Execute `python3 verify_bitangent_arrangement.py` with Python 3 and SymPy. The program checks square-coefficient identities, polynomial gcd and Groebner elimination, distinctness of the finite triple roots, all 28 line equations and all 378 pair intersections at 433, an independent enumeration of 3-line determinant zeros, and the exact singularity/genus identities. Its success marker is `BITANGENT_28_LINE_18_TRIPLE_324_DOUBLE_CERTIFIED`. All tests are exact integer/rational or finite-field computations. The reduction argument in the proof, rather than a numerical extrapolation, converts the modular census into a characteristic-zero upper bound.

## Relationship to prior work
Liang (2019, Theorem 4.1 and the accompanying bitangent equations) computes all 28 bitangents of the order-nine quartic, including the ninth-degree slope equation. That **enumeration is preexisting**, and the present claim does not rename it as new. The earlier published level-two study identifies the three free nine-element bitangent automorphism orbits and associated theta structures, but does not classify concurrence of three or more bitangent lines. The Ciani-pencilled triple-concurrence classification concerns another curve family and does not imply the current isolated order-nine incidence basket. The new contribution is the complete singularity/intersection classification of this natural full bitangent union, with explicit two-stratum triple loci and a sharp modular certificate.

## Limitations
No claim of exhaustive historical priority is made. Older papers may encode the same 28-line arrangement under a different projective normalization or through an unlabeled incidence table; such possible coverage needs independent specialist assessment. The theorem is characteristic zero; the prime 433 is only an exact proof device, and its incidence profile is not asserted uniformly across all positive characteristics. Neither contact divisor arithmetic nor a family-wide classification is claimed.

## References
1. E. Badr and F. Bars, *On the automorphism group of non-singular plane curves fixing the degree*, first public arXiv posting 2015-03-03, arXiv:1503.01149 (earlier class-level context).
2. Dun Liang, *Invariants, Bitangents and Matrix Representations of Plane Quartics with 3-Cyclic Automorphisms*, arXiv:1902.02914, first posted 2019-02-08, Theorem 4.1 and equations of bitangents.
3. *The order-nine Picard quartic has level-two orbit profile \(1+9+9+9,\ 9^4,\ 9^7\)*, published geometric orbit calculation, 2026-10-13, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-the-order-nine-picard-quartic-has-level-two-orbit-profile-1-9-9--b8d8cc6b1ea4.
4. *Triple-concurrence discriminant of the Ciani quartic bitangents*, published 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-triple-concurrence-discriminant-of-the-ciani-quartic-bitangents--3c19cc0fc0c4.
