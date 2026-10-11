# AdaGrad-Diff self-tunes into the classical stability interval on separable quadratics
## Finding
Consider the diagonal positive-definite quadratic
\[
f(x)=\frac12\sum_{i=1}^{d}\lambda_i x_i^2,\qquad \lambda_i>0,
\]
with no nonsmooth term, and apply AdaGrad-Diff with arbitrary base parameter \(\eta>0\), regularizer \(\varepsilon>0\), and the convention \(g^0=0\). For coordinate \(i\), write
\[
w_i^n=\varepsilon+\left(\sum_{k=1}^{n}|g_i^k-g_i^{k-1}|^2\right)^{1/2}.
\]
If \(x_i^1\neq0\), then \(w_i^n\) has a finite limit \(w_i^\infty\) satisfying the strict bound
\[
w_i^\infty>\frac{\eta\lambda_i}{2}.
\]
Equivalently, the limiting effective coordinate stepsize \(\alpha_i^\infty:=\eta/w_i^\infty\) lies strictly in the classical gradient-descent stability interval
\[
0<\alpha_i^\infty<\frac{2}{\lambda_i}.
\]
Moreover, if that coordinate is never hit exactly, then
\[
\lim_{n\to\infty}\frac{|x_i^{n+1}|}{|x_i^n|}
=\left|1-\frac{\eta\lambda_i}{w_i^\infty}\right|<1.
\]
Consequently, in finite dimension the full iterate sequence is eventually Q-linearly convergent to the unique minimizer \(0\) (or reaches it in finitely many coordinates even sooner).

## Assumptions and scope
The statement concerns the exact deterministic AdaGrad-Diff update of Bojović, Salzo, and Pontil on a finite-dimensional separable strongly convex quadratic, with \(\varphi\equiv0\), \(\eta>0\), and \(\varepsilon>0\). The diagonal form is essential for the coordinatewise recurrence used below. A coordinate with \(x_i^1=0\) stays identically zero and is excluded from the strict lower-bound statement because no stability repair is needed there.

The source theorem applies because this objective is convex and has globally Lipschitz gradient. Its unique minimizer is \(0\), so weak convergence of the source theorem is ordinary convergence in finite dimension.

## Proof
For the diagonal quadratic, \(g_i^n=\lambda_i x_i^n\), and the AdaGrad-Diff step reduces exactly to
\[
x_i^{n+1}=\left(1-\frac{\eta\lambda_i}{w_i^n}\right)x_i^n.
\]
The weights are nondecreasing. Proposition 3.4 of the source paper proves
\[
\sum_{n=1}^{\infty}\|g^{n+1}-g^n\|^2<\infty,
\]
so each coordinate sum defining \(w_i^n\) converges and therefore \(w_i^n\to w_i^\infty<\infty\).

Theorem 2.5 of the source paper gives convergence of the iterates to a minimizer in the smooth convex setting. Here the minimizer is unique, hence \(x_i^n\to0\) for every \(i\).

Fix an active coordinate with \(x_i^1\neq0\). Suppose for contradiction that
\[
w_i^\infty\leq\frac{\eta\lambda_i}{2}.
\]
Because \(w_i^n\) is nondecreasing and bounded above by its limit, for every \(n\),
\[
w_i^n\leq\frac{\eta\lambda_i}{2}.
\]
Thus
\[
1-\frac{\eta\lambda_i}{w_i^n}\leq-1,
\]
and hence \(|x_i^{n+1}|\geq|x_i^n|\) for every \(n\). Starting from \(x_i^1\neq0\), this is incompatible with \(x_i^n\to0\). Therefore
\[
w_i^\infty>\frac{\eta\lambda_i}{2}.
\]

If the coordinate never becomes exactly zero, dividing the recurrence by \(x_i^n\) and passing to the limit yields
\[
\lim_{n\to\infty}\frac{|x_i^{n+1}|}{|x_i^n|}
=\left|1-\frac{\eta\lambda_i}{w_i^\infty}\right|<1.
\]
If it becomes zero at a finite iteration, it remains zero thereafter. Since there are finitely many coordinates, the maximum of the limiting contraction factors over the nonzero coordinates is strictly below one. Choosing any \(\rho\) strictly between that maximum and one gives an index \(N\) such that
\[
\|x^{n+1}\|_2\leq\rho\|x^n\|_2\qquad(n\geq N),
\]
which is eventual Q-linear convergence.

## Verification
The proof uses only two nontrivial ingredients from the source analysis: convergence of the iterates in the smooth convex case and square-summability of successive gradient differences. The full preprint states the former in Theorem 2.5 and the latter in Proposition 3.4; the appendix proof of Proposition 3.4 was checked through its case split that bounds the cumulative gradient-difference energy. The remaining argument is the exact scalar coordinate recurrence above.

Boundary cases were checked explicitly. Equality \(w_i^\infty=\eta\lambda_i/2\) is impossible for an active coordinate because it would make every finite-step multiplier have magnitude at least one. A coordinate initialized at zero remains zero. A finite exact hit of zero is compatible with, and stronger than, eventual linear convergence.

## Relationship to prior work
The AdaGrad-Diff preprint introduces accumulation of successive gradient differences, proves an \(\mathcal O(1/n)\) ergodic objective bound for smooth convex objectives, and proves convergence of the iterates. It also reports robustness to very small and very large values of \(\eta\). The finding above converts that qualitative robustness into a sharp-form structural statement for the canonical separable quadratic test class: regardless of the base \(\eta\), every active coordinate's limiting effective stepsize is forced strictly below its exact scalar instability threshold, and this yields a last-iterate linear rate on this class.

Malitsky and Mishchenko also use observed gradient differences to adapt local stepsizes, but their adaptive proximal-gradient rule is a different, noncumulative mechanism based on local curvature ratios. The later AdaGrad composite-objective counterexample paper discusses successive gradient differences as an alternative accumulation mechanism, but the available statement concerns avoiding excessive decay rather than the coordinatewise stability threshold and asymptotic linear rate proved here.

## Limitations
The result is for diagonal positive-definite quadratics. It does not claim the same coordinatewise threshold for nondiagonal Hessians, composite nonsmooth terms, stochastic gradients, or nonconvex objectives. It also does not give a closed form for \(w_i^\infty\), and it does not claim that the lower bound \(\eta\lambda_i/2\) is attained or globally sharp over initializations. The linear rate is asymptotic; transient behavior can be oscillatory when the limiting multiplier is negative.

## References
1. M. Bojović, S. Salzo, and M. Pontil, “AdaGrad-Diff: A New Version of the Adaptive Gradient Algorithm,” arXiv:2602.13112v1, first posted 2026-02-13. https://arxiv.org/abs/2602.13112
2. Y. Malitsky and K. Mishchenko, “Adaptive Proximal Gradient Method for Convex Optimization,” arXiv:2308.02261. https://arxiv.org/abs/2308.02261
3. M. Bojović, S. Salzo, and M. Pontil, “AdaGrad does not adapt to Hölder-smoothness for composite objectives,” arXiv:2606.29893. https://arxiv.org/abs/2606.29893
