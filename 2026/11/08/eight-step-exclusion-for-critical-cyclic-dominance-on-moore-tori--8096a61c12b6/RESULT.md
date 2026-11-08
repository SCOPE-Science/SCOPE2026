# Eight-step exclusion for critical cyclic dominance on Moore tori

## Finding
Let \(G=(V,E)\) be any finite connected simple \(8\)-regular undirected graph containing a \(K_4\). Each vertex \(v\) carries a color \(c_t(v)\in\mathbb Z/3\mathbb Z\). At each simultaneous step, \(v\) advances by one modulo three precisely when **at least four** of its eight neighbors have the successor color \(c_t(v)+1\). Otherwise it stays put.

**Theorem.** Every periodic trajectory is either a fixed configuration or has least temporal period at least \(9\). In addition, every vertex of any nonfixed periodic trajectory changes color during each full period, and every such change has **exactly four** supporting successor-colored neighbors. In particular the period exclusion applies on **every** periodic \(H\times W\) Moore-neighborhood torus with integers \(H,W\ge3\), independently of its area or aspect ratio.

This is an exclusion theorem, **not** a claim that any nonfixed periodic orbit exists at threshold four or that all trajectories converge. The graph-wide activity and exact-four-support properties apply to any periodic orbit, regardless of its length.

## Assumptions and scope
The graph is finite, connected, simple, undirected, \(8\)-regular, and contains a complete four-vertex subgraph. No symmetry or spatial homogeneity is assumed. The phase space is finite, and “periodic” means \(c_p=c_0\) for an integer \(p\ge1\). For the \(H\times W\) torus, vertices are elements of \(\mathbb Z/H\mathbb Z\times\mathbb Z/W\mathbb Z\) and the eight neighbors are offsets in \(\{-1,0,1\}^2\setminus\{(0,0)\}\); for \(H,W\ge3\) these eight sites are distinct. Every adjacent \(2\times2\) block is a \(K_4\).

## Proof
Write \(u_v(t)\in\{0,1\}\) for the indicator that vertex \(v\) advances at time \(t\). Define, for an edge \(e=\{v,w\}\),
\[
 s_e(t)=u_v(t){\mathbf{1}}_{\{c_t(w)=c_t(v)+1\}}
 +u_w(t){\mathbf{1}}_{\{c_t(v)=c_t(w)+1\}},\qquad
 d_e(t)={\mathbf{1}}_{\{c_t(v)\ne c_t(w)\}},
\]
with color equations modulo three. The elementary **edge inequality** is
\[
 2s_e(t)\le u_v(t)+u_w(t)+d_e(t)-d_e(t+1). \tag{1}
\]
It follows by checking three colors for each endpoint and the four possible update-indicator pairs; the accompanying checker exhausts all \(36\) possibilities, with zero violations. Equation (1) is an identity about **possible** updates, so it applies in particular to those selected by the threshold rule.

Suppose a trajectory has period \(p\). Set \(U_v=\sum_{t=0}^{p-1}u_v(t)\) and \(C_e=\sum_{t=0}^{p-1}s_e(t)\). Summing (1) around the period cancels its disagreement-potential terms and yields
\[
 2C_e\le U_v+U_w.\tag{2}
\]
Each actual update receives at least four directed successor-neighbor supports, so \(\sum_e C_e\ge4\sum_v U_v\). But summing (2) over edges and using \(8\)-regularity gives
\[
 2\sum_eC_e\le 8\sum_vU_v\le2\sum_eC_e.
\]
All inequalities are equalities. Therefore \(C_e=(U_v+U_w)/2\) **for every edge**, and **every update has exactly four** successor neighbors.

The number \(U_v\) is divisible by three, since each update increments the color modulo three and the vertex returns to its initial color. If \(U_v>0\) but a neighbor \(w\) is frozen, \(U_w=0\), then as \(v\) advances, its pre-update colors are \(0,1,2\) equally often. The fixed color of \(w\) supports exactly \(U_v/3\) of \(v\)'s updates, so \(C_e=U_v/3\), contradicting the edge equality \(C_e=U_v/2\). Hence an active vertex cannot be adjacent to an inactive one. Connectedness shows that any nonfixed periodic orbit advances **every** vertex.

Now assume \(2\le p\le8\). For \(p=2\), divisibility by three forces every \(U_v=0\), so the state is fixed. For \(3\le p\le8\), activity and divisibility imply \(U_v\in\{3,6\}\) where allowed by \(p\). The equality \(2C_e=U_v+U_w\), together with integrality of \(C_e\), forbids an edge between a vertex with \(U_v=3\) and one with \(U_w=6\). By connectedness the **same** positive update count \(s\in\{3,6\}\) occurs at every vertex.

