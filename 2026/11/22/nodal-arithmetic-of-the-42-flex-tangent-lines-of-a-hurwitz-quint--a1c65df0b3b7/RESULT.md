# Nodal arithmetic of the 42 flex-tangent lines of a Hurwitz quintic in characteristic five

## Finding
Let \(C\subset\mathbb P^2_{\mathbb F_5}\) be the smooth Hurwitz quintic
\[
C:\quad XY^4+YZ^4+X^4Z=0.
\]
Let \(\mathcal L\) be the reduced union, over an algebraic closure, of the tangent lines at all points of \(C\) having tangent contact order at least three. **All 42 such tangent lines are distinct, and no three are concurrent.** Thus the reduced line arrangement \(\mathcal L\) has exactly \(\binom{42}{2}=861\) geometric singular points, all ordinary nodes. Its absolute fifth-power Frobenius permutation on these nodes has cycle type
\[
1^3\,3^4\,6^3\,12^{69}.
\]
Equivalently, the zero-dimensional reduced singular-support scheme has zeta function
\[
Z_{\operatorname{Sing}(\mathcal L)_{\mathrm{red}}}(T)=
\frac{1}{(1-T)^3(1-T^3)^4(1-T^6)^3(1-T^{12})^{69}}.
\]
All lines and all nodes become rational over \(\mathbb F_{5^{12}}\); a common smaller extension does not suffice. The three rational nodes are precisely the three coordinate flex points, each lying on two of the three coordinate flex tangents. The 39 other flex points lie on exactly their own flex tangents.

## Assumptions and scope
Everything takes place over \(\mathbb F_5\), with geometric points and concurrency evaluated over \(\overline{\mathbb F}_5\). The curve is a plane curve of degree five and genus six. A flex tangent means the unique projective tangent at a smooth point where the intersection multiplicity is at least three. An ordinary node of a reduced union of lines means the transverse meeting of exactly two distinct geometric lines. The zeta function is for the reduced finite singular-support scheme, not for the quintic or the entire line union.

## Proof
**1. Complete flex support.** The curve is smooth because its Hurwitz parameter \(n=4\) satisfies \(5\nmid n^2-n+1=13\), as in Arakelian–Borges–Speziali, Theorem 3.6. Their flex formula gives the three coordinate hyperflexes of contact four, together with exactly 39 ordinary flexes of contact three, parametrized by
\[
(t:\lambda t^4:1),\quad
\lambda^3+\lambda^2-2\lambda-1=0,\qquad
t^{13}=-\frac{\lambda+1}{\lambda^4}.
\]
The cubic has no root in \(\mathbb F_5\), hence three distinct roots in \(\mathbb F_{125}\). For each, the right-hand side is nonzero and the thirteenth-power equation has 13 distinct roots. There are no further flex points by that theorem. Independently, the direct Hessian identity
\[
\det\operatorname{Hess}(XY^4+YZ^4+X^4Z)
=-64(3X^7Y^2-29X^3Y^3Z^3+3X^2Z^7+3Y^7Z^2)
\]
provides an elementary check of the flex equations in characteristic five.

**2. Exact splitting field and line Frobenius.** Put \(s=t^{13}\). Reduction modulo the displayed cubic yields
\[
s=\lambda^2-2\lambda+1,\quad
s^3+2s-1=0,\quad
\lambda=4+4s+2s^2\pmod5.
\]
Consequently the non-coordinate flex abscissas satisfy \(t^{39}+2t^{13}-1=0\), with 39 distinct roots. Since \(\gcd(13,5^3-1)=1\), each of the three conjugate \(\lambda\)'s has exactly one associated \(t\) in \(\mathbb F_{125}\). For the remaining twelve thirteenth roots in each fibre, fifth-cubed Frobenius acts via exponent \(5^3\equiv8\pmod {13}\), of multiplicative order four. The absolute Frobenius therefore has one cycle of length three and three of length twelve on the 39 ordinary flexes, while fixing the three coordinate hyperflexes. Their distinct tangent lines inherit the same cycle type \(1^3\,3\,12^3\).

**3. Complete geometric line-incidence certificate.** The accompanying dependency-free exact verifier constructs the field \(\mathbb F_{5^{12}}=\mathbb F_5[u]/(P(u))\), where
\[
P(u)=u^{12}+2u^{11}-u^{10}+2u^9+u^7-2u^6+u^5-2u^3+u^2-2u+1.
\]
Its degree-twelve irreducibility is certified by the Rabin test: \(u^{5^{12}}\equiv u\pmod P\) and the two gcds \(\gcd(P,u^{5^4}-u)=\gcd(P,u^{5^6}-u)=1\). The verifier constructs one flex \((u:\lambda u^4:1)\), a primitive thirteenth root \(\zeta\), and its complete 39-point orbit under diagonal transformations
\[
(X:Y:Z)\mapsto(\zeta^{-3}X:\zeta Y:Z)
\]
and coordinate cycling \((X:Y:Z)\mapsto(Y:Z:X)\), adding the three coordinate hyperflexes. It independently checks all 42 points against the quintic and checks distinctness.

