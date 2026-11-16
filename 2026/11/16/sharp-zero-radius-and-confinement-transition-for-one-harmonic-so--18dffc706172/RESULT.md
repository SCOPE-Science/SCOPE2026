# Sharp zero-radius and confinement transition for one-harmonic Sobolev circle polynomials

## Finding
For an integer \(m\ge1\), a real \(\tau>0\), and a complex \(\gamma\) with \(|\gamma|\le 1/2\), equip complex polynomials with
\[
\langle p,q\rangle=\int_{\mathbb T}p(z)\overline{q(z)}\,d\sigma(z)
+\tau\int_{\mathbb T}p'(z)\overline{q'(z)}
\left(1+\gamma z^m+\overline\gamma z^{-m}\right)d\sigma(z),
\]
where \(\sigma\) is normalized Haar measure. Let \(S_n\) be the unique monic degree-\(n\) polynomial orthogonal to smaller degrees. Then the following **all-degree and all-strength zero confinement criterion** is exact:
\[
\boxed{\text{Every zero of every }S_n\text{ lies in }|z|<1
\text{ for every }\tau>0\iff |\gamma|\le\frac1{m+1}.}
\]
When \(0<|\gamma|\le1/(m+1)\), the stronger sharp radius law holds:
\[
\boxed{\sup_{n\ge1,\,\tau>0}\max_{S_n(\zeta)=0}|\zeta|
=\big((m+1)|\gamma|\big)^{1/m}.}
\]
Each individual zero has **strictly smaller** modulus than this supremum for every finite \(\tau\). At \(\gamma=0\), every \(S_n(z)=z^n\) and the sharp radius is zero. If \(m\ge2\) and \(1/(m+1)<|\gamma|\le1/2\), the first possible escaping degree is exactly \(m+1\): all earlier polynomials are monomials, but this degree has a zero outside the unit disk for sufficiently large \(\tau\).

## Assumptions and scope
The inner product is positive definite because the Haar term is strictly positive on nonzero polynomials and the derivative weight is nonnegative for \(|\gamma|\le1/2\), including the boundary where it vanishes at finitely many points. The same \(\tau\) is used in defining the degree-\(n\) polynomial for that experiment; the extrema quantify over arbitrary positive \(\tau\), including degree-dependent choices such as \(\lambda/n^s\). The zero-radius statement concerns complex zeros with multiplicities. All statements include boundary parameters, and require no asymptotic assumption on \(n\).

## Proof
**1. Phase reduction and Gram blocks.** Rotating the circle by the argument of \(\gamma\) changes the derivative weight to \(1+2\beta\cos(m\theta)\), where \(\beta=|\gamma|\), without changing zero moduli. Assume henceforth that \(0\le\beta\le1/2\). For monomials \(z^j,z^k\), direct Haar integration gives
\[
G_{jk}=\delta_{jk}(1+\tau j^2)
+\tau\beta jk\,(\delta_{j,k+m}+\delta_{k,j+m}).
\]
Thus index zero is isolated and the positive indices separate into residue classes modulo \(m\). Because \(G\) is strictly positive definite, the monic orthogonal polynomial is supported on just the class of its leading index. Write \(n=r+Jm\) with \(1\le r\le m\), \(J\ge0\). There are unique real coefficients \(c_{r+jm}\) such that
\[
S_n(z)=\sum_{j=0}^J c_{r+jm} z^{r+jm},\qquad c_n=1.
\]
When \(\beta>0\), every coefficient in this class is nonzero and signs alternate.

**2. Exact tridiagonal elimination.** Put \(a_k=1+\tau k^2\) and \(b_k=\tau\beta k(k+m)\). On each positive residue class, define positive pivots
\[
d_k=a_k-\frac{b_{k-m}^{\,2}}{d_{k-m}}\quad(k>m),
\qquad d_k=a_k\quad(1\le k\le m).
\]
These are positive Schur complements of principal submatrices of the positive definite Gram matrix. The equations of orthogonality, eliminated in increasing degree, give
\[
c_k=-R_kc_{k+m},\qquad R_k=\frac{b_k}{d_k}>0
\quad(k=r,r+m,\ldots,n-m).
\]
In particular the ratios of consecutive coefficient **magnitudes in increasing degree** are exactly \(R_k\), and \(d_k=a_k-b_{k-m}R_{k-m}\).

