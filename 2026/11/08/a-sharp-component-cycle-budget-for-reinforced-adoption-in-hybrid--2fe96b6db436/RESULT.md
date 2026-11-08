# A sharp component–cycle budget for reinforced adoption in hybrid social contagion

## Finding

In a finite simple connected social network, consider irreversible adoption with a nonempty initial seed set. Each remaining vertex has an integer adoption threshold: an imitator requires one adopting neighbor, while a reinforced adopter requires at least two. For the final adopting set \(C\), define \(c(X)\) to be the number of connected components of its induced subgraph \(G[X]\) and \(\beta(X)=|E(G[X])|-|X|+c(X)\) its cycle rank. Then every legal activation history obeys the **sharp component–cycle resource inequality**

\[
\sum_{v\in C\setminus S}\bigl(\tau(v)-1\bigr)
\le c(S)-c(C)+\beta(C)-\beta(S).
\tag{1}
\]

In particular, if \(h\) newly adopting vertices have thresholds at least \(r\ge2\), then

\[
 h\le\left\lfloor\frac{|S|-1+\beta(G)}{r-1}\right\rfloor.
\tag{2}
\]

For a single seed, this says that each \((r-1)\) units of independent network cycles can support at most one threshold-\(r\) adoption, regardless of the number of one-neighbor imitators. The bound is attained by infinitely many connected graphs: for each \(r\ge2\) and \(k\ge1\), a \((kr+1)\)-vertex reinforced fan of \(k\) gadgets with cycle rank \(k(r-1)\) has \(k\) distinct threshold-\(r\) nonseed vertices, all of which adopt from one seed. Thus the coefficient in (2) cannot be improved.

If each enabled vertex changes state at a strictly positive state-dependent time-homogeneous rate, including an imitator's Fermi imitation rate \(\theta m/\deg(v)\) with \(\theta>0\), the eventual set \(C\) equals the deterministic threshold closure almost surely. The claim is therefore pathwise and insensitive to the positive rate parameter, but makes no assertion about adoption times or the singular limit \(\theta=0\).

## Assumptions and scope

Let \(G=(V,E)\) be a finite undirected simple connected graph with at least two vertices. Fix a nonempty seed set \(S\subseteq V\), activated permanently at time zero. Every nonseed vertex \(v\) has an integer threshold \(1\le\tau(v)\le\deg(v)\). For deterministic synchronous dynamics, all inactive vertices with at least \(\tau(v)\) currently active neighbors activate in the next round. Its eventual closed set is \(C\supseteq S\). For asynchronous dynamics, any enabled inactive vertex may activate, and every such vertex has a strictly positive time-homogeneous rate depending only on the current active set. In particular, since the state space is finite, each enabled vertex has a rate bounded below by a positive constant while it remains enabled. A particularly relevant instance assigns threshold \(1\) to imitators (rate \(\theta m/\deg(v)\) when \(m\ge1\)) and threshold \(\lceil\phi\deg(v)\rceil\) to threshold-followers (rate one when enabled), with \(0<\phi\le1\), \(\theta>0\). The original hybrid model employs irreversible adoption and these two types of positive-rate rule.

The cycle rank is \(\beta(X)=|E(G[X])|-|X|+c(X)\); it is zero for a forest and counts independent undirected cycles in a general graph. In (2), \(\beta(G)=|E|-|V|+1\). Vertices counted by \(h\) are explicitly **nonseeds that eventually activate**, not seeded vertices whose numerical thresholds may also be high. For mixed thresholds the stronger weighted bound (1) applies directly. The model excludes recovery, spontaneous nonseed activation, and permanent zero imitation rates.

## Proof

Order the vertices of \(C\setminus S\) in any legal chronological activation order, with all seeds earlier than all nonseeds; for synchronous rounds, break ties arbitrarily within each round. When a nonseed \(v\) activates, at least \(\tau(v)\) of its incident edges have their other endpoint earlier in the order. Edges joining two seeds are \(E(G[S])\); every other edge of \(G[C]\) belongs to exactly one new vertex when that edge is counted from the later endpoint. It follows that

\[
|E(G[C])|\ge |E(G[S])|+
\sum_{v\in C\setminus S}\tau(v).
\tag{3}
\]

Subtract \(|C|=|S|+|C\setminus S|\) and add \(c(C)\). Using the definition of cycle rank on \(S\) and \(C\) gives

\[
\beta(C)\ge\beta(S)-c(S)+c(C)
+\sum_{v\in C\setminus S}(\tau(v)-1),
\]

which proves (1) without probabilistic or asymptotic assumptions. Moreover, \(c(S)\le|S|\), \(c(C)\ge1\), \(\beta(S)\ge0\), and \(\beta(C)\le\beta(G)\) because cycles in an induced subgraph are independent only to the extent permitted by the original graph's cycle space. Hence the sum in (1) is at most \(|S|-1+\beta(G)\). Each of the \(h\) stated reinforced nonseed activations contributes at least \(r-1\) to that sum, proving (2).

