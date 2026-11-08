# Exact tristability window in a three-agent sigmoidal opinion network

## Finding

Consider one persuadable agent connected to two fixed zealots of opinions \(-1\) and \(+1\). Under the continuous-time sigmoidal bounded-confidence rule of Brooks, Chodrow, and Porter, fix the sigmoid steepness at \(\gamma=1\), and vary the nonnegative squared-distance receptiveness parameter \(\delta\). Define
\[
Q(x)=e^{x^2}\left(\frac{\sinh(2x)}{x}-\cosh(2x)\right),\qquad 0<x\leq1,\qquad Q(0)=1.
\]
There is exactly one \(m\in(0,1)\) satisfying
\[
2m(1-m^2)=\tanh(2m).
\]
Define the sharp threshold \(\delta_*=1+\log Q(m)\), with numerical values \(m\approx0.457314620422500\) and \(\delta_*\approx1.037743156221737\). The exact equilibrium and attraction classification for all \(\delta\geq0\) is:

1. If \(0\leq\delta\leq1\), there are precisely three equilibria \(0,\pm u\), where \(u\in(m,1)\) uniquely solves \(Q(u)=e^{\delta-1}\). The equilibria \(\pm u\) attract all strictly positive and strictly negative initial opinions, respectively; \(0\) repels. At \(\delta=1\), the repulsion of \(0\) is nonhyperbolic.
2. If \(1<\delta<\delta_*\), there are precisely five equilibria \(0,\pm a,\pm b\), where \(0<a<m<b<1\) uniquely solve \(Q(a)=Q(b)=e^{\delta-1}\). The equilibria \(0,\pm b\) are asymptotically stable, whereas \(\pm a\) are unstable and delimit their basins: \((-a,a)\) is attracted to \(0\), \((a,\infty)\) to \(b\), and \(( -\infty,-a)\) to \(-b\).
3. If \(\delta=\delta_*\), the only equilibria are \(0,\pm m\). The origin attracts \((-m,m)\), and \(\pm m\) are semistable: trajectories exterior to these thresholds approach the corresponding nonzero equilibrium, while interior trajectories approach \(0\).
4. If \(\delta>\delta_*\), \(0\) is the unique equilibrium and attracts every initial opinion in \(\mathbb R\).

Consequently the smallest connected network with two opposing zealots and a persuadable node already has an exactly determined interval of *three simultaneously attracting opinions*, bounded by a neutral-state stability change at \(\delta=1\) and a pair of nonzero saddle-node collisions at \(\delta=\delta_*\). This establishes an exact hysteresis window rather than merely a local linear-instability criterion.

## Assumptions and scope

The graph is the unweighted three-vertex path. The leaves are fixed at \(-1\) and \(+1\); the center opinion \(x(t)\) is arbitrary real initially. The update is the original smooth, normalized influence rule, without self-interactions:
\[
\dot x=F_\delta(x)=\frac{(1-x)W_\delta(1-x)-(1+x)W_\delta(1+x)}{W_\delta(1-x)+W_\delta(1+x)},\qquad W_\delta(s)=\frac{1}{1+\exp(s^2-\delta)}.
\]
Only \(\gamma=1\) is asserted; other steepness values and larger network topologies are not classified. All claims concern deterministic continuous time and the exact logistic kernel above.

## Proof

**Step 1: invariant interval and reduction.** Both weights are positive, so the right-hand side is a convex combination of the zealot opinions minus \(x\). In particular, for \(x>1\) it is negative and for \(x<-1\) it is positive, with inward-pointing flow at \(\pm1\). Smoothness and at-most-linear growth give a global unique solution. Every solution starting outside \([-1,1]\) enters it in finite time because \(F_\delta(\pm1)\ne0\). The field is odd: \(F_\delta(-x)=-F_\delta(x)\).

Put \(A_\delta(x)=1+\exp((1-x)^2-\delta)\) and \(B_\delta(x)=1+\exp((1+x)^2-\delta)\). Clearing the positive denominators yields, for \(x>0\),
\[
F_\delta(x)=\frac{(1-x)B_\delta(x)-(1+x)A_\delta(x)}{A_\delta(x)+B_\delta(x)}
=\frac{2x\bigl(e^{1-\delta}Q(x)-1\bigr)}{A_\delta(x)+B_\delta(x)}.
\]
Thus every positive equilibrium lies in \((0,1)\) and satisfies precisely \(Q(x)=e^{\delta-1}\). No positive equilibrium can lie beyond \(1\), by the inward-pointing field.

