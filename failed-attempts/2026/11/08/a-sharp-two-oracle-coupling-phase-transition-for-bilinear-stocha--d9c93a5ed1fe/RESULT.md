# A sharp two-oracle coupling phase transition for bilinear stochastic extragradient

## Finding

Consider the interpolating two-component bilinear saddle problem with sample losses \(f_1(x,y)=a xy\), \(f_2(x,y)=b xy\), where \(0<a<b\). Each stochastic extragradient (SEG) predictor call and corrector call uses one of the two component operators, with each call marginally uniform. The two calls within one iteration may be arbitrarily coupled, and the pairs are independently resampled between iterations. Both stages use the same positive stepsize \(\eta\).

**Theorem (complete coupling and stability phase law).** Write \(z_n=(x_n,y_n)\), \(s=\eta^2\), and \(p=\Pr(A=B)\), where \(A\) and \(B\) are the sampled predictor and corrector coefficients. Every admissible joint distribution is uniquely determined by \(p\in[0,1]\). For every deterministic \(z_0\) and integer \(n\ge0\),
\[
\mathbb E\|z_n\|^2 = Q_p(s)^n\|z_0\|^2,
\qquad Q_p(s)=pQ_{\mathrm{same}}(s)+(1-p)Q_{\mathrm{anti}}(s),
\]
where
\[
\begin{aligned}
Q_{\mathrm{same}}(s)&=1-\frac{a^2+b^2}{2}s+\frac{a^4+b^4}{2}s^2,\\
Q_{\mathrm{anti}}(s)&=1+\left(\frac{a^2+b^2}{2}-2ab\right)s+a^2b^2s^2.
\end{aligned}
\]
The unique risk-minimizing coupling at each fixed \(s>0\), except at the tie, is the **same component at both stages** when \(s<2/(a+b)^2\), and the **opposite component at the two stages** when \(s>2/(a+b)^2\). At equality all couplings have the same risk.

There is a sharp ratio at which the coupling maximizing the *admissible mean-square-stable stepsize* changes. Put
\[
R_* =\frac{1+\sqrt5+\sqrt{2+2\sqrt5}}2
=2.890053638263\ldots,
\qquad r=b/a>1.
\]
The supremal stable **squared stepsize** over all admissible couplings is
\[
S_*(a,b)=
\begin{cases}
\dfrac{4ab-a^2-b^2}{2a^2b^2},&1<r<R_*,\\[3pt]
\dfrac{a^2+b^2}{a^4+b^4},&r>R_*.
\end{cases}
\]
At \(r=R_*\), the two formulas agree and every coupling has the same sharp stable ceiling. Thus antithetic sampling uniquely maximizes this ceiling for \(1<r<R_*\), while same-sample sampling uniquely maximizes it for \(r>R_*\). The endpoint is excluded: mean-square convergence occurs for \(0<s<S_*\) under some coupling, never at \(s=S_*\).

In contrast, if the stepsize and coupling are optimized **jointly for the fastest mean-square geometric contraction**, then same-sample coupling is always uniquely optimal for every \(0<a<b\), with
\[
\boxed{\min_{s>0,\ p\in[0,1]}Q_p(s)
=1-\frac{(a^2+b^2)^2}{8(a^4+b^4)}}
\]
attained only at \(p=1\) and \(s=(a^2+b^2)/[2(a^4+b^4)]\). Maximizing the allowable stepsize and minimizing the convergence factor are therefore genuinely different design objectives.

For \((a,b)=(1,2)\) and \(s=1/3\), the mean-square multipliers are exactly \(Q_{\mathrm{same}}=10/9\), \(Q_{\mathrm{iid}}=37/36\), and \(Q_{\mathrm{anti}}=17/18\): same-sample and independent predictor/corrector sampling both diverge in mean square, but antithetic coupling contracts at the same two-call cost.

## Assumptions and scope

The sample operator is \(F_c(z)=cJz\), where \(J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\), and \(c\in\{a,b\}\). The population saddle function is \(\mathbb Ef_c(x,y)=(a+b)xy/2\), with unique saddle point \((0,0)\). Every component operator is monotone (indeed skew), and every sample vanishes at the equilibrium. The unconstrained two-stage update is
\[
z_{n+1/2}=z_n-\eta F_A(z_n),\qquad
z_{n+1}=z_n-\eta F_B(z_{n+1/2}).
\]
Both \(A\) and \(B\) individually have probability \(1/2\) of each coefficient. The joint pair is independent across iterations, but its two members need not be independent. The process starts at any deterministic state. Mean-square stability refers to \(\mathbb E\|z_n\|^2\to0\) for every initial state; no assertion about other convergence notions is used in the theorem.

## Proof

Since \(J^2=-I\), direct substitution into the two-stage update gives
\[
z_{n+1}=\left((1-sAB)I-\eta BJ\right)z_n.
\]
The two terms are mutually orthogonal when applied to a real vector, as \(z^\top Jz=0\), and \(J\) preserves Euclidean norm. Consequently the **conditional** squared-norm multiplier is the scalar
\[
q(A,B;s)=(1-sAB)^2+sB^2.
\]
Every coupling of two uniform binary variables has joint masses \(\Pr(a,a)=\Pr(b,b)=p/2\) and \(\Pr(a,b)=\Pr(b,a)=(1-p)/2\). Averaging these four explicit multipliers gives the stated \(Q_p\). Iteration-wise independence then proves the exact \(n\)-step moment formula by conditional expectation.

The difference is the factorization
\[
Q_{\mathrm{same}}(s)-Q_{\mathrm{anti}}(s)
=s(b-a)^2\left(-1+\frac{s(a+b)^2}{2}\right).
\]
Because \(Q_p\) is affine in \(p\), this proves the sharp unique optimizer for every fixed \(s\), including the tie.