For sharpness fix \(r\ge2\) and \(k\ge1\). Construct one seed vertex \(o\). For each \(j=1,\ldots,k\), add \(r-1\) distinct imitators \(a_{j,1},\ldots,a_{j,r-1}\), one reinforced vertex \(t_j\) of threshold \(r\), and the edges \(oa_{j,i}\), \(a_{j,i}t_j\), and \(ot_j\). Every added imitator has threshold one. The resulting connected graph has \(1+kr\) vertices and \(k(2r-1)\) edges, so \(\beta(G)=k(r-1)\). Starting at \(S=\{o\}\), all imitators activate, then every \(t_j\) has \(r\) active neighbors and activates. Thus \(h=k\) and equality holds in (1) and (2). For \(r=2\) these are triangular petals sharing the seed; for larger \(r\) each gadget has \(r-1\) independent cycles.

Finally, on any finite network, the deterministic closure is monotone and contains every asynchronous reachable state: no vertex can activate before meeting its threshold, and threshold enablement is permanent once attained. If the current active set differs from the deterministic closure, some nonseed vertex eligible under the current set can be found by choosing the earliest deterministic activation round not yet completed. An enabled vertex has a positive rate bounded away from zero while that active set persists; thus the probability of remaining at that state forever is zero. There can be at most \(|V|-|S|\) changes. Consequently the asynchronous process reaches the same deterministic closed set almost surely. For the imitation rate specified above, each enabled imitator has rate at least \(\theta/\deg(v)>0\), and enabled threshold-followers have rate one. This proves the pathwise applicability of (1) and (2).

## Verification

The standalone \`verify.py\` recomputes closures and component-cycle ranks independently from graph edges. It tests all connected labeled graphs with up to four vertices, every compatible positive integer threshold assignment and every nonempty seed set; for those instances it also enumerates all possible asynchronous activation orders and checks their unique terminal set. It then checks 20,000 pseudorandomly generated larger connected graph/threshold/seed instances and 99 sharp fan constructions spanning \(2\le r\le10\), \(1\le k\le11\). The script uses only Python's standard library. Running \`python verify.py\` prints counts and PASS messages. These finite checks are not substitutes for the all-size edge-counting proof.

## Relationship to prior work

Shu, Yang, Ruan and Xuan, *Social contagion under hybrid interactions* (arXiv:2408.05050, first public August 9, 2024), introduce the specific mix of threshold-followers and Fermi imitators, show numerical cascade transitions on random graphs, and derive an approximate master-equation description. Their Discussion already notes that imitation parameters can affect speed without affecting the asymptotic state. The novel object here is instead the exact finite-network **component-versus-cycle accounting of reinforced nonseed activations**, an all-graph bound and sharp constructions. No independence-of-rates claim is presented as an independent contribution.

Earlier target-set-selection work of Nichterlein, Niedermeier, Uhlmann and Weller (2010 conference version; 2013 journal version), *On tractable cases of Target Set Selection*, treats arbitrary vertex thresholds and uses feedback edge number for fixed-parameter algorithms and kernelization. Its relevant sections analyze computational tractability, not a sharp universal bound on how many high-threshold **nonseed** activations a specified seed set can cause. The known problem class is broader than the hybrid model; novelty is asserted for the quantitative budget and its equality examples, not for threshold diffusion itself. The relevant closest published mathematical record on complete-multipartite minimum conversion sets solves an exact seed distribution problem on a different graph family, not this unrestricted resource inequality.

## Limitations

This theorem counts higher-threshold *new* adopters; it does not determine the full adoption set of a general graph without simulating the closure. A large cycle rank permits but does not guarantee reinforced adoption. The bound is deliberately strongest for sparse, nearly tree-like graphs; it may be weak for dense graphs. It concerns a finite, static, undirected, irreversible process, not finite-time adoption speed, behavior on directed or dynamically rewired networks, stochastic recovery, or simultaneous global population limits. An equivalent edge-count argument might appear elsewhere in the extensive target-set-selection literature; no claim of priority beyond checked sources or independent external validation is made.

## References

1. Shu, X., Yang, M., Ruan, Z., and Xuan, Q., *Social contagion under hybrid interactions*, arXiv:2408.05050, first posted 2024-08-09. https://arxiv.org/abs/2408.05050
2. Nichterlein, A., Niedermeier, R., Uhlmann, J., and Weller, M., *On tractable cases of Target Set Selection*, Social Network Analysis and Mining 3 (2013), 233–256; earlier conference version (2010), DOI:10.1007/s13278-012-0067-7.
3. Freund, D., Poloczek, M., and Reichman, D., *Contagious Sets in Dense Graphs*, arXiv:1503.00158, first posted 2015-02-28. https://arxiv.org/abs/1503.00158
4. Janson, S., Łuczak, T., Turova, T., and Vallier, T., *Bootstrap percolation on the random graph \(G(n,p)\)*, arXiv:1012.3535, first posted 2010-12-16. https://arxiv.org/abs/1012.3535
