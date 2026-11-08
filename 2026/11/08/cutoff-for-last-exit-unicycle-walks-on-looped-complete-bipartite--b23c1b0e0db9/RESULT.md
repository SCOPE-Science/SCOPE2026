# Cutoff for last-exit unicycle walks on looped complete bipartite graphs

## Finding

Let \(a_n,b_n\) be positive integers with \(M_n=\max(a_n,b_n)\to\infty\) and \(\liminf_n\min(a_n,b_n)/M_n>0\). Form the undirected complete bipartite graph with parts of sizes \(a_n,b_n\), and add exactly one self-loop at every vertex. Regard its edges as permitted oriented steps in both directions. A *rooted unicycle state* consists of an outgoing arrow \(\rho(v)\) from each vertex to a permitted neighbor, whose directed functional graph has exactly one cycle, and a walker position \(X\) on that cycle. The uniform unicycle walk updates the arrow at \(X\) to a uniformly chosen permitted neighbor \(Y\), then moves the walker to \(Y\). Let \(\pi_n\) be its unique invariant distribution and define the worst-case total-variation distance

\[
d_n(t)=\max_{(x,\rho)}\|\mathcal L_{x,\rho}(X_t,\rho_t)-\pi_n\|_{\mathrm{TV}}.
\]

**Theorem.** For every fixed \(\varepsilon\in(0,1)\),

\[
\lim_{n\to\infty}d_n\big(\lfloor(1-\varepsilon)2M_n\log M_n\rfloor\big)=1,
\qquad
\lim_{n\to\infty}d_n\big(\lceil(1+\varepsilon)2M_n\log M_n\rceil\big)=0.
\]

In particular the worst-case total-variation cutoff occurs at \(2M_n\log M_n\). This includes all bounded-aspect-ratio balanced and unbalanced complete bipartite families, with self-loops as specified. For a graph with \(2m\) vertices divided equally, the cutoff is at \(2m\log m\).

## Assumptions and scope

The row at a vertex in the part of size \(a\) is uniform on the other \(b\) vertices and the vertex itself; the row at a vertex in the part of size \(b\) is uniform on the \(a\) opposite vertices and itself. The two parts are complete across; no other edges or multiple loops are present. The chain is restricted to rooted unicycle states, not to arbitrary initial arrow configurations. The aspect-ratio assumption means that some \(\delta>0\) satisfies \(m_n\ge\delta M_n\) eventually, where \(m_n=\min(a_n,b_n)\). All limits are for integer time. No result for the strictly loop-free, periodic walk is asserted.

## Proof

**1. Well-posed finite chain and stationary symmetry.** Replacing the arrow at the current cycle vertex by any allowed outgoing edge and moving along it preserves the property of being a rooted unicycle: deleting that vertex's old outgoing edge breaks the unique cycle into a directed tree pointing to that vertex, and the new edge closes one cycle through the new root. Finite irreducibility of this total chain for positive local transitions and strongly connected underlying graph is established in Kaiser--Levine--Sava-Huss, Proposition 3.3 in the open preprint (equivalently Proposition 3.9 in the journal version). Self-loops make it aperiodic. Uniqueness and invariance under arbitrary permutations within either vertex part follow.

For completeness, the uniform counting distribution on rooted unicycle states is invariant: fix state \((y,\rho)\), and let \(x\) be the predecessor of \(y\) around its unique directed cycle. Every predecessor state must have walker at \(x\); deleting its outgoing arrow leaves a directed tree toward \(x\), so each choice of an old arrow from \(x\) gives exactly one legal predecessor. If \(d(x)\) is the number of permitted outgoing neighbors, there are \(d(x)\) such predecessor states, each transitioning to \((y,\rho)\) with probability \(1/d(x)\). Thus each transition column sums to one. In particular, for any fixed vertex \(z\) in a part of size \(m\), automorphism symmetry gives

\[
\mathbb E_{\pi}\#\{v\text{ in the opposite part}:\rho(v)=z\}\le M/m,
\]

where \(M\) is the opposite part size.

**2. Upper bound by full-memory coupling.** Set \(M=\max(a,b)\), \(m=\min(a,b)\). Couple two independent-initial-state chains by a maximal coupling of their position chains at every step until the walkers coincide; thereafter use identical position choices. This is valid because position transitions do not depend on stored arrows. From any pair of distinct positions in opposite parts, the two transition rows overlap at both current vertices, with total mass at least \(2/(M+1)\). From distinct positions in the same part, the rows overlap on every vertex of the opposite part, with mass at least \(m/(m+1)\), which exceeds \(2/(M+1)\) for all sufficiently large \(M\). Thus the meeting time \(\tau\) satisfies

\[
\Pr(\tau>h)\le\exp[-2h/(M+1)].
\]

After meeting, memories agree once their common walk has used every vertex as a departure point. For a specified target vertex in a part of size \(s\), with opposite part size \(r\), the probability of hitting that target within two steps from any initial position is at least \(r/[(r+1)(s+1)]\): from the opposite part one can hit immediately, and from another point of the same part one can cross and return. Hence, uniformly over all target vertices, this probability is bounded below by

\[
q=\frac{m}{(m+1)(M+1)}=\frac{1+o(1)}M.
\]

Repeated conditioning on non-hit two-step blocks and a union bound show that, from any starting position, the probability of failing to depart from at least one of the \(a+b\) vertices during a further \(s\) steps is at most

