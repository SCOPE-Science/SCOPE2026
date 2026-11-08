# Geometric irreducibility of the quartic normal-bundle jumping divisor on a line blow-up

## Finding
Let \(k=\mathbb C\) and \(X=\operatorname{Bl}_{\mathbb P^1}\mathbb P^3\), where the centre is a line. Let \(U\) be the smooth, nonempty fixed-source parameter space of unramified maps \(f:\mathbb P^1\to X\) of degree four and exceptional intersection degree two, in the Cox description of Iwasaki [1, §6]. **The first normal-bundle jumping divisor is geometrically irreducible and reduced on \(U\).** More explicitly, the generic normal bundle is \(\mathcal O(6)^{\oplus2}\), and
\[
\mathcal J=\{f\in U:N_f\not\cong\mathcal O(6)^{\oplus2}\}
=V(\det\Theta_{\mathcal O(-7)}^1)\cap U
\]
with the natural determinantal scheme structure, is an integral effective Cartier divisor. Its class is \(8\zeta_u+4\zeta_v\), as already computed in [1, Proposition 6.7]. The new assertion is **integrality**; nonemptiness, the class and the existence of a smooth point are inputs from [1].

## Assumptions and scope
Work in characteristic zero. Homogeneous source coordinates are \([s:t]\). The Cox coordinates of a map are \(u_0,u_1\in H^0(\mathbb P^1,\mathcal O(4))\) and \(v_2,v_3,w\in H^0(\mathbb P^1,\mathcal O(2))\), subject to the honest-map and unramified open conditions described in [1, §6.1]. In particular \(v_2,v_3\) are coprime. The stated divisor is the determinant of the sixteen-dimensional cohomology morphism constructed in [1, Proposition 6.7 and Appendix A]. The full coefficient space is used for polynomial calculations; the conclusion is on \(U\), not on the boundary of its toric quasimap compactification.

For a binary form \(h(s,t)=\sum_{j=0}^e h_j s^{e-j}t^j\), define the \(a\times b\) Toeplitz matrix \(T(h;a,b)\), for \(e=b-a\ge0\), by \(T_{ij}=h_{j-i}\), taking out-of-range coefficients to be zero. In ordered source blocks of widths \((6,5,5)\), the two rows corresponding to each quartic \(u_i\) are \([0,T(\partial_su_i;2,5),T(\partial_tu_i;2,5)]\). The four rows corresponding to each quadratic \(v_j\) are \([T(v_j;4,6),T(\partial_sv_j;4,5),T(\partial_tv_j;4,5)]\); those for \(w\) replace the first block by its negative. Their concatenation is a \(16\times16\) matrix \(M\). The scheme \(\mathcal J\) is \(\det M=0\) on \(U\) [1, Appendix A.1].

## Proof
**1. A geometric parameter reduction.** The pair of coprime quadratic forms \((v_2,v_3)\) gives a separable degree-two morphism \(\mathbb P^1\to\mathbb P^1\). Over \(\mathbb C\), every such morphism is equivalent to \([s:t]\mapsto[s^2:t^2]\) under independent projective changes of source and target coordinates: use its two ramification points and two branch values. These changes preserve the jumping condition. Thus, for detecting components whose projection to the quadratic-form parameters is proper, it suffices to examine the normal form
\[
(v_2,v_3,w)=(s^2,t^2,As^2+Bst+Ct^2).
\]
For every nonzero triple \((A,B,C)\), at least one choice of \((u_0,u_1)\) makes \(\det M\ne0\). Indeed the following three choices give the exact determinants (the coefficient ring has characteristic zero):
\[
\begin{array}{c|c|l}
u_0&u_1&\det M/16384\\\hline
s^4&t^4&B^2(AC-B^2)\\
s^3t&st^3&-A^2C^2\\
s^4+t^4&s^3t+st^3&-(A^4+A^2B^2+2A^2C^2-2AB^2C+B^2C^2+C^4).
\end{array}
\]
If the first two determinants vanish, the triple lies on one of the coordinate axes \(A\ne0,B=C=0\) or \(C\ne0,A=B=0\), or is zero. The third determinant is nonzero at each nonzero axial triple. Consequently the full determinant does **not** vanish identically as a polynomial in the two quartics above any coprime quadratic pair with \(w\ne0\). The exceptional set \(w=0\) has codimension three in the quadratic coefficients, hence cannot support a vertical divisor.

