# Transmission zero forcing on complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) with \(r\ge3\), \(1\le n_1\le\cdots\le n_r\), \(N=\sum_{i=1}^r n_i\), and at least one \(n_i\ge2\). For \(0<\alpha\le1\) and \(0<\beta\le1\), set \(q_\alpha(s)=\min\{(s-1)\alpha,(N-s-1)\alpha+(s-1)\alpha^2\}\) and \(Q_\alpha(G)=\max_{2\le j\le r}q_\alpha(n_j)\). Then \(Z_{\alpha,\beta}(G)=N-2\) if \(\beta\le Q_\alpha(G)\), \(Z_{\alpha,\beta}(G)=N-1\) if \(Q_\alpha(G)<\beta\le(N-n_1)\alpha\), and \(Z_{\alpha,\beta}(G)=N\) if \((N-n_1)\alpha<\beta\).

Equivalently, for each possible larger part size \(s\) of a pair of distinct parts, the minimum-size regime is controlled by
\[
q_\alpha(s)=\min\bigl\{{(s-1)\alpha},\ {(N-s-1)\alpha+(s-1)\alpha^2}\bigr\}.
\]
The best pair determines \(Q_\alpha(G)\). In particular, for a balanced graph \(K_{{m,\ldots,m}}\) with \(r\ge3\) and \(m\ge2\), one has \(Q_\alpha(G)=(m-1)\alpha\).

## Assumptions and scope
The graph is finite, simple, connected, complete multipartite, and noncomplete. Its part sizes are positive integers ordered as \(1\le n_1\le\cdots\le n_r\), with \(r\ge3\), and \(N=\sum_i n_i\). The transmission parameters satisfy \(0<\alpha\le1\) and \(0<\beta\le1\). A filled vertex transmits at most once, exactly as in the definition of transmission zero forcing in the cited source.

The complete-graph case, in which every part has size one, is excluded because its ordinary zero forcing number is \(N-1\) rather than \(N-2\). The cited source already gives the complete-graph and complete-bipartite formulas.

## Proof
First establish the ordinary zero forcing baseline. For every noncomplete complete multipartite graph with at least two parts, \(Z(G)=N-2\). Indeed, if exactly two vertices are initially unfilled and they lie in distinct parts, then a filled vertex in either omitted vertex's part has the other omitted vertex as its unique unfilled neighbor, so both omitted vertices are forced. Conversely, suppose at least three vertices are initially unfilled. For a filled vertex in a part \(P\), its unfilled neighbors are exactly the unfilled vertices outside \(P\). Thus, if a force is possible, exactly one unfilled vertex lies outside the transmitter’s part; at least two unfilled vertices lie inside that part. After the unique outside vertex is forced, those two or more same-part vertices remain unfilled and no further force is possible. If no such first force exists, the process is already stalled. If exactly two unfilled vertices lie in the same part, the process also stalls. Consequently every transmission forcing set has size at least \(N-2\), and a transmission forcing set of size \(N-2\) must omit one vertex from each of two distinct parts.

Fix such omitted vertices \(x\) and \(y\), lying in parts of sizes \(n_i\) and \(n_j\). Write \(s=\max\{n_i,n_j\}\), and suppose without loss of generality that \(n_j=s\). Put \(a=n_i-1\), \(b=s-1\), and \(c=N-n_i-s\), so \(b\ge a\). At the first transmission step, \(x\) receives weight \(b\alpha\) from the initially filled vertices in the part of \(y\), while \(y\) receives weight \(a\alpha\) from the initially filled vertices in the part of \(x\). Vertices in all other parts have two unfilled neighbors and cannot yet transmit.

