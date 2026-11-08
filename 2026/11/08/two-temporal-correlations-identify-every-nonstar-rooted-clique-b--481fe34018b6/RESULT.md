# Two temporal correlations identify every nonstar rooted clique bouquet

## Finding

Let \(F_{m,s}=K_1\vee(mK_s)\) be the graph consisting of \(m\) disjoint cliques with \(s\) vertices each, together with one vertex adjacent to every clique vertex. All integers \(m,s\ge1\) are allowed, and the distinguished observation vertex is the universal hub. Thus \(s=1\) gives centered stars; \(m=1\) gives complete graphs; and \(s=2\) gives friendship graphs.

**Theorem.** Fix a *known* \(\varepsilon\in(0,1)\). Under synchronous independent fair-refresh noisy voting on \(F_{m,s}\), the joint limiting lag-one and lag-two endpoint repetition frequencies distinguish every two distinct rooted graphs in this family, except that all centered stars are indistinguishable by these frequencies (indeed, their entire rooted observation processes are indistinguishable). More specifically, write the observed hub spin as \(Z_t\in\{-1,1\}\), let \(c=1-\varepsilon\), \(q=c^2\), and set

\[
r_d=\lim_{T\to\infty}\frac1T\sum_{t=1}^T Z_t Z_{t+d},\qquad d\in\{1,2\}.
\]

These limits exist almost surely, from every initial state. For \(s=1\), \((r_1,r_2)=(0,q)\) for every \(m\). For \(s\ge2\), put \(u=r_1/c\). Then

\[
r_2=q\left(\frac1s+\frac{s-1}{s}u\right),\qquad
s=\frac{1-u}{r_2/q-u}.
\]

Define

\[
 v=\frac{q(s-1)(1+2u)}{s^2-q(s^2-3s+3)},\qquad
 w=\frac{q[1+2(s-1)u]}{s^2-q(s-1)^2}.
\]

The number of clique blades is recovered exactly by

\[
 m=\frac{q(s-1)[1+(s-1)v-sw]}{s^2u-qsu-qs(s-1)w}.
\]

Every displayed denominator is positive. For each fixed \(s\ge2\), \(r_1\) decreases strictly as \(m\) increases. In the usual zero-one opinion convention, the empirical lag-\(d\) repetition frequency tends almost surely to \((1+r_d)/2\); thus both reconstruction inputs are observable from the one hub.

## Assumptions and scope

The graph is finite, simple, undirected and unweighted. Its universal hub is observed. Every vertex simultaneously updates at every integer time, independently of other vertices; it refreshes to an unbiased random sign with probability \(\varepsilon\), otherwise copies a uniformly random neighbor from the preceding time. The same known noise probability is used when comparing graphs. The claim is for all finite integers \(m,s\ge1\), without assumptions that the observer sees other vertices. It does not apply to asynchronous one-vertex-at-a-time updates, nor to unknown or different noise parameters.

## Proof

**1. Stationary pair equations.** Because every vertex has a positive chance of refreshing to either sign, every state of the finite configuration space communicates with every other state in one step, and the chain has a unique stationary distribution. It is ergodic from every initial law. Global sign-flip symmetry gives mean-zero spins. Let \(u\) be the stationary product expectation between the hub and an outer vertex, \(v\) between two distinct vertices of the same clique blade, and \(w\) between vertices in different blades. For \(m=1\), the last pair orbit is absent; the equation below may nevertheless define an auxiliary \(w\), which does not affect the hub equation because its coefficient is zero.

Write \(q=(1-\varepsilon)^2\). For any pair of *distinct* vertices, both must copy to retain a nonzero product expectation. Conditional on both copying, coincident chosen ancestors contribute one, while distinct ancestors contribute the stationary correlation of their orbit. Counting possible ancestors gives

\[
\begin{aligned}
 u&=q\left[\frac{u}{s}+\frac{s-1}{ms^2}
       +\frac{(s-1)^2}{ms^2}v
       +\frac{(m-1)(s-1)}{ms}w\right],\\
 v&=q\left[\frac{s-1}{s^2}+\frac{2(s-1)}{s^2}u
       +\frac{s^2-3s+3}{s^2}v\right],\\
 w&=q\left[\frac1{s^2}+\frac{2(s-1)}{s^2}u
       +\frac{(s-1)^2}{s^2}w\right].
\end{aligned}
\]

The second and third equations yield exactly the displayed formulas for \(v=v(u)\) and \(w=w(u)\). Both are increasing affine functions on \([0,1]\) and have values strictly below one because \(0<q<1\). The equations form a contraction: each nonconstant row-sum of the underlying pair transition kernel is at most \(q<1\), hence the stationary solution is unique. If \(s\ge2\), the hub equation has a strictly positive constant term \(q(s-1)/(ms^2)\), so \(0<u<1\). For \(s=1\), the hub and leaf are in opposite bipartition classes under synchronous copying, their equal-time product correlation is zero, and the hub two-step ancestor is necessarily the hub.

