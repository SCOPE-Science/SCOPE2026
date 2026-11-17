# Exact minimax compromise for circumscribed random polytopes and a sixth-order sharp separation

## Finding

For a smooth strictly convex body \(K\subset\mathbb R^d\), \(d\ge2\), there is a unique boundary-sampling density which minimizes the **worst of the two separately normalized leading expected errors** in volume and mean width of a circumscribed random polytope. The exact minimax penalty is a one-dimensional concave maximization, with both errors equal at the optimum. For every nonball its value is strictly greater than one.

More precisely, let \(\kappa>0\) denote Gauss curvature and \(dS\) boundary area. Define the two *individually optimal* probability densities
\[
f=\frac{\kappa^{1/(d+1)}}{\int_{\partial K}\kappa^{1/(d+1)}\,dS},\qquad
g=\frac{\kappa^{d/(d+1)}}{\int_{\partial K}\kappa^{d/(d+1)}\,dS},\qquad
p=\frac{d+1}{d-1}.
\]
For positive continuous boundary densities \(\rho\) of total mass one, put
\[
R_V(\rho)=\int_{\partial K}f^p\rho^{1-p}\,dS,\qquad
R_W(\rho)=\int_{\partial K}g^p\rho^{1-p}\,dS.
\]
These are respectively the volume and mean-width leading expected-error coefficients divided by their *separately attainable minima*. Define
\[
H_K(\lambda)=\int_{\partial K}\bigl(\lambda f^p+(1-\lambda)g^p\bigr)^{1/p}\,dS,\qquad 0\le\lambda\le1.
\]
If \(K\) is not a Euclidean ball, there is a **unique** \(\lambda_*\in(0,1)\), characterized by
\[
\int_{\partial K}(f^p-g^p)\bigl(\lambda_*f^p+(1-\lambda_*)g^p\bigr)^{1/p-1}\,dS=0,
\]
and the exact best worst relative error is
\[
\boxed{\min_\rho\max\{R_V(\rho),R_W(\rho)\}=H_K(\lambda_*)^p>1.}
\]
The minimizer is unique and equals
\[
\boxed{\rho_* =\frac{(\lambda_*f^p+(1-\lambda_*)g^p)^{1/p}}{H_K(\lambda_*)},\qquad R_V(\rho_*)=R_W(\rho_*)=H_K(\lambda_*)^p.}
\]
For a Euclidean ball the two densities coincide, the unique optimal sampler is uniform, and the minimax value is one; every \(\lambda\in[0,1]\) then maximizes \(H_K\).

The **equal-weight average-error bound** corresponds to fixing \(\lambda=1/2\). It is generally not sharp. This difference can be determined exactly to the first nonzero order for the planar oval with support function
\[
h_t(\theta)=1-\frac t3\cos(2\theta),\qquad 0<|t|<1,
\]
whose curvature radius is \(r_t(\theta)=h_t+h_t''=1+t\cos(2\theta)\). For sufficiently small nonzero \(t\),
\[
\boxed{\lambda_*(t)=\frac12+\frac5{96}t^2+O(t^4),\qquad
\mathcal Q(K_t)-H_{K_t}(1/2)^3=\frac{25}{55296}t^6+O(t^8)>0.}
\]
Here \(\mathcal Q(K_t)\) denotes the exact minimax value. Thus the natural fixed half-and-half average bound misses a strictly positive, explicitly quantified sixth-order term, even arbitrarily close to a disk.

## Assumptions and scope

The dimension \(d\) is any integer at least two. The convex body \(K\) is compact, full-dimensional and of class \(C_+^2\): its boundary is twice continuously differentiable, and all principal curvatures are positive. The admissible sampling densities are strictly positive continuous functions on \(\partial K\), of integral one with respect to \(dS\). Fix any enclosing cube \(Q\) containing \(K\) in its interior, and independently sample \(N\) boundary points according to \(\rho\,dS\). Intersect their outer supporting halfspaces with \(Q\) to obtain a bounded circumscribed random polytope. The asymptotic coefficients are those of the expected excess Euclidean volume and mean width as \(N\to\infty\), separately normalized by their individual minima. The entire optimization concerns these leading coefficients for fixed densities, **not** finite-\(N\) expected errors or sampling laws depending on \(N\). The constants in the random-polytope asymptotics cancel under this normalization.

The support-family example is planar and centrally symmetric. Its support function is \(C^\infty\), and \(r_t>0\) for \(|t|<1\), so these ovals satisfy the required positive-curvature hypotheses. Angles are outer-normal directions, not polar-radius directions.

## Proof

**1. Reduction to normalized risks.** The classical circumscribed-random-polytope asymptotics, for each fixed continuous positive \(\rho\), have leading curvature weights \(\kappa^{1/(d-1)}\) for excess volume and \(\kappa^{d/(d-1)}\) for excess mean width, both multiplied by \(\rho^{-2/(d-1)}\). Put \(p=(d+1)/(d-1)\). By Hölder's inequality the separately minimizing densities are precisely \(f\) and \(g\), and the minimized integrals are the respective \(p\)-th powers of their normalizing integrals. Dividing by these minima yields exactly \(R_V\) and \(R_W\) above. Equality in each individual Hölder bound forces \(\rho=f\) or \(\rho=g\), respectively.

