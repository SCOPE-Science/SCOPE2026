# Spatial delay heterogeneity is spectrally free, but temporal memory mixing is costly on directed opinion cycles

## Finding

**Theorem (sharp spatial–temporal delay dichotomy).** Consider any directed opinion cycle with \(n\ge2\) vertices, homogeneous retention factor \(0<s<1\), fixed baseline \(0<c<1-s\), and any finite maximum communication lag \(L\ge0\). For each vertex \(i\), choose a probability law \(q_i\) on the integer lags \(\{0,\ldots,L\}\). The beliefs obey
\[
 p_i(t+1)=c+s\sum_{k=0}^L q_i(k)p_{i-1}(t-k),\quad i\pmod n.
\]
The unique steady belief is \(p_i^*=c/(1-s)\). Its **sharp global worst-case exponential relaxation factor** is the unique \(r\in(0,1)\) solving
\[
 \boxed{s^n\prod_{i=1}^n\left(\sum_{k=0}^Lq_i(k)r^{-(k+1)}\right)=1.}
\]
It is the exact spectral radius of the full finite-memory state-update matrix; an admissible positive perturbation of the steady history realizes this factor exactly at every step in a weighted norm.

Write \(\mu_i=\sum_k kq_i(k)\) and \(B=\sum_i\mu_i\). Then the sharp aggregate-delay bound is
\[
 \boxed{r\ge s^{n/(n+B)},}
\]
with equality **if and only if every** \(q_i\) is concentrated on a single lag. Thus arbitrary spatial variation in *fixed* delays has **no effect** on the relaxation factor beyond their sum, whereas any genuine temporal averaging of lags strictly increases it when aggregate mean delay is held constant. For any integer \(0\le B\le nL\), the bound is attained by every deterministic schedule whose integer lags add to \(B\).

More generally, replacing any \(q_i\) by a strict mean-preserving spread increases \(r\). With individual means \(\mu_i\) and bounded support fixed, \(r\) is uniquely minimized by adjacent-integer laws on \(\lfloor\mu_i\rfloor,\lceil\mu_i\rceil\) and uniquely maximized by endpoint laws on \(\{0,L\}\), except for forced degenerate cases. Each extremal rate is obtained by substituting the corresponding laws into the boxed equation.

For example, at \(n=4\), \(s=1/2\), and aggregate mean delay \(B=4\), fixed lag vectors \((1,1,1,1)\) and \((4,0,0,0)\) both give \(r=1/\sqrt2\). Giving every vertex the nondegenerate lag distribution \(q_i(0)=3/4\), \(q_i(4)=1/4\) preserves \(B=4\) yet yields \(r=0.756552333059\ldots>1/\sqrt2\).

## Assumptions and scope

The vertices form a single directed cycle, so each nonbaseline influence comes from precisely the preceding vertex. The baseline and influence multiplier are the same at all vertices. The lag laws are fixed in time; a weighted memory law is a **deterministic linear combination of past beliefs**, not a random delay sampled at every update. At \(t=0\), supply arbitrary histories \(p_i(-L),\ldots,p_i(0)\in[0,1]\). Since \(c+s<1\), all resulting beliefs stay in \((0,1)\) after one update. The theorem includes zero coefficients and reducible finite-memory matrices, and does not assume irreducibility of the augmented transition. The overall rate is a worst-case rate, not a claim that every initial history decays at exactly that rate. For \(L=0\) the extremal-law statements are vacuous.

## Proof

**1. Steady state and error recurrence.** The vector of constant beliefs \(p^*\mathbf1\) with \(p^*=c/(1-s)\) is fixed. Put \(e_i(t)=p_i(t)-p^*\); then
\[e_i(t+1)=s\sum_{k=0}^{L}q_i(k)e_{i-1}(t-k).\]
If \(z\) is a fixed point, the maximum norm obeys \(\|z-p^*\mathbf1\|_\infty\le s\|z-p^*\mathbf1\|_\infty\), so that point is unique.

**2. Exact spectral law, including arbitrary zero entries.** Let \(\mathcal B\) be the \(n(L+1)\)-dimensional companion matrix on the stacked error history \((e(t),e(t-1),\ldots,e(t-L))\). It is entrywise nonnegative. Define \(H_i(r)=\sum_{k=0}^L q_i(k)r^{-(k+1)}\). The continuous function \(s^n\prod_iH_i(r)\) is strictly decreasing from infinity to \(s^n<1\) as \(r\) increases from zero to one, proving the existence of a unique \(r\in(0,1)\) in the boxed equation.

Choose positive \(v_1,\ldots,v_n\) recursively from
\[v_i=sH_i(r)v_{i-1},\]
indices modulo \(n\); the root identity makes the cycle consistent. The strictly positive stacked vector \(V\), with lag-layer components \(V_{i,k}=r^{-k}v_i\), satisfies \(\mathcal BV=rV\): its leading rows obey the defining recursion and its lower rows are the history shifts. Set \(D=\operatorname{diag}(V)\). Then \(D^{-1}\mathcal BD\) is nonnegative and all its row sums equal \(r\). Its infinity operator norm is \(r\), giving \(\rho(\mathcal B)\le r\); since \(r\) is an eigenvalue, \(\rho(\mathcal B)=r\). This argument requires neither aperiodicity nor irreducibility. It proves for all initial histories
\[\|D^{-1}E(t)\|_\infty\le r^t\|D^{-1}E(0)\|_\infty.\]
Choosing \(E(0)=\varepsilon V\) with sufficiently small positive \(\varepsilon\) to keep all the initial beliefs within \([0,1]\) gives equality at all times. Therefore the rate is sharp and physically admissible.

