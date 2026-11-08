# A sharp spatial-symmetry onset for phase-inverting oscillations in logistic Game of Life

## Finding

Consider the exact logistic Game-of-Life update on a periodic \(H\times W\) Moore lattice with \(H,W\ge4\), and \(0<\lambda\le1\). A *phase-inverting two-level orbit* has, at one time, values \(x<y\) at the sites of an arbitrary binary spatial coloring and, at the next time, the two values interchanged at every site. Such an orbit exists **if and only if**
\[
x=\frac{1-\lambda}{2-\lambda},\quad y=\frac1{2-\lambda},\quad
k_v\in K_\lambda:=\left\{k\in\{0,1,2,3\}: \frac2{9-2k}\le\lambda\le\frac6{11-2k}\right\}\quad\text{for every site }v,
\]
where \(k_v\) is the number of Moore neighbors carrying the color opposite to that at \(v\). Each such orbit with **strict** inequalities in the displayed membership condition is locally exponentially attracting in the **entire** \(HW\)-dimensional state space; the two-step return has derivative \((1-\lambda)^2 I\). At \(\lambda=1\), the contraction is superattracting.

Two regimes separate sharply. For \(\lambda<2/3\), every phase-inverting two-level orbit must be spatially uniform. The uniform orbit exists exactly for \(2/9\le\lambda\le6/11\); hence **no phase-inverting two-level orbit exists for \(6/11<\lambda<2/3\)**. Conversely, if \(4\mid H\) or \(4\mid W\), two-wide alternating horizontal or vertical bands give spatially nonuniform primitive two-cycles for every \(2/3\le\lambda\le1\), with local exponential attraction whenever \(2/3<\lambda\le1\). Thus \(2/3\) is the exact onset of *nonuniform* phase-inverting two-level orbits on these tori, and the two families occupy disjoint coupling windows. Finally, for \(6/7<\lambda\le1\), every such orbit corresponds exactly to a binary sign vector \(\varepsilon\in\{-1,1\}^{HW}\) satisfying \(A\varepsilon=2\varepsilon\), where \(A\) is Moore adjacency (equivalently, every site has exactly three oppositely colored neighbors).

## Assumptions and scope

The state is \(s=(s_v)\in[0,1]^{HW}\), updated simultaneously. Each site has eight distinct Moore neighbors (periodic boundaries; dimensions at least four). Let \(m_v=\sum_{u\sim v}s_u\). With \(c=1-\lambda\), the updated value is \(s_v\) when \(3/2\le m_v<5/2\), \(cs_v+\lambda\) when \(5/2\le m_v\le7/2\), and \(cs_v\) otherwise. The exact untruncated continuous-state dynamics is considered. The binary coloring may be constant; a nonconstant coloring means both levels occur in space. The phase inversion swaps values at every site and is a primitive period-two orbit because \(x<y\). This is a classification *within the specified two-level phase-inverting class*, not of all periodic orbits or all attractors.

## Proof

1. **Forced temporal itinerary.** Since \(0<\lambda\le1\), the only update raising \(x<y\) is the growth operation \(G(s)=cs+\lambda\), and the only update lowering \(y>x\) is decay \(D(s)=cs\). Hence phase inversion forces \(y=G(x)\), \(x=D(y)\). Solving these two linear equations gives the displayed \(x=c/(1+c)\) and \(y=1/(1+c)\). They obey \(x+y=1\) and \(0\le x<y\le1\).

2. **Cut-degree equivalence.** At a site with value \(x\), exactly \(k_v\) of its eight neighbors have value \(y\), so its field is \(M_v=8x+k_v(y-x)=[8-(8-k_v)\lambda]/(2-\lambda)\). The growth condition is \(5/2\le M_v\le7/2\). At a site holding \(y\), the field is \(8y-k_v(y-x)=8-M_v\in[9/2,11/2]\); it therefore decays. After swapping, each site's number of opposite-colored neighbors remains \(k_v\), and the same two inequalities ensure the return. Conversely, a phase-inverting orbit necessarily satisfies the growth condition at every site. As \(M_v\ge4\) when \(k_v\ge4\), only \(k_v\le3\) is possible. For \(k\in\{0,1,2,3\}\), elementary rearrangement of \(5/2\le[8-(8-k)\lambda]/(2-\lambda)\le7/2\) gives \(2/(9-2k)\le\lambda\le6/(11-2k)\). This proves the complete equivalence, including both endpoints.

