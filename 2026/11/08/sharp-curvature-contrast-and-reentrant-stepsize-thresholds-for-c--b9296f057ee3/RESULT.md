# Sharp curvature-contrast and reentrant-stepsize thresholds for cyclic heavy-ball

## Finding

Consider the two-component scalar finite-sum problem with losses \(f_1(x)=a x^2/2\) and \(f_2(x)=b x^2/2\), where \(0<a<b\). Apply classical heavy-ball momentum with constant \(0\leq\beta<1\) and stepsize \(\eta>0\), alternating the exact component gradients in the order \(a,b,a,b,\ldots\):
\[
x_{k+1}=x_k-\eta a_k x_k+\beta(x_k-x_{k-1}),\qquad a_{2j}=a,\quad a_{2j+1}=b.
\]
Put \(r=b/a>1\), \(z=\eta a\), \(c=1+\beta\) and \(d=1-\beta\). Restrict to the full common *frozen-component stability interval* \(0<z<2c/r\): within this interval, heavy-ball with either single component gradient held fixed converges to zero for every initial state.

**Exact two-step classification.** For \(0<\beta<1\), alternating heavy-ball is asymptotically stable for every initial pair exactly when
\[
H_{\beta,r}(z):=(c-z)(c-rz)+d^2>0.
\]
It has an exponentially growing solution exactly when \(H_{\beta,r}(z)<0\). At \(H_{\beta,r}(z)=0\), the two-step multipliers are \(-1\) and \(-\beta^2\): the iteration is bounded but does not decay for generic initial data.

**Optimal curvature-contrast barrier.** Define \(\beta_\star=2-\sqrt3\) and \(\delta=(1-\beta)/(1+\beta)\). For every \(0<\beta<1\), there exists a stepsize within the common frozen-component stability interval producing exponential instability if and only if \(r>R(\beta)\), where
\[
R(\beta)=\begin{cases}
\dfrac{(1+\beta)^2}{2\beta},&0<\beta\leq 2-\sqrt3,\\[4pt]
\bigl(\sqrt{1+\delta^2}+\delta\bigr)^2,&2-\sqrt3<\beta<1.
\end{cases}
\]
For \(r<R(\beta)\), every stepsize in the stated interval is asymptotically stable. At \(r=R(\beta)\), all such stepsizes remain asymptotically stable if \(\beta\leq\beta_\star\); if \(\beta>\beta_\star\), exactly one interior stepsize has a neutral multiplier \(-1\), and all others are asymptotically stable. At zero momentum, \(\beta=0\), no alternating instability can occur within the common frozen-component stability interval, regardless of curvature ratio.

**Sharp disconnected-stability classification.** Let \(R_2(\beta)=(1+\beta)^2/(2\beta)\). The admissible stepsize interval has *two nonempty separated open regions of asymptotic stability, with an open interval of instability between them*, if and only if
\[
\beta>2-\sqrt3,\qquad R(\beta)<r<R_2(\beta).
\]
In that case the two neutral stepsizes correspond to
\[
z_\pm=\frac{c(r+1)\pm\sqrt{c^2(r-1)^2-4rd^2}}{2r},
\]
so the stable set is precisely \((0,z_-)\cup(z_+,2c/r)\) and the unstable set is \((z_-,z_+)\). For other parameter regimes, no such disconnected pair of stable open intervals occurs.

For instance, \(a=1\), \(b=2\), \(\beta=1/2\) yields frozen-component stability for \(0<\eta<3/2\) but alternating stability only for \(0<\eta<1\) or \(5/4<\eta<3/2\); the two boundary stepsizes are neutral. At \(\eta=9/8\), the two-step eigenvalues are \((-41\pm3\sqrt{73})/64\), one smaller than \(-1\), even from the conventional initialization \(x_{-1}=x_0=1\). The Cesàro average of the iterates is also unbounded along some subsequence for that initialization.

## Assumptions and scope

