# Two counter-rotating necklace sectors for every sequential bi-threshold cycle schedule

## Finding

Let \(n\ge3\) and give the labelled undirected cycle \(C_n\) the Boolean bi-threshold rule with activation threshold one and persistence threshold three on the **closed** neighborhood. At each sweep, visit every vertex once in an arbitrary fixed permutation order \(\pi\), updating in place, and repeat this same sweep. Write \(p(i)\) for the position of vertex \(i\) in the order, with all indices modulo \(n\). Define
\[
A=\{i:p(i)<p(i+1)\},\quad B=\{i:p(i)>p(i+1)\},\quad a=|A|,\quad b=|B|=n-a.
\]
Both \(a\) and \(b\) are positive. Let
\[
H_A=\{x\in\{0,1\}^n:x_i=x_{i+1}\ \text{for all }i\in B\},\qquad
H_B=\{x\in\{0,1\}^n:x_i=x_{i+1}\ \text{for all }i\in A\}.
\]

**Theorem.** The recurrent set of the sweep map \(F_\pi\) is \(H_A\cup H_B\). The two invariant sets are conjugate to rotations of binary words of lengths \(a\) and \(b\) in opposite directions. They intersect exactly in the two constant configurations. Consequently
\[
|\operatorname{Per}(F_\pi)|=2^a+2^b-2,\qquad
P_d:=|\{x:F_\pi^d(x)=x\}|=2^{\gcd(a,d)}+2^{\gcd(b,d)}-2\quad(d\ge1).
\]
The number of temporal orbits of least period \(d\) is
\[
N_d=\frac1d\sum_{e\mid d}\mu(d/e)\left(2^{\gcd(a,e)}+2^{\gcd(b,e)}-2\right).
\]
The possible least periods are exactly the positive divisors of \(a\) or \(b\); the maximal period is \(\max(a,b)\). These counts depend on the schedule only through \(a\), while the labelled configurations in the sectors depend on the ascent-edge set \(A\).

There are \(n\left\langle{n-1\atop a-1}\right\rangle\) permutation schedules with \(a\) ascents, where the brackets denote Eulerian numbers. Let \(A_m(z)=\sum_{j=0}^{m-1}\left\langle{m\atop j}\right\rangle z^j\) for \(m\ge1\) and \(A_0(z)=1\). For a uniformly sampled schedule \(\pi\), held fixed during the dynamics,
\[
\mathbb E_\pi |\operatorname{Per}(F_\pi)|=\frac{4A_{n-1}(2)}{(n-1)!}-2\sim\frac{2}{(\log2)^n},\qquad
\mathbb E_\pi\frac{|\operatorname{Per}(F_\pi)|}{2^n}\sim\frac{2}{(2\log2)^n}.
\]

## Assumptions and scope

The graph is the simple cycle on labelled vertices \(0,\ldots,n-1\), with edge \(i\) joining \(i\) to \(i+1\). The neighbors remain distinct for \(n=3\). If \(\ell,c,r\) are the current left, center and right bits when a vertex is visited, the local replacement is
\[
T(\ell,c,r)=\begin{cases}\ell\lor r,&c=0,\\\ell\land r,&c=1.\end{cases}
\]
An ascent is a comparison of the two visit times along the chosen cyclic direction. A configuration is periodic if a positive number of sweeps returns to it, and a temporal orbit is a cycle of distinct configurations counted once. Simultaneous updating and randomly resampled sweeps are not considered.

## Proof

**1. Domain walls and two trajectories.** Put \(w_i=x_i\oplus x_{i+1}\). At a vertex visit the pair of walls in the adjacent left and right slots evolves as
\[
(0,0)\mapsto(0,0),\quad(1,0)\mapsto(0,1),\quad
(0,1)\mapsto(1,0),\quad(1,1)\mapsto(0,0).
\]
Thus we can first draw fictitious wiring that swaps two slots at every vertex visit and then impose the rule that if both incoming slots hold a wall, they both become empty instead. The total wall count drops by two at each such collision and cannot increase.

At sweep start give slots their edge labels \(A\) and \(B\), and exchange these labels at a visit even when no walls are present. The incoming left slot at any vertex visit has label \(B\); the incoming right slot has label \(A\). To see this inductively, an incoming left edge not previously visited has its right endpoint earlier and hence starts as \(B\). If previously visited at its left endpoint, it was that endpoint's outgoing right slot and received label \(B\) there. Likewise an incoming right edge either starts as \(A\) or received label \(A\) as the outgoing left slot at its earlier right endpoint. After both endpoint visits, each edge has its original label: for an \(A\)-edge the second visit is at its right endpoint, and for a \(B\)-edge the second visit is at its left endpoint.

An \(A\)-wall moves left at every crossed vertex, and a \(B\)-wall moves right. In the absence of collisions an \(A\)-wall on edge \(i\in A\) first crosses vertex \(i\). After a leftward move the next vertex is still to be visited exactly when that new edge is in \(B\); at the first edge in \(A\) the wall stops until the next sweep. Thus each sweep moves it to the preceding \(A\)-edge, including a full turn when \(a=1\). Symmetrically the \(B\)-wiring moves a wall to the next \(B\)-edge. Collisions require walls of opposite labels.

