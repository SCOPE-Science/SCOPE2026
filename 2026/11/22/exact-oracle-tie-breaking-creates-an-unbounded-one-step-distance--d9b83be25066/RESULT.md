# Exact-oracle tie-breaking creates an unbounded one-step distance transient under gradient-radius initialization

## Finding

For the default gradient-norm initial radius of adaptive short-step Broximal Gradient Descent, the following two-dimensional isotropic quadratic has a **sharp, discontinuous first-step point-error phase diagram**. The smoothness and strong-convexity constants are both one, and the exact local linear oracle is used throughout.

Fix \(a\ge0\), \(p>0\), and \(q\in\mathbb R\). Over the closed halfspace \(X=\{(u,v)\in\mathbb R^2:u\ge0\}\), set
\[
f_a(u,v)=\tfrac12\big((u+a)^2+v^2\big),\qquad x_\star=(0,0),\qquad x_0=(p,q).
\]
The initial radius prescribed when no radius is supplied is
\[
t_0=\|\nabla f_a(x_0)\|=\sqrt{(p+a)^2+q^2}.
\]
Let \(z\) be **any exact** minimizer of the local linear problem over \(X\cap\overline B(x_0,t_0)\). Define \(d=z-x_0\), \(\eta=\min\{1,-\langle\nabla f_a(x_0),d\rangle/\|d\|^2\}\), \(x_1=x_0+\eta d\), and the squared solution-distance ratio \(R=\|x_1\|^2/\|x_0\|^2\).

**Nontied oracle (\(q\ne0\)).** The exact oracle is unique. Writing \(b=\sqrt{a^2+2ap+q^2}\), its output and the exact distance ratio are
\[
z=(0,q-\operatorname{sgn}(q)b),\qquad
R=\frac{p^2\big((b-|q|)^2+a^2\big)}{(p^2+b^2)(p^2+q^2)}<2.
\]
The strict bound is sharp: the supremum of \(R\) over all admissible nontied parameters is \(2\). It can be approached **with the single fixed objective \(f_1\)** by taking \(p\downarrow0\) and \(q=p^3>0\).

**Tied oracle (\(q=0\)).** All and only the exact outputs are \(z=(0,y)\) with \(|y|\le\sqrt{a^2+2ap}\). The squared distance ratio ranges from zero to the following attained maximum:
\[
\max_z R=\begin{cases}
\dfrac{2a}{p+a},&0\le a\le p,\\[3pt]
\dfrac{a}{p},&a\ge p.
\end{cases}
\]
For \(a\ge p\), the worst selection is \(y=\pm\sqrt{ap}\), for which \(\eta=1\). This yields unbounded one-step distance amplification even for the fixed objective \(f_1\) and fixed feasible set \(X\): choosing \(p=n^{-2}\), \(q=0\), \(z=(0,n^{-1})\) for an integer \(n\ge2\) gives
\[
x_1=(0,n^{-1}),\qquad\frac{\|x_1-x_\star\|}{\|x_0-x_\star\|}=n.
\]
The objective error nevertheless **strictly decreases** by the exact factor
\[
\frac{f_1(x_1)-f_1(x_\star)}{f_1(x_0)-f_1(x_\star)}
=\frac{1}{2+n^{-2}}<\frac12.
\]
Finally, at every fixed \(a,p\), the unique-oracle ratios for \(q\to0\), \(q\ne0\), approach \(2a/(p+a)\). For \(a>p\) this is strictly below the tied-oracle maximum \(a/p\), quantifying the exact-oracle selection discontinuity.

## Assumptions and scope

All calculations are in exact real arithmetic, in two dimensions, for the first update only. The objective \(f_a\) has Hessian \(I_2\), so \(L=\mu=1\). Its unique constrained minimizer is \((0,0)\); the objective gap is \(f_a(u,v)-f_a(x_\star)=au+(u^2+v^2)/2\) for feasible \(u\ge0\), verifying global quadratic growth with constant one. The feasible halfspace is closed, convex, and need not be bounded. The default initial radius is used, not the solution-dependent or Polyak radius. All oracle selections described are exact; no approximate-oracle assumptions enter. The next-radius update is irrelevant to this first-step claim.

## Proof

**1. Oracle geometry.** The local feasible disk is \(u\ge0\), \((u-p)^2+(v-q)^2\le t_0^2\); the linear objective is \((p+a)u+qv\). When \(q=0\), minimizing this positive horizontal coefficient forces \(u=0\). The disk cross-section there is exactly \(v=y\), \(|y|\le b_0:=\sqrt{t_0^2-p^2}=\sqrt{a^2+2ap}\). This characterizes *all* exact oracle minimizers, including interior points of the local ball.

When \(q\ne0\), let \(s=\operatorname{sgn}(q)\), \(b=\sqrt{a^2+2ap+q^2}\), and \(z=(0,q-sb)\). This point is feasible and satisfies \(\|z-x_0\|=t_0\). With Lagrange multiplier \(\lambda=|q|/b>0\) for the half-squared ball constraint and \(\nu=p+a-p|q|/b\ge0\) for the constraint \(-u\le0\), the first-order stationarity equation is
\[
(p+a,q)+\lambda(z-x_0)-\nu(1,0)=0.
\]
Convexity makes these conditions sufficient; the nonzero tangential coefficient \(q\) makes the minimizer on the supporting face unique. For \(a=0\) this is also the unique unconstrained disk minimizer \((0,0)\).

