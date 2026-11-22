# Sharp mixing boundary for global homogeneity in sigmoid threshold networks

## Finding

For every integer \(N\ge2\), every nonnegative row-stochastic \(N\)-by-\(N\) matrix \(W\), every \(\beta>0\), and every \(h\in\mathbb R\), consider the sigmoid response flow
\[
\dot x_i=-x_i+\sigma\bigl(h+\beta(Wx)_i\bigr),\qquad
\sigma(z)=(1+e^{-z})^{-1},\qquad x(0)\in[0,1]^N.
\]
Let its row-overlap deficit (Dobrushin coefficient) be
\[
\delta(W)=\frac12\max_{i,j}\sum_{k=1}^N|w_{ik}-w_{jk}|\in[0,1],
\]
and let \(D(x)=\max_i x_i-\min_i x_i\).

**Global homogeneous selection:** If \(\beta\delta(W)\le4\), every trajectory converges to a homogeneous equilibrium \(s\mathbf1\), with \(s=\sigma(h+\beta s)\), and no nonhomogeneous equilibrium or recurrent orbit exists. In the strict regime \(\beta\delta(W)<4\), the explicit uniform estimate holds for every \(t\ge0\):
\[
D(x(t))\le D(x(0))\exp\bigl[-(1-\beta\delta(W)/4)t\bigr].
\]
The endpoint \(\beta\delta(W)=4\) is included for convergence, but not for a positive uniform exponential rate.

**Sharpness within the same model:** For the two-site symmetric stochastic matrix
\[
W_\delta=\frac12\begin{pmatrix}1+\delta&1-\delta\\1-\delta&1+\delta\end{pmatrix},\quad 0<\delta\le1,
\]
set \(h=-\beta/2\). Nonhomogeneous equilibria on the invariant line \(x_1+x_2=1\) exist if and only if \(\beta\delta>4\): they are exactly the two points \((1/2\pm z_*,1/2\mp z_*)\), with \(z_*\in(0,1/2)\) the unique positive solution of
\[
z_*=\tfrac12\tanh(\beta\delta z_*/2).
\]
For \(\beta=8\) and \(\delta=3/4\), both such nonhomogeneous equilibria are asymptotically stable; the off-diagonal network weights are strictly positive. Exactly at \(\beta\delta=4\), every nonzero antisymmetric trajectory with \(x_1(0)+x_2(0)=1\) obeys the sharp critical law
\[
\lim_{t\to\infty}t\bigl(x_1(t)-x_2(t)\bigr)^2=\frac32.
\]
Thus the coefficient-four boundary is optimal as a universal exclusion threshold for heterogeneous equilibria in the two-site family, and the loss of exponential mixing has an explicit algebraic critical signature.

## Assumptions and scope

The system is deterministic and autonomous. The same strictly increasing logistic distribution function is used at every node; the external field \(h\) and social-feedback strength \(\beta\) are shared. All entries of \(W\) are nonnegative and all row sums equal one; irreducibility, symmetry, and diagonal positivity are not assumed for the global theorem. Solutions start in the full cube \([0,1]^N\). The two-site sharpness statements use the additional displayed symmetry and stimulus conditions only.

The linear contraction condition \(\beta<4\) from a global Lipschitz argument is sufficient for a *unique* equilibrium on every network. The new condition \(\beta\delta(W)\le4\) instead ensures *homogeneity of all asymptotic states* and allows multiple distinct homogeneous equilibria when \(\beta>4\). It is therefore not a uniqueness claim. For example, \(\beta=8\), \(h=-4\), and \(W=(1-\gamma)\mathbf1\mathbf1^T/N+\gamma I\), with \(0\le\gamma<1/2\), have \(\delta(W)=\gamma\), global homogenization, and exactly three scalar equilibria (two sinks and a middle unstable equilibrium).

## Proof

