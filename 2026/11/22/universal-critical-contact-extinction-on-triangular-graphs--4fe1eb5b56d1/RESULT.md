# Universal critical-contact extinction on triangular graphs

## Finding
For every integer \(n\ge5\), let \(T(n)=L(K_n)=J(n,2)\) have the unordered pairs of \(\{1,\dots,n\}\) as vertices; two pairs are adjacent exactly when they intersect. For synchronous three-state Greenberg–Hastings dynamics at contact threshold \(\theta=n-2\), **every initial state eventually becomes all resting**, although \(T(n)\) has degree \(2(n-2)\), so the threshold is exactly half its degree. At the first two orders, \(n=5,6\), every state reaches all rest by four updates, and four is sharp. The exact first-extinction histograms at times \(t=0,1,2,3,4\) are respectively
\[
(1,1023,24548,29797,3680),\qquad (1,32767,5733037,8327727,255375).
\]
For \(n=3,4\), nonzero periodic excitation instead exists: each graph has two primitive three-cycles.

## Assumptions and scope
Graphs are finite, simple, and undirected. Every vertex is simultaneously in state \(0\) (rest), \(1\) (excited), or \(2\) (refractory). The update sends \(1\mapsto2\mapsto0\). A resting vertex becomes \(1\) if and only if at least \(\theta\) **distinct** neighboring vertices are excited at that instant. For \(T(n)\), the number of vertices is \(m=\binom n2\), its degree is \(d=2(n-2)\), and \(\theta=d/2=n-2\). The extinction time is the least nonnegative integer \(t\) at which every vertex is in state \(0\); this is an absorbing state. The infinite-family result is an eventual-extinction statement, not an order-independent bound on time to extinction.

## Proof
**Critical-contact temporal identity.** Let \(G\) be any finite undirected \(2r\)-regular graph, with threshold \(r\), and suppose a trajectory is periodic with period \(p\). Write \(u_t(v)=1\) if site \(v\) is excited at time \(t\), and \(u_t(v)=0\) otherwise, taking time indices modulo \(p\). A site excited at time \(t\) cannot be excited at \(t+1\) or \(t+2\), because those states are refractory and resting, respectively. For an edge \(\{v,w\}\), call a transmission an occurrence of \(u_t(v)u_{t+1}(w)=1\) or \(u_t(w)u_{t+1}(v)=1\). No excited vertex-time event participates in more than one transmission along any fixed incident edge: two such transmissions would require the opposite endpoint to be excited two updates apart. Each transmission uses two event endpoints, so the total transmissions along that edge are at most half the number of excitation events on its two endpoints (counted with time multiplicity). Summing all edges, total transmissions are at most \(r\sum_{t,v}u_t(v)\). Yet each excited event must have at least \(r\) transmissions arriving from the preceding step, and all events occur by activation on a periodic orbit. Thus equality holds at both ends. Each excited event receives exactly \(r\) incoming transmissions, and **on every spatial edge each excitation event must be paired with exactly one event on its opposite endpoint one update earlier or later**.

For a vertex \(v\) with \(u_{t+1}(v)=1\), its \(r\) incoming transmissions give \((Au_t)(v)=r\). If \(u_{t-1}(v)=1\), that earlier excitation had exactly \(r\) neighbors excited at time \(t-2\); perfect pairing on all its \(2r\) edges forces its other \(r\) neighbors to be excited at time \(t\), so \((Au_t)(v)=r\). If both \(u_{t-1}(v)\) and \(u_{t+1}(v)\) vanish, an excited neighbor at \(t\) would have no event to pair with at \(v\), which is impossible, so \((Au_t)(v)=0\). Excitation events at a fixed vertex cannot occur two updates apart, hence the two indicators never both equal one. Consequently, for **every** \(t\),
\[
 A u_t=r(u_{t-1}+u_{t+1}). \tag{1}
\]
The argument is valid even if different vertices are active at different fractions of time; no assumption of a globally rotating coloring is used.

**Temporal spectral obstruction.** For every \(p\)-th root of unity \(\omega\), Fourier transforming (1) in time yields
\[
 A\widehat u(\omega)=r(\omega+\omega^{-1})\widehat u(\omega).
\]
Hence a nonzero temporal Fourier mode requires the adjacency eigenvalue \(2r\cos(2\pi k/p)\). The elementary algebraic-integer fact \(2\cos(2\pi k/p)\in\mathbb Z\) whenever this quantity is rational follows because the root-of-unity sum is an algebraic integer; its possible values are \(-2,-1,0,1,2\). Thus a rational cosine at rational angle belongs to \(\{-1,-1/2,0,1/2,1\}\).

