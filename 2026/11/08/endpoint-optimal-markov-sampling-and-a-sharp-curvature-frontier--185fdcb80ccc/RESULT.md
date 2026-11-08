# Endpoint-optimal Markov sampling and a sharp curvature frontier for scalar SGD

## Finding

For two strongly convex scalar component losses with opposite affine offsets, the stationary mean-square error of constant-step stochastic gradient descent can be minimized exactly over **every** symmetric two-state Markov sampling schedule. Contrary to the expectation that partially alternating samples might yield the best balance, no genuinely stochastic interior switching probability improves on both deterministic endpoints. At small normalized steps the unique optimum is perfect alternation; at sufficiently large but individually stable steps, perfect persistence can be better. A persistence-optimal admissible step exists precisely when the relative curvature contrast is less than \(1/2\).

For \(a>0\), \(b\ne0\), \(0\le t<1\), let
\[
f_s(x)=\frac{a(1+st)}2x^2+sbx,\qquad s\in\{-1,1\}.
\]
The average objective is \(F(x)=ax^2/2\), with minimizer \(x_*=0\). Choose \(S_k\) from the stationary symmetric Markov chain with \(\Pr(S_{k+1}=S_k)=p\in[0,1]\) and \(\Pr(S_0=1)=\Pr(S_0=-1)=1/2\), and perform
\[
x_{k+1}=x_k-\eta f'_{S_k}(x_k).
\]
Let \(h=\eta a\), \(r=2p-1\), \(A=1-h\), \(D=ht\), \(Q=A^2+D^2\), and \(U=1-h(1-t^2)\). Throughout, require
\[
0<h<\frac{2}{1+t},
\]
which makes both component step maps strict contractions. For each real deterministic \(x_0\), the limit exists and is
\[
\lim_{k\to\infty}\mathbb E[x_k^2]=\left(\frac ba\right)^2V(r),\quad
V(r)=\frac{h^2\big[(1+Ur)(1-Qr)+4Aht^2r^2\big]}{(1-Ur)\big[(1-Q)(1-Qr)-4A^2h^2t^2r\big]}.
\]
All denominators displayed here are strictly positive for \(-1\le r\le1\).

The exact global minimizers on the *closed* range \(0\le p\le1\) are:

- If \(h(1-t^2)<1\), **only** \(p=0\) (perfect alternation).
- If \(h(1-t^2)>1\), **only** \(p=1\) (one random sign retained forever).
- If \(h(1-t^2)=1\) and \(t>0\), exactly the two endpoints \(p=0,1\), tied; every \(0<p<1\) is worse.
- If \(h=1,t=0\), all probabilities are tied, because the next iterate equals the negative of the current sampled sign.

The endpoint risks are
\[
V(-1)=\frac{h^2(1+t^2)}{[2-h(1-t^2)]^2},\qquad
V(1)=\frac{1+t^2}{(1-t^2)^2}.
\]
The crossover step \(h_*=1/(1-t^2)\) is inside the stability range if and only if \(t<1/2\). Therefore for \(t\ge1/2\) perfect alternation is strictly optimal at every admissible step. At \(t=1/4\), \(h=7/5\), the persistence risk equals \(272/225\), less than the alternating risk \(13328/3025\); but at \(h=1/2\), alternation is better, with risk \(272/2401\) versus \(272/225\).

## Assumptions and scope

The sign process is exogenous, stationary at the initial time, and follows the same symmetric transition rule at every iteration. At \(p=1\) its initially selected sign is fixed for all time; at \(p=0\) signs alternate deterministically with a uniformly random initial phase. There is exactly one component-gradient evaluation per iteration and no additional independent gradient noise. The stationary optimization criterion is the limit of \(\mathbb E[x_k^2]\); it equals twice the stationary expected objective gap divided by \(a\). The initial iterate is arbitrary deterministic, independent of the sign chain. This theorem concerns fixed \(h>0\), not a diminishing-step limit.

