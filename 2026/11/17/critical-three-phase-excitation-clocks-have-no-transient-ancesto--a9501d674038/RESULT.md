# Critical three-phase excitation clocks have no transient ancestors on even-regular graphs

## Finding

Consider the synchronous three-state Greenberg–Hastings map \(F_\theta\) on any finite simple graph, with state \(0\) resting, \(1\) excited, and \(2\) refractory. At every vertex, \(1\mapsto2\mapsto0\); state \(0\) advances to \(1\) precisely when at least \(\theta\ge1\) adjacent vertices are excited. A **full three-phase clock** is a coloring \(y:V\to\{0,1,2\}\) such that \(F_\theta(y)=y+1\pmod 3\) and hence \(F_\theta^3(y)=y\).

**Exact inverse law.** For every full clock \(y\), define \(d_2^y(v)=|\{u\in N(v):y(u)=2\}|\). Its total number of one-step predecessors, including configurations outside the clock, is
\[
\left|F_\theta^{-1}(\{y\})\right|=2^{b_\theta(y)},\qquad b_\theta(y)=\bigl|\{v:y(v)=0,\ d_2^y(v)<\theta\}\bigr|.
\]

**Critical-threshold isolation theorem.** If \(G\) is finite, connected, simple and \(2r\)-regular with integer \(r\ge1\), and \(\theta=r\), then every primitive three-periodic configuration is a full clock having exactly \(r\) neighbors in each of its two other phase classes. Each of its three configurations has exactly one one-step predecessor, namely its preceding clock phase. Consequently, **no configuration outside the union of primitive three-cycles ever reaches a primitive three-cycle**. In particular, with uniformly independent initial states, the probability of eventual primitive period three equals the number of initially primitive-three configurations divided by \(3^{|V|}\); this statement does not exclude attractors of other periods.

The contact threshold is genuinely relevant to inverse branching. On \(C_6^2\) at threshold \(1\), the clock \(y=(0,0,0,1,1,2)\) has the two distinct immediate predecessors \(p=(2,2,2,0,0,1)\) and \(q=(2,2,0,0,0,1)\), with \(q\) outside that three-cycle. At the critical threshold \(2\), such extra ancestry is impossible for every three-cycle.

As a concrete finite-ring specialization, for \(G=C_n^2\), \(n\ge5\), at \(\theta=2\), the previously established initial clock census yields the exact eventual-period-three probability \(6/3^n\) when \(3\mid n\), and \(0\) otherwise. The initial clock census itself is not claimed as new here.

## Assumptions and scope

All graphs are finite, undirected, loopless and simple. The inverse formula needs no regularity or connectivity, but assumes \(\theta\ge1\) and a full clock \(y\). The isolation assertion assumes connected \(2r\)-regular \(G\), \(r\ge1\), \(\theta=r\), with three states and synchronous open-neighborhood counting. A primitive period-three configuration is a state \(x\) satisfying \(F^3(x)=x\) but not \(F(x)=x\). The **basin** of a periodic orbit is the set of all finite configurations whose forward orbit eventually enters that orbit. All counts concern labelled configurations, without dividing by automorphisms.

## Proof

**1. Exact inverse law for a full clock.** Fix a target coloring \(y\) that advances by one modulo three under the dynamics. If \(F_\theta(x)=y\), then every vertex with target state \(2\) must previously have state \(1\), and every vertex with target state \(1\) must previously have state \(0\). At every target-\(0\) vertex, the previous state can only be \(2\) (automatic refractory advance) or \(0\) (remaining rested). Thus the set of excited sites in \(x\) is **fixed**, equal to \(\{v:y(v)=2\}\). A target-\(0\) vertex can therefore choose previous state \(0\) exactly when its number \(d_2^y(v)\) of neighbors with target state \(2\) is strictly smaller than \(\theta\). Otherwise it is forced to state \(2\). These choices are independent, because the excited-source set never changes with them. This proves the claimed power of two; in particular the clock's own preceding phase is one permitted predecessor.

**2. Phase-class saturation at half-degree contact.** Suppose \(G\) is connected and \(2r\)-regular, \(\theta=r\), and \(y\) has primitive period three. The allowed local time transitions imply that each vertex either remains \(0\) at all three times or visits the phases \(0,1,2\) cyclically. Indeed a vertex that ever reaches \(1\) must traverse \(1\to2\to0\), and closure at period three forces \(0\to1\); all other vertices remain rested.

