# Sharp softmax local-step disagreement and its angular safeguard

## Finding
For a single classification example with a one-hot label, compare the infinitesimal-probe limits of the *so-dz* (quadratic cross-entropy) and *cs-dq* (linearized closest-softmax) steps of Bauwens, Krivodub and Zhang [1], along the negative cross-entropy gradient in **logit coordinates**. Their ratio is exactly the reciprocal squared cosine between the logit-gradient direction and its softmax response. It equals one in binary classification, but in three or more classes there is no finite uniform ratio bound.

For exactly three classes and a fixed true-class probability \(p\in(0,1)\), the *sharp* worst-case ratio is uniquely attained (up to exchanging the two incorrect classes) at the imbalance specified below. Its high-misclassification-probability limit is
\[
\lim_{p\downarrow0}p\sup_{q:q_1=p}\frac{\eta_{\mathrm{so}}}{\eta_{\mathrm{cs}}}=\frac1{12}.
\]
The proposed cosine-based per-example rejection rule in [1] has an exact safeguard interpretation in this limit: retaining only examples with cosine at least \(c\in(0,1)\) ensures \(\eta_{\mathrm{so}}/\eta_{\mathrm{cs}}\le c^{-2}\), and this bound is sharp for three classes when the true-class probability is free. The value \(c=1/4\) used in [1] yields the exact limiting retained-sample ceiling \(16\).

