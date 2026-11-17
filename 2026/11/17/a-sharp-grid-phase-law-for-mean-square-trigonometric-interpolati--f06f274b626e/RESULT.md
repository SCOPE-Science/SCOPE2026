# A sharp grid-phase law for mean-square trigonometric interpolation across one jump

## Finding

Let \(N=2n+1\) be odd and \(0\le a<1\). For the \(N\)-point equispaced grid \(x_j=2\pi(j+a)/N\), let \(L_{N,a}\) denote trigonometric Lagrange interpolation of degree at most \(n\). Define the periodic sawtooth \(G(x)=x\) for \(0<x<2\pi\) and \(G(0)=0\). Let \(f=cG+h\), with fixed \(c\in\mathbb C\setminus\{0\}\) and periodic continuous \(h\) having Fourier coefficients \(|\widehat h(k)|\le C(1+|k|)^{-2}\) for every integer \(k\). Normalize \(\|u\|_2^2=(2\pi)^{-1}\int_0^{2\pi}|u(x)|^2\,dx\). Then, uniformly for \(0\le a<1\),

\[
N\|f-L_{N,a}f\|_2^2=|c|^2 F(a)+O_{c,h}(N^{-1}),
\qquad
F(a)=4+2\int_0^{1/2}\left|\frac{\pi\exp[-2\pi i(a-1/2)t]}{\sin(\pi t)}-\frac1t\right|^2\,dt.
\]

The removable endpoint singularity is interpreted by continuity. The coefficient \(F(a)\) is uniquely minimized at \(a=1/2\), the placement of the jump midway between consecutive nodes. In particular \(F(1/2)\approx4.334096272882\), whereas \(F(0)\approx15.002531876980\). If the aligned node instead receives the midpoint value \(G(0)=\pi\), the corresponding leading coefficient is

\[
F_{\mathrm{mid}}=4+2\int_0^{1/2}\left(\pi\cot(\pi t)-\frac1t\right)^2dt
\approx5.132927475891>F(1/2).
\]

The normalized error depends only on the jump amplitude at leading order. The improvement remains strict even compared with the midpoint-value convention at an aligned jump.

## Assumptions and scope

Only odd \(N\) are considered, so that the interpolant has the unambiguous frequency band \(\{-n,\ldots,n\}\). Complex-valued inputs are permitted. The point value \(G(0)=0\) matters exactly at the aligned phase \(a=0\); otherwise the grid does not encounter the jump. The smooth remainder assumption is sufficient, for example, when a periodic \(h\) has absolutely continuous first derivative and integrable second derivative. Its Fourier-coefficient hypothesis is the one used in the proof. Phase \(a\) may vary with \(N\) because the error remainder is uniform in phase. For a general jump \(J=-2\pi c\), multiply \(F\) by \(|J|^2/(4\pi^2)\).

## Proof

**1. Exact Fourier coefficients.** The Fourier coefficients of \(G\) are \(\widehat G(0)=\pi\) and \(\widehat G(k)=i/k\) for nonzero integers \(k\). Summation of the finite geometric derivative gives the coefficient of the trigonometric interpolant at every \(0<|k|\le n\):

\[
\widehat{L_{N,a}G}(k)=\frac{i\pi}{N}\frac{\exp[-2\pi i(a-1/2)k/N]}{\sin(\pi k/N)},
\qquad
\widehat{L_{N,a}G}(0)=\pi+\frac{\pi(2a-1)}N.
\]

To see this directly, insert \(G(x_j)=2\pi(j+a)/N\) into the discrete Fourier coefficient \(N^{-1}\sum_jG(x_j)e^{-ikx_j}\) and differentiate \(\sum_jz^j=(1-z^N)/(1-z)\) at \(z=e^{-2\pi ik/N}\). The result applies at every fixed phase, including \(a=0\), because its sampled jump value is prescribed as zero.

**2. Parseval and the sharp limit.** The positive and negative modes are conjugate. Consequently,

\[
\|G-L_{N,a}G\|_2^2=
\frac{\pi^2(2a-1)^2}{N^2}
+2\sum_{k=1}^{n}\left|\frac{\pi}{N}\frac{e^{-2\pi i(a-1/2)k/N}}{\sin(\pi k/N)}-\frac1k\right|^2
+2\sum_{k=n+1}^\infty\frac1{k^2}.
\]

The first term becomes \(O(N^{-2})\). For the last term, \(2N\sum_{k>n}k^{-2}=4+O(N^{-1})\). Multiply the middle sum by \(N\) and write \(t=k/N\): it is a Riemann sum for twice the stated integral. The integrand, written as

\[
\left(\frac\pi{\sin\pi t}-\frac1t\right)^2+
\frac{2\pi}{t\sin\pi t}\bigl(1-\cos(2\pi(a-1/2)t)\bigr),
\]

extends to a jointly continuously differentiable function on \([0,1/2]\times[0,1]\). Hence the Riemann-sum error is \(O(N^{-1})\), uniformly in \(a\), proving the stated asymptotic for \(G\).

