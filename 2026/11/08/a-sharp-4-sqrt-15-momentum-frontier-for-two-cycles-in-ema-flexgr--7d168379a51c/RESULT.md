# A sharp \(4-\sqrt{15}\) momentum frontier for two-cycles in EMA FlexGrad

## Finding

Consider the equal-buffer specialization of the exponential-moving-average (EMA) mirror-style FlexGrad rule, with no additive denominator stabilizer. On every positive-curvature scalar quadratic, it has a **unique nonzero sign-symmetric period-two orbit**. This orbit is locally asymptotically attracting for precisely
\[
0<\beta<4-\sqrt{15}\approx0.127016653792583,
\]
and is linearly unstable for \(4-\sqrt{15}<\beta<1\), regardless of curvature and learning rate. At equality, two Floquet multipliers equal \(-1\); nonlinear stability at that point is not asserted. The stable cycle has a strictly positive objective error at both orbit points. This classifies the symmetric cycle, not all possible periodic orbits or global trajectories.

## Assumptions and scope

Fix curvature \(\kappa>0\), learning rate \(\eta>0\), and EMA decay \(0<\beta<1\). Let \(f(x)=\kappa x^2/2\) for \(x\in\mathbb R\). For a state \((x_t,s_t,v_t)\) with \(v_{t+1}>0\), define
\[
\begin{aligned}
s_{t+1}&=\beta s_t+(1-\beta)\kappa x_t,\\
v_{t+1}&=\beta v_t+(1-\beta)\kappa^2x_t^2,\\
x_{t+1}&=x_t-\eta\frac{|s_{t+1}|s_{t+1}}{v_{t+1}}.
\end{aligned}
\]
This is the special case \(m_{t+1}=s_{t+1}\) (equal first-moment and signal-buffer decays) of the optional EMA/mirror-descent update in Barros, Defazio and Guigues, Section 5. It is **not** the paper's primary cumulative dual-averaging method. There is no bias correction, decoupled weight decay, or denominator \(\varepsilon\)-floor. Results concern the autonomous full state in the open set where the denominator is positive. Existence of a cycle does not imply that every prescribed zero-memory initialization approaches it.

Write
\[
c_\beta=\frac{1-\beta}{1+\beta},\qquad
 a_\beta=\frac\eta2 c_\beta^2.
\]
The unique nonzero sign-symmetric orbit consists of
\[
P_+=(a_\beta,-\kappa c_\beta a_\beta,\kappa^2a_\beta^2),\qquad
P_-=(-a_\beta,\kappa c_\beta a_\beta,\kappa^2a_\beta^2).
\]
Its objective gap, constant along the two-cycle, is
\[
f(\pm a_\beta)-f(0)=\frac{\kappa\eta^2}{8}c_\beta^4>0.
\]

## Proof

**Cycle existence and uniqueness within the sign-symmetric class.** Suppose the two positions are \(a\) and \(-a\), \(a>0\), with alternating gradient inputs \(\pm\kappa a\). The scalar EMA has the unique periodic response with moment signs opposite the current positive-position state: \(s(P_+)=-\kappa c_\beta a\), \(s(P_-)=+\kappa c_\beta a\). The second-moment EMA is constant at \(\kappa^2a^2\). Thus a positive-position step has normalized displacement \(\eta c_\beta^2\); requiring \(x_{t+1}=-x_t\) forces \(2a=\eta c_\beta^2\). This proves existence and uniqueness among nonzero sign-symmetric two-cycles.

**Derivative and Floquet polynomial.** Rescale the state by \(X=x/a_\beta\), \(U=s/(\kappa a_\beta)\), and \(W=v/(\kappa^2a_\beta^2)\). The rescaled map uses \(S=\beta U+(1-\beta)X\), \(V=\beta W+(1-\beta)X^2\), and
\[
(X,U,W)\mapsto\left(X-\frac{2}{c_\beta^2}\frac{|S|S}{V},S,V\right).
\]
At the positive-position point \((1,-c_\beta,1)\), the Jacobian is
\[
J_+=\begin{pmatrix}
1-8\beta&-4\beta/c_\beta&2\beta\\
1-\beta&\beta&0\\
2(1-\beta)&0&\beta
\end{pmatrix}.
\]
At the other point, \(J_-=TJ_+T\) where \(T=\operatorname{diag}(-1,-1,1)\). Since \(S\ne0\) and \(V>0\) on the cycle, the map is differentiable in its neighborhood. The two-step monodromy \(M=J_-J_+\) has characteristic polynomial
\[
\chi_\beta(z)=z^3+(32\beta-66\beta^2-1)z^2
 +(\beta^4-32\beta^3+66\beta^2)z-\beta^4.
\]
In particular, it is independent of \(\eta\) and \(\kappa\).

