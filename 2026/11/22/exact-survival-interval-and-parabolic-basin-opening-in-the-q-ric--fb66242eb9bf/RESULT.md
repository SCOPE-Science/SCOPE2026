# Exact survival interval and parabolic basin opening in the q-Ricker map

## Finding

For the q-deformed Ricker population map
\[
R_{\varepsilon}(x)=\frac{\lambda x e^{-\beta x}}{1+\varepsilon(1-\lambda x e^{-\beta x})},\qquad x\geq0,
\]
introduce the population coordinate \(t=\beta x\) and parameters
\[
\alpha=\frac{\lambda}{1+\varepsilon},\qquad k=\frac{\varepsilon\lambda}{\beta(1+\varepsilon)}.
\]
Then \(t_{n+1}=G_{\alpha,k}(t_n)\), where
\[
G_{\alpha,k}(t)=\frac{\alpha t e^{-t}}{1-kte^{-t}}.
\]
For every \(1<k<e\) and \(0<\alpha<\min\{1,e-k\}\), set
\[
c=\log k,\quad \alpha_c=k(1-\log k),\quad
b_c=-W_{-1}(-c e^{-c})>1,
\]
where \(W_0,W_{-1}\) are the real Lambert \(W\) branches. The following is an exact classification for **every** initial \(t_0\geq0\), not merely for initial populations in a prescribed compact interval.

**Below the fold:** If \(\alpha<\alpha_c\), every orbit converges exponentially to zero.

**At the fold:** If \(\alpha=\alpha_c\), precisely the initial interval \([c,b_c]\) converges to the positive nonhyperbolic fixed point \(c\); every initial state outside this interval converges to zero. For every \(c<t_0<b_c\),
\[
\lim_{n\to\infty}n(t_n-c)=\frac{2(1-c)}c.
\]
The two boundary states \(c,b_c\) land on (or remain at) \(c\) in at most one step, so the displayed positive asymptotic is intentionally not asserted at either endpoint.

**Above the fold:** If \(\alpha_c<\alpha<\min\{1,e-k\}\), there are exactly two positive equilibria \(0<t_-<c<t_+<1\), explicitly
\[
t_-=-W_0\left(-\frac{e^{-\alpha/k}}k\right)-\frac\alpha k,\qquad
t_+=-W_{-1}\left(-\frac{e^{-\alpha/k}}k\right)-\frac\alpha k.
\]
Let \(b=-W_{-1}(-t_- e^{-t_-})>1\). Every \(t_0\in(t_-,b)\) converges to the attracting equilibrium \(t_+\); the two boundary states \(t_-,b\) converge to the repelling equilibrium \(t_-\); all remaining initial states converge to zero. The exact length of the positive-attractor basin, including its fold onset, is
\[
b-t_-=(b_c-c)+\frac{b_c-c}{c(b_c-1)}\sqrt{\frac{2(\alpha-\alpha_c)}k}+O_k(\alpha-\alpha_c).
\]
In particular the nonextinction basin length jumps from zero below the fold to \(b_c-c>0\) at the fold, followed by a square-root expansion immediately above it.

There are no periodic orbits of period greater than one in the stated sector. Every invariant Borel probability is a convex combination of the Dirac probabilities at its fixed points (one, two, or three fixed points depending on the regime).

## Assumptions and scope

The natural physical parameters are \(\lambda,\beta,\varepsilon>0\); the theorem is the nonempty open sector expressed by \(1<k<e\) and \(0<\alpha<\min\{1,e-k\}\), plus the interior fold surface. Conversely every such \((\alpha,k)\) can be realized by physical positive parameters: choose any \(\varepsilon>0\), put \(\lambda=\alpha(1+\varepsilon)\) and \(\beta=\varepsilon\alpha/k\). Fixed \(k\) is held constant in the fold expansions. All intervals are in the normalized coordinate \(t=\beta x\); in original population units, divide their endpoints and lengths by \(\beta\). There is no uniform convergence-speed assertion over all initial states in an open basin.

## Proof

