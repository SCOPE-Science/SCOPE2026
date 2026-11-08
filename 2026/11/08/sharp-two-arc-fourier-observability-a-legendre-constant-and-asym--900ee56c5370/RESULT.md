# Sharp two-arc Fourier observability: a Legendre constant and asymptotic antipodal design

## Finding
For every integer \(m\ge1\), the worst observed degree-\(m\) trigonometric polynomial on two short equal-length arcs has an exact leading concentration eigenvalue, including its dependence on the distance between arc centers. The leading coefficient has a unique optimum when the arc centers are antipodal. The sharp optimized coefficient is
\[
\lim_{\alpha\downarrow0}\alpha^{-(2m+1)}\max_{\alpha\le\theta\le\pi-\alpha}\lambda_m(\alpha,\theta)
=\frac{2^{4m+1}}{\pi(2m+1)\binom{2m}{m}^{3}}.
\]
Every sequence of maximizing center parameters tends to \(\pi/2\). For the three-mode space \(m=1\), antipodal centers are in fact uniquely optimal at *every* admissible positive arc width.

## Assumptions and scope
Use the circle \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) with normalized Haar measure \(dt/(2\pi)\). Define
\[
 V_m=\left\{f(t)=\sum_{k=-m}^{m}a_ke^{ikt}:a_k\in\mathbb C\right\},
 \qquad\|f\|_2^2=\sum_{k=-m}^{m}|a_k|^2.
\]
For \(0<\alpha<\pi/2\) and \(\alpha\le\theta\le\pi-\alpha\), take the union of two nonoverlapping arcs
\[
E_{\alpha,\theta}=\{t:\operatorname{dist}_{\mathbb T}(t,\theta)\le\alpha\}\cup
\{t:\operatorname{dist}_{\mathbb T}(t,-\theta)\le\alpha\}.
\]
Define the concentration eigenvalue \(\lambda_m(\alpha,\theta)=\min_{f\in V_m,\|f\|_2=1}\int_{E_{\alpha,\theta}}|f|^2dt/(2\pi)\). Its positivity follows from analyticity. Write \(B_m=\binom{2m}{m}\), and
\[
S_m(c)=\sum_{k=0}^{2m}\left|[z^k](z^2-2cz+1)^m\right|^2.
\]
The limit at a *fixed* center angle \(0<\theta<\pi\) is
\[
C_m(\theta)=\lim_{\alpha\downarrow0}\frac{\lambda_m(\alpha,\theta)}{\alpha^{2m+1}}
=\frac{2^{4m+1}(\sin\theta)^{2m}}{\pi(2m+1)B_m^2 S_m(\cos\theta)}.
\]
The bandwidth \(m\) is fixed as \(\alpha\to0\); no uniform-in-bandwidth assertion is made.

## Proof
**1. Vanishing-jet characterization of the limiting direction.** Every \(f\in V_m\) has the form \(f(t)=e^{-imt}P(e^{it})\) with \(\deg P\le2m\). Let \(z_\pm=e^{\pm i\theta}\). A unit-norm polynomial proportional to
\[
Q_\theta(z)=(z-z_+)^m(z-z_-)^m=(z^2-2\cos\theta\,z+1)^m
\]
has concentration \(O_{m,\theta}(\alpha^{2m+1})\), so the minimum has that order as an upper bound. Choose normalized minimizers \(f_\alpha\); along any convergent subsequence of coefficients, rescale around each center \(t=\pm\theta+\alpha u\) and divide by \(\alpha^m\). Their \(L^2([-1,1])\) norms stay bounded. The Taylor remainder beyond order \(m\) is \(O_m(\alpha)\) uniformly, because the original coefficient norms equal one. Equivalence of norms on polynomials of degree at most \(m\) now bounds every rescaled Taylor coefficient \(\alpha^{j-m}f_\alpha^{(j)}(\pm\theta)/j!\), for \(0\le j\le m\). Thus any coefficient limit vanishes to order at least \(m\) at both centers. The available degree \(2m\) makes this one-dimensional: the limiting polynomial is a scalar multiple of \(Q_\theta\).

**2. Sharp local cost.** Its normalized coefficient modulus is \(S_m(\cos\theta)^{-1/2}\). The absolute value of the degree-\(m\) Taylor coefficient at either center, with respect to the angular variable, is
\[
L_m(\theta)=\frac{(2\sin\theta)^m}{\sqrt{S_m(\cos\theta)}}.
\]
After rescaling \(t=\pm\theta+\alpha u\), each local limit is a complex polynomial of degree \(m\) with leading coefficient of modulus \(L_m(\theta)\). The least possible integral squared modulus on \([-1,1]\) for a polynomial with prescribed leading coefficient \(L\) is \(|L|^2 h_m\), where the monic Legendre polynomial gives
\[
 h_m=\frac{2\cdot4^m}{(2m+1)B_m^2}.
\]
Accounting for the two arcs and Haar normalization, any minimizing sequence has lower limit \(L_m(\theta)^2h_m/\pi\). This is the stated \(C_m(\theta)\). Conversely, the Hermite interpolation map sending the \(2m\) jets of orders \(0,\ldots,m-1\) at the two distinct centers to polynomials in \(V_m\), modulo the span of \(Q_\theta\), is invertible. Adding corrections of orders \(\alpha^{m-j}\) to these jets produces, independently on both arcs, the monic Legendre residual polynomial in the rescaled coordinate, while the corrected unit vector still tends to \(Q_\theta/\sqrt{S_m}\). Thus the lower bound is attained asymptotically. The same argument is uniform on compact subintervals of \((0,\pi)\), since the Hermite interpolation matrices vary smoothly and remain nonsingular there.

