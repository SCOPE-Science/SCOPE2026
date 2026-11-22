# Two counter-rotating necklace sectors for every sequential bi-threshold cycle schedule

## Finding

Let \(n\ge3\) and give the labelled undirected cycle \(C_n\) the Boolean bi-threshold rule with activation threshold one and persistence threshold three on the **closed** neighborhood. At each sweep, visit every vertex once in an arbitrary fixed permutation order \(\pi\), in place, and repeat this same sweep indefinitely. Write \(p(i)\) for the position of vertex \(i\) in this order, with all indices modulo \(n\). Set

\[
A=\{i:p(i)<p(i+1)\},\quad B=\{i:p(i)>p(i+1)\},\quad a=|A|,\quad b=|B|=n-a.
\]

Both \(a\) and \(b\) are strictly positive. Define the two families

\[
H_A=\{x\in\{0,1\}^n:x_i=x_{i+1}\text{ for every }i\in B\},\qquad
H_B=\{x\in\{0,1\}^n:x_i=x_{i+1}\text{ for every }i\in A\}.
\]

**Theorem.** The entire recurrent set of the sweep map \(F_\pi\) is \(H_A\cup H_B\). Each of these two invariant sets is conjugate to binary rotation of length \(a\) or \(b\), respectively. They intersect exactly in the two constant configurations. In particular,

\[
|\operatorname{Per}(F_\pi)|=2^a+2^b-2,
\]

and, for **every** positive integer \(d\),

\[
P_d:=|\{x:F_\pi^d(x)=x\}|=2^{\gcd(a,d)}+2^{\gcd(b,d)}-2.
\]

Thus the exact number of primitive temporal \(d\)-cycle **orbits** is

\[
N_d=\frac1d\sum_{e\mid d}\mu(d/e)\left(2^{\gcd(a,e)}+2^{\gcd(b,e)}-2\right).
\]

The possible least temporal periods are exactly the positive divisors of \(a\) or \(b\), and the largest possible period is \(\max(a,b)\). The classification depends on a schedule only through its cyclic ascent count, although the labelled recurrent configurations themselves depend on the edge positions.

There are exactly \(n\left\langle {n-1\atop a-1}\right\rangle\) labelled schedules with a given \(a\), where brackets denote Eulerian numbers. Let \(A_m(z)=\sum_{j=0}^{m-1}\left\langle{m\atop j}\right\rangle z^j\) for \(m\ge1\) and \(A_0(z)=1\). For uniformly random \(\pi\),

\[
\mathbb E_\pi|\operatorname{Per}(F_\pi)|
=\frac{4A_{n-1}(2)}{(n-1)!}-2
\sim\frac{2}{(\log2)^n},\qquad
\mathbb E_\pi\frac{|\operatorname{Per}(F_\pi)|}{2^n}
\sim\frac2{(2\log2)^n}.
\]

This is a **recurrent-set and order-statistics classification**, not a formula for all transient entrance times or individual attraction basins under arbitrary orders.

## Assumptions and scope

The graph is the simple cycle with labelled vertices \(0,1,\ldots,n-1\), edges from \(i\) to \(i+1\pmod n\), and no loops. At the vertex being updated, let \(\ell,c,r\in\{0,1\}\) be the **current** left, center and right bits (some neighbors may already have been updated during the sweep). The local replacement is

\[
T(\ell,c,r)=\begin{cases}\ell\lor r,&c=0,\\\ell\land r,&c=1.\end{cases}
\]

Thus an inactive vertex activates if at least one neighbor is active, while an active vertex persists exactly if both neighbors are active. For \(n=3\), the two neighbors are distinct. Neither simultaneous updating nor a randomly resampled order is considered.

An edge \(i\) is the pair \(\{i,i+1\}\). The adjective 'ascent' concerns **visit times** \(p(i)\), not the numerical vertex labels. A configuration is *periodic* if some positive iterate returns to it; a primitive temporal orbit is one entire cycle of distinct states, counted once.

## Proof

**1. Domain-wall transfer and annihilation.** Write the wall on edge \(i\) as \(w_i=x_i\oplus x_{i+1}\). Consider the pair of walls adjacent to a vertex about to update, in the order left, right. Direct substitution into \(T\) gives exactly

