# An exact two-sided large-deviation law for transient means in a globally attracting replicator map

## Finding

Let \(0<a\leq4\), \(0<b<1\), and \(p,q>0\). Consider the deterministic replicator map
\[
f_{a,b}(x)=\frac{x}{x+(1-x)\exp(a(x-b))},\qquad 0<x<1.
\]
Sample only the starting point, \(X_0\sim\operatorname{Beta}(p,q)\), and thereafter evolve deterministically by \(X_{j+1}=f_{a,b}(X_j)\). Write \(A_n=n^{-1}\sum_{j=0}^{n-1}X_j\). The probability laws of \(A_n\) obey a full large-deviation principle of speed \(n\) on \(\mathbb R\), with the good rate function
\[
I(y)=\begin{cases}
ap(b-y),&0\le y\le b,\\
aq(y-b),&b\le y\le1,\\
+\infty,&y\notin[0,1].
\end{cases}
\]
Thus, for every closed \(C\subset\mathbb R\) and every open \(G\subset\mathbb R\),
\[
\limsup_{n\to\infty}\frac1n\log\Pr(A_n\in C)\le-\inf_{y\in C}I(y),\qquad
\liminf_{n\to\infty}\frac1n\log\Pr(A_n\in G)\ge-\inf_{y\in G}I(y).
\]
The limiting scaled log-moment-generating function exists for every real \(t\) and equals
\[
\Lambda(t):=\lim_{n\to\infty}\frac1n\log\mathbb E\exp(tnA_n)
=\begin{cases}
-apb,&t<-ap,\\
bt,&-ap\le t\le aq,\\
t-aq(1-b),&t>aq.
\end{cases}
\]
The tilted pressure has two genuine slope jumps, at \(t=-ap\) and \(t=aq\). Although every interior deterministic trajectory converges to the same fixed point \(b\), exponentially atypical initial conditions near either repelling endpoint keep finite-time empirical means away from \(b\) for a macroscopic fraction of their observation horizon. The asymmetric slopes are determined exactly by the two endpoint exponents of the initial law.

## Assumptions and scope

The map and parameters above are fixed as \(n\to\infty\); the randomness is exclusively in \(X_0\), not in the updates. The Beta density is \(x^{p-1}(1-x)^{q-1}/B(p,q)\) on \((0,1)\). We include the monotonicity boundary \(a=4\), at which the map has an isolated zero derivative, but exclude \(a>4\), where the map may have folding and chaotic invariant sets. All logarithms are natural. The LDP includes its endpoint values \(y=0,1\): these describe exponentially rare initial conditions, not positive probability of exactly starting at either endpoint. \(\operatorname{Beta}(1,1)\) is the uniform-prior special case.

## Proof

**1. Order preservation and a globally attracting interior point.** Let \(h(x)=\log((1-x)/x)\), with inverse \(\ell(u)=(1+e^u)^{-1}\). The conjugated map is
\[
g(u):=h(f_{a,b}(\ell(u)))=u+a(\ell(u)-b).
\]
Since
\[
g'(u)=1-a\ell(u)(1-\ell(u))\ge1-a/4\ge0,
\]
\(g\) is strictly increasing (for \(a=4\) the derivative vanishes at only one point). Its unique fixed point is \(u_*=h(b)\), and \(g(u)<u\) for \(u>u_*\), while \(g(u)>u\) for \(u<u_*\). As \(g\) is increasing, the entire orbit of any finite \(u\) stays between its initial value and \(u_*\) and converges monotonically to \(u_*\). Equivalently, all interior \(x\)-orbits converge to \(b\).

**2. Exact finite-horizon coboundary and a scaling map.** For any \(x_0\in(0,1)\), write \(u_j=h(f^j(x_0))\). Telescoping the exact identity \(u_{j+1}-u_j=a(x_j-b)\) gives
\[
\frac1n\sum_{j=0}^{n-1}x_j=b+\frac{u_n-u_0}{an}.
\]
For each real \(r\), choose an \(n\)-dependent initial point \(x_{0,n}=\ell(anr)\) and define
\[
P_n(r)=\frac{g^n(anr)}{an},\qquad F_n(r)=b+P_n(r)-r.
\]
The latter is precisely the empirical mean \(A_n\) for this initial point.

