# Sharp logarithmic extinction clocks above the half-degree excitation threshold

## Finding
For a three-state Greenberg–Hastings process with an excitation threshold strictly greater than half of a finite graph's maximum degree, the excitation count contracts **geometrically at the sharp universal rate**. This yields an optimal logarithmic maximum extinction clock, with an explicit family of graphs attaining its leading constant.

For every integer \(t\ge1\),
\[
\theta e_{t+1}\le(\Delta-\theta)e_t.
\]
For \(0<b=\Delta-\theta<\theta\), put \(a=\theta/b\) and \(M=\lfloor \Delta n/(\Delta+\theta)\rfloor\). Every initial state reaches the all-resting configuration by time
\[
2+\min\{k\in\mathbb Z_{\ge0}:M a^{-k}<1\}.
\]
For every fixed \(\Delta/2<\theta<\Delta\), the sharp worst-case asymptotic over graphs of order \(n\) and maximum degree *at most* \(\Delta\) is
\[
\sup_{G,x}T(G,x)=\frac{\log n}{\log(\theta/(\Delta-\theta))}+O_{\Delta,\theta}(1).
\]
Here \(T(G,x)\) means the first update at which every vertex is resting. For \(\theta=\Delta\), extinction occurs by time three, uniformly in \(n\).

## Assumptions and scope
The graph is finite, simple, undirected, with \(n\ge1\) vertices and degrees at most an integer \(\Delta\ge1\). Choose an integer threshold \(\theta\) satisfying \(\Delta/2<\theta\le\Delta\). States are \(0\) (resting), \(1\) (excited), \(2\) (refractory). In one *simultaneous* update, \(1\mapsto2\), \(2\mapsto0\), and \(0\mapsto1\) iff at least \(\theta\) neighbors were excited before the update, remaining \(0\) otherwise. Let \(E_t\) be the vertices in state \(1\) after \(t\) updates and \(e_t=|E_t|\). The initial state is arbitrary, including arbitrary refractory sites. The asymptotic uses fixed integer \(\Delta,\theta\), then \(n\to\infty\); its extremum includes disconnected graphs and isolated vertices.

## Proof
**The two-step refractory exclusion.** Two excitations at the same vertex must be at least three time steps apart. Consequently \(E_{t-1}\cap E_{t+1}=\varnothing\) for every \(t\ge1\). Every vertex in \(E_t\) for \(t\ge1\) must have had at least \(\theta\) neighbors in \(E_{t-1}\); with degree at most \(\Delta\), it has at most \(b=\Delta-\theta\) neighbors in the disjoint set \(E_{t+1}\). Conversely, each vertex in \(E_{t+1}\) has at least \(\theta\) neighbors in \(E_t\). Counting edges between \(E_t\) and \(E_{t+1}\) from both sides gives \(\theta e_{t+1}\le b e_t\).

**Initial-step bound and extinction.** The sets \(E_0,E_1\) are disjoint, while counting edges between them gives \(\theta e_1\le\Delta e_0\le\Delta(n-e_1)\). Hence \(e_1\le M\), and the geometric inequality gives \(e_{k+1}\le M(b/\theta)^k\) for all integers \(k\ge0\). Once this real bound is strictly below one, the integer excitation count vanishes; one additional update clears the last refractory sites. Thus the displayed stopping-time bound follows. If \(b=0\), then \(e_2=0\) and the state is all resting at time three.

**Sharp constructions.** Fix \(0<b<\theta\) and any integer height \(h\ge1\). Build \(h+1\) vertex layers \(L_0,\ldots,L_h\), backwards from sizes \(|L_h|=1\), \(|L_{h-1}|=\theta\), and, when \(j\le h-2\), \(|L_j|=\lceil\theta|L_{j+1}|/b\rceil\). For each consecutive layer pair of sizes \(s=|L_j|\) and \(r=|L_{j+1}|\), label their vertices by residues modulo their layer size. Join each successor indexed \(i\in\{0,\ldots,r-1\}\) to the \(\theta\) distinct predecessors indexed \(\theta i+k\pmod s\), for \(0\le k<\theta\). The predecessor indices are distinct because \(s\ge\theta\); each successor has exactly \(\theta\) predecessor neighbors, while a predecessor has at most \(\lceil\theta r/s\rceil\le b\) successor neighbors. Thus every vertex has degree at most \(\theta+b=\Delta\), and there are no edges except between consecutive layers.

