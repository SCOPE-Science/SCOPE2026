# Topology-free exponential attraction for arbitrarily delayed Michaelis–Menten networks

## Finding
For any finite directed network of Michaelis–Menten activation and inhibition links, existence of a strictly positive equilibrium implies exponential convergence to it for **all** strictly positive continuous histories, for **arbitrary finite fixed interaction delays** and **without a connectivity assumption**. The rate can be computed from the history's logarithmic box and a Halanay-type scalar inequality.

Writing \(r\) for the initial maximal logarithmic error and \(\tau\) for the largest delay, the conclusion is
\[
\max_i\left|\log\frac{x_i(t)}{\bar x_i}\right|\le r e^{-\eta t}\qquad(t\ge0)
\]
for each \(\eta>0\) with \(\eta+B_r(e^{\eta\tau}-1)<\delta_r\), where \(\delta_r\) and \(B_r\) are given explicitly below. The result applies to reducible mixed-sign interaction graphs beyond the topology restrictions of the existing delayed theorem.

## Assumptions and scope
Let \(n\ge1\) be an integer and, for each \(i\), let \(d_i>0\), \(b_i\ge0\). Each directed link \(j\to i\) with \(j\neq i\) is either absent or has one of the forms
\[
h_{ij}(s)=\frac{a_{ij}s}{k_{ij}+s}\quad\text{(activation)},\qquad
h_{ij}(s)=\frac{a_{ij}k_{ij}}{k_{ij}+s}\quad\text{(inhibition)},
\]
where \(a_{ij},k_{ij}>0\). An absent link contributes zero to every sum. All delays \(\tau_{ij}\ge0\) are fixed and finite; set \(\tau=\max\tau_{ij}\), with \(\tau=0\) if no links exist. Consider
\[
\dot x_i(t)=-d_i x_i(t)+b_i+\sum_{j\ne i}h_{ij}(x_j(t-\tau_{ij})).
\]
Suppose **only** that there is \(\bar x\in(0,\infty)^n\) satisfying
\[
d_i\bar x_i=b_i+\sum_{j\ne i}h_{ij}(\bar x_j)\qquad(1\le i\le n).
\]
Take any continuous history \(\phi:[-\tau,0]\to(0,\infty)^n\), with \(x(s)=\phi(s)\) on the history interval. Define
\[
r=\max_{i,\,-\tau\le s\le0}\left|\log\frac{\phi_i(s)}{\bar x_i}\right|,\qquad
K_r=\prod_{i=1}^n[\bar x_i e^{-r},\bar x_i e^r].
\]
For each positive vector \(z\), define
\[
q_i(z)=b_i+\sum_{j\ne i}\frac{h_{ij}(z_j)^2}{a_{ij}},\qquad
\delta_r=\min_{i,\,z\in K_r}\frac{q_i(z)}{z_i},\qquad
B_r=\max_{i,\,z\in K_r}\frac{\sum_{j\ne i}z_j|h'_{ij}(z_j)|}{z_i}.
\]
Sums omit absent links. Since each equilibrium coordinate is positive, every \(i\) has either \(b_i>0\) or at least one incoming link. Consequently \(q_i(z)>0\) on \(K_r\), so \(\delta_r>0\), while \(B_r<\infty\). For \(r=0\) the history is already the equilibrium and the claim is immediate.

## Proof
**Step 1: multiplicative-box invariance.** For any Michaelis–Menten link \(h\) and all \(s,c>0\), the subhomogeneity inequalities
\[
\min\{c,c^{-1}}\,h(s)\le h(cs)\le\max\{c,c^{-1}}\,h(s)
\]
hold, for either activation or inhibition. In both cases this follows by comparing the ratios of the denominators directly; the reciprocal factor is necessary for inhibitory links. In particular every link evaluated anywhere on \(K_r\) lies between \(e^{-r}h(\bar x_j)\) and \(e^rh(\bar x_j)\). The same holds for a constant input because \(b_i\ge0\). Thus, at an upper face \(x_i=e^r\bar x_i\), the derivative is at most \(-d_i e^r\bar x_i+e^r d_i\bar x_i=0\), while at a lower face it is at least zero. The standard first-exit argument for retarded functional differential equations proves that all future coordinates stay in \(K_r\). The vector field is locally Lipschitz and bounded there, hence there is a unique forward-complete positive solution.

**Step 2: exact logarithmic error equation.** Put \(w_i(t)=\log(x_i(t)/\bar x_i)\), and interpolate \(z_i^s(t)=\bar x_i\exp(s w_i(t))\), \(z_j^s(t-\tau_{ij})=\bar x_j\exp(s w_j(t-\tau_{ij}))\), for \(0\le s\le1\). Apply the fundamental theorem of calculus to the transformed vector field, with the equilibrium as reference. This gives the *exact* identity
\[
\dot w_i(t)=-A_i(t)w_i(t)+\sum_{j\ne i}C_{ij}(t)w_j(t-\tau_{ij}),
\]
where
\[
A_i(t)=\int_0^1\frac{b_i+\sum_{j\ne i}h_{ij}(z_j^s(t-\tau_{ij}))}{z_i^s(t)}\,ds,
\qquad
C_{ij}(t)=\int_0^1\frac{z_j^s(t-\tau_{ij})h'_{ij}(z_j^s(t-\tau_{ij}))}{z_i^s(t)}\,ds.
\]
For both the activating and the inhibiting rational forms, differentiation gives
\[
s|h'_{ij}(s)|=h_{ij}(s)-\frac{h_{ij}(s)^2}{a_{ij}}.
\]
Since the entire interpolated state lies in \(K_r\), the triangle inequality yields, at every time,
\[
A_i(t)-\sum_{j\ne i}|C_{ij}(t)|\ge\delta_r,
\qquad\sum_{j\ne i}|C_{ij}(t)|\le B_r.
\]
This is a strictly diagonally dominant, time-dependent delayed comparison system, irrespective of the graph's connectivity and edge signs.

**Step 3: delayed exponential comparison.** Choose \(\eta>0\) satisfying \(\eta+B_r(e^{\eta\tau}-1)<\delta_r\). Such a number exists by continuity at \(\eta=0\). Put \(u_i(t)=e^{\eta t}|w_i(t)|\) for \(t\ge-\tau\). At any first time when a component \(u_i(t)\) would exceed its initial history supremum \(r\), all delayed weighted components are at most that same supremum. The upper right Dini derivative then obeys
\[
D^+u_i(t)\le\left[\eta-A_i(t)+\sum_{j\ne i}|C_{ij}(t)|e^{\eta\tau_{ij}}\right]u_i(t)
\le -[\delta_r-\eta-B_r(e^{\eta\tau}-1)]u_i(t)<0.
\]
The first-crossing contradiction (or the elementary Halanay comparison) implies \(u_i(t)\le r\) for every \(i\) and \(t\ge0\). In the first inequality, delayed contributions are bounded by the first-crossing level; the displayed expression is evaluated when the current component attains that level. The asserted exponential estimate follows.

If another strictly positive equilibrium existed, using it as a constant positive history would contradict convergence to \(\bar x\). If a nonconstant strictly positive periodic orbit existed, its positive periodic history would similarly contradict convergence. Both conclusions hold for all finite delay choices.

## Verification
The standalone script `verify.py` checks the rational link derivative identity exactly, checks the equilibrium and conservative constants of a three-node reducible example with mixed activating/inhibiting edges, and integrates representative histories with positive delays. Exact finite arithmetic verifies the identities and inequalities; numerical trajectories are illustrative and are *not* proofs of universal convergence.

For the example take \(n=3\), \(d_i=2\), \(b_i=1\), activating edges \(2\to1\) and \(1\to3\), and an inhibiting edge \(1\to2\). Every nonzero edge has \(a=2\), \(k=1\); the delays are respectively \(3,7,5\), with \(\tau=7\). The equilibrium is \(\bar x=(1,1,1)\). The graph is **not** strongly connected. For histories with \(r\le\log2\), the box is \([1/2,2]^3\), and \(\delta_r\ge11/18\), \(B_r\le1\). Hence \(\eta=1/100\) is admissible, since \(1/100+e^{7/100}-1<11/18\), and the theorem guarantees \(\max_i|\log x_i(t)|\le(\log2)e^{-t/100}\).

## Relationship to prior work
Sontag (2026, arXiv:2610.24351, first posted October 17, 2026) establishes topology-free global exponential convergence for the **undelayed** Michaelis–Menten system in Theorem 3 and, separately, global convergence with arbitrary delays in Theorem 6 **under** graph assumptions (A2) and (A3). The latter theorem's statement is explicitly restricted to a strongly connected graph with a nondegeneracy condition. The present theorem makes the all-positive-history delayed conclusion *topology-free conditional on a positive equilibrium* and gives the explicit history-dependent Halanay exponent. The three-node example violates (A2); the result is therefore not a special case of the source's delayed theorem. The proof uses the source's logarithmic structural cancellation, extended to delayed pairs of states. The older Blanchini–Breda–Giordano–Liessi (2023) result gives structural stability, including local delayed stability, not the same global topology-free assertion.

The classical Halanay differential inequality is the stability tool, not claimed here as new. This result is a model-specific global implication of the rational activation/inhibition identity and a positive-equilibrium hypothesis. General delayed-system contraction theorems could provide an alternative derivation; identifying all such general prior coverage remains a historical-priority risk.

## Limitations
The initial history is required to be strictly positive; no theorem about boundary histories on reducible graphs is asserted. Delays are constant, finite, and act only on interaction terms. The interaction law is exactly Hill exponent one with linear degradation; arbitrary Hill exponents, state-dependent delays, or distributed kernels are not covered. The guarantee is conditional on existence of a positive equilibrium; it does not determine when one exists. The lower bound on the exponential rate is generally conservative and depends on the initial multiplicative box. This work is not independently validated.

## References
1. E. D. Sontag, *Global stability of Michaelis–Menten networks*, arXiv:2610.24351v1, first public October 17, 2026, Theorems 3 and 6, Section 8. https://arxiv.org/abs/2610.24351.
2. F. Blanchini, D. Breda, G. Giordano, D. Liessi, *Michaelis–Menten networks are structurally stable*, Automatica 147 (2023), article 110683. DOI:10.1016/j.automatica.2022.110683.
3. A. Halanay, *Differential Equations: Stability, Oscillations, Time Lags*, Academic Press (1966), exponential delay comparison inequality.