All assumptions matter: for steps outside \(0<h<2/(1+t)\), the uniform contraction and positive-denominator argument are not asserted; for nonsymmetric or state-dependent sampling, the proof does not apply. Both losses are individually strongly convex since \(0\le t<1\).

## Proof

**Step 1: exact moment recursion.** Normalize \(y_k=(a/b)x_k\). Then
\[
y_{k+1}=(A-DS_k)y_k-hS_k,
\]
while \(\mathbb E[S_{k+1}\mid S_k]=rS_k\). Put
\[
g_k=\mathbb E[y_k],\quad H_k=\mathbb E[y_kS_k],\quad
v_k=\mathbb E[y_k^2],\quad W_k=\mathbb E[y_k^2S_k].
\]
Direct expansion and conditional expectation give **exactly**
\[
\begin{aligned}
g_{k+1}&=Ag_k-DH_k,\\
H_{k+1}&=r(AH_k-Dg_k-h),\\
v_{k+1}&=Qv_k-2ADW_k+2hDg_k-2AhH_k+h^2,\\
W_{k+1}&=r(QW_k-2ADv_k+2hDH_k-2Ahg_k).
\end{aligned}
\]
Because both possible multipliers \(A\pm D=1-h(1\mp t)\) have modulus strictly less than one, the affine trajectories are uniformly contractive under common sign paths. The stationary joint moment solution is unique and each expected moment converges to it, also at the two deterministic endpoints. Solving the four linear equations yields the stated rational formula for \(V(r)\); the signed mixed stationary moment is \(H=-rh/(1-Ur)\) and \(g=-DH/h\).

**Step 2: strictly positive denominator.** Put
\[
\Delta(r)=(1-Ur)\big[(1-Q)(1-Qr)-4A^2D^2r\big].
\]
The stability condition implies \(|U|<1\) and \(Q<1\). The second factor is affine in \(r\); at \(r=1\) it equals \([1-(A+D)^2][1-(A-D)^2]>0\), and at \(r=-1\) it equals \(1-Q^2+4A^2D^2>0\). Thus \(\Delta(r)>0\) throughout \([-1,1]\). Substitution produces the two endpoint formulas, with
\[
V(1)-V(-1)=\frac{4(1+t^2)U}{(1-t^2)^2[2-h(1-t^2)]^2}.
\]

**Step 3: global optimization, not merely endpoint comparison.** Let \(q=1-t^2\) and \(u=U=1-hq\). The positive-denominator function \(V(r)\) is a ratio of quadratic polynomials. The polynomial \(\Delta(r)[V(r)-V(-1)]\) vanishes at \(r=-1\), hence equals \((r+1)L_-(r)\) for an affine polynomial \(L_-\). By elementary interpolation, \(L_-(r)\ge0\) on \([-1,1]\) if its two endpoint values are nonnegative. Those values have the signs of \(V'(-1)\) and \(V(1)-V(-1)\). The symmetric argument with \(\Delta(r)[V(r)-V(1)]=(1-r)L_+(r)\) uses \(V'(1)\) and \(V(-1)-V(1)\). Derivatives are exact:
\[
V'(-1)=\frac{2hJ}{q^2(2-hq)^3(2-2h+h^2q)},
\]
\[
J=(4-2u)z^2+(u^3-5u)z+u^3+u,\qquad z=t^2,
\]
\[
V'(1)=-\frac{2G}{hq^3[2-h(1-t)][2-h(1+t)]},
\quad G=\frac{4z^2-(1+z)u(u+1)}q.
\]
When \(u\ge0\), we have \(u<1\) and the **explicit square decomposition**
\[
\begin{aligned}
J={}&(4-2u)\left(z-\frac{u(5-u^2)}{8-4u}\right)^2\\
&+\frac{u(1-u)^2(16-u-2u^2-u^3)}{8(2-u)}\ge0.
\end{aligned}
\]
Both terms are nonnegative because \(0\le u<1\). Combined with \(V(1)-V(-1)\ge0\), the affine-factor argument gives \(V(r)\ge V(-1)\) for every \(r\), strictly for \(-1<r\le1\) when \(u>0\).

