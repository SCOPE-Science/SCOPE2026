# The sharp three-node Fourier volume gap for the sparse modes \(0,1,4\)

## Finding

Let \(z_1,z_2,z_3\) be any three points of the unit circle and let
\[
 M(z_1,z_2,z_3)=\begin{pmatrix}1&z_1&z_1^4\\1&z_2&z_2^4\\1&z_3&z_3^4\end{pmatrix}.
\]
There is a unique root \(\rho\in(3/4,4/5)\) of
\[
 4\rho^3+7\rho^2-4\rho-3=0.
\]
**Sharp unrestricted determinant theorem.** The exact optimal squared sampling volume is
\[
 \boxed{\max_{|z_1|=|z_2|=|z_3|=1}|\det M|^2
 =\rho^2(1-\rho)(1+\rho)^2(3+\rho)^3
 =22.90675193636629\ldots .}
\]
Equality holds **if and only if** the unordered sample set is, for some \(|\eta|=1\),
\[
 \boxed{\{z_1,z_2,z_3\}=\{\eta,\eta e^{i\vartheta},\eta e^{-i\vartheta}\},\qquad
 \cos\vartheta=-\frac{1+\rho}{2},\quad 0<\vartheta<\pi.}
\]
Thus the optimum is unique up to simultaneous rotation and permutation, and strictly below the orthogonal-volume ceiling \(27\). For the row-normalized matrix \(3^{-1/2}M\), the maximum squared determinant is the stated constant divided by \(27\), approximately \(0.8483982198654\).

**Arithmetic tightness boundary.** More generally, replace the three exponents by \(\{0,1,m\}\) for any integer \(m\ge2\), keeping three unit-circle sample nodes. A perfectly tight three-by-three sampling matrix exists if and only if \(m\equiv2\pmod3\). In that case and only then, the nodes of a tight design are a rotated equilateral triple and the sharp squared determinant is \(27\). In particular, \(m=4\) is the first sparse exponent with a degree-two Schur factor; its non-tight optimum has a genuinely two-variable phase-geometry trade-off.

## Assumptions and scope

The sampling nodes are unconstrained points on \(\mathbb T=\{z\in\mathbb C:|z|=1\}\), may initially coincide, and have no prescribed angular spacing. The determinant uses the unnormalized columns \(1,z,z^4\) evaluated at the three nodes. Equal sampling weights are implicit in this matrix; arbitrary weighting, oversampling, and condition-number optimization are not claimed. The determinant equals the product of the squared singular values of \(M\) and quantifies squared information volume, not the minimum singular value separately. The arithmetic boundary statement concerns the same number of samples as modes and the unweighted evaluation matrix.

The three modes may also be interpreted as an order-variable trigonometric polynomial \(P(t)=c_0+c_1e^{it}+c_4e^{4it}\) evaluated at three arbitrary orders. This is a **scalar** measurement problem; it is not a claim that a full function-valued fractional Fourier transform requires three samples to invert.

## Proof

**1. Algebraic reduction.** Put \(S=z_1+z_2+z_3\), \(P=z_1z_2+z_2z_3+z_3z_1\), and \(Q=z_1z_2z_3\). The alternant/Schur factorization gives
\[
 \det M=\prod_{1\le i<j\le3}(z_j-z_i)\,(S^2-P).
\]
A simultaneous rotation multiplies the determinant by a unit modulus number. Rotate so that \(Q=1\). Since every node has modulus one, now \(P=\overline S\). Write \(r=|S|\in[0,3]\) and, for \(r>0\), \(u=\operatorname{Re}(S^3)/r^3\in[-1,1]\). At \(r=0\) the determinant vanishes. The cubic whose roots are the nodes is \(X^3-SX^2+\overline S X-1\). Its discriminant, together with \(Q=1\), gives
\[
 \left|\prod_{i<j}(z_j-z_i)\right|^2
 =27-18r^2-r^4+8r^3u.
\]
Moreover, \(|S^2-\overline S|^2=r^4+r^2-2r^3u\). Consequently
\[
 |\det M|^2=F(r,u)
 :=(27-18r^2-r^4+8r^3u)(r^4+r^2-2r^3u).
\tag{1}
\]
Every actual triple gives \(0\le r\le3\) and \(-1\le u\le1\). Maximizing the right side over that entire rectangle therefore gives an upper bound on the genuine maximum, even if certain rectangle points do not represent triples.

