# Sharp squeezing threshold for three rotated Gaussian ambiguity windows

## Finding

For every radius \(R>0\), put \(c=\pi R^2\). Let \(a=e^s\geq1\) and take three unit-norm Gaussian windows with identical squeezing and fractional Fourier rotation angles \(0,\pi/3,2\pi/3\). Choose nonnegative observation weights \(w_0,w_1,w_2\) summing to one. Let \(\mathcal A g_j\) denote their centered ambiguity functions and define the worst squared-ambiguity response on the closed time-frequency disk by

\[
\mathcal M_R(s,w)=\min_{x^2+\xi^2\leq R^2}\sum_{j=0}^2w_j|\mathcal A g_j(x,\xi)|^2.
\]

The exact maximum over all \(s\geq0\) and all such weights undergoes a sharp transition at \(c=2\):

* For \(0<c\leq2\), the optimal value is \(e^{-c}\). Every optimal design is unsqueezed, \(s=0\), and any weights summing to one are optimal.
* For \(c>2\), there is exactly one optimal design: \(w_0=w_1=w_2=1/3\) and \(s=s_c>0\), where \(s_c\) is the unique positive solution of
\[
\frac{e^{3c\sinh(s_c)/2}-1}{1+2e^{3c\sinh(s_c)/2}}=\tanh(s_c).
\]
The sharp value then is
\[
\mathcal M_R^*=\frac{e^{-c\cosh s_c}}3\left(e^{-c\sinh s_c}+2e^{c\sinh s_c/2}\right).
\]
For \(c>2\), its worst points are exactly the six boundary points on the three unoriented axes at angles \(0,\pi/3,2\pi/3\).

The transition has cubic onset, and the optimal dilation has a finite limiting value:
\[
 s_c=(c-2)+O((c-2)^2),\qquad
 e^c\mathcal M_R^*=1+\frac{(c-2)^3}{6}+O((c-2)^4)
 \quad(c\downarrow2),
\]
\[
 e^{s_c}\longrightarrow\sqrt3,\qquad
 \mathcal M_R^*\sim\frac23e^{-\sqrt3 c/2}
 \quad(c\to\infty).
\]

## Assumptions and scope

The ambiguity convention is
\[
\mathcal A g(x,\xi)=\int_{\mathbb R}g(t+x/2)\overline{g(t-x/2)}e^{-2\pi i t\xi}\,dt.
\]
The normalized Gaussian is \(g_a(t)=(2a)^{1/4}e^{-\pi a t^2}\). Its fractional Fourier rotations are defined by their standard metaplectic action on time-frequency ambiguity magnitudes; the corresponding ambiguity ellipses are rotated by \(j\pi/3\). The theorem concerns the stated three fixed orientations, a common dilation \(a\geq1\), and unrestricted nonnegative weights with total one. The criterion is a deterministic multiplier margin, not a claim about uniform nonlinear phase-retrieval stability or about optimally choosing arbitrary angles.

If each window supplies independent whitened ambiguity-domain observations with relative precision \(w_j\), the local inverse-variance multiplier is proportional to the displayed sum of squared ambiguity magnitudes. This interpretation requires the stipulated noise model; the theorem itself requires no stochastic assumptions.

## Proof

**1. Gaussian normalization and disk reduction.** Completing a Gaussian square gives
\[
\mathcal A g_a(x,\xi)=e^{-\pi(a x^2+a^{-1}\xi^2)/2}.
\]
For a rotation by \(\alpha_j=j\pi/3\), in polar coordinates \((x,\xi)=r(\cos\phi,\sin\phi)\),
\[
|\mathcal A g_j(r\cos\phi,r\sin\phi)|^2
=e^{-\pi r^2[\cosh s+\sinh s\cos(2\phi-2\alpha_j)]}.
\]
Every term decreases strictly with \(r\geq0\). Therefore every disk minimum occurs on \(r=R\).

