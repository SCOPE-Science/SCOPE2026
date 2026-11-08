# Chord-distance formula and bulk universality for majority two-cycles on singly chorded rings

## Finding

Let \(H_{n,d}\) be the labelled graph obtained from the cycle on vertices \(0,1,\ldots,n-1\) by adding the single edge \(\{0,d\}\), where \(n\ge4\) and \(2\le d\le n-2\). Under synchronous binary majority of **open neighbors**, with the current state retained at ties, let \(P(n,d)\) count configurations which are periodic **from time zero** with least temporal period two.

Set \(f_0=0\), \(f_1=1\) and \(f_{j+2}=f_{j+1}+f_j\). For integers \(m\ge1\), define
\[
A_m=\begin{cases}1,&m=1,\\ f_{m-1},&m\ge2,\end{cases}\qquad
D_m=\begin{cases}1,&m=1,\\ (1,1,0,-1,-1,0)_{(m-2)\bmod6},&m\ge2.\end{cases}
\]
Put \(u=d-1\) and \(v=n-d-1\). Then the exact all-distance census is
\[
\boxed{P(n,d)=2(A_uA_v+D_uD_v)
 +4\bigl(\mathbf1_{2\nmid d}A_v+\mathbf1_{2\nmid(n-d)}A_u\bigr)
 +2\mathbf1_{2\mid n}.}
\]
Every primitive two-cycle reverses both endpoints of the inserted chord. The number of distinct temporal two-orbits is \(P(n,d)/2\).

In particular, unlike a bare cycle, which has no initially primitive two-cycles at odd order and exactly two at even order, **every** singly chorded cycle admits primitive two-cycles. Write \(\varphi=(1+\sqrt5)/2\). For every sequence of allowable chord distances \(d_n\),
\[
\lim_{n\to\infty}\frac{\log P(n,d_n)}{n}=\log\varphi.
\]
If both cycle arcs become long, meaning \(\min(d_n,n-d_n)\to\infty\), the stronger chord-position-independent leading law holds:
\[
\boxed{P(n,d_n)\sim\frac25\varphi^{n-4}.}
\]
Thus the relative influence of the chord position disappears in the bulk, even though the exact counts depend on both arc lengths and their parity.

## Assumptions and scope

A configuration is a function \(x:V(H_{n,d})\to\{0,1\}\). At each step, a vertex adopts the strictly prevailing state among its graph neighbors; in a tie it retains its previous state. All updates are simultaneous. If \(M\) is this deterministic map, we count \(x\) satisfying \(M^2x=x\) and \(Mx\ne x\), not states merely attracted to a two-cycle. Vertex labels are fixed; no quotient by graph symmetries is taken. The edge \(\{0,d\}\) must be nonconsecutive and not already present. The formula is symmetric under exchanging the two arc lengths.

## Proof

**1. Propagation of a two-cycle flip.** Write \(x\) for a period-two configuration and \(y=Mx\). Every vertex other than \(0\) and \(d\) has degree two. If such a vertex changes between \(x\) and \(y\), it must have both neighbors in its new state at time zero; at time one both neighbors must have its old state, since it changes back. Therefore both neighbors also flip, with opposite temporal phase. Following this implication along either cycle arc forces *both chord endpoints to flip* and all interior vertices of that arc to flip with alternating phases. If neither interior arc contains a flipping vertex, all neighbors of a chord endpoint are stationary except possibly the other chord endpoint. A lone flipping endpoint would have three stationary inputs and could not reverse between updates, while two flipping endpoints are treated below. If no endpoint flips, the interior propagation rule rules out all flips. Hence any nontrivial two-cycle flips both endpoints, and on each arc either every interior vertex flips with alternating phase (a **flipping arc**) or every interior vertex stays stationary (a **stationary arc**).

**2. Stationary arcs.** Consider an arc with \(m\ge1\) interior vertices and flipping endpoints. If the endpoints flip in opposite phases, a stationary arc is permitted precisely when its interior word has every constant run of length at least two; the one-vertex word is also permitted (its two endpoint neighbors are always in opposite states). Indeed, at the first or last interior site, a flipping neighbor forces equality with the next stationary neighbor; at all other sites, an isolated symbol would be changed by its two neighbors. These conditions are also sufficient at both temporal phases. Let \(E_m\) be the number of permitted stationary words which start and end in zero, and \(O_m\) the number which start in zero and end in one. Colour complementation gives the other two boundary counts. Define \(A_m=E_m+O_m\), \(D_m=E_m-O_m\). At length one, \((E_1,O_1)=(1,0)\). For lengths at least two, a constant run has generating series \(q(z)=z^2/(1-z)\), whence
\[
\sum_{m\ge2}A_mz^m=\frac{q(z)}{1-q(z)}=\frac{z^2}{1-z-z^2},
\qquad
\sum_{m\ge2}D_mz^m=\frac{q(z)}{1+q(z)}=\frac{z^2}{1-z+z^2}.
\]
The first generating function gives \(A_m=f_{m-1}\). The second gives the displayed six-periodic values of \(D_m\). In particular the total number of stationary words of length \(m\) is \(2A_m\).

