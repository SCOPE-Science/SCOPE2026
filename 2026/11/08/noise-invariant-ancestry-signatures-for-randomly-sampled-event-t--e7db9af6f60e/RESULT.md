# Noise-invariant ancestry signatures for randomly sampled event trees

## Finding

Let a finite rooted tree have one binary event indicator for each non-root vertex (equivalently, for each oriented edge). Select **one** tree vertex at random with strictly positive probability at every vertex, and record the indicators of edges on its root path. Independently pass each indicator through an arbitrary, **unknown and event-specific** binary observation channel, whose true-positive probability strictly exceeds its false-positive probability. Assume observation errors are conditionally independent across event coordinates given the latent indicators. No equality or calibration of the error rates is assumed.

**Theorem.** For any two distinct observed event indicators, their covariance is strictly positive if and only if their tree edges are ancestor-comparable, and strictly negative if and only if their edges lie in different branches. Consequently:

1. The graph linking exactly the positive-covariance pairs is a *trivially perfect graph* (the ancestor-comparability graph of a rooted forest). Conversely, every finite trivially perfect graph is realized as the positive-covariance graph of such a positive-mass event tree, even with informative event-specific channels.
2. The positive-covariance graph determines the rooted event forest uniquely **after contracting maximal unary runs**. More precisely, its equivalence classes of equal closed graph neighborhoods are exactly the maximal consecutive chains of event edges with no branch between them; after contracting each class, recursive removal of the unique universal class from each connected component recovers the entire labelled quotient forest. The relative order of labels within a class cannot be determined from **covariance signs alone**. The forest's roots are attached to a new common root to recover the quotient event tree.
3. Write \(p\ge 2\) for the number of events, \(\gamma=\min_{i<j}|\operatorname{Cov}(X_i,X_j)|>0\), and \(\widehat C_{ij}\) for the empirical covariance from \(N\) independent observation vectors, calculated using divisor \(N\). For every \(0<\delta<1\), if

\[
N\ge \frac{8}{\gamma^2}\log\frac{2p^2}{\delta},
\]

then the sign graph and its entire contracted rooted forest are recovered exactly with probability at least \(1-\delta\).

Here “conversely” refers to *sign-graph feasibility*, not to realizability of every numerical covariance matrix with that sign graph. The result is not a claim of identification of noise rates or of the full latent distribution.

## Assumptions and scope

The tree \(T=(V,E)\) is finite, directed away from a distinguished root \(r\), with \(p=|E|\ge2\). Every vertex \(v\) receives mass \(\rho_v>0\), with \(\sum_v\rho_v=1\). A sampled vertex \(Z\) induces \(Y_e=\mathbf 1\{Z\text{ descends from the head of }e\}\). Thus each observation follows one path, *not* an independent edge-retention process that can activate several branches.

For every event edge \(e\), let \(X_e\in\{0,1\}\) have conditional probabilities \(f_e=\Pr(X_e=1\mid Y_e=0)\) and \(t_e=\Pr(X_e=1\mid Y_e=1)\). Require \(0\le f_e<t_e\le1\), with conditional independence of the coordinates \(X_e\) given the vector \(Y\). The observation channels and all masses may vary with the event. Across observations, the complete vectors are independent and identically distributed. No assumption of exchangeability, binary-tree branching, common error rates, or observed marginal ordering is made.

Write \(e\prec h\) when the head of \(e\) is a strict ancestor of the head of \(h\). Denote by \(S_e\) the subtree below the head of \(e\), and set \(q_e=\Pr(Z\in S_e)\). A unary run means consecutive event edges along a directed path such that every intermediate head vertex has exactly one child. A run ends at the next branching head or leaf. Its final edge belongs to the run.

## Proof

**1. Exact covariance signs.** The sets \(S_e\) form a laminar family: for distinct edges, either one descendant set strictly contains the other or they are disjoint. Strictly positive vertex masses give \(0<q_e<1\), and strict inclusion gives strict inequality between the corresponding subtree masses. Since \(Y_e=\mathbf1\{Z\in S_e\}\),