3. **Full-space local contraction.** If each growth inequality is strict, both visits have a positive uniform margin from all switching surfaces (the decay fields lie above \(9/2\)). In a sufficiently small full-dimensional neighborhood of either orbit point, every site follows exactly the same growth/decay itinerary for two steps. A low-phase site's return is \(c^2s_v+c\lambda\); a high-phase site's return is \(c^2s_v+\lambda\). Consequently the two-step Jacobian is \(c^2I\), and these affine maps contract to the displayed orbit for \(c<1\). For \(\lambda=1\) they map the neighborhood to the orbit in one return.

4. **Sharp spatial onset.** Any nonconstant coloring has a horizontally or vertically adjacent opposite-colored pair because the cardinal-edge subgraph is connected. The Moore neighborhoods of this pair contain four shared neighbors other than the two sites themselves. Each shared neighbor is opposite to exactly one endpoint, contributing a total of four to their two cut degrees; the two endpoints additionally count each other, so \(k_v+k_w\ge6\). At least one cut degree is therefore \(\ge3\). But \(k=3\) requires \(\lambda\ge2/3\), and \(k\ge4\) is impossible. This excludes nonuniform patterns below \(2/3\). For a uniform coloring \(k_v=0\), giving precisely \([2/9,6/11]\).

5. **Stripe existence and strong-coupling spectral law.** If one side is divisible by four, color successive pairs of parallel rows or columns alternately, repeating \(0011\). Every site sees exactly three neighbors of the opposite color, so the cycle exists precisely for \(2/3\le\lambda\le1\), and is locally exponentially attracting for \(\lambda>2/3\). Finally, if \(\lambda>6/7\), the bounds for \(k=0,1,2\) all fail whereas those for \(k=3\) hold strictly. Thus every site must have \(k_v=3\). Setting \(\varepsilon_v=\pm1\) by color, \((A\varepsilon)_v=(8-2k_v)\varepsilon_v=2\varepsilon_v\). Conversely any sign eigenvector with eigenvalue two has \(k_v=3\), giving exactly such an orbit. The spatial eigenvalue constraint is necessary and sufficient **for sign-valued eigenvectors**, not merely for the appearance of eigenvalue two in the spectrum.

## Verification

Run `python3 verify.py` with Python 3 standard library. The program tests 655,360 exact-rational size-four color/parameter pairs against the parameter inequalities, replays the two-step dynamics for every valid case, checks representative stripes and endpoint parameters, and verifies a nonuniform perturbation return by rational arithmetic. This finite census is a diagnostic; the proof above establishes all dimensions.

## Relationship to prior work

The logistic Game-of-Life rule and its Cantor-state construction were introduced by Ibrahimi, Gülseren and Jahangirov (2019). Their discussion derives a growth/decay period-two value pair **for the different two-neighbor logistic Rule 90** and studies stripes there; that scalar mechanism and the original Conway periodic stripe wallpaper are prior work. Akgün and colleagues (first preprint 2024, published 2026) study logistic Game-of-Life critical phases, cluster statistics and numerical thresholds near \(0.861\) and \(0.875\). The present statement does not claim a new underlying rule or new scalar growth/decay equations. It establishes an all-colorings *if-and-only-if* Moore cut-degree criterion, the disjoint sharp uniform/nonuniform windows, rigorous all-spatial-mode contraction, and the sign-eigenvector equivalence at strong coupling. The published materials examined did not explicitly contain this combined graph-theoretic classification; specialized earlier discoveries of infinite Life wallpapers remain a priority risk.

## Limitations

The theorem does not classify period-two states with more than two levels, states lacking global phase inversion, arbitrary-period orbits, basins of random initial conditions, or all perfect colorings. The nonuniform existence construction requires a torus dimension divisible by four; no assertion is made that the same onset is attained on all other sizes. Local stability at the threshold equality \(\lambda=2/3\) is not asserted. No independent audit has been performed.

## References

1. M. Ibrahimi, O. Gülseren and S. Jahangirov, “Deterministic phase transitions and self-organization in logistic cellular automata,” *Physical Review E* **100**, 042216 (2019), https://doi.org/10.1103/PhysRevE.100.042216 .
2. H. Akgün et al., “Deterministic criticality & cluster dynamics hidden in the Game of Life,” arXiv:2411.07189, first submitted 2024-11-11, https://arxiv.org/abs/2411.07189 .
3. H. Akgün et al., “Deterministic scale-invariant dynamics in a logistic Game-of-Life model,” *Communications Physics* **9**, 173 (2026), https://doi.org/10.1038/s42005-026-02568-w .
