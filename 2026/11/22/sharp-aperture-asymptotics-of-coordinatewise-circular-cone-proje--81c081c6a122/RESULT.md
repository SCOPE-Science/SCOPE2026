# Sharp aperture asymptotics of coordinatewise circular-cone projection

## Finding
Let \(d\ge2\) be an integer and \(\kappa>0\). Let \(P_{d,\kappa}\) be Euclidean nearest-point projection in \(\mathbb R^{d+1}\) onto the circular cone
\[
K_{d,\kappa}=\{(t,x)\in\mathbb R\times\mathbb R^d:t\ge\kappa\|x\|_2\}.
\]
Measure both input and output differences in the coordinate maximum norm, and set
\[
L_d(\kappa)=\sup_{z\ne z'}\frac{\|P_{d,\kappa}(z)-P_{d,\kappa}(z')\|_\infty}{\|z-z'\|_\infty}.
\]
Put \(h_d(s)=s\sqrt{d-1}\sqrt{1-s^2}\). The **exact finite-dimensional coefficient** is
\[
L_d(\kappa)=\max\{1,A_d(\kappa),B_d(\kappa),C_d(\kappa)\},
\]
where
\[
\begin{aligned}
A_d(\kappa)&=\frac{\kappa(\kappa+\sqrt d)}{1+\kappa^2},\\
B_d(\kappa)&=\max_{0\le s\le1}\frac{\kappa s+s^2+h_d(s)}{1+\kappa^2},\\
C_d(\kappa)&=\max_{0\le s\le1}\left[1+\frac{\kappa s+\kappa^2(h_d(s)-s^2)}{1+\kappa^2}\right].
\end{aligned}
\]
The two scalar maximizations are over compact intervals and yield exact constants without enumerating all input vectors.

More significantly, define
\[
g(\kappa)=\frac{\max\{\kappa,1/2,\kappa^2/2\}}{1+\kappa^2}.
\]
Then the following **uniform, all-aperture bound** holds for every \(d\ge2\), \(\kappa>0\):
\[
\boxed{0\le \frac{L_d(\kappa)}{\sqrt d}-g(\kappa)\le\frac{3}{2\sqrt d}.}
\]
Thus, even when the aperture depends on dimension,
\[
\lim_{d\to\infty}\inf_{\kappa>0}\frac{L_d(\kappa)}{\sqrt d}=\frac25.
\]
The continuous limiting aperture profile \(g\) has exactly **two global minimizers**, \(\kappa=1/2\) and \(\kappa=2\), both with value \(2/5\). Any sequence of nearly minimizing apertures (whose normalized coefficients approach \(2/5\)) necessarily approaches this two-point set. The dominant limiting derivative row has three regimes: spatial radial for \(0<\kappa<1/2\), axial for \(1/2<\kappa<2\), and spatial tangent for \(\kappa>2\). At the thresholds the adjacent mechanisms tie at leading order; no finite-dimensional exact crossover is asserted.

## Assumptions and scope
All coordinates, projections and norms are real and finite-dimensional. Spatial dimension is \(d\), ambient dimension \(d+1\). The map is the **Euclidean** metric projector, not a nearest-point map for the maximum norm. The half-aperture angle of the cone is \(\arctan(1/\kappa)\). The Lipschitz constant is the supremum of all distinct-input ratios. The claim does not assert existence of distinct inputs achieving that supremum.

## Proof
**1. Exact projection formula.** Write \(r=\|x\|_2\), with \(r>0\). Orthogonal projection onto a ray through \((\kappa,u)\), \(\|u\|_2=1\), reduces to one scalar problem. The angular minimization picks \(u=x/r\). Consequently
\[
P_{d,\kappa}(t,x)=
\begin{cases}
(t,x),&t\ge\kappa r,\\
(0,0),&t\le-r/\kappa,\\
(\kappa q,q x/r),&-r/\kappa<t<\kappa r,
\end{cases}
\qquad q=\frac{\kappa t+r}{1+\kappa^2}.
\]
The formula extends continuously across both boundaries and at \(r=0\), where the projection is \((\max\{t,0\},0)\). The middle region is open, and for every unit vector \(u\) its full range of radial parameters is realizable.

