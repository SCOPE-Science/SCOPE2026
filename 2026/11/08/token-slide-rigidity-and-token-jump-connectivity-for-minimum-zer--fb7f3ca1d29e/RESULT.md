# Token-slide rigidity and token-jump connectivity for minimum zero-forcing sets of circular ladders

## Finding
For each integer \(n\ge5\), let \(P_n=C_n\square K_2\), with vertices \(u_i,v_i\) indexed by \(i\in\mathbb Z/n\mathbb Z\), cycle edges in each layer, and rung edges \(u_iv_i\). A zero-forcing set is a set of initially blue vertices from which the usual color-change rule (a blue vertex with exactly one white neighbor forces that neighbor blue) colors the entire graph.

Let \(\mathcal R_n^{\mathrm{TS}}\) have the *minimum* zero-forcing sets as vertices, with an edge if a single blue vertex is replaced by an adjacent unselected vertex. Let \(\mathcal R_n^{\mathrm{TJ}}\) use an unrestricted one-vertex replacement instead. Then
\[
Z(P_n)=4,\qquad |V(\mathcal R_n^{\mathrm{TS}})|=13n,
\]
\[
\mathcal R_5^{\mathrm{TS}}\cong15K_1\sqcup10P_4\sqcup2C_5,
\qquad
\mathcal R_n^{\mathrm{TS}}\cong13nK_1\quad(n\ge6).
\]
In contrast, \(\mathcal R_n^{\mathrm{TJ}}\) is connected for **every** \(n\ge5\). The zero-forcing number and complete five-orbit classification of the \(13n\) optimum states are previously known; **the claim of novelty is restricted to the exact token-slide component decomposition and the all-parameter token-jump connectivity contrast**.

## Assumptions and scope
Graphs are finite, simple, undirected and labeled by cyclic column and layer. The cycle length is an integer \(n\ge5\); the five-cycle case is essential. Zero forcing uses the standard blue-only rule, with any valid chronology or simultaneous application; these have the same eventual closure. Every intermediate state of a reconfiguration path must be a set of cardinality four that zero forces the entire graph. Token sliding requires adjacency in the original prism; token jumping does not. A component \(P_4\) denotes a four-vertex path, not a four-edge path.

Write \(U(i)=u_i\) and \(V(i)=v_i\), with indices understood modulo \(n\). Up to rotations, reflections and exchange of the layers, the five minimum-set orbits have representatives
\[
\begin{array}{ll}
A=\{u_0,u_1,u_2,u_3\},& |A^{\rm orb}|=2n,\\
B=\{u_0,u_1,u_2,v_0\},& |B^{\rm orb}|=4n,\\
C=\{u_{-2},u_0,u_1,v_0\},& |C^{\rm orb}|=4n,\\
D=\{u_0,u_1,v_0,v_1\},& |D^{\rm orb}|=n,\\
E=\{u_1,u_2,v_0,v_1\},& |E^{\rm orb}|=2n.
\end{array}
\]
Here the \(13n\) count and the orbit types are included as the independently reconstructed *input* to the new reconfiguration theorem; their earlier determination is not rebranded as new.

## Proof
**1. A self-contained recovery of the minimum-state classification.** The degree of every prism vertex is three. With fewer than three initially blue vertices no force is possible. For three blue vertices, a first force requires a blue center together with two of its neighbors. Up to prism automorphisms the triple is one of
\[
T_1=\{u_0,u_1,u_2\},\qquad T_2=\{u_0,u_1,v_0\}.
\]
Starting with \(T_1\), precisely \(v_1\) is forced, and the process stops. Starting with \(T_2\), precisely \(u_{-1}\) is forced, and it stops. Thus no three-set zero forces.

For a four-set containing \(T_1\), a fourth vertex can make the entire configuration forcing only if it is one of \(u_{-1},u_3,v_0,v_2\). If it is \(v_1\), the sole preliminary force is blocked; every other fourth vertex leaves the closure of \(T_1\) inert after its first force, since it supplies no second blue neighbor to any frontier vertex. For a four-set containing \(T_2\), the only successful fourth vertices are \(u_{-2},u_2,v_{-1},v_1\). The fourth vertex \(u_{-1}\) blocks the preliminary force; all more distant possibilities leave an inert frontier. Each of the eight displayed completions produces one of the five listed orbit types. Conversely, each listed representative can force two adjacent *entirely blue columns*: for \(A\), force \(v_1,v_2\); for \(B\), force \(u_{-1},v_1,v_{-1}\); for \(C\), force \(u_{-1},v_{-1}\); for \(D\), the first two columns are already full; and for \(E\), force \(u_0,v_2\). Two adjacent full columns propagate simultaneously in both directions along the cylinder, hence force everything. Direct rotation, reflection and layer-exchange orbit counting gives the displayed five disjoint orbit sizes for all \(n\ge5\). Therefore four is minimum and exactly these \(13n\) states occur. This recovers the known classification solely to supply verified premises for the new result.