The sample losses are scalar, smooth, globally strongly convex quadratics sharing minimizer zero. Sampling is deterministic, strictly two-periodic, and uses one exact component gradient per step; there is no additive noise. The momentum \(\beta\) and stepsize \(\eta\) are constant. Stability means convergence of \((x_k,x_{k-1})\to(0,0)\) for every initial pair; exponential instability means at least one initial pair produces a component growing exponentially along the even subsequence. All results are for the strict frozen-component stability window; its endpoint is excluded. The classification does not cover arbitrary schedules, nonlinear losses, time-varying momentum or minibatch sampling with independent draws.

## Proof

**1. Matrix reduction.** Define the state \(u_k=(x_k,x_{k-1})^\top\) and the single-step matrix \(A(t)=\begin{psmallmatrix}c-t&-\beta\\1&0\end{psmallmatrix}\). Then \(u_{2j}=P^j u_0\) for every integer \(j\geq0\) with \(P=A(rz)A(z)\). Multiplication gives
\[
\operatorname{tr}P=(c-z)(c-rz)-2\beta,\qquad\det P=\beta^2.
\]
The same two-step spectrum results if the two component orders are reversed, since \(A(z)\) and \(A(rz)\) have positive determinant when \(\beta>0\).

**2. Exact Schur test.** For \(0<\beta<1\), a real monic quadratic \(\lambda^2-T\lambda+\beta^2\) has both roots strictly in the unit disk if and only if \(\beta^2<1\) and \(1\pm T+\beta^2>0\). Within \(0<z<2c/r\), both numbers \(c-z\) and \(c-rz\) lie strictly between \(-c\) and \(c\). Thus
\[
1+\beta^2-\operatorname{tr}P=c^2-(c-z)(c-rz)>0,
\]
while
\[
1+\beta^2+\operatorname{tr}P=H_{\beta,r}(z).
\]
If the latter is zero, the characteristic polynomial factors as \((\lambda+1)(\lambda+\beta^2)\). If it is negative, the characteristic polynomial is negative at \(\lambda=-1\) but positive at negative infinity, proving the existence of a real multiplier less than \(-1\). For \(\beta=0\), the one-step maps collapse to scalar gradient-descent multipliers, whose two-step product has modulus less than one within the common frozen interval.

**3. Optimization over permissible stepsizes.** Expand
\[
H_{\beta,r}(z)=rz^2-c(r+1)z+c^2+d^2.
\]
Its convex vertex is \(z_v=c(r+1)/(2r)\). This lies below the admissible ceiling \(z_c=2c/r\) precisely when \(r<3\). Consequently, for \(1<r\leq3\), the minimum or infimum equals \(d^2-c^2(r-1)^2/(4r)\), while for \(r\geq3\), the infimum (at the excluded endpoint) equals \(d^2+c^2(2/r-1)\). The first becomes negative exactly when \(r>(\sqrt{1+\delta^2}+\delta)^2\); the second becomes negative exactly when \(r>2/(1-\delta^2)=(1+\beta)^2/(2\beta)\). Both transitions meet at \(r=3\) precisely when \(\delta=1/\sqrt3\), equivalently \(\beta=2-\sqrt3\). This proves the piecewise sharp contrast law, including the distinct endpoint equality cases.

**4. Reentrant-stability criterion.** The convex quadratic \(H\) is positive at \(z=0\). It has a negative interior interval exactly when the contrast barrier is crossed. Both of its positive roots lie below \(z_c\) precisely when the endpoint value
\[
H_{\beta,r}(z_c)=c^2\left(\frac2r-1+\delta^2\right)
\]
is strictly positive and the vertex is interior. The endpoint inequality is \(r<R_2(\beta)\). For \(\beta\leq2-\sqrt3\), the necessary instability contrast already satisfies \(r\geq R_2(\beta)\), so reentrance is impossible. For \(\beta>2-\sqrt3\), the two positive roots lie in the admissible domain precisely when \(R(\beta)<r<R_2(\beta)\). The quadratic formula gives their displayed values and proves necessity, sufficiency and all strict boundaries.