\[
\operatorname{Cov}(Y_e,Y_h)=
\begin{cases}
q_h(1-q_e),&e\prec h,\\
q_e(1-q_h),&h\prec e,\\
-q_eq_h,&S_e\cap S_h=\varnothing.
\end{cases}
\]

Every displayed term is strictly nonzero. Conditional expectation through the binary channels is \(\mathbb E[X_e\mid Y_e]=f_e+(t_e-f_e)Y_e\). Conditional independence across coordinates and total covariance imply, for distinct \(e,h\),

\[
\operatorname{Cov}(X_e,X_h)
=(t_e-f_e)(t_h-f_h)\operatorname{Cov}(Y_e,Y_h).
\]

The two positive factors preserve each sign, proving the first statement without knowing either error rate.

**2. Exact class of feasible graphs.** The positive-covariance graph links precisely the ancestor-comparable edge pairs. Delete the common root of \(T\) and regard each remaining head vertex as the corresponding event edge. Each root-child subtree is now a rooted component; adding edges between all ancestor-descendant pairs in that rooted forest gives exactly the positive-covariance graph. Such graphs are the standard *trivially perfect graphs*: equivalently, every nonempty connected induced subgraph has a universal vertex. Conversely, for any trivially perfect graph \(H\), recursively choose a universal vertex from each nonempty connected component, make it the root of that component, delete it and repeat on the remaining components. Induction shows that the ancestor closure of the resulting rooted forest is exactly \(H\). Attach the forest roots beneath a new root, assign all vertices positive probabilities, and apply any channels satisfying the assumptions. The preceding covariance formula realizes precisely \(H\).

**3. Precise identifiable quotient.** If two vertices of \(H\) have the same *closed* neighborhood, they are adjacent and hence ancestor-comparable. Suppose the corresponding edges satisfy \(e\prec h\). If any intermediate head on the chain from \(e\) to \(h\) has an off-chain child, an event edge in that side branch is adjacent to \(e\) but not \(h\), contradicting equality of closed neighborhoods. Conversely, if there is no such branch, every event edge is comparable to \(e\) exactly when it is comparable to \(h\), apart from the two themselves, which are adjacent; their closed neighborhoods coincide. Thus true-twin classes are exactly maximal unary runs.

Now contract each class. In any connected component of the contracted graph, the universal vertex is unique: universals in the original component form precisely its initial true-twin class, and any two distinct universals would have identical closed neighborhoods. Removing the unique universal class leaves exactly the rooted child components. Recursing gives a uniquely determined labelled quotient forest, independently of the order of contracting. Finally, permuting the event labels along any unary run changes their ancestral order without changing any ancestor-comparability pair; positive masses can be reassigned to every vertex, so all those orderings yield the same sign graph. The claimed identifiability limit concerns only the sign graph, not all moments or the full data law.

**4. Finite-sample control.** The empirical covariance is \(\widehat C_{eh}=\overline{X_eX_h}-\overline{X_e}\,\overline{X_h}\). Hoeffding's bound gives, for any one marginal or product marginal, the probability of an absolute estimation error exceeding \(u>0\) at most \(2e^{-2Nu^2}\). There are \(p+\binom p2\le p^2\) such means. By the union bound, with probability at least \(1-2p^2e^{-2Nu^2}\), all their errors are at most \(u\). Because all empirical and population means lie in \([0,1]\), the product-of-means error is at most \(2u\), so every covariance error is at most \(3u\). Taking \(u=\gamma/4\) yields error at most \(3\gamma/4<\gamma\), preserves every strict sign, and proves the sample guarantee.

## Verification

