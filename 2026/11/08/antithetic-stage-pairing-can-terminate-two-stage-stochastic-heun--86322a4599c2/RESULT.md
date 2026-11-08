# Antithetic stage pairing can terminate two-stage stochastic Heun in one update

## Finding

Consider the two-component, scalar, interpolating finite-sum quadratic
\[
F(x)=\frac12(f_-(x)+f_+(x)),\qquad
f_\pm(x)=\frac{m(1\pm\delta)}2x^2,
\]
where \(m>0\) and \(0<\delta<1\). The component gradient oracle returns \(g_\pm(x)=m(1\pm\delta)x\). For a fixed \(h>0\), let \(I_k,J_k\in\{-,+\}\) be any pair with each marginal uniform and with \(q=\Pr(I_k\ne J_k)\). Apply the two-stage Heun-form update
\[
X_{k+1}=X_k-\frac h2\left[g_{I_k}(X_k)
+g_{J_k}\bigl(X_k-hg_{I_k}(X_k)\bigr)\right].
\]
Assume the oracle pairs are independent and identically distributed across updates. Write \(t=hm\), and define
\[
R_\times(t,\delta)=1-t+\frac{t^2}{2}(1-\delta^2).
\]
For every deterministic initial \(X_0\) and every integer \(k\ge0\),
\[
\boxed{\mathbb E X_k^2=X_0^2\left[R_\times(t,\delta)^2
+(1-q)t^2\delta^2\bigl(2(t-1)^2+1\bigr)\right]^k.}
\]
Therefore **unique** optimal coupling for expected squared error at every \(k\ge1\), when \(X_0\ne0\), is the antithetic choice \(q=1\), in which each pair uses both component gradients once. This makes each update completely deterministic even though the oracle order is random.

A positive stepsize makes the antithetic update terminate at \(X_1=0\) for every starting point **if and only if** \(\delta\ge1/\sqrt2\). Every such stepsize is one of
\[
\boxed{t_\pm=\frac{1\pm\sqrt{2\delta^2-1}}{1-\delta^2}.}
\]
At equality of the contrast threshold the two roots coincide. For strictly smaller contrast no positive one-update exact termination is possible under *any* coupling preserving the uniform stage marginals.

In particular, the exact positive-curvature example \(m=1\), \(\delta=5/7\), \(h=7/3\) (component curvatures \(2/7\) and \(12/7\)) gives
\[
R_\times=0,\quad M_{q=0}=\frac{1025}{81},\quad
M_{q=1/2}=\frac{1025}{162},\quad M_{q=1}=0.
\]
Thus antithetic stages reach the minimizer in one two-oracle update whereas fresh independent stages and repeated-component stages both grow in mean square. The exact full-gradient Heun multiplier at this same stepsize is \(25/18>1\), so its deterministic iteration is unstable as well.

## Assumptions and scope

The model is one-dimensional, has exactly two equally weighted positive-definite quadratic components sharing minimizer zero, and uses exact gradients. The step \(h>0\) and the joint law of the two oracle indices are held fixed across iterations; each stage separately sees each component with probability \(1/2\). Only the *within-update* dependence varies. Oracle pairs are independent between updates. The statement concerns expected squared error and deterministic one-update termination, not noisy gradient evaluations, general nonlinear objectives, higher-dimensional noncommuting Hessians, or total oracle-cost optimality.

## Proof

Let \(A=g_I(1)\) and \(B=g_J(1)\). Since \(g_I(x)=Ax\), one update has scalar multiplier
\[
R(A,B)=1-\frac h2(A+B)+\frac{h^2}2 AB.
\]
This expression is symmetric in \(A,B\); hence the two orders of a mixed pair have the same multiplier. Put \(u_-=t(1-\delta)\), \(u_+=t(1+\delta)\) and
\[
R_\pm=1-u_\pm+\frac12u_\pm^2,
\qquad R_\times=1-\frac{u_-+u_+}{2}+\frac12u_-u_+.
\]
Every joint distribution with uniform marginals is necessarily of the form
\[
\Pr(--)=\Pr(++)=\frac{1-q}{2},\qquad
\Pr(-+)=\Pr(+-)=\frac q2,
\qquad 0\le q\le1.
\]
Thus one-step conditional second-moment amplification is
\[
M_q=\frac{1-q}{2}(R_-^2+R_+^2)+qR_\times^2.
\]
Direct polynomial expansion, retaining all powers of \(t\), yields the *exact* identity
\[
\frac12(R_-^2+R_+^2)-R_\times^2
=t^2\delta^2(2t^2-4t+3)
=t^2\delta^2\bigl(2(t-1)^2+1\bigr)>0.
\]
It follows that \(M_q=R_\times^2+(1-q)t^2\delta^2[2(t-1)^2+1]\) is strictly decreasing in \(q\). Thus the unique optimal law is \(q=1\); uniqueness is among all joint laws with the two stated uniform marginals. Since independent update pairs have the same law in time and are independent of \(X_k\), conditioning on \(X_k\) and iterating gives \(\mathbb E X_k^2=M_q^kX_0^2\). In particular, geometric mean-square stability for every nonzero deterministic start holds exactly when \(M_q<1\). At equality the second moment remains constant and at greater values it diverges.

