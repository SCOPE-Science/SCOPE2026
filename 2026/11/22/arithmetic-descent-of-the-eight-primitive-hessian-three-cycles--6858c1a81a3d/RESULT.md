# Arithmetic descent of the eight primitive Hessian three-cycles

## Finding

Write \(j\) for the modular invariant of an elliptic curve and put \(x=j/1728\). Over \(\mathbb Q\), the classical Hessian map on the moduli line becomes
\[
h(x)=\frac{(4-x)^3}{27x^2}:\mathbb P^1\longrightarrow\mathbb P^1.
\]
Its exact-period-three locus consists of 24 reduced geometric points grouped into eight unordered three-cycles. Although the total number eight is known, these cycles have the following arithmetic descent partition:

* Two three-cycles form one Galois orbit and have minimal fields of definition \(\mathbb Q(\sqrt{-3})\).
* Another two three-cycles form a second Galois orbit, again with minimal field \(\mathbb Q(\sqrt{-3})\).
* The remaining four three-cycles form one Galois orbit; each has a minimal degree-four field defined by a root of
\[
G(z)=z^4+420z^3+57456z^2+174528z+269568.
\]
The normal closure of each such quartic cycle field has Galois group \(D_4\), of order eight. In particular **none of the eight geometric three-cycles descends as an unordered three-element set to \(\mathbb Q\)**. The individual periodic points have degrees \(6,6,12\) in three respective rational irreducible blocks.

## Assumptions and scope

All statements concern the rational moduli self-map \(h\) over characteristic zero, not an equality of chosen cubic equations or twists. A three-cycle is the unordered set \(\{x,h(x),h^2(x)\}\) of a point of *exact* period three; its field of definition is the minimal field over which this unordered reduced set is stable under absolute Galois. The projective point \(\infty\) is fixed and is excluded. The invariant \(j=0\) is not periodic. The result concerns the finite reduced geometric period-three scheme and its quotient by the iteration action, not other periods or all postcritical points.

## Proof

1. Define the three explicit polynomials
\[
\begin{aligned}
F_1(x)={}&x^6+84x^5+11040x^4-47936x^3+204288x^2-33792x+4096,\\
F_2(x)={}&19x^6+912x^5+18240x^4-54272x^3+47616x^2+3072x+4096,\\
F_3(x)={}&37x^{12}+15540x^{11}+2026416x^{10}-30549568x^9\\
&+86526720x^8+656409600x^7+378470400x^6\\
&-4591042560x^5+6717505536x^4-4462477312x^3\\
&+1588592640x^2+25165824x+16777216.
\end{aligned}
\]
Exact rational-function composition and polynomial cancellation give
\[
\operatorname{numerator}(h^3(x)-x)\ \doteq\ (x-1)(7x^2+4x+16)F_1(x)F_2(x)F_3(x),
\]
where \(\doteq\) means equality up to a nonzero rational scalar in reduced form. The denominator is coprime to the numerator. The first two factors describe the three finite fixed points of \(h\). Since three is prime, every root of the remaining factors has exact period three. Their degrees sum to 24. Infinity is the fourth fixed point of the degree-three map. Every factor is separable, as shown in Step 2.

2. Each of \(F_1,F_2,F_3\) remains irreducible modulo five, of degrees \(6,6,12\), respectively. This is an exact irreducibility certificate over \(\mathbb F_5\): after making each polynomial monic, verify \(x^{5^n}\equiv x\pmod F\) and \(\gcd(F,x^{5^{n/\ell}}-x)=1\) for every prime \(\ell\mid n\), where \(n=6\) or \(12\). The attached verifier performs all these tests by finite-field polynomial arithmetic. Therefore these factors are irreducible and separable over \(\mathbb Q\), and the 24 roots are exactly the primitive period-three points.

