# Three precision regimes for one-site gradient-enhanced Matérn quadrature

## Finding
Let \(X\) be a centered stationary Gaussian process on the real line with unit-variance Matérn-\(3/2\) covariance \(K_\lambda(s,t)=(1+\lambda|s-t|)e^{-\lambda|s-t|}\), \(\lambda>0\), and let \(J=\int_0^1X(t)\,dt\). At one predetermined site \(x\in[0,1]\), two independent Gaussian-noise channels may read \(X(x)\) and its mean-square derivative \(X'(x)\), with nonnegative allocated precisions \(p,q\) summing to \(P>0\). A zero precision means that channel is omitted; a positive precision \(r\) means additive noise variance \(1/r\), in the fixed dimensionless physical units specified here. The estimator is the posterior mean of \(J\).

**Theorem.** For every \(\lambda>0\), all sufficiently large finite budgets \(P\) have exactly one optimal design: \(x=1/2\), \(p=P\), \(q=0\). At the concrete decay \(\lambda=8\), there are three distinct budget regimes: for all sufficiently small \(P>0\), the only optimal designs are \((x,p,q)=(0,0,P)\) and \((1,0,P)\); at \(P=1/20\), **every** globally optimal design has \(p>0\) and \(q>0\); and at all sufficiently large \(P\), the sole optimum is the midpoint value-only design. The intermediate-budget assertion is global: it excludes every purely value-based or purely gradient-based design, not just two particular competitors. Moreover, the mixed-only property persists throughout an open neighborhood of \((\lambda,P)=(8,1/20)\). No location or full classification of the mixed optima is claimed.

This establishes a genuine pure-gradient / mixed / pure-value transition with increasing *absolute* total precision under a single co-located sensor design. It does not assert exact phase boundaries or claim that the three regimes are the only possible intermediate behaviors.

## Assumptions and scope
The Gaussian process is defined on \(\mathbb R\), so derivatives are meaningful even when their observation site is an endpoint of \([0,1]\). The Matérn-\(3/2\) kernel is once mean-square differentiable with \(\operatorname{Var}(X(x))=1\), \(\operatorname{Var}(X'(x))=\lambda^2\), and \(\operatorname{Cov}(X(x),X'(x))=0\). Observation noises are mutually independent and independent of the process. The function and derivative channels are charged in their **absolute noise precision** (not standardized to their different marginal variances); changing the channel's physical units or cost modifies the conclusion. Only one common site is permitted; separate-site measurements, adaptive designs and nonlinear observations are outside the scope.

Write
\[
\begin{aligned}
 a_\lambda(x)&=\frac{4-(2+\lambda x)e^{-\lambda x}-(2+\lambda(1-x))e^{-\lambda(1-x)}}{\lambda},\\
 b_\lambda(x)&=(1+\lambda x)e^{-\lambda x}-(1+\lambda(1-x))e^{-\lambda(1-x)}.
\end{aligned}
\]
These equal \(\operatorname{Cov}(J,X(x))\) and \(\operatorname{Cov}(J,X'(x))\). The exact Bayes-risk reduction is
\[
 G_\lambda(P;x,p)=\frac{a_\lambda(x)^2p}{1+p}+\frac{b_\lambda(x)^2(P-p)}{1+\lambda^2(P-p)},\quad 0\le p\le P.
\]
Consequently \(\operatorname{Var}(J\mid\text{observations})=\operatorname{Var}(J)-G_\lambda(P;x,p)\), with
\[
\operatorname{Var}(J)=\frac{2(2\lambda-3+(\lambda+3)e^{-\lambda})}{\lambda^2}.
\]
The objective is continuous on a compact design set, so a global optimum exists at every \(P>0\).

## Proof
1. **Exact Gaussian reduction.** Differentiating the stationary kernel gives the derivative variance \(\lambda^2\) and zero same-site cross-covariance. The two noisy Gaussian readings are thus independent. Integrating the kernel and its derivative against \(J\) gives \(a_\lambda,b_\lambda\) above, and Gaussian conditioning adds the two orthogonal explained-variance terms. Reflection \(x\mapsto1-x\) preserves \(a_\lambda\) and changes the sign of \(b_\lambda\). Therefore it suffices to optimize on \(0\le x\le1/2\).

2. **A strict noiseless domination lemma.** On \([0,1/2)\), \(b_\lambda(x)>0\), \(a'_\lambda(x)=b_\lambda(x)\), and
\[
 b'_\lambda(x)=-\lambda^2\bigl(xe^{-\lambda x}+(1-x)e^{-\lambda(1-x)}\bigr).
\]
A direct rearrangement yields
\[
 a_\lambda(x)+\frac{b'_\lambda(x)}{\lambda^2}
 =\frac2\lambda\bigl[2-K_\lambda(x,0)-K_\lambda(x,1)\bigr]>0.
\]
Thus \(F_\lambda(x):=a_\lambda(x)^2+b_\lambda(x)^2/\lambda^2\) satisfies
\[
 F'_\lambda(x)=2b_\lambda(x)\left(a_\lambda(x)+\frac{b'_\lambda(x)}{\lambda^2}\right)>0\qquad(0\le x<1/2).
\]
Writing \(a_c=a_\lambda(1/2)\), we have \(F_\lambda(x)<F_\lambda(1/2)=a_c^2\) at every \(x<1/2\). At the midpoint the derivative channel has zero covariance with the integral.

3. **Value-only midpoint at every sufficiently large budget, for every \(\lambda>0\).** Set \(H(x)=a_c^2-a_\lambda(x)^2\) and, for \(x<1/2\),
\[
 r_\lambda(x)=\frac{b_\lambda(x)^2}{\lambda^2H(x)}.
\]
The preceding strict inequality shows \(0\le r_\lambda(x)<1\). This ratio extends continuously to the midpoint: if \(d=-b'_\lambda(1/2)=\lambda^2e^{-\lambda/2}>0\), then Taylor expansion gives
\[
\lim_{x\uparrow1/2}r_\lambda(x)=\frac{d}{\lambda^2 a_c}=\frac{e^{-\lambda/2}}{a_c}<1,
\]
where the last inequality follows from the positive expression for \(a_\lambda(1/2)+b'_\lambda(1/2)/\lambda^2\). Compactness gives \(\rho_\lambda:=\max_{0\le x\le1/2}r_\lambda(x)<1\). Since \(p\le P\) and \(q=P-p\), for every \(x<1/2\),
\[
 G_\lambda(P;x,p)\le a_\lambda(x)^2\frac P{1+P}+\frac{b_\lambda(x)^2}{\lambda^2}
 =a_c^2\frac P{1+P}-H(x)\left(\frac P{1+P}-r_\lambda(x)\right).
\]
If \(P>\rho_\lambda/(1-\rho_\lambda)\), this is strictly below the midpoint value-only performance \(a_c^2P/(1+P)\). At \(x=1/2\), the derivative term vanishes and \(a_c^2p/(1+p)\) is strictly maximized at \(p=P\). Reflection completes uniqueness.

4. **Gradient-only endpoints at all sufficiently small budgets when \(\lambda=8\).** On \([0,1/2]\), \(a_8(x)\) is strictly increasing, while \(b_8(x)\) is strictly decreasing to zero. Write \(a_c=a_8(1/2)=1/2-3e^{-4}/2<1/2\), and \(b_e=b_8(0)=1-9e^{-8}>247/256>1/2\), using \(e>2\). With \(p=rP\), the normalized captured variance
\[
 \Phi(P,x,r)=\frac{r a_8(x)^2}{1+Pr}+\frac{(1-r)b_8(x)^2}{1+64P(1-r)}
\]
converges uniformly on the compact square \([0,1/2]\times[0,1]\) as \(P\downarrow0\) to \(r a_8(x)^2+(1-r)b_8(x)^2\). Because \(b_e>a_c\), this limit has exactly one maximum \((x,r)=(0,0)\). Thus every finite-budget maximizer approaches this corner as \(P\downarrow0\). At the corner, the two one-sided partial derivatives of \(\Phi\) are strictly negative: \(\partial_x\Phi(0,0,0)=2b_e b'_8(0)<0\) and \(\partial_r\Phi(0,0,0)=a_8(0)^2-b_e^2<0\). By continuity both remain strictly negative throughout a fixed neighborhood for all sufficiently small \(P\). Hence the maximizing corner is *exactly* \((0,0)\) for all sufficiently small positive budgets, not merely asymptotically. Reflecting gives the other endpoint, and there are no additional optima.

5. **A rigorous mixed-only budget at \(\lambda=8\).** Take \(P=1/20\) and the feasible mixed witness \(x=0\), \(p=3/1000\), \(q=47/1000\). Write \(u=e^{-8}\), \(v=e^{-4}\), \(a_e=1/4-5u/4\), \(b_e=1-9u\), and \(a_c=1/2-3v/2\). The best value-only design is the midpoint, giving \(G_V=a_c^2/21\); the best derivative-only design is an endpoint, giving \(G_D=b_e^2/84\). The witness gives
\[
 G_M=\frac{3a_e^2}{1003}+\frac{47b_e^2}{4008},\qquad
 G_M-G_D=\frac{3a_e^2}{1003}-\frac{5b_e^2}{28056}.
\]
The elementary bounds \(2<e<11/4\) imply \(0<u<1/256\) and \(v>1/64\). Therefore
\[
 G_M-G_D>\frac{3(251/1024)^2}{1003}-\frac5{28056}
 =\frac{5507441}{3688388100096}>0,
\]
and
\[
 G_D-G_V>\frac{(247/256)^2}{84}-\frac{(61/128)^2}{21}
 =\frac{491}{1835008}>0.
\]
All pure-function and pure-gradient designs are dominated by the mixed witness. Existence of a global maximizer then forces every optimum to have \(p>0\) and \(q>0\). In particular, a simplistic rule always spending the entire budget on just one type of measurement is false. Because the witness and the two pure-channel optimum values depend continuously on \((\lambda,P)\), the two strict inequalities persist on an open parameter neighborhood of \((8,1/20)\) (keeping the witness precision \(p=3/1000\) and using \(q=P-p>0\)). This concludes the theorem.

## Verification
Run \(\texttt{python verify.py}\) with Python 3. The standalone checker independently integrates the kernel for the function/derivative covariances, checks the Gaussian-conditioning reduction at sample parameters, checks the monotonicity identity on supplemental grids, and checks the *exact rational* positive margins used in Step 5. The global statements are proved symbolically in Steps 2–5 and do not rely on finite grids. For \(\lambda=8\), \(P=1/20\), the captured variances are approximately \(0.01063244440855616\) (best value-only), \(0.01183298557198699\) (best gradient-only), and \(0.01184215766670178\) (displayed feasible mixed witness).

## Relationship to prior work
Wu, Aoi, and Pillow (arXiv:1704.00060, first public 31 March 2017), Sections 3 and 5.2, formulate derivative-enhanced Gaussian process regression and Bayesian quadrature and demonstrate empirical benefits, but their accessible original full text does not state a total absolute-precision, co-located Matérn-\(3/2\) global design theorem or this pure/mixed/pure regime witness. Karvonen, Kanagawa, and Särkkä (arXiv:1812.08509, first public 20 December 2018), Sections 2–4, study univariate Bayesian quadrature weights, positivity and magnitude, rather than allocation between value and derivative channels. The related earlier two-site Matérn-\(3/2\) quadrature result optimizes reflection-paired *function values* with equal noise, not a single common site with two distinct measurement functionals. Inference formulas alone do not imply the present global allocation classes, while the precise proof above establishes them for the stated model. No absolute guarantee of historical priority is claimed.

## Limitations
The intermediate mixed optimum's exact location and the transition thresholds are not determined. The proof of small-budget endpoint optimality uses the particular length-scale parameter \(\lambda=8\); the high-budget result is uniform in \(\lambda>0\) only in the sense of applying separately to each fixed parameter (not with a uniform threshold). At boundary sites, derivative measurements refer to the process on the real line. Modifying relative channel costs, standardizing derivative precision to derivative prior variance, changing the kernel, relaxing co-location, or permitting adaptive observations changes the problem. Independent mathematical and historical-priority audits have not been performed.

## References
- A. Wu, M. C. Aoi, J. W. Pillow, *Exploiting gradients and Hessians in Bayesian optimization and Bayesian quadrature*, arXiv:1704.00060 (first public 2017-03-31). https://arxiv.org/abs/1704.00060
- T. Karvonen, M. Kanagawa, S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, arXiv:1812.08509 (first public 2018-12-20). https://arxiv.org/abs/1812.08509
- F. de Roos, A. Gessner, P. Hennig, *High-Dimensional Gaussian Process Inference with Derivatives*, ICML 2021. https://proceedings.mlr.press/v139/de-roos21a.html