**2. Short-step formula for \(q\ne0\).** The displacement is \(d=(-p,-sb)\), with \(\|d\|^2=p^2+b^2=t_0^2\), and the linear decrease is \(G=p(p+a)+|q|b\). By Cauchy--Schwarz, \(0<G\le\|\nabla f_a(x_0)\|\|d\|=t_0^2\); hence clipping is inactive and
\[
\eta=\frac{p(p+a)+|q|b}{p^2+b^2}.
\]
Substitute this expression into \(x_1=(p,q)+\eta(-p,-sb)\) and expand to obtain
\[
\|x_1\|^2=\frac{p^2\big((b-|q|)^2+a^2\big)}{p^2+b^2}.
\]
Using \(b^2=a^2+2ap+q^2\), the numerator's bracket is \(2b^2-2(ap+b|q|)\le2b^2\). Consequently
\[
R\le\frac{2p^2b^2}{(p^2+b^2)(p^2+q^2)}<2.
\]
For \(a=1\), \(p\downarrow0\), \(q=p^3>0\), direct substitution gives \(R\to2\); this proves optimality of the constant even for one fixed objective.

**3. Complete tie optimization.** If \(q=0\) and \(z=(0,y)\), put \(s_0=p^2+y^2\) and \(C=p(p+a)>0\). Then \(\eta=\min\{1,C/s_0\}\) and \(x_1=(p(1-\eta),\eta y)\), so exact expansion gives
\[
R(y)=\begin{cases}
\dfrac{y^2}{p^2},&s_0\le C,\\[3pt]
1+\dfrac{(p+a)(a-p)}{s_0},&s_0\ge C.
\end{cases}
\]
The admissible interval for \(s_0\) is \([p^2,(p+a)^2]\), and \(C\) lies in this interval. The first branch increases to \(a/p\) at \(s_0=C\). The second decreases when \(a>p\) and increases when \(a<p\), giving the maximum \(a/p\) for \(a\ge p\) and \(2a/(p+a)\) for \(a\le p\). The choice \(y=0\) gives \(\eta=1\) and \(x_1=0\), proving the minimum zero. If \(a\ge p\), the maximizers \(y^2=ap\) are feasible, give \(s_0=C\), and are accepted in full.

**4. Unbounded amplification and discontinuity.** Fix \(a=1\) and choose \(p=n^{-2}\), \(n\ge2\), \(q=0\). The valid exact output \(z=(0,n^{-1})\) satisfies \(\|z-x_0\|^2=p(p+1)\le(1+p)^2=t_0^2\) and \(G=\|z-x_0\|^2\), so \(x_1=z\) exactly. The stated point-distance and objective-gap formulas follow by evaluating the quadratic. For fixed \(a,p\), letting nonzero \(q\to0\) in the unique-oracle formula gives \(R\to2a/(p+a)\). Since \(a/p>2a/(p+a)\) exactly when \(a>p\), the claimed strict discontinuity follows.

## Verification

The standalone standard-library verifier `check.py` evaluates the actual oracle and step formulas. It tests exact rational tied-face envelopes, admissibility and KKT signs, exact objective descent on representative rational inputs, representative nontied oracle geometries and the sharp limiting families. It reports 31,024 passing finite assertions. These checks are **not** a substitute for the preceding proof for all real parameters.

Reproduce from the directory containing `check.py` using `python3 check.py`. The only dependency is Python's standard library. In particular, no floating-point enumeration is invoked as a proof of the full oracle classification.

## Relationship to prior work

Kolzenburg and Richtárik, arXiv:2611.11354v1, specify the exact local oracle, the clipped segment step, and the default initial radius \(\|\nabla f(x_0)\|/L\); they establish objective convergence under quadratic growth. The present exact two-dimensional result examines the **one-step point-distance response to multiple exact oracle selections** at that default radius. Their objective-rate theorem neither asserts nor rules out the reported point-error amplification.

Richtárik, Gruntkowska and Li, arXiv:2605.08850v2, establish distance decrease at different, solution-controlled admissible radii and distinguish exact oracle steps from a counterexample using relaxed oracle conditions. An exact point from the present gradient-radius query need not satisfy those radius hypotheses, and the present construction uses no inexact oracle. Richtárik and Mahran, arXiv:2609.33383, identify a projection/Fejér regime when the local radius is at most the Polyak radius; that regime does not cover the default radius in the present fixed-objective witness. These are distinct implication statements, not proof of priority over unindexed work.

## Limitations

The result is a complete **first-update** classification on the indicated halfspace and isotropic quadratic family, not a worst-case claim over all convex functions or future iterations. It does not establish failure of objective convergence, numerical instability in floating point, a bound on total iteration complexity, or that practical local-oracle software chooses a particular maximizer. Large point-distance ratios arise because boundary optimality permits a linear objective-gap term while the local oracle has a tied face. The strict nontied bound does not apply to an exactly tied direction, even when that tie is approached by nontied directions. Independent validation of the mathematical theorem has not been performed.

## References

1. J. N. Kolzenburg and P. Richtárik, *An Adaptive Short-Step Variant of BroxGD with Linear Convergence under Quadratic Growth*, arXiv:2611.11354v1, publicly submitted 2026-11-08, https://arxiv.org/abs/2611.11354.
2. P. Richtárik, K. Gruntkowska, and H. Li, *Broximal Gradient Descent: A Projection-Free Sister of Projected Gradient Descent*, arXiv:2605.08850v2, https://arxiv.org/abs/2605.08850.
3. P. Richtárik and A. Mahran, *Local LMO is Secretly a Projection Method!*, arXiv:2609.33383, https://arxiv.org/abs/2609.33383.
