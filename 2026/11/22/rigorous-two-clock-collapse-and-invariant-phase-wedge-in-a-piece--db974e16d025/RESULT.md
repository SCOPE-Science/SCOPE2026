# Rigorous two-clock collapse and invariant phase wedge in a piecewise-smooth competition map

## Finding

For the map of maximal presences introduced by Satur [1] at its critical resource value \(\alpha=2\), every nonsymmetric initial pair has an exact asymptotic two-step contraction ratio of \(3/4\), while symmetric initial pairs have exact one-step contraction asymptotic to \(1/2\). More precisely, put
\[
\Phi(x,y)=\left(\frac{\max\{2x(1-y),1-x\}}{2x(1-y)+1-x},\frac{\max\{2y(1-x),1-y\}}{2y(1-x)+1-y}\right),\quad \frac12\le x,y<1,
\]
and write \(u_t=2x_t-1\), \(v_t=2y_t-1\). For every \(x_0\ne y_0\), after possibly exchanging the two coordinates there is an integer \(N\ge0\) and a vector \((U,V)\) with \(U>0\) and \(0\le V\le U/2\) such that
\[
\lim_{k\to\infty}\left(\frac43\right)^k(u_{N+2k},v_{N+2k})=(U,V),\qquad
\lim_{k\to\infty}\left(\frac43\right)^k(u_{N+2k+1},v_{N+2k+1})=(U-V/2,U/2-V).
\]
The set \(\mathcal P=\{(u,v):0\le v<u<1,\ 2v-u-uv\le0\}\) is forward invariant, and \(N\) can be chosen at its first entrance. Thus, for \(G_t=\max(x_t,y_t)\),
\[
\lim_{t\to\infty}\frac{G_{t+2}-1/2}{G_t-1/2}=\frac34\quad\text{when }x_0\ne y_0.
\]
For \(x_0=y_0>1/2\), the deviations coincide and satisfy the *exact* law
\[
 u_t=v_t=\frac{1}{2^t(1/u_0+1)-1},\qquad \lim_{t\to\infty}2^tu_t=\frac{u_0}{1+u_0}.
\]
The uniform initial point is fixed. This establishes rigorously the asymmetric \(3/4\) two-step rate that [1, Section 5.2] reported numerically and derived only from a leading-order model.

## Assumptions and scope

All iterates refer to the continuous, well-defined **maximal-value map** \(\Phi\) on \([1/2,1)^2\), not to an arbitrary convention for selecting the dominant position in the underlying full probability-vector dynamics when a tie occurs. The parameter is exactly \(\alpha=2\), and all nonuniform initial coordinates are strictly less than one. The ordered case \(u_0>v_0\ge0\) suffices by exchange symmetry; if initially \(v_0>u_0\), exchange labels throughout. No uniformity of the entrance time \(N\) over all asymmetric initial data is asserted.

## Proof

**1. Exact deviation dynamics and strict order preservation.** Direct reduction of \(\Phi\) gives
\[
 F(u,v)=\left(\frac{|2u-v-uv|}{2-v-uv},\frac{|2v-u-uv|}{2-u-uv}\right),\qquad 0\le u,v<1.
\]
Both denominators are positive. For \(0\le v<u<1\), set \(A=2u-v-uv>0\), \(B=2-v-uv>0\), \(C=2v-u-uv\), and \(D=2-u-uv>0\). When \(C\ge0\),
\[
 AD-CB=2(u-v)(3-u-v-uv)>0;
\]
when \(C<0\),
\[
 AD+CB=2(1-u)(1-v)(uv+u+v)>0.
\]
Therefore \(0\le v_{t+1}<u_{t+1}<1\) whenever \(v_t<u_t\). The larger deviation is always \(u_t\), with
\[
 u_{t+1}=\frac{A}{B}=u_t-\frac{v_t(1-u_t^2)}{B}\le u_t.
\]
The inequality is strict for \(v_t>0\). If \(v_t=0<u_t\), then \(u_{t+1}=u_t\) but \(v_{t+1}=u_t/(2-u_t)>0\), so \(u_{t+2}<u_t\). It follows that \(u_t\downarrow0\): otherwise a convergent subsequence \((u_{t_j},v_{t_j})\to(\bar u,\bar v)\) with \(\bar u>0\) would have \(u_{t_j+2}-u_{t_j}\to0\), contradicting the continuous strict two-step decrease at every state with \(\bar u>\bar v\ge0\). The case \(\bar u=\bar v>0\) is also excluded because on the diagonal \(F(\bar u,\bar u)=(\bar u/(2+\bar u),\bar u/(2+\bar u))\), which strictly decreases the maximum. Thus \((u_t,v_t)\to(0,0)\). This also independently verifies the global-collapse premise used below.

**2. A forward-invariant exact branch wedge.** Define \(\mathcal P\) by \(C=2v-u-uv\le0\) in the ordered half square. On this set \(F(u,v)=(A/B,-C/D)\). A direct rational identity gives
\[
 2v'-u'-u'v'=-\frac{2v(1-u)(3-u-v-uv)}{BD}\le0.
\]
Hence \(\mathcal P\) is forward invariant, including its boundary. (The displayed right-hand side is nonpositive; it is strictly negative if \(v>0\).)

