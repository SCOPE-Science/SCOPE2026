# A Rayleigh–Gaussian root-degree law for frontier-grown bipartite trees

## Finding
For each integer \(b\ge1\), start a spanning-tree growth process at a fixed vertex \(s\) in the two-vertex part of \(K_{2,b}\). At each step, choose uniformly among edges having exactly one endpoint in the current tree, and add the chosen edge and its new endpoint. Let \(D_b\) be the final degree of \(s\). Define \(J_b\) as the number of vertices in the \(b\)-vertex part present immediately before the other vertex of the two-vertex part first enters the tree. Then, for \(1\le j\le b\),
\[
\Pr(J_b=j)=\frac{j}{b}\prod_{h=1}^{j-1}\left(1-\frac{h}{b}\right),\qquad
(D_b\mid J_b=j)\mathrel{\overset{d}{=}}j+\operatorname{Bin}(b-j,1/2).
\]
Consequently the exact probability-generating function is
\[
\mathbb E[z^{D_b}]=\sum_{j=1}^{b}\frac{j}{b}\prod_{h=1}^{j-1}\left(1-\frac{h}{b}\right)z^j\left(\frac{1+z}{2}\right)^{b-j}.
\]
If \(R\) is Rayleigh with \(\Pr(R>x)=e^{-x^2/2}\) for \(x\ge0\), and \(Z\) is an independent standard Gaussian, then
\[
\frac{D_b-b/2}{\sqrt b}\ \xrightarrow[b\to\infty]{d}\ \frac{R+Z}{2}.
\]
The limiting law is not Gaussian. Moreover, if \(U_b\) is the degree of \(s\) in a *uniform* spanning tree of the same \(K_{2,b}\), then \(U_b\mathrel{\overset d=}1+\operatorname{Bin}(b-1,1/2)\), and \(D_b\) stochastically dominates \(U_b\), strictly when \(b\ge2\). In particular,
\[
\mathbb E[D_b]-\mathbb E[U_b]\sim\sqrt{\frac{\pi b}{8}}.
\]

## Assumptions and scope
\(K_{2,b}\) is the simple, unweighted complete bipartite graph. Growth is by uniformly choosing one *frontier edge*, not by uniformly choosing a frontier vertex, and it runs until every vertex is reached. The root \(s\) is specified in the two-vertex part. Each edge-selection step is independent conditional on the current tree. The comparison object \(U_b\) is uniform over all labeled spanning trees, not the result of the frontier-growth process. Stochastic dominance means \(\Pr(D_b\ge k)\ge\Pr(U_b\ge k)\) at every integer threshold \(k\).

## Proof
**First-bridge hazard.** Write \(t\) for the other vertex of the two-vertex part. Until \(t\) is discovered, the current vertex set consists of \(s\) and \(j\) of the \(b\) opposite-part vertices. At this stage the frontier consists of exactly \(b-j\) edges from \(s\) to unseen vertices and \(j\) edges from the reached opposite-part vertices to \(t\), hence exactly \(b\) edges. Initially \(j=0\), and the first step reaches an opposite-part vertex. For \(1\le j\le b\), the probability that the next addition is \(t\) is \(j/b\), with continuation probability \((b-j)/b\). Multiplying continuation probabilities proves the formula for \(J_b\); at \(j=b\) the hazard equals one. All those \(j\) reached opposite-part vertices were joined to \(s\), so the current root degree is \(j\).

**Remaining attachments.** After \(t\) enters, each of the \(b-j\) unseen opposite-part vertices has exactly two frontier edges, one from \(s\) and one from \(t\). Whichever unseen vertex is selected next, its parent is an equally likely choice between \(s\) and \(t\). The sequence of parent choices is conditionally independent, because every vertex selected has the same two parent-edge choices, and each such choice does not affect the future choice probabilities. Thus the number attached to \(s\) afterward is exactly \(\operatorname{Bin}(b-j,1/2)\). This yields the conditional law and generating function without approximation.

**Asymptotic first-bridge size.** For each nonnegative integer \(j<b\),
\[
\Pr(J_b>j)=\prod_{h=1}^{j}\left(1-\frac{h}{b}\right).
\]
For each fixed \(x\ge0\), substitute \(j=\lfloor x\sqrt b\rfloor\). Expanding \(\log(1-u)=-u+O(u^2)\) uniformly for \(u=O(b^{-1/2})\) gives
\[
\log\Pr(J_b>\lfloor x\sqrt b\rfloor)=-\frac{x^2}{2}+o(1).
\]
Hence \(J_b/\sqrt b\Rightarrow R\), and therefore \(J_b/b\to0\) in probability. The bound
\[
\Pr(J_b>j)\le\exp\left(-\frac{j(j+1)}{2b}\right)
\]
provides uniform integrability of \(J_b/\sqrt b\). Thus \(\mathbb E[J_b]/\sqrt b\to\mathbb E R=\sqrt{\pi/2}\).