Let \(A_i\) consist of vertices with state \(i\) at time zero that cycle through all three states, and let \(S\) be permanently silent vertices. Put \(A=A_0\cup A_1\cup A_2\). For \(i\) modulo three, each vertex in \(A_i\) must have at least \(r\) neighbors in \(A_{i+1}\) at the time it advances from \(0\) to \(1\). Therefore
\[
 E(A_0,A_1)+E(A_1,A_2)+E(A_2,A_0)\ge r|A|,
\]
where \(E(X,Y)\) denotes the number of undirected edges between disjoint sets \(X,Y\). But the three edge sets on the left are disjoint internal edges of \(G[A]\), so their total is at most \(|E(G[A])|\le r|A|\), the latter from the \(2r\)-regularity of \(G\). All inequalities are equalities. Consequently no active vertex has a neighbor in \(S\) or in its own phase class. Since the periodic configuration is nonconstant in time, \(A\ne\varnothing\); connectedness forces \(S=\varnothing\). Every vertex has precisely \(r\) neighbors in its succeeding phase class, and by degree saturation precisely \(r\) in the preceding phase class. Thus \(y\) is a full clock and is phase-balanced.

**3. Isolation.** In any full clock \(y\) at critical threshold, a vertex with \(y(v)=0\) has exactly \(r\) neighbors with \(y(u)=2\). Hence \(b_r(y)=0\) in the inverse formula. Its one-step predecessor is unique and is the earlier phase \(y-1\pmod3\). This is true for every phase on the cycle. If a state outside the cycle entered it after positive time, the final pre-entry step would give an additional predecessor of a clock phase, contradiction. The complete attraction basin is therefore the orbit itself, proving the uniform-start probability identity.

**4. Strictly subcritical boundary witness.** On \(C_6^2\), use indices \(0,\ldots,5\) modulo six, with edges at cyclic offsets \(\pm1,\pm2\). Under \(\theta=1\), \(y=(0,0,0,1,1,2)\) has a successor-phase neighbor at each vertex and is a full clock. The target-\(0\) vertex at index \(2\) has no target-\(2\) neighbor, while indices \(0,1\) do. The inverse formula gives exactly two predecessors, \(p\) and \(q\) displayed above; direct substitution confirms \(F_1(p)=F_1(q)=y\), and \(q\) is not in the three-phase orbit.

## Verification

The provided standard-library program `verify_critical_clocks.py` exhaustively enumerates all \(3^n\) states on each of several small critical examples, builds all one-step indegrees, and checks the inverse formula for every full clock. It also checks balance, the uniqueness of critical clock predecessors, and the explicit subcritical witness. Tested graph families include cycles, squared cycles, complete graphs, and the octahedral complete tripartite graph. Its captured output is `verify_critical_clocks.txt`. The infinite-family theorem rests on the preceding direct proof, not on finite enumeration.

## Relationship to prior work

Durrett–Griffeath (1993) introduced and studied spatial excitation models including three-state Greenberg–Hastings rules. Fisch–Gravner (1995), especially Sections 1–3, characterize stable periodic structures and various infinite one-dimensional regimes, not this exact finite-graph inverse-fiber formula or graph-wide basin isolation. Kesseböhmer–Rademacher–Ulbrich (2019 preprint, 2021 journal) examine the non-wandering set and preimages of pulse subshifts for the nearest-neighbor infinite one-dimensional automaton, not an arbitrary connected \(2r\)-regular graph at contact threshold \(r\). Their invertibility of particular pulse subshifts does not entail uniqueness of *all* ambient preimages of finite-graph three-cycles.

An earlier recorded classification identifies the balanced three-phase configurations on connected \(2r\)-regular graphs at threshold \(r\), and gives six such states on squared cycles when the circumference is divisible by three. Those prior results alone count **initially periodic** configurations. The additional question answered here is whether a nonperiodic configuration can ever *enter* them, together with a general exact inverse-fiber law and a concrete sharp failure below the critical threshold. Previously reported basin enumerations on complete bipartite and tripartite graphs do not imply the arbitrary-regular-graph statement.

## Limitations

No assertion is made about extinction rates, maximal transient times, attraction to periods other than three, general threshold-to-period phase diagrams, or noncritical graphs except for the displayed exact inverse formula. The earlier 1993 source was available only as abstract and bibliographic record in this check, so possible historical equivalences beyond the accessible material remain a residual priority risk. Independent audit has not been performed.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, original arXiv submission dated 1993-03-22, `patt-sol/9303002`, https://arxiv.org/abs/patt-sol/9303002.
2. R. Fisch and J. Gravner, *One-dimensional Deterministic Greenberg–Hastings Models*, *Complex Systems* 9 (1995), 329–348, https://content.wolfram.com/sites/13/2018/02/09-5-1.pdf.
3. M. Kesseböhmer, J. D. M. Rademacher and D. Ulbrich, *Dynamics and topological entropy of 1D Greenberg–Hastings cellular automata*, first arXiv submission 2019-03-06, `1903.02459`; *Ergodic Theory and Dynamical Systems* 41 (2021), 1397–1430, https://arxiv.org/abs/1903.02459.