**2. Temporal observations.** Conditional on the configuration at time \(t\), the hub's next spin has conditional mean \(c\) times the mean spin of its outer neighbors. Thus \(r_1=cu\). A backward two-step ancestry from the hub returns to the hub with probability \(1/s\); otherwise it arrives at a uniformly distributed outer vertex, whose stationary correlation with the hub is \(u\). Both updates must copy, so \(r_2=q[1/s+(s-1)u/s]\). Since \(u<1\), solving this equation for \(s\) gives \(s=(1-u)/(r_2/q-u)\), with \(r_2/q-u=(1-u)/s>0\). The identical argument for \(s=1\) yields \((r_1,r_2)=(0,q)\).

**3. Strict blade-number recovery.** Let

\[
D_v=s^2-q(s^2-3s+3),\qquad D_w=s^2-q(s-1)^2.
\]

Both are strictly positive. Direct subtraction yields the exact identity

\[
v-w=\frac{q(s-2)\{s^2-q[s^2-2s+2+2(s-1)u]\}}{D_vD_w}\ge0.
\]

Indeed, the expression in braces is at least \(s^2(1-q)>0\) because \(u\le1\). Also \(w<1\), hence \(H(u)=1+(s-1)v(u)-sw(u)=1-w(u)+(s-1)[v(u)-w(u)]>0\).

After substitution into the first pair equation, the hub correlation is the unique fixed point in \([0,1]\) of

\[
F_m(u)=q\left[\frac us+\frac{s-1}{s}w(u)
 +\frac{s-1}{ms^2}H(u)\right].
\]

This map is increasing, affine, and contractive. To see contractivity directly, in the original hub equation its coefficients for \(u,v,w\) are nonnegative and have sum at most one; the slopes of \(v(u),w(u)\) lie in \([0,1)\), and the whole expression is multiplied by \(q<1\). If \(m_1<m_2\), then \(F_{m_1}(u)>F_{m_2}(u)\) at every \(u\in[0,1]\), since \(H(u)>0\). Comparing their unique fixed points proves \(u(m_1,s)>u(m_2,s)\). Rearranging the same fixed-point equation gives the displayed formula for \(m\); its denominator equals \(q(s-1)H(u)/m>0\). Therefore the two observed correlations determine \(s\) and then \(m\) uniquely.

**4. Almost-sure empirical convergence.** The finite-state chain has a strictly positive one-step transition matrix, so its stationary ergodic theorem applies to each bounded function of finitely many consecutive states, in particular \(Z_tZ_{t+1}\) and \(Z_tZ_{t+2}\). Their empirical averages converge almost surely to \(r_1,r_2\), from any initial law. This finishes the theorem.

## Verification

The attached standard-library script `verify.py` constructs each finite graph explicitly, solves the stationary two-walker correlation system by exact rational Gaussian elimination and, independently, solves the three-orbit reduction. It also calculates lag-one and lag-two temporal correlations from one- and two-step transition kernels, applies both inverse formulas, and checks the strict blade-number order. Its test grid consists of three rational copying probabilities, clique sizes two through four and blade counts one through three, together with centered-star checks: 33 exact parameter cases, all passed. The executable proves no infinite quantified assertion; those follow from the inequalities and fixed-point argument above. Run `python verify.py` in the directory containing this document.

## Relationship to prior work

Benjamini, Helman Tov and Zhukovskii introduced the local-observation identifiability problem for *this synchronous model* and proved pairwise identification for complete graphs, cycles and certain perfect trees; their Section 6 treats complete bipartite graphs and the nonidentifiability of centered stars. The complete-graph subfamily \(m=1\) and centered-star exception are therefore not presented as new discoveries. The distinct claim here is the explicit joint two-lag reconstruction across the entire two-parameter clique-bouquet family, including changes in both parameters, and strict monotonicity with respect to blade count. Pymar and Rivera study a different asynchronous single-vertex-update version and a global density process; their results do not give these local temporal inversion formulas. General pair-coalescence identities are used as established tools rather than claimed as new.

## Limitations

Noise probability must be known and strictly between zero and one. Only the hub-rooted clique-bouquet class is classified, and only asymptotic observational identification is established: no sample complexity or finite-sample statistical risk bounds are claimed. Synchronous updating is essential to the formulas. Existing broad general-duality theory may rederive parts of the correlation computations, and independent historical-priority review remains to be done.

## References

- I. Benjamini, H. Helman Tov, and M. Zhukovskii, *Global information from local observations of the noisy voter model on a graph*, first posted 2022-07-04, arXiv:2207.01224, https://arxiv.org/html/2207.01224v2 (especially Sections 2, 4, 6).
- R. Pymar and N. Rivera, *Asymptotic behaviour of the noisy voter model density process*, first posted 2021-12-02, arXiv:2112.01478, https://arxiv.org/html/2112.01478v2 (model definition and Sections 1–3).
- A. Carro, R. Toral, and M. San Miguel, *The noisy voter model on complex networks*, 2016-04-20, https://doi.org/10.1038/srep24775 (network heterogeneity; different observables).
