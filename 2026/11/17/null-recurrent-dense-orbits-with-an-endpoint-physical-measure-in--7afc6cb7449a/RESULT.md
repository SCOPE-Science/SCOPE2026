# Null-recurrent dense orbits with an endpoint physical measure in an infinite-entropy interval map

## Finding
The continuous mixing infinite-entropy interval map constructed in Proposition 5.2 of Vinod Kumar P B [1] has a statistical behavior that sharply differs from its topological behavior. Let \(D_+:[0,\infty)\to[0,\infty)\) be the piecewise-affine map specified below, let \(\psi(u)=1-2^{-u}\), and let \(D_I=\psi\circ D_+\circ\psi^{-1}\) on \([0,1)\), extended by \(D_I(1)=1\).

For a uniform initial point in any unit block, the integer-part itinerary is an exact irreducible **null-recurrent**, reversible, nearest-neighbor Markov chain. Its transition probabilities are
\[
P_{00}=\frac59,\qquad P_{01}=\frac49,
\]
\[
P_{k,k-1}=P_{k,k+1}=\frac{2(k+2)}{6k+13},\qquad
P_{kk}=\frac{2k+5}{6k+13}\quad(k\ge1).
\]
Its infinite stationary weights, normalized by \(\pi_0=1\), are
\[
\boxed{\pi_k=\frac{2(6k+13)}{9(k+2)}=\frac43+\frac{2}{9(k+2)}\quad(k\ge1).}
\]
Consequently \(D_+\) preserves the explicit sigma-finite, infinite measure whose density equals \(\pi_k\) almost everywhere on \([k,k+1]\). The corresponding measure for \(D_I\) has density
\[
\boxed{\frac{d\mu}{dx}(x)=\frac{\pi_{\lfloor-\log_2(1-x)\rfloor}}{(1-x)\log 2}\quad\text{for almost every }0<x<1,}
\]
with \(\pi_0=1\). In particular its density is asymptotic to \(4/[3(1-x)\log2]\) as \(x\uparrow1\).

**For Lebesgue-almost every \(x\in[0,1]\), the forward orbit of \(x\) is dense in \([0,1]\), visits every nonempty open interval infinitely often, but its empirical probabilities converge weakly to the endpoint atom:**
\[
\boxed{\frac1N\sum_{n=0}^{N-1}\delta_{D_I^n(x)}\ \Longrightarrow\ \delta_1\qquad(N\to\infty).}
\]
Thus \(\delta_1\) is the unique physical invariant probability for this map, although no typical orbit converges pointwise to \(1\); there is no absolutely continuous invariant probability. These facts hold for the exact source map, without modifying its defining branches.

## Assumptions and scope
For each integer \(k\ge0\) write \(B_k=[k,k+1]\) and \(N_k=k+2\). On \(B_0\), split into \(4N_0+1=9\) equal subintervals and prescribe successive vertex values by \(0,(1,2,1,0)\) repeated twice, followed by \(1\). On \(B_k\), \(k\ge1\), split into \(6N_k+1=6k+13\) equal subintervals and prescribe values by \(k,(k-1,k,k+1,k+2,k+1,k)\) repeated \(N_k\) times, followed by \(k+1\). Interpolate affinely. This is precisely the source's Proposition 5.2 construction [1], not a family of maps with freely adjustable branches.

Every subdivision interval, called an edge branch, maps bijectively onto exactly one unit block, with absolute slope equal to the number of branches in its source block. For integer endpoints and all their preimages, the block index may be ambiguous; this countable set has Lebesgue measure zero and is excluded from symbolic probability statements. The measure \(\mu\) is not finite and is not a probability. Statements involving almost every initial condition use one-dimensional Lebesgue measure on the compact interval. The word physical means the basin of empirical weak convergence has positive Lebesgue measure, here full measure. The existing topological mixing and infinite-entropy properties are those proved in [1].

## Proof
**1. Exact Markov coding from full affine branches.** The nine edge branches of \(B_0\) lead five times to \(B_0\) and four times to \(B_1\). For every \(k\ge1\), the repeated six-step vertex word gives \(2(k+2)\) branches each to \(B_{k-1}\) and \(B_{k+1}\), with \(2(k+2)+1\) branches to \(B_k\). Each source branch has the same length, namely \(1/9\) for \(k=0\) and \(1/(6k+13)\) for \(k\ge1\). Conditional on the current block being uniform, the probability of a target block is its number of edge branches divided by the total. Moreover, under any chosen edge branch the image conditional law is uniform on the target block, because the restriction is affine and onto. Induction on the full finite edge history therefore shows that, from uniform initial position in any \(B_j\), the block process \(K_n=\lfloor D_+^n(u)\rfloor\) is exactly the Markov chain with the displayed matrix. Its finite edge cylinders have products of the appropriate reciprocal branch counts, and conditioning on such a cylinder leaves the terminal position uniform in its terminal block.