\[
(a+b)(1-q)^{\lfloor(s-1)/2\rfloor}.
\]

Take the second chain initially distributed according to \(\pi_n\), let \(h=\lfloor\varepsilon M\log M/2\rfloor\), and \(t=\lceil(1+\varepsilon)2M\log M\rceil\). By the coupling inequality and the strong Markov property at \(\tau\),

\[
d_n(t)\le e^{-2h/(M+1)}+(a+b)(1-q)^{\lfloor(t-h-1)/2\rfloor}=o(1).
\]

Indeed the second term is at most \(2M\exp[-(1+3\varepsilon/4+o(1))\log M]\to0\), and the first is \(M^{-\varepsilon+o(1)}\).

**3. Lower bound by untouched arrows.** Let the larger part have size \(M\), the other size \(m\), choose a fixed vertex \(z\) in the smaller part and \(w\) in the larger part. Initialize all larger-part arrows pointing to \(z\), all smaller-part arrows pointing to \(w\), and the walker at \(z\). This is a valid rooted unicycle: \(z\leftrightarrow w\) is its unique two-cycle.

A new distinct larger-part vertex can be visited only through a transition from the smaller to the larger part. Each such crossing chooses a uniform larger-part vertex independently of previous crossing destinations, as the stay/cross decision depends only on the present part. The number of such crossings before time \(t\) is at most \(\lceil t/2\rceil\), deterministically (consecutive crossings in the same direction are impossible). Thus the number \(U\) of untouched larger-part arrows stochastically dominates the empty-bin count after \(k=\lceil t/2\rceil\) independent uniform draws from \(M\) bins. Its mean equals \(M(1-1/M)^k\), and its variance is at most its mean, because distinct empty-bin indicators have nonpositive covariance:

\[
\left(1-\frac2M\right)^k\le\left(1-\frac1M\right)^{2k}.
\]

At \(t=\lfloor(1-\varepsilon)2M\log M\rfloor\), the mean is \(M^{\varepsilon+o(1)}\); Chebyshev's inequality gives \(\Pr(U\ge M^{\varepsilon/2})\to1\). Every untouched larger-part arrow still points to \(z\). For the event \(F=\{\#\{v\text{ in larger part}:\rho(v)=z\}\ge M^{\varepsilon/2}\}\), we consequently have \(\Pr_{\mathrm{initial}}(F)\to1\). Yet stationary symmetry and Markov's inequality imply

\[
\pi_n(F)\le\frac{M/m}{M^{\varepsilon/2}}\le\frac{1}{\delta M^{\varepsilon/2}}\to0.
\]

The variational characterization of total variation gives \(d_n(t)\ge\Pr_{\mathrm{initial}}(F)-\pi_n(F)\to1\). This finishes the proof. \(\square\)

## Verification

The exact-arithmetic standalone script `checks.py` enumerates all rooted unicycle states and legal transitions for part sizes \((2,2),(2,3),(3,2),(3,3)\). It checks closure, strong connectivity, invariant counting measure through column sums, stationary arrow-count bounds, and all ordered-pair two-step hitting inequalities. It separately checks the negative-covariance occupancy variance formula over integer bin counts \(2\) through \(17\) and draw counts \(0\) through \(35\). Run `python3 checks.py` from this package; it reports 12,430 exact assertions passing. These finite checks are not a substitute for the analytic bounds for all sizes.

## Relationship to prior work

Kaiser, Levine and Sava-Huss, *Locally Markov walks on finite graphs* (arXiv:2412.13766, first posted December 18, 2024), define the total/unicycle chain, give stationary and recurrence theory, and establish cutoff for complete graphs, with self-loops permitted in the cutoff section. Their Section 5 expressly asks whether a non-complete graph sequence exhibits uniform-unicycle cutoff. The present theorem gives an explicit bounded-aspect-ratio bipartite family, using direct coupling and a stationary persistent-arrow witness; its proof does not assume the source's complete-graph distance identity on other graphs.

Earlier tree-walk/Markov chain tree-theorem work of Anantharam--Tsoucas addresses tree representations and stationarity. Lamplighter mixing literature considers independent lamp coordinates rather than last-exit unicycle arrows, so a lamplighter cutoff does not by itself imply the stated total-chain result. Relevant historical-priority comparison remains non-exhaustive.

## Limitations

The result is restricted to one self-loop per vertex, uniform transitions, complete bipartite structure, and bounded aspect ratio. No sharp bounded-width cutoff profile, second-order mixing center, loop-free parity-class result, or arbitrary-graph cutoff criterion is claimed. The 12,430 finite checks corroborate only tested finite identities. No independent mathematical audit or definitive comprehensive priority certification has been performed.

## References

1. R. Kaiser, L. Levine, E. Sava-Huss, *Locally Markov walks on finite graphs*, arXiv:2412.13766 (v1 December 18, 2024; later publication in *Random Structures & Algorithms*, 2026). https://arxiv.org/html/2412.13766
2. V. Anantharam, P. Tsoucas, *A proof of the Markov chain tree theorem*, *Statistics & Probability Letters* 8 (1989), 189–192. https://doi.org/10.1016/0167-7152(89)90016-3
3. J. Miller, Y. Peres, *Uniformity of the uncovered set of random walk and cutoff for lamplighter chains*, *Annals of Probability* 40 (2012), 535–577. https://www.microsoft.com/en-us/research/publication/uniformity-uncovered-set-random-walk-cutoff-lamplighter-chains/
