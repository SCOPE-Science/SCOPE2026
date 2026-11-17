# Sharp robustness radius for heterogeneous cyclic two-tap averaging

## Finding
Let \(n\ge4\), \(0<\theta<1\), and \(\mu=\min\{\theta,1-\theta\}\). On cyclic real vectors, set
\[
(P_{\boldsymbol a}f)_i=(1-a_i)f_i+a_i f_{i+1\pmod n},
\qquad
G(f)=\sum_{0\le i<j<n}|f_i-f_j|.
\]
For every \(0\le\varepsilon\le\mu/(n-2)\), every coefficient vector with \(|a_i-\theta|\le\varepsilon\), and every real vector \(f\), the **sharp uniform defect inequality** is
\[
\boxed{\ G(f)-G(P_{\boldsymbol a}f)\ \ge\ 2[\mu-(n-2)\varepsilon]\,[\max_i f_i-\min_i f_i].\ }
\]
The coefficient on the right cannot be increased uniformly over admissible coefficients and signals. Consequently, the **exact uniform \(\ell^\infty\) parameter-perturbation radius for Gini nonexpansivity** about homogeneous cyclic two-tap averaging is
\[
\boxed{\ \varepsilon_\ast=\frac{\min\{\theta,1-\theta\}}{n-2}.\ }
\]
More precisely, if \(\varepsilon_\ast<\varepsilon\le\mu\), some admissible \(\boldsymbol a\) and real \(f\) satisfy \(G(P_{\boldsymbol a}f)>G(f)\). Thus a single step has strict Gini contraction for every nonconstant input at every perturbation size below the critical radius, nonexpansivity at the radius, and possible amplification immediately above it. Here the parameter cube is restricted to \(0\le\varepsilon\le\mu\) so all coefficients lie in \([0,1]\); the same critical radius applies to larger clipped cubes.

## Assumptions and scope
The indices \(i\) are taken modulo \(n\), and the transition matrix is row stochastic. The coefficient \(a_i\) is allowed to vary independently by site. The oscillation is \(\operatorname{osc}(f)=\max_i f_i-\min_i f_i\). The result is uniform over all real inputs, not only binary inputs, and includes \(\varepsilon=0\) and \(\varepsilon=\varepsilon_\ast\). The endpoints \(\theta=0,1\) are excluded because they give a degenerate zero-radius neighborhood, and cycles of length at most three are excluded because every row-stochastic map there contracts this Gini seminorm.

## Proof
**1. Binary cuts and runs.** Let \(S\) be a nonempty proper cyclic subset, \(k=|S|\), and let \(r\ge1\) be the number of cyclic runs of \(S\). There are \(r\) exit sites \(E=\{i\in S:i+1\notin S\}\) and \(r\) entry sites \(F=\{i\notin S:i+1\in S\}\); necessarily \(r\le\min\{k,n-k\}\). For the constant vector \(\boldsymbol a=(\theta,\dots,\theta)\), the values of \(P_{\boldsymbol a}\mathbf1_S\) are \(1\) on \(k-r\) sites, \(0\) on \(n-k-r\) sites, \(1-\theta\) on \(E\), and \(\theta\) on \(F\). Summing all cross-class and boundary-pair distances gives the exact identity
\[
G(P_{\theta\mathbf1}\mathbf1_S)
=k(n-k)-r^2[1-|1-2\theta|]
=k(n-k)-2\mu r^2. \tag{1}
\]
This count makes no assumption about the relative lengths of the runs.

**2. A uniform perturbation estimate.** Write \(a_i=\theta+\delta_i\), with \(|\delta_i|\le\varepsilon\). Only the \(2r\) boundary outputs change. The exit outputs are \(1-\theta-\delta_i\), and entry outputs are \(\theta+\delta_j\). The pairs touching one boundary point and one unchanged point contribute exactly
\[
(2k-n)\left(\sum_{i\in E}\delta_i-\sum_{j\in F}\delta_j\right)
\]
to the change in Gini variation. The remaining pair contributions (exit–exit, entry–entry and exit–entry) are bounded above by
\[
\sum_{i<i'\in E}|\delta_i-\delta_{i'}|
+\sum_{j<j'\in F}|\delta_j-\delta_{j'}|
+\sum_{i\in E,j\in F}|\delta_i+\delta_j|. \tag{2}
\]
The bound for the last sum is the reverse triangle inequality applied to the pair \(1-\theta-\delta_i\), \(\theta+\delta_j\). The resulting upper bound is convex separately in every \(\delta_i\), hence takes its maximum over the parameter cube at a vertex \(\delta_i\in\{-\varepsilon,+\varepsilon\}\).

Suppose \(t\) of the \(r\) exit perturbations and \(u\) of the \(r\) entry perturbations equal \(+\varepsilon\). Put \(d=t-u\), so \(|d|\le r\). The right side of (2), including the linear term, is then exactly
\[
2\varepsilon\left[(2k-n)d+t(r-t)+u(r-u)+tu+(r-t)(r-u)\right]
=2\varepsilon\,[r^2+(2k-n)d-d^2]. \tag{3}
\]
For every feasible integer quadruple \((n,k,r,d)\) with \(n\ge4\), \(1\le k<n\), \(1\le r\le\min\{k,n-k\}\), \(|d|\le r\), one has
\[
r^2+(2k-n)d-d^2\le r^2(n-2). \tag{4}
\]
Indeed, when \(r=1\), \(d=-1,0,1\) gives values among \(1,\pm(2k-n)\), all at most \(n-2\). When \(r\ge2\), use \(|2k-n|\le n-2r\) to bound the left side by \(r^2+r(n-2r)=r(n-r)\le r^2(n-2)\). Thus (1)–(4) imply for each cut
\[
G(P_{\boldsymbol a}\mathbf1_S)\le k(n-k)-2r^2[\mu-(n-2)\varepsilon]. \tag{5}
\]