**3. Scaled deterministic orbit law.** We prove pointwise convergence
\[
P_n(r)\longrightarrow P(r)=
\begin{cases}
\min(r+1-b,0),&r\le0,\\
\max(r-b,0),&r\ge0.
\end{cases}
\]
For \(r>0\), the starting coordinate \(anr\) exceeds \(u_*\) for all large \(n\), so the iterates decrease towards \(u_*\). Each decrement lies in \([-ab,0]\), proving \(P_n(r)\ge\max(r-b,0)+o(1)\). Fix \(\varepsilon\in(0,b)\) and a threshold \(K>\max(u_*,0)\) with \(\ell(K)<\varepsilon\). While the orbit remains above \(K\), each decrement is at least \(a(b-\varepsilon)\). If it stays above \(K\) for all \(n\) steps, then \(P_n(r)\le r-b+\varepsilon\). Otherwise, monotonicity traps its remaining iterates below \(K\), hence \(P_n(r)\le K/(an)\). Thus \(\limsup P_n(r)\le\max(r-b+\varepsilon,0)\), and \(\varepsilon\downarrow0\) proves the positive half.

For \(r<0\), the orbit increases toward \(u_*\). Each increment lies in \([0,a(1-b)]\). Fix \(\varepsilon\in(0,1-b)\) and \(K>0\) with \(-K<u_*\) and \(\ell(-K)>1-\varepsilon\). While the orbit is below \(-K\), its increment is at least \(a(1-b-\varepsilon)\); after crossing, it is trapped between \(-K\) and \(u_*\). Exactly the analogous lower and upper bounds yield \(P_n(r)\to\min(r+1-b,0)\). At \(r=0\), the starting coordinate is independent of \(n\) and its orbit remains bounded, yielding \(P_n(0)\to0\). Since each \(g^n\) is increasing, so is each \(P_n\). The pointwise limit \(P\) is continuous. By the elementary monotone-function convergence lemma (partition each compact interval so that the continuous limit changes by at most a prescribed \(\varepsilon\), then sandwich between its finitely many partition values), \(P_n\to P\) uniformly on each compact interval. Consequently
\[
F_n(r)\xrightarrow[\mathrm{locally\ uniformly}]{} F(r)=b+P(r)-r
=\max\{0,\min\{1,b-r\}\}.
\]

**4. Initial-data large deviations.** Put \(R_n=h(X_0)/(an)\). A change of variables from the Beta density yields the exact density
\[
\rho_n(r)=\frac{an}{B(p,q)}\frac{\exp(aqnr)}{(1+\exp(anr))^{p+q}}.
\]
Its exponential scale is \(\rho_n(r)=\exp[-nJ(r)+o(n)]\) locally uniformly, with
\[
J(r)=a\bigl(p\max(r,0)+q\max(-r,0)\bigr).
\]
Indeed, the identity \(\log(1+e^v)=\max(v,0)+\log(1+e^{-|v|})\) bounds the error in its log-density by a constant plus \(\log(an/B(p,q))\), uniformly in \(r\). The elementary interval integral bounds therefore prove the LDP lower bound on open intervals and upper bound on compact intervals. The exact exponential tails, \(\Pr(R_n>K)\le C e^{-apnK}\) and \(\Pr(R_n<-K)\le C e^{-aqnK}\) for positive \(K\) (enlarging \(C\) independently of \(n\)), provide exponential tightness and extend the upper bound to all closed sets. Hence \(R_n\) has a good speed-\(n\) LDP with rate \(J\).

