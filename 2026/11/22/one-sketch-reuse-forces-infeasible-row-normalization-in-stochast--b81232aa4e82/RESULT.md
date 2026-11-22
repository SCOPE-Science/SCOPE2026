# One-sketch reuse forces infeasible row-normalization in stochastic Stiefel landing

## Finding
Consider the stochastic normal direction used in landing methods for the Stiefel constraint, but **reuse the same rank-one coordinate sketch in both occurrences** instead of taking the two independent sketches prescribed in the cited methods. The resulting fixed-step iteration has a deterministic, explicitly computable almost-sure limit for every initially orthonormal frame. In every column dimension at least two, that limit is necessarily infeasible, even when the step is arbitrarily small.

**Theorem.** Let integers \(n\ge p\ge2\) be given and let \(X_0\in\mathbb R^{n\times p}\) satisfy \(X_0^{\mathsf T}X_0=I_p\). At each iteration independently select \(i_t\) uniformly from \(\{1,\ldots,n\}\), set \(B_{i_t}=n e_{i_t}e_{i_t}^{\mathsf T}\), and update
\[
X_{t+1}=X_t-\eta B_{i_t}X_t\bigl(X_t^{\mathsf T}B_{i_t}X_t-I_p\bigr),
\qquad 0<\eta\le\frac1{2n^2}.
\]
Let \(r_i\) be row \(i\) of \(X_0\), and let \(S=\{i:\|r_i\|_2>0\}\) with \(s=|S|\). With probability one, \(X_t\) converges to the **nonrandom** matrix \(X_\infty\) whose rows are
\[
(X_\infty)_{i,:}=\begin{cases}
\displaystyle\frac{r_i}{\sqrt n\,\|r_i\|_2},&i\in S,\\
0,&i\notin S.
\end{cases}
\]
In particular, \(\|X_\infty\|_F^2=s/n\le1\), whereas every \(n\times p\) Stiefel frame has squared Frobenius norm \(p\). Therefore the conventional constraint violation \(\mathcal N(X)=\frac12\|X^{\mathsf T}X-I_p\|_F^2\) satisfies
\[
\boxed{\mathcal N(X_\infty)\ge\frac{(p-s/n)^2}{2p}\ge\frac{(p-1)^2}{2p}>0.}
\]
The final universal constant is sharp over the stated class: for \(n=p\) and \(X_0=I_p\), one gets \(X_\infty=I_p/\sqrt p\) and equality. The same limit and violation bound hold for every positive fixed \(\eta\) in the stated interval; no lower bound on \(\eta\) is required.

## Assumptions and scope
The process is defined in exact real arithmetic, with \(n\ge p\ge2\), a **rank-one coordinate sketch** \(B_i=n e_i e_i^{\mathsf T}\), independent uniformly sampled indices across iterations, and a constant effective normal step \(\eta\). The objective function is constant, so there is no tangential component. The sketch is unbiased as an estimator of the identity, since \(\mathbb E B_i=I_n\), but its **reuse within the same normal direction is a deliberate modification** of the two-independent-sketch algorithm. If that algorithm's normal direction is written with a factor \(2\) and weight \(\omega_N\), its effective step here is \(\eta=2\alpha\omega_N\). We do not claim convergence or failure for the algorithm with independent sketches.

The initial matrix is an exact Stiefel frame, hence has full column rank and \(\|r_i\|_2^2\le1\) for every row. At each finite step and in the limit it remains full column rank, because each initially nonzero row is scaled by a strictly positive number. The theorem concerns this invariant, initially feasible class; it is not a result for arbitrary infeasible initial matrices.

## Proof
**Step 1: the row-direction invariant.** Write \(x_i\) for a row of the current matrix. Since \(x_i(x_i^{\mathsf T}x_i)=\|x_i\|_2^2x_i\), direct multiplication yields
\[
B_iX(X^{\mathsf T}B_iX-I_p)=n e_i x_i\bigl(n\|x_i\|_2^2-1\bigr).
\]
Consequently, only sampled row \(i\) changes, and it is multiplied by
\[
1+\beta-\beta y_i,\qquad\beta=\eta n,\quad y_i=n\|x_i\|_2^2.
\]
Zero rows remain zero, and every nonzero row retains its direction whenever this multiplier stays positive.

**Step 2: a scalar monotonic convergence identity.** For every initially nonzero row, \(0<y_i\le n\). Upon sampling the row again its squared magnitude evolves by
\[
y^+=y(1+\beta-\beta y)^2,
\qquad y^+-1=(y-1)g_\beta(y),
\]
where
\[
g_\beta(y)=1-\beta y\bigl(2-\beta(y-1)\bigr).
\]
Because \(0<\beta\le1/(2n)\) and \(0<y\le n\), we have \(0<g_\beta(y)<1\). Indeed the expression subtracted from one is strictly positive; if \(y\ge1\), it is at most \(2\beta y\le1\), with strict inequality at the only possible endpoint; if \(0<y<1\), it is at most \(\beta(2+\beta)\le9/16\). Thus each sampled squared magnitude lies strictly between its previous value and one, unless already one. It stays in \((0,n]\), increases when below one, decreases when above one, and converges to a fixed point, necessarily \(y=1\). Moreover \(1+\beta-\beta y\ge1-\beta(n-1)>0\), so the original row direction and sign do not reverse. The preceding argument applies to the deterministic subsequence of times at which the row is sampled.