**3. Finite entrance for every asymmetric orbit.** Suppose an ordered orbit never enters \(\mathcal P\). Then \(C_t>0\) for every step, and \(v_t'=C_t/D_t\). For \(q_t=(u_t-v_t)/u_t\in(0,1]\), the order identity from step 1 yields
\[
 \frac{q_{t+1}}{q_t}=
 \frac{2u_t(3-u_t-v_t-u_tv_t)}{(2u_t-v_t-u_tv_t)(2-u_t-u_tv_t)}.
\]
Eventually \(u_t\le1/4\), by step 1. In this region the first denominator factor is at most \(2u_t\), the second at most \(2\), and the factor in parentheses in the numerator is at least \(39/16\). Therefore \(q_{t+1}\ge(39/32)q_t\) for every subsequent all-active step. This contradicts \(q_t\le1\). Thus entrance occurs in finite time, and step 2 keeps the orbit in \(\mathcal P\) thereafter.

**4. Exact two-step map and asymptotic amplitude.** On \(\mathcal P\), both the first and second updates use the same branch selection. Direct substitution yields
\[
\begin{split}
 u_{t+2}&=\frac{3u_t+u_tv_t-2v_t^2-2u_tv_t^2}{4+u_t-u_tv_t-2v_t^2-2u_tv_t^2},\\
 v_{t+2}&=\frac{v_t(3-u_t-v_t-u_tv_t)}{4-v_t-v_t^2-u_tv_t-u_tv_t^2}.
\end{split}
\]
Because \(0\le v_t\le u_t/(2-u_t)\), as \(u_t\to0\) these formulas give **uniform relative** estimates along the wedge,
\[
 \frac{u_{t+2}}{u_t}=\frac34+O(u_t),\qquad
 \frac{v_{t+2}}{v_t}=\frac34+O(u_t)\quad(v_t>0).
\]
All denominators are bounded away from zero sufficiently near the origin. In particular, after a finite index, \(u_{t+2}\le(4/5)u_t\), so \(\sum_k u_{N+2k}<\infty\). The infinite products of the positive ratios \([u_{N+2k+2}/u_{N+2k}]/(3/4)=1+O(u_{N+2k})\) converge to a **strictly positive finite** limit; the same applies to the \(v\)-coordinate if it is nonzero at the entry time. If it is zero there, the exact two-step formula keeps it zero. Consequently there exist \(U>0\), \(V\ge0\) with
\[
 (u_{N+2k},v_{N+2k})=(3/4)^k((U,V)+o(1)).
\]
The wedge inequality implies \(V/U\le1/2\). Finally, within the wedge
\[
 F(u,v)=(u-v/2,\ u/2-v)+O(u^2),
\]
so applying one additional iterate proves the odd-time vector limit. The ratio for \(G_t\) follows, since the first coordinate remains the larger deviation and all limiting first-coordinate amplitudes are positive.

**5. Symmetric initial data.** If \(u_0=v_0>0\), symmetry implies \(u_t=v_t\) and the exact reduction is \(u_{t+1}=u_t/(2+u_t)\). Thus \(1/u_{t+1}=2/u_t+1\), whose solution is the stated closed formula. The origin is fixed.

## Verification

Run `python3 check.py` from this package. The exact-rational checker confirms the deviation update, order preservation, the passive-wedge invariant and the rational two-step formulas on 6,510 rational pairs (4,855 passive), tests the explicit symmetric recursion for 4,949 rational initial conditions with eight iterates each, and checks an exact-rational asymmetric example. These are finite cross-checks of algebra, *not* proofs for all real initial states. The proof in the preceding section establishes all quantified claims.

## Relationship to prior work

Satur [1] introduces this map, establishes qualitative global convergence at \(\alpha=2\), and in Section 5.2 reports the conjectured two-step rate \(3/4\) based on simulations and a piecewise-linear approximation; that section explicitly notes that a proof requires control of second-order terms. Our contribution is the global finite-entry lemma for an **exact** invariant nonlinear wedge, an explicit rational two-step map, and convergent normalized even/odd orbit vectors. The numerical value \(3/4\) and the linearized involution are **not** claimed as new observations. Simpson [2] proves general perturbative exponential-stability results for piecewise-homogeneous maps; those general results do not state this model-specific sharp amplitude and parity law.

## Limitations

Only the critical resource parameter is treated. The positive amplitude \(U\) and phase \(V/U\) are defined by convergent limits, not by a closed elementary formula for all initial conditions; the entrance time is finite but not uniformly bounded near the diagonal. Full-position tie-breaking is outside scope. Historical priority for any unindexed model-specific proof remains unresolved; no independent validation is asserted.

## References

[1] O. R. Satur, *From oscillations to symmetry breaking in a two-dimensional piecewise-smooth dynamical system*, arXiv:2611.13318v1 (first public 2026-11-09), especially Theorem 2 and Section 5.2. https://arxiv.org/abs/2611.13318

[2] D. J. W. Simpson, *The stability of fixed points on switching manifolds of piecewise-smooth continuous maps*, arXiv:1612.02932v1 (2016), Sections 1–3; J. Dyn. Differential Equations 32 (2020), 1527–1552. https://arxiv.org/abs/1612.02932
