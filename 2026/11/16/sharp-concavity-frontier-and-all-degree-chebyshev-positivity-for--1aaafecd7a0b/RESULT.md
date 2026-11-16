# Sharp concavity frontier and all-degree Chebyshev positivity for an arcsine-power deformation

## Finding
For each real parameter \(0\le t\le3\), define an even probability measure on \([-1,1]\) by
\[
 d\eta_t(x)=Z_t^{-1}\left(\frac{\arcsin x}{x}\right)^t dx,
 \qquad Z_t=\int_{-1}^1\left(\frac{\arcsin y}{y}\right)^t dy,
\]
where the ratio is continuously extended to \(1\) at zero. Let \(P_n^{(t)}\) be its unique degree-\(n\) orthogonal polynomial normalized by \(P_n^{(t)}(1)=1\). For \(z=e^{2i\theta}\), define the reciprocal coefficient polynomial by
\[
 V_n^{(t)}(z)=e^{in\theta}P_n^{(t)}(\cos\theta)
 =\sum_{k=0}^n v_{n,k}^{(t)}z^k.
\]
**All** these coefficients are strictly positive: \(v_{n,k}^{(t)}>0\) for every \(n\ge0\), \(0\le k\le n\), and every \(0\le t\le3\). They are symmetric and sum to one. Equivalently, the associated circle probability measure has strictly negative every nonconstant Fourier coefficient, and every one of its real Verblunsky coefficients is strictly between \(-1\) and \(0\).

There is an exact geometric frontier behind this interval. Put
\[
 h_t(u)=\cos u\left(\frac{u}{\sin u}\right)^t,
 \qquad 0<u<\frac{\pi}{2},\quad t\ge0.
\]
Then \(h_t\) is strictly concave throughout this interval **if and only if** \(0\le t\le3\). In particular the endpoint \(3\) is exact for concavity, **not** claimed to be the sharp endpoint of Fourier negativity or coefficient positivity.

## Assumptions and scope
All exponents in the finding are real. The measure is positive, even, and supported on the full compact interval. The normalized orthogonal polynomial exists and has nonzero value at \(1\) because all its simple zeros lie in \((-1,1)\). The coefficient identity uses \(z=e^{2i\theta}\), so it is a polynomial in \(z\) despite the apparent dependence on the angular square root. This is a statement at every finite polynomial degree, not a large-degree asymptotic.

## Proof
**1. The exact concavity frontier.** For \(|u|<\pi\) the classical Mittag–Leffler partial fraction formula implies
\[
 \frac1{\sin^2u}=\frac1{u^2}+\sum_{j=0}^\infty b_j u^{2j},
 \qquad b_j=\frac{2(2j+1)\zeta(2j+2)}{\pi^{2j+2}}>0.
\]
The series and its derivatives converge locally uniformly away from the poles. At the upper endpoint parameter,
\[
 h_3(u)=\frac{u^3\cos u}{\sin^3u}
 =-\frac{u^3}{2}\frac{d}{du}\frac1{\sin^2u}
 =1-\sum_{j=1}^\infty j b_j u^{2j+2}.
\]
It follows by twice differentiating the convergent series that \(h_3''(u)<0\) for \(0<u<\pi/2\). Also \(h_0''(u)=-\cos u<0\). For a fixed such \(u\), write \(A(u)=\log(u/\sin u)\) and \(B(u)=\log(\cos u)\). The identity
\[
 \frac{h_t''(u)}{h_t(u)}=B''(u)+tA''(u)+[B'(u)+tA'(u)]^2
\]
is a convex quadratic function of \(t\). Being negative at \(t=0\) and \(t=3\), it is strictly negative for every intermediate \(t\). Conversely, as \(u\downarrow0\),
\[
 h_t(u)=1+\frac{t-3}{6}u^2+O_t(u^4).
\]
Thus \(h_t''(u)>0\) near \(0\) whenever \(t>3\). This proves the if-and-only-if statement for \(t\ge0\).

