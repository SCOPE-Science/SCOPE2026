# A unique Brownian first-passage crossover for every static diffusivity mixture

## Finding

Fix a target at zero, start a particle at \(a>0\), and independently draw one positive diffusivity \(D\) before its Brownian trajectory. Let its dynamics have generator \(D\partial_{xx}\), with absorption on reaching the target. Assume only that \(D\) is nonconstant and that \(0<\bar D=\mathbb E[D]<\infty\). Define the cumulative targeting probabilities

\[
H_a(t)=\mathbb E\!\left[\operatorname{erfc}\left(\frac a{\sqrt{4Dt}}\right)\right],\qquad
G_a(t)=\operatorname{erfc}\left(\frac a{\sqrt{4\bar D t}}\right).
\]

**Theorem.** There is exactly one \(t_*(a)\in(0,\infty)\) for which \(H_a(t_*)=G_a(t_*)\). The difference \(\Delta_a=H_a-G_a\) is strictly positive before \(t_*\), strictly negative afterward, and has precisely two positive-time critical points: one positive local and global maximum before \(t_*\) and one negative local and global minimum after \(t_*\). Both are strict and nondegenerate. There is a dimensionless constant \(s_*\) depending only on the distribution of \(D/\bar D\) such that

\[
t_*(a)=\frac{a^2}{4\bar D}s_*.
\]

If \(0<d_-\le D\le d_+<\infty\) almost surely, then

\[
\boxed{\frac{a^2}{6d_+}<t_*(a)<\frac{a^2}{6d_-}.}
\]

No negative moment of \(D\) is assumed finite; in particular the theorem applies when \(\mathbb E[D^{-1/2}]=\infty\).

## Assumptions and scope

The random diffusivity is **quenched along each trajectory**: conditional on its initial draw, the process is \(X_t=a+\sqrt{2D}\,W_t\), stopped at its first contact with zero. The draw of \(D\) is independent of the Brownian noise. The comparison process uses a single deterministic diffusivity \(\bar D\). The distribution of \(D\) may be discrete, continuous, unbounded above, or concentrated arbitrarily close to zero; only positivity almost surely and finite positive mean are required. The Brownian reflection principle gives the displayed \(\operatorname{erfc}\) formulas.

## Proof

**1. Opposite signs at the two time ends.** A nonconstant positive integrable random variable has positive probability above its mean. Thus some \(d_0>\bar D\) and \(p>0\) satisfy \(\mathbb P(D\ge d_0)=p\). Since \(H_a(t)\ge p\operatorname{erfc}(a/\sqrt{4d_0t})\) and the standard Gaussian-tail comparison gives

\[
\frac{\operatorname{erfc}(a/\sqrt{4d_0t})}{\operatorname{erfc}(a/\sqrt{4\bar D t})}\longrightarrow\infty \quad(t\downarrow0),
\]

we obtain \(\Delta_a(t)>0\) for all sufficiently small positive \(t\). Next, put \(q=a/\sqrt\pi\). The inequality \(0\le\operatorname{erf}(z)\le 2z/\sqrt\pi\), dominated convergence when the negative half-moment is finite, and Fatou's lemma otherwise show the extended-real limit

\[
\lim_{t\to\infty}\sqrt t\,[G_a(t)-H_a(t)]
=q\bigl(\mathbb E[D^{-1/2}]-\bar D^{-1/2}\bigr)\in(0,\infty].
\]

Strict convexity of \(x\mapsto x^{-1/2}\) gives the strict positivity of this limit, including the infinite case. Therefore \(\Delta_a(t)<0\) for all sufficiently large \(t\). Both cumulative distribution functions approach zero as \(t\downarrow0\) and one as \(t\to\infty\), so \(\Delta_a\) approaches zero at both ends.

**2. A strict-convexity reduction of the density difference.** For \(t>0\), differentiation under the diffusivity expectation is justified because \(D^{-1/2}e^{-a^2/(4Dt)}\) is bounded uniformly over \(D>0\), locally uniformly in \(t\). Put \(y=a^2/(4t)\) and \(c=\bar D^{-1/2}\), and define

\[
K(y)=\mathbb E\!\left[D^{-1/2}\exp\left(-y(D^{-1}-\bar D^{-1})\right)\right],\qquad y>0.
\]

Direct differentiation of the Brownian first-passage CDF yields

\[
\Delta_a'(t)=\frac{a\,e^{-y/\bar D}}{2\sqrt\pi\,t^{3/2}}[K(y)-c].
\]

For every \(y>0\), all differentiated integrands are bounded near \(D=0\) by exponential damping and at \(D=\infty\) by powers of \(D^{-1}\). Therefore

\[
K''(y)=\mathbb E\!\left[D^{-1/2}(D^{-1}-\bar D^{-1})^2e^{-y(D^{-1}-\bar D^{-1})}\right]>0.
\]

The inequality is strict because \(D\) is nonconstant. Monotone convergence after factoring out \(e^{y/\bar D}\) and strict Jensen give

\[
K(0+)=\mathbb E[D^{-1/2}]>c,
\]

where the expectation may be infinite. Also, because \(\mathbb P(D>\bar D)>0\), the positive contribution from a bounded diffusivity interval lying strictly above \(\bar D\) implies \(K(y)\to\infty\) as \(y\to\infty\).