Initially excite every vertex of \(L_0\), leaving all other vertices resting. Induction proves \(E_t=L_t\) exactly for \(0\le t\le h\): each vertex of the next layer has \(\theta\) excited predecessors, whereas every previously visited layer sees at most \(b<\theta\) neighbors in the moving excited front; all more distant layers have no excited neighbors. After step \(h+1\) no vertex is excited; the last refractory vertices clear at step \(h+2\). Therefore this initial state has extinction time exactly \(h+2\).

Set \(a=\theta/b>1\). The recurrence \(s_j=\lceil a s_{j+1}\rceil\), with fixed terminal value \(s_{h-1}=\theta\), implies the total number of vertices is \(n_h=\Theta_{\Delta,\theta}(a^h)\). Indeed, the backward recurrence is bounded below by multiplication by \(a\) and above by multiplication by \(a\) plus one; summing its geometric envelope yields constants independent of \(h\). Hence the constructed extinction time is \(\log n_h/\log a+O_{\Delta,\theta}(1)\). For every sufficiently large \(n\), take the largest height with \(n_h\le n\) and add isolated vertices; successive \(n_h\) have bounded ratio. This proves the matching lower bound for **every** sufficiently large \(n\), not merely for a subsequence. The first-step and decay bounds give the matching upper bound, completing the asymptotic statement.

## Verification
`verification/verify_geometric_decay.py` constructs the graph and state evolution from scratch, testing 24 layered examples for \((\Delta,\theta)\) in \(\{(3,2),(5,3),(7,4),(7,5),(8,5),(9,7)\}\) at heights one through four. It verifies every degree bound and the exact travelling-front trajectory. Independently, for every ternary initial state on five additional small graphs (including all \(19,683\) states of a nine-vertex instance), it checks the claimed two-step excitation contraction. Run `python3 verification/verify_geometric_decay.py` using Python 3 with no dependencies, comparing stdout to `verification/verify_geometric_decay.out`. These computations check illustrative finite cases; the all-graph theorem is proved algebraically above.

## Relationship to prior work
The classical Greenberg–Hastings framework and threshold excitable media precede this result. A published general **maximum-induced-edge-density** theorem proves extinction when the maximum induced edge density \(\rho(G)\) is below \(\theta\), and gives an explicit total excitation-event bound. Since \(\rho(G)\le\Delta/2\), it already implies **qualitative extinction** throughout the present parameter regime; that fact is not new. Its published event budget is linear in the number of initially excited vertices and does not state the present geometric two-step contraction, sharp logarithmic worst-time constant, or matching layered sharpness examples. The new assertion is specifically the **optimal time-scale and its precise coefficient**, not a novel qualitative density obstruction.

Doba studies the threshold-one finite-graph Greenberg–Hastings map; Bello and Sivakoff study random initial states on infinite regular trees. Neither accessible text states this deterministic, arbitrary-initial-state finite-graph sharp clock. Durrett and Griffeath's archival abstract concerns excitable cellular automata on spatial lattices; its full paper was not accessible for a definitive comparison. The distinction between the known density theorem and the new sharp clock is essential; no claim is made that the problem was previously unstudied.

## Limitations
The bound is for the deterministic three-state rule and a global threshold strictly greater than half the **maximum** graph degree. The best leading constant concerns a worst case over all finite graphs with maximum degree *at most* \(\Delta\), not every fixed graph or connected graph. The layered extremizers may be disconnected and have low-degree vertices. The result does not treat the critical boundary \(2\theta=\Delta\), where oscillations can persist, nor multi-state or stochastic dynamics. The literature search cannot exclude an unindexed equivalent estimate, and the 1993 primary paper was inspected only through its archival abstract. Independent external mathematical validation is outstanding.

## References
1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002 (first public version 1993-03-22), https://arxiv.org/abs/patt-sol/9303002.
2. *A densest-subgraph threshold and finite excitation budget for three-state graph dynamics*, publicly indexed finding, 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-densest-subgraph-threshold-and-finite-excitation-budget-for-th--352367f51e91.
3. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, *Complex Systems* 27 (2018), doi:10.25088/ComplexSystems.27.2.101, https://wpmedia.wolfram.com/sites/13/2018/09/27-2-1.pdf.
4. J. Bello and D. Sivakoff, *Cyclic Cellular Automata and Greenberg–Hastings Models on Regular Trees*, arXiv:2108.06404 (2021), https://arxiv.org/abs/2108.06404.