**3. Endpoint compatibility and disjoint cases.** First suppose the chord endpoints flip in *opposite* phases. Their common chord is therefore a correctly opposed neighbor at each time phase. If **both** arcs are stationary, at each endpoint its two stationary arc-neighbor opinions must be different: one must support each of the two opposite updates. Given boundary types on the first arc, the second must have complementary types at both ends. There are
\[
2\sum_{a,b\in\{0,1\}}N_u(a,b)N_v(1-a,1-b)
=4(E_uE_v+O_uO_v)=2(A_uA_v+D_uD_v)
\]
configurations, where the outer factor two chooses the phase at vertex zero and \(N_m(a,b)\) counts stationary words with endpoint bits \((a,b)\). If exactly one arc is flipping, it must have **odd** edge-length for its two endpoint phases to differ. The opposite stationary arc can carry any admissible word, since the flipping arc and the chord supply the two supporting neighbors at each degree-three endpoint. This yields \(4A_v\) when \(d\) is odd and \(4A_u\) when \(n-d\) is odd. If **both** arcs flip, both lengths must be odd and there are two possible phase assignments at vertex zero.

If instead the chord endpoints flip in the *same* phase, their chord neighbor does not support the change. Both incident arc neighbors must therefore flip in the opposite phase. Hence both arcs flip entirely, both arc lengths are even, and there are exactly two configurations. These last two all-flipping alternatives (both odd with opposed chord-endpoint phases, or both even with equal phases) are disjoint and exist exactly when \(n\) is even. Summing the four disjoint possibilities establishes the formula. The flip-propagation and stationary-word conditions are necessary and sufficient, so the count is exact.

**4. Oscillations and entropy.** For even \(n\), the final term of the formula provides two configurations. For odd \(n\), precisely one of the arcs has odd length and the corresponding mixed term is positive. On a bare cycle, propagation has no chord endpoint at which to stop, so a flipping site forces an alternating flip around the whole cycle; this yields exactly two configurations at even length, none at odd length.

For \(m\ge2\), \(A_m=f_{m-1}=\varphi^{m-1}/\sqrt5+O(\varphi^{-m})\), whereas \(|D_m|\le1\); the special value \(A_1=D_1=1\) is bounded. These facts give absolute positive constants \(c,C\) such that \(c\varphi^n\le P(n,d)\le C\varphi^n\) uniformly over admissible \(d\) and all sufficiently large \(n\): the product \(A_uA_v\) is uniformly comparable to \(\varphi^{u+v-2}=\varphi^{n-4}\), while \(|D_uD_v|\le1\) and all remaining terms are nonnegative. This proves the entropy law. If both \(u\) and \(v\) diverge, then \(2A_uA_v\sim(2/5)\varphi^{n-4}\), while the bounded correction and the two mixed-arc terms are of smaller order. This proves the bulk law.

## Verification

The standalone program `verify_exhaustive.py` independently implements synchronous neighbor voting, exhaustively explores all initial binary configurations for every \(5\le n\le16\) and \(2\le d\le\lfloor n/2\rfloor\), and additionally asserts that both chord endpoints flip for every primitive-two state. It checks 48 different chorded graphs and 830,112 initial states, with no discrepancies. The four-vertex case \((n,d)=(4,2)\) was also evaluated directly and gives six states.

The independently written `verify_runs.py` enumerates stationary interior words up to length seventeen, verifies their boundary statistics and the Fibonacci/six-residue formulas, and tests both algebraic coefficient recurrences through degree 100. Each program uses only Python's standard library and writes a deterministic text output included with this result. These finite checks corroborate, but do not substitute for, the proof for all lengths.

Selected exact populations \((n,d,P(n,d))\) are \((5,2,8)\), \((6,2,6)\), \((6,3,14)\), \((9,3,16)\), \((10,3,34)\), \((10,5,26)\), \((12,3,86)\), \((12,6,22)\), \((16,3,538)\), and \((16,8,130)\).

## Relationship to prior work

Goles and Olivos (1980, 1981) establish the eventual period-one/period-two restriction for symmetric threshold systems; this restriction does not enumerate period-two states on a graph with one exceptional edge. Benjamini, Chan, O'Donnell, Tamuz and Tan (2014 preprint) study majority dynamics and convergence on transitive and random graphs; their results likewise concern eventual behavior rather than the exact two-parameter cycle count. Flocchini (2008) surveys majority-based contagion and dynamo problems on regularly *multiply* chorded rings, particularly irreversible infection; the single-chord finite graph, reversible initial two-cycles and all-chord-distance formula are different objects and questions.

An earlier exact one-leaf majority-cycle census concerns a pendant vertex rather than a chord; the inserted edge here changes the degrees of **two** existing vertices, makes both endpoints flip in every nontrivial two-cycle, and produces a two-arc interaction formula and universal bulk placement law. Exact wheel and fan studies have a universal hub and do not subsume this chorded-cycle theorem. The local run-count method is elementary, but the stated full parameter classification is not an immediate specialization of any of these cited results.

## Limitations

Only configurations initially in exact temporal period two are counted; attraction basins, stabilization times and fixed-state counts are not determined. The bulk coefficient requires both arc lengths to diverge; fixed-distance chords can have different leading constants. The public abstract of the original 1980 threshold paper was examined, but its complete full text was not obtained, so an unindexed equivalent classification cannot be categorically excluded. The result has no independent external validation.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189. DOI: 10.1016/0012-365X(80)90121-1.
2. E. Goles and J. Olivos, *Comportement périodique des fonctions à seuil binaires et applications*, Discrete Applied Mathematics 3 (1981), 93–105. DOI: 10.1016/0166-218X(81)90034-2.
3. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, first preprint public May 11, 2014, arXiv:1405.2486.
4. P. Flocchini, *Contamination and Decontamination in Majority-Based Systems*, Journal of Cellular Automata (2008), publicly accessible author manuscript, https://site.uottawa.ca/~flocchin/Papers/majority.pdf.
