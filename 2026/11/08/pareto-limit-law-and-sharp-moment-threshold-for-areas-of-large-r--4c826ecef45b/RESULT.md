# Pareto limit law and sharp moment threshold for areas of large random hyperbolic triangles

## Finding

**Theorem.** In hyperbolic space \(\mathbb H^d\) of constant curvature \(-1\), fix any integer \(d\geq 2\). Let \(X_1,X_2,X_3\) be independent points sampled uniformly by hyperbolic \(d\)-volume from a geodesic ball of radius \(R\). Let \(A_R\) be the hyperbolic area of their geodesic triangle, measured in the unique totally geodesic plane through them. Then \(0<A_R<\pi\) almost surely. Set \(\kappa=d-1\).

Independently sample directions \(U_1,U_2,U_3\) uniformly from \(S^{d-1}\) and independent Pareto random variables \(Y_i\) with \(\Pr(Y_i>y)=y^{-\kappa}\) for \(y\geq1\). Define \(s_{ij}=\|U_i-U_j\|/2\) and, for each permutation \(\{i,j,k\}=\{1,2,3\}\), \(a_i=2s_{jk}/(s_{ij}s_{ik})\). All denominators are positive almost surely. The scaled area deficit has the nondegenerate limiting law

\[
 e^R(\pi-A_R)\ \Longrightarrow\ W_d:=\sum_{i=1}^3 a_iY_i.
\]

**Conditional distribution and tail.** Given the three directions, \(W_d\) is the convolution of three independent Pareto variables with scales \(a_1,a_2,a_3\), and

\[
\lim_{t\to\infty}t^{\kappa}\Pr(W_d>t\mid U_1,U_2,U_3)=\sum_{i=1}^3a_i^{\kappa}\qquad\text{almost surely in the directions}.
\]

**Sharp global moment threshold.** For every real \(p>0\),

\[
\mathbb E[W_d^p]<\infty\quad\Longleftrightarrow\quad p<d-1.
\]

Thus in dimension \(2\) the limiting deficit has infinite mean, while in dimension \(3\) its mean is finite and its variance is infinite. These are properties of the *limiting variable*; no convergence of moments of the finite-radius variables is asserted.

## Assumptions and scope

The center of the ball is fixed but arbitrary by hyperbolic homogeneity. The triangle is formed by the three pairwise minimizing geodesic segments. For \(d>2\), its area means intrinsic two-dimensional hyperbolic area in their span, not \(d\)-dimensional volume. Degenerate collinear triples or coincident radial directions are null events. All limits take \(R\to\infty\) at fixed \(d\). The probability law is volume-uniform in the *ball*; sampling on its boundary gives a different radial coefficient.

## Proof

**1. A joint boundary-layer coupling.** In geodesic polar coordinates at the ball center, independent radii have cumulative distribution

\[
 F_R(r)=\frac{\int_0^r\sinh^{\kappa}u\,du}{\int_0^R\sinh^{\kappa}u\,du},\qquad 0\le r\le R,
\]

and are independent of the directions, which are independent and Haar-uniform on \(S^{d-1}\). Since \(\int_0^R\sinh^{\kappa}u\,du\sim e^{\kappa R}/(2^{\kappa}\kappa)\), for fixed \(x\geq0\) one has \(F_R(R-x)\to e^{-\kappa x}\). In the common-quantile coupling \(r_{i,R}=F_R^{-1}(V_i)\), where the independent \(V_i\) are uniform on \((0,1)\), this implies

\[
 R-r_{i,R}\longrightarrow E_i=-\kappa^{-1}\log V_i\quad\text{almost surely},
\]

where the \(E_i\) are independent exponentials of rate \(\kappa\), independent of the fixed sampled directions. Their exponentials \(Y_i=e^{E_i}\) are the claimed Pareto variables.

**2. Pairwise distances and angle asymptotics.** Let \(b_{ij}=d_{\mathbb H}(X_i,X_j)\), and let \(\theta_{ij}\) be the angle at the center between the directions \(U_i,U_j\). The hyperbolic cosine law gives the exact identity

\[
\cosh b_{ij}=\cosh(r_i-r_j)+2\sinh r_i\sinh r_j\,s_{ij}^{2},\qquad s_{ij}=\sin(\theta_{ij}/2).
\]

Along the coupling, \(r_i\to\infty\), while all \(s_{ij}\) are fixed and strictly positive almost surely. Therefore

\[
 b_{ij}=r_i+r_j+2\log s_{ij}+o(1).
\]

Denote the triangle angle at \(X_i\) by \(\alpha_i\); let \(h=(b_{12}+b_{13}+b_{23})/2\). The exact hyperbolic half-angle identity is

\[
 \sin^2\!\left(\frac{\alpha_i}{2}\right)
 =\frac{\sinh(h-b_{ij})\sinh(h-b_{ik})}{\sinh b_{ij}\sinh b_{ik}}.
\]

Substitute the preceding side asymptotics. In particular,

\[
 h-b_{ij}=r_k+\log\frac{s_{ik}s_{jk}}{s_{ij}}+o(1),
\]

