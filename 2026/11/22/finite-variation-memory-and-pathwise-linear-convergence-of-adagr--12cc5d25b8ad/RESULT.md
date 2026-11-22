# Finite variation memory and pathwise linear convergence of AdaGrad-Diff under Bernoulli interpolation

## Finding

**Theorem.** Fix an integer \(d\geq1\), positive numbers \(\eta,\varepsilon\), and \(L_i>0\), \(p_i\in(0,1)\) for each \(i\in\{1,\ldots,d\}\). Let the random vectors \(A_n=(A_{n,1},\ldots,A_{n,d})\) be independent and identically distributed **across time**, with coordinate marginals \(\Pr(A_{n,i}=L_i)=p_i\), \(\Pr(A_{n,i}=0)=1-p_i\). Coordinates **within one vector** may be arbitrarily dependent; the full vector is independent of the past at every step. Starting from any deterministic \(x_0\in\mathbb R^d\), run the unregularized coordinatewise AdaGrad-Diff algorithm, with observed gradient \(g_{n,i}=A_{n,i}x_{n,i}\), initial gradient \(g_{-1,i}=0\), and

\[
S_{n,i}=\sum_{k=0}^n(g_{k,i}-g_{k-1,i})^2,\qquad
w_{n,i}=\varepsilon+\sqrt{S_{n,i}},\qquad
x_{n+1,i}=x_{n,i}-\frac{\eta}{w_{n,i}}g_{n,i}.
\]

Then, simultaneously for every coordinate, almost surely,

\[
\boxed{\sum_{n=0}^{\infty}(g_{n,i}-g_{n-1,i})^2<\infty,\quad
w_{n,i}\uparrow w_{\infty,i}<\infty,\quad
\sum_{n=0}^{\infty}g_{n,i}^2<\infty.}
\]

Moreover, every \(x_{n,i}\) either reaches zero in finitely many iterations and stays there, or converges to zero exponentially fast. In the latter case its limiting adaptive weight satisfies the **strict terminal stability inequality**

\[
\boxed{w_{\infty,i}>\frac{\eta L_i}{2}}
\]

and its exact pathwise logarithmic rate is

\[
\boxed{\lim_{n\to\infty}\frac{1}{n}\log|x_{n,i}|
=p_i\log\left|1-\frac{\eta L_i}{w_{\infty,i}}\right|\in[-\infty,0).}
\]

Here \(\log0=-\infty\). The right side is random through the final accumulated weight. The rate is not asserted to be a deterministic constant, nor is it a mean-square rate.

## Assumptions and scope

The stochastic oracle is unbiased for the globally smooth, strongly convex quadratic

\[
f(x)=\frac12\sum_{i=1}^{d}p_iL_i x_i^2,
\qquad \mathbb E[g_n\mid x_n]=\nabla f(x_n).
\]

Its stochastic-gradient variance is exactly

\[
\mathbb E[\|g_n-\nabla f(x_n)\|^2\mid x_n]
=\sum_i p_i(1-p_i)L_i^2x_{n,i}^2
\leq 2\max_i((1-p_i)L_i)\,[f(x_n)-f(0)].
\]

Thus the example has interpolation at the unique minimizer, nonzero multiplicative noise away from it, and an **unbounded optimization domain**. Each observation uses the current iterate, and its difference is computed against the *previous independently sampled gradient*, not a gradient recomputed at the current iterate. The accumulator includes the current difference before the corresponding update. Both \(\eta\) and \(\varepsilon\) are arbitrary positive constants. The result does not apply to coupled Hessians, additive noise at the minimizer, or generic stochastic interpolation oracles.

## Proof

**1. A deterministic finite-variation lemma.** Let \((a_n)_{n\geq0}\) be *any* sequence in \([0,L]\), with \(L>0\), and consider the scalar recursion

\[
g_n=a_nx_n,\quad g_{-1}=0,\quad
S_n=\sum_{j=0}^{n}(g_j-g_{j-1})^2,\quad
w_n=\varepsilon+\sqrt{S_n},\quad
x_{n+1}=(1-\eta a_n/w_n)x_n.
\]