For fixed \(p,s\), the complete temporal signature of a vertex consists of its initial color \(a\in\{0,1,2\}\) and an update-time subset \(S\subseteq\{0,\ldots,p-1\}\) with \(|S|=s\). There are exactly \(3\binom ps\) signatures. A signature determines its entire color history by \(c_{t+1}=c_t+{\mathbf{1}}_{\{t\in S\}}\pmod3\). Two signatures \((a,S),(b,T)\) can occur at adjacent vertices **only if** the exact edge support count computed from their histories satisfies \(C_e=s\). No signature is compatible with itself, because two identical histories always have equal colors and hence \(C_e=0<s\).

Form the finite simple signature-compatibility graph with these vertices and edges wherever \(C_e=s\). If the original \(G\) contains \(K_4\), its four vertices must carry four **distinct**, pairwise compatible signatures. The compatibility graph would therefore contain \(K_4\). The included standard-library checker exhaustively builds every one of the following nine graphs and finds no \(K_4\):

| \(p\) | updates per vertex \(s\) | signature vertices | compatible edges |
|---:|---:|---:|---:|
| 3 | 3 | 3 | 3 |
| 4 | 3 | 12 | 24 |
| 5 | 3 | 30 | 120 |
| 6 | 3 | 60 | 444 |
| 6 | 6 | 3 | 3 |
| 7 | 3 | 105 | 1323 |
| 7 | 6 | 21 | 42 |
| 8 | 3 | 168 | 3360 |
| 8 | 6 | 84 | 372 |

The checker implements an exact bitset search for four-cliques: every potential pair of the first two clique vertices is compared against every adjacent pair in their common higher-index neighbor set. Thus there is **no** nonfixed orbit with period \(2\le p\le8\). This proves the theorem.

## Verification
Run the supplied source using a standard Python 3 interpreter:

```sh
python3 verification/check_period_gap.py
```

The deterministic checker verifies all \(36\) local edge-inequality cases, enumerates the nine signature graphs for \(3\le p\le8\), confirms their vertex/edge counts, and finds no \(K_4\) in any of them. As a boundary stress test for the method, it also detects an actual \(K_4\) in the \(p=9,s=3\) compatibility graph; this **does not** establish a realizable period-nine automaton orbit.

For comparison of thresholds, at threshold **three**, a Moore torus with both side lengths divisible by three admits the coloring \(c(i,j)=i+j\pmod3\). Each site has exactly three successor-colored neighbors, so **every** site advances at every step, producing a genuine global period-three orbit. This is a contrast between the threshold-three and threshold-four rules, not a claim that the number eight in the excluded interval is optimal.

## Relationship to prior work
Muñoz and Nuño (2026) study exactly this three-color Moore-neighborhood rule and examine its temporal periods by symmetry. They report that no oscillating attractor was observed in their threshold-four sample and that more than 99.5% of those sampled trajectories freeze; neither sampled observation proves that periods \(2\) through \(8\) are impossible on **all** torus sizes. Fisch, Gravner, and Griffeath (1991) introduce and investigate the threshold-range cyclic automata, including traveling-wave and fixation regimes. Their inspected rule and scaling sections do not state the present graph-uniform short-period obstruction. The present result relies instead on an exact edge-support budget and an exhaustive nine-case finite signature certificate.

## Limitations
The theorem does not rule out periodic orbits of period \(9\) or greater, does not prove global fixation, and does not cover graphs lacking a four-clique or having degrees other than eight. The finite signature census is exhaustive only because the edge budget reduces every potential period-\(\le8\) orbit to one of the nine cases; it is not a finite experimental extrapolation. Historical priority remains provisional against potentially unindexed specialized literature. No independent review or validation has been performed.

## References
1. F. J. Muñoz and J. C. Nuño, *Symmetry-resolved periods in a cyclic-dominance automaton: separating intrinsic from lattice-induced periodicity*, arXiv:2610.37990v1, first posted 27 October 2026. https://arxiv.org/abs/2610.37990 . In particular, model §II and threshold experiment supplement §S3.
2. R. Fisch, J. Gravner, and D. Griffeath, *Threshold-range scaling of excitable cellular automata*, Statistics and Computing 1 (1991), 23–39. https://www.math.ucdavis.edu/~gravner/papers/fgg.pdf .