**2. Maximize the auxiliary angle.** For fixed \(r>0\), expression (1) is strictly concave quadratic in \(u\), with unconstrained vertex
\[
 u_*(r)=\frac{5r^4+22r^2-27}{16r^3}.
\]
Let \(r_-\) be the unique positive root of \(5r^4+16r^3+22r^2-27=0\), and \(r_+\) the unique positive root of \(5r^4-16r^3+22r^2-27=0\). Both defining polynomials are strictly increasing on the positive axis: for the second the derivative is \(4r(5r^2-12r+11)>0\). Exact rational substitution yields
\[
 \frac56<r_-<1,\qquad \frac85<r_+<\frac95.
\]
The optimal auxiliary angle is \(u=-1\) on \((0,r_-]\), \(u=u_*(r)\) on \([r_-,r_+]\), and \(u=1\) on \([r_+,3]\). In these three ranges the maximal values are, respectively,
\[
 F_-(r)=r^2(1-r)(1+r)^2(3+r)^3,\quad
 F_0(r)=\frac{(3r^4-14r^2+27)^2}{16},\quad
 F_+(r)=r^2(3-r)^3(r-1)^2(r+1).
\tag{2}
\]
These polynomial formulas arise by direct substitution, so no numerical search is used in the proof.

**3. The low-\(r\) branch has one strict maximizer.** Direct differentiation gives
\[
 F_-'(r)=-2r(1+r)(3+r)^2(4r^3+7r^2-4r-3).
\]
The cubic has exactly one positive root by Descartes' sign rule; its signs at \(3/4\) and \(4/5\) are opposite. Call it \(\rho\). Because \(\rho<4/5<r_-\), it lies in this branch, where \(F_-\) increases strictly up to \(\rho\) and decreases thereafter. In particular
\[
 F_-(\rho)\ge F_-(3/4)=\frac{1488375}{65536}>22.
\tag{3}
\]

**4. Neither remaining branch can compete.** Set \(H(r)=3r^4-14r^2+27\), which is strictly positive, with its unique positive minimum at \(r=\sqrt{7/3}\). On \([r_-,r_+]\), its maximum occurs at an endpoint. Since \(r_->5/6\), \(r_+<9/5\), and \(H\) decreases before \(\sqrt{7/3}\) and increases afterward,
\[
 F_0(r)\le\frac1{16}\max\{H(5/6)^2,H(9/5)^2\}
 =\frac1{16}\left(\frac{8089}{432}\right)^2<22.
\]
For \(r\ge r_+\), differentiating \(F_+\) produces the sign-controlling factor \(4r^3-7r^2-4r+3\). It is strictly increasing on \([r_+,3]\), negative at \(2\), and positive at \(21/10\). Hence \(F_+\) has a single maximum there, attained at a point \(c\in(2,21/10)\). At that point
\[
 F_+(c)<\left(\frac{21}{10}\right)^2
 \left(\frac{11}{10}\right)^2\left(\frac{31}{10}\right)
 =\frac{1654191}{100000}<22.
\]
Equations (2)--(3) therefore prove the global bound \(F\le F_-(\rho)\), with equality only at \(r=\rho,u=-1\).

**5. Attainment and uniqueness.** Choose \(\vartheta\in(0,\pi)\) with \(\cos\vartheta=-(1+\rho)/2\) and nodes \(1,e^{i\vartheta},e^{-i\vartheta}\). Then \(Q=1\), \(S=-\rho\), hence \(r=\rho,u=-1\); equality is attained. Conversely, any maximizing triple has \(r=\rho,u=-1\) after normalizing \(Q=1\). A further cube-root-of-unity rotation makes \(S=-\rho\). Its node polynomial factors exactly as
\[
 X^3+\rho X^2-\rho X-1
 =(X-1)(X^2+(1+\rho)X+1).
\]
Thus its roots are precisely the claimed isosceles triple. Undo the rotations and allow row permutations to obtain all equality cases.

