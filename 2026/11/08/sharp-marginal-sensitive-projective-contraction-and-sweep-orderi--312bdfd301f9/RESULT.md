# Sharp marginal-sensitive projective contraction and sweep ordering for binary Sinkhorn scaling

## Finding

Let \(K=\begin{pmatrix}a&b\\c&d\end{pmatrix}\) have strictly positive real entries, with prescribed row masses \((r,1-r)\) and column masses \((s,1-s)\), where \(r,s\in(0,1)\). One unrelaxed row-then-column Sinkhorn sweep acts on the log-ratio \(u=\log(v_1/v_2)\) of the positive column scaling as a smooth map \(F_{r,s}\). Put
\[
R=\frac{ad}{bc},\qquad \eta_r^2=\frac{r(1-r)(R-1)^2}{R}.
\]
The **exact smallest global projective Lipschitz constant** of this one-sweep map is
\[
\boxed{q(r,R)=\frac{\eta_r^2}{\bigl(1+\sqrt{1+\eta_r^2}\bigr)^2}.}
\]
For all positive column scalings \(v,w\), the projective distance \(d_H(v,w)=|\log(v_1/v_2)-\log(w_1/w_2)|\) decreases by at most the factor \(q(r,R)<1\) per complete sweep, and no smaller universal factor can hold. Thus the unique projective fixed point \(u_{\mathrm{fix}}\) satisfies \(|u_k-u_{\mathrm{fix}}|\le q(r,R)^k|u_0-u_{\mathrm{fix}}|\) for every \(k\ge0\). When \(R=1\), one sweep reaches the fixed point exactly.

The generic two-positive-map Birkhoff bound is
\[
q_B(R)=\left(\frac{\sqrt R-1}{\sqrt R+1}\right)^2.
\]
For \(R\ne1\), the sharp constant satisfies \(q(r,R)\le q_B(R)\), with equality exactly when \(r=1/2\); the inequality is strict for every imbalanced row target. It is independent of the column mass \(s\). The reverse column-then-row sweep, considered in the corresponding row log-ratio projective coordinate, has sharp constant \(q(s,R)\). Consequently, among these two projective global Lipschitz certificates, for \(R\ne1\), row-first is optimal exactly when \(r(1-r)\le s(1-s)\), and column-first is optimal exactly when \(s(1-s)\le r(1-r)\); for \(R=1\), both orientations have zero contraction. This certificate comparison does not claim that one order is faster on every individual trajectory or has a different local limiting rate.

For example, when \(K=\begin{pmatrix}20&1\\1&20\end{pmatrix}\), \(r=0.01\), and \(s=0.5\), the row-first sharp factor is approximately \(0.379395\), versus \(0.818594\) for column-first and the standard Birkhoff bound.

## Assumptions and scope

The kernel is any real, strictly positive \(2\times2\) matrix; both target marginals have positive entries summing to one. There is no symmetry, small-step, bounded-iterate, or proximity-to-solution assumption. Each half-step exactly enforces one target marginal, without overrelaxation. The projective metric is the absolute difference of log-component ratios, which is precisely Hilbert's projective metric in dimension two. The bound concerns the map on scaling factors in these intrinsic log-ratio coordinates, not Euclidean distances between arbitrary plans or marginal errors. The reverse order uses row-scaling coordinates, so the ordering comparison is between dimensionless global projective contraction certificates.

## Proof

