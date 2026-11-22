# A one-degree Milnor-algebra jump in the characteristic-three MacLane arrangement

## Finding
Let \(k\) be an algebraically closed field of characteristic three, let \(S=k[x,y,z]\) with standard grading, and define the eight-line MacLane arrangement by
\[
F=x(x-z)(x+z)y(y-z)(y+z)(x-y)(-x+y+z).
\]
Write \(J_F=(F_x,F_y,F_z)\) and \(M_F=S/J_F\). Its **minimal graded free resolution** is
\[
0\longrightarrow S(-13)\longrightarrow S(-10)\oplus S(-12)^2
\longrightarrow S(-7)^3\longrightarrow S\longrightarrow M_F\longrightarrow0.
\]
In particular, the three minimal homogeneous Jacobian syzygies have degrees \(3,5,5\), and their single minimal relation has coefficient-degree pattern \(3,1,1\). Compare the MacLane arrangement over characteristic zero, whose known minimal graded free resolution is
\[
0\longrightarrow S(-12)\longrightarrow S(-11)^3
\longrightarrow S(-7)^3\longrightarrow S\longrightarrow M_{\mathbb C}\longrightarrow0.
\]
The corresponding Hilbert series satisfy the unusually sharp relation
\[
\boxed{H_{M_F}(T)-H_{M_{\mathbb C}}(T)=T^{10}.}
\]
Thus their graded dimensions agree in every degree **except degree ten**, where the dimensions are respectively \(37\) and \(36\). Both arrangements have the identical labeled intersection lattice: eight ordinary triple intersections and four ordinary double intersections, with total local Tjurina number \(36\). This is an exact characteristic-dependent global Jacobian-module distinction, not a change of incidence combinatorics.

## Assumptions and scope
Take the Nazir–Yoshinaga normal form over \(\mathbb Z[t]/(t^2-t+1)\), with the eight line forms
\[
x,\quad x-z,\quad x-tz,\quad y,\quad y-z,\quad y-tz,\quad x-y,\quad tx+y-tz.
\]
Over characteristic zero, \(t\) is either complex root of \(t^2-t+1\). Over characteristic three its unique reduction is \(t=-1\); multiplying individual linear forms by units gives the displayed \(F\). The claim concerns this fixed labeled eight-line projective divisor and its unsaturated homogeneous gradient ideal, not a universal assertion about all eight-line arrangements. The symbol \(M_{\mathbb C}\) denotes either characteristic-zero conjugate; both share the known resolution. No characteristic-two or other special-reduction assertion is made.

## Proof
**Unchanged incidence.** For each of the \(\binom83=56\) distinct triples of line coefficient vectors in the integral quadratic normal form, take its determinant and reduce modulo \(t^2-t+1\). Exactly eight determinants vanish. Every other determinant has algebraic norm \(\pm1\), hence remains nonzero in every residue characteristic. All eight line vectors remain pairwise nonproportional in characteristic three. Therefore there are exactly eight ordinary triple points and \(\binom82-3\cdot8=4\) ordinary double points; there are no larger multiple points. Their Tjurina lengths are \(4\) and \(1\), totaling \(36\).

**The cubic syzygy.** Every line form \(\ell\) has coefficients in \(\mathbb F_3\), so the Frobenius vector field \(\Theta=x^3\partial_x+y^3\partial_y+z^3\partial_z\) satisfies \(\Theta(F)=hF\), where \(h=\sum_{i=1}^{8}\ell_i^2\). Euler's vector field \(E\) satisfies \(E(F)=8F=2F\) in characteristic three. Consequently \(\Theta-2hE\) annihilates \(F\), yielding a degree-three Jacobian syzygy \(U\). Exact homogeneous linear algebra over \(\mathbb F_3\) shows that the syzygy dimensions in degrees \(0,1,2,3,4,5\) are respectively \(0,0,0,1,3,8\). Hence \(U\) is the unique primitive syzygy through degree four, and there are precisely two new minimal degree-five syzygies.