When \(u\le0\), the stability condition yields \(-1<u\le0\), so \(G=[4z^2-(1+z)u(u+1)]/q\ge0\). Thus \(V'(1)\le0\), and since \(V(1)-V(-1)\le0\), the other affine-factor argument gives \(V(r)\ge V(1)\) for every \(r\), strictly for \(-1\le r<1\) when \(u<0\). When \(u=0\), both endpoints tie; the derivatives are strictly signed if \(t>0\), so the interior is strictly worse. When \(u=t=0\), one has \(h=1\) and \(V(r)=1\) identically. This proves the complete optimizer classification.

**Step 4: sharp contrast threshold.** The crossover \(h=1/q\) lies strictly below \(2/(1+t)\) precisely when \(1<2(1-t)\), or \(t<1/2\). The endpoint comparisons above are sharp, so the threshold cannot be improved within this family.

## Verification

Run `python checks/verify.py` with Python 3 and SymPy. The standalone script symbolically checks the four-moment stationary fixed point, the rational risk, endpoint formulas, derivative identities, and the nonnegative square decomposition. It then uses exact rational arithmetic to compare the moment recurrence against enumerated Markov paths at 600 finite horizons, and checks 306 exact stationary fixed points and interior inequalities. These finite checks are **not** used to infer the all-parameter theorem: Steps 1–4 provide the analytic proof. Independent specialist validation has not been performed.

## Relationship to prior work

Even, *Stochastic Gradient Descent under Markov-Chain Sampling Schemes* (2023, arXiv:2302.14428, Appendix D.2), studies a symmetric two-state chain with equal-curvature scalar quadratics and derives a finite-horizon noise-correlation expression for lower bounds. This materially overlaps the equal-curvature test mechanism: **that special case is not proposed here as independently new**. The separate claim is the complete unequal-curvature fixed-step stationary-risk optimization, the endpoint-optimality proof for all switching probabilities, and its sharp contrast boundary. Doan et al. (2020) give finite-time SGD bounds with diminishing steps under Markov sampling, not this fixed-step exact optimization. Liu and Xu (2018) use negatively correlated samples **within** minibatches, rather than a single sample per step from a cross-iteration Markov chain. These inspected texts do not furnish the present heterogeneous-curvature global frontier; however more general Markov-jump affine-recursion and stochastic-control formulas may indirectly subsume parts of the calculation. A lack of located matching titles is not proof of publication novelty.

## Limitations

The statement is exact only for two symmetric scalar quadratic components with opposite affine residuals, a uniform starting sign, a fixed stable step, and a symmetric exogenous Markov transition. The fact that \(p=1\) sometimes minimizes stationary mean-square risk does **not** mean frozen-component SGD converges to the full-objective minimizer: it converges to the selected component's minimizer. The result does not prove any large-dimensional, nonlinear, nonstationary, unconstrained-step, or arbitrary-chain extension. Publication-precedence uncertainty remains around equivalent stationary-covariance calculations in classical Markov-jump system literature.

## References

1. Mathieu Even, *Stochastic Gradient Descent under Markovian Sampling Schemes*, arXiv:2302.14428, initial public version 2023-02-28. <https://arxiv.org/html/2302.14428v3>; Appendix D.2.
2. Thinh T. Doan, Lam M. Nguyen, Nhan H. Pham and Justin Romberg, *Finite-Time Analysis of Stochastic Gradient Descent under Markov Randomness*, arXiv:2003.10973, 2020. <https://arxiv.org/html/2003.10973v2>; Sections 2–3.
3. Jingchang Liu and Linli Xu, *Accelerating Stochastic Gradient Descent Using Antithetic Sampling*, arXiv:1810.03124, 2018. <https://arxiv.org/html/1810.03124v1>; Sections 3–4.