**(1) Invariance and overlap.** At \(x_i=0\) the vector field component is positive and at \(x_i=1\) it is negative. Thus the cube is forward invariant, and smoothness plus compactness ensures global forward solutions. For arbitrary \(x\in[0,1]^N\), put \(m=\min_i x_i\), \(M=\max_i x_i\). Since two stochastic rows have difference summing to zero, splitting their positive and negative differences gives
\[
\bigl|(Wx)_i-(Wx)_j\bigr|
\le\frac{M-m}{2}\sum_k|w_{ik}-w_{jk}|
\le\delta(W)D(x).
\]
The logistic derivative is \(\sigma'(z)=\sigma(z)(1-\sigma(z))\le1/4\), with equality only at \(z=0\). Consequently its secant slope across any nondegenerate interval is *strictly* below \(1/4\).

**(2) Diameter dissipation.** At a right-differentiability time of the maximum/minimum, select an index \(i\) attaining the maximum and \(j\) attaining the minimum that realize the one-sided diameter derivative. Then
\[
D^+D(x(t))\le -D(x(t))+
\frac\beta4\bigl|(Wx(t))_i-(Wx(t))_j\bigr|
\le -(1-\beta\delta(W)/4)D(x(t)).
\]
The same inequality holds at ties by the upper-right Dini derivative formula. For \(\beta\delta(W)<4\), Gronwall's inequality gives the claimed exponential bound. For \(\beta\delta(W)=4\), whenever \(D(x)>0\), the first inequality is strict after using the logistic *strict* secant inequality if the two row inputs differ, and equals \(-D(x)<0\) if they agree. This gives \(D^+D(x)<0\) at every nonhomogeneous state. Compactness of the cube and upper-semicontinuity of the finite maximum of the active-pair derivatives give a uniform negative upper bound for \(D^+D\) on \(\{x:D(x)\ge\epsilon\}\), for each \(\epsilon>0\). Since \(D(t)\) is nonincreasing, its limit cannot be positive; hence \(D(t)\to0\) also at equality.

**(3) Convergence of the common level.** Let \(a(t)=N^{-1}\sum_i x_i(t)\) and \(g(a)=-a+\sigma(h+\beta a)\). Because every \((Wx)_i\) lies between the current minimum and maximum,
\[
\dot a(t)=g(a(t))+r(t),\qquad |r(t)|\le\tfrac\beta4D(x(t))\to0.
\]
The real-analytic function \(g\) is not identically zero (indeed \(g(0)>0\) and \(g(1)<0\)), so it has finitely many zeros on \([0,1]\). A bounded scalar solution of \(\dot a=g(a)+r(t)\), where \(r(t)\to0\) and \(g\) has only finitely many zeros, converges to a zero: otherwise its distinct liminf and limsup would force infinitely many crossings in both directions through an interval on which \(g\) has one strict sign, impossible for sufficiently small \(r\). Once a limit exists, it must be a zero since a nonzero limiting drift contradicts convergence. Hence \(a(t)\to s\) with \(g(s)=0\). Since \(D(t)\to0\), all coordinates tend to \(s\). In particular every recurrent state is a homogeneous fixed point.

**(4) Sharp two-site onset.** On the line \(x_1=1/2+z\), \(x_2=1/2-z\) with \(h=-\beta/2\), the two-site dynamics reduce *exactly* to
\[
\dot z=-z+\tfrac12\tanh(\beta\delta z/2).
\]
The function \(\tanh v/v\) strictly decreases from one to zero on \((0,\infty)\), so the reduced field has two nonzero zeros precisely if \(\beta\delta>4\), one positive and one negative. Their uniqueness on this line follows from the same monotonicity.

At such a nonzero equilibrium, \(\sigma'(\pm\beta\delta z_*)=1/4-z_*^2\). Its full two-dimensional Jacobian equals \(-I+\beta(1/4-z_*^2)W_\delta\), with eigenvalues
\[
-1+\beta(1/4-z_*^2),\qquad -1+\beta\delta(1/4-z_*^2).
\]
For \(\beta=8\), \(\delta=3/4\), the positive root solves \(z_*=(1/2)\tanh(3z_*)\) and satisfies \(z_*>2/5\), since \(\tanh(6/5)>4/5\) is equivalent to \(e^{12/5}>9\), proved by the first five positive terms of its exponential series. Therefore \(1/4-z_*^2<9/100\), making both eigenvalues smaller than \(-7/25\). The two heterogeneous equilibria are strict local sinks.

**(5) Exact endpoint relaxation.** When \(\beta\delta=4\), the reduced two-site equation is \(\dot z=-z+(1/2)\tanh(2z)\). Every initial \(0<|z(0)|<1/2\) retains its sign and tends monotonically to zero since \(\tanh v<v\) for \(v>0\). Its Taylor expansion is
\[
\dot z=-\tfrac43z^3+O(z^5),\qquad
\frac d{dt}(z^{-2})=\tfrac83+O(z^2).
\]
It follows that \(z(t)^{-2}/t\to8/3\), hence \(t(2z(t))^2\to3/2\), as claimed.

## Verification

The independent, standard-library-only script `verify.py` checks 900 finite row-overlap inequalities for random stochastic matrices and states, verifies a stable nonhomogeneous two-site equilibrium and its two negative Jacobian multipliers, tests four strongly mixing three-node examples in the scalar-bistable regime, and evaluates the critical contrast law along the exactly invariant antisymmetric line. Run from a directory containing the script with `python3 verify.py`.

The program is a finite diagnostic, not a proof of the quantified statements. Analytic steps (1)--(5), especially the strict endpoint dissipation and the scalar convergence argument, establish the infinite assertions.

## Relationship to prior work

Boudourides, *Collective Hysteresis and Multistability in Threshold Networks* (arXiv:2609.10580v1, September 5, 2026), introduced the row-stochastic threshold-network model and established weak-feedback contraction, preservation of the homogeneous cusp, weak-coupling multistability, and two-block heterogeneous cusp scaling. The present result addresses the complementary regime of *strong feedback combined with strongly overlapping rows*: a graph-explicit criterion rules out all heterogeneous long-time states, while retaining possible scalar hysteresis. It additionally determines a closed, sharp two-site onset criterion and exact inverse-time critical contrast.

Kaye's 2026 scalar dawn-chorus model supplies the one-dimensional bistable threshold mechanism, but not a finite weighted-network mixing cutoff. Gaubert and Qu's Dobrushin theory supplies the classical row-overlap coefficient and contraction framework; those tools are explicitly credited rather than presented as new. Their nonlinear consensus models preserve translation along the homogeneous direction, unlike this saturating logistic-feedback flow. The model-specific global selection and two-site critical classification are the claims assessed here. The accessible literature comparison is not a claim of definitive historical priority.

## Limitations

The general bound is sufficient, not necessary, for every fixed network. Sharpness is established as a *universal threshold* by a two-node family; it does not assert that all networks with \(\beta\delta>4\) have nonhomogeneous equilibria. The inverse-time coefficient applies to an exactly invariant antisymmetric line; for \(\beta>4\) the central homogeneous equilibrium may be unstable transversely. The result does not address heterogeneous external fields, time-dependent links, noise, or non-sigmoid response distributions. Independent verification and a definitive historical-priority determination have not been performed.

## References

1. M. Boudourides, *Collective Hysteresis and Multistability in Threshold Networks*, arXiv:2609.10580v1 (first submitted September 5, 2026), https://arxiv.org/abs/2609.10580.
2. A. R. Kaye, *From individual thresholds to collective hysteresis: a mechanistic model of the dawn chorus*, Journal of the Royal Society Interface 23 (2026), article 20260267, https://doi.org/10.1098/rsif.2026.0267.
3. S. Gaubert and Z. Qu, *Dobrushin ergodicity coefficient for Markov operators on cones, and beyond*, arXiv:1302.5226 (2013), https://arxiv.org/abs/1302.5226.
