# The seven-vertex onset of distance-first failure in two-offer random walks

## Finding

Let \(G\) be a finite connected simple unweighted graph, let \(t\) be a target, and consider a discrete-time walker which at every non-target vertex receives two independent uniform neighbor offers **with replacement** and chooses one. The objective is to minimize the expected number of steps until first reaching \(t\), over all history-dependent randomized controls. A *distance-first* strategy must choose a neighbor with smaller graph distance to \(t\) whenever the two offered neighbors have unequal distances; it may use any optimal tie rule when their distances agree.

**Theorem.** Every connected graph of order at most six admits an optimal distance-first target-hitting strategy for every target. Seven is the smallest order for which the distance-first constraint can be strictly suboptimal. More precisely, take a cycle \(0-1-2-3-4-0\), attach \(k\) distinct leaves only to vertex \(0\), and set target \(t=1\). For every integer \(k\ge2\), at vertex \(4\) the optimal choice when offered the pair \(\{0,3\}\) is vertex \(3\), although \(d(0,1)=1<d(3,1)=2\). For \(k=0,1\), some distance-first policy is optimal. The sharp preference gap for \(k\ge2\) is
\[
V_k(0)-V_k(3)=\frac{4(18k^2-10k-51)}{134k+147}>0,
\]
where \(V_k(v)\) is the optimal mean target-hitting time from \(v\). In the first failing instance, \(k=2\) (seven vertices), the gap is exactly \(4/415\). The failure persists for every larger pendant load \(k\).

## Assumptions and scope

All graphs are finite, connected, simple and loopless; offered neighbors are sampled independently and uniformly with repetition. Step costs are one. The controller knows the graph, the current vertex, the target, and both offers. Policies may be randomized and history-dependent. At the target the process stops. A pair with different distances creates a compulsory distance-first preference; ties are unrestricted. The graph order includes the target and all pendant vertices.

## Proof

**1. Optimal-value equation.** For a graph \(G\), the optimal value \(V(t)=0\) satisfies, at every \(v\ne t\),
\[
V(v)=1+\frac{1}{\deg(v)^2}\sum_{u,w\in N(v)}\min\{V(u),V(w)\}.
\tag{1}
\]
For any control and any current vertex, there is a fixed positive probability (uniform in the control) that both offers force the walk to follow a shortest path to the target in at most \(|V(G)|-1\) steps. Applying this argument in successive blocks gives uniformly finite mean hitting times. First-step conditioning and dynamic programming therefore establish (1); choosing the smaller continuation value is optimal. Conversely, any finite nonnegative solution of (1) gives the true optimal value: under any control, conditional expected next value is at least the Bellman minimum, while under the value-minimizing stationary control it equals the minimum. The bounded-value stopped-martingale argument (or finite-horizon truncation followed by the uniform geometric hitting bound) proves both inequalities and uniqueness.

**2. Exact calculation on the decorated five-cycle.** Write \(A=V_k(0)\), \(B=V_k(2)\), \(C=V_k(3)\), and \(D=V_k(4)\). A pendant leaf has value \(A+1\). Consider the preference ordering which chooses \(3\) over \(0\) at vertex \(4\) and chooses \(4\) over a leaf whenever both are offered at vertex \(0\). The Bellman equations for that ordering are
\[
\begin{aligned}
B&=1+C/4,\\
C&=1+3B/4+D/4,\\
D&=1+3C/4+A/4,\\
A&=1+\frac{2k+1}{(k+2)^2}D+\frac{k^2}{(k+2)^2}(A+1).
\end{aligned}
\tag{2}
\]
In the last equation, the probability of choosing the target neighbor is \((2k+3)/(k+2)^2\); the probability of choosing vertex \(4\) is \((2k+1)/(k+2)^2\); the probability of choosing a leaf is \(k^2/(k+2)^2\). The target term is zero.

Let \(Q=134k+147\). Direct exact elimination in (2) gives
\[
\begin{aligned}
A&=\frac{8(10k^2+54k+37)}Q, &B&=\frac{2(k^2+126k+136)}Q,\\
C&=\frac{4(2k^2+118k+125)}Q, &D&=\frac{2(13k^2+298k+298)}Q.
\end{aligned}
\tag{3}
\]
To check that the assumed preferences really are optimal for every integer \(k\ge2\), note that
\[
\begin{aligned}
A-C&=\frac{4(18k^2-10k-51)}Q,\\
A+1-D&=\frac{3(18k^2-10k-51)}Q,\\
D-B&=\frac{4(6k^2+86k+81)}Q,\\
C-B&=\frac{2(3k^2+110k+114)}Q.
\end{aligned}
\tag{4}
\]
The polynomial \(18k^2-10k-51\) equals \(1\) at \(k=2\) and is strictly increasing for \(k\ge2\). All inequalities in (4) are therefore strict. Together with \(B>0\), they validate every neighbor comparison at vertices \(0,2,3,4\) and the forced leaf move. Hence (3) satisfies (1), is globally optimal, and yields the stated gap. With \(k=2\), the six distinct value levels are
\[
V_2(1)=0,\quad V_2(2)=\frac{784}{415},\quad V_2(3)=\frac{1476}{415},\quad V_2(0)=\frac{1480}{415},\quad V_2(4)=\frac{1892}{415},\quad V_2(5)=V_2(6)=\frac{1895}{415}.
\]
At \(k=0\), symmetry of the cycle gives the distance-first optimum. At \(k=1\), an exact Bellman solution in vertex order \(0,1,2,3,4,5\) is
\[
\left(\frac{656}{249},0,\frac{152}{83},\frac{276}{83},\frac{316}{83},\frac{905}{249}\right),
\]
which has no unequal-distance preference inversion. Thus its optimal decisions can respect distance-first (with suitable tie-breaking).

