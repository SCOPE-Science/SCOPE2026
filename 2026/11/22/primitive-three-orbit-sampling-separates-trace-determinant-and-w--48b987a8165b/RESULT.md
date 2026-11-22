# Primitive three-orbit sampling separates trace, determinant, and worst-case Gaussian uncertainty

## Finding

**Theorem (a sharp three-orbit conflict).** Let \(d\ge3\) be an integer with \(3\mid d\), put \(N=3d\), and let \(\lambda>0\). On the real Hilbert space \(\ell^2(\mathbb Z/N\mathbb Z)\), let \(S\) be the coordinate cyclic shift and define the positive self-adjoint precision operator
\[
Q_\lambda=\lambda I+2I-S-S^*.
\]
For a centered Gaussian forcing vector \(w\) with covariance \(Q_\lambda^{-1}\), make noiseless observations of the three coordinates indexed by \(E_s=\{0,s,2s\}\pmod N\), where the sampling step is **primitive**, meaning \(\gcd(s,N)=1\). Let \(\Sigma_s\) be the conditional covariance of the other \(N-3\) coordinates. Then, among **all** primitive steps:

- The mean-squared error \(\operatorname{Tr}(\Sigma_s)\) and conditional generalized variance \(\det(\Sigma_s)\) attain exactly the two reflected optimal site sets given by \(s\equiv\pm(d-1)\pmod N\).
- The worst-direction mean-squared error \(\|\Sigma_s\|_{\mathrm{op}}\) attains exactly the two reflected optimal site sets given by \(s\equiv\pm(d+1)\pmod N\).

These optimal sets are disjoint, even though **all three unrestricted** criteria are optimized by the unattainable equispaced three-site set \(\{0,d,2d\}\). The primitive-step condition ensures that the underlying one-coordinate dynamical orbit spans the full \(N\)-dimensional state space when observed for \(N\) consecutive times; the unrestricted equispaced step \(d\) instead has orbit length three.

Set
\[
\theta=\operatorname{arcosh}(1+\lambda/2),\qquad
F_\theta(g)=\frac{g\coth(g\theta)-\coth\theta}{2\sinh\theta}.
\]
The exact restricted optima, with the criteria all **minimized**, are
\[
\begin{aligned}
A_{\rm prim}&=2F_\theta(d-1)+F_\theta(d+2),\\
D_{\rm prim}&=\frac{\sinh^3\theta}{\sinh^2((d-1)\theta)\sinh((d+2)\theta)},\\
E_{\rm prim}&=\frac{1}{\lambda+2-2\cos(\pi/(d+1))}.
\end{aligned}
\]
Their unrestricted counterparts are
\[
A_{\rm free}=3F_\theta(d),\qquad
D_{\rm free}=\frac{\sinh^3\theta}{\sinh^3(d\theta)},\qquad
E_{\rm free}=\frac{1}{\lambda+2-2\cos(\pi/d)}.
\]
In particular, \(A_{\rm prim}>A_{\rm free}\), \(D_{\rm prim}>D_{\rm free}\), and \(E_{\rm prim}>E_{\rm free}\). The exact A-penalty obeys
\[
\lim_{\lambda\downarrow0}(A_{\rm prim}-A_{\rm free})=1,
\]
and the competing nearest primitive steps satisfy
\[
\big[2F_\theta(d-1)+F_\theta(d+2)\big]
-\big[2F_\theta(d+1)+F_\theta(d-2)\big]
=-\frac{8d}{15}\lambda+O_d(\lambda^2).
\]
The last expansion is at each fixed integer \(d\), not uniformly as \(d\) grows.

## Assumptions and scope

The graph is the **unweighted simple cycle** of \(N\ge9\) vertices, with one unit-conductance edge between successive vertices. The precision is the exact \(Q_\lambda\) above; no additional observation noise, unknown covariance parameters, nonuniform weights, or complex Gaussian normalization is assumed. A primitive step is a generator of \(\mathbb Z/N\mathbb Z\). The three observations are the first three points of its orbit, not three independently placed sensors. The determinant acts on the conditional covariance of the \(N-3\) **unobserved** coordinates, so dimensions agree across designs. We make no claim about the reconstruction error of the original dynamical state in a forced trajectory; the criteria are for the forcing posterior.

## Proof