**Triangular graph spectrum.** Let \(B\) be the \(n\)-by-\(\binom n2\) unsigned vertex-edge incidence matrix of \(K_n\). For \(n\ge4\), \(A_{T(n)}=B^{\mathsf T}B-2I\), while \(BB^{\mathsf T}=(n-2)I+J\). Hence the complete adjacency spectrum consists of
\[
 2(n-2),\quad n-4,\quad -2,
\]
with multiplicities \(1,n-1,\binom n2-n\), respectively. At \(r=n-2\), the three corresponding temporal cosine values are \(1\), \((n-4)/(2(n-2))\), and \(-1/(n-2)\). For every \(n\ge5\), the latter two lie strictly between \(0\) and \(1/2\), or between \(-1/2\) and \(0\), respectively. Neither can be a cosine of a rational multiple of \(2\pi\). Thus the only nonzero Fourier coefficient of \(u_t\) is the constant-in-time mode; the excitation indicator is constant in time. The refractory rule forbids a vertex being excited at consecutive instants, so that constant is zero. A periodic trajectory therefore has no excited vertices; any refractory vertex would disappear in one update, so periodicity forces every vertex to be resting. Every finite deterministic trajectory eventually becomes periodic. Therefore every trajectory eventually reaches all rest.

**Small orders.** For \(n=3,4\), a direct full-state computation gives two primitive period-three attractors in each case. The computational evidence for the two sharp four-update cutoffs for \(n=5,6\) is detailed below; these exact finite claims are distinguished from the proof of arbitrary-order eventual extinction.

## Verification
The reproducible source files `verification/functional_graph.cpp` and `verification/direct_forward.cpp` independently implement the labelled triangular graph and update rule. The first enumerates the complete functional graph and its recurrent components; the second directly updates every base-three state to extinction and tabulates the least extinction time without relying on the functional-graph recurrence. Compile with a C++17 compiler using optimization, and run each executable with arguments `5` and `6`. For orders five and six, the first method finds one fixed component, no nonzero cycle, and maximum transient depth four. The second finds exact time histograms \((1,1023,24548,29797,3680)\) and \((1,32767,5733037,8327727,255375)\), summing to \(3^{10}=59049\) and \(3^{15}=14348907\). Explicit base-three labelled witnesses `94` and `3199` attain time four, respectively. The first checker also verifies that the exceptional orders three and four have two primitive three-cycles each. These finite calculations test the stated rule but do not replace the arbitrary-order proof.

## Relationship to prior work
The Greenberg–Hastings model and its contact thresholds were studied on lattices by Durrett–Griffeath (1993) and Fisch–Gravner (1995); their spatially extended phase-diagram analyses are not the present family-specific half-degree extinction theorem. Gravner–Lyu–Sivakoff (2016, §§1–4) treat arbitrary finite graphs **at one-contact threshold** and obtain a circulation criterion; their theorem cannot imply extinction for this different threshold. A published maximum-induced-edge-density extinction criterion assumes a **strict** density inequality. Every \(T(n)\) is \(2(n-2)\)-regular, so its full-graph density equals \(n-2=\theta\), precisely the case the strict theorem leaves open. Earlier half-degree rigidity on connected regular graphs classifies only initially primitive-three periodic points; it does not rule out longer recurrent periods. A critical-spectrum proof on projective nonincidence networks and one on Paley graphs concern distinct graph spectra. No inspected prior result supplies universal extinction on all \(T(n)\) at this threshold or either full finite extinction histogram.

## Limitations
A graph's spectral intersection with allowed temporal frequencies is only a **necessary** condition for a nonzero periodic orbit; its absence is decisive here, but its presence does not imply an orbit. The theorem does not establish a uniform-in-order extinction time for \(n\ge5\), nor a complete first-extinction histogram beyond \(n=6\). The completeness of finite histograms depends on exhaustive, deterministic enumeration as described. Unindexed or inaccessible historical treatments might contain an equivalent result. Independent review of the proof and code has not been performed.

## References
1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, first public 1993-03-22, https://arxiv.org/abs/patt-sol/9303002.
2. R. Fisch and J. Gravner, *One-dimensional Deterministic Greenberg–Hastings Models*, Complex Systems 9 (1995), 329–348, https://content.wolfram.com/uploads/sites/13/2018/02/09-5-1.pdf.
3. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, first public 2016-10-24, https://arxiv.org/html/1610.07320v1.
4. *A densest-subgraph threshold and finite excitation budget for three-state graph dynamics*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-densest-subgraph-threshold-and-finite-excitation-budget-for-th--352367f51e91.
5. *Half-degree rigidity and a sharp contact-threshold collapse on squared cycles*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-half-degree-rigidity-and-a-sharp-contact-threshold-collapse-on-s--7c3fe196f42d.