**3. Uniform ratio bound.** Assume \(0<\beta\le1/(m+1)\), and set \(L=(m+1)\beta\le1\). For \(k\le m\),
\[
R_k=\frac{\tau\beta k(k+m)}{1+\tau k^2}
<\beta\left(1+\frac mk\right)\le L.
\]
Suppose inductively that \(R_{k-m}<L\) for \(k>m\). It is enough to show \(L(a_k-b_{k-m}L)>b_k\), since this also ensures the denominator is positive. Indeed,
\[
L(a_k-b_{k-m}L)-b_k
=\beta\left[(m+1)+\tau k\left(m(k-1)-L^2(k-m)\right)\right].
\]
As \(k>m\), \(L^2\le1\), and \(m(k-1)-(k-m)=(m-1)k\ge0\), this is strictly positive. Induction yields \(0<R_k<L\) for every \(k\) and every finite \(\tau\).

**4. Zeros and sharpness.** The alternating coefficient signs mean that
\[
S_n(z)=(-1)^Jz^r H(-z^m),\qquad
H(w)=\sum_{j=0}^J |c_{r+jm}|w^j.
\]
All coefficients of \(H\) are strictly positive and \(|c_{r+jm}|/|c_{r+(j+1)m}|=R_{r+jm}<L\). By the Eneström–Kakeya bound, every nonzero root of \(H\) has modulus \(<L\); consequently every nonzero root of \(S_n\) satisfies \(|z|<L^{1/m}\). If \(J=0\), the polynomial is \(z^n\) and the assertion is immediate. If \(\beta=0\), the entire Gram matrix is diagonal and \(S_n=z^n\).

For \(n=m+1\), a direct two-by-two Gram calculation gives
\[
S_{m+1}(z)=z^{m+1}-\frac{\tau\beta(m+1)}{1+\tau}\,z
\]
(up to the harmless rotation for nonreal \(\gamma\)). Its nonzero roots have modulus \(\big(L\tau/(1+\tau)\big)^{1/m}\), approaching \(L^{1/m}\) as \(\tau\to\infty\). This proves optimality of the universal radius. If \(L>1\), the same roots are exterior precisely when \(\tau>1/(L-1)\), while for \(n\le m\) no positive degrees are coupled and \(S_n=z^n\). This proves both necessity and the first escaping degree.

## Verification
The self-contained standard-library script `CHECK.py` constructs the orthogonal polynomials with exact rational arithmetic. It checks the monomial Gram equations, all relevant pivot recurrences, coefficient-ratio bounds in the subcritical range, and the first-escape formula, for integer harmonics through eight, multiple rational weights and strengths, and degrees up to 25. The recorded execution completed 38,011 exact rational assertions. The unbounded degree and parameter statements follow from the inequalities above, not from the finite tests.

## Relationship to prior work
Majumder and Swaminathan (2026, arXiv:2610.31994, first submitted October 22) study degree-dependent Sobolev orthogonality on the circle, establishing strong asymptotic formulas and examining zero locations for a Bernstein–Christoffel example. This motivates a finite-degree, uniform-in-strength zero-confinement question, which strong exterior asymptotics alone do not settle. Related published investigations of balanced first-harmonic and general one-harmonic derivative weights provide effective-weight limits and asymptotic norm corrections; those claims do not state the sharp all-degree zero-radius threshold \(1/(m+1)\). Classical Eneström–Kakeya is the final root-location tool, but the essential input here is the sharp uniform Schur-complement ratio inequality and its matching escape example.

## Limitations
No optimal universal radius is claimed when \(|\gamma|>1/(m+1)\); the theorem supplies a sharp failure example instead. The result does not classify the entire zero configuration or extend to a derivative weight with multiple different harmonics. Related circular-Jacobi Sobolev polynomial work has only been compared at abstract/metadata level, and could contain an equivalent general criterion under different terminology; priority remains provisional. The proof and tests are not an independent validation.

## References
1. S. Majumder and A. Swaminathan, *Sobolev Orthogonal Polynomials on the unit circle with varying inner product*, arXiv:2610.31994v1 (2026-10-22), https://arxiv.org/html/2610.31994.
2. C. F. Bracciali, J. V. da Silva, and A. Sri Ranga, *A class of Sobolev orthogonal polynomials on the unit circle and associated continuous dual Hahn polynomials: Bounds, asymptotics and zeros*, J. Approx. Theory 268 (2021), 105604, https://doi.org/10.1016/j.jat.2021.105604.
3. E. Berriochoa and A. Cachafeiro, *Bernstein–Szegő–Lebesgue Sobolev orthogonal polynomials on the unit circle*, J. Difference Equ. Appl. 6 (2000), 719–737, https://doi.org/10.1080/10236190008808254.
4. Eneström–Kakeya theorem on zeros of polynomials with positive coefficients (classical root bound).
