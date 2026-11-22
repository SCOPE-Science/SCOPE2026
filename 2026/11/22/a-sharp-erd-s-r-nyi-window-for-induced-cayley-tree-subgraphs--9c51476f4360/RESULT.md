# A sharp Erdős–Rényi window for induced Cayley-tree subgraphs

## Finding

Let \(T_n\) be a uniformly chosen labeled tree on \([n]=\{1,\ldots,n\}\), and let \(H_{n,k}=T_n[[k]]\) be its induced graph on the first \(k\) vertices. Independently define \(G_{n,k}\) with law \(G(k,2/n)\), on the **same fixed labeled vertex set** \([k]\). For every integer \(n\ge3\) and \(1\le k\le n\), the total variation distance between their *complete labeled graph laws* satisfies

\[
d_{\mathrm{TV}}(\mathcal L(H_{n,k}),\mathcal L(G_{n,k}))
\le \min\!\left\{1,\frac{k^2(k-1)+2k(k-1)+21\binom{k}{3}}{n^2}\right\}.
\]

Hence the two complete graphs are asymptotically indistinguishable in total variation if \(k=o(n^{2/3})\). The exponent is sharp: if \(k/n^{2/3}\to c\in(0,\infty)\), the numbers of *wedges* (unordered pairs of distinct edges sharing an endpoint) satisfy

\[
W(H_{n,k})\Rightarrow\operatorname{Poisson}(3c^3/2),\qquad
W(G_{n,k})\Rightarrow\operatorname{Poisson}(2c^3).
\]

In particular, the event that the graph is a matching (there are no wedges) yields the positive separation

\[
\liminf_{n\to\infty}d_{\mathrm{TV}}(\mathcal L(H_{n,k}),\mathcal L(G_{n,k}))
\ge e^{-3c^3/2}-e^{-2c^3}>0.
\]

There is also a spatial refinement at the earlier, edge-onset scale. The point measure placing a point at \((i/\sqrt n,j/\sqrt n)\) for each tree edge \(\{i,j\}\) with \(i<j\) converges on bounded portions of \(\{0<u<v\}\) to a Poisson point process with intensity \(2\,du\,dv\). Consequently, if the first edge to be uncovered is indexed by its earlier and later endpoint, their limits \((U,V)\) have joint density \(2e^{-v^2}\) for \(0<u<v\); thus \(\Pr(V>t)=e^{-t^2}\) and \(U\mid V=v\) is uniform on \((0,v)\). The scalar first-edge limit follows already from the previously known edge-count process; the location-marked law follows here from full graph approximation.

## Assumptions and scope

The uniform distribution is on the \(n^{n-2}\) Cayley trees with vertex set \([n]\). All probabilities include the randomness of the tree; in \(G_{n,k}\), all \(\binom{k}{2}\) possible edges are independent with probability \(2/n\). The total variation distance is \(\sup_A|\Pr(H_{n,k}\in A)-\Pr(G_{n,k}\in A)|\) over labeled graphs on \([k]\). A wedge is determined by an unordered pair of incident edges and is counted once; equivalently \(W(Q)=\sum_{v}\binom{\deg_Q(v)}2\). At the critical window, \(k\) is an integer sequence satisfying the stated limit. The point-process convergence is vague convergence on each bounded set with boundary of zero limiting intensity; points at the boundary do not affect the limit. The first edge is the one with smallest later endpoint, with a fixed tie-breaking rule (ties have vanishing probability on the \(\sqrt n\) scale).

## Proof

**Forest-extension identity.** Let \(F\) be a forest of \(r\) prescribed edges on \([n]\), including isolated vertices, with connected-component sizes \(s_1,\ldots,s_{n-r}\). Contracting these components leaves \(s_as_b\) choices for each link between components \(a,b\). The weighted Cayley formula for this contracted complete graph gives \(n^{n-r-2}\prod_a s_a\) spanning trees extending \(F\). Dividing by \(n^{n-2}\),