**Step 2: one maximum, proved globally.** Direct differentiation gives
\[
Q'(x)=\frac{e^{x^2}\cosh(2x)}{x^2}\,H(x),\qquad H(x)=2x(1-x^2)-\tanh(2x),
\]
and
\[
H'(x)=2\bigl(\tanh^2(2x)-3x^2\bigr).
\]
The function \(x\mapsto\tanh(2x)/x\) strictly decreases on \((0,1]\), from \(2\) to \(\tanh2\). Indeed, its derivative has numerator \(2x\operatorname{sech}^2(2x)-\tanh(2x)<0\), equivalent to \(\sinh(4x)>4x\). Hence \(H'\) changes sign exactly once, from positive to negative, where \(\tanh(2x)/x=\sqrt3\). Since \(H(0)=0\), \(H\) is initially positive; since \(H(1)=-\tanh2<0\), it crosses zero at exactly one point \(m\in(0,1)\). Therefore \(Q\) is strictly increasing on \((0,m)\) and strictly decreasing on \((m,1)\). Its endpoints satisfy \(Q(0)=1\) and \(Q(1)=-e^{-1}\), so \(Q(m)>1\). The threshold \(\delta_*\) is well defined and exceeds \(1\).

**Step 3: exact equilibrium census.** Compare the horizontal level \(e^{\delta-1}\) with the increasing and decreasing branches of \(Q\). A positive level up to \(1\) meets only the decreasing branch, giving one positive root when \(\delta\leq1\). A level strictly between \(1\) and \(Q(m)\) meets both branches, giving two. At \(Q(m)\) they coincide at the unique maximum, and above \(Q(m)\) there are none. Odd symmetry supplies all negative roots; \(x=0\) is always a root. This proves all counts, including the double-root boundary.

**Step 4: stability, basins, and boundary cases.** The sign of \(F_\delta(x)\) for \(x>0\) is the sign of \(Q(x)-e^{\delta-1}\). Thus at a simple positive root the sign of the derivative of the vector field is the sign of \(Q'\): the smaller root on the increasing branch is repelling, and the larger root on the decreasing branch is attracting. At the origin,
\[
F_\delta'(0)=\frac{e^{1-\delta}-1}{e^{1-\delta}+1},
\]
which is positive for \(\delta<1\) and negative for \(\delta>1\). At \(\delta=1\), direct Taylor expansion gives \(Q(x)=1+x^2/3+O(x^4)\) and \(F_1(x)=x^3/6+O(x^5)\), so the origin still repels. At \(\delta=\delta_*\), \(Q(x)<Q(m)\) for \(x>0\), \(x\ne m\), and hence the nonzero roots attract only from the exterior side. The monotonicity intervals and uniqueness of one-dimensional ODE solutions imply all stated basins and limits for arbitrary real initial opinions.

The small separating equilibrium in the tristable window additionally satisfies \(a\sim\sqrt{3(\delta-1)}\) as \(\delta\downarrow1\), exhibiting the basin boundary's square-root emergence. The nonzero roots coalesce at \(m\) with the standard square-root saddle-node scaling because \(Q''(m)<0\), proved by the strictly negative value of \(H'(m)\).

## Verification

The included `verify.py` evaluates the defining formulas independently with high-precision standard-library arithmetic, bisects the unique maximum, checks the reported numerical brackets and root ordering, compares the normalized vector field with the reduced sign expression, and checks sample signs and local expansions in all parameter regimes. It is a computational cross-check, not the proof of the infinite-quantifier statements; those follow from Steps 1–4.

## Relationship to prior work

Brooks, Chodrow, and Porter introduced this sigmoidally smoothed bounded-confidence flow, proved local stability criteria for the harmonic state on paths and balanced-exposure graphs, and numerically displayed multistability for larger path and community networks. Their Theorem 5 implies the center's local stability boundary at \(\gamma=1\), but neither that criterion nor the reported larger-network numerical pictures determines this three-agent model's complete equilibrium count, the exact nonlinear threshold \(\delta_*\), or all basins. The present proof provides this exact smallest-network global classification without claiming that multistability or sigmoid models were newly discovered.

The related nonlinear-consensus framework of Homs-Dones, Devriendt, and Lambiotte concerns an unnormalized edge-coupling flow rather than this normalized two-zealot sigmoid equation. The tunable-sensitivity model of Bizyaeva, Franci, and Leonard employs saturating opinion updates, not the same state-dependent logistic edge weights. General one-dimensional bifurcation theory explains the type of collision after it is located but does not imply the global uniqueness or numerical location of \(\delta_*\) for this kernel.

## Limitations

The model's binary zealot opinions, its three-node topology, equal edge weights, and fixed steepness \(\gamma=1\) are essential to the statement. The result proves neither that the same window survives arbitrary asymmetric zealots nor that the number of steady states remains five on larger graphs. The decimals are approximations to implicitly defined exact constants, not a closed elementary expression. Similar exact classifications may exist in unindexed literature; no independent external audit is asserted.

## References

1. H. Z. Brooks, P. S. Chodrow, and M. A. Porter, *Emergence of polarization in a sigmoidal bounded-confidence model of opinion dynamics*, arXiv:2209.07004, first public release 2022-09-15; SIAM Journal on Applied Dynamical Systems **23** (2024), 1442–1470, DOI:10.1137/22M1527258. https://arxiv.org/abs/2209.07004 ; https://doi.org/10.1137/22M1527258 .
2. M. Homs-Dones, K. Devriendt, and R. Lambiotte, *Nonlinear consensus on networks: equilibria, effective resistance and trees of motifs*, SIAM Journal on Applied Dynamical Systems **20** (2021), 1544–1570, DOI:10.1137/20M1376844. https://arxiv.org/abs/2008.12022 .
3. A. Bizyaeva, A. Franci, and N. E. Leonard, *Nonlinear opinion dynamics with tunable sensitivity*, IEEE Transactions on Automatic Control **68** (2023), 1415–1430, DOI:10.1109/TAC.2022.3159527. https://arxiv.org/abs/2009.04332 .