**2. Weighted-minimax duality.** Write \(w_\lambda=\lambda f^p+(1-\lambda)g^p\). For every \(0\le\lambda\le1\), strict Hölder inequality with its equality characterization gives
\[
\min_{\rho>0,\,\int\rho=1}\bigl(\lambda R_V(\rho)+(1-\lambda)R_W(\rho)\bigr)
=\left(\int_{\partial K}w_\lambda^{1/p}\,dS\right)^p=H_K(\lambda)^p,
\]
with unique minimizer \(\rho_\lambda=w_\lambda^{1/p}/H_K(\lambda)\). Thus \(\min_\rho\max(R_V,R_W)\ge\max_\lambda H_K(\lambda)^p\).

If \(f\ne g\), then
\[
H_K''(\lambda)=\frac1p\left(\frac1p-1\right)
\int_{\partial K}(f^p-g^p)^2 w_\lambda^{1/p-2}\,dS<0.
\]
Since \(H_K(0)=H_K(1)=1\), strict concavity gives a unique interior maximizer \(\lambda_*\), strictly above one. Its derivative equation is the one displayed in the Finding. At the unique \(\rho_*\), direct differentiation gives
\[
R_V(\rho_*)-R_W(\rho_*)=H_K(\lambda_*)^{p-1}\,pH_K'(\lambda_*)=0.
\]
Their common value is the \(\lambda_*\)-weighted average, which by the Hölder equality above equals \(H_K(\lambda_*)^p\). This proves the matching minimax upper bound and existence. Every alternative minimax optimizer would minimize the strictly convex positive weighted sum at \(\lambda_*\); the Hölder equality case forces it to equal \(\rho_*\). The equality \(f=g\) holds exactly when Gauss curvature is constant, which for a smooth compact strictly convex hypersurface characterizes Euclidean balls. The ball case is immediate.

**3. An explicit planar curvature model.** Let \(h_t=1-(t/3)\cos2\theta\). Since \(h_t+h_t''=r_t=1+t\cos2\theta>0\) for \(|t|<1\), it is the support function of a smooth strictly convex oval. Write \(\langle u\rangle=(2\pi)^{-1}\int_0^{2\pi}u(\theta)\,d\theta\); the boundary measure satisfies \(dS=r_t\,d\theta\), and \(\kappa=r_t^{-1}\). Define
\[
A_t=\langle r_t^{2/3}\rangle,\qquad B_t=\langle r_t^{1/3}\rangle,
\quad W_t(\theta,\lambda)=\lambda r_t A_t^{-3}+(1-\lambda)B_t^{-3}.
\]
Substituting the source-optimal densities \(f=r_t^{-1/3}/(2\pi A_t)\) and \(g=r_t^{-2/3}/(2\pi B_t)\) gives the exact, dimensionless scalar objective
\[
H_t(\lambda)=\langle r_t^{1/3}W_t(\theta,\lambda)^{1/3}\rangle.
\]
The \(\theta\mapsto\theta+\pi/2\) change replaces \(t\) by \(-t\), so \(H_t\) and all its \(\lambda\)-derivatives are even analytic functions of \(t\) near zero, uniformly in \(\lambda\in[0,1]\).