\[
\Pr(F\subseteq T_n)=n^{-r}\prod_a s_a.
\]

An impossible cyclic prescription has probability zero. Thus an edge belongs to \(T_n\) with probability \(2/n\), two distinct incident edges with probability \(3/n^2\), and two disjoint edges with probability \(4/n^2\). More generally \(\Pr(F\subseteq T_n)\le (2/n)^r\), because \(s\le2^{s-1}\) for each nontrivial forest component.

**Exact edge-count marginal, a previously established result.** Give every edge inside \([k]\) weight \(z\) and all other edges weight one. The weighted complete-graph Laplacian has nonzero eigenvalues \(n-k+kz\) (multiplicity \(k-1\)) and \(n\) (multiplicity \(n-k\)), with endpoint cases obtained directly. The matrix-tree theorem gives

\[
\mathbb E[z^{|E(H_{n,k})|}]
=\left(1-\frac{k}{n}+\frac{k}{n}z\right)^{k-1}.
\]

Therefore \(|E(H_{n,k})|\sim\operatorname{Bin}(k-1,k/n)\). Its mean equals \(\binom{k}{2}(2/n)=k(k-1)/n\), the mean of \(|E(G_{n,k})|\sim\operatorname{Bin}(\binom{k}{2},2/n)\). The exact marginal and its process interpretation are established in the literature and are used, not claimed as novel here.

**Full graph coupling.** For every labeled graph with a fixed number \(r\) of edges, conditional on having \(r\) edges and being a matching, the law is uniform over the labeled \(r\)-edge matchings, under *either* model: in the tree model this is permutation invariance; in the independent-edge model it is direct. Standard independent-Bernoulli to Poisson coupling bounds for the respective edge counts, both of mean \(\mu=k(k-1)/n\), give

\[
d_{\mathrm{TV}}(|E(H_{n,k})|,|E(G_{n,k})|)
\le\frac{(k-1)k^2+2k(k-1)}{n^2}.
\]

There are \(3\binom{k}{3}\) possible labeled wedges. Their expected numbers are exactly \(9\binom{k}{3}/n^2\) in the tree and \(12\binom{k}{3}/n^2\) in the independent-edge graph. Markov's inequality bounds the respective probabilities of any wedge by these expectations. Maximally couple the two edge counts; on the event of equal counts and no wedge in either model, couple their uniform conditional matchings identically. The union bound on coupling failure yields precisely the asserted total-variation inequality. This step addresses the whole labeled graph, not merely the edge count.

**Sharp critical obstruction.** Fix \(r\ge1\). The number of ordered \(r\)-tuples of wedges supported on pairwise disjoint vertex triples is \((k)_{3r}/2^r\). The forest-extension identity shows that each such tuple occurs in the tree with probability \(3^r/n^{2r}\); in the independent-edge graph its probability is \(4^r/n^{2r}\). If \(k\sim c n^{2/3}\), these tuples contribute, respectively, \((3c^3/2)^r\) and \((2c^3)^r\) to the \(r\)-th factorial moments.

All other tuples have two distinct wedges in at least one common connected component of their union. Every such component contains at least three edges. For a union having \(v\) vertices and \(e\) edges, the forest-extension identity bounds its contribution by a constant times \(k^v n^{-e}\), while cyclic unions have zero probability in the tree and satisfy the same upper bound in the independent-edge model. A connected union of wedges with \(e\ge3\) has at most \(e+1\) vertices, and hence contributes \(O(n^{(2-e)/3})=o(1)\). A finite classification of union types exists for each fixed factorial order \(r\). Thus overlapping tuples together contribute \(o(1)\); all factorial moments converge to those of the displayed Poisson laws, which uniquely determine their distributions. The event \(\{W=0\}\) then gives the sharp positive total-variation lower bound.