**2. All nonconstant Fourier moments are strictly negative.** Push \(\eta_t\) forward by \(x\mapsto e^{2i\arccos x}\). Its conjugation-symmetric probability density \(\rho_t\) on the circle, for \(0<\vartheta<\pi\), is
\[
 \rho_t(\vartheta)=\frac{1}{2Z_t}
 h_t\!\left(\frac{\pi-\vartheta}{2}\right).
\]
It is strictly concave on \((0,\pi)\), and \(\rho_t'(\pi)=0\) by the even power-series expansion of \(h_t\) at the origin. Integration by parts twice therefore gives, for every integer \(m\ge1\),
\[
 \widehat\sigma_t(m)=2\int_0^\pi\rho_t(\vartheta)\cos(m\vartheta)\,d\vartheta
 =-\frac2{m^2}\int_0^\pi[-\rho_t''(\vartheta)]
 [1-\cos(m\vartheta)]\,d\vartheta<0.
\]
The endpoint term vanishes precisely because \(\rho_t'(\pi)=0\); the integral is strictly positive because \(\rho_t''<0\) and the bracket is nonnegative and not identically zero.

**3. Conversion to all-degree coefficient positivity.** Let \(\mathcal F_t(z)=1+2\sum_{m\ge1}\widehat\sigma_t(m)z^m\) be the circle measure's Carathéodory function, and set \(A_t(z)=-\sum_{m\ge1}\widehat\sigma_t(m)z^m\). Every nonzero Taylor coefficient of \(A_t\) is strictly positive. Its Schur function is
\[
 f_t(z)=\frac{\mathcal F_t(z)-1}{z[\mathcal F_t(z)+1]}
 =-\frac{A_t(z)}{z[1-A_t(z)]},
\]
which has strictly negative Taylor coefficients. The Schur iterate of \(f=-G\), where \(G(z)=a+\sum_{m\ge1}d_mz^m\) with \(0<a<1\) and all \(d_m>0\), is
\[
 f_{\mathrm{next}}(z)=-\frac{G(z)-a}{z[1-aG(z)]}.
\]
The reciprocal denominator has nonnegative Taylor coefficients and positive constant term, so the next iterate likewise has strictly negative coefficients. The circle measure has infinite support, so every Schur parameter \(\alpha_j\) lies strictly in \((-1,0)\).

The Szegő recurrence \(\Phi_{j+1}=z\Phi_j-\alpha_j\Phi_j^*\), starting with \(\Phi_0=1\), now shows that every coefficient of every monic circle orthogonal polynomial \(\Phi_j\) is positive. The standard para-orthogonal real-line identity, obtainable directly by testing circle orthogonality against monomials, reads
\[
 V_n^{(t)}(z)=\frac{z\Phi_{n-1}(z)+\Phi_{n-1}^*(z)}{2\Phi_{n-1}(1)}\quad(n\ge1).
\]
Its numerator has strictly positive coefficients and its denominator is positive; \(V_0=1\). The reciprocal identity yields \(v_{n,k}^{(t)}=v_{n,n-k}^{(t)}\), and evaluation at \(z=1\) gives the sum-one normalization. This establishes the coefficient claim for every degree.

## Verification
The standalone file `CHECK.py` checks the derivative identity, the first exact Mittag–Leffler coefficients, the \((t-3)/3\) endpoint second-derivative law, and sample strict concavity/Fourier-sign inequalities, including exact first moments at \(t=0\) and \(t=1\). All 224 finite symbolic/numerical checks pass. These tests are consistency checks only; the universal statements are proved by the convergent Mittag–Leffler expansion, convexity of the normalized curvature in the parameter, and the Schur recurrence. Run `python CHECK.py` after installing `requirements.txt`.

## Relationship to prior work
Xu (arXiv:2609.10328, first submitted September 9, 2026) studies precisely the power deformation \(d\eta_t\), proves coefficient positivity for the distinguished weight \(t=1\), and establishes a first-variation theorem at \(t=0\). The present finding proves positivity for the entire explicit interval \([0,3]\) and determines the exact concavity frontier of the lifted density. The general negative-Fourier-moments-to-negative-Schur-parameters mechanism and para-orthogonal identity are **prior theory** and are not claimed as new. Chenevier originally introduced the particular critical vectors associated with \(t=1\); our general \(t\) vectors are their natural deformations. The classical trigonometric inequality \((\sin u/u)^3>\cos u\) is related but does not by itself imply second-derivative concavity or the all-degree coefficient statement.

## Limitations
The threshold \(t=3\) is sharp **only for strict concavity** of the circle density. For \(t>3\), failure of that sufficient criterion does not imply a positive Fourier moment or a negative Chebyshev coefficient. No maximal positivity interval, recurrence-coefficient asymptotic, or numerical conditioning claim beyond \([0,3]\) is established. Historical priority remains provisional because not every older trigonometric-inequality or orthogonal-polynomial publication could be read in full; independent mathematical review has not been performed.

## References
- Shisong Xu, *Positivity and Asymptotics for Chenevier's Orthogonal Polynomials*, arXiv:2609.10328 (initial version 2026-09-09). https://arxiv.org/abs/2609.10328
- Gaëtan Chenevier, *An automorphic generalization of the Hermite–Minkowski theorem*, arXiv:1802.05066 (initial version 2018-02-14). https://arxiv.org/abs/1802.05066
- Barry Simon, *Orthogonal Polynomials on the Unit Circle*, Part 1: Classical Theory (2005), Schur algorithm and Szegő recurrences.
- *New approximation inequalities for circular functions*, Journal of Inequalities and Applications (2018), classical Mitrinović–Adamović inequality and refinements. https://doi.org/10.1186/s13660-018-1910-9