**5. Exact example and averaging.** At \(a=1\), \(b=2\), \(\beta=1/2\), the Schur condition reduces to \(H=(\eta-1)(2\eta-5/2)>0\), giving exactly the two stable intervals above. At \(\eta=9/8\),
\[
P=\begin{pmatrix}-25/32&3/8\\3/8&-1/2\end{pmatrix},
\qquad \operatorname{spec}(P)=\left\{\frac{-41-3\sqrt{73}}{64},\frac{-41+3\sqrt{73}}{64}\right\}.
\]
The initial vector \((1,1)^\top\) is not an eigenvector of this symmetric matrix, so it has a nonzero projection on the unstable eigenvector and the resulting scalar position sequence grows exponentially on an even or odd subsequence. If its Cesàro averages were all bounded, its partial sums would be \(O(k)\), so each position \(x_k\), being the difference of consecutive partial sums, would also be \(O(k)\). This contradicts exponential growth; therefore those averages are unbounded along a subsequence.

## Verification

The accompanying `verify_heavyball.py` reconstructs the transition matrices symbolically with exact SymPy arithmetic, verifies trace, determinant, Jury identities, example eigenvalues and several exact-rational boundary checks. It also evaluates 10,000 deterministic-seeded parameter samples, a 70-case grid and 135 checks of the reentrant-region classification. Running `python verify_heavyball.py` with Python 3 and SymPy reproduces `verification_output.txt`. The universal results are certified by the symbolic proof above, not by numerical sampling, grids or logs.

## Relationship to prior work

Classical heavy-ball stability for a *fixed* Hessian and the frozen two-step characteristic equation appear, for example, in Sun et al. (2018), Danilova and Malinovsky (2021), and Orvieto (2023). The cyclic multiblock method of Sun et al. updates different coordinate blocks of one fixed objective; it does not alternate different scalar sample curvatures for one common coordinate. Bollapragada, Chen and Ward (2022) study independently sampled minibatch momentum and sufficient batch-size guarantees, not the deterministic two-sample Floquet boundary. Pasechnyuk-Vilensky (2026) studies nonlinear trajectories for one fixed smooth strongly convex objective, not time-alternating gradient oracles from two different component objectives. The classical Schur/Jury test supplies the algebraic criterion, but does not itself provide the optimized contrast barrier or the complete reentrant-stepsize region. Searches against related available mathematical findings and primary literature did not identify an exact statement implying these two parameter thresholds; this is a bounded originality assessment, not a claim of exhaustive historical novelty.

## Limitations

The result does not claim divergence under independent random sampling, arbitrary curvature schedules, general smooth nonquadratic losses, or all initial states in the unstable region (a stable eigendirection persists). At neutral boundaries there is no exponential growth, but convergence fails for generic initial states. Averaging is proved insufficient only for the explicit exponentially unstable example, not for all parameter choices. An unindexed period-two damped-oscillator or incremental-gradient study could contain an equivalent parameter law; independent expert assessment remains to be performed.

## References

1. T. Sun, P. Yin, D. Li, C. Huang, L. Guan, and H. Jiang, *Non-ergodic Convergence Analysis of Heavy-Ball Algorithms*, arXiv:1811.01777, initial public submission 2018-11-05. https://arxiv.org/abs/1811.01777
2. M. Danilova and G. Malinovsky, *Averaged Heavy-Ball Method*, arXiv:2111.05430, initial public submission 2021-11-09. https://arxiv.org/abs/2111.05430
3. R. Bollapragada, T. Chen, and R. Ward, *On the fast convergence of minibatch heavy ball momentum*, arXiv:2206.07553, initial public submission 2022-06-15. https://arxiv.org/abs/2206.07553
4. A. Orvieto, *An Accelerated Lyapunov Function for Polyak's Heavy-Ball on Convex Quadratics*, arXiv:2301.05799, initial public submission 2023-01-14. https://arxiv.org/abs/2301.05799
5. D. Pasechnyuk-Vilensky, *Two Answers on Heavy-Ball Dynamics*, arXiv:2610.09912, initial public submission 2026-10-07. https://arxiv.org/abs/2610.09912
