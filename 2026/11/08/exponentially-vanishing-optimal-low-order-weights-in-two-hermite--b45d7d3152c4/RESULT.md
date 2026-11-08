# Exponentially vanishing optimal low-order weights in two-Hermite ambiguity coverage

## Finding

Let \(h_k\) be the unit-norm Hermite function of order \(k\geq0\), normalized so that its centered self-ambiguity function is
\[
\mathcal A h_k(x,\xi)=e^{-t/2}L_k(t),\qquad t=\pi(x^2+\xi^2),\qquad L_k(t)=\sum_{j=0}^{k}\frac{(-1)^j\binom{k}{j}}{j!}t^j.
\]
For fixed integers \(0\leq m<n\), suppose that \(L_m\) and \(L_n\) have no common positive zero. For \(T>0\), let
\[
\rho_{m,n}(T,w)=\min_{0\leq t\leq T}e^{-t}\bigl(wL_m(t)^2+(1-w)L_n(t)^2\bigr),\quad
\rho^*_{m,n}(T)=\max_{0\leq w\leq1}\rho_{m,n}(T,w).
\]
Write \(r_1,\ldots,r_n\) for the positive simple zeros of \(L_n\), and put
\[
 c_{m,n}=\min_{1\leq j\leq n}e^{-r_j}L_m(r_j)^2>0,
 \qquad b_n(T)=e^{-T}L_n(T)^2.
\]
**Theorem.** For every such fixed pair \((m,n)\), and for all sufficiently large \(T\), there is exactly one maximizing weight \(w_{m,n}(T)\), lying strictly between zero and one. It obeys the sharp two-scale laws
\[
 \boxed{w_{m,n}(T)=\frac{b_n(T)}{c_{m,n}}+O_{m,n}(b_n(T)^2)},
\qquad
 \boxed{\rho^*_{m,n}(T)=b_n(T)-\frac{b_n(T)^2}{c_{m,n}}+o_{m,n}(b_n(T)^2).}
\]
The optimal lower-order measurement fraction therefore tends to zero at the explicit rate
\[
 w_{m,n}(T)\sim\frac{e^{-T}T^{2n}}{c_{m,n}(n!)^2},
\]
while the best positive radial ambiguity floor differs from the outer-boundary high-order value by precisely \(b_n(T)^2/c_{m,n}\) to first nontrivial order. In particular, the theorem applies **without extra assumptions** to every adjacent pair \(n=m+1\), because consecutive Laguerre polynomials have no common root.

For the physically simple pair \((m,n)=(1,2)\), the limiting bottleneck is the *inner*, not outer, zero circle of the second-Hermite ambiguity function:
\[
 c_{1,2}=(3-2\sqrt2)e^{-2+\sqrt2}\approx0.0955091130284885,
\qquad
 w_{1,2}(T)\sim\frac{e^{-T}T^4}{4c_{1,2}}.
\]

## Assumptions and scope

The disk is \(\{(x,\xi):\pi(x^2+\xi^2)\leq T\}\). The scalar \(w\) is the fraction of squared channel exposure assigned to \(h_m\), while \(1-w\) is assigned to \(h_n\). The objective is the minimum squared singular value of the **two-channel ambiguity multiplier**
\[
 z\longmapsto\bigl(\sqrt w\,\overline{\mathcal A h_m}\,z,\ \sqrt{1-w}\,\overline{\mathcal A h_n}\,z\bigr)
\]
on that disk. It is not a global nonlinear phase-retrieval error constant. The order pair is fixed before \(T\to\infty\), and the no-common-zero assumption is essential: a shared zero inside the disk forces the minimum to vanish for every weight.

## Proof

1. **The outer interval is controlled by its endpoint.** Set \(P(t)=e^{-t}L_n(t)^2\) and \(Q(t)=e^{-t}L_m(t)^2\). Because each Laguerre polynomial has a nonzero leading coefficient and finitely many roots, there exists \(R_0>0\), beyond the roots, such that \(P,Q\) are strictly positive and strictly decreasing for \(t\geq R_0\). Indeed, their logarithmic derivatives tend to \(-1\). Consequently, for every \(T\geq R_0\) and \(0\leq w\leq1\),
\[
 \rho_{m,n}(T,w)=\min\{G(w),H_T(w)\},\quad
 G(w)=\min_{0\leq t\leq R_0}((1-w)P(t)+wQ(t)),
\]
\[
 H_T(w)=(1-w)b_n(T)+w a_m(T),\qquad a_m(T)=e^{-T}L_m(T)^2.
\]
Here \(a_m(T)/b_n(T)\to0\), so \(H_T\) is strictly decreasing in \(w\) for sufficiently large \(T\).

