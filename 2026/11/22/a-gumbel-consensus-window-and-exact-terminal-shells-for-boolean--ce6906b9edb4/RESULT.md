# A Gumbel consensus window and exact terminal shells for Boolean-cube OR dynamics

## Finding
For each integer \(d\ge3\), place Boolean states at the vertices of the binary Hamming cube \(Q_d\) and update synchronously by open-neighbor disjunction,
\[
(Fx)_v=\bigvee_{i=1}^{d}x_{v\oplus e_i}.
\]
Write \(\tau(x)\) for the first time that the trajectory is periodic, \(N=2^{d-1}\), \(H=2^N\), and
\[
U=N\left(2^d-d-1-\frac12\binom d2\right).
\]
The exact sharp maximal entrance time is \(d-1\), with the following labelled-state terminal-shell counts:
\[
\boxed{\#\{x:\tau(x)=d-1\}=2NH-N^2},
\]
\[
\boxed{\#\{x:\tau(x)=d-2\}=2U(H-N)-U^2}.
\]
There are exactly four immediately periodic states. The remaining earlier first-entry populations are not claimed to have a closed formula here.

Independently initialize all \(2^d\) sites with Bernoulli activation probability \(p_d=1/2+a/d\), where \(a\in\mathbb R\) is fixed and \(d\) is sufficiently large to make this a probability. Then the exact first-entry time has the two-point asymptotic law
\[
\boxed{\lim_{d\to\infty}\Pr(\tau=1)=\exp(-e^{-2a}),\qquad
\lim_{d\to\infty}\Pr(\tau=2)=1-\exp(-e^{-2a}).}
\]
In particular \(\Pr(\tau\le1)\to\exp(-e^{-2a})\) and \(\Pr(\tau\le2)\to1\). For any fixed \(0<p<1/2\), \(\Pr(\tau=2)\to1\); for fixed \(1/2<p<1\), \(\Pr(\tau=1)\to1\). Thus the one-update consensus threshold is at initial density \(1/2\), with a critical window of order \(1/d\), even though exceptionally sparse configurations may take \(d-1\) updates.

## Assumptions and scope
The vertex set is \(\{0,1\}^d\); an edge joins two words at Hamming distance one. There are no self-inputs. All sites update simultaneously, and all enumerations count individually labelled binary configurations. A state \(y\) is periodic if \(F^r(y)=y\) for some integer \(r\ge1\). The entrance time \(\tau(x)\) is the smallest \(t\ge0\) for which \(F^t(x)\) is periodic. The random limit concerns product Bernoulli initial conditions; it does not assert a deterministic two-update bound. The terminal-shell identities hold for every integer \(d\ge3\), without asymptotic qualification. Initial density exactly zero or one is excluded from the fixed-density random dichotomy.

## Proof
**Reachability and periodic states.** Put \(P_0\) and \(P_1\) for the two Hamming-parity classes, both of size \(N\). If \(S\) is an initial support, the support at time \(t\) is exactly the collection of endpoints of walks of length \(t\) beginning at \(S\), because OR distributes over path concatenation. For a particular start and endpoint, a length-\(t\) walk exists if and only if their distance is at most \(t\) and congruent to \(t\) modulo two: follow a shortest path and insert backtracking pairs. The support from each initial parity class therefore evolves independently through alternating target classes. Within a fixed parity class the distance-two graph is connected; the second iterate includes every old active vertex and its distance-two neighbors. Consequently repeated second iterates of a nonempty support strictly expand it unless it is the entire class. Any periodic support must be empty or the full class. The four recurrent configurations are the zero state, the all-one state and the two alternating parity-class indicators.

**Covering-radius clock.** Let \(S\) be a nonempty subset of one parity class, and define its Hamming covering radius in the *whole* cube by
\[
R(S)=\max_{v\in\{0,1\}^d}\min_{s\in S}d_H(v,s).
\]
Let \(r_0\) and \(r_1\) be the two maxima restricted to vertices at even and odd distance from \(S\), respectively. Each is an integer of the corresponding parity. The distance-to-set function is one-Lipschitz across an edge. Taking a neighbor of a vertex attaining either maximum proves \(|r_0-r_1|\le1\); the parity difference makes the difference exactly one. At time \(\min(r_0,r_1)\), every vertex of the target parity class is reached, and at the next time the other target class is full. No earlier iterate has filled its target class. Thus the first periodic-entry time contributed by this support is
\[
T(S)=R(S)-1.
\]
Set \(T(\varnothing)=0\). For the two independently chosen parity supports \(S_0,S_1\), the first-entry time is precisely \(\tau=\max(T(S_0),T(S_1))\). Since \(R(S)\le d\) for a nonempty support and a singleton has radius \(d\), the sharp global maximum is \(d-1\).

**Terminal shells.** For a support \(S\) lying in a specified parity class, \(R(S)=d\) precisely when \(S\) is a singleton: the only point at distance \(d\) from a given vertex is its antipode. Hence exactly \(N\) supports on each parity class have \(T=d-1\). A nonsingleton has \(T=d-2\) exactly when there is a cube vertex at distance at least \(d-1\) from every seed. Such a vertex cannot be at distance \(d\) from two different seeds, so the support must be a subset of the \(d\) ordinary Hamming neighbors of the antipode. Conversely every subset of that star having at least two elements has covering radius exactly \(d-1\). The parity class contains \(N\) possible star centers in the opposite parity class.

Each of these stars has \(2^d-d-1\) subsets of size at least two. Two different stars intersect in exactly two sites if their centers have Hamming distance two, and otherwise do not intersect. A pair of same-parity sites at Hamming distance two has exactly two common neighboring centers; a subset of size at least three cannot be shared between stars. Therefore the number of distinct qualifying nonsingleton supports is
\[
N(2^d-d-1)-\frac N2\binom d2=U.
\]
There are \(H\) supports per parity class, \(H-N\) of them with contribution at most \(d-2\), and \(H-N-U\) with contribution at most \(d-3\). Taking the maximum of the two independent contributions gives respectively
\[
H^2-(H-N)^2=2NH-N^2,
\]
\[
(H-N)^2-(H-N-U)^2=2U(H-N)-U^2.
\]
For \(d=3\), the latter is the time-one shell, with 140 states; the former is the time-two shell, with 112 states. Four states are recurrent at time zero.

**Critical-density law.** Put \(M=2^d\), \(q_d=1-p_d\), and let \(W_d\) be the number of zero sites at time one. For each vertex \(v\), the event that it stays zero is that all \(d\) initial neighbors are zero, so
\[
\lambda_d=\mathbb E W_d=Mq_d^d=(1-2a/d)^d\longrightarrow e^{-2a}.
\]
Distinct vertex-neighborhoods are disjoint except when the vertices lie at Hamming distance two, in which case they share exactly two sites. For every fixed positive integer \(k\), all but \(O_k(M^{k-1}d^2)\) ordered distinct \(k\)-tuples of sites have pairwise disjoint neighborhoods. A disjoint tuple contributes probability \(q_d^{kd}\). For any exceptional tuple, the union of its \(k\) neighborhoods has at least \(kd-2\binom k2\) vertices, so its contribution is at most \(q_d^{kd-2\binom k2}\). Since \(q_d\to1/2\), the exceptional total is \(O_k(d^2/M)\) times a bounded factor. Therefore every fixed factorial moment satisfies
\[
\mathbb E(W_d)_k\longrightarrow(e^{-2a})^k.
\]
The factorial-moment criterion for nonnegative integer variables yields \(W_d\Rightarrow\mathrm{Poisson}(e^{-2a})\), and consequently \(\Pr(W_d=0)\to\exp(-e^{-2a})\).

If the initial support occupies both parity classes, the only periodic target at time one is the all-one configuration. The probability that an initial parity class is empty is at most \(2q_d^N\), and the probability of being recurrent already at time zero also tends to zero. Hence \(\Pr(\tau=1)\) has the same limit as \(\Pr(W_d=0)\). At time two the predecessor set of any vertex is the closed distance-two Hamming ball within its parity class, of size \(1+\binom d2\). The union bound gives
\[
\Pr(F^2(x)\ne\mathbf1)\le Mq_d^{1+\binom d2}\longrightarrow0.
\]
This proves the two-point distribution. If \(p\) is fixed above \(1/2\), Markov's inequality applied to \(\mathbb EW=M(1-p)^d\to0\) gives one-update consensus. If \(p\) is fixed below \(1/2\), the mean diverges and the neighborhood-intersection count bounds
\[
\frac{\mathrm{Var}(W)}{(\mathbb EW)^2}\le\frac1{\mathbb EW}+\frac{\binom d2}{M(1-p)^2}\longrightarrow0.
\]
Thus one-update consensus fails with probability tending to one, while the same two-step union bound gives two-update consensus. The fixed-density assertions follow.

## Verification
Three standalone scripts are supplied. `check_hypercube.py` explicitly builds the synchronous OR state transition, computes each state's true least preperiod by cycle detection, and enumerates *every* binary configuration for dimensions two, three and four. Its histograms are respectively \((4,12)\), \((4,140,112)\), and \((4,33852,27648,4032)\) in increasing entrance-time order. Both terminal-shell formulas agree in the claimed dimensions. `check_radius.py` independently computes Hamming covering radii for every support on either parity class through dimension five, reproducing the per-class terminal contributions \((N,U)=(4,10),(8,64),(16,336)\) at dimensions three through five. `check_window.py` implements bit-parallel independent updates and Monte Carlo spot checks at dimensions six, eight, ten and twelve; it also checks the exact second factorial moment identity
\[
\mathbb E(W_d)_2=M(M-1-\binom d2)q_d^{2d}+M\binom d2\,q_d^{2d-2}.
\]
These finite tests support implementation correctness and finite instances; the unrestricted assertions follow from the preceding proofs, not from extrapolating simulations.

## Relationship to prior work
Jarrah, Laubenbacher and Veliz-Cuba (2008) establish the general graph-walk/Boolean-matrix framework, recurrent period constraints and height bounds for conjunctive and disjunctive networks. The four recurrent configurations and the existence of an eventual two-periodic regime are not claimed as new. The published *Exact maximal-transient census for disjunctive dynamics on halved Boolean cubes* concerns the **distance-two** graph on the cube, whose two Hamming-parity components are invariant under one update. Here the **distance-one** graph exchanges the parity classes, and the contribution is the exact penultimate as well as ultimate first-entry population paired with a critical-density Gumbel one-step consensus law. A distance-two-graph maximal-shell theorem does not yield this one-step density window or these one-step dynamics.

Weichsel (1994) studies *perfect dominating sets* of hypercubes, a different exact covering requirement. Weber (1987) studies Poisson limits for isolated subcubes and degree counts in randomly vertex- or edge-deleted hypercubes; this is a relevant potential antecedent for the Poisson method, but his complete text was unavailable for an implication-level comparison. The present one-update missing-site count includes sites irrespective of whether the site itself was initially occupied, and the second-step entry law and exact terminal-shell census are additional dynamical assertions. Random threshold-two bootstrap percolation on cubes uses permanent activation and a different local threshold, so its critical-density results do not imply the synchronous open-neighbor OR result.

## Limitations
The results concern the open-neighbor, nonpersistent Boolean OR update, not persistent infection, majority bootstrap percolation, asynchronous updating or Greenberg–Hastings excitation. The exact finite formulas address the two final entrance shells, not a complete closed census of every intermediate depth. The critical-window limit is for initial independent Bernoulli states; it does not imply every configuration converges within two updates. The historically related 1987 Poisson paper could not be inspected in full, so priority against equivalent stochastic formulations is not certified. The proof is self-contained but has not undergone independent mathematical review.

## References
1. A. S. Jarrah, R. Laubenbacher and A. Veliz-Cuba, *The Dynamics of Conjunctive and Disjunctive Boolean Networks*, public preprint 2008-05-02, arXiv:0805.0275, https://arxiv.org/abs/0805.0275.
2. K. Weber, *Poisson Convergence in the n-Cube*, Mathematische Nachrichten 131 (1987), 49–57, https://doi.org/10.1002/mana.19871310105.
3. P. M. Weichsel, *Dominating sets in n-cubes*, Journal of Graph Theory 18 (1994), 479–488, https://doi.org/10.1002/jgt.3190180506.
4. J. Balogh, B. Bollobás and R. Morris, *Majority bootstrap percolation on the hypercube*, 2007-02-13 preprint, arXiv:math/0702373, https://arxiv.org/abs/math/0702373.
5. *Exact maximal-transient census for disjunctive dynamics on halved Boolean cubes*, publicly available result, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-maximal-transient-census-for-disjunctive-dynamics-on-halve--52e59b4571bb.
