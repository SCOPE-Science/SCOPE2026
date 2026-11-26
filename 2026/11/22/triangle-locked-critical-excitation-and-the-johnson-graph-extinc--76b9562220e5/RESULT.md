# Triangle-locked critical excitation and the Johnson-graph extinction dichotomy

## Finding

**Triangle-locking theorem.** Let \(G=(V,E)\) be a finite connected simple graph with at least one edge and with **every vertex belonging to a triangle**. At each vertex \(v\), run synchronous three-state Greenberg–Hastings excitation with local contact threshold \(\theta(v)=\lceil d(v)/2\rceil\). Then its only possible recurrent configurations are the all-rest equilibrium and the primitive three-periodic configurations arising from proper colorings \(c:V\to\{0,1,2\}\) satisfying
\[
 d(v)\text{ is even,}\qquad
 \#\{w\sim v:c(w)=c(v)+1\pmod3\}
 =\#\{w\sim v:c(w)=c(v)-1\pmod3\}=d(v)/2
\]
for **every** vertex \(v\). The update adds one modulo three to all colors of each such coloring. Hence every initial configuration eventually reaches rest if and only if there is no such balanced proper three-coloring. In particular, if any degree is odd, or if \(\chi(G)\ge4\), universal extinction follows. Nonzero recurrent periods other than three are impossible.

**Complete Johnson-graph application.** On the Johnson graph \(J(n,k)\), whose vertices are the \(k\)-subsets of \(\{1,\ldots,n\}\) and whose edges join subsets differing in exactly one element, assume \(n\ge2k\ge4\). Its degree is \(d=k(n-k)\), and the threshold is \(\lceil d/2\rceil\). Every initial configuration eventually becomes all-rest **except** for \((n,k)=(4,2)\). In that exceptional octahedral graph, there are exactly six nonzero recurrent configurations, forming two primitive three-cycles. These correspond to assigning the three colors bijectively to the three pairs of opposite vertices. All other Johnson graphs in the stated range have only the all-rest recurrent state. This is a classification of recurrent orbits; no uniform settling-time bound is claimed.

## Assumptions and scope

The graph is finite, undirected, loopless, without parallel edges, connected and contains an edge. Each vertex has state \(0\) (rest), \(1\) (excited) or \(2\) (refractory). In one simultaneous update, states \(1\to2\) and \(2\to0\) occur unconditionally; state \(0\) changes to \(1\) exactly when at least \(\theta(v)\) distinct neighbors are excited, and otherwise remains \(0\). The threshold can vary with vertex degree. A recurrent configuration lies on a periodic orbit of this finite deterministic map; every trajectory reaches some recurrent configuration. Vertex and color labels are distinguished, and automorphisms are not quotiented. “Every vertex belongs to a triangle” allows triangles to share vertices or edges and does not assume regularity or edge-triangle coverage.

The balanced condition is a local equitable requirement, stronger than ordinary three-colorability. All degrees must be even for any nonzero recurrent state. In the Johnson specialization \(n\ge2k\ge4\), \(J(n,k)\) is connected and every vertex lies in triangles. When \(d\) is odd, its rounded-half threshold is strictly above half degree.

## Proof

**1. Saturation of the periodic contact budget.** Consider any periodic trajectory of period \(T\ge1\), writing \(E_t\) for the vertices in state \(1\) at time \(t\), with indices modulo \(T\). Since a site excited at \(t\) is refractory at \(t+1\) and resting at \(t+2\), the sets \(E_{t-1}\) and \(E_{t+1}\) are disjoint. Every occurrence \(v\in E_{t+1}\) was resting at time \(t\) and hence had at least \(\theta(v)\) neighbors in \(E_t\). Thus
\[
 \sum_t\sum_{v\in E_t}\theta(v)
 \le \sum_t e(E_t,E_{t+1}),
\]
where \(e(A,B)\) counts edges from the disjoint sets \(A,B\). On the other hand, counting both predecessor and successor contacts of the excited events gives
\[
 2\sum_t e(E_t,E_{t+1})
 =\sum_t\sum_{v\in E_t}\bigl(|N(v)\cap E_{t-1}|+|N(v)\cap E_{t+1}|\bigr)
 \le\sum_t\sum_{v\in E_t} d(v)
 \le 2\sum_t\sum_{v\in E_t}\theta(v).
\]
All inequalities are equalities. For every excited event \((v,t)\), this implies \(d(v)=2\theta(v)\), all neighbors of \(v\) are excited at precisely one of the times \(t-1,t+1\), and exactly \(\theta(v)\) neighbors occur at each of those times. In particular, each excitation set \(E_t\) is independent.