Write \(A=a/b\), \(C=c/d\), \(x=e^u\), and
\[
p_1(u)=\frac{Ax}{1+Ax},\quad p_2(u)=\frac{Cx}{1+Cx},\quad m(u)=r p_1(u)+(1-r)p_2(u).
\]
After row normalization, the first-column mass is \(m\), while the second-column mass is \(1-m\). Column scaling by its target masses therefore gives the exact log-ratio update
\[
F_{r,s}(u)=u+\log\frac{s}{1-s}+\log\frac{1-m(u)}{m(u)}.
\]
By differentiating the two logistic functions, one obtains
\[
m'=r p_1(1-p_1)+(1-r)p_2(1-p_2),\qquad m(1-m)-m'=r(1-r)(p_1-p_2)^2.
\]
Hence the derivative is nonnegative and equals
\[
F_{r,s}'(u)=1-\frac{m'}{m(1-m)}=\frac{r(1-r)(p_1-p_2)^2}{m(1-m)}.
\]
In particular it is independent of the prescribed column mass \(s\). When \(R=1\), the two conditional probabilities are identical for every \(u\), and \(F'\equiv0\).

Suppose \(R\ne1\). Set \(k=\sqrt R\), \(t=\sqrt{AC}\,e^u>0\), and define \(U=(1-r)+rk^2\), \(V=r+(1-r)k^2\). Direct cancellation in the last expression gives
\[
F_{r,s}'(u)=\frac{r(1-r)(k^2-1)^2 t}{(U+kt)(k+Vt)}.
\]
The reciprocal of the \(t\)-dependent fraction is
\[
\frac{(U+kt)(k+Vt)}{t}=\frac{kU}{t}+UV+k^2+kVt.
\]
By the arithmetic–geometric mean inequality, its unique minimum occurs at \(t_*=\sqrt{U/V}\), where it equals \((\sqrt{UV}+k)^2\). Since \(UV=k^2+r(1-r)(k^2-1)^2\), the supremum of \(F'\) is exactly
\[
\frac{r(1-r)(k^2-1)^2}{(\sqrt{UV}+k)^2}
=\frac{\eta_r^2}{(1+\sqrt{1+\eta_r^2})^2}=q(r,R).
\]
This value is attained by the derivative at the finite input \(u_{\mathrm{peak}}=\log(t_*/\sqrt{AC})\). The fundamental theorem of calculus proves the global Lipschitz inequality; taking two inputs approaching this maximizer proves that any smaller constant fails. Moreover \(0\le q<1\) for every finite positive kernel and interior marginal, so the contraction mapping theorem supplies a unique fixed point and the stated global iterated estimate.

The function \(h(z)=z/(1+\sqrt{1+z})^2\) is strictly increasing for \(z>0\). Since \(r(1-r)\le1/4\), with equality precisely at \(r=1/2\), this proves the comparison to the balanced case. When \(r=1/2\), \(\sqrt{UV}=(1+k^2)/2\), and the sharp constant simplifies to \((k-1)^2/(k+1)^2=q_B(R)\). Applying the same argument to the transposed kernel and swapped margins gives the exact reverse-order factor \(q(s,R)\). Strict monotonicity of \(h\) proves the claimed ordering criterion. This completes the proof, including the degenerate case \(R=1\).

## Verification

The accompanying standard-library `verify.py` checks the logistic derivative identity in exact rational arithmetic over 972 enumerated configurations, then tests 4,200 positive kernels and interior marginals using independent matrix-scaling updates, finite-difference derivatives, analytic derivative maximizers, projective contraction, reverse ordering and the Birkhoff bound. The largest recorded finite-difference discrepancy in this stress test is about \(2.31\times10^{-8}\); the finite-difference tolerance is \(10^{-7}\). Run `python3 verify.py` in the directory containing the file. All conclusions quantified over infinitely many kernels, margins and initial scalings are established by the preceding analytic argument, not by finite experiments.

## Relationship to prior work

The alternating row/column normalization map and Hilbert-projective contraction are classical. Lehmann, von Renesse, Sambale and Uschmajew (2021/2022) establish the general Birkhoff contraction factor \(\Lambda(K)^2\) and analyze overrelaxation and local rates; for a binary kernel the factor is \(q_B(R)\). The present result computes the **smallest global** factor for each fixed, possibly imbalanced binary row marginal and compares both sweep orders. The general derivative formulation of Forde (2026) also provides a pointwise Markov-composition approach, but does not state the optimized one-dimensional binary envelope or the marginal-imbalance orientation criterion. Xu and Chen (2026) study an accelerated method, not this exact global constant; Gao, Qu, Ye and Udell (2026) treat tight local convergence, a different quantifier. The equal-marginal case recovers the classical factor rather than claiming to improve it.

## Limitations

The result is confined to strictly positive \(2\times2\) kernels and exact, unrelaxed, alternated scaling. It does not prove a dimension-independent improvement for larger kernels, numerical speedup, Euclidean-plan contraction, or an advantage for every trajectory. Its order comparison concerns sharp global projective envelopes on different scaling spaces; the local asymptotic convergence eigenvalue is not asserted to differ by order. Earlier binary contingency-table or IPFP literature may contain equivalent optimizations not indexed by the searches performed; scientific priority is therefore provisional. No independent mathematical audit is claimed.

## References

1. Xu and Chen, *Accelerating Sinkhorn for Entropy-Regularized Optimal Transport*, arXiv:2605.30267v1, first posted 2026-05-28, https://arxiv.org/abs/2605.30267.
2. Lehmann, von Renesse, Sambale and Uschmajew, *A note on overrelaxation in the Sinkhorn algorithm*, Optimization Letters, https://doi.org/10.1007/s11590-021-01830-0.
3. Gao, Qu, Ye and Udell, *Tight Nonasymptotic Local Convergence of Sinkhorn–Knopp*, arXiv:2608.11760v1, https://arxiv.org/abs/2608.11760.
4. Forde, *Transport Topology for Fixed-Support Sinkhorn Layers*, arXiv:2609.07954v1, https://arxiv.org/abs/2609.07954.
5. Knight, *The Sinkhorn–Knopp Algorithm: Convergence and Applications*, SIAM Journal on Matrix Analysis and Applications 30 (2008), https://doi.org/10.1137/060659624.