**3. Optimal separation, including moving centers.** By Parseval,
\[
 S_m(c)=\frac1{2\pi}\int_0^{2\pi}(2\cos t-2c)^{2m}dt.
\]
Expanding in even powers of \(c\), every nonconstant coefficient is strictly positive, because all odd cosine moments vanish and the even moments are positive. Hence \(S_m(c)>S_m(0)=B_m\) whenever \(c\ne0\). Meanwhile \(\sin^{2m}\theta\le1\), strictly except at \(\theta=\pi/2\); therefore \(C_m\) has its unique maximum at the antipodal centers and equals \(2^{4m+1}/(\pi(2m+1)B_m^3)\). For center parameters approaching \(0\) or \(\pi\) as \(\alpha\to0\), the normalized trial vector from \(Q_\theta\) gives the uniform estimate
\[
 0\le\lambda_m(\alpha,\theta)
 \le K_m\alpha^{2m+1}(\sin\theta+\alpha)^{2m},
\]
with a constant depending only on \(m\), since \(S_m(c)\ge B_m\). This rules out endpoint-approaching maximizers. Compact-uniform convergence of the rescaled eigenvalue then establishes the optimized limit and convergence of every maximizing center parameter.

**4. Condition number at antipodal centers.** As \(\alpha\downarrow0\), the concentration matrix has leading term \(\alpha/\pi\) times the sum of two rank-one point-evaluation Gram matrices. At antipodal centers the normalized evaluation vectors each have squared norm \(2m+1\) and their inner-product modulus is \(1\). Hence \(\lambda_{\max}=(2m+2)\alpha/\pi+O_m(\alpha^3)\). Dividing by the minimal eigenvalue yields
\[
 \kappa(C_{m,\alpha,\pi/2})\sim
 \frac{(2m+2)(2m+1)B_m^3}{2^{4m+1}}\alpha^{-2m}.
\]

**5. Exact three-mode boundary.** For \(m=1\), the concentration Toeplitz matrix has diagonal \(a=2\alpha/\pi\), first off-diagonal \(b=(2\sin\alpha/\pi)\cos\theta\), and second off-diagonal \(c=(\sin2\alpha/\pi)\cos2\theta\). Its lower even-sector eigenvalue is \(a+c/2-\sqrt{c^2/4+2b^2}\). Put \(A=2\sin\alpha/\pi\), \(B=A\cos\alpha>0\). For \(\cos\theta\ne0\), the identity \(2b^2>B^2+Bc=2B^2\cos^2\theta\) shows this lower eigenvalue is strictly below \(a-B\). At \(\theta=\pi/2\), the eigenvalues are \(a-B,a,a+B\). Thus the antipodal arrangement is the unique maximizer and
\[
 \lambda_1(\alpha,\pi/2)=\frac{2\alpha-\sin2\alpha}{\pi},\quad 0<\alpha<\pi/2.
\]

## Verification
The standalone `check.py` constructs the full \((2m+1)\)-dimensional Toeplitz Gram matrix directly from integrated Fourier moments, independently of the Legendre-limit formula. It compares high-precision eigenvalues against the limiting constants for degrees \(1\) through \(5\), checks positivity and the unique limiting angular optimum, and checks exact combinatorial identities and finite-width designs for small bands. Running `python check.py` with `mpmath` installed returns `NARROW_TWO_ARC_CHECKS_PASS 112`. Finite numerical tests are supplementary; the proof above establishes the infinite parameter family.

## Relationship to prior work
The general eigenvalue-distribution theory of Marceca, Romero, and Speckbacher treats irregular Fourier concentration domains but estimates the number of eigenvalues in a prescribed interval, not the exact smallest finite-band eigenvalue in the vanishing two-arc regime. Andén and Romero develop multitaper estimation for irregular acquisition domains, without this small-two-arc sharp coefficient or optimal separation. Batenkov and Diab bound clustered confluent Vandermonde singular values in a complementary Fourier-data model; their sharp **orders** and constants depending on cluster parameters do not give this Legendre-derived concentration coefficient or the all-degree angular optimizer. The fixed-band, two-arc asymptotic is not claimed to establish a global phase-transition theorem for arbitrary bandlimit or finite arc width.

## Limitations
The theorem fixes the integer bandwidth before the arc width tends to zero. It assumes two arcs of equal width and continuous noiseless observations. The result optimizes only the smallest concentration eigenvalue, not an arbitrary nonlinear estimator or the global spectral condition number over all placements. For \(m\ge2\), only asymptotic optimality of antipodal placement is proved; strict finite-width optimality is neither claimed nor inferred from numerical experiments. The historical-priority comparison is provisional, particularly regarding older Slepian, polynomial approximation, and confluent sampling results.

## References
- F. Marceca, J. L. Romero, and M. Speckbacher, *Eigenvalue estimates for Fourier concentration operators on two domains*, arXiv:2301.11685, initial version 2023-01-27. https://arxiv.org/abs/2301.11685
- J. Andén and J. L. Romero, *Multitaper estimation on arbitrary domains*, arXiv:1812.03225, initial version 2018-12-07. https://arxiv.org/abs/1812.03225
- D. Batenkov and N. Diab, *Super-resolution of generalized spikes and spectra of confluent Vandermonde matrices*, arXiv:2203.11923, initial version 2022-03-22. https://arxiv.org/abs/2203.11923
