# A sharp fourth-iterate objective-monotonicity frontier for classical FISTA on SPD quadratics

## Finding
Consider the classical constant-step FISTA iteration applied to
\[
f(x)=\frac12 x^{\mathsf T}Ax,
\qquad
0<\mu I\preceq A\preceq LI,
\]
with no nonsmooth term, minimizer at the origin, and step size \(1/L\). Set
\[
t_1=1,
\qquad
t_{k+1}=\frac{1+\sqrt{1+4t_k^2}}2,
\qquad
\beta_k=\frac{t_k-1}{t_{k+1}}.
\]
Define
\[
a=1+\beta_2,
\qquad
c=a(1+\beta_3).
\]
Numerically,
\[
a=1.2817535251253208181\ldots,
\qquad
c=1.8380893920091768047\ldots.
\]

The first three completed FISTA steps satisfy
\[
f(x_1)\le f(x_0),\qquad
f(x_2)\le f(x_1),\qquad
f(x_3)\le f(x_2)
\]
for every SPD quadratic. The fourth completed step is universally objective-nonincreasing exactly through the condition-number threshold
\[
\boxed{
\kappa_*=\frac{c}{1+c-a}
=1.1810364530693856446\ldots
}.
\]
More precisely, every SPD quadratic with
\[
\frac L\mu\le\kappa_*
\]
satisfies
\[
f(x_4)\le f(x_3)
\]
for every starting point. For every
\[
\frac L\mu>\kappa_*,
\]
there is a diagonal SPD quadratic of that exact condition number and a starting point for which
\[
f(x_4)>f(x_3).
\]

A concrete witness already occurs at condition number \(4/3\):
\[
A=\operatorname{diag}\!\left(\frac34,1\right),
\qquad
x_0=(1,0)^{\mathsf T}.
\]
For this problem,
\[
\frac{f(x_4)}{f(x_3)}
=5.9852687051217627\ldots.
\]
Thus a large relative objective spike can occur on a very well-conditioned quadratic, despite the standard global convergence guarantee.

## Assumptions and scope
The recurrence is the constant-step FISTA algorithm with the original Beck--Teboulle momentum sequence. The nonsmooth term is zero, so the proximal-gradient step is an ordinary gradient step. The step size is exactly the reciprocal of the true Lipschitz constant \(L=\lambda_{\max}(A)\).

The theorem concerns objective monotonicity between completed iterates \(x_k\), not the extrapolated points \(y_k\). It classifies the first index at which ordinary FISTA can increase the objective and gives the sharp condition-number frontier for avoiding that increase at the fourth completed iterate.

No claim is made that \(\kappa\le\kappa_*\) guarantees monotonicity at all later iterations. Monotone FISTA variants explicitly modify the algorithm and are outside the theorem.

## Proof
Diagonalize \(A\). Because FISTA is linear on a quadratic and uses a scalar step size, each eigenmode evolves independently. Normalize an eigenvalue by
\[
q=\frac{\lambda}{L}\in(0,1],
\qquad
s=1-q.
\]
Let \(p_k(q)\) be the scalar multiplier mapping the initial modal coordinate to the completed iterate \(x_k\). Directly from the FISTA recurrence,
\[
p_0=1,
\qquad
p_1=s,
\qquad
p_2=s^2.
\]
The first nonzero momentum coefficient is \(\beta_2\), so
\[
p_3=s^2(1-aq),
\qquad
a=1+\beta_2.
\]
The next momentum coefficient gives
\[
p_4=s^3(1-cq),
\qquad
c=a(1+\beta_3).
\]

Since \(0\le s<1\), the first two objective comparisons are immediate. Also
\[
0<\beta_2<1,
\]
because \(1<t_2<2\) and \(t_3>1\); hence
\[
1<a<2.
\]
Therefore
\[
|1-aq|\le1
\qquad (0\le q\le1),
\]
which proves
\[
|p_3(q)|\le|p_2(q)|.
\]
Thus the first three completed steps are universally objective-nonincreasing.

For the fourth comparison,
\[
p_4(q)^2-p_3(q)^2
=(1-q)^4D(q),
\]
where
\[
D(q)=(1-q)^2(1-cq)^2-(1-aq)^2.
\]
A direct factorization gives
\[
D(q)
=q\,[a+cq-c-1]\,[cq^2-(a+c+1)q+2].
\]
Write
\[
q_+=\frac{1+c-a}{c}
=1-\frac{a-1}{c}.
\]
Because \(c>a>1\), one has
\[
0<q_+<1.
\]
For the quadratic factor
\[
F(q)=cq^2-(a+c+1)q+2,
\]
one has
\[
F(0)=2>0,
\qquad
F(1)=1-a<0.
\]
Moreover,
\[
F(q_+)=\frac{2(a-1)(a-c)}{c}<0.
\]
Hence its smaller root satisfies
\[
0<q_-<q_+,
\]
with
\[
q_-=\frac{a+c+1-\sqrt{(a+c+1)^2-8c}}{2c},
\]
and its second root is larger than \(1\). It follows that, on \((0,1)\),
\[
D(q)>0
\quad\Longleftrightarrow\quad
q_-<q<q_+.
\]
Thus a single spectral mode increases the objective from the third to the fourth iterate exactly on that open curvature band.