**2. Mixed wall classes cannot recur.** Suppose both classes are occupied and that no annihilation occurs for \(ab\) sweeps. Choose one wall from each class and lift their positions to integer edge coordinates on the universal cover of the spatial cycle. After \(a\) sweeps the \(A\)-wall has made one leftward turn; after \(b\) sweeps the \(B\)-wall has made one rightward turn. Their relative displacement therefore changes by \(n(a+b)\) over \(ab\) sweeps. Without collisions each vertex update moves at most one of the chosen walls, so relative displacement changes by at most one at a time. It must hit a multiple of \(n\), which would put two walls on the same slot. This is impossible: an attempted exchange through one vertex with both slots occupied would instead annihilate both. Hence a mixed configuration must lose walls within \(ab\) sweeps. Because walls cannot be created, every orbit eventually reaches a configuration supported on a single class, and a periodic point cannot start with both classes occupied.

**3. The two rotations on bits.** In \(H_A\) there are only \(A\)-walls and thus no collisions. At each vertex visit the incoming left slot has no wall, so \(\ell=c\) and \(T(\ell,c,r)=r\). Contract the \(B\)-edges, giving \(a\) constant-bit blocks in cyclic order. In each block the visit times decrease from left to right along \(B\)-edges. Its rightmost vertex is visited before the first vertex of the next block, across an \(A\)-edge, so it copies that block's old bit. The remaining vertices of the first block are visited from right to left and propagate this bit. Thus each block gets the old bit of its next block, also when the only block is the whole cycle. For \(H_B\), reverse left and right, so each block gets the old bit of its preceding block. These rotations are bijections on their respective sectors, making all configurations in both sectors periodic. A point in both has no walls, so the intersection consists of the two fixed constants. This proves the recurrent-set description.

**4. Orbit counts.** A rotation of \(m\) cyclic positions by \(d\) has \(\gcd(m,d)\) cycles of positions, each of which must have a constant bit in a fixed word. The two sectors give the two summands in \(P_d\), less their two common fixed states. Möbius inversion of \(P_d=\sum_{e\mid d}eN_e\) gives the orbit count. For every divisor \(d\ge2\) of a rotation length, repeating the length-\(d\) word with just one 1 gives a least-period-\(d\) point. The constants have period one.

**5. Counting schedules, not orientations.** Read the visit times around the labelled vertex cycle and fix the position of the largest time, which has \(n\) possibilities. The edge entering it contributes one ascent and the edge leaving it contributes none. The other \(n-1\) visit times, read as a linear order starting immediately after the largest, therefore have \(a-1\) ascents. This gives \(n\left\langle{n-1\atop a-1}\right\rangle\) schedules. In contrast, orienting edges from earlier to later visits gives \(\binom na\) different acyclic orientations with \(a\) forward edges: any subset of \(a\) forward edges is allowed for \(1\le a\le n-1\). Each such orientation has one or more compatible schedules, and it is the schedules that are sampled uniformly here.

Reversal of all visit times interchanges \(a\) and \(b\). Hence the expectation of \(2^a+2^b\) is twice that of \(2^a\), which by the schedule law equals \(2A_{n-1}(2)/(n-1)!\). The Eulerian exponential generating function at \(2\) is
\[
\sum_{m\ge0}A_m(2)\frac{z^m}{m!}=\frac1{2-e^z}.
\]
Its unique closest pole is \(L=\log 2\); the principal part is \(1/[2(L-z)]\) and the other poles are \(L+2\pi i k\), \(k\ne0\). Subtracting the principal part leaves a function analytic in a disk of radius greater than \(L\), so \(A_{n-1}(2)/(n-1)!\sim1/(2L^n)\). Subtracting the two common fixed states and, for the fraction, dividing by \(2^n\) yields the asserted asymptotics.

## Verification

The C++ source `checks/check_all_orders.cpp` evaluates the in-place map on all bitstrings and schedules for \(3\le n\le8\), classifies recurrent states by their actual functional graph, and compares recurrent membership and the period-dividing-\(d\) counts for \(1\le d\le n\). Its saved output records 46,230 schedules and 11,017,392 schedule–state pairs. The Python source `checks/check_sampled.py` tests invariant sectors and return after the corresponding sector length, and tests for a wall loss within \(ab\) sweeps from mixed states. It covers all schedules through \(n=6\) and seeded samples for \(7\le n\le10\), with all states for each selected schedule. These checks corroborate but do not replace the all-schedule proof.

## Relationship to prior work and limitations

Macauley and Mortveit [1] relate update orders and acyclic orientations and give general cycle-equivalence principles. These do not identify the recurrent sectors or periods for this local rule. Kuhlman et al. [2] study long cycles for bi-threshold systems, including the \((1,3)\) rule. The known natural-scan classification [3] gives a single rotation sector of length \(n-1\), the case \((a,b)=(n-1,1)\), and goes further for that scan in describing basins. The cyclic-ascent schedule count also appears in the different sequential Rule 170 setting [4]; the count is a permutation statistic, not specific to this rule. The claim here is the recurrent classification for all fixed permutation schedules and its period and schedule-population consequences, not an arbitrary-schedule basin formula or a sharp transient-time bound.

## References

1. M. Macauley and H. S. Mortveit, *Cycle Equivalence of Graph Dynamical Systems*, https://arxiv.org/abs/0802.4412.
2. C. Kuhlman, H. S. Mortveit, D. Murrugarra and V. S. A. Kumar, *Bifurcations in Boolean Networks*, https://arxiv.org/abs/1108.2974.
3. *Binary-necklace attractors and triangular-run basins for sequential bi-threshold cycles*, Resultary, https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-binary-necklace-attractors-and-triangular-run-basins-for-sequent--e79a108b9794/RESULT.md.
4. *Eulerian necklace clocks and uniform basins for sequential Rule 170*, Resultary, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-eulerian-necklace-clocks-and-uniform-basins-for-sequential-rule--4683274af27b/RESULT.md.