**2. Invariant density and reversibility.** Put \(\pi_0=1\) and \(\pi_k=2(6k+13)/[9(k+2)]\) for \(k\ge1\). Direct substitution gives
\[
\pi_kP_{k,k+1}=\pi_{k+1}P_{k+1,k}=\frac49\quad(k\ge0).
\]
Thus detailed balance holds, including the special boundary edge. Summing detailed balance across the (at most three) incoming edges of each state proves \(\sum_i\pi_iP_{ij}=\pi_j\). For the density equal to \(\pi_j\) on \(B_j\), the Perron–Frobenius transfer formula on a target point in \(B_j\) is exactly that incoming sum: each full affine branch originating in \(B_i\) contributes \(\pi_i/(\#\text{ of branches of }B_i)\). Hence the piecewise-constant density is invariant. Since \(\pi_k>4/3\) for all \(k\ge1\), its total mass is infinite, while mass in any finite block union is finite. The Jacobian \(du/dx=[(1-x)\log2]^{-1}\) under \(x=\psi(u)\) gives the density formula for \(\mu\); since \(\pi_k\to4/3\), the endpoint asymptotic follows.

**3. Recurrence with infinite mean return.** For each interior state \(k\ge1\), the two outward transition probabilities are equal and strictly positive. Therefore the function \(k\mapsto k/L\) is harmonic on \(\{1,\ldots,L-1\}\), with boundary values zero and one. Stopping at the first hit of \(0\) or \(L\) is almost surely finite (a finite irreducible killed chain), and the bounded optional-stopping theorem gives
\[
\Pr_k(T_L<T_0)=\frac{k}{L}\qquad(1\le k<L).
\]
Letting \(L\to\infty\) shows \(\Pr_k(T_0=\infty)=0\): an unbounded upward escape would have to reach every level \(L\) before hitting zero, and a path staying forever within a finite set while avoiding zero has probability zero. Hence every state hits \(0\) almost surely. The positive transition from \(0\) to \(1\) and the self-loop at \(0\) yield recurrent returns to \(0\), and irreducibility propagates recurrence to all states.

For a recurrent irreducible countable Markov chain, the existence of a finite invariant probability is equivalent to finite expected return time to one state; its invariant measure is then unique up to scale. Here detailed balance yields a positive invariant measure with \(\pi_k\ge4/3\) for all positive \(k\), and irreducible recurrence makes every invariant measure proportional to it. Thus no invariant probability exists, all return-time means are infinite, and the chain is **null recurrent**. An equivalent direct argument uses the standard first-return occupation formula: expected number of visits to \(k\) between successive visits to \(0\) is \(\pi_k/\pi_0\), so summing over all \(k\) gives infinite mean excursion length.

**4. Almost-sure zero occupation of finite blocks.** Successive return times to any fixed state form an iid renewal sequence with infinite mean. If \(\tau_i\) are its excursion lengths, then \(m^{-1}\sum_{i=1}^m\tau_i\to\infty\) almost surely: apply the ordinary strong law to \(\min(\tau_i,R)\), then let \(R\to\infty\). Consequently the number of visits to that state through time \(N\), divided by \(N\), tends to zero almost surely. Taking the countable intersection over all states gives
\[
\frac1N\#\{0\le n<N:K_n\le M\}\longrightarrow0
\quad\text{for every fixed }M\in\mathbb N.
\]
This holds for uniform initial points in any block, hence for Lebesgue-almost every \(u\ge0\), and, by the smooth change of coordinates on each compact subinterval of \([0,1)\), for Lebesgue-almost every \(x\in[0,1)\). Given any continuous \(f\) on \([0,1]\) and \(\varepsilon>0\), choose \(M\) so that \(|f(\psi(u))-f(1)|<\varepsilon\) for \(u\ge M\). The preceding zero-occupation statement bounds the limsup of the average difference by \(\varepsilon\). Letting \(\varepsilon\downarrow0\) proves the empirical weak convergence to \(\delta_1\). The endpoint is fixed by [1], so \(\delta_1\) is indeed invariant.

**5. Almost-sure density, despite concentration of time averages.** Fix an open interval \(U\) strictly within some \(B_j\). The full affine edge branches are uniformly expanding (absolute slope at least five). Their nested cylinders shrink at least geometrically, so \(U\) contains the interior of some finite admissible edge cylinder \(C\) starting in state \(j\), away from subdivision endpoints. Its conditional probability under the uniform law on \(B_j\) is a fixed \(p_C>0\).

The null-recurrent chain visits \(j\) infinitely often. Starting with any initial uniform block, choose successive hitting times of \(j\) separated by at least the length of \(C\). By the full-branch conditional-uniform property from Step 1 (also at stopping times measurable from the finite edge history), each such visit has conditional probability exactly \(p_C\) of following \(C\). The chance that the first \(m\) opportunities all fail is at most \((1-p_C)^m\), hence zero as \(m\to\infty\). Restarting after any finite number of opportunities shows infinitely many successful entries into \(U\). Applying this to a countable basis of rational intervals in \([0,\infty)\) proves that a Lebesgue-typical \(D_+\) orbit visits every such interval infinitely often. Transport by \(\psi\) makes the \(D_I\) orbit dense in \([0,1)\), and visits to arbitrarily large blocks put \(1\) in its closure. Since typical orbits also return to \(B_0\) infinitely often, they cannot converge pointwise to \(1\).

**6. Physicality and absence of absolutely continuous invariant probabilities.** The full-Lebesgue basin in Step 4 makes \(\delta_1\) a physical measure and excludes any other physical invariant probability: basins for different weak limits are disjoint. Suppose \(\nu\) were an invariant probability absolutely continuous with respect to Lebesgue measure. Its almost-everywhere empirical limits would be \(\delta_1\) as well. For every continuous \(f\), dominated convergence and invariance yield \(\int f\,d\nu=\lim_N\int N^{-1}\sum_{n<N}f(D_I^n(x))\,d\nu(x)=f(1)\). Thus \(\nu=\delta_1\), contradicting absolute continuity. This completes the proof.

## Verification
`CHECK.py` is a standalone Python-standard-library test. It reconstructs the original subdivision vertex values for all initial block indices \(0\le k\le100\), counts each target block, verifies normalized transition probabilities, exact detailed balance and stationary transfer balance, tests harmonic gambler's-ruin functions for finite ceilings \(2\le L\le100\), and enumerates all admissible block paths through four steps from four starting states. The recorded outcome is `VERIFY_OK direct_branch_counts=101 invariant_balance=101 reversible_edges=101 harmonic_ruin_boundaries=99 finite_path_depth=4`. Run `python3 CHECK.py` from the folder containing this document. These finite checks are consistency evidence only; all-state and almost-sure assertions rely on the mathematical argument in Steps 1–6.

## Relationship to prior work
The map, compactification, topological mixing, and infinite topological entropy were established by Vinod Kumar P B [1]. The new result is its exact **Lebesgue-induced block transition law**, null-recurrence classification, sigma-finite invariant density, and simultaneous full-Lebesgue dense-orbit and endpoint-empirical-limit properties. A related published finite-survivor entropy result [2] studies the **same map** and obtains a tridiagonal Perron matrix and Airy asymptotics for closed bounded-block survivor sets. Its combinatorial transition counts are compatible with Step 1, but spectral radii for compact survivor sets do not supply the stochastic normalization, null-recurrence result, invariant density, or physical time-average statements proved here. Classical irreducible-chain recurrence and renewal facts [3] supply the abstract probabilistic implications, not their concrete application or the explicit densities for this map. These comparisons do not establish universal historical priority.

## Limitations
The conclusion concerns Lebesgue-typical initial conditions and the **specific** 2026 construction, not arbitrary mixing infinite-entropy interval maps. The endpoint measure is a weak empirical limit, not the pointwise limit of typical trajectories, and the invariant absolutely continuous measure displayed here is sigma-finite of infinite mass, not a probability. No general return-time tail or mixing-rate asymptotic is claimed. The natural Markov statement applies to a random initial point uniformly distributed inside a block, not to a fixed individual point regarded as a random Markov trajectory. General countable-state ergodic methods might yield related results for other maps, and historical priority beyond inspected sources remains an acknowledged risk.

## References
1. Vinod Kumar P B, *The entropy spectra of chaotic maps of an interval*, arXiv:2610.39443v1, first publicly posted 2026-10-29, Proposition 5.2 and proof of the main theorem. https://arxiv.org/html/2610.39443v1
2. *An Airy-edge law for finite-survivor entropy in a mixing infinite-entropy interval map*, mathematical research record, 2026-11-08. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-an-airy-edge-law-for-finite-survivor-entropy-in-a-mixing-infinit--8e937cf17390/RESULT.md
3. J. R. Norris, *Markov Chains*, Cambridge University Press, 1997, chapters on recurrent chains, invariant measures and hitting times.