**4. Exact sixth-order calculation.** Put \(c=\cos2\theta\). The necessary trigonometric moments are \(\langle c\rangle=\langle c^3\rangle=0\), \(\langle c^2\rangle=1/2\), \(\langle c^4\rangle=3/8\). Binomial Taylor expansion through fourth order gives
\[
\begin{aligned}
A_t&=1-\frac{t^2}{18}-\frac{7t^4}{648}+O(t^6),
& A_t^{-3}&=1+\frac{t^2}6+\frac{11t^4}{216}+O(t^6),\\
B_t&=1-\frac{t^2}{18}-\frac{5t^4}{324}+O(t^6),
& B_t^{-3}&=1+\frac{t^2}6+\frac{7t^4}{108}+O(t^6).
\end{aligned}
\]
Let \(D_t=r_t A_t^{-3}-B_t^{-3}\) and \(S_t=(r_t A_t^{-3}+B_t^{-3})/2\). In particular,
\[
D_t=tc+\frac{t^3}6c-\frac{t^4}{72}+O(t^5),\qquad
S_t=1+\frac t2c+\frac{t^2}6+\frac{t^3}{12}c+\frac{25t^4}{432}+O(t^5).
\]
The precise derivative formulas are
\[
H_t'(1/2)=\frac13\langle r_t^{1/3} D_t S_t^{-2/3}\rangle,
\qquad
H_t''(1/2)=-\frac29\langle r_t^{1/3}D_t^2S_t^{-5/3}\rangle.
\]
Expanding these products and integrating with the listed moments yields
\[
H_t'(1/2)=\frac5{864}t^4+O(t^6),\qquad
H_t''(1/2)=-\frac19t^2+O(t^4).
\]
(The displayed derivative identities and the explicit \(A_t,B_t,D_t,S_t\) expansions provide direct coefficient-by-coefficient reproducibility without needing a computer algebra package.) Since the derivative divided by \(t^2\) is analytic in \(t^2\), with limiting \(\lambda\)-derivative \(-1/9\), the analytic implicit-function theorem gives
\[
\lambda_*(t)-\frac12=-\frac{H_t'(1/2)}{H_t''(1/2)}+O(t^4)
=\frac5{96}t^2+O(t^4).
\]
Taylor's theorem around \(\lambda=1/2\), using \(\lambda_*-1/2=O(t^2)\) and \(H_t^{(3)}=O(t^3)\), gives
\[
H_t(\lambda_*)-H_t(1/2)=\frac{[H_t'(1/2)]^2}{-2H_t''(1/2)}+O(t^8)
=\frac{25}{165888}t^6+O(t^8).
\]
Here the stronger even remainder follows from analyticity in \(t^2\). Because both values of \(H_t\) tend to one, cubing yields
\[
H_t(\lambda_*)^3-H_t(1/2)^3=\frac{25}{55296}t^6+O(t^8),
\]
proving strict separation for all sufficiently small nonzero \(t\). This is a positive correction **to the previously known averaged-risk lower bound**, not a new estimate for the separately optimal volume or mean-width errors.

## Verification

The standalone standard-library script `verify_circumscribed_tradeoff.py` performs 16,384-node midpoint quadrature, independent scalar bisection of the minimax stationarity equation, and direct evaluations of *both* normalized curvature risks at the proposed angular sampling density. It checks their equality and the sharp sixth-order improvement numerically on multiple noncircular ovals. The script prints `CIRCUMSCRIBED_TRADEOFF_NUMERICAL_CHECKS_OK` when every assertion passes. Symbolic series can be regenerated from the displayed binomial expansions and cosine moments in Proof step 4. Finite quadrature only corroborates the analytic result.

## Relationship to prior work

Böröczky and Reitzner (2004), Theorems 1 and 3, establish the separate asymptotic circumscribed volume and mean-width functionals and their optimal densities; these are **inputs**, not claimed discoveries. Hoehner (2026), Theorem 2.4 and Proposition 3.5, proves their simultaneous-optimality rigidity and uniquely minimizes the **average** of two normalized errors. Theorem 3.6 obtains the averaged value as a lower bound for the **maximum**, and Remark 3.7 explicitly does **not** identify it as the exact minimax value. The strict new separation is what distinguishes these two objectives. Earlier published research on inscribed-polytope minimax sampling establishes an analogous duality method for different sampling bodies and intrinsic-volume weights, not the present circumscribed sharp sixth-order comparison.

## Limitations

The exact scalar minimax formula is generally an integral-root characterization; no elementary closed form for an arbitrary convex body is asserted. The explicit sixth-order separation is only for a specified smooth planar oval family and only as \(t\to0\), not a universal all-curvature quantitative gap. The output concerns leading \(N^{-2/(d-1)}\) expected-error coefficients at fixed densities, not a finite-sample optimal law. The universal minimax optimization is a new application of a familiar Hölder/duality technique; originality concerns the **circumscribed** risk and the sharp gap from the published equal-weight bound, not the basic duality method itself. Historical priority may be affected by unindexed convex-approximation literature; no independent mathematical audit has been carried out.

## References

1. S. Hoehner, *Simultaneous random polytope approximation characterizes the Euclidean ball*, arXiv:2602.18547v2 (13 October 2026), originally posted 20 February 2026; especially Theorems 2.3–2.4, Proposition 3.5, Theorem 3.6 and Remark 3.7. https://arxiv.org/html/2602.18547v2
2. K. Böröczky, Jr. and M. Reitzner, *Approximation of smooth convex bodies by random circumscribed polytopes*, Annals of Applied Probability 14 (2004), 239–273, Theorems 1 and 3. DOI 10.1214/aoap/1075828053. Open manuscript: https://www.renyi.hu/~carlos/randomapprox.pdf
3. *A universal near-sphere price for simultaneous intrinsic-volume sampling*, public mathematical record 20a687e8594a (18 October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-universal-near-sphere-price-for-simultaneous-intrinsic-volume--20a687e8594a (inscribed model, not circumscribed).
4. *Sharp spherical-harmonic cost of sharing random-polytope sampling laws*, public mathematical record 4e45a188ddc4 (25 October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-spherical-harmonic-cost-of-sharing-random-polytope-samplin--4e45a188ddc4 (inscribed model).
5. *Unique minimax area–perimeter sampling law for random polygons in ellipses*, public mathematical record 179adc1046b6 (11 October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-unique-minimax-area-perimeter-sampling-law-for-random-polygons-i--179adc1046b6 (inscribed model).
