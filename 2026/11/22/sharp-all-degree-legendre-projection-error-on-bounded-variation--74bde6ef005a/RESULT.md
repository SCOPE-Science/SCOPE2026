# Sharp all-degree Legendre projection error on bounded-variation data

## Finding

Let \(\Pi_n:L^2(-1,1)\to\mathcal P_n\) be the unweighted orthogonal projector onto polynomials of degree at most \(n\), for any integer \(n\ge0\). Equip real \(BV(-1,1)\) with \(\operatorname{TV}(f)=|Df|((-1,1))\). Let \(P_j\) denote the ordinary Legendre polynomial normalized by \(P_j(1)=1\), and let \(\xi_n\) be the least nonnegative zero of \(P_{n+1}\). Then the **sharp** error norm is

\[
\sup_{\operatorname{TV}(f)>0}\frac{\|f-\Pi_nf\|_{L^2(-1,1)}}{\operatorname{TV}(f)}
=C_n=\frac{|P_n(\xi_n)|}{\sqrt2}.
\]

This is attained **only** by the nonconstant single-jump functions \(f(x)=c+a\mathbf1_{(t,1)}(x)\) almost everywhere, \(a\ne0\), with \(t=0\) for even \(n\), and \(t\in\{-\xi_n,\xi_n\}\) for odd \(n\). In particular,

\[
C_{2m}^2=\frac12\left(\frac{\binom{2m}{m}}{4^m}\right)^2\quad(m\ge0),
\qquad
\lim_{n\to\infty}\sqrt n\,C_n=\frac1{\sqrt\pi}.
\]

For odd degrees the extremizing jump is **strictly displaced** from the midpoint, although its displacement tends to zero as the degree increases. Examples of squared constants are \(C_0^2=1/2\), \(C_1^2=1/6\), \(C_2^2=1/8\), and \(C_3^2\approx0.0847599728573\).

## Assumptions and scope

All functions are real, and \(BV(-1,1)\) means the almost-everywhere equivalence classes of integrable functions whose distributional derivative is a finite signed measure in the open interval. Endpoint choices for jump representatives do not affect the \(L^2\) statement. No endpoint boundary variation is counted. The norm is taken with *unweighted* Lebesgue measure \(dx\), not normalized probability measure \(dx/2\). The polynomial degree \(n\) ranges over **all nonnegative integers**.

## Proof

**1. Reduction to one jump.** Define \(h_t(x)=\mathbf1_{(t,1)}(x)\) for \(-1<t<1\), and \(R_n=I-\Pi_n\). For any \(f\in BV(-1,1)\) there is a constant \(c\) and a signed finite measure \(\mu=Df\) for which \(f=c+\int_{-1}^1h_t\,d\mu(t)\) almost everywhere. Since \(R_nc=0\), Bochner integration and the Hilbert-space triangle inequality give

\[
\|R_nf\|_2\le \int\|R_nh_t\|_2\,d|\mu|(t)
\le \left(\sup_{-1<t<1}\|R_nh_t\|_2\right)\operatorname{TV}(f).
\]

Conversely each such jump has variation one and realizes its own residual, so the supremum is exactly the largest single-jump residual.

**2. The jump residual identity.** Write \(E_n(t)=\|R_nh_t\|_2^2\). Orthogonality and the Legendre normalization \(\int_{-1}^1P_k^2=2/(2k+1)\) give

\[
E_n(t)=1-t-\sum_{k=0}^n\frac{2k+1}{2}
\left(\int_t^1P_k(s)\,ds\right)^2.
\]