**2. Exact derivative reduction.** In the middle region set \(u=x/r\), \(c=(1+\kappa^2)^{-1}\) and \(\rho=(1+\kappa t/r)c\). Then \(0<\rho<1\) and differentiation gives
\[
DP_{d,\kappa}=
\begin{pmatrix}
\kappa^2c&\kappa c u^{\mathsf T}\\
\kappa c u&c uu^{\mathsf T}+\rho(I_d-uu^{\mathsf T})
\end{pmatrix}.
\]
It is affine in \(\rho\), so each absolute row sum is convex in \(\rho\) and is bounded by its larger endpoint value. At \(\rho=0\), the derivative is the rank-one orthogonal projector \(vv^{\mathsf T}/(1+\kappa^2)\) with \(v=(\kappa,u)\). At \(\rho=1\), it is the rank-\(d\) orthogonal projector \(I_{d+1}-ww^{\mathsf T}/(1+\kappa^2)\) with \(w=(1,-\kappa u)\). Both endpoint derivatives are limits of derivatives at open middle-region points, so neither bound is artificial.

The axial row sum at either endpoint is \(\kappa(\kappa+\|u\|_1)/(1+\kappa^2)\). Its exact maximum is \(A_d(\kappa)\), by Cauchy--Schwarz. For spatial row \(i\), write \(s=|u_i|\) and \(H=\sum_{j\ne i}|u_j|\). At the \(\rho=0\) endpoint the row sum is \(s(\kappa+s+H)/(1+\kappa^2)\); at \(\rho=1\) it is \(1+[\kappa s+\kappa^2(sH-s^2)]/(1+\kappa^2)\). For each \(s\in[0,1]\), Cauchy--Schwarz gives \(H\le\sqrt{d-1}\sqrt{1-s^2}\), with equality when the other coordinate magnitudes are equal. Every such \(s\) and equality configuration is realizable for \(d\ge2\). Thus the exact derivative supremum is the displayed maximum of \(1,A_d,B_d,C_d\).

Because a Euclidean metric projector is globally Euclidean-Lipschitz, its restriction to every line segment is absolutely continuous. Away from the piecewise-smooth boundaries the derivative bound applies almost everywhere; one can alternatively integrate along generic translated segments and pass to the limit by continuity. This proves the global maximum-norm upper bound. Conversely, an interior differentiability point and a row-sign perturbation produce local ratios arbitrarily close to its absolute row sum. Letting middle-region parameters approach either endpoint proves the matching global lower bound.

**3. Uniform high-dimensional envelope.** Denote the three leading profiles by
\[
a(\kappa)=\frac{\kappa}{1+\kappa^2},\quad b(\kappa)=\frac1{2(1+\kappa^2)},\quad c(\kappa)=\frac{\kappa^2}{2(1+\kappa^2)}.
\]
Then \(A_d/\sqrt d\in[a,a+1/\sqrt d]\). The bound \(0\le s\sqrt{1-s^2}\le1/2\) implies
\[
B_d\le \sqrt d\,b+\frac{\kappa+1}{1+\kappa^2},\qquad
C_d\le \sqrt d\,c+1+\frac{\kappa}{1+\kappa^2}.
\]
The auxiliary bounds \((\kappa+1)/(1+\kappa^2)\le(1+\sqrt2)/2<3/2\) and \(\kappa/(1+\kappa^2)\le1/2\) therefore give \(L_d/\sqrt d\le g+3/(2\sqrt d)\). For the matching lower bound, \(A_d/\sqrt d\ge a\). Evaluating the scalar objectives at \(s=1/\sqrt2\) gives \(B_d\ge\sqrt d\,b\) and \(C_d\ge\sqrt d\,c\): the required inequalities follow from \(\sqrt d-\sqrt{d-1}<1\) and positivity of the remaining terms. Hence \(L_d/\sqrt d\ge\max\{a,b,c\}=g\).