\[
(0,0)\mapsto(0,0),\quad(1,0)\mapsto(0,1),\quad
(0,1)\mapsto(1,0),\quad(1,1)\mapsto(0,0).
\]

In other words, walls traverse the vertex as if the two incident edge slots were exchanged, **except** that two occupied slots mutually annihilate. No update can create walls; every collision lowers the total wall number by two.

To label the two classes of possible wall trajectories, temporarily ignore annihilation and draw the *swap wiring* through every vertex visit. At the start of a sweep, label the edge slots in \(A\) by \(A\), those in \(B\) by \(B\). Whenever either endpoint is visited, its two incident slot labels exchange; the claim that the labels reaching a vertex from its **left** and **right** at that visit are respectively \(B\) and \(A\) follows by considering its two incident edges separately: an edge whose left endpoint is visited first starts as \(A\), then changes label at that first visit, whereas an edge whose right endpoint is visited first starts as \(B\), then changes label. Hence at each local update the entering left edge slot has label \(B\), and the entering right slot has label \(A\). All labels return to their original edge classes after a full sweep, since each edge exchanges labels at both endpoints.

Thus occupied \(A\)-slots are transported **leftward** and occupied \(B\)-slots **rightward**, and a wall collision can only happen between opposite classes. The action of a complete sweep on the disjoint \(A\)-slots is a one-position cyclic rotation of these \(a\) slots, with the opposite cyclic rotation on the \(b\) disjoint \(B\)-slots. The latter assertion can also be seen by following an occupied slot through the updates: it travels along consecutive edges until it reaches the next slot of its own class, then stops for that sweep.

**2. Mixed wall classes cannot recur.** Suppose a configuration has at least one wall in each class. As long as no collision occurs, the total number of each class stays positive and the swap wiring transports the two classes in opposite directions. Choose one particle from each class and lift their edge positions to the universal cover of the spatial circle. After \(ab\) complete sweeps, the \(A\)-particle has travelled \(b\) full spatial turns left and the \(B\)-particle \(a\) full turns right. Their relative displacement changes by \(n(a+b)\) edge steps. On a circle, two particles occupying different slots cannot exchange their cyclic order or acquire a nonzero relative winding through a sequence of single-vertex swaps without meeting in one such vertex event: it would force both incoming slots of that event to be occupied. Such an event is precisely a collision. Consequently any interval of \(ab\) sweeps that begins with both classes occupied contains an annihilation. Since there are at most \(n\) walls and annihilation strictly decreases their number, after finitely many sweeps every orbit has walls of at most one class. This argument proves eventual entry, without asserting an optimal transient bound.

**3. The two rotation sectors and their intersection.** In \(H_A\) there are no \(B\)-walls, and hence no annihilations. Contract the \(B\)-edges to obtain exactly \(a\) constant-bit blocks in cyclic order. At the vertex updates, the absence of a left \(B\)-wall reduces the local rule to copying the current right-neighbor bit, so the sweep cyclically shifts the block values once. Similarly, absence of \(A\)-walls reduces the local rule to copying the left-neighbor bit, rotating the \(b\) blocks of \(H_B\) in the opposite orientation. Both restricted maps are bijective, so every configuration in each sector is already periodic. The sectors meet iff no edge carries a wall, i.e. at the all-zero and all-one configurations, both fixed. Since a periodic point cannot lose walls and later recover them, step 2 excludes periodic points outside these sectors. The union is therefore the full recurrent set.

**4. Exact orbit counts.** A binary word of cyclic length \(m\) fixed by its \(d\)-fold rotation is constant on the \(\gcd(m,d)\) rotation classes and has \(2^{\gcd(m,d)}\) choices. Apply this independently to the length-\(a\) and length-\(b\) sector rotations, subtracting their two common fixed states. This yields \(P_d\) and \(|\operatorname{Per}(F_\pi)|\). Möbius inversion of \(P_d=\sum_{e\mid d}eN_e\) yields \(N_d\). A primitive binary word of every length \(d\ge2\) exists (for example, one 1 followed by \(d-1\) zeros), giving every divisor of either sector length; the only period-one words are the two common constants.

