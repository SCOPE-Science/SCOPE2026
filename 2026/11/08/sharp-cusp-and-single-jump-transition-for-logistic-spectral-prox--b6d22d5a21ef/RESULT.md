# Sharp cusp and single-jump transition for logistic spectral proximal maps

## Finding

Let \(a,\lambda>0\), and prescribe the logistic shrinker and its inverse-designed penalty by
\[
 f(s)=\frac{s}{1+\exp[-a(s/\lambda-1)]},\quad
 \phi(u)=\int_0^u\bigl(f^{-1}(v)-v\bigr)\,dv,
 \qquad s,u\geq0.
\]
For \(\beta>0\), consider the (possibly set-valued) scaled scalar proximal map
\[
 P_\beta(s)=\operatorname*{argmin}_{u\geq0}
 \left\{J_{\beta,s}(u):=\tfrac12(u-s)^2+\beta\phi(u)\right\},
 \qquad s\geq0.
\]
Let \(h(t)=t/[1+e^{-a(t-1)}]\), let \(t_a>1\) be the unique solution of
\[
 at_a\tanh\!\left(\frac{a(t_a-1)}2\right)=2,
\]
and set
\[
 L=h'(t_a)>1,\quad \rho=1-L^{-1},\quad
 \beta_c=\rho^{-1},\quad u_c=\lambda h(t_a),\quad
 D=-\frac{h'''(t_a)}{\lambda^2 L^4}>0.
\]
Then the following trichotomy holds **for every** \(a,\lambda>0\).

1. For \(0<\beta<\beta_c\), \(P_\beta(s)\) is a singleton for every \(s\geq0\), and its scalar output is globally Lipschitz with constant at most \((1-\beta\rho)^{-1}\). This is the source paper's strong-convexity regime.
2. At \(\beta=\beta_c\), \(P_{\beta_c}\) is **still single-valued at every input**, but is not locally Lipschitz at the unique critical input \(s_c=u_c+\beta_c\phi'(u_c)\). More precisely, with \(p(s)\) denoting its sole element,
\[
 p(s)-u_c=\left(\frac{6}{\beta_cD}\right)^{1/3}
 \operatorname{sgn}(s-s_c)|s-s_c|^{1/3}
 +o(|s-s_c|^{1/3})\quad (s\to s_c).
\]
3. For **each** \(\beta>\beta_c\), there is exactly one input \(s_\beta>0\) at which \(P_\beta(s_\beta)\) consists of **exactly two distinct global minimizers**, \(u_-(\beta)<u_+(\beta)\). At every other nonnegative input the global minimizer is unique. Thus every single-valued global-minimizer selection has a jump at \(s_\beta\). The stationary-point equation has precisely two fold inputs \(s_{\mathrm{lo}}(\beta)<s_{\mathrm{hi}}(\beta)\) enclosing \(s_\beta\). With \(\epsilon=\beta\rho-1\downarrow0\),
\[
 u_+(\beta)-u_-(\beta)
 =2\sqrt{\frac{6}{\beta_cD}}\,\epsilon^{1/2}
 +o(\epsilon^{1/2}),
\]
\[
 s_{\mathrm{hi}}(\beta)-s_{\mathrm{lo}}(\beta)
 =\frac43\sqrt{\frac{2}{\beta_cD}}\,\epsilon^{3/2}
 +o(\epsilon^{3/2}),
 \qquad
 s_\beta=\bigl(u_c+\beta\phi'(u_c)\bigr)+o(\epsilon^{3/2}).
\]
The transition also occurs in the matrix spectral proximal problem: a rank-one matrix with sole positive singular value \(s_\beta\) has at least two different aligned global minimizing matrices for the scaled penalty \(\Phi(X)=\sum_i\phi(\sigma_i(X))\).

## Assumptions and scope

All statements use exact real arithmetic and the particular logistic shrinker above, with the penalty **fixed by inverse design at unit proximal scale**. The parameter \(\beta\) is a subsequent multiplier of that fixed penalty. The scalar input and output are nonnegative. In the matrix observation, the matrix is real and the spectral sum is over its singular values. The result concerns global minimizers of an individual proximal subproblem, not trajectories of an iterative reconstruction scheme. The original algorithm uses the proximal scale \(\beta=\eta\alpha\), so the threshold has a direct interpretation for parameter choice.

## Proof

**1. Unique curvature maximizer.** Put \(\ell(t)=(1+e^{-a(t-1)})^{-1}\). Direct differentiation gives
\[
 h'(t)=\ell(t)+at\ell(t)(1-\ell(t))>0,
\]
\[
 h''(t)=a\ell(t)(1-\ell(t))\bigl[2+at(1-2\ell(t))\bigr].
\]
For \(0\leq t\leq1\) the bracket is positive. For \(t>1\), its sign is the sign of \(2-at\tanh[a(t-1)/2]\). The function \(t\mapsto at\tanh[a(t-1)/2]\) increases strictly from \(0\) to infinity on \((1,\infty)\). Therefore \(h'\) increases strictly to a unique maximum at \(t_a\), then decreases strictly to \(1\). Since \(h'(t_a)>1\) (equivalently, \(h(t)<t\) while \(t-h(t)\to0\)), the constants \(L,\rho,\beta_c\) above are well defined. At the maximum,
\[
 h'''(t_a)=a\ell_a(1-\ell_a)
 \left[a(1-2\ell_a)-2a^2t_a\ell_a(1-\ell_a)\right]<0,
 \qquad \ell_a=\ell(t_a)>\tfrac12.
\]

**2. Curvature of the induced penalty and its graph.** Since \(f(s)=\lambda h(s/\lambda)\), it is a smooth increasing bijection of \([0,\infty)\) onto itself, and
\[
 \phi'(u)=f^{-1}(u)-u,\qquad
 \phi''(u)=\frac{1}{f'(f^{-1}(u))}-1.
\]
Thus \(\phi''\) has its **unique strict global minimum** \(-\rho\) at \(u_c\), with \(\phi'''(u_c)=0\) and
\[
 \phi''''(u_c)=
 -\frac{f'''(\lambda t_a)}{L^4}
 =-\frac{h'''(t_a)}{\lambda^2L^4}=D>0.
\]
The stationarity equation for \(J_{\beta,s}\) is
\[
 T_\beta(u):=u+\beta\phi'(u)=s,
 \qquad
 T_\beta'(u)=1+\beta\phi''(u).
\]
Here \(T_\beta(0)=0\), \(T_\beta(u)\geq u\), and \(T_\beta(u)\to\infty\) with \(u\). Also \(J_{\beta,s}\) is coercive, so a global minimizer always exists. The map \(T_\beta\) has the explicit parametric representation
\[
 u=\lambda h(t),\qquad
 T_\beta(u)=\lambda\bigl[\beta t+(1-\beta)h(t)\bigr].
\]

**3. At and below the critical scale.** If \(\beta<\beta_c\), then \(T'_\beta\geq 1-\beta\rho>0\), proving strong convexity, unique global minimization and the stated inverse Lipschitz bound. At equality, \(T'_{\beta_c}\) is nonnegative and vanishes **only** at \(u_c\); integration of this derivative on every nontrivial interval shows \(T_{\beta_c}\) remains strictly increasing. Hence its inverse remains single-valued. Taylor's formula gives
\[
 T_{\beta_c}(u_c+v)-T_{\beta_c}(u_c)
 =\frac{\beta_cD}{6}v^3+O(v^4).
\]
Inverting this strictly increasing local cubic proves the displayed signed cubic-root law and failure of local Lipschitz regularity.

**4. Exactly two folds and one global-minimizer tie.** If \(\beta>\beta_c\), then \(\beta>1\) and
\[
 1<\frac{\beta}{\beta-1}<L.
\]
The strict unimodality of \(h'\) makes the equation \(h'(t)=\beta/(\beta-1)\) have precisely two positive solutions \(t_1<t_a<t_2\). They give positive turning points \(v_1=\lambda h(t_1)<v_2=\lambda h(t_2)\) of \(T_\beta\); the former is a strict local maximum and the latter a strict local minimum. Put
\[
 s_{\mathrm{lo}}=T_\beta(v_2),\qquad
 s_{\mathrm{hi}}=T_\beta(v_1).
\]
Then \(0<s_{\mathrm{lo}}<s_{\mathrm{hi}}\). For inputs strictly between them, \(T_\beta(u)=s\) has exactly three roots: a low local minimum \(l(s)\), an intermediate local maximum, and a high local minimum \(r(s)\) of \(J_{\beta,s}\). At the lower fold input, the low local minimum lies strictly below the (degenerate) upper stationary point: \(J'_{\beta,s_{\mathrm{lo}}}>0\) between them. At the upper fold input, the high local minimum lies strictly below the (degenerate) lower stationary point: \(J'_{\beta,s_{\mathrm{hi}}}<0\) between them. Define
\[
 \Delta(s)=J_{\beta,s}(r(s))-J_{\beta,s}(l(s)).
\]
The endpoint observations give \(\Delta(s_{\mathrm{lo}}+)>0\) and \(\Delta(s_{\mathrm{hi}}-)<0\). Differentiating the stationary values by the envelope rule yields
\[
 \Delta'(s)=l(s)-r(s)<0.
\]
Therefore there is exactly one \(s_\beta\in(s_{\mathrm{lo}},s_{\mathrm{hi}})\) with \(\Delta(s_\beta)=0\). At that input the two local minima are exactly the two global minimizers. At other inputs there is a unique global minimum, including at both fold endpoints. The equal-area characterization is
\[
 \int_{u_-(\beta)}^{u_+(\beta)}[T_\beta(u)-s_\beta]\,du=0.
\]
This also proves the discontinuity of any global-minimizer selection. (No dynamic hysteresis property is claimed.)

**5. Sharp critical exponents.** Write \(\epsilon=\beta\rho-1\), so \(\beta=\beta_c(1+\epsilon)\). Uniform Taylor expansion about \(u_c\) gives
\[
 T_\beta(u_c+v)-T_\beta(u_c)
 =-\epsilon v+\frac{\beta_cD}{6}v^3
 +O(\epsilon|v|^3+|v|^4).
\]
Solving its derivative for the two folds gives
\[
 v_{\mathrm{fold},\pm}
 =\pm\sqrt{\frac{2}{\beta_cD}}\epsilon^{1/2}
 +O(\epsilon),
\]
which yields the stated fold-input separation. Next put \(v=\epsilon^{1/2}z\) and \(s=T_\beta(u_c)+\epsilon^{3/2}q\). Using the identity \(J'_{\beta,s}=T_\beta-s\), uniformly for bounded \(z,q\),
\[
 \epsilon^{-2}\bigl[J_{\beta,s}(u_c+\epsilon^{1/2}z)-J_{\beta,s}(u_c)\bigr]
 =\frac{\beta_cD}{24}z^4-\frac12z^2-qz+O(\epsilon^{1/2}).
\]
The tie input lies between folds, so \(q\) is bounded. The limiting quartic has two equal-depth minima **only at** \(q=0\), where they are \(z=\pm\sqrt{6/(\beta_cD)}\); strict monotonicity of \(\Delta\) and continuous convergence of the two branches force the tie's \(q\to0\). Consequently the minimizer jump and tie-input expansions follow. All limits hold with fixed \(a,\lambda>0\) as \(\beta\downarrow\beta_c\) from above.

**6. Spectral consequence.** For a nonzero rank-one matrix \(Y=s_\beta pq^{\mathsf T}\) with unit vectors \(p,q\), the unitarily invariant proximal objective reduces by singular-vector alignment and von Neumann's trace inequality to the scalar objective. Both \(X=u_-(\beta)pq^{\mathsf T}\) and \(X=u_+(\beta)pq^{\mathsf T}\) attain its global minimum, and are different. Thus single-valuedness of the matrix scaled proximal map genuinely fails above \(\beta_c\), already at rank one.

## Verification

The standalone `verify.py` evaluates the unique maximum of \(h'\), both fold equations, the equal-area tie, the jump and fold-width scaling, and the critical cubic-root response using only the Python standard library. Run `python3 verify.py` in the directory containing this document. With \(a=4\), \(\lambda=1\), it obtains \(L\approx1.718092822612\), \(\beta_c\approx2.392577628561\), \(u_c\approx0.859046411306\), \(D\approx0.929930127555\). The script's finite precision checks supplement the analytic proof; they do not certify all real parameter values.

## Relationship to prior work

Yang, Wang and Yang [1, Sections 3–5] introduce exactly this logistic shrinker and inverse-designed penalty, prove \(\rho=1-L^{-1}\), and guarantee unique scaled proximal minimizers when \(\beta\rho<1\). Their results do **not** state uniqueness at equality, loss of uniqueness for every larger scale, a unique Maxwell/tie input, or the critical exponents proved here. The present result uses their analytic definitions and curvature identity but provides an additional complete classification of the scaling boundary.

Chartrand [2] develops the general inverse-design principle for other shrinkage families, without this particular logistic scaling and cusp. Lu et al. [3] treat set-valued proximal singular-value thresholding generally and allow multiple scalar proximal minimizers; their theorem provides generic monotonicity and spectral reduction, but not the location, uniqueness or critical size of the present family's jump. The general existence of multivalued nonconvex proximal mappings is not claimed as novel.

## Limitations

The result is a precise one-subproblem phenomenon; it neither establishes divergence of an iterative inverse-problem algorithm nor invalidates the descent guarantees in the source's admissible parameter regime. The matrix statement proves nonuniqueness by a rank-one input and does not classify all higher-rank minimizer multiplicities. The near-critical expansions are for fixed hardness and threshold, not uniform in the hard-threshold limit \(a\to\infty\).

## References

[1] G. Yang, Z. Wang, G. Yang, *Data-Driven Smooth-to-Hard Spectral Regularization for General Linear Inverse Problems*, arXiv:2610.21664v1, initially posted 2026-10-15, Sections 3–5. https://arxiv.org/html/2610.21664v1

[2] R. Chartrand, *Shrinkage mappings and their induced penalty functions*, ICASSP (2014), 1026–1029, doi:10.1109/ICASSP.2014.6853752. https://www.researchgate.net/publication/272790166_Shrinkage_mappings_and_their_induced_penalty_functions

[3] C. Lu, C. Zhu, C. Xu, S. Yan, Z. Lin, *Generalized Singular Value Thresholding*, AAAI (2015), arXiv:1412.2231, Sections 2–3. https://arxiv.org/abs/1412.2231