**3. Smooth remainder.** The Fourier coefficients of \(L_{N,a}h\) on \(|k|\le n\) equal \(\sum_{\ell\in\mathbb Z}\widehat h(k+\ell N)e^{2\pi i\ell a}\). This identity follows by absolute Fourier convergence and sampling orthogonality. The aliasing error in each retained mode is \(O_h(N^{-2})\), uniformly in phase, while the squared tail of \(h\) is \(O_h(N^{-3})\). Parseval gives \(\|h-L_{N,a}h\|_2=O_h(N^{-3/2})\). Since \(\|G-L_{N,a}G\|_2=O(N^{-1/2})\), the cross term in the squared error of \(cG+h\) is \(O_{c,h}(N^{-2})\), as required.

**4. Strict phase optimality.** For \(0<t\le1/2\), both \(\pi/\sin(\pi t)\) and \(1/t\) are strictly positive. Thus the integrand is minimized pointwise exactly when \(\cos(2\pi(a-1/2)t)=1\). Within \(0\le a\le1\), this occurs for almost every \(t\) only when \(a=1/2\). Consequently the minimizer of \(F\) is unique and strict.

**5. Midpoint-value alignment.** Replacing \(G(0)=0\) with \(G(0)=\pi\) adds \(\pi/N\) to every interpolation coefficient. For nonzero \(k\), the exact coefficient becomes \(i\pi\cot(\pi k/N)/N\), and the constant coefficient becomes exactly \(\pi\). The same Parseval limit gives \(F_{\mathrm{mid}}\). For \(0<t\le1/2\), the difference of the two squared integrands is strictly positive, because
\[
\left(\frac1t-\pi\cot(\pi t)\right)-\left(\pi\csc(\pi t)-\frac1t\right)
=\frac2t-\pi\cot(\pi t/2)>0,
\]

where the last inequality is \(x\cot x<1\) for \(0<x\le\pi/4\). Both quantities on the left are positive. Integration proves \(F_{\mathrm{mid}}>F(1/2)\). This completes the proof.

## Verification

The accompanying standard-library-only program `verify.py` independently checks discrete Fourier coefficient identities by direct nodal summation for multiple odd mesh sizes and phases, compares the finite Parseval error to the integral coefficient, and checks the strict ordering of sample phases and the midpoint-convention comparison. It uses finite floating-point computations as diagnostics only. The asymptotic and strict global minimization follow analytically from Steps 1–5.

## Relationship to prior work

Yurii Kolomoitsev, *Approximation by Linear Sampling Operators in Banach Spaces* (first public arXiv:2601.19012v1, 26 January 2026; later J. Fourier Anal. Appl. 2026), develops general direct/inverse sampling estimates and cites the \(O(N^{-1/p})\) trigonometric interpolation rate for functions of bounded variation. Neither the exact leading mean-square error coefficient for a phase-shifted jump nor its strict optimal phase is asserted there.

Jürgen Prestin and Ewald Quak, *On the arclength of trigonometric interpolants* (2001), study a closely related sawtooth with the jump at or between grid nodes. They derive finite Fourier formulas and prove that the **arclength** of an interpolant can change from bounded to logarithmically divergent with the sampling geometry. These exact formulas are essential nearby prior machinery; that article does not state the phase-dependent normalized \(L^2\) error law or the half-cell optimality for the unmodified odd-grid interpolant. The related source, Arnak Poghosyan, *On a pointwise convergence of trigonometric interpolations with shifted nodes* (2013), reports sharp pointwise asymptotics for **corrected** interpolation methods; those are distinct operators and loss functions. This paper's full text was not accessible during comparison, so complete noncoverage is not asserted.

## Limitations

The result treats a single jump with a Fourier-\(O(k^{-2})\) remainder and odd equispaced meshes. It is not a classification for multiple interacting jumps, even mesh sizes, \(L^p\) errors other than \(p=2\), or nonuniform nodes. A relevant earlier paper with an equivalent \(L^2\)-phase identity under a different parametrization may exist; priority needs additional independent literature review. No independent audit has been performed.

## References

- Y. Kolomoitsev, *Approximation by Linear Sampling Operators in Banach Spaces*, arXiv:2601.19012v1, 26 January 2026. https://arxiv.org/abs/2601.19012. https://doi.org/10.1007/s00041-026-10302-x.
- J. Prestin and E. Quak, *On the arclength of trigonometric interpolants*, J. Numer. Anal. Approx. Theory 30(2), 2001, pp. 219–227. https://ictp.acad.ro/jnaat/journal/article/download/2001-vol30-no2-art10/Prestin-Quak-pdf/699.
- J. Prestin and Y. Xu, *Convergence Rate for Trigonometric Interpolation of Non-smooth Functions*, J. Approx. Theory 77 (1994), 113–122. https://doi.org/10.1006/jath.1994.1037.
- A. Poghosyan, *On a pointwise convergence of trigonometric interpolations with shifted nodes*, Armenian J. Math. 5(2) (2013), 105–122. https://arar.sci.am/dlibra/publication/14982/edition/13265/content.