**Exact Schur stability boundary.** Put \(d=-\beta^4\), \(a_2=32\beta-66\beta^2-1\), and \(a_1=\beta^4-32\beta^3+66\beta^2\). For the monic cubic \(\chi=z^3+a_2z^2+a_1z+d\), the standard Schur reduction divides \(\chi-d\chi^*\) by \(z\), with \(\chi^*(z)=1+a_2z+a_1z^2+dz^3\). This gives the quadratic \(Az^2+Bz+C\), where
\[
A=1-\beta^8,\quad B=a_2+\beta^4a_1,\quad C=a_1+\beta^4a_2.
\]
The cubic is strictly Schur stable exactly when \(|d|<1\) and this quadratic is strictly Schur stable. As \(A>0\), the quadratic conditions are \(|C|<A\), \(A+B+C>0\), and \(A-B+C>0\).

Let \(q=\beta^2-8\beta+1\). Direct polynomial factorization gives
\[
\begin{aligned}
A-C&=(1-\beta^2)q(\beta^4+8\beta^3-2\beta^2+8\beta+1),\\
A+C&=(1-\beta^2)(\beta^6+67\beta^4-32\beta^3+67\beta^2+1),\\
A+B+C&=32\beta(1-\beta^2)(1+\beta^4),\\
A-B+C&=2(1-\beta^4)q^2.
\end{aligned}
\]
Both parenthesized polynomials in the first two lines are strictly positive for \(0<\beta<1\): the first contains \(8\beta-2\beta^2>0\) and otherwise nonnegative terms; the second contains \(\beta^2(67-32\beta+67\beta^2)>0\) and otherwise nonnegative terms. Thus strict Schur stability holds exactly when \(q>0\), namely \(0<\beta<4-\sqrt{15}\). For \(4-\sqrt{15}<\beta<1\), \(A-C<0\), so the reduced quadratic has a root strictly outside the unit disk, and the original two-step map is linearly unstable. At \(\beta=4-\sqrt{15}\), substitution yields
\[
\chi_\beta(z)=(z+1)^2(z-\beta^4),
\]
so the cycle is nonhyperbolic. In the strictly Schur regime, the smooth two-step map has a locally attracting fixed point, proving local asymptotic attraction of the period-two orbit.

## Verification

The standalone file `verify.py` is executable with Python 3, SymPy and NumPy. It differentiates the branch maps symbolically, checks the two-cycle equations, factors the Floquet polynomial and Schur inequalities, and tests independent finite-difference Jacobians and illustrative finite trajectories at several decay values. Its successful execution reports `VERIFY_OK`. These computations reproduce algebraic identities; the uniform classification for every \(\beta\) comes from the proof and exact positivity factorizations above, not from sampling.

## Relationship to prior work

Barros, Defazio and Guigues introduce the EMA signal/square buffers and optional mirror-style step, including \(|s_{t+1}|\le\sqrt{v_{t+1}}\); their stated convex convergence theorems cover cumulative, **not EMA**, FlexGrad. The present cycle and sharp \(4-\sqrt{15}\) frontier are not assertions from that source. Bock and Weiß analyze two-cycles in Adam with a square-root second-moment normalizer and distinct momentum decays; Fong and Yang analyze Adam's adaptive edge-of-stability response; Itin analyzes kinetic maps with a fixed preconditioner. Their results motivate the question but do not supply this linear-in-\(v\), equal-buffer three-state Floquet polynomial or its exact Schur frontier. Earlier analyses of periodic adaptive optimizers establish that nonconvergence is possible in principle, so mere existence of an optimizer cycle is **not** claimed as an unprecedented phenomenon.

## Limitations

The result applies only to the explicitly specified, zero-denominator-floor, equal-buffer, bias-uncorrected EMA special case and deterministic scalar quadratics. It does not cover differing EMA decay factors, positive denominator floors, stochastic gradients, higher dimensions, the cumulative FlexGrad update, or arbitrary nonlinear objectives. The critical decay \(\beta=4-\sqrt{15}\) is identified as nonhyperbolic but its nonlinear stability is unresolved. Only **local** cycle attraction is proved; no global basin theorem or universal behavior from zero-initialized accumulators is asserted. A historical priority risk remains for potentially unindexed exact-cycle calculations of similarly normalized adaptive algorithms.

## References

1. P. Barros, A. Defazio and V. Guigues, *FlexGrad: A Root-Free Approach to Adaptive Step Sizes*, arXiv:2610.09203v1, 6 October 2026, Sections 4–5, https://arxiv.org/html/2610.09203.
2. S. Bock and M. G. Weiß, *Non-Convergence and Limit Cycles in the Adam optimizer*, arXiv:2210.02070v1, 5 October 2022, Sections 2–3, https://arxiv.org/abs/2210.02070.
3. Y. Fong and H. Yang, *Provable Edge-of-Stability for Adam on a One-Dimensional Quadratic*, arXiv:2608.20638v1, 21 August 2026, Section 3, https://arxiv.org/abs/2608.20638.
4. A. Itin, *Physics-Inspired Optimizers beyond the Edge of Stability: Period-Two Orbits and Delayed Instability*, arXiv:2610.27321v1, 19 October 2026, Section 3 and Appendix A, https://arxiv.org/abs/2610.27321.