## Assumptions and scope
Let \(K\ge2\) be a finite number of classes, \(q\in(0,1)^K\) with \(\sum_iq_i=1\) the softmax probability vector, and \(y=e_1\) the true one-hot label (permuting classes changes nothing). Treat the logits \(z\in\mathbb R^K\) themselves as optimization variables, so a unit-direction scaling is **not** imposed: use the unnormalized descent direction \(d=y-q\ne0\) and the logit path \(z(h)=z+hd\). Every strictly positive probability vector is realized by finite logits. Define the softmax covariance \(H=\operatorname{diag}(q)-qq^\top\). Then \(q'(0)=Hd\), and the curvature of \(-\log q_1\) along the path at zero is \(d^\top Hd\).

Define the two positive local surrogate minimizers by
\[
\eta_{\mathrm{so}}=\frac{\|d\|^2}{d^\top Hd},\qquad
\eta_{\mathrm{cs}}=\frac{d^\top Hd}{d^\top H^2d}.
\]
They are precisely the zero-test-step limits of the probe estimators in equations (3) and (4) of [1] for the stated single-example identity-logit model. Denominators are positive because \(H\) is strictly positive on the zero-sum subspace and \(d\) is a nonzero vector in it. The claims concern these **local raw estimates**, *not* their finite-probe counterparts, minibatch aggregates, schedule modulation, momentum, clipping or actual finite-step loss decrease.

In the ternary case set
\[
p=q_1,\quad t=\frac{q_2-q_3}{q_2+q_3}\in(-1,1),\quad u=t^2\in[0,1),\quad D=p(u+3)^2+u(1-u).
\]
For a fixed \(p\), all \(u\in[0,1)\) are feasible, by taking \(q_2=(1-p)(1+t)/2\), \(q_3=(1-p)(1-t)/2\). Define \(u_0=6-\sqrt{33}\in(0,1)\). There exists a unique \(u_p\in(0,u_0)\) satisfying
\[
p(u_p+3)(u_p^2-12u_p+3)=u_p(1-u_p)^2.
\]

## Proof
**1. General equality and angular identity.** The local quadratic expansion of cross-entropy along \(z+hd\) is \(L(0)-h\|d\|^2+\tfrac12h^2d^\top Hd\). Linearizing softmax as \(q+hHd\), the squared label residual is \(\tfrac12\|d-hHd\|^2\). Differentiation gives the two displayed minimizers. Set
\[
\cos\phi=\frac{d^\top Hd}{\|d\|\,\|Hd\|}>0.
\]
Therefore
\[
\boxed{\frac{\eta_{\mathrm{so}}}{\eta_{\mathrm{cs}}}
=\frac{\|d\|^2d^\top H^2d}{(d^\top Hd)^2}
=\frac1{\cos^2\phi}\ge1.}
\]
Cauchy--Schwarz proves the inequality and equality holds exactly when \(Hd\) is proportional to \(d\). Let \(a=q^\top d\). For each incorrect class \(j>1\), \((Hd)_j=q_j(-q_j-a)\), while \(d_j=-q_j\), so \((Hd)_j/d_j=q_j+a\). Positivity of the incorrect-class probabilities forces equality precisely when they are all equal; conversely, if they are equal, the incorrect components have a common multiplier and the zero sum of both vectors forces the same multiplier in the correct component. This also proves unconditional equality for \(K=2\).

**2. Exact ternary ratio.** Direct substitution using \(t^2=u\) gives the three scalar moments
\[
\begin{aligned}
\|d\|^2&=\tfrac12(1-p)^2(u+3),\\
 d^\top Hd&=\tfrac14(1-p)^3D,\\
 d^\top H^2d&=\frac{(1-p)^4}{8(u+3)}\{D^2+3u(1-u)^2\}.
\end{aligned}
\]
Hence
\[
\boxed{R(p,u):=\frac{\eta_{\mathrm{so}}}{\eta_{\mathrm{cs}}}
=1+\frac{3u(1-u)^2}{[p(u+3)^2+u(1-u)]^2}.}
\]
This equals one at \(u=0\) and is strictly greater than one whenever \(0<u<1\).

**3. Exact fixed-probability maximizer.** Differentiating the exact rational function,
\[
\partial_u R(p,u)=\frac{3(1-u)}{D^3}
\left\{p(u+3)(u^2-12u+3)-u(1-u)^2\right\}.
\]
For \(u\ge u_0\), the braced expression is strictly negative. On \((0,u_0)\), the critical equation is \(p=\Phi(u)\), where
\[
\Phi(u)=\frac{u(1-u)^2}{(u+3)(u^2-12u+3)},\qquad
\Phi'(u)=\frac{(1-u)(7u^3+75u^2-27u+9)}{(u+3)^2(u^2-12u+3)^2}>0.
\]
The numerator is positive since \(75u^2-27u+9>0\) (negative quadratic discriminant) and \(7u^3\ge0\). Since \(\Phi\) increases from zero to infinity, there is exactly one \(u_p\). The derivative of \(R\) switches from positive to negative there; the endpoints have limiting value one. Consequently
\[
\boxed{\sup_{q:q_1=p}\frac{\eta_{\mathrm{so}}}{\eta_{\mathrm{cs}}}
=1+\frac{3u_p(1-u_p)^2}{[p(u_p+3)^2+u_p(1-u_p)]^2}.}
\]
The maximizers are the two probability vectors whose incorrect-class imbalance is \(t=\pm\sqrt{u_p}\).

**4. Sharp small-\(p\) law and angular pruning.** The strictly increasing inverse \(u_p=\Phi^{-1}(p)\) tends to zero, and \(\Phi(u)/u\to1/9\). Thus \(u_p/p\to9\). Substituting into the exact ratio gives
\[
p\{R(p,u_p)-1\}\longrightarrow\frac{3\cdot9}{(9+9)^2}=\frac1{12}.
\]
It follows that \(R\) has no dimension-uniform finite bound for \(K\ge3\) (the ternary construction already suffices, with arbitrarily small positive masses assigned to additional classes). Since \(R=1/\cos^2\phi\), a criterion \(\cos\phi\ge c\) gives \(R\le c^{-2}\). This is sharp: on strictly positive ternary probability vectors \(R\) varies continuously from one to arbitrarily large values, hence attains \(c^{-2}\) for every \(c\in(0,1)\). The source rule drops a sample when the corresponding cosine is **strictly below** \(1/4\), so equality \(R=16\) is retained in the zero-probe model.

## Verification
Run `python verify.py` with Python 3 and SymPy. The code symbolically reconstructs all relevant softmax moments, the rational ratio, its derivative, the monotonicity derivative, and cross-checks thousands of exact-rational positive probability vectors. It also isolates the optimizer numerically for several true-class probabilities; those finite checks are not used as proofs of the general claims.

As an exact example, take \(p=1/10000\) and \(t=3/100\), so
\[
q=\left(\frac1{10000},\frac{1029897}{2000000},\frac{969903}{2000000}\right).
\]
The ratio is exactly
\[
R=\frac{99940045013498380243}{119964013498380243}=833.083539797\ldots.
\]
This example has cosine approximately \(0.0346\), so it would **not** pass the source's \(1/4\) angular filter in the infinitesimal-probe regime.

## Relationship to prior work
Bauwens--Krivodub--Zhang [1] define the *so-dz* and *cs-dq* probes and report near agreement of averaged rates in their empirical training settings. Their Section 3 further proposes cosine-based per-sample pruning. The present result neither disputes those empirical averages nor reclaims the original estimators; it identifies the exact logit-gradient local ratio, its unique fixed-probability ternary extremizer, its sharp rare-true-class growth and an exact interpretation of that pruning threshold. Korbit--Zanon [2] independently decompose the softmax curvature into true-versus-rest and within-competitor parts; this does not optimize or even compare the two rates here. Sao [3] bounds a different quantity, the complex-analytic Taylor radius of the cross-entropy line profile; no such radius is asserted here.

## Limitations
The theorem is restricted to a single example, identity-logit parametrization, raw positive infinitesimal-probe estimators and a direction equal to the negative cross-entropy gradient in logit space. For general parameter Jacobians, mini-batches, optimizer momentum, non-infinitesimal probes or the final arctangent-modulated schedule, the ratio and cosine identity need not hold. An extreme ratio is not by itself an actual-loss divergence or evidence of downstream training instability; in fact, the displayed extreme example would be removed by the source's angular pruning. Priority relative to unindexed or inaccessible literature remains uncertain. Independent audit has not been performed.

## References
[1] B. Bauwens, V. Krivodub and B. Zhang, *Stepsize modulation for cross entropy from local quadratic optimization*, arXiv:2611.05191v1, first public 2026-11-03, https://arxiv.org/abs/2611.05191 (Sections 2, 3 and Appendix A).

[2] M. Korbit and M. Zanon, *Fast Gauss-Newton for Multiclass Cross-Entropy*, arXiv:2605.06081, first public 2026-05-07, https://arxiv.org/abs/2605.06081 (Sections 2--3, Theorem 3.1 and Proposition 3.2).

[3] P. Sao, *Ghosts of Softmax: Complex Singularities That Limit Safe Step Sizes in Cross-Entropy*, arXiv:2603.13552v1, first public 2026-03-13, https://arxiv.org/html/2603.13552v1 (Section 4 and Appendix E).