**3. All real signals.** For a nonconstant real \(f\), let \(m=\min_i f_i\), \(M=\max_i f_i\), and \(S_t=\{i:f_i>t\}\). Since \(P_{\boldsymbol a}\mathbf1=\mathbf1\), the layer-cake identity \(f=m\mathbf1+\int_m^M\mathbf1_{S_t}\,dt\), linearity and the triangle inequality imply
\[
G(P_{\boldsymbol a}f)\le\int_m^M G(P_{\boldsymbol a}\mathbf1_{S_t})\,dt.
\]
Likewise, \(G(f)=\int_m^M|S_t|(n-|S_t|)\,dt\). For almost every \(t\in(m,M)\), \(S_t\) is a nontrivial cut with at least one run. If \(\mu-(n-2)\varepsilon\ge0\), (5) gives
\[
G(P_{\boldsymbol a}f)\le G(f)-2[\mu-(n-2)\varepsilon](M-m),
\]
as claimed. Constants satisfy the inequality with equality.

**4. Sharpness, failure above the radius and boundary.** Fix a site \(s\) and choose \(f=\mathbf1_{\{s\}}\). Select \(a_s=\theta-\varepsilon\), \(a_{s-1}=\theta+\varepsilon\), and arbitrary admissible coefficients elsewhere. Then \(P_{\boldsymbol a}f\) has exactly two nonzero values, \(1-\theta+\varepsilon\) at \(s\) and \(\theta+\varepsilon\) at \(s-1\). Consequently,
\[
G(P_{\boldsymbol a}f)=(n-2)(1+2\varepsilon)+|1-2\theta|,
\quad G(f)=n-1,
\]
so
\[
G(f)-G(P_{\boldsymbol a}f)=2[\mu-(n-2)\varepsilon]. \tag{6}
\]
For \(0\le\varepsilon\le\varepsilon_\ast\), (6) attains the defect coefficient in the theorem. For every \(\varepsilon_\ast<\varepsilon\le\mu\), (6) is negative and gives the announced amplifying witness. For larger clipped uncertainty cubes, choose an admissible inner \(\varepsilon\) strictly between \(\varepsilon_\ast\) and \(\mu\).

## Verification
The supplied standalone `check_weighted_cyclic_robustness.py` uses only Python's standard library and checks all nontrivial binary cuts and all endpoint parameter environments in dimension \(4\le n\le7\), at \(\theta\in\{1/4,1/2,3/4\}\), both at the critical radius and at \(5/4\) times that radius. It also checks (4) for all admissible integer parameters with \(4\le n\le199\), using exact integer arithmetic. It reports 127,680 exact cut-environment tests and 34,324,941 inequality instances. The infinite-dimensional quantifiers over \(n\) and all real coefficients and signals follow from the proof, not from these finite checks.

## Relationship to prior work
Classical Dobrushin/Hopf oscillation contraction theory provides contraction formulas for stochastic matrices in the oscillation seminorm and its dual total-variation norm. These are not the unweighted complete-pair Gini seminorm of the output signal. Earlier homogeneous two-tap cut-deficit calculations establish the special case \(a_i=\theta\), but do not imply the sharp independently perturbed coefficient cube, its dimension-dependent threshold or the minimax oscillation defect (6). The general perturbation literature on time-inhomogeneous finite-state Markov kernels uses total-variation or Wasserstein-type metrics for distributions; its estimates do not yield this sharp Gini radius. The present statement is a one-step, signal-seminorm assertion and not a general Markov-chain mixing theorem.

## Limitations
The exact radius concerns a homogeneous center with independent entrywise \(\ell^\infty\) perturbations of two-tap probabilities, finite directed cycles of length at least four, and complete-pair Gini variation. It does not classify the entire nonexpansivity polytope of arbitrary spatially varying coefficients, give the sharp operator norm outside the stability cube, or analyze products of different kernels. Historical priority has been investigated against accessible literature and research records, but cannot be established by search alone; unindexed equivalent estimates remain a possibility. No independent mathematical audit is claimed.

## References
1. S. Gaubert and Z. Qu, *Dobrushin ergodicity coefficient for Markov operators on cones, and beyond*, arXiv:1302.5226, first posted 2013-02-21, https://arxiv.org/abs/1302.5226.
2. S. Gaubert and Z. Qu, *Dobrushin's ergodicity coefficient for Markov operators on cones*, arXiv:1307.4649, first posted 2013-07-17, https://arxiv.org/abs/1307.4649.
3. L. Truquet, *Local stationarity and time-inhomogeneous Markov chains*, arXiv:1610.01290, first posted 2016-10-05, https://arxiv.org/abs/1610.01290.