**1. Conditional compression and the path spectrum.** For any observed set \(E\), put \(U=(\mathbb Z/N\mathbb Z)\setminus E\). Completing the square in the positive Gaussian precision density shows directly that \(\operatorname{Cov}(w_U\mid w_E)=(Q_\lambda)_{U,U}^{-1}\). If the three positive clockwise distances between consecutive points of \(E\) are \(g_1,g_2,g_3\), the principal compression is the orthogonal sum of three Dirichlet path matrices \(T_{g_i-1}\), each with diagonal \(\lambda+2\), off-diagonal \(-1\), and empty blocks when \(g_i=1\). The nonempty path block has eigenvalues
\[
\lambda+2-2\cos(k\pi/g),\qquad 1\le k<g.
\]
The second-order determinant recurrence, initialized by \(\det T_0=1\), gives \(\det T_{g-1}=\sinh(g\theta)/\sinh\theta\). Differentiating its logarithm in \(\lambda\) yields the exact trace \(\operatorname{Tr} T_{g-1}^{-1}=F_\theta(g)\), and the smallest eigenvalue gives the largest conditional covariance eigenvalue. Therefore
\[
\begin{aligned}
\operatorname{Tr}(\Sigma_E)&=\sum_{i=1}^3F_\theta(g_i),\\
\det(\Sigma_E)&=\prod_{i=1}^3\frac{\sinh\theta}{\sinh(g_i\theta)},\\
\|\Sigma_E\|_{\rm op}&=\frac1{\lambda+2-2\cos(\pi/\max_i g_i)}.
\end{aligned}
\]

**2. Three orbit sites have only one independent gap.** Replacing \(s\) by \(N-s\) reflects the observed set. With \(t=\min(s,N-s)\), its three clockwise gap lengths (up to cyclic order) are precisely \(t,t,N-2t\). The primitive condition is \(\gcd(t,N)=1\). Since \(N=3d\) and \(3\mid d\), the distances \(d-1\) and \(d+1\) are both primitive. Their respective gap triples are \((d-1,d-1,d+2)\) and \((d+1,d+1,d-2)\). The ideal \(t=d\) is nonprimitive because \(\gcd(d,N)=d>1\).

**3. A general strict-curvature comparison.** Suppose a smooth function \(h:(0,\infty)\to\mathbb R\) satisfies \(h''>0\) and \(h'''<0\). Then \(G_h(t)=2h(t)+h(3d-2t)\) is strictly decreasing for \(t<d\) and strictly increasing for \(t>d\), because \(G'_h(t)=2[h'(t)-h'(3d-2t)]\). Of the admissible integer steps on each side, the closest are \(d-1\) and \(d+1\). Writing \(\Delta^2h(k)=h(k+1)-2h(k)+h(k-1)\), direct algebra gives
\[
G_h(d-1)-G_h(d+1)=\Delta^2h(d+1)-\Delta^2h(d-1)<0,
\]
as \(h'''<0\) makes \(\Delta^2h(k)\) strictly decreasing. Hence \(t=d-1\) uniquely minimizes \(G_h\) over primitive steps.

Apply the comparison first to \(h(x)=F_\theta(x)\). Strict convexity follows from
\[
\frac{d^2}{dx^2}[x\coth x]
=2\operatorname{csch}^2x\,(x\coth x-1)>0.
\]
For its strictly negative third derivative, the required sign reduces to positivity of \(H(y)=y(\cosh y+2)-3\sinh y\) for \(y>0\). Indeed \(H(0)=H'(0)=H''(0)=0\), while \(H'''(y)=y\sinh y>0\). This establishes \(F_\theta''>0\) and \(F_\theta'''<0\) at all positive arguments and proves the A-optimal step.

Apply the same argument to \(h(x)=-\log\sinh(\theta x)\). Here \(h''(x)=\theta^2\operatorname{csch}^2(\theta x)>0\), and \(h'''(x)=-2\theta^3\operatorname{csch}^2(\theta x)\coth(\theta x)<0\). As the log determinant is a constant plus \(G_h(t)\), this proves the D-optimal step.

**4. The opposite worst-direction choice.** The operator-norm criterion is strictly increasing in the longest cyclic gap \(\max(t,3d-2t)\). For admissible \(t<d\), that maximum is at least \(d+2\), while the admissible \(t=d+1\) has maximum \(d+1\). Every \(t>d+1\) has maximum at least \(d+2\). Thus the unique optimal length is \(t=d+1\), proving the E-optimal assertion.