**(1) Global trapping.** For all \(t\geq0\), \(0\leq te^{-t}\leq e^{-1}\), hence \(1-kte^{-t}>1-k/e>0\). Direct differentiation gives
\[
G'_{\alpha,k}(t)=\frac{\alpha e^{-t}(1-t)}{(1-kte^{-t})^2}.
\]
Thus \(G\) increases up to \(t=1\) and decreases afterward; its global range is \([0,\alpha/(e-k)]\subset[0,1)\). Every forward orbit therefore enters \([0,1)\) after one step, on which \(G\) is strictly increasing. A strictly increasing interval map cannot have a nonconstant periodic orbit: if a first step moves up, all subsequent steps move up, and likewise if it moves down. Bounded monotone iterates converge to fixed points.

**(2) Fixed-point threshold.** For \(t>0\) define
\[
h(t)=\frac{G(t)}t=\frac{\alpha e^{-t}}{1-kte^{-t}},\quad
h'(t)=\frac{\alpha e^{-t}(k e^{-t}-1)}{(1-kte^{-t})^2}.
\]
Consequently \(h\) rises until \(c=\log k\), then falls, with \(h(0)=\alpha<1\), \(h(1)=\alpha/(e-k)<1\), and \(h(c)=\alpha/\alpha_c\). The inequalities \(0<\alpha_c<\min\{1,e-k\}\) follow from \(1<k<e\) by elementary differentiation. Therefore the positive fixed-point count is zero, one double, or two according as \(\alpha<\alpha_c\), \(\alpha=\alpha_c\), or \(\alpha>\alpha_c\). The fixed-point equation is \(e^t=\alpha+kt\); shifting \(t\) by \(\alpha/k\) gives the stated real Lambert-\(W\) expressions. The lower root is on the increasing branch of \(h\), so \(G'(t_-)>1\); the upper root is on the decreasing branch of \(h\), so \(0<G'(t_+)<1\). At the fold the derivative equals one.

**(3) All initial-data basins.** When \(\alpha<\alpha_c\), \(h(t)\leq\alpha/\alpha_c<1\), giving uniform geometric extinction. At the fold, \(h(t)<1\) off \(c\). On \([0,1]\), monotonicity of \(G\) implies that points below \(c\) decrease toward zero, and points strictly above \(c\) decrease toward \(c\). Because \(G(1)>G(c)=c\), and \(G\) strictly decreases from \(G(1)\) to zero on \((1,\infty)\), the equation \(G(b_c)=c\) has exactly one second solution \(b_c>1\). Since \(G(b_c)=G(c)\), cancelling the positive common factors in \(G(t)\) gives \(b_ce^{-b_c}=ce^{-c}\), yielding the stated \(W_{-1}\) formula and the exact global basin \([c,b_c]\).

Above the fold, on \([0,1]\), the sign of \(G(t)-t\) is respectively negative, positive, negative on \((0,t_-)\), \((t_-,t_+)\), \((t_+,1]\). Monotone iteration then converges to zero below \(t_-\) and to \(t_+\) above it; \(t_-\) stays fixed. Since \(G(1)>G(t_+)=t_+>t_-\), the decreasing branch has exactly one other preimage \(b>1\) of \(t_-\), characterized by \(be^{-b}=t_-e^{-t_-}\). Values of \(t_0>1\) map above, equal to, or below \(t_-\) exactly when \(t_0<b\), \(t_0=b\), or \(t_0>b\). This proves all the stated basins.

**(4) Parabolic rate.** At \(\alpha=\alpha_c\), exact differentiation and \(e^c=k\) give
\[
G(c)=c,\quad G'(c)=1,\quad G''(c)=-\frac{c}{1-c}<0.
\]
Every nonstationary orbit in \((c,b_c)\) eventually has positive displacement \(u_n=t_n-c\downarrow0\). Taylor's theorem gives
\[
u_{n+1}=u_n-\frac{c}{2(1-c)}u_n^2+O(u_n^3).
\]
It follows that \(1/u_{n+1}-1/u_n\to c/[2(1-c)]\); Cesàro summation yields \(n u_n\to2(1-c)/c\). No endpoint is included in this asymptotic.