**Step 3: almost-sure simultaneous row convergence.** With independent uniform index draws, each of the finitely many rows is selected infinitely often with probability one. Apply Step 2 to each nonzero row on that event. Its normalized magnitude converges to \(\|x_i\|_2=1/\sqrt n\), with the original direction preserved; any initially zero row remains zero. This proves the displayed formula for \(X_\infty\) and shows it is nonrandom. Every row-scaling factor is strictly positive, so full column rank is preserved for every finite step; the limit has full rank as well, since it is obtained by a positive diagonal row scaling of \(X_0\).

**Step 4: a sharp incompatibility with orthogonality.** There are exactly \(s\) nonzero limiting rows, each of squared norm \(1/n\). Hence \(\operatorname{tr}(X_\infty^{\mathsf T}X_\infty)=s/n\le1\). For any real symmetric \(p\times p\) matrix \(G\), Cauchy–Schwarz gives \(\|G-I_p\|_F^2\ge (\operatorname{tr}G-p)^2/p\). Substitute \(G=X_\infty^{\mathsf T}X_\infty\) to obtain the two displayed lower bounds. With \(n=p\) and \(X_0=I_p\), all rows are nonzero and normalize to length \(1/\sqrt p\); thus \(G=I_p/p\) and equality holds.

**Step 5: why sketch independence changes the target.** If two *independent* rank-one sketches \(B_i,B_j\) are used, then
\[
\mathbb E[B_j X(X^{\mathsf T}B_iX-I_p)]=X(X^{\mathsf T}X-I_p),
\]
so the expected normal vector vanishes at every Stiefel frame. Under shared sampling instead,
\[
\mathbb E[B_i X(X^{\mathsf T}B_iX-I_p)]
=\nabla\widetilde{\mathcal N}(X)/2,
\qquad
\widetilde{\mathcal N}(X)=\frac1{2n}\sum_{i=1}^n\bigl(n\|x_i\|_2^2-1\bigr)^2.
\]
Thus the shared-sketch update follows the wrong quartic expected constraint penalty, which seeks normalized row magnitudes instead of orthonormal columns. This verifies the mechanism behind the almost-sure limit rather than merely providing a numerical example.

## Verification
The standalone Python 3 checker `verify.py` uses only the standard library. It checks the scalar recurrence and both independent/shared drift identities over exact-rational grids, the scalar contraction inequalities, the exact two-dimensional Stiefel witness, and full-rank randomly constructed orthonormal frames with overlapping row supports. Simulations support the limiting formula but **do not constitute the infinite-time proof**; the proof is Steps 1–4 and the infinite-visitation property. The checker passed 96,768 total assertions when executed from the packaged source.

For the elementary exact example \(n=p=2\) and \(X_0=I_2\), the almost-sure limit is \(I_2/\sqrt2\) and the constraint violation equals \(1/4\). The same effect occurs at every smaller positive allowed step.

## Relationship to prior work
Goyens, Mataigne and Absil (2026), Section III, define low-rank sketches satisfying \(\mathbb E B_i=I_n\), introduce sparse row selection, and explicitly prescribe **two independent sketches** for their stochastic normal and tangent directions. Their convergence statement presupposes that unbiased structure and a safe-region hypothesis. Vary, Ablin, Gao and Absil (2024), Equation (3), likewise use separate sketches to estimate the normal field on a generalized Stiefel manifold. The exact normal-field identity and independent-sample requirement are credited here.

The present theorem concerns a **different coupling**: it sets the two sketch draws equal and gives the complete long-run row-normalization law, universal infeasibility lower bound for \(p\ge2\), and the sharp dimension-family witness. Those claims are not contained in the inspected independent-sketch convergence statements and do not contradict them. Generic separable quartic coordinate-descent observations explain parts of the mechanism, but do not alone specify its Stiefel-frame geometric consequence. The originality comparison remains conditional on the literature inspected; an unindexed result treating this exact sketch-reuse coupling could subsume it.

## Limitations
This is an exact-arithmetic, constant-effective-step theorem for rank-one uniformly sampled coordinate sketches with **perfect within-update sketch reuse**, a constant objective, and an initially orthonormal frame. The step restriction is a sufficient bound for monotone scalar dynamics; it is **not asserted sharp**. The theorem does not analyze the published independent-sketch algorithm, an objective-dependent tangent field, arbitrary dense or higher-rank sketches, finite-precision rounding, or a general safe-region guarantee. Almost-sure convergence concerns the mathematical iid process, not finite experiments.

## References
1. F. Goyens, S. Mataigne and P.-A. Absil, *The sketched landing method for large-scale optimization under orthogonality constraints*, arXiv:2605.31505, first version May 29, 2026. https://arxiv.org/abs/2605.31505
2. S. Vary, P. Ablin, B. Gao and P.-A. Absil, *Optimization without retraction on the random generalized Stiefel manifold*, arXiv:2405.01702, first version May 2, 2024. https://arxiv.org/abs/2405.01702