**The marked edge-onset process.** For every fixed \(b>0\), set \(k=\lfloor b\sqrt n\rfloor\). The preceding bound tends to zero at order \(O_b(n^{-1/2})\). For the independent-edge graph, the Laplace functional of \(\sum_{1\le i<j\le k}X_{ij}\delta_{(i/\sqrt n,j/\sqrt n)}\), with independent \(X_{ij}\sim\operatorname{Bernoulli}(2/n)\), is a product. Its logarithm tends by Riemann sums to \(2\int_{0<u<v<b}(e^{-f(u,v)}-1)\,du\,dv\), for every nonnegative continuous test function \(f\) of compact support. The full-graph total-variation bound transfers that convergence to \(T_n\). The void probability before time \(v\) equals \(e^{-v^2}\); multiplying by the intensity at \((u,v)\) gives the first-point density \(2e^{-v^2}\). Tightness of the first later-endpoint follows from the exact no-edge probability \((1-k/n)^{k-1}\to e^{-b^2}\), as \(b\to\infty\).

## Verification

The included standalone standard-library `checker.py` enumerates every Prüfer code for \(3\le n\le7\), derives the corresponding labeled tree, and independently checks the exact edge-count marginal, wedge expectations, one-edge and two-edge inclusion probabilities, and the stated full-labeled-graph total-variation bound. It passed 142 exact-rational assertions. These finite checks test the formulas and code but do not establish any infinite-size limit; the preceding arguments establish those limits.

Reproduce with `python3 checker.py`; no external Python dependencies are required.

## Relationship to prior work

Hackl, Panholzer and Wagner (initial public preprint 2023-01-02) analyzed the uncover process of uniform labeled trees, including the exact induced-edge **count** distribution and macroscopic Gaussian process. This exact binomial marginal is expressly treated here as prior work. Janson (initial public preprint 2023-12-21) generalized uncovering results to other graphs, studying edge-count processes and small-subgraph counting at macroscopic scale. His Section 9 treats possible extensions to small-subgraph counts, rather than the two-thirds-scale Poisson wedge obstruction and full labeled graph total variation. Grimmett and Winkler (initial public preprint 2003-02-17) treat uniform forests and spanning-tree edge dependence, including negative association. Their work gives relevant foundational probability context but does not state the joint full-graph approximation and sharp wedge separation above.

The present contribution is the explicit **whole labeled induced-graph** coupling range \(k=o(n^{2/3})\), the matching sharpness via distinct wedge Poisson intensities, and the location-marked early-edge limit. The edge-count marginal and scalar first-edge consequences are not asserted to be independently new.

## Limitations

This theorem concerns the complete graph law only on an initial deterministic vertex set for a uniformly labeled Cayley tree, under the fixed edge density \(2/n\). The upper bound is not asserted to have a sharp constant; the lower bound proves that the approximation cannot extend in total variation throughout the critical window, but does not determine the full limiting total-variation distance there. The marked process statement concerns compactly supported observations at the \(\sqrt n\) scale. Priority relative to possible unpublished or unindexed treatments of induced spanning-tree subgraphs remains uncertain; exact edge-count information is already published. No independent mathematical audit has been conducted.

## References

1. G. R. Grimmett and S. N. Winkler, *Negative association in uniform forests and connected graphs*, arXiv:math/0302185, first publicly posted 2003-02-17, https://arxiv.org/abs/math/0302185.
2. B. Hackl, A. Panholzer and S. Wagner, *The Uncover Process for Random Labeled Trees*, arXiv:2301.00664, first posted 2023-01-02, https://arxiv.org/abs/2301.00664.
3. S. Janson, *Uncovering a graph*, arXiv:2312.13823, first posted 2023-12-21, https://arxiv.org/abs/2312.13823.
4. Cayley's classical labeled-tree formula, the weighted matrix-tree theorem, and the Poisson approximation bound for sums of independent Bernoulli variables are standard ingredients; their use does not imply priority over earlier treatments.