We claim \(S_\infty<\infty\), for all finite initial \(x_0\) and all \(\eta,\varepsilon>0\). Suppose instead that \(S_n\to\infty\). Then \(w_n\to\infty\), so choose an index \(N\) for which \(w_n\geq\eta L\) for every \(n\geq N\). With \(t_n=\eta a_n/w_n\in[0,1]\), the scalar energy identity and \(a_n^2\leq La_n\) give

\[
x_n^2-x_{n+1}^2=(2t_n-t_n^2)x_n^2
\geq t_nx_n^2
=\frac{\eta a_nx_n^2}{w_n}
\geq\frac{\eta g_n^2}{Lw_n}.
\]

Summing from \(N\) shows

\[
\sum_{n=N}^\infty\frac{g_n^2}{w_n}\leq\frac{Lx_N^2}{\eta}<\infty.
\tag{1}
\]

Set \(u_n=g_n^2\) and \(B_n=\sum_{j=N}^nu_j\), with \(B_{N-1}=0\). Since \((g_j-g_{j-1})^2\leq2g_j^2+2g_{j-1}^2\),

\[
S_n\leq S_{N-1}+2g_{N-1}^2+4B_n,
\qquad
w_n\leq C+2\sqrt{B_n},
\qquad C=\varepsilon+\sqrt{S_{N-1}+2g_{N-1}^2}.
\]

If \(B_n\to\infty\), then whenever \(\sqrt{B_n}\geq C\),

\[
\frac{u_n}{C+2\sqrt{B_n}}
=(\sqrt{B_n}-\sqrt{B_{n-1}})
\frac{\sqrt{B_n}+\sqrt{B_{n-1}}}{C+2\sqrt{B_n}}
\geq\frac13(\sqrt{B_n}-\sqrt{B_{n-1}}).
\]

The series of the right-hand increments diverges, so \(\sum_nu_n/(C+2\sqrt{B_n})=\infty\). But \(w_n\leq C+2\sqrt{B_n}\), contradicting (1). Thus \(B_\infty<\infty\), which by the displayed estimate for \(S_n\) contradicts \(S_n\to\infty\). This proves finite variation for arbitrary bounded nonnegative curvature sequences. No probabilistic or bounded-iterate hypothesis was used.

**2. Strict terminal stability.** Apply the lemma independently to the observed sequence of each coordinate (the lemma is pathwise). Fix a nonzero initial coordinate whose trajectory never becomes zero. Almost surely there are infinitely many transitions \(A_{n-1,i}=0\), \(A_{n,i}=L_i\): disjoint two-time blocks have positive independent probability \((1-p_i)p_i\). Suppose \(w_{\infty,i}\leq\eta L_i/2\). All active steps then have \(\eta L_i/w_{n,i}\geq2\), so they cannot decrease the absolute iterate; inactive steps leave it unchanged. Hence \(|x_{n,i}|\geq|x_{0,i}|>0\) at every time. Every zero-to-active transition contributes

\[
(g_{n,i}-g_{n-1,i})^2=L_i^2x_{n,i}^2\geq L_i^2x_{0,i}^2
\]

to the finite-variation accumulator, an impossibility. Therefore \(w_{\infty,i}>\eta L_i/2\).

**3. Exponential convergence and the exact rate.** Choose \(N_i\) with \(w_{N_i,i}>\eta L_i/2\). Monotonicity and convergence of the weights give, for every subsequent active step,

\[
\frac{\eta L_i}{w_{n,i}}\in
\left[\frac{\eta L_i}{w_{\infty,i}},\frac{\eta L_i}{w_{N_i,i}}\right]\subset(0,2).
\]