A deterministic standalone checker `verify.py` enumerates every labelled tree on \(2\) through \(6\) vertices by Prüfer codes and every possible root, assigns strictly positive unequal rational masses and heterogeneous rational observation channels, evaluates all pairwise covariances in exact rational arithmetic, and checks (i) each sign against ancestor comparability, (ii) the true-twin partition, and (iii) reconstruction of the original unary-contracted forest. This is a finite diagnostic and is not used as a proof of the theorem for arbitrary tree sizes.

The proof above independently covers every finite rooted tree, every positive vertex-mass vector, all informative independent coordinate channels, and the stated finite-sample guarantee.

An explicit noise contrast is useful. On the four-node path with equal node masses, let only the middle event indicator pass through a symmetric bit-flip channel of rate \(1/4\). Conditioning on its observed value \(1\) leaves the first and last *latent* event indicators with conditional covariance \(3/64>0\), whereas conditioning on the noiseless middle indicator makes them independent. Measurement noise therefore destroys the original chain's conditional-independence screening, even though the positive pairwise covariance sign graph remains unchanged.

## Relationship to prior work

Labouriau's October 2026 event-accumulation paper defines the same one-path observation model and identifies its noiseless conditional-independence graph as the *line graph* of the event tree. It also explains that measurement error destroys exact graphical screening. The present result concerns a **different graph**, derived from signs of unconditional pairwise covariances, and identifies its exact noise-robust class and recoverable quotient under unknown, heterogeneous binary channels.

The characterization of trivially perfect graphs as ancestor-comparability graphs of rooted forests is classical (Wolk; Golumbic); it is used here, not claimed as new. Covariance attenuation by independent binary channels is also elementary and not claimed as a standalone novelty. The assessed contribution is the *complete combined sign-graph classification, identifiable quotient, and finite-sample noisy-recovery theorem for single-lineage event data*.

Szabo and Boucher (2002) and Olde Loohuis et al. (2014) consider noisy oncogenetic progression trees and tree reconstruction. Their models allow multiple descendant branches to be simultaneously present through independent edge-event accumulation, rather than observing one sampled node/path. Their results do not directly establish the negative-covariance relations for disjoint branches or the claim here for unknown event-specific channels. The complete original 2002 article was not accessible during this assessment; priority with respect to that and further latent-tree literature is a residual risk.

## Limitations

The theorem assumes positive sampling mass at **every** tree node. Leaf-only sampling or a zero-mass internal node can make nested indicators identical or degenerate and invalidate strict sign and identifiability statements. Channels must be conditionally independent across events and positively informative; arbitrary correlated or sign-reversing errors need not preserve the graph. Only the unary-contracted topology, not the ordering within each unary run or the noise parameters, is identified from signs. The sample bound is sufficient, not claimed minimax-optimal, and can be large when the smallest absolute covariance is tiny. The graph characterization addresses covariance sign patterns, **not** the complete compatibility of an observed joint distribution with the accumulation mechanism. Independent review and a definitive historical priority determination remain outstanding.

## References

1. R. Labouriau, *Graphical Models Induced by Irreversible Event Accumulation on Trees*, arXiv:2610.40127v1, first posted 2026-10-29. https://arxiv.org/html/2610.40127
2. E. S. Wolk, *The comparability graph of a tree*, Proc. Amer. Math. Soc. 13 (1962), 789–795, https://doi.org/10.1090/S0002-9939-1962-0172273-0.
3. M. C. Golumbic, *Trivially perfect graphs*, Discrete Mathematics 24 (1978), 105–107. https://doi.org/10.1016/0012-365X(78)90178-4.
4. L. Olde Loohuis et al., *Inferring tree causal models of cancer progression with probability raising*, PLOS ONE 9(10), e108358 (2014), https://doi.org/10.1371/journal.pone.0108358 ; preprint arXiv:1311.6293.
5. A. Szabo and K. Boucher, *Estimating an oncogenetic tree when false negatives and positives are present*, Mathematical Biosciences 176 (2002), 219–236, https://doi.org/10.1016/S0025-5564(02)00086-X.