**Integral presentation in characteristic three.** The companion certificate `verify.py` exhibits explicit quintic triples \(B,C\), checks \(U,B,C\) annihilate the gradient, and checks the polynomial syzygy
\[
(xy^2-y^3+y^2z-yz^2)U+(x+y-z)B+zC=0.
\]
The vectors \(B,C\) are linearly independent modulo the six quadratic multiples of \(U\). The coefficient triple in the displayed relation is primitive because \(x+y-z\) and \(z\) are coprime. Moreover \(U,B\) are independent over the fraction field; thus every relation among the three generators is a multiple of the displayed primitive relation. This gives a submodule of the gradient syzygies with presentation
\[
0\to S(-6)\to S(-3)\oplus S(-5)^2\to N\to0.
\]
Here the shifts use syzygy-coefficient degrees, before the gradient's degree-seven shift.

**Exhaustion and exact Hilbert series.** An exact degree-reverse-lexicographic Gröbner basis over \(\mathbb F_3\) for the ideal \(J_F\) has leading monomial exponent triples
\[
(1,9,1),(0,9,2),(2,7,1),(3,5,1),(1,6,2),
(3,3,2),(4,3,0),(5,1,1),(5,0,2).
\]
The monomial-ideal lcm inclusion–exclusion identity gives the exact Hilbert-series numerator
\[
(1-T)^3H_{M_F}(T)=1-3T^7+T^{10}+2T^{12}-T^{13}.
\]
This equals the Hilbert numerator obtained from the displayed three-generator/one-relation syzygy presentation after shifting by seven. The inclusion of that presentation into the full gradient-syzygy module therefore has zero Hilbert-series quotient, hence is an equality. This proves the claimed minimal free resolution. The characteristic-zero resolution follows from Malara–Pokora–Tutaj-Gasińska, Proposition 2.1, specialized to their \(n=3\) MacLane arrangement. Its Hilbert numerator is \(1-3T^7+3T^{11}-T^{12}\). Subtracting yields precisely \(T^{10}(1-T)^3\), and division by \((1-T)^3\) proves the one-degree assertion.

## Verification
Run `python verify.py` with SymPy version at least 1.13. The script checks all three exact syzygies, their primitive relation, their degree-five independence, the absence of smaller syzygies, the nine reduced Gröbner leading monomials, the full Hilbert numerator, the difference of Hilbert functions, and all \(56\) labeled triple determinants in the quadratic integral model. It prints `MACLANE_CHAR3_INTEGRAL_SYZYGY_HILBERT_VERIFIED_OK`. Exact finite-field and integer-arithmetic operations are used; the Gröbner step is an exact symbolic calculation, not a finite-degree extrapolation.

## Relationship to prior work
Nazir–Yoshinaga provide the eight-line equation and identify the two characteristic-zero realization-space components; these facts are input, not novel claims. Malara–Pokora–Tutaj-Gasińska identify the MacLane case of a nearly-free family and determine its characteristic-zero minimal Milnor-algebra resolution; that result is used as the comparator. Earlier observations that the MacLane arrangement is representable in characteristic three are not claimed as new. The specific characteristic-three minimal free resolution, complete Hilbert numerator, and isolated degree-ten defect are the present contribution. Comparison has been made with general positive-characteristic logarithmic-derivation results and other characteristic-dependent arrangement syzygies, which do not directly imply the exact values above.

## Limitations
The result concerns one natural integral model and its characteristic-three specialization; it does not establish that the same syzygy jump occurs for all arithmetic models of the abstract matroid or for different primes. The term *Milnor algebra* here means the graded quotient by the unsaturated homogeneous gradient ideal, not a local Milnor-number invariant. Its characteristic-zero comparison uses a published theorem rather than a newly proved characteristic-zero resolution. No exhaustive historical priority claim or independent verification is made. Exact computations are reproducible with the bundled script.

## References
1. S. Nazir and M. Yoshinaga, *On the connectivity of the realization spaces of line arrangements*, arXiv:1009.0202 (first submitted September 1, 2010); published in Annali della Scuola Normale Superiore di Pisa 11 (2012), Example 4.3. https://arxiv.org/abs/1009.0202 ; https://www.numdam.org/article/ASNSP_2012_5_11_4_921_0.pdf
2. G. Malara, P. Pokora and H. Tutaj-Gasińska, *On 3-syzygy and unexpected plane curves*, Geometriae Dedicata 214 (2021), Proposition 2.1 and Section 6. https://doi.org/10.1007/s10711-021-00602-5