For each fixed coupling, \(Q_p(s)=1-A_ps+B_ps^2\) with \(B_p>0\). Thus its stable squared-step interval is exactly \(0<s<A_p/B_p\) when \(A_p>0\), and it is empty otherwise. A ratio of affine functions of \(p\) attains its maximum at one of the endpoints, so the overall stability ceiling is the larger of the same-sample ceiling
\[
S_{\mathrm{same}}=\frac{a^2+b^2}{a^4+b^4}
\]
and the antithetic ceiling \(S_{\mathrm{anti}}=(4ab-a^2-b^2)/(2a^2b^2)\), the latter being usable only when its numerator is positive. Put \(r=b/a\). Their difference has the exact sign factorization
\[
S_{\mathrm{anti}}-S_{\mathrm{same}}
=-\frac{(r-1)^2(r^4-2r^3-2r^2-2r+1)}{2a^2r^2(1+r^4)}.
\]
For \(r>1\), division of the quartic by \(r^2\) and substitution \(u=r+r^{-1}>2\) yields \(u^2-2u-4\). This is negative below the unique positive root \(u=1+\sqrt5\), and positive above it. Solving \(r+r^{-1}=1+\sqrt5\) for \(r>1\) yields exactly \(R_*\). At equality, both endpoint quadratics have the same positive root; by affinity every intermediate coupling shares it. Strict inequality in \(Q_p(s)<1\) excludes the ceiling.

Finally, the minimum over all \(s>0\) of \(Q_{\mathrm{same}}\) is the stated value, reached at the stated squared step. If \(u=r+r^{-1}\ge4\), then \(Q_{\mathrm{anti}}(s)>1\) for every positive \(s\), so it cannot be faster. If \(2<u<4\), minimizing the antithetic quadratic gives
\[
\min_{s>0}Q_{\mathrm{anti}}(s)=1-\frac{(4-u)^2}{16},
\qquad
\min_{s>0}Q_{\mathrm{same}}(s)=1-\frac{u^2}{8(u^2-2)}.
\]
The difference between their improvements over one is
\[
\frac{u^2}{8(u^2-2)}-\frac{(4-u)^2}{16}
=\frac{(u-2)^2(8+4u-u^2)}{16(u^2-2)}>0
\quad (2<u<4).
\]
For any \(s\), no convex combination of the two factors beats their smaller value; hence minimization jointly over coupling and stepsize reduces to the minima of the two endpoint quadratics. Strictness proves global uniqueness. For \((a,b)=(1,2)\), direct substitution at \(s=1/3\) yields the three rational witness multipliers, with independent-stage sampling corresponding to \(p=1/2\). This completes the proof.

## Verification

Run `python3 verify.py` with Python 3 standard library. It checks the exact polynomial identities, all four deterministic stage-pair updates for rational test parameters, the complete coupling-mixture formula, the sharp stability-ceiling factorization, the optimal-rate formula, and the stated divergence/contraction witness. Recorded output is included in `verification_output.txt`. The analytic factorization and inequality arguments above, not the finite test census, establish the universal quantifiers.

## Relationship to prior work

Mishchenko et al. introduced and analyzed same-sample stochastic extragradient, motivated by its contrast to independent predictor/corrector sampling. Li et al. studied the resulting bilinear game dynamics and convergence rates, while Gorbunov et al. developed arbitrary-sampling frameworks for same-sample and independent-sample variants. Chae et al. analyzed shuffling across successive updates, not arbitrary dependence **between the two oracle calls within each update**. These papers motivate the question but, in the inspected formulations and results, neither optimize the full joint law with fixed uniform marginals nor establish the antithetic maximum-stepsize reversal and ratio threshold \(R_*\). The familiar same-sample special-case multiplier alone is not asserted to be new. No literature search establishes absolute novelty, and further specialist overlap is possible.

## Limitations

This is an exact two-component, scalar bilinear, iid-iteration, equal-stage-stepsize result with no additive oracle noise. It does not imply antithetic coupling is preferable for the fastest rate (it is not), nor does it apply automatically to more components, nonlinear fields, general matrix games, varying marginal sampling laws, temporally dependent couplings, or alternative extragradient schemes. All assertions are mean-square, not unconditional pathwise statements. Source comparisons are research-level and have not undergone independent expert audit.

## References

1. K. Mishchenko, D. Kovalev, E. Shulgin, P. Richtárik and Y. Malitsky, *Revisiting Stochastic Extragradient*, arXiv:1905.11373, first publicly posted 2019-05-27; AISTATS 2020. https://proceedings.mlr.press/v108/mishchenko20a.html
2. C. J. Li, Y. Yu, N. Loizou, G. Gidel, Y. Ma, N. Le Roux and M. I. Jordan, *On the Convergence of Stochastic Extragradient for Bilinear Games using Restarted Iteration Averaging*, arXiv:2107.00464, first posted 2021-06-30; AISTATS 2022. https://proceedings.mlr.press/v151/junchi-li22a.html
3. E. Gorbunov, H. Berard, G. Gidel and N. Loizou, *Stochastic Extragradient: General Analysis and Improved Rates*, arXiv:2111.08611, first posted 2021-11-16; AISTATS 2022. https://proceedings.mlr.press/v151/gorbunov22b.html
4. J. Chae, C. Yun and D. Kim, *Stochastic Extragradient with Flip-Flop Shuffling & Anchoring: Provable Improvements*, NeurIPS 2024. https://proceedings.neurips.cc/paper_files/paper/2024/hash/df658fe5097f65485ad80b06e6cb30dd-Abstract-Conference.html