**5. Contraction and the exact rate.** We have the identity in law \(A_n=F_n(R_n)\). For any \(\delta>0\) and \(K>0\), local uniform convergence implies \(|F_n(R_n)-F(R_n)|<\delta\) on \(|R_n|\le K\) for sufficiently large \(n\). Since the exponential rate of \(\Pr(|R_n|>K)\) can be made arbitrarily negative by taking \(K\to\infty\), these two random quantities are exponentially equivalent. The contraction principle gives the rate \(I(y)=\inf\{J(r):F(r)=y\}\). For \(0<y<1\), the unique preimage is \(r=b-y\), and the expression above follows. At \(y=0\), the preimage is \([b,\infty)\), with infimum \(apb\). At \(y=1\), it is \(( -\infty,b-1]\), with infimum \(aq(1-b)\). No other values are attained. This proves the full LDP, including the endpoint rates.

**6. Tilted pressure.** Because \(A_n\in[0,1]\), the bounded continuous version of Varadhan's lemma applies for every \(t\in\mathbb R\):
\[
\Lambda(t)=\sup_{0\le y\le1}(ty-I(y)).
\]
The objective is affine on each of \([0,b]\) and \([b,1]\), with slopes \(t+ap\) and \(t-aq\), respectively. Evaluating at their endpoints gives the three stated branches, including continuity at the transition parameters. Since \(b\in(0,1)\), both slope changes are strict. This completes the proof.

## Verification

The standalone \(`checker.py`\) confirms the finite-step coboundary to floating-point tolerance, compares rescaled transient trajectories with their limiting clipped profile for multiple \(a,b,r,n\) choices (including \(a=4\)), and independently maximizes \(ty-I(y)\) on a fine grid against the proposed piecewise log-moment-generating function for three distinct Beta priors. Run \(`python3 checker.py`\) in a standard Python 3 environment; it requires no third-party packages. The 93 finite sanity checks passed. These finite tests do not substitute for the proof of the infinite LDP or its boundaries.

## Relationship to prior work

Chotibut–Falniowski–Misiurewicz–Piliouras prove the globally Cesàro-attracting mean \(b\) for all interior orbits and explicitly derive the telescoping exponent underlying the coboundary. Kryzhevich–Zhang develop the statistical-invariant/coboundary framework and describe the related chaotic regime. Those facts are premises, not new claims. The present result instead takes a fixed nondegenerate random initial distribution and resolves the *entire exponentially small finite-horizon empirical-mean law* and its two tilted-pressure transitions. General large-deviation theory for nonuniformly expanding maps and topologically exact systems concerns substantially different hyperbolicity and invariant-statistical mechanisms; it does not directly furnish this particular Beta-prior formula for an order-preserving attracting system. The topic of deterministic transient survival under randomized initial data is also distinct from the exact observable and rate calculated here.

## Limitations

This is a deterministic initial-condition large-deviation principle, not a stochastic-noise process or an invariant-measure large-deviation principle. The shape parameters \(p,q\) are fixed as \(n\to\infty\). The formula is not asserted for \(a>4\), a compactly supported prior away from the repelling endpoints, or heavy-tailed priors in logit coordinates. The pressure limit establishes no finite-\(n\) prefactor or uniform \(t\)-dependent asymptotic. Comparison with inaccessible or unindexed historical research remains a publication-priority risk, and there has been no independent mathematical audit.

## References

1. S. Kryzhevich and Y. Zhang, *Shift maps and statistical invariants for some dynamical systems*, arXiv:2603.20685, first posted March 21, 2026. https://arxiv.org/abs/2603.20685
2. T. Chotibut, F. Falniowski, M. Misiurewicz and G. Piliouras, *Family of chaotic maps from game theory*, arXiv:1807.06831, first posted July 18, 2018, especially Section 3.1. https://arxiv.org/html/1807.06831v1
3. V. Araújo and M. J. Pacifico, *Large deviations for non-uniformly expanding maps*, arXiv:math/0601449. https://arxiv.org/abs/math/0601449
4. F. Hellmann et al., *Survivability of deterministic dynamical systems*, Scientific Reports 6 (2016), 29654. https://www.nature.com/articles/srep29654