If \(A\) has condition number \(\kappa=L/\mu\), all normalized eigenvalues obey
\[
q\in\left[\frac1\kappa,1\right].
\]
The interval avoids the violation band for every admissible spectrum exactly when
\[
\frac1\kappa\ge q_+.
\]
Therefore the sharp universal frontier is
\[
\kappa\le\frac1{q_+}
=\frac{c}{1+c-a}.
\]

Conversely, if \(\kappa>\kappa_*\), then
\[
\frac1\kappa<q_+.
\]
Choose any
\[
q\in\left(\max\left\{\frac1\kappa,q_-\right\},q_+\right)
\]
and take
\[
A=\operatorname{diag}\!\left(\frac1\kappa,q,1\right).
\]
Starting in the \(q\)-eigendirection gives
\[
f(x_4)>f(x_3).
\]
The matrix has exact condition number \(\kappa\). If a start with every coordinate nonzero is desired, sufficiently small perturbations in the two endpoint eigendirections preserve the strict inequality.

For the displayed \(\kappa=4/3\) witness, \(q=3/4\). The modal values are
\[
p_3\!\left(\frac34\right)=\frac{4-3a}{64},
\qquad
p_4\!\left(\frac34\right)=\frac{4-3c}{256},
\]
so
\[
\frac{f(x_4)}{f(x_3)}
=
\left(
\frac{4-3c}{4(4-3a)}
\right)^2
=5.9852687051217627\ldots.
\]

## Verification
The embedded `verify.py` independently reconstructs \(t_2,t_3,t_4\), \(\beta_2,\beta_3\), \(a,c\), \(q_-,q_+\), and \(\kappa_*\) at high precision using only the Python standard library.

It checks the displayed numerical enclosures, verifies the signs of the factored fourth-step difference on both sides of the violation band, directly replays the scalar FISTA recurrence, and confirms the \(\kappa=4/3\) objective-spike ratio. It also samples representative condition numbers on both sides of \(\kappa_*\) to verify the interval logic used in the analytic proof.

The universal theorem is the factorization and spectral argument above; numerical replay is not used as a substitute for that proof.

## Relationship to prior work
Beck and Teboulle introduced FISTA and proved its global accelerated objective-rate guarantee. Their constant-step algorithm uses the same \(t_k\) recurrence and extrapolation coefficients used here. The source contrasts ordinary ISTA's descent behavior with FISTA's acceleration, but it does not give a condition-number threshold for stepwise FISTA objective monotonicity.

A later Beck--Teboulle paper introduced a monotone FISTA variant and explicitly observed that ordinary FISTA is not a monotone algorithm: its objective values are not guaranteed to decrease at every iteration. That establishes the practical motivation for enforcing monotonicity, but it does not identify the earliest possible increase on SPD quadratics or a sharp conditioning frontier.

Kim and Fessler later analyzed FISTA through worst-case performance-estimation ideas and optimized global cost-function bounds. Their work concerns worst-case objective guarantees across classes of convex problems rather than the exact local comparison \(f(x_4)\) versus \(f(x_3)\) on a condition-number-bounded SPD quadratic. The accessible full-text metadata and abstract do not state the threshold above.

Targeted searches for FISTA together with fourth-iterate objective increase, condition-number monotonicity, scalar quadratic curvature bands, and the numerical constants \(1.181036453\ldots\) and \(0.8467139159\ldots\) did not locate an implication-equivalent result.

## Limitations
The theorem is about classical constant-step FISTA with the original momentum sequence and exact knowledge of \(L\). Backtracking variants, restart rules, monotone FISTA, strongly-convex parameterizations, proximal nonsmooth terms, and inexact gradients can behave differently.

The threshold controls only the first possible objective increase, namely the comparison between the fourth and third completed iterates. It does not assert later-iterate monotonicity below \(\kappa_*\).

The counterexample construction can concentrate the starting point in one interior eigendirection. Strictly nonzero components in every eigendirection follow by perturbation but are not needed for the sharp universal statement.

Residual originality risk remains that an older performance-estimation, inertial-gradient, or orthogonal-polynomial treatment may encode the same fourth-iterate threshold without the FISTA-specific or condition-number terminology used in the searches.

## References
1. A. Beck and M. Teboulle, “A Fast Iterative Shrinkage-Thresholding Algorithm for Linear Inverse Problems,” SIAM Journal on Imaging Sciences 2 (2009), 183–202, DOI 10.1137/080716542. Published online 2009-03-04; MSC 90C25, 90C06, 65F22.
2. A. Beck and M. Teboulle, “Fast Gradient-Based Algorithms for Constrained Total Variation Image Denoising and Deblurring Problems,” IEEE Transactions on Image Processing 18 (2009), 2419–2434, DOI 10.1109/TIP.2009.2028250.
3. D. Kim and J. A. Fessler, “Another Look at the Fast Iterative Shrinkage/Thresholding Algorithm (FISTA),” SIAM Journal on Optimization 28 (2018), 223–250, DOI 10.1137/16M108940X; arXiv:1608.03861.