The opposite signs of \(\Delta_a\) established in Step 1 imply by the mean-value theorem that \(\Delta_a'(t)<0\) somewhere. Hence \(K(y)<c\) at some positive \(y\). A strictly convex function exceeding \(c\) at both ends and strictly below it at an interior point has exactly two simple crossings of the horizontal line \(c\). Consequently \(\Delta_a'(t)\) has exactly two zeros, with signs \(+,-,+\) in increasing-time order. Since \(\Delta_a\) starts at zero, becomes positive, eventually becomes negative, and returns to zero, its first stationary point is a strict positive maximum and its second a strict negative minimum. The strictly decreasing segment between them contains exactly one zero; neither of the two increasing segments contains any other positive-time zero. This proves the universal single-crossing theorem and the two-extremum claim. The nondegeneracy of extrema follows because the two horizontal crossings of the strictly convex differentiable \(K\) occur on opposite sides of its unique minimizer, with nonzero derivative.

**3. Scaling and a bracket for bounded diffusivities.** Write \(Q=D/\bar D\) and \(s=4\bar D t/a^2\). Then

\[
\Delta_a(t)=\mathbb E\!\left[\operatorname{erfc}\left(\frac1{\sqrt{sQ}}\right)\right]
-\operatorname{erfc}\left(\frac1{\sqrt s}\right).
\]

The unique zero therefore has the stated scaling. For fixed \(t\), elementary differentiation in the diffusivity variable gives

\[
\frac{\partial^2}{\partial D^2}\operatorname{erfc}\left(\frac a{\sqrt{4Dt}}\right)
=\frac{a\,e^{-a^2/(4Dt)}}{2\sqrt{\pi t}\,D^{5/2}}\left(\frac{a^2}{4Dt}-\frac32\right).
\]

The cumulative first-passage function is strictly convex in \(D\in[d_-,d_+]\) at \(t=a^2/(6d_+)\) and strictly concave there at \(t=a^2/(6d_-)\), except possibly for a zero-curvature endpoint. Strict Jensen then gives opposite signs of \(\Delta_a\) at these two times. The unique crossing must lie strictly between them.

## Verification

The accompanying \(\texttt{checker.py}\) symbolically differentiates the Brownian targeting kernel in \(D\) and in \(t\), then performs independent high-precision tests for binary, three-point and four-point diffusivity mixtures. For equally likely \(D\in\{1,4\}\) and \(a=1\), it yields \(\bar D=5/2\) and

\[
t_*\approx0.07643348250903497200108,\qquad H_1(t_*)=G_1(t_*)\approx0.10574719393975522.
\]

The positive maximum and negative minimum occur at approximately \(0.04134906320124803\) and \(0.46169020078200986\), respectively. The checker also tests an explicitly integrable law with divergent negative half-moment: for \(D=U^2\), \(U\sim\operatorname{Unif}(0,1)\), \(a=1\), the heterogeneous CDF is

\[
H_1(t)=\operatorname{erfc}(b)-\frac b{\sqrt\pi}\,E_1(b^2),\quad b=\frac1{2\sqrt t},
\]

where \(E_1\) is the exponential integral, and \(t_*\approx0.61606293116130586\). These checks verify identities and examples; the universally quantified conclusion follows from the proof, not numerical sampling. Run with \(\texttt{python checker.py}\) (requires \(\texttt{sympy}\), \(\texttt{mpmath}\)).

## Relationship to prior work

Sposini et al. (2024), equations (31) and (34)–(39), provide the Brownian hitting CDF, the arbitrary-distribution superstatistical mixture, and an implicit equation for a crossover. They describe a crossing as *typical* and demonstrate its application numerically. Those formulas and the short-time advantage of heterogeneous searchers are not claimed as new here. The new part is a global uniqueness theorem for every nonconstant positive finite-mean diffusivity distribution, an exact count of two extrema, and explicit distribution-free time brackets under bounded support, including an extension through infinite negative half-moments.

Sposini, Chechkin and Metzler (2018) describe a crossover of a specific time-fluctuating Ornstein–Uhlenbeck diffusivity model; its initial-position universality does not establish uniqueness for every quenched random diffusivity. The 2024 companion discusses extreme many-particle targeting. Grebenkov et al. (2020) address three time-varying diffusivity constructions. General first-passage transform methods may supply equivalent formulations but the inspected primary results do not state or imply the universal crossing count without a separate shape argument.

## Limitations

This is a theorem for **constant diffusivity within each realization**. It does not apply unchanged to diffusivities that fluctuate during a path, spatially dependent diffusivities, finite absorbing intervals, or multidimensional nonplanar targets. The result states one finite intersection, not an explicit closed form for the crossover for arbitrary \(D\). The bounded-support bracket requires genuine strictly positive lower and finite upper support bounds. Publication priority may be affected by an equivalent result in unindexed literature or a general shape/variation-diminishing theorem not identified in the inspected works. No independent scientific audit has been performed.

## References

1. V. Sposini, S. Nampoothiri, A. Chechkin, E. Orlandini, F. Seno and F. Baldovin, *Being heterogeneous is disadvantageous: Brownian non-Gaussian searches*, arXiv:2403.10138v1 (first public March 15, 2024), especially equations (31), (34)–(39). https://arxiv.org/abs/2403.10138
2. V. Sposini, A. V. Chechkin and R. Metzler, *First passage statistics for diffusing diffusivity*, arXiv:1809.09186v1 (2018), especially Sections 3–4. https://arxiv.org/abs/1809.09186
3. V. Sposini et al., *Being heterogeneous is advantageous: Extreme Brownian non-Gaussian searches*, arXiv:2403.10143v1 (2024). https://arxiv.org/abs/2403.10143
4. D. S. Grebenkov, V. Sposini, R. Metzler, G. Oshanin and F. Seno, *Exact first-passage time distributions for three random diffusivity models*, arXiv:2007.05765v1 (2020). https://arxiv.org/abs/2007.05765
5. Y. Lanoiselée and V. Sposini, *First-Passage Times for Random Diffusivity Models*, 2024 book chapter, DOI:10.1007/978-3-031-67802-8_13. Full chapter not available for inspection; overlap risk remains.