**5. Order frequencies and the asymptotic.** For each permutation, rotate its sequence of visited labels cyclically to put vertex \(0\) first. This rotation does not affect the cyclic ascent-edge count, since cyclic comparisons of rank positions have the same number of ascents as comparisons in a single linear order after choosing the vertex visited earliest. Equivalently, the number of acyclic orientations of \(C_n\) with \(a\) ascent edges is \(n\left\langle{n-1\atop a-1}\right\rangle\); each can be realized by the corresponding number of compatible visit orders. A direct counting argument is to fix the position of the numerically largest time stamp on the circular ordering of vertex indices: there are \(n\) choices, and after cutting there, the other \(n-1\) distinct time stamps have \(a-1\) ascents. Thus exactly \(n\left\langle{n-1\atop a-1}\right\rangle\) permutations have ascent count \(a\).

The Eulerian polynomials satisfy

\[
\sum_{m\ge0}A_m(2)\frac{z^m}{m!}=\frac1{2-e^z}.
\]

The expected sector population over the schedules is \(4A_{n-1}(2)/(n-1)!\), before subtracting the duplicated constant states. The generating function has a unique smallest-modulus singularity at \(z=\log2\), a simple pole with principal part \(1/[2(\log2-z)]\). Its other poles are \(\log2+2\pi i k\) for nonzero integers \(k\), which are further away. Therefore \(A_{n-1}(2)/(n-1)!\sim 1/[2(\log2)^n]\), proving the asserted expectations.

## Verification

The included `checks/check_all_orders.cpp` independently computes the actual in-place bi-threshold map on every bitstring, for all \(n!\) update permutations and \(3\le n\le8\). It decomposes each finite functional graph and checks periodic-state membership, recurrent counts and period-dividing-\(d\) populations for every \(1\le d\le n\). This is 46,230 permutation schedules and 11,017,392 schedule-state pairs.

The separately implemented `checks/check_sampled.py` checks direct updates against both one-class rotation properties and the mixed-wall annihilation bound for all permutations through \(n=6\), plus specified random samples for \(7\le n\le10\), using exhaustive states for each sampled order. Results from both scripts are included. These checks are finite corroboration; the proof above, not extrapolation from experiments, establishes the theorem for all \(n\).

## Relationship to prior work

Macauley and Mortveit's *Cycle Equivalence of Graph Dynamical Systems* (first deposited February 29, 2008) proves order-equivalence principles for sequential systems and counts orientation classes on cycles, but does not classify this concrete threshold rule's attractor sectors or the complete period distribution as a function of ascents. Kuhlman, Mortveit, Murrugarra and Kumar's *Bifurcations in Boolean Networks* (first arXiv deposited August 15, 2011) studies the exact \((1,3)\) rule and exhibits long cycles for a natural scanning order, but does not provide the arbitrary-order recurrent-set decomposition. A published single-scan classification, *Binary-necklace attractors and triangular-run basins for sequential bi-threshold cycles*, determines the binary necklace and basin laws for the specific order \(0,1,\ldots,n-1\); that result corresponds here to \((a,b)=(n-1,1)\), so it does not entail the two-sector formula for general permutations.

The exact cyclic ascent-count law and its Eulerian average make the new result more than a relabelling of the natural-order classification. The cycle-equivalence results constrain how update orders may be related, but do not alone supply the present explicit invariant-set and period formulas.

## Limitations

Only sequential in-place updating on simple cycles, with one fixed permutation repeated, and the exact closed-neighborhood thresholds \((1,3)\), are considered. The complete transient-depth census and each individual attraction basin for arbitrary permutations are not classified here. The proof provides a finite-time eventual-entry mechanism but not a claimed sharp entry bound. Prior-work searches and accessible full-text comparisons cannot rule out an undiscovered equivalent formulation; the result has no independent external mathematical audit.

## References

1. M. Macauley and H. S. Mortveit, *Cycle Equivalence of Graph Dynamical Systems*, first public arXiv deposit 2008-02-29. https://arxiv.org/abs/0802.4412
2. C. Kuhlman, H. Mortveit, D. Murrugarra and V. S. A. Kumar, *Bifurcations in Boolean Networks*, first public arXiv deposit 2011-08-15. https://arxiv.org/abs/1108.2974
3. *Binary-necklace attractors and triangular-run basins for sequential bi-threshold cycles*, published 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-binary-necklace-attractors-and-triangular-run-basins-for-sequent--e79a108b9794