If \(\beta\le a\alpha\), both vertices fill immediately. If \(a\alpha<\beta\le b\alpha\), then \(x\) fills first. At the next step, \(y\) keeps its first-step weight \(a\alpha\), receives \(b\alpha^2\) from \(x\), and receives \(c\alpha\) from the initially filled vertices in the other parts, which have not transmitted before. No vertex that transmitted at the first step may transmit a second time. Thus the final weight of \(y\) is
\[
a\alpha+c\alpha+b\alpha^2=(N-s-1)\alpha+(s-1)\alpha^2.
\]
If \(\beta>b\alpha\), neither omitted vertex fills at the first step and the process stops. Therefore this particular omitted pair is a transmission forcing complement exactly when
\[
\beta\le q_\alpha(s)=\min\bigl\{{(s-1)\alpha},\ {(N-s-1)\alpha+(s-1)\alpha^2}\bigr\}.
\]
Because the part sizes are ordered, the possible values of the larger size \(s\) are precisely \(n_j\) for \(2\le j\le r\). Hence a transmission forcing set of size \(N-2\) exists exactly when \(\beta\le Q_\alpha(G)\).

It remains to distinguish \(N-1\) from \(N\). Leave one vertex unfilled in a smallest part. It has degree \(N-n_1\), and every neighbor is initially filled and has that vertex as its unique unfilled neighbor. Hence it receives total weight \((N-n_1)\alpha\) in one step, so \(N-1\) initial vertices suffice whenever \(\beta\le(N-n_1)\alpha\). Conversely, if \(\beta>(N-n_1)\alpha\), then an omitted vertex receives at most \(\Delta(G)\alpha=(N-n_1)\alpha\), so no set of size \(N-1\) can succeed. Combining this with the \(N-2\) criterion proves the formula.

For the balanced specialization, \(s=m\) for every pair and
\[
(N-m-1)\alpha+(m-1)\alpha^2>(m-1)\alpha
\]
for \(r\ge3\), \(m\ge2\), and \(0<\alpha\le1\), so \(Q_\alpha(G)=(m-1)\alpha\).

## Verification
A standalone exact-arithmetic verifier accompanies this result. It implements the transmission process with the one-transmission-per-filled-vertex restriction, computes the optimum by exhaustive search over all initial subsets, and compares it with the closed formula. Using rational arithmetic, it checks every ordered part profile obtained from three parts of sizes at most three and four parts of sizes at most two, excluding complete graphs, at \(\alpha,\beta\in\{{1/4,1/2,3/4,1}\}\). It also separately checks every omitted-part pair for three asymmetric profiles. The replay reports `ALL CHECKS PASSED; exact_fraction_cases=400; graph_profiles=13`.

These finite checks are consistency tests, not a proof of the infinite statement; the proof above supplies the general argument.

## Relationship to prior work
Berliner, Bozeman, Collins, Flagg, Furst, and Hunnell introduced transmission zero forcing in 2026. Their Section 4.1 is explicitly devoted to complete graphs and complete bipartite graphs and gives exact formulas for \(K_n\), stars, and \(K_{{m,n}}\). Their general observations also give \(Z_{{\alpha,\beta}}(G)\ge Z(G)\) and characterize the regime \(Z_{{\alpha,\beta}}(G)=|V(G)|\) through maximum degree.

The present formula treats complete multipartite graphs with at least three parts. The additional term \((N-s-1)\alpha\) has no bipartite analogue: after one omitted vertex fills, vertices in all third and later parts become newly eligible transmitters and contribute at the second step. Searches for the parameter under the phrases “transmission zero forcing”, “transmission forcing”, “weighted transmission zero forcing”, and “complete multipartite” located the initiating paper but no statement covering this complete multipartite formula.

## Limitations
The theorem does not claim a new formula for complete graphs or complete bipartite graphs, which are already treated in the initiating paper. It is stated only for positive transmission parameters; degenerate endpoint conventions involving \(\beta=0\) are not addressed. The literature comparison is based on the initiating preprint, exact-phrase and alias searches, and a semantic mathematical-results index; absence from those searches is not a proof that no unindexed or later source contains an equivalent result.

The computational verification covers only the finite profiles and rational parameter grid stated above. It is not used to infer the general theorem.

## References
Adam H. Berliner, Chassidy Bozeman, Karen L. Collins, Mary Flagg, Veronika Furst, and Mark Hunnell, “Transmission Zero Forcing,” arXiv:2606.22246, first public version 2026-06-20, https://arxiv.org/abs/2606.22246.