2. **The compact portion is controlled by Laguerre zeros.** All zeros \(r_j\) of \(L_n\) are simple, positive, and contained in \((0,R_0)\). The no-common-zero assumption makes \(Q(r_j)>0\). At \(w=0\), the minimum of \(G\) is exactly zero, attained precisely at the \(r_j\). Near each such root, \(P(t)\) has a nondegenerate quadratic zero. The implicit-function theorem applied to \(\partial_t((1-w)P+wQ)=0\) yields a unique local minimum at \(r_j+O(w)\), with value \(wQ(r_j)+O(w^2)\). Away from small disjoint root neighborhoods \(P\) is bounded below. Hence, as \(w\downarrow0\),
\[
 G(w)=c_{m,n}w+O_{m,n}(w^2).
\]
In addition, by shrinking the root neighborhoods and choosing \(\delta>0\) small enough, \(Q(t)-P(t)>c_{m,n}/2\) at every active compact minimizer for \(0\leq w\leq\delta\). Comparing affine functions at a minimizer proves that \(G\) is *strictly increasing* on \([0,\delta]\).

3. **The crossing is the unique global maximum.** For sufficiently large \(T\), \(G(0)=0<H_T(0)=b_n(T)\) and \(G(\delta)>H_T(\delta)\). Strict increase of \(G\) and strict decrease of \(H_T\) yield exactly one crossing \(w_T\in(0,\delta)\). Before the crossing, \(G\) is the active constraint and increases; after it, \(H_T\) is active and decreases. Every \(w\geq\delta\) also gives a smaller value, since \(\rho\leq H_T(w)\leq H_T(\delta)<H_T(w_T)\). Thus \(w_T=w_{m,n}(T)\) is the unique global maximizer.

4. **Sharp asymptotics.** The crossing equation and the preceding expansion give
\[
 c_{m,n}w_T+O(w_T^2)=b_n(T)-(b_n(T)-a_m(T))w_T.
\]
First \(w_T=O(b_n(T))\), then \(w_T=b_n(T)/c_{m,n}+O(b_n(T)^2)\), because \(a_m(T)\leq b_n(T)\) for large \(T\). Substitution into \(H_T(w_T)\), using \(a_m(T)/b_n(T)\to0\), proves the second boxed formula. Finally \(L_n(T)\sim(-1)^nT^n/n!\) supplies the displayed exposure scaling.

5. **Adjacent orders and the explicit pair.** The three-term recurrence
\[
 nL_n(t)=(2n-1-t)L_{n-1}(t)-(n-1)L_{n-2}(t)
\]
shows inductively that \(L_n\) and \(L_{n-1}\) cannot share a root, since \(L_0=1\). For \(L_2(t)=1-2t+t^2/2\), the roots are \(2\pm\sqrt2\). Evaluating \(e^{-t}L_1(t)^2\) at both and comparing
\[
 (3+2\sqrt2)e^{-2-\sqrt2}>(3-2\sqrt2)e^{-2+\sqrt2}
\]
shows that the inner circle has smaller weight-lifting slope. The strict inequality follows, for instance, from \(\log(3+2\sqrt2)=2\operatorname{arsinh}(1)>\sqrt2\).

## Verification

The accompanying `check_hermite_weights.py` constructs exact polynomial coefficients of the Laguerre factors, enumerates real stationary points of the one-dimensional weighted objective, and numerically solves the compact-root/outer-endpoint crossing for three adjacent order pairs at four large radii. It checks the weight and deficit ratios predicted above and the identity of the limiting root for \((m,n)=(1,2)\). These finite numerical checks support but do not replace the general analytical proof.

## Relationship to prior work

Alaifari and Yang (arXiv:2410.05486v1, §2.2 and §3.2) derive the radial Hermite ambiguity formula and construct multiwindow coverage by selecting annuli of reliable inversion, but do not optimize a shared exposure split by the smallest squared singular value on an expanding disk, or derive the exponentially vanishing weight and sharp second-order floor defect. Alaifari and Wellershoff (arXiv:2006.10579v1, §4) discuss ambiguity zero circles and uniqueness for Hermite windows, not the weighted maximin design.

The Gaussian-envelope-corrected all-plane ambiguity problem studied elsewhere uses \(\inf_{t\geq0}(wL_m(t)^2+(1-w)L_n(t)^2)\), which is a *different optimization*: it removes \(e^{-t}\), has no finite expanding boundary, and does not imply the present \(T\)-dependent optimal weights or endpoint--root balance. Bibliographic uniqueness is not proven; an equivalent asymptotic optimization could exist under different signal-design terminology.

## Limitations

The onset radius for uniqueness is not explicit. The asymptotics are not uniform in growing Hermite orders. A common Laguerre zero is excluded. No claim is made for nonsymmetric observation sets, more than two channels, unequal frequency-dependent noise, nonlinear phase-retrieval guarantees, or optimal sampling on lattices. The stable multiplier minimum is strictly positive for each sufficiently large but finite disk and decays rapidly as the disk expands.

## References

1. R. Alaifari and Y. Yang, *Multi-Window Approaches for Direct and Stable STFT Phase Retrieval*, arXiv:2410.05486v1, posted 7 October 2024, especially §2.2 and §3.2. https://arxiv.org/abs/2410.05486
2. R. Alaifari and M. Wellershoff, *Uniqueness of STFT phase retrieval for bandlimited functions*, arXiv:2006.10579v1, posted 18 June 2020, especially §4. https://arxiv.org/abs/2006.10579
3. Classical Laguerre recurrence and simple-zero facts, as stated explicitly and used above.