3. Let \(s(x)=x+h(x)+h^2(x)\), constant on every unordered three-cycle. Polynomial modular inversion in each \(\mathbb Q[x]/(F_i)\) gives the exact congruences
\[
\begin{aligned}
 s^2+84s+10512&\equiv0\pmod{F_1},\\
 s^2+48s+1008&\equiv0\pmod{F_2},\\
 s^4+420s^3+57456s^2+174528s+269568&\equiv0\pmod{F_3}.
\end{aligned}
\]
The two quadratic polynomials have discriminants \(-3\cdot108^2\) and \(-3\cdot24^2\). The quartic \(G\) is irreducible modulo five. In each block of degree \(3r\), its cycle-sum minimal polynomial has degree \(r\) (respectively \(r=2,2,4\)). Each sum consequently occurs at exactly three roots. Those three roots are precisely one cycle, because \(h\) preserves the sum and each orbit has size three. Thus the cycle sum distinguishes all cycles and generates the full field of definition of each unordered cycle. The two quadratic blocks descend over \(\mathbb Q(\sqrt{-3})\), while the last block has degree-four cycle fields. In particular, no sum is rational, so no cycle descends to \(\mathbb Q\).

4. The quartic \(G\) has discriminant
\[
\operatorname{disc}(G)=2^{24}3^{20}7^2\cdot37\cdot211^2.
\]
Its cubic resolvent is
\[
R(w)=(w-288)(w^2-57168w+55759104).
\]
Hence the quartic's Galois group is contained in a dihedral subgroup \(D_4\subset S_4\). The irreducible reduction of \(G\) modulo five supplies a four-cycle, while its squarefree factorization pattern \((1,1,2)\) modulo seven supplies a transposition. No proper transitive subgroup of this dihedral group contains both; therefore its Galois group is exactly \(D_4\). This identifies the normal closures of the degree-four cycle fields.

## Verification

Run `python verify.py` in an environment with SymPy. The verifier recomputes the rational-function identity, checks coprimality of the defining numerator and denominator, performs Rabin irreducibility tests modulo five, derives the three cycle-sum congruences in exact polynomial quotient rings, and verifies the discriminants, cubic resolvent and modulo-seven factor pattern. Expected final token: `HESSIAN_PERIOD3_EIGHT_CYCLE_DESCENT_VERIFIED`.

The argument is exact and finite. No numerical approximation or point sampling is used to establish the infinite-field assertions. The modular irreducibility certificates prove irreducibility over \(\mathbb Q\), not just irreducibility over a finite sample field.

## Relationship to prior work

The Hessian rational map is classical and is explicitly computed in Popescu-Pampu (2008) and Mula–Pintore–Taufer (first public version 2024). Kettinger (first public version 2024) establishes the general complex orbit-count formula and gives explicit period-two examples. In particular the existence of eight complex three-cycles is **not** claimed as new. The narrower statement here is the full arithmetic Galois-orbit partition of those eight unordered cycles, their exact minimal fields of definition, and the dihedral normal closure of the four-cycle component. None of those three explicit descent assertions was identified in the inspected relevant sections of the sources below. The Lattès structure in Mula–Pintore–Taufer provides a broader conceptual framework, but does not by itself state these particular number-field calculations.

## Limitations

This is a classification of degree-three periodic-orbit descent on the rational \(j\)-line in characteristic zero; it is not a classification of fields of definition of *plane cubic models* realizing prescribed orbits, nor of higher periods. Only the cycle-field quartic Galois closure is explicitly identified; no complete Galois-group statement is needed or claimed for the degree-12 point polynomial. Historical priority has been checked against named full-text primary sources and available mathematical records; an unindexed equivalent calculation may exist. Independent mathematical validation has not been performed.

## References

1. M. Mula, F. Pintore and D. Taufer, *The Hessian of elliptic curves as a Lattès map*, first public arXiv posting 2024-07-24, https://arxiv.org/abs/2407.17042 . Relevant material: Sections 2.2, 3, 6 and 7.
2. J. Kettinger, *The dynamics of the Hesse derivative on the j-invariant*, first public arXiv posting 2024-08-07, https://arxiv.org/abs/2408.04117 . Relevant material: Sections 3.1, 3.2 and 4.1 of the 2026 revision.
3. P. Popescu-Pampu, *Iterating the Hessian: a dynamical system on the moduli space of elliptic curves and dessins d'enfants*, first public arXiv posting 2008-09-25, https://arxiv.org/abs/0809.4340 .