Differentiating and using \((2k+1)P_k=(P_{k+1}'-P_{k-1}')\) for \(k\ge1\), the sum telescopes to \(E_n'(t)=-P_n(t)P_{n+1}(t)\). As \(E_n(1)=0\), the Legendre recurrence and its derivative yield the exact identity

\[
E_n(t)=\frac12\bigl(P_n(t)^2+P_{n+1}(t)^2-2tP_n(t)P_{n+1}(t)\bigr).
\]

Equivalently, if \(K_n(t,t)=\sum_{k=0}^n(2k+1)P_k(t)^2/2\) is the diagonal Legendre reproducing kernel, the Christoffel–Darboux formula gives \(E_n(t)=(1-t^2)K_n(t,t)/(n+1)^2\).

**3. Classification of global maxima.** The zeros of consecutive Legendre polynomials are simple and strictly interlacing. Because \(E_n'=-P_nP_{n+1}\) and both polynomials are positive immediately to the left of \(1\), its interior local maxima are precisely the zeros of \(P_{n+1}\) (the zeros of \(P_n\) are local minima). At a zero \(z\) of \(P_{n+1}\), \(E_n(z)=P_n(z)^2/2\).

To order these critical values, put \(g=P_{n+1}\), \(\lambda=(n+1)(n+2)\), and introduce the nonnegative **Legendre energy**

\[
\Phi(x)=(1-x^2)^2g'(x)^2+\lambda(1-x^2)g(x)^2.
\]

The Sturm–Liouville equation \(((1-x^2)g')'+\lambda g=0\) gives the *exact* identity

\[
\Phi'(x)=-2\lambda xg(x)^2.
\]

Thus \(\Phi\) is strictly decreasing from one positive zero of \(g\) to the next. At such a zero, the Legendre derivative identity \((1-z^2)g'(z)=(n+1)P_n(z)\) yields \(\Phi(z)=(n+1)^2P_n(z)^2\). Consequently the positive-zero local maxima of \(E_n\) strictly decrease outward. Since \(E_n\) is even and \(E_n(\pm1)=0\), the global maxima occur exactly at the innermost zeros of \(P_{n+1}\). If \(n\) is even this is \(0\); if \(n\) is odd these are \(\pm\xi_n\). This proves the exact constant.

**4. All equality cases.** The triangle inequality in a Hilbert space is strict unless the nonzero residual vectors \(R_nh_t\) are collinear with a common orientation (after absorbing the sign of \(D f\)). For distinct \(s,t\), such collinearity is impossible: otherwise a nontrivial linear combination of \(h_s,h_t\) would equal a polynomial almost everywhere, yet it has an interior jump. Thus equality forces \(Df\) to be a single signed atom at one maximizing location. Every prescribed single jump plainly gives equality.

**5. Asymptotic constant.** For \(n=2m\), the central Legendre value is \(P_{2m}(0)=(-1)^m\binom{2m}{m}/4^m\). Stirling's formula gives \((2m)C_{2m}^2\to1/\pi\). Since the projectors are nested, \(C_{n+1}\le C_n\), and therefore \(C_{2m+2}\le C_{2m+1}\le C_{2m}\). Squeezing proves \(nC_n^2\to1/\pi\) for both parities. The convergence of odd-degree minimizing positive roots to zero follows from standard interlacing or the classical Legendre zero asymptotics; it is not needed for the norm asymptotic.

## Verification

The accompanying `CHECK.py` performs exact symbolic checks of the jump-residual and Legendre-energy identities for degrees \(0\) through \(15\) or \(9\), exact Parseval checks for selected rational jump locations, and independent floating-point Gauss-root checks through degree \(79\). On the supplied run the program passed **892 assertions**. The identities, Sturm monotonicity, and BV measure reduction above—not finite-degree enumeration—prove the theorem for every degree.

## Relationship to prior work

Classical orthogonal-polynomial theory supplies the Legendre recurrence, Gauss-root interlacing and Christoffel–Darboux kernel identity; these are explicitly credited as inputs. Maday–Ould Kaber–Tadmor (1993) use Legendre spectral projection in discontinuous-data numerical analysis. Klimach–Zudrop–Roller (2015) explicitly calculate the \(L^2\) error of a step at the **fixed** location \(2/3\), reporting a table over degrees, but do not classify which jump location is globally worst or give the exact variation-normalized norm. The earlier Bojanić–Vuilleumier (1981) study of Fourier–Legendre convergence on BV functions is a close historical comparison whose full text was not accessible during this review; its exact coverage remains an originality risk. The present result isolates a sharp *global* energy error, all equality cases and the parity-dependent optimizing Gauss node.

## Limitations

The result does not cover weighted Jacobi projectors, multivariate tensor or total-degree projections, pointwise or \(L^\infty\) error, or nonlinear projection procedures. The origin of all constants uses the unnormalized \(L^2(-1,1;dx)\) norm. General classical identities used in the proof are not claimed as new. Historical completeness and independent verification remain unresolved.

## References

1. H. G. Klimach, J. Zudrop and S. P. Roller, *Generation of high order geometry representations in Octree meshes*, PeerJ Computer Science **1** (2015), e35, https://doi.org/10.7717/peerj-cs.35 (publicly dated 2015-11-25).
2. Y. Maday, S. M. Ould Kaber and E. Tadmor, *Legendre Pseudospectral Viscosity Method for Nonlinear Conservation Laws*, SIAM J. Numer. Anal. **30** (1993), 321–342, https://www.math.umd.edu/~tadmor/pubs/files/Mad-Ould-Tad_Legendre_SV_SINUM93.pdf.
3. R. Bojanić and M. Vuilleumier, *On the rate of convergence of Fourier–Legendre series of functions of bounded variation*, J. Approx. Theory **31** (1981), 67–79, https://doi.org/10.1016/0021-9045(81)90031-9 (full text unavailable for comparison).
4. NIST Digital Library of Mathematical Functions, §18.2(v), *Christoffel–Darboux Formula*, https://dlmf.nist.gov/18.2.v.