**2. An absolutely irreducible coefficient fiber.** Choose the fixed quadratic triple
\[
(v_2,v_3,w)=(s^2+t^2,s^2+st,s^2+2st+3t^2).
\]
For the ten coefficients of \((u_0,u_1)\), restrict to the three-dimensional linear subspace described, modulo \(101\), by the successive coefficient vectors (in the basis \((x,y,z)\))
\[
(86,5,100),(66,15,65),(25,50,44),(67,37,74),(18,76,33),
(13,33,52),(41,34,13),(98,41,39),(2,72,79),(25,9,25).
\]
Direct evaluation of the published \(16\times16\) matrix, on fifteen triangular-grid points and polynomial interpolation, gives the homogeneous ternary quartic \(47F(x,y,z)\), where, modulo \(101\),
\[
\begin{aligned}
F={}&x^4-19x^3y-17x^3z+10x^2y^2+8x^2yz+38x^2z^2\\
&-22xy^3-12xy^2z-35xyz^2-27xz^3-22y^4+39y^3z\\
&+45y^2z^2+32yz^3-24z^4.
\end{aligned}
\]
Its projective singularities all lie in \(x\ne0\). On \(x=1\), the reduced Gröbner basis of the Jacobian ideal is
\[
\{y+41z^2+33z+40,\;z^3+25z^2-48z+15\}
\quad\text{over }\mathbb F_{101}.
\]
The cubic is squarefree; the Hessian determinant is coprime to it, so there are exactly three ordinary nodes over the algebraic closure. They are not collinear: the elements \(1,z,-41z^2-33z-40\) are linearly independent in the cubic quotient (coefficient determinant \(41\ne0\)). There are no singularities at \(x=0\), as both boundary charts have unit Jacobian ideal. A reduced plane quartic with only three ordinary nodes that are noncollinear is absolutely irreducible: two conics intersect in total multiplicity four, and a line-plus-cubic splitting with exactly three nodes would put the three nodes on that line; other decompositions force more intersection singularities. Thus \(F\) is geometrically integral over \(\mathbb F_{101}\). The specialized homogeneous quartic over \(\mathbb Q\) is geometrically integral as well, by flat specialization from a geometrically integral special fiber.

**3. Irreducibility of the divisor.** Let \(B\) denote the irreducible parameter space of coprime ordered quadratic pairs and a quadratic form \(w\), and let \(\mathbb P^9_B\) parameterize the two quartics. The determinant is a homogeneous polynomial of degree four in the ten quartic coefficients. Step 1 shows that it is not identically zero on any fiber over \(B\) with \(w\ne0\), so the associated family of projective quartic hypersurfaces is a relative effective Cartier divisor, flat over this open base. Step 2 exhibits a geometrically integral fiber; openness of geometric integrality for the projective flat family gives geometrically integral generic fiber. Hence there is a unique horizontal irreducible component, of multiplicity one. Any other divisor component would be vertical and project onto a divisor of \(B\), requiring the determinant to vanish identically in the quartic variables above its generic point. Step 1 excludes that over \(w\ne0\); \(w=0\) has codimension three. Therefore the determinantal divisor over the map space has exactly one reduced irreducible component. Restriction to the nonempty unramified open \(U\) retains integrality, and the published smooth point [1, Proposition 6.7] confirms that this restriction is nonempty. \(U\) is smooth and the determinant is an effective Cartier divisor [1], so the resulting divisor scheme is integral.

## Verification
Execute `python verify.py` with Python 3 and SymPy 1.14. The script computes the three exact nonvanishing determinant witnesses, verifies the entire ternary quartic identity by fifteen unisolvent evaluations, and checks the finite-field Jacobian Gröbner basis, the two infinity charts, squarefreeness, ordinary nodes, and noncollinearity. A successful replay prints `CERTIFICATE_OK`. These finite computations certify the explicit algebraic identities used in the all-parameter proof; they are not a substitute for the geometric argument in Step 3.

## Relationship to prior work
Iwasaki [1] proves that the general normal bundle is balanced, identifies the first jumping locus as a nonempty Cartier divisor, calculates its divisor class, and constructs a smooth point. The present claim strengthens that result to the assertion that the entire determinantal divisor on \(U\) is geometrically integral. Cela and Lian [2] determine normal-bundle behavior for general rational curves with secancy conditions; their generic-splitting/interpolation statements do not imply uniqueness of components of this particular jumping divisor. No uniqueness assertion about boundary components of the ambient quasimap compactification is made.

## Limitations
The proof is for complex curves. It does not classify deeper jumping strata, singularities of the jumping divisor, its compactified boundary, or the corresponding divisor in arbitrary positive characteristic. Historical priority is provisional. 

## References
[1] H. Iwasaki, *Normal Bundle Splitting Strata of Rational Curves in Toric Varieties*, arXiv:2609.39309v1 (submitted 2026-09-30), especially §6.4, Proposition 6.7, and Appendix A.1. https://arxiv.org/html/2609.39309

[2] A. Cela and C. Lian, *Interpolation for rational curves with secants*, arXiv:2607.01432v1 (submitted 2026-07-01). https://arxiv.org/abs/2607.01432