**2. Exact angular minimum for equal weights.** Put \(u=c\sinh s\), and let \(\vartheta=2\phi\). Apart from the common factor \(e^{-c\cosh s}\), the equal-weight angular sum is
\[
F_u(\vartheta)=\sum_{j=0}^2 e^{-u\cos(\vartheta-2\pi j/3)}.
\]
The three cosines are the roots of \(P_t(X)=X^3-3X/4-t/4\), where \(t=\cos(3\vartheta)\). For \(-1<t<1\) the roots are distinct. Implicit differentiation shows
\[
\frac{dF_u}{dt}=\frac14\sum_{P_t(x)=0}\frac{(-u)e^{-ux}}{P_t'(x)}
=\frac14[x_1,x_2,x_3]\bigl((-u)e^{-uX}\bigr)<0
\]
when \(u>0\). Indeed, the second divided difference is half the third derivative at an intermediate point, and that third derivative is \(-u^3e^{-uX}<0\). By continuity at double roots, the unique angular minima are where \(t=1\), i.e. \(\phi=j\pi/3\) modulo \(\pi\). Their cosine triple is \((1,-1/2,-1/2)\), so the minimum equals
\[
e^{-c\cosh s}\frac{e^{-u}+2e^{u/2}}3.
\]
When \(s=0\), every angle gives \(e^{-c}\).

**3. Optimal allocation is equal whenever squeezed.** At the three candidate worst directions \(\phi=k\pi/3\), the weighted response is
\[
e^{-c\cosh s}\bigl[w_ke^{-u}+(1-w_k)e^{u/2}\bigr].
\]
Their average is the equal-weight minimum from step 2. Thus any weights have disk minimum at most that average. Equal weights attain the bound. For \(u>0\), the three displayed values agree only when all \(w_k=1/3\); any unequal weights give a strictly smaller minimum. For \(s=0\), all allocations are identical.

**4. Unique scalar optimum and sharp threshold.** Set \(u=c\sinh s\). The logarithm of the best fixed-squeezing margin is
\[
L_c(u)=-\sqrt{c^2+u^2}+\log\frac{e^{-u}+2e^{u/2}}3.
\]
Define \(v(u)=(e^{3u/2}-1)/(1+2e^{3u/2})\). For \(u>0\), \(0<v(u)<1/2\), and
\[
L_c'(u)=v(u)-\frac{u}{\sqrt{c^2+u^2}}.
\]
A positive stationary point exists precisely when \(c=C(u):=u\sqrt{v(u)^{-2}-1}\). The function \(C\) is strictly increasing from \(2\) to infinity. To prove strict monotonicity, it suffices to verify \(u v'(u)<v(u)(1-v(u)^2)\). With \(y=e^{3u/2}>1\), this inequality is equivalent to
\[
(1+2y)\log y<(y-1)(y+2).
\]
For the difference of right and left sides, both its value and first derivative vanish at \(y=1\), while its second derivative equals \(1+(1-y^{-1})^2>0\) for \(y>1\). Finally \(v(u)\sim u/2\) at the origin and \(v(u)\to1/2\) at infinity, so \(C(0+)=2\) and \(C(u)\to\infty\). The derivative \(L_c'\) is negative everywhere when \(c\leq2\); when \(c>2\), it is positive before the sole solution of \(C(u)=c\) and negative after. Thus the stated maxima are global and unique in squeezing.

**5. Endpoint laws.** A Taylor expansion at \(s=0\) yields
\[
\log\bigl(e^c\mathcal M_R(s,(1/3,1/3,1/3))\bigr)
=\frac{c(c-2)}4s^2-\frac{c^3}{24}s^3+O(s^4).
\]
Dividing the stationary equation by \(s>0\) and expanding gives \(0=(c-2)/2-s/2+O((c-2)s+s^2)\); the implicit-function theorem therefore yields \(s_c=c-2+O((c-2)^2)\) as \(c\downarrow2\), proving the cubic law. As \(c\to\infty\), the stationary equation forces \(\tanh s_c\to1/2\), so \(s_c\to\operatorname{arctanh}(1/2)=\tfrac12\log3\). Its convergence is exponentially fast by \(1/2-v(u)=3/[2(1+2e^{3u/2})]\). Inserting this into the exact sharp margin gives \(\mathcal M_R^*\sim(2/3)e^{-\sqrt3 c/2}\).

## Verification

The standalone `check_three_gaussians.py` checks the key rational monotonicity identity symbolically; compares direct angular-grid minima with the exact formula; checks optimal squeezing against parameter grids across both regimes; and tests the critical and large-radius asymptotics. It reports `THREE_GAUSSIAN_DISK_MINIMAX_CHECKS_PASS 99` with Python, NumPy, SciPy and SymPy. The finite grid is corroborative only: the strict angular and squeezing statements are proved analytically above.

## Relationship to prior work

Alaifari and Yang, *Multi-Window Approaches for Direct and Stable STFT Phase Retrieval* (arXiv:2410.05486, first posted 2024-10-07), derive rotated dilated-Gaussian ambiguity ellipses, summed-ambiguity recovery and geometric coverage estimates (Section 2.1, Remark 2.1, equation (2.3)), followed by stability estimates (Section 3). Their results motivate the present family but do not give an optimum for the normalized squared-ambiguity multiplier under a three-window precision budget, the exact threshold \(\pi R^2=2\), or the limiting dilation \(\sqrt3\). The squared multiplier here is distinct from their sum of ambiguity amplitudes.

Hardin, Kendall and Saff (arXiv:1208.5261) prove optimality of equally spaced points for specified geodesically decreasing convex polarization kernels. That setting may illuminate the angular balancing step but does not determine the optimizing squeeze or the radial threshold. Grohs, Liehr and Rathmair (arXiv:2207.10620) treat lattice uniqueness of multiwindow STFT intensities, not this continuous ambiguity-multiplier minimax. The present result makes no assertion about arbitrary-angle global optimality or discrete-lattice phase-retrieval injectivity.

## Limitations

The result applies to exactly three prescribed equally spaced unoriented axes and a common squeeze, not to general window sets. Squared ambiguity magnitudes define the exact stated criterion, but the paper's amplitude-sum inversion and fully nonlinear phase retrieval are different problems. No uniform signal-level error bound is asserted. No complete historical priority guarantee is possible; an unlocated general theorem on Gaussian polarizations or exponential minimax might imply part or all of the result. The large-radius asymptotic optimizes a separate design for each radius rather than a single fixed design for every radius.

## References

1. R. Alaifari and Y. Yang, *Multi-Window Approaches for Direct and Stable STFT Phase Retrieval*, arXiv:2410.05486 (first posted 2024-10-07), later SIAM J. Appl. Math. 85 (2025), DOI 10.1137/24M1701332. Accessible author-uploaded full-text: https://www.researchgate.net/publication/384770463_Multi-Window_Approaches_for_Direct_and_Stable_STFT_Phase_Retrieval.
2. D. P. Hardin, A. P. Kendall and E. B. Saff, *Polarization optimality of equally spaced points on the circle for discrete potentials*, arXiv:1208.5261 (2012).
3. P. Grohs, L. Liehr and M. Rathmair, *Multi-window STFT phase retrieval: lattice uniqueness*, arXiv:2207.10620 (2022).