**3. A spatial-delay identity and a strict temporal penalty.** Strict convexity of \(x\mapsto r^{-x}\) for \(r\in(0,1)\) gives Jensen's inequality
\[H_i(r)=r^{-1}\mathbb E[r^{-K_i}]\ge r^{-(1+\mu_i)},\]
with equality exactly for a point-mass lag law. At \(r_0=s^{n/(n+B)}\), the product of the right sides equals \(s^{-n}\); thus \(s^n\prod_iH_i(r_0)\ge1\), strictly if any law is nondegenerate. Since that product decreases strictly with \(r\), its unique unit root obeys \(r\ge r_0\), with the asserted equality characterization. When every \(q_i=\delta_{k_i}\), the defining equation reduces to \(s^nr^{-(n+\sum_i k_i)}=1\), proving both exact invariance under spatial redistribution and attainability for each integer total budget \(B\). An integer between \(0\) and \(nL\) can always be represented as the sum of \(n\) integers in \([0,L]\).

**4. Convex ordering and extremal laws.** If \(q_i'\) is a strict mean-preserving spread of \(q_i\), every strictly convex \(x\mapsto r^{-x}\) has strictly larger expectation under \(q_i'\); the defining product rises at each \(r<1\), moving the unique unit root to the right. For a fixed mean \(\mu\), any convex function on \(\{0,\ldots,L\}\) has expected value bounded below by its linear interpolation at the two integers bracketing \(\mu\), and bounded above by the chord joining its endpoint values. Both inequalities are strict unless the law lies on the respective extremal support (when the mean forces uniqueness). Apply these inequalities separately to each \(H_i(r)\) and use the strict decrease of the product to establish the sharp minimum and maximum spectral factors. This completes the proof.

## Verification

A reproducible standalone script `verify.py` constructs the complete lifted matrices, computes their eigenvalue spectral radii and the unique positive product roots over generated small directed cycles. It also tests the two exact spatial rearrangements, the temporal mixture example and optimal fixed-mean supports. Such tests are secondary to the preceding analytic proof; they cannot certify the theorem for all graph sizes, lags or distributions. No arbitrary precision or external certificates are necessary for the symbolic identities used.

## Relationship to prior work

Singh, Moharir and Sahasrabudhe (2026) introduce fixed finite memory sets, directed influence networks, and delayed affine belief dynamics. The model here restricts their broad influence setting to a homogeneous directed ring, allows explicitly weighted finite memory, and asks a different question: **the exact spectral rate under spatial versus temporal placement of a fixed memory budget**. The source's abstract describes asymptotic convergence and fixed-point properties, not this cyclic delay-budget dichotomy; its full original text was not accessible during the literature comparison, so this remains a material priority limitation.

Yao and Li (2025/2026) examine convergence and delays in more general signed opinion systems, including qualitative slowing in discrete time; their accessible abstract does not specify the cyclic product formula or the deterministic-spatial-versus-temporally-mixed strict contrast. Tsianos and Rabbat (2012) study constant and varying link communication delay for consensus, but their accessible abstract does not identify this anchored affine-belief rate law.

The published *Exact delay-distribution law for two-coordinate randomized Gauss-Seidel* proves a structurally related **convex-order delay penalty and endpoint-versus-adjacent extremizers**, for a distinct scalar **randomized linear-solver mean-square** recursion. Those generic convex-order consequences are not independently claimed as a new mechanism. In contrast, its full result is not a directed network of coupled opinion beliefs and does not imply the spatial-delay conservation identity or the cycle product formula without the new directed-cycle reduction. The published *Sharp gain optimization for consensus with exponential fading memory* treats continuous-time Laplacian dynamics with a common infinite-memory kernel, not heterogeneous finite-lag cyclic influence. These are the closest known comparisons, not proof of universal priority.

## Limitations

The theorem applies to linear time-invariant affine beliefs on a single **directed cycle** with identical \(s,c\) at all vertices. It is not a result on arbitrary graphs, heterogeneous influence strengths, nonlinear or stochastic opinion updates, time-varying memory sets, bot targeting, absolute mean consensus, or empirical human behavior. Spatial delay redistribution invariance may fail outside this class. The full original Singh–Moharir–Sahasrabudhe article and the full Yao–Li work were inaccessible; unresolved equivalent statements in their main text or appendices are an originality risk. The Gaussian/second-moment result cited above already contains the convex-order algebra in a different application. An independent assessment of historical priority and mathematical significance remains necessary.

## References

1. S. Singh, S. Moharir, N. Sahasrabudhe, *Opinion Dynamics with Memory Loss and Communication Delays*, arXiv:2608.10491v1 (first public August 11, 2026), https://arxiv.org/abs/2608.10491 .
2. L. Yao and A. Li, *Convergence of time-delayed opinion dynamics with complex interaction types*, arXiv:2501.12219v1 (2025), https://arxiv.org/abs/2501.12219 ; SIAM J. Control Optim. (2026), https://doi.org/10.1137/25M1824525 .
3. K. I. Tsianos and M. G. Rabbat, *The Impact of Communication Delays on Distributed Consensus Algorithms*, arXiv:1207.5839 (2012), https://arxiv.org/abs/1207.5839 .
4. *Exact delay-distribution law for two-coordinate randomized Gauss-Seidel* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-exact-stochastic-delay-law-randomized-gauss-seidel--9ae0040f2dac .
5. *Sharp gain optimization for consensus with exponential fading memory* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-gain-optimization-for-consensus-with-exponential-fading-me--a3cf7ff47956 .