Thus there is a (possibly random) \(r_i<1\) bounding the absolute active-step multiplier for all \(n\geq N_i\). By the strong law of large numbers, the number of active steps before time \(n\) divided by \(n\) tends to \(p_i>0\). Consequently \(|x_{n,i}|\) decays exponentially. Enumerating the active steps also proves \(\sum_n g_{n,i}^2<\infty\): each new active observation occurs after at least one more contraction by \(r_i\), so its squared gradient is dominated by a geometric series. If a coordinate reaches zero, both assertions are immediate after that time.

For a nonzero trajectory, taking logarithms of the exact product of its active multipliers gives

\[
\log|x_{n,i}|=\log|x_{N_i,i}|+
\sum_{k=N_i}^{n-1}{\mathbf{1}}_{\{A_{k,i}=L_i\}}
\log\left|1-\frac{\eta L_i}{w_{k,i}}\right|.
\]

If the limiting multiplier is nonzero, continuity of the logarithm, convergence of \(w_{k,i}\), and the strong law yield the stated limit. If the limiting multiplier is zero, the logarithmic factors tend to \(-\infty\); the same strong law applied with an arbitrary negative cutoff forces the normalized sum to \(-\infty\). Intersecting the probability-one events over finitely many coordinates completes the proof.

## Verification

The included standard-library script `verify.py` checks the elementary algebraic inequalities with exact rational arithmetic and executes deterministic and independently seeded Bernoulli sample-path tests. It checks source-consistent update order, nondecreasing accumulation, late-step contraction, and terminal behavior. These finite computations provide implementation diagnostics only; the infinite-time claims are established by the preceding argument. To reproduce, run `python3 verify.py` in the directory containing this document.

## Relationship to prior work

Bojović, Salzo and Pontil's AdaGrad-Diff algorithm uses precisely the coordinatewise accumulation of successive sampled gradients analyzed here [1, Algorithm 3.6]. Its deterministic Lipschitz theory proves summability of squared differences; the stochastic interpolation analysis supplies convergence-rate bounds but explicitly leaves stochastic finite-variation/iterate convergence beyond that setting as future work [1, Sections 3, 4, 6]. The present statement resolves this issue **only for diagonal Bernoulli-interpolated quadratic oracles**, and adds an exact pathwise logarithmic rate. The prior deterministic theorem cannot be applied because consecutive gradients are sampled independently even at the same iterate.

Rodomanov, Jiang and Stich study the related variation-adaptive UniSgd mechanism [2]. Their finite-domain diameter assumption and expected optimization guarantees do not yield the stated unconstrained pathwise finite-variation theorem or its terminal-weight exponent. Classical AdaGrad-Norm accumulates gradient magnitudes rather than sampled gradient differences, so its scalar terminal-step results do not imply the conclusion [3].

## Limitations

The almost-sure rate is random and may be very slow; no uniform rate or expected-error bound is asserted. The proof relies on nonnegative, uniformly bounded, coordinate-decoupled curvature and on infinitely recurring positive and zero oracle states. It neither proves finite variation for general interpolating stochastic gradients nor treats coupled quadratics, adaptive momentum, proximal penalties, or bias. No finite experiment certifies an infinite-horizon assertion. Historical novelty remains subject to independent scholarly checking; mathematical correctness and novelty have not received independent audit.

## References

[1] M. Bojović, S. Salzo and M. Pontil, *AdaGrad-Diff: a Corrected Version of the Adaptive Gradient Algorithm for Composite Optimization*, arXiv:2602.13112, first publicly submitted 2026-02-13; revised 2026-10-29. https://arxiv.org/html/2602.13112

[2] A. Rodomanov, X. Jiang and S. Stich, *Universality of AdaGrad Stepsizes for Stochastic Optimization: Inexact Oracle, Acceleration and Variance Reduction*, arXiv:2406.06398, 2024. https://arxiv.org/abs/2406.06398

[3] R. Ward, X. Wu and L. Bottou, *AdaGrad Stepsizes: Sharp Convergence Over Nonconvex Landscapes*, arXiv:1806.01811, 2018. https://arxiv.org/abs/1806.01811