**2. Active-vertex closure.** If the periodic orbit has at least one excitation, any vertex excited at some time has every neighbor excited at some time by the preceding saturation. Since \(G\) is connected, **every** vertex is excited at some time. Therefore all degrees in \(G\) are even; an odd-degree vertex is an immediate obstruction to a nonzero periodic orbit.

**3. A triangle forces three-step recurrence.** Suppose \(a,b,c\) form a triangle and \(a\in E_t\). The saturation rule puts \(b,c\) in \(E_{t-1}\cup E_{t+1}\). They cannot occupy the same one of these sets, since \(b\sim c\) and every \(E_s\) is independent. Relabel so that \(b\in E_{t-1}\), \(c\in E_{t+1}\). Since \(b\) is excited at \(t-1\), its neighbor \(c\) must be excited at \(t-2\) or \(t\); it cannot be excited at \(t\), one step before its known excitation at \(t+1\). Thus \(c\in E_{t-2}\). Similarly, since \(c\in E_{t+1}\), its neighbor \(b\) is excited at \(t\) or \(t+2\); its known excitation at \(t-1\) rules out \(t\), so \(b\in E_{t+2}\). Since \(b\in E_{t+2}\), its neighbor \(a\) is excited at \(t+1\) or \(t+3\), and excitation at \(t+1\) is ruled out by \(a\in E_t\). Therefore \(a\in E_{t+3}\). The same argument backward gives \(a\in E_{t-3}\). Iteration forces \(a\) to be excited at precisely every third step; additional excitations between these times are prohibited by the refractory cycle.

By assumption every vertex lies in a triangle, and by Step 2 every vertex is active. Consequently every vertex is excited at a single fixed residue class of time modulo three. Its states rotate through \(0,1,2\) without waiting, so the full configuration has least period three.

**4. The coloring bijection.** Assign the color \(c(v)\) equal to the state of \(v\) at a chosen time slice. At a time \(t\) when \(v\) is excited, its neighbors excited at \(t-1\) and \(t+1\) have colors \(2\) and \(0\), respectively, at time \(t\). Saturation gives exactly \(d(v)/2\) of each, and none of color \(1\). Changing the time slice shifts every color by the same amount modulo three, so every vertex of color \(i\) has exactly \(d(v)/2\) neighbors of each color \(i+1\) and \(i-1\). Thus \(c\) is balanced and proper. Conversely any balanced proper coloring has enough excited successor-color neighbors whenever a vertex is resting, so the map rotates the entire coloring by one modulo three; its least period is three. The all-zero state is the unique fixed point, since states 1 and 2 cannot remain fixed and no excitation is generated from all zero. Since the graph state space is finite, absence of nonzero periodic states is equivalent to universal extinction.

**5. Johnson family.** The graph \(J(n,k)\) is connected of degree \(k(n-k)\); each vertex belongs to a triangle, since one can fix \(k-1\) elements and vary the final element among three alternatives. Fixing any \((k-1)\)-subset creates a clique of size \(n-k+1\). For \(n\ge2k\ge4\), this is at least four except at \((n,k)=(4,2)\). Thus all nonexceptional graphs contain \(K_4\) and cannot have a proper three-coloring; the theorem forces extinction, independently of the degree parity. For \(J(4,2)\), the six two-subsets form three disjoint nonadjacent complementary pairs, each vertex adjacent to all four vertices of the other two pairs. A proper three-coloring must color each pair uniformly and all three pairs differently, giving exactly \(3!=6\) balanced colorings. Every vertex has two neighbors of each other color, so all six rotate in two primitive three-cycles.

## Verification