**3. The lower-order cutoff.** The separate self-contained `verify.py` enumerates all labeled simple undirected graphs on \(n\) vertices, for \(2\le n\le6\), by taking each of the \(2^{\binom n2}\) edge masks; it skips disconnected masks. Relabeling any selected target as \(0\) loses no case. For each connected mask the program constructs the exact rational Bellman values by proper-policy iteration: at a fixed value ordering it solves the corresponding integer-coefficient linear equations by exact Gaussian elimination, updates the ordering, and terminates only when the same ordering solves every equality in (1). It then checks every pair of neighbors of every non-target vertex for a strict reversal between shortest-path distance and optimal continuation value. Every test is an exact rational comparison, not a floating-point tolerance.

The exhaustive connected-graph counts for \(n=2,3,4,5,6\) are respectively \(1,4,38,728,26704\), totaling \(27475\) rooted labeled cases. None exhibits an unequal-distance inversion. Hence an optimal policy can prioritize smaller distances for all those graph-target pairs. The seven-vertex example in Step 2 proves the cutoff is sharp. A single-vertex graph has no non-target state, so the assertion is vacuous there.

## Verification

Execute `python3 verify.py` using only the Python standard library. It recomputes the seven-vertex rational values, checks the family formulas and Bellman identities for additional finite instances, and independently enumerates every labeled graph up to order six with exact-rational policy evaluation. The observed terminal line is `VERIFY_OK`, preceded by `EXHAUSTIVE_CONNECTED_LABELLED_ROOTED {2: 1, 3: 4, 4: 38, 5: 728, 6: 26704} TOTAL 27475`. The unbounded pendant-load conclusion follows from the algebra and the sign of the displayed quadratic, not from the finite-instance checks. The cutoff relies on fully exhaustive finite enumeration; its reproducibility is conditional on correct execution of the included source code, and no external formal proof certificate is claimed.

## Relationship to prior work

Georgakopoulos, Haslegrave, Sauerwald and Sylvester study precisely this two-offer choice random walk and prove that ordering neighbors by their *optimal expected hitting times* gives an optimal policy, together with general bounds and polynomial-time optimization. That ordering theorem is a prerequisite here, not a new claim; the source does not provide this sharp seven-vertex graph-order boundary, the decorated-cycle preference gap, or the pendant-load threshold. Azar, Broder, Karlin, Linial and Phillips had already explicitly observed that going closer to a target need not be optimal, but their controller has an independent bias coin allowing an arbitrarily selected move, rather than a pair of uniformly offered neighbors. Consequently the qualitative existence of some distance-heuristic failure is prior knowledge. The result asserted here is the exact minimum graph order for the two-offer model and its all-parameter unicyclic witness family. Earlier complete-tree parent-preference results do not imply the cyclic obstruction or the small-graph minimality. No bibliographic/database search proves global uniqueness or priority; further independent literature review remains appropriate.

## Limitations

The optimality criterion is expected first-hitting time, not stochastic domination at each deadline or cover time. Neighbor proposals must be independent draws with replacement. The seven-vertex witness is not asserted unique, and no complete classification of all seven-vertex obstructions is established. For the finite-size minimum the proof uses an independently replayable finite enumeration, not a handwritten classification or externally formalized certificate. No claims are made for directed, weighted, lazy, or adaptive-graph variants.

## References

1. A. Georgakopoulos, J. Haslegrave, T. Sauerwald, J. Sylvester, *The Power of Two Choices for Random Walks*, arXiv:1911.05170 (first submitted 2019-11-12), especially Section 7. https://arxiv.org/abs/1911.05170 .
2. Y. Azar, A. Z. Broder, A. R. Karlin, N. Linial, S. Phillips, *Biased Random Walks*, Combinatorica 16 (1996), 1–18; DOI:10.1007/BF01300124. https://www.cs.tau.ac.il/~azar/walk.pdf .