**Joint normal limit.** Put \(B_b=D_b-J_b\); conditional on \(J_b\), it is binomial with size \(b-J_b\) and success probability \(1/2\). For any fixed real \(u\),
\[
\mathbb E\!\left[\exp\left(iu\frac{2B_b-(b-J_b)}{\sqrt b}\right)\middle|J_b\right]
=\cos(u/\sqrt b)^{b-J_b}\xrightarrow{\Pr}e^{-u^2/2}.
\]
These conditional characteristic functions are bounded by one, so their products with bounded functions of \(J_b/\sqrt b\) have the same factorization limit. This proves joint convergence of \(J_b/\sqrt b\) and \((2B_b-(b-J_b))/\sqrt b\) to independent \(R\) and \(Z\). Since
\[
\frac{D_b-b/2}{\sqrt b}=\frac12\left(\frac{J_b}{\sqrt b}+\frac{2B_b-(b-J_b)}{\sqrt b}\right),
\]
the asserted limit follows. It is non-Gaussian: if the sum of an independent nondegenerate Gaussian and \(R\) were Gaussian, the characteristic functions would force \(R\) to be Gaussian, contrary to its half-line support.

**Comparison with uniform spanning trees.** Every spanning tree of \(K_{2,b}\) has exactly one opposite-part vertex joined to both \(s\) and \(t\), and each other opposite-part vertex is joined to exactly one of them. All \(b2^{b-1}\) resulting labeled choices are distinct spanning trees. Therefore \(U_b\stackrel d=1+\operatorname{Bin}(b-1,1/2)\). Conditional on \(J_b=j\), couple \(D_b=j+\sum_{i=1}^{b-j}\xi_i\) with \(U_b=1+\sum_{i=1}^{b-j}\xi_i+\sum_{i=b-j+1}^{b-1}\xi_i\), where the \(\xi_i\) are iid fair Bernoulli. Then \(D_b-U_b=(j-1)-\sum_{i=b-j+1}^{b-1}\xi_i\ge0\) almost surely. For \(b\ge2\), the event \(J_b\ge2\) has positive probability and can give strict inequality. Finally,
\[
\mathbb E[D_b]=\frac{b+\mathbb E[J_b]}{2},\qquad \mathbb E[U_b]=\frac{b+1}{2},
\]
so the stated mean gap follows from the Rayleigh expectation limit.

## Verification
The accompanying `verify.py` enumerates, by exact rational dynamic programming, *all possible frontier edges* and corresponding root-degree increments for each labeled \(K_{2,b}\) with \(1\le b\le9\). It independently computes the proposed conditional-mixture law, compares every probability exactly, and verifies stochastic-tail dominance against the uniform-spanning-tree binomial law. This is a finite regression check of the formulas, not a proof of the asymptotic theorem; the general proof is above. Execute using `python3 verify.py` with only the Python standard library.

## Relationship to prior work
Devroye, Dujmović, Frieze, Mehrabian, Morin, and Reed introduced and studied uniform-frontier-edge spanning-tree growth and its equivalence with exponential first-passage percolation, chiefly obtaining height and first-passage bounds. The exact root-degree law and non-Gaussian \(K_{2,b}\) limit above are not consequences of their stated height theorems. Bhamidi, Goodman, van der Hofstad, and Komjáthy derived shortest-path-tree degree distributions for complete graphs and configuration-model random graphs; their graph models and degree observables do not give this fixed-root, fixed-two-vertex-part asymptotic by substitution. The uniform-spanning-tree comparison uses the elementary labeled enumeration of \(K_{2,b}\), which is background rather than a novelty claim.

## Limitations
The exact law and Rayleigh–Gaussian limit apply only to \(K_{2,b}\), with the root in the part of size two, and uniform frontier-edge selection. This does not classify degrees at arbitrary vertices or growth on \(K_{a,b}\) when both part sizes vary. The literature search does not prove absolute historical novelty. The asymptotic result is an ordinary mathematical proof and has not received independent audit.

## References
1. L. Devroye, V. Dujmović, A. Frieze, A. Mehrabian, P. Morin, B. Reed, *Notes on Growing a Tree in a Graph*, arXiv:1707.00083 (first posted 2017-07-01), https://arxiv.org/abs/1707.00083 .
2. S. Bhamidi, J. Goodman, R. van der Hofstad, J. Komjáthy, *Degree distribution of shortest path trees and bias of network sampling algorithms*, Ann. Appl. Probab. 25 (2015), 1780–1826, arXiv:1310.5672, https://arxiv.org/abs/1310.5672 .