**5. Strict premiums and the small-mass boundary.** The strict convexity of \(F_\theta\) and of \(-\log\sinh(\theta\cdot)\) implies both A and D strictly exceed their balanced triples at \(t=d\); the longer maximum gap gives strict E loss. As \(\lambda\downarrow0\), \(\theta^2=\lambda+O(\lambda^2)\) and, for each fixed integer \(g\),
\[
F_\theta(g)=\frac{g^2-1}{6}
-\theta^2\left(\frac{g^4-1}{90}+\frac{g^2-1}{36}\right)+O_g(\theta^4).
\]
Substitution gives the claimed unit A-penalty and the first-order left/right difference \(-8d\lambda/15\). The singular \(\lambda=0\) Gaussian prior is **not** included; these are limits of proper priors.

## Verification

A finite diagnostic in `check_triple.py` independently constructs conditional precision blocks and compares direct matrix inversions with the hyperbolic formulas for sample cycle sizes and masses. It also searches primitive steps for the global minimizers of all three objectives, using high-precision arithmetic to distinguish exponentially close values. Run `python check_triple.py` with Python 3, NumPy, and mpmath installed. This finite test is supplementary; the analytic curvature and gap arguments prove the theorem for all permitted \(d\) and \(\lambda\).

For a concrete instance, take \(d=3\), \(N=9\), \(\lambda=1\). The trace/determinant choice \(t=2\) has gaps \((2,2,5)\), A-risk \(76/33\) and determinant \(1/495\). The worst-direction choice \(t=4\) has gaps \((4,4,1)\), A-risk \(50/21\) and determinant \(1/441\). Their operator norms are approximately \(0.7236067977\) and \(0.6306019375\), respectively, from the path eigenvalue formulas.

## Relationship to prior work

Giribet and Feldberg, *Augmented Dynamical Sampling under unmodeled Forcing* (2026, arXiv:2611.17137v1), establish Gaussian residual conditioning and separate forcing visibility from nominal observability. Their results motivate the primitive-orbit restriction, but they do not optimize the three-site restricted posterior trace, determinant and spectral norm, nor exhibit their contradictory optimizers. An earlier pinned-cycle extremizer theorem already identifies unrestricted balanced configurations, the exact path-block inverse trace, and general heat-trace/resolvent trace extrema. Those facts are **credited**, not claimed as new; they do not determine the primitive-orbit winners or the conflict between trace/determinant and operator-norm objectives. Dasgupta, Mukhopadhyay and Keith (2020) and cited earlier Ornstein–Uhlenbeck kriging literature likewise establish equispaced optimal designs under different geometric constraints. Baz, Alonso and Pérez-Fernández (2023) study circulant Gaussian Markov correlation/precision matrices without this restricted-design classification. These differences concern actual hypotheses and implications, not merely terminology.

## Limitations

The exact claim is restricted to \(N=3d\) with \(3\mid d\), three consecutive coordinates of a **primitive** shift orbit, noiseless observations, and the massive nearest-neighbor cycle prior. This is an infinite arithmetic family rather than a full classification of every sensor budget and modulus. It is not a new general Gaussian-conditioning identity, a new unrestricted pinned-cycle theorem, or a statement about noisy residuals or the full initial-state reconstruction error. High-precision finite diagnostics cannot establish uniqueness without the proof. Older optimal-design results in a broader specialized form might imply parts of the restricted theorem; a human bibliographic audit remains appropriate.

## References

1. Juan I. Giribet and Serena Feldberg, *Augmented Dynamical Sampling under unmodeled Forcing*, arXiv:2611.17137v1, first posted 12 November 2026. https://arxiv.org/html/2611.17137v1
2. Subhadra Dasgupta, Siuli Mukhopadhyay and Jonathan Keith, *Optimal designs for some bivariate cokriging models*, arXiv:2004.13967, first posted 29 April 2020. https://arxiv.org/abs/2004.13967
3. Baz, Alonso and Pérez-Fernández, *Correlation matrices of Gaussian Markov random fields over cycle graphs*, Linear Algebra and its Applications 663 (2023), 32–61. https://doi.org/10.1016/j.laa.2022.12.028
4. Andreas Krause, Ajit Singh and Carlos Guestrin, *Near-Optimal Sensor Placements in Gaussian Processes: Theory, Efficient Algorithms and Empirical Studies*, Journal of Machine Learning Research 9 (2008), 235–284. https://jmlr2020.csail.mit.edu/papers/v9/krause08a.html
5. *Universal heat-trace and Schatten-resolvent extremizers on pinned cycles*, earlier mathematical result (publication details not independently established); the free-placement and inverse-trace formulas are credited prior work.