**2. The new token-slide classification.** Each of the five canonical representatives has at most twelve proposed slides. Using the representatives above, cyclically substituting a neighbor of each selected vertex and checking against the five orbit patterns gives the following complete table (the middle column counts *all* proposed moves to unselected neighbors):

| Type | Proposed slides | Legal slides if \(n=5\) | Legal slides if \(n\ge6\) |
| --- | ---: | ---: | ---: |
| \(A\) | 6 | 2 | 0 |
| \(B\) | 6 | 1 | 0 |
| \(C\) | 8 | 2 | 0 |
| \(D\) | 4 | 0 | 0 |
| \(E\) | 6 | 0 | 0 |

This is a finite symbolic case check: all columns in a representative and its one-slide neighbors lie between offsets \(-3\) and \(4\), so for \(n\ge9\) the equality tests between the five local cyclic patterns stabilize; the cases \(n=6,7,8\) are checked separately by the same substitutions. The table is also regenerated independently by both embedded checkers. Since symmetry acts transitively on each type, for \(n\ge6\) all optimum states are isolated. For \(n=5\), the \(A\)-states form two cycles of length five (one in each layer); the \(B\)-states are twenty degree-one endpoints; the \(C\)-states have one \(B\)-neighbor and one \(C\)-neighbor, forming ten four-vertex paths; and the \(D,E\)-states are fifteen isolated vertices. Hence the stated decomposition.

**3. Token jumping connects everything.** Let \(D_i=\{u_i,u_{i+1},v_i,v_{i+1}\}\) and \(E_i=\{u_{i+1},u_{i+2},v_i,v_{i+1}\}\). Both are minimum states and
\[
D_i\longleftrightarrow E_i\longleftrightarrow D_{i+1}
\]
are two legal single-token jumps. Thus all \(D_i\) lie in one component. Each type representative reaches \(D_0\) by at most two jumps, as witnessed by
\[
\begin{array}{ll}
A\to\{u_0,u_1,u_3,v_1\}\to D_0,&
B\to D_0,\\
C\to D_0,&D=D_0,\\
E\to D_0.&
\end{array}
\]
Every intermediate set is a listed orbit type and each consecutive pair overlaps in three vertices. Applying any prism automorphism sends this path to a path from any desired minimum state to some \(D_i\). This establishes token-jump connectivity for the entire infinite family.

## Verification
Run `python3 exhaustive_check.py` and `python3 local_check.py` from the directory containing the extracted files, with Python 3.9 or later; both require only the standard library. The first program independently enumerates every four-subset for \(5\le n\le12\), computes forcing closure directly on the graph, verifies the five orbit descriptions and tabulates token-slide components. It checks no three-set forces for \(5\le n\le9\). The second generates five orbit families without enumerating all four-subsets, checks both three-seed closures and all symbolic-pattern slides for \(5\le n\le60\), and checks explicit token-jump paths. Output files `exhaustive_check_output.txt` and `local_check_output.txt` record exact executions. These finite tests are corroboration; the all-\(n\) theorem follows from the preceding local case proof and constructive token-jump paths.

## Relationship to prior work
Benson, Ferrero, Flagg, Furst, Hogben, Vasilevska and Wissman (initial public version 2015-10-08, arXiv:1510.02421) study zero forcing and graph products; their theorems concern forcing numbers rather than the prism's minimum-state reconfiguration graph. Petruk (2020) considers the zero forcing number of prism graphs (minimum cardinality is not new). Geneson, Haas and Hogben (arXiv:2009.00220, 2020-09-01) introduce minimum-zero-forcing reconfiguration under token **jumping** and study several graph classes; their analyzed families do not give the prism-specific token-slide classification or the contrast proved here. The earlier complete five-orbit classification and propagation-time enumerator for prism optimum sets already determine the vertex set of the reconfiguration graph: this work expressly **does not claim them** as novel. Computing the legal transitions and contrasting adjacent relocation with arbitrary replacement is the new assertion.

## Limitations
No exact token-jump diameter is claimed, despite finite numerical tests suggesting a simple formula. The result does not cover the triangular prism \(n=3\), the cube \(n=4\), positive-semidefinite or skew forcing, nonminimum zero-forcing sets, or intermediate configurations of larger cardinality. Historical priority is qualified: searchable sources and accessible texts do not exhaust all older or unpublished work.

## References
1. K. F. Benson, D. Ferrero, M. Flagg, V. Furst, L. Hogben, V. Vasilevska and B. Wissman, *Power domination and zero forcing*, original arXiv posting 2015-10-08, arXiv:1510.02421; revised as *Zero forcing and power domination for graph products*, https://arxiv.org/abs/1510.02421 .
2. J. Geneson, R. Haas and L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220 (2020), https://arxiv.org/abs/2009.00220 .
3. V. O. Petruk, *Zero forcing number of some families of graphs*, Mohyla Mathematical Journal 3 (2020), 48–52, DOI:10.18523/2617-70803202048-52cs, https://doi.org/10.18523/2617-70803202048-52cs .