Two standalone, independently organized Python 3 programs are included. `verification/check_cycles.py` enumerates every state and constructs the entire functional digraph for six explicitly defined finite graphs: \(J(4,2)\), \(J(5,2)\), \(K_3\square C_3\), \(K_3\square C_4\), the three-triangle friendship graph, and \(K_{2,2}\). The observed primitive-cycle multiplicities (including the all-rest fixed point) are respectively \(\{1:1,3:2\}\), \(\{1:1\}\), \(\{1:1,3:4\}\), \(\{1:1\}\), \(\{1:1,3:8\}\), and \(\{1:1,4:2\}\). The second script, `verification/check_colorings.py`, independently constructs graph neighborhoods and enumerates the balanced proper three-colorings on the first five graphs, yielding respectively 6, 0, 12, 0, and 24. Recorded output files are embedded; run the scripts from any directory using only the Python standard library. These experiments corroborate the steps and illustrate both a heterogeneous-degree example and a triangle-free four-cycle boundary, but the universal claim rests on the finite-graph proof, not finite enumeration.

## Relationship to prior work

The Greenberg–Hastings update and parameterized contact thresholds originate in classical excitable-media literature [1, 2]. Fisch and Gravner [3, §§1–4] investigate one-dimensional finite and infinite interval dynamics, local periodic objects, and threshold phase behavior, rather than arbitrary finite triangle-covered graphs with degree-dependent rounded-half contact. Gravner, Lyu and Sivakoff [4, §§1–2] give a covering-space analysis for the **single-contact** three-color rules, which does not imply a multi-contact triangle-locking theorem.

A general equality-case statement [5] identifies **initially period-three** configurations on even-regular graphs with balanced proper three-colorings, but leaves other periods unclassified. Another general statement [6] proves extinction for threshold **strictly greater** than maximal induced-edge-density and does not classify the equality case. The triangle-locking argument rules out every other nonzero period at the local half-degree threshold, permits heterogeneous even degrees and gives a complete Johnson-family recurrent classification. The triangular-graph case \(J(n,2)\), including the \(J(4,2)\) exception, is also established in [7], a record with the same displayed date; no priority within that date is claimed. The triangle-locking criterion and the full \(J(n,k)\) range are the distinct scope. A cubic-line-graph result [8] counts initially three-periodic states via Tait colorings but does not characterize all possible recurrent periods.

## Limitations

No bound uniform in graph size is asserted for the time needed to reach rest or a cycle. The theorem assumes finite connectivity and **every vertex** lies in a triangle; triangle-free graphs at the half-degree threshold can support four-cycles, as the \(K_{2,2}\) check exhibits. A balanced proper coloring may fail to exist even when the graph is three-colorable; ordinary three-colorability alone is not a sufficiency test. The result does not classify full attraction basins. Unindexed historical coverage remains possible, and no independent external validation has been performed.

## References

[1] J. M. Greenberg and S. P. Hastings, *Spatial Patterns for Discrete Models of Diffusion in Excitable Media*, SIAM J. Appl. Math. 34 (1978), 515–523, https://doi.org/10.1137/0134040.

[2] R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, first public preprint 1993-03-22, https://arxiv.org/abs/patt-sol/9303002.

[3] R. Fisch and J. Gravner, *One-dimensional Deterministic Greenberg–Hastings Models*, Complex Systems 9 (1995), 329–348, https://content.wolfram.com/uploads/sites/13/2018/02/09-5-1.pdf.

[4] J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, first public 2016-10-24; later version https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf.

[5] *Half-degree rigidity and a sharp contact-threshold collapse on squared cycles*, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-half-degree-rigidity-and-a-sharp-contact-threshold-collapse-on-s--7c3fe196f42d.

[6] *A densest-subgraph threshold and finite excitation budget for three-state graph dynamics*, https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-a-densest-subgraph-threshold-and-finite-excitation-budget-for-th--352367f51e91.

[7] *Universal critical-contact extinction on triangular graphs*, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-universal-critical-contact-extinction-on-triangular-graphs--4fe1eb5b56d1.

[8] *Tait colourings as primitive-three excitation on cubic line graphs, with a constant-six seam law*, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-tait-colourings-as-primitive-three-excitation-on-cubic-line-grap--c4fb511b080a.