**4. Aperture optimization.** Direct comparison of \(a,b,c\) yields
\[
g(\kappa)=
\begin{cases}
\frac1{2(1+\kappa^2)},&0<\kappa\le1/2,\\
\frac{\kappa}{1+\kappa^2},&1/2\le\kappa\le2,\\
\frac{\kappa^2}{2(1+\kappa^2)},&\kappa\ge2.
\end{cases}
\]
The outer branches are strictly decreasing and increasing, respectively; the middle branch rises to \(1/2\) at \(\kappa=1\) and falls thereafter. Its only global minima are \(1/2\) and \(2\), both yielding \(2/5\). The uniform bound lets one take the infimum over all \(\kappa>0\), not merely fixed apertures. It also forces the distance of any asymptotically minimizing sequence from the two-point minimizer set to vanish, since \(g\) is bounded strictly away from \(2/5\) outside neighborhoods of those points, including at \(\kappa\to0\) and \(\kappa\to\infty\). This completes the proof.

## Verification
Run `python3 verify.py` with Python 3.8 or newer; no third-party dependencies are needed. The checker evaluates the exact cone projection, compares analytic Jacobians against centered finite differences at smooth points, tests two-input Lipschitz inequalities, and checks the uniform envelope numerically in several dimensions and apertures. It reports 400 Jacobian configurations, 400 distinct-input pairs and 15 envelope comparisons. Numerical evidence corroborates the derivation; the universal assertions follow from the proof, not from finite sampling.

## Relationship to prior work
Zhou, Chen and Mordukhovich (2014) derive the generalized projector derivatives for circular cones. In particular, their orthogonal-projector representation (Proposition 4.2) supplies the derivative building blocks used here, but does not optimize their coordinate row-sum norms across all apertures and dimensions. Zhang and Liu (2018) use explicit circular-cone projectors in a convergence analysis of projection neural networks; their Lyapunov stability is not coordinatewise Lipschitz stability of the projector. Thinh (2020) establishes calm B-differentiability and complementarity applications, again without the sharp induced maximum-norm envelope. A separately published standard Lorentz-cone result determines the \(\kappa=1\) special case, including a finite-dimensional output-row transition; that special case does not determine the all-aperture optimizer or the two reciprocal high-dimensional minimizing apertures. A published result for \(\ell_p\)-metric projection onto planar scaled cones is about a different ambient norm and dimension. This comparison does not exclude older equivalent work stated in different coordinates.

## Limitations
The exact scalar formula leaves two one-variable maximizations and does not classify finite-dimensional crossover apertures or finite-input attainment. The double-minimum statement concerns normalized stability as dimension grows, not exact finite-dimensional optimum aperture values. No results are claimed for elliptical cones, non-Euclidean nearest-point projection, or other input/output coordinate systems. The novelty assessment depends on the literature inspected and is not a claim of exhaustiveness.

## References
1. J. Zhou, J.-S. Chen, B. S. Mordukhovich, *Variational analysis of circular cone programs*, Optimization 64 (2015), first publicly available 2014, https://doi.org/10.1080/02331934.2014.951043 .
2. Y. Zhang, H. Liu, *A Projection Neural Network for Circular Cone Programming*, Mathematical Problems in Engineering (2018), first published 2018-06-10, https://doi.org/10.1155/2018/4607853 .
3. V. D. Thinh, *On the calm B-differentiability of projector onto circular cone and its applications*, Science & Technology Development Journal 23(4) (2020), published 2020-10-10, https://doi.org/10.32508/stdj.v23i4.2426 .
4. *Sharp coordinatewise Lipschitz transition for Euclidean Lorentz-cone projection*, published mathematical result, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-coordinatewise-lipschitz-transition-for-euclidean-lorentz--2d1b9aa4230e .
5. *Exact planar stability and nonexpansivity rigidity for \(\ell_p\) projections onto scaled Lorentz cones*, published mathematical result, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-planar-stability-and-nonexpansivity-rigidity-for-ell-p-pro--fbfc40872e9c .