with its analogous expression for \(h-b_{ik}\). As all the arguments of the hyperbolic sines tend to infinity, direct cancellation yields

\[
\sin\!\left(\frac{\alpha_i}{2}\right)=e^{-r_i}\frac{s_{jk}}{s_{ij}s_{ik}}(1+o(1)),\qquad
 \alpha_i=2e^{-r_i}\frac{s_{jk}}{s_{ij}s_{ik}}(1+o(1)).
\]

Here each \(o(1)\) is pathwise with the sampled radial offsets and directions held fixed; no uniformity near coincident directions is claimed.

**3. Area limit.** Gauss–Bonnet gives \(\pi-A_R=\alpha_1+\alpha_2+\alpha_3\). Hence the coupling above yields pathwise

\[
 e^R(\pi-A_R)\longrightarrow
 \sum_{i=1}^3\frac{2s_{jk}}{s_{ij}s_{ik}}e^{E_i}=W_d.
\]

Almost-sure convergence under this coupling proves the asserted convergence in distribution.

**4. Conditional tail.** Fix admissible directions. For independent Pareto variables and positive constants \(a_i\), each summand has tail \(\Pr(a_iY_i>t)=(a_i/t)^{\kappa}\) once \(t>a_i\). The union of individual exceedances gives a lower limit \(\sum a_i^{\kappa}\). For an upper bound, fix \(\varepsilon>0\). Either some summand exceeds \((1-\varepsilon)t\), or, if the sum exceeds \(t\), at least two summands exceed a positive constant multiple of \(t\) (depending only on \(\varepsilon\)). By independence the latter event is \(O(t^{-2\kappa})\). Let \(\varepsilon\downarrow0\) to get the exact constant. Integrating no conditional constant over directions is asserted here: that integral may diverge.

**5. Sharp moment cutoff.** The chordal triangle inequality \(s_{jk}\le s_{ij}+s_{ik}\) implies

\[
 a_i\le 2(s_{ij}^{-1}+s_{ik}^{-1}).
\]

For a Haar pair of directions in \(S^{d-1}\), the angular separation has density proportional to \(\sin^{d-2}\theta\), so \(\Pr(s_{ij}<\delta)=O_d(\delta^{d-1})\) as \(\delta\downarrow0\). Consequently \(\mathbb E[a_i^p]<\infty\) for \(0<p<\kappa\). Also \(\mathbb E[Y_i^p]=\kappa/(\kappa-p)\) exactly for \(0<p<\kappa\), and these factors are independent. The inequality \((x_1+x_2+x_3)^p\le 3^{\max\{p-1,0\}}\sum x_i^p\) proves \(\mathbb E[W_d^p]<\infty\) in this range. Conversely, \(W_d\ge a_1Y_1\), with \(a_1>0\) independent of \(Y_1\) and \(\mathbb E[Y_1^p]=\infty\) for \(p\ge\kappa\), proving divergence at and above the threshold.

## Verification

The standalone `check_hyperbolic.py` samples the actual volume-uniform radial law and Haar directions for three dimensions \(d=2,3,5\) and three radii \(R=5,7,9\). It computes all three exact hyperbolic angles via the half-angle identity and separately constructs the limiting Pareto mixture from coupled uniform variates. It verifies convergence on nondegenerate compact-coordinate samples and includes an equilateral-direction normalization check. These numerical experiments corroborate, but do not prove, the assertions for infinite \(R\) or the moment cutoff. Run with `python check_hyperbolic.py` and dependencies `numpy`, `scipy`.

## Relationship to prior work

Orsingher and Toaldo (2013, DOI below, hyperbolic section) analyze a randomized geodesic-ray model and an area law for hyperbolic *right* triangles, not three independent hyperbolic-volume-uniform vertices in growing balls. Bao and Chen (2014, DOI below, Section 2) give deterministic area formulas for hyperbolic triangles, without the sampled-ball limiting distribution. The basic hyperbolic cosine law, half-angle identities, and Gauss–Bonnet formula are classical inputs, not new results. An existing generic asymptotic formula for three hyperbolic distances would not alone provide the stochastic angular–Pareto area law or its integrability threshold without further arguments.

## Limitations

This result proves weak convergence, an explicit conditional limiting tail, and the moment threshold for the limit only. It does **not** prove convergence of finite-radius moments, uniform-in-angle asymptotics, or an unconditional exact tail constant of \(W_d\). The conditional tail coefficient need not be integrable over directions. Historical priority is provisional: additional older literature on random hyperbolic triangles or ideal boundaries could imply parts of the statement. This is not an independent mathematical validation.

## References

1. E. Orsingher and B. Toaldo, *Shooting randomly against a line in Euclidean and non-Euclidean spaces*, Stochastics (online 2013-02-19). DOI: https://doi.org/10.1080/17442508.2012.749260. An accessible full preprint is available from Sapienza University of Rome's institutional site.
2. H. Bao and X. Chen, *A New Hyperbolic Area Formula of a Hyperbolic Triangle and Its Applications*, Journal of Mathematics (published 2014-08-13). DOI: https://doi.org/10.1155/2014/838497.
