# Strict geodesic concavity of the Luce increasing-subsequence path functional

## Finding

For every strictly positive, nonincreasing \(f\in C^1([0,1])\), the Luce longest-increasing-subsequence path functional
\[
\mathcal A_f(u)=\int_0^1\sqrt{f(t)u'(t)e^{-f(t)u(t)}}\,dt
\]
is *strictly concave along a canonical nonlinear interpolation* of admissible paths. Consequently it has **at most one maximizer** among locally absolutely continuous, nonnegative, nondecreasing paths \(u:[0,1)\to[0,\infty)\) satisfying \(u(0)=0\) and remaining finite on every compact subinterval. No existence, smoothness, or uniqueness among a wider class containing singular paths is asserted.

For distinct admissible \(u_0,u_1\) and \(0<\theta<1\), define
\[
u_\theta(t)=-\frac1{f(t)}\log\left(\theta e^{-f(t)u_0(t)}+(1-\theta)e^{-f(t)u_1(t)}\right).
\]
Then \(u_\theta\) is again admissible and
\[
\mathcal A_f(u_\theta)>\theta\mathcal A_f(u_0)+(1-\theta)\mathcal A_f(u_1).
\]
In fact a pointwise quantitative Jensen bound, derived below, strengthens the inequality.

## Assumptions and scope

Fix \(f\in C^1([0,1])\) with \(f(t)>0\) and \(f'(t)\le0\) for every \(t\in[0,1]\). This includes uniform weights and exponentially decaying positive profiles, but not profiles that vanish at the right endpoint. Let \(\mathscr U\) contain precisely the locally absolutely continuous functions \(u:[0,1)\to[0,\infty)\), finite at each \(t<1\), with \(u(0)=0\) and \(u'\ge0\) almost everywhere. Functions may diverge as \(t\uparrow1\), without a prescribed terminal value.

All derivatives of paths are almost-everywhere derivatives. The functional has its literal integral meaning; no contributions are assigned to singular derivatives or jumps. Since \(f\) is positive on the closed interval, all the integrals below are finite, as proved explicitly.

## Proof

**Step 1: transform the integrand.** Define \(v_u=1-e^{-fu}\), \(k=-f'/f\ge0\), and \(H(s)=-(1-s)\log(1-s)\) for \(0\le s<1\). For every admissible path, \(v_u\) is locally absolutely continuous, \(v_u(0)=0\), and \(0\le v_u<1\). By the chain rule, almost everywhere
\[
q_u:=f u'e^{-fu}=v_u'+kH(v_u)\ge0.
\]
Moreover \(H''(s)=-(1-s)^{-1}\le-1\) and \(0\le H(s)\le e^{-1}\). Integrating on \([0,T]\) and taking \(T\uparrow1\),
\[
\int_0^1 q_u(t)\,dt\le1+\frac1e\int_0^1 k(t)\,dt
=1+\frac1e\log\frac{f(0)}{f(1)}<\infty.
\]
Cauchy–Schwarz gives \(\mathcal A_f(u)\le[1+e^{-1}\log(f(0)/f(1))]^{1/2}\). Thus the supremum and every value appearing below are finite.

**Step 2: preserve the admissible set.** For \(u_0,u_1\in\mathscr U\), set \(v_i=1-e^{-fu_i}\), \(q_i=v_i'+kH(v_i)\), and \(v_\theta=\theta v_0+(1-\theta)v_1\). The nonlinear interpolation in the finding satisfies \(v_{u_\theta}=v_\theta\). Write
\[
\Delta_H=H(v_\theta)-\theta H(v_0)-(1-\theta)H(v_1).
\]
The strict curvature of \(H\) implies the *pointwise* estimate
\[
\Delta_H\ge\frac{\theta(1-\theta)}2(v_0-v_1)^2\ge0.
\]
Consequently,
\[
q_\theta:=v_\theta'+kH(v_\theta)
=\theta q_0+(1-\theta)q_1+k\Delta_H
\ge\theta q_0+(1-\theta)q_1
+\frac{\theta(1-\theta)}2 k(v_0-v_1)^2\ge0.
\]
Since \(f(1-v_\theta)>0\) on each compact subinterval,
\[
u_\theta'=\frac{q_\theta}{f(1-v_\theta)}\ge0
\]
almost everywhere. The interpolation is nonnegative, locally absolutely continuous, finite on compact subintervals and zero at the left endpoint. Hence \(u_\theta\in\mathscr U\).

**Step 3: quantitative and strict concavity.** Combining the preceding bound with concavity of the square root yields
\[
\begin{aligned}
\mathcal A_f(u_\theta)
&\ge\int_0^1\left[\theta q_0+(1-\theta)q_1
+\frac{\theta(1-\theta)}2k(v_0-v_1)^2\right]^{1/2}dt\\
&\ge\theta\mathcal A_f(u_0)+(1-\theta)\mathcal A_f(u_1).
\end{aligned}
\]
To see strictness, suppose the last inequality were equality. Strict concavity of the square root on \([0,\infty)\), together with nonnegativity of the intervening integrands, forces \(q_0=q_1\) almost everywhere. The difference \(d=v_0-v_1\) then solves
\[
d'=-k\big(H(v_0)-H(v_1)\big),\qquad d(0)=0.
\]
For each \(T<1\), \(v_0,v_1\) range over a compact subset of \([0,1)\), so \(H\) is Lipschitz on their common range and \(k\) is bounded. Gronwall's inequality implies \(d=0\) on \([0,T]\). Since \(T<1\) was arbitrary, \(v_0=v_1\) throughout \([0,1)\), hence \(u_0=u_1\). Therefore distinct paths make the inequality strict.

If two distinct paths both attained the supremum over \(\mathscr U\), their interpolation would attain a larger value, contradiction. This proves the asserted **at-most-one** result without assuming that a maximizing path exists.

## Verification

The analytic proof is complete on the stated path class and needs no limiting numerical certificate. The standalone `CHECK.py` evaluates the transformed density, the curvature-based Jensen remainder, positivity of the interpolated derivative, and the integral strict-Jensen inequality for 240 deterministic parameter configurations, including constant and exponentially decreasing positive weight profiles. It is run with Python 3 and NumPy, using `python CHECK.py`. Its output is `PASS: 240 parameter configurations; smallest Jensen gap 0.000148618459`. These finite diagnostics do not replace the all-path proof.

## Relationship to prior work

Borga and Dubach, *The longest increasing subsequences of Luce permutations and permutons*, arXiv:2610.30382v2, Lemma 3.14, equation (26), derive the functional above; Remark 3.15 explicitly identifies existence and uniqueness of a smooth optimal curve as unresolved. The present result answers the **conditional uniqueness** part within the precisely specified locally absolutely continuous class. Their paper provides neither the displayed exponential-mixture identity nor this at-most-one theorem in the inspected variational section. Their stronger existence and regularity question remains open here.

Rolla and Teixeira, *Last Passage Percolation in Macroscopically Inhomogeneous Media*, arXiv:0804.1810, develop a uniqueness criterion for another inhomogeneous LPP path action of the form \(\int\alpha(x,y)(1+\sqrt{1-\dot y^2})\,dx\), under a curvature condition on \(\alpha\). Although conceptually related, their stated criterion is not a direct implication of, nor a direct theorem about, the Luce functional in equation (26). The earlier Luce-permuton paper arXiv:2509.07729 concerns the permuton and its statistics, not this transformed strict-concavity inequality in the inspected material.

## Limitations

This is not a proof that any maximizer exists; it does not prove \(C^1\) regularity or uniqueness in the full right-continuous nondecreasing class allowing singular paths. It assumes \(f\) remains bounded away from zero on \([0,1]\), hence does not directly cover, for example, the Sukhatme profile \(f(t)=1-t\). Historical-priority assessment cannot exclude an abstract general variational theorem that implies the specialized strict-concavity result by a nonobvious change of variables. Numerical diagnostics are nonexhaustive.

## References

1. J. Borga and V. Dubach, *The longest increasing subsequences of Luce permutations and permutons*, arXiv:2610.30382v2 (first public version 2026-10-21), https://arxiv.org/html/2610.30382v2.
2. L. T. Rolla and A. Q. Teixeira, *Last Passage Percolation in Macroscopically Inhomogeneous Media*, arXiv:0804.1810 (2008), https://arxiv.org/abs/0804.1810.
3. J. Borga et al., earlier work on Luce permuton limits, arXiv:2509.07729 (2025), https://arxiv.org/abs/2509.07729.