**(5) Square-root basin opening.** The fold equation \(\alpha=e^t-kt\) has second derivative \(k>0\) at \(t=c\), hence for \(\delta=\alpha-\alpha_c>0\)
\[
t_-=c-\sqrt{2\delta/k}+O_k(\delta).
\]
For \(b(t)>1\) defined by \(b(t)e^{-b(t)}=te^{-t}\), implicit differentiation gives \(b'(t)=-b(t)(1-t)/[t(b(t)-1)]\). At \(t=c\), subtracting \(t_-=c-\sqrt{2\delta/k}+O(\delta)\) from \(b(t_-)\) yields exactly the claimed coefficient, since \(1-b'(c)=(b_c-c)/[c(b_c-1)]\). The error is \(O_k(\delta)\) by analyticity away from \(t=1\).

**(6) Invariant measures.** Every orbit converges to one of the listed fixed points. If \(\mu\) is invariant, then for each bounded continuous observable \(\varphi\), invariance and dominated convergence imply \(\int\varphi\,d\mu=\int\varphi(\lim_nG^n(t))\,d\mu(t)\). Thus \(\mu\) is the pushforward under the limiting fixed-point selector, supported entirely on the finite fixed-point set. Conversely each convex mixture of its point masses is invariant.

## Verification

The included standalone script `verify.py` uses Python's standard library. Execute `python3 verify.py`. It checks the normalized formula, a concrete admissible \(k=3/2\) parameter slice, all three predicted basin types, exact fixed/preimage identities numerically, critical inverse-time relaxation, and square-root basin opening. Its finite diagnostics are supplemental; the all-parameter and infinite-time assertions are supplied by the proof above. For an independent symbolic check one may differentiate the displayed rational-exponential formula three times; no proprietary solver or external table is needed.

## Relationship to prior work

Aishwaraya, Gupta and Chandramouli introduced this specific rationally deformed Ricker map and analyzed its Lambert-\(W\) equilibria, local fold/flip boundaries, coexistence, extinction and numerically observed chaotic regimes. Those model facts and fixed-point fold formulas are prior work, **not new claims here**. A full published thesis chapter of the originating research (available in the institutional repository) was inspected through its fixed-point, fold, coexistence and bifurcation sections. The added results concern an explicit global trapping sector, an exact basin for *every nonnegative initial population* including upper-density extinction, a universal parabolic time law, the square-root length correction of the full survival interval, and classification of all invariant measures in that sector. Standard monotone interval-map facts are used, not claimed as new. Related earlier Allee-type Ricker work and published calculations for a cubic Allee population map give similar qualitative pictures for different recurrences; these statements do not directly establish the displayed q-Ricker thresholds or rate coefficient.

## Limitations

The theorem does not classify parameters outside \(1<k<e\), \(0<\alpha<\min\{1,e-k\}\). The universal \(1/n\) relaxation holds only on the nonstationary positive side of the fold. The fold's jump in basin **length** is not automatically a jump in every probability of persistence unless an initial distribution is specified. The original article's full publisher PDF could not be retrieved; the originating authors' substantially overlapping thesis chapter was read instead, and the specific novelty comparison remains subject to publication-priority uncertainty. Other literature may establish equivalent results under a general unimodal basin theorem or a different parametrization. No independent mathematical audit has been performed.

## References

1. Aishwaraya, D. Gupta, and V. V. M. S. Chandramouli, *Dynamics of q deformed Ricker map*, Journal of Difference Equations and Applications 28 (2022), 1423–1448, published online 11 November 2022. DOI: https://doi.org/10.1080/10236198.2022.2142468.
2. Aishwaraya, *Dynamics of the Homographic Ricker-like maps*, doctoral thesis (2024), Chapter 2, full text: https://ir-api.iitj.ac.in/ir/api/core/bitstreams/a0082d15-cdb9-406c-9494-10b5131cf0a6/content.
3. Y. Yang and R. J. Sacker, *Periodic unimodal Allee maps, the semigroup property and the lambda-Ricker map with Allee effect*, Discrete and Continuous Dynamical Systems - B 19 (2014), 589–606. https://doi.org/10.3934/dcdsb.2014.19.589.
