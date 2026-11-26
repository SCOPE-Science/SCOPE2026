# Unique directed relative-entropy projection of the circle heat kernel onto Poisson kernels

## Finding
For every heat time \(t>0\), the normalized circle heat density \(H_t\) has a unique minimizer of **forward** Kullback–Leibler divergence \(D(H_t\Vert P)\) over Poisson kernels with freely chosen radius and center. The optimal center agrees with the heat center. The optimal radius \(r_t\) is strictly decreasing in \(t\), satisfies \(0<r_t<e^{-t}\), and is determined by the strictly monotone equation below.

As \(t\downarrow0\), \(1-r_t\sim c_*\sqrt t\), with \(c_*=0.86550319873261586\ldots\). The optimum divergence tends to \(K_*=0.18275830866970635\ldots\); matching the first Fourier moment instead gives divergence \(\tfrac12\log(1/t)+\tfrac12\log\pi-\log2-\tfrac12-\gamma+o(1)\), so the excess loss diverges. At large heat times, with \(q=e^{-t}\), the optimal radius is \(q-q^3+3q^5+O(q^7)\), and the optimum divergence is \(q^4(1+o(1))\).

## Assumptions and scope
For Haar probability measure \(d\mu=d\theta/(2\pi)\) on \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), set
\[
H_t(\theta)=\sum_{n\in\mathbb Z}e^{-tn^2}e^{in\theta},\qquad
P_{r,\phi}(\theta)=\frac{1-r^2}{1-2r\cos(\theta-\phi)+r^2},\qquad 0\le r<1.
\]
These are positive probability densities against \(\mu\). We use \(D(p\Vert q)=\int p\log(p/q)\,d\mu\); the reverse divergence and generic circular densities are not considered. All centers label the same density when \(r=0\).

## Proof
**Fourier identity and center.** Absolute convergence gives
\[
D(H_t\Vert P_{r,\phi})=\int H_t\log H_t\,d\mu-\log(1-r^2)-2\sum_{n\ge1}\frac{e^{-tn^2}r^n}{n}\cos(n\phi).
\]
For \(r>0\), all Fourier weights are positive and the first harmonic forces equality only at \(\phi=0\pmod{2\pi}\). In this direction the right radius derivative at zero is \(-2e^{-t}<0\), ruling out the uniform density.

**Unique radius.** Set \(s=-\log r\), \(A_t(s)=\sum_{n\ge1}e^{-tn^2-sn}\), and \(B(s)=(e^{2s}-1)^{-1}\). The derivative in \(r\) has the sign of \(B-A_t\); the radius equation is \(R_t(s)=1\), where \(R_t=A_t/B\). This quotient tends to zero as \(s\downarrow0\) and is asymptotic to \(e^{s-t}\) as \(s\to\infty\). The expectation of \(n\) under normalized weights \(e^{-sn-tn^2}\) is strictly less than under weights \(e^{-sn}\), since tilting by the strictly decreasing function \(e^{-tn^2}\) gives a strictly negative covariance with \(n\) under the original geometric weights. Consequently
\[
\frac{d}{ds}\log R_t(s)=\frac{2}{1-e^{-2s}}-\mathbb E_{A,t,s}n
>\frac{2}{1-e^{-2s}}-\frac{1}{1-e^{-s}}=\frac1{1+e^{-s}}>0.
\]
The crossing is the unique global minimum by the radius derivative signs. At \(s=t\), termwise comparison \(e^{-tn^2-tn}\le e^{-2tn}\), strict for \(n\ge2\), gives \(R_t(t)<1\). Thus \(s_t>t\), so \(r_t<e^{-t}\). Since \(R_t(s)\) strictly decreases with \(t\) for fixed \(s\), the unique crossing moves strictly right, smoothly by the implicit function theorem.

**Sharp small-time scale.** For fixed \(c>0\) a Riemann sum gives \(\sqrt{t}\,A_t(c\sqrt t)\to\int_0^\infty e^{-x^2-cx}\,dx\), and \(\sqrt t B(c\sqrt t)\to1/(2c)\). The limiting quotient is
\[
L(c)=2c\int_0^\infty e^{-x^2-cx}\,dx=2\int_0^\infty e^{-u-u^2/c^2}\,du.
\]
It increases continuously and strictly **from zero to two** and crosses one at a unique \(c_*>0\). For any two fixed \(c\)'s on opposite sides of \(c_*\), convergence and radial monotonicity bracket \(s_t/\sqrt t\) between them for small enough \(t\). Therefore \(s_t/\sqrt t\to c_*\) and \(1-r_t\sim c_*\sqrt t\).