**6. Exact tightness boundary for all three-mode exponent triples.** All three columns have squared norm three. Hadamard's inequality gives \(|\det M_m|^2\le27\), with equality precisely when the columns are pairwise orthogonal. The first two columns being orthogonal requires \(z_1+z_2+z_3=0\), which for unit-modulus points forces a rotated set of cubic roots of unity. For such a triple the power sum \(\sum_jz_j^k\) vanishes precisely when \(3\nmid k\). Orthogonality with the third column requires this for the differences \(m\) and \(m-1\), hence exactly \(m\equiv2\pmod3\). All equality geometries follow. Compactness yields a strict gap otherwise.

## Verification

The standalone `CHECK.py` uses only the Python standard library. It verifies the exact polynomial derivative identities using rational polynomial arithmetic, brackets all required scalar roots, compares the determinant with the Schur/discriminant identities at independent complex triples, checks the explicitly constructed equality set, and independently searches a dense two-angle grid for competitors. The finite grid checks do not establish global optimality; Steps 1--6 give the proof for the full continuum.

## Relationship to prior work

The order-variable Hermite expansion and exact uniform-order interpolation in Bawaneh (2026) motivate sparse order-frequency sampling; the source's abstract concerns function-valued fractional Fourier transform orbits and does **not** imply a three-scalar-sample determinant optimum. Generalized Vandermonde/Fekete theory supplies the determinant objective and Schur factorization, not this explicit global optimizer. Bos and De Marchi (2000) study generalized monomial alternants on real intervals, whereas Dubickas and Pritsker (2019) solve specific externally weighted *ordinary* Vandermonde problems on the circle.

The published three-interval Fourier Riesz-basis determinant design (2026) optimizes a one-parameter family of equally spaced frequency cosets with integer fibers \(\{0,1,3\}\); it obtains another exact radical but neither allows arbitrary three unit-circle nodes nor uses the exponent triple \(\{0,1,4\}\). The published separated-interval result similarly optimizes the constrained one-parameter family \(\{1,e^{2\pi i m\tau},e^{2\pi i(m+1)\tau}\}\) rather than arbitrary nodes for our fixed sparse exponent set. General Hadamard and spectral-moment facts are acknowledged as classical.

## Limitations

The sharp formula is specific to three minimal samples and the exponent triple \(\{0,1,4\}\). It is not the best spectral condition number, the best lower frame bound, or a result about all sparse exponent triples. The arithmetic tightness criterion is elementary and is context, not an assertion of novelty on its own. The motivating 2026 article's full body was not recoverable from its publicly indexed HTML view; its accessible abstract and bibliography were inspected, leaving a residual bibliographic comparison risk. Earlier differently titled work on generalized Fekete configurations may contain an equivalent fixed-exponent calculation. No independent validation or worldwide-priority certification is claimed.

## References

1. Sameer Bawaneh, *Spectral sampling and stable reconstruction for fractional-order Fourier transforms*, AIMS Mathematics 11 (2026), 36747--36770; first verified public date 2026-11-06, https://doi.org/10.3934/math.20261421.
2. Len Bos and Stefano De Marchi, *Fekete points for bivariate polynomials restricted to y=x^m*, East Journal on Approximations (2000), https://www.research.unipd.it/handle/11577/120340.
3. Arturas Dubickas and Igor Pritsker, *Weighted Fekete points on the real line and the unit circle*, arXiv:1902.08348 (2019), https://arxiv.org/abs/1902.08348.
4. *A three-regime sharp determinant design for three-interval Fourier Riesz bases*, public research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-three-regime-sharp-determinant-design-for-three-interval-fouri--c9a6f8a9b1bc.
5. *Sharp arithmetic determinant gap for three-coset Fourier bases on separated integer intervals*, public research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-arithmetic-determinant-gap-for-three-coset-fourier-bases-o--a0b1e6f9ca2a.