For \(q=1\), the actual multiplier is \(R_\times\) in either oracle order. Its zero equation is
\[
(1-\delta^2)t^2-2t+2=0.
\]
The discriminant is \(4(2\delta^2-1)\), giving real roots precisely for \(\delta\ge1/\sqrt2\). When they exist, both roots displayed in the finding are positive because \(0<\delta<1\). Conversely, at any \(q<1\) and \(t>0\), the strictly positive excess term makes \(M_q>0\), so termination for every start is impossible. If \(q=1\) and the contrast condition fails, \(R_\times\ne0\) at every positive step. This establishes the sharp classification, including equality.

For the rational example, \(h m(1-\delta)=2/3\) and \(h m(1+\delta)=4\). The mixed multiplier is \(1-7/3+4/3=0\); the two same-component multipliers are \(5/9\) and \(5\). Their average square is \(1025/81\). Independent pairing gives half that amount, \(1025/162\). The full-gradient multiplier is \(1-7/3+(7/3)^2/2=25/18\). Every stated number follows exactly, without a limiting approximation.

## Verification

A standalone Python 3 standard-library verifier (`verify.py`) checks the multiplier identity and strict ordering over 432 rational parameter pairs, all five rational coupling probabilities, all three sample schemes, and the exact rational separation example. It also enumerates all oracle histories through three updates to verify the moment product identity. The recorded execution reports **4,337 exact assertions passed**. These finite regressions independently test algebra and normalization; the preceding symbolic argument supplies the all-parameter proof.

## Relationship to prior work

Stillfjord and Williamson (2022, arXiv:2201.12782) develop stochastic Runge–Kutta–Chebyshev optimization and explicitly use the *same batch across the stages* of each macrostep; their convergence and linearization analysis does not provide an optimization over two-stage coupling laws or an exact finite-termination contrast threshold. Liu and Xu (2018, arXiv:1810.03124) use antithetic sampling to form a *single averaged minibatch gradient at the same state*; this does not yield the predictor/corrector composition and the algebraic root classification above. Bochacik et al. (2020, arXiv:2006.12131) analyze randomized evaluation times and noisy ODE information rather than coupling a finite-sum gradient oracle across two Heun stages. Shaw and Whalley (2025, arXiv:2504.04274) analyze symmetric minibatch splitting and momentum-based optimization; their inspected stochastic-gradient splitting results are different from the staged Heun coupling law here. These are close methodological sources, not assertions that all related literature is exhausted.

## Limitations

The finding does not imply better efficiency than a full-gradient computation, does not extend automatically to independent noninterpolating gradients, and does not produce a dimension-independent stability law for arbitrary Hessians. Matching the two components and choosing a threshold stepsize requires knowledge of their curvatures. Exact termination may require a step that violates standard full-gradient Heun stability, so no general numerical ODE consistency or robustness conclusion is drawn. The literature comparison is not independent expert validation; unindexed equivalent formulas are a remaining precedence risk.

## References

1. T. Stillfjord and M. Williamson, *SRKCD: a stabilized Runge–Kutta method for stochastic optimization*, initial public version 2022-01-30, https://arxiv.org/abs/2201.12782.
2. J. Liu and L. Xu, *Accelerating Stochastic Gradient Descent Using Antithetic Sampling*, initial public version 2018-10-07, https://arxiv.org/abs/1810.03124.
3. T. Bochacik, M. Goćwin, P. M. Morkisz, and P. Przybyłowicz, *Randomized Runge–Kutta method—stability and convergence under inexact information*, initial public version 2020-06-22, https://arxiv.org/abs/2006.12131.
4. L. Shaw and P. A. Whalley, *Randomised Splitting Methods and Stochastic Gradient Descent*, initial public version 2025-04-05, https://arxiv.org/abs/2504.04274.