Use \(\theta=\sqrt t\,x\), \(R=\pi/\sqrt t\). The scaled Lebesgue densities on \([-R,R]\) are
\[
g_t(x)=\sum_{k\in\mathbb Z}g(x+2kR),\quad g(x)=\frac{e^{-x^2/4}}{\sqrt{4\pi}},\qquad
q_{t,s}(x)=\frac{\sqrt t\,\sinh s}{2\pi(\cosh s-\cos(\sqrt t\,x))}.
\]
The wrapped Gaussian identity follows by taking Fourier coefficients. On \([-R,R]\), each translated summand divided by \(g(x)\) is bounded by \(e^{-|k|(|k|-1)R^2}\); thus \(g\le g_t\le Cg\) uniformly for small \(t\). Also \(1-\cos y\) is comparable to \(y^2\) for \(|y|\le\pi\), while \(\cosh s-1\) is comparable to \(s^2\) at small \(s\). If \(s/\sqrt t\to c>0\), then \(q_{t,s}\) is uniformly comparable to \((1+x^2)^{-1}\) and converges pointwise to \(q_c(x)=c/[\pi(c^2+x^2)]\). Hence \(|g_t\log(g_t/q_{t,s})|\le C'(1+x^2)g(x)\) on the whole expanding interval; dominated convergence gives
\[
K_*=D(g\Vert q_{c_*})=\log(\pi/c_*)-\tfrac12\log(4\pi e)+\mathbb E\log(c_*^2+X^2),\quad X\sim N(0,2).
\]
In fact \(c\,dD(g\Vert q_c)/dc=2\mathbb E[c^2/(c^2+X^2)]-1=L(c)-1\), using \(\mathbb E\cos(uX/c)=e^{-u^2/c^2}\) in the Laplace integral for \(1/(1+(X/c)^2)\). So \(c_*\) is the unique Gaussian–Cauchy optimum as well.

**Moment matching and large heat time.** The first Fourier coefficients give the moment match \(r=e^{-t}\), \(\phi=0\). For \(s=t\), \(q_{t,t}/\sqrt t\) is uniformly comparable to \((x^2+t)^{-1}\) on \([-R,R]\) and tends to \(1/(\pi x^2)\) for \(x\ne0\). For small \(t\), the absolute logarithm of \(x^2+t\) is bounded by a constant plus \(2|\log|x||+2\log(1+|x|)\) off zero. The bounds on \(g_t\) therefore dominate the integrand of \(D(H_t\Vert P_{e^{-t},0})+\tfrac12\log t\) by a Gaussian times a polynomial and an integrable logarithm at zero. Its limit is \(\int g(\log g+\log\pi+\log x^2)\,dx=\tfrac12\log\pi-\log2-\tfrac12-\gamma\), since \(\mathbb E\log X^2=-\gamma\) for \(X\sim N(0,2)\).

With \(q=e^{-t}\), the radius equation becomes \(r/(1-r^2)=\sum_{n\ge1}q^{n^2}r^{n-1}\). This is analytic near \((r,q)=(0,0)\) with nonzero derivative of the stationarity residual in \(r\). The analytic root is odd in \(q\) (the equation is invariant after changing both signs) and, by comparing coefficients through degree five, is \(q-q^3+3q^5+O(q^7)\). The leading unmatched coefficient is \(q^4-r^2=-q^2+o(q^2)\) in the second harmonic, and the contribution of every other harmonic together is \(o(q^2)\) in uniform norm. Both densities tend uniformly to one, so Taylor expansion of the divergence gives \(\tfrac12\int(H_t-P)^2\,d\mu\,(1+o(1))=q^4(1+o(1))\).

## Verification
The included `checker.py` (Python, NumPy, SciPy) tests the scalar crossing and limiting constants, direct circle KL quadratures, and the two asymptotic regimes. The 92 recorded diagnostics are finite numerical checks, not proofs of global uniqueness or of any asymptotic limit.

## Relationship to prior work and limitations
The claim concerns the unique forward-KL projection of a **single** wrapped normal onto the wrapped Cauchy family, with exact heat-time laws. It does not cover mixtures, reverse KL, other losses, or non-heat Fourier sequences. Bailey's thesis compares wrapped normal and wrapped Cauchy models for mixtures, mainly under squared \(L^2\) discrepancy and with numerical KL comparisons in Appendix C1. Bailey and Codling study the emergence of wrapped Cauchy structure in mixed directional models. Otani and Matsuda study circular projections under Wasserstein loss and give KL formulas for von Mises and wrapped Cauchy inputs. The [squared-\(L^2\) heat-to-Poisson calibration](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-optimal-heat-to-poisson-calibration-on-the-circle-uniqueness-str--ef5e05ae5838/RESULT.md) uses the same families but a different loss; its small-time scale constant is about \(1.07774\), and its minimum squared error diverges rather than approaching a finite limit. No comprehensive priority claim is made.

## References
- J. D. Bailey, *Modelling and Analysis of Individual Animal Movement*, University of Essex PhD thesis (public repository deposit 8 January 2020), chapter 6 and appendix C1. https://repository.essex.ac.uk/26383/1/Thesis_2%281%29.pdf
- J. D. Bailey and E. A. Codling, *Emergence of the wrapped Cauchy distribution in mixed directional data* (2020). https://doi.org/10.1007/s10182-020-00380-7
- J. González-Pérez, *Hölder classes via semigroups and Riesz transforms* (2022). https://doi.org/10.1007/s00209-022-02982-0
- N. Otani and T. Matsuda, *Wasserstein projection estimators for circular distributions* (2026). https://link.springer.com/article/10.1007/s41884-026-00214-6