For each point \((x:y:z)\), the tangent line is the linear form with coefficients
\[
(F_X,F_Y,F_Z)=(y^4+4x^3z,\ 4xy^3+z^4,\ 4yz^3+x^4).
\]
The verifier checks that the 42 projective coefficient triples are distinct. For each of their \(\binom{42}{2}=861\) unordered pairs, it computes the exact projective cross product and finds 861 different intersection points. As an independently organized check, it evaluates the determinant of every unordered triple of tangent-line coefficient vectors: all \(\binom{42}{3}=11480\) determinants are nonzero. Because every geometric flex tangent is represented over the proved splitting field, the test is exhaustive over the algebraic closure, not merely a rational-point experiment. All intersections are therefore transverse double points.

**4. Frobenius on nodes.** In a simple arrangement, nodes correspond bijectively and equivariantly to unordered pairs of lines. Starting with line permutation \(1^3\,3\,12^3\), the induced permutation on its 861 unordered pairs has three fixed pairs, four 3-cycles, three 6-cycles, and 69 12-cycles. One can check the 12-cycle tally by splitting pairs into fixed–12 (nine cycles), 3–12 (nine), within each 12-cycle (five per cycle, hence fifteen), and between two distinct 12-cycles (twelve per pair of cycles, hence thirty-six): \(9+9+15+36=69\). The three 6-cycles come from opposite pairs within each 12-cycle. This gives the asserted zeta function and minimal common splitting extension.

## Verification
Run `python3 verify_hurwitz_flex_arrangement.py` using only the Python 3 standard library. It verifies the finite-field modulus by a polynomial gcd irreducibility test; constructs and checks all 42 distinct flex points and tangent lines; checks 861 distinct pair intersections and all 11480 independent triple determinants; and computes the fifth-power Frobenius orbits on the lines and nodes. Its successful terminal line is:

`HURWITZ_F5_FLEX_ARRANGEMENT_VERIFIED lines=42 double_points=861 triple_points=0 triples_tested=11480 frobenius=1^3,3^4,6^3,12^69`

The proof reduces the infinite geometric assertion to a genuinely exhaustive finite calculation through the established complete flex parametrization and the proved common splitting field. No probabilistic or time-limited search is used.

## Relationship to prior work
Arakelian, Borges and Speziali (2018 preprint; 2021 journal publication) give the complete geometric flex support and the automorphism group of general Hurwitz curves. These are used as inputs, not claimed anew. Their relevant theorem and follow-up sections do not compute the full incidence lattice of the 42 tangent lines for this specific reduction, the absence of triple concurrence, or the Frobenius spectrum of its 861 nodes. The published computation for the 72 flex tangents of a different Hessian-invariant sextic concerns another curve and shows that many higher-order concurrence points can occur. A characteristic-five Klein quartic calculation concerns a different degree-four curve, not this genus-six quintic. The claim is about complete line arrangement incidence and descent, not merely a specialization of an existing flex-point count.

## Limitations
The result is specific to the displayed quintic over characteristic five; no analogous assertion is made for arbitrary Hurwitz exponents, other characteristics, or the complex fibre. The symbolic computation is exact and rerunnable, but no formal proof-assistant certificate is supplied. An equivalent unindexed historical line-arrangement computation cannot be excluded by the bounded literature searches. The zeta function refers only to reduced nodes, not the arrangement's full cohomology or the quintic's Hasse–Weil polynomial.

## References
- N. Arakelian, H. Borges and P. Speziali, *The Hurwitz curve over a finite field and its Weierstrass points for the morphism of lines*, arXiv:1811.09224v1 (first public 22 November 2018), Theorem 3.6 and Section 4; later *Finite Fields and Their Applications* 73 (2021), 101842, DOI:10.1016/j.ffa.2021.101842.
- *The 72 flex tangents of the Hessian-invariant sextic form an arrangement with 12 sixfold points, 216 triple points and 1728 nodes*, publicly indexed mathematical comparison record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-72-flex-tangents-of-the-hessian-invariant-sextic-form-an-arr--094d1c44685b.
- *Frobenius splitting of the characteristic-five Klein quartic's flex triangles*, publicly indexed mathematical comparison record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-frobenius-splitting-of-the-characteristic-five-klein-quartic-s-f--07295989c49b.
