# Poisson Cantor spectrum and sharp precision entropy for one-step modal counting

## Finding
Fix a real parameter \(\lambda>0\). For each integer \(n>\max\{1,\lambda\}\), let \(G_n\) be a loopless directed graph on \(n\) labelled vertices in which distinct directed arcs are independent with probability \(\lambda/n\); distinguish a fixed vertex \(o\). Let \(\mathcal L_1^{\#}\) be the proposition-free, modal-depth-at-most-one Boolean counting language at \(o\): its nonconstant counting term \(\#\top\) is the number of outgoing neighbors, and atomic formulas compare integer-affine expressions in this count with zero.

Write \(\mathscr S_\lambda\) for all limits \(\lim_{n\to\infty}\Pr((G_n,o)\models\varphi)\) as \(\varphi\) ranges over \(\mathcal L_1^{\#}\). Put
\[
 w_k=e^{-\lambda}\frac{\lambda^k}{k!}\quad(k\ge0),\qquad
 E_\lambda=\left\{\sum_{k=0}^{\infty}\varepsilon_kw_k:\varepsilon_k\in\{0,1\}\right\}.
\]
Then every sentence has a limit and the **exact** set of limits is
\[
 \mathscr S_\lambda
 =\left\{\sum_{k\in F}w_k:F\subset\mathbb N_0\text{ finite}\right\}
 \cup\left\{1-\sum_{k\in F}w_k:F\subset\mathbb N_0\text{ finite}\right\}.
\]
Its closure is \(E_\lambda\), a compact perfect nowhere-dense Cantor set with Hausdorff and upper box-counting dimensions zero. Let \(N_\lambda(\varepsilon)\) be the smallest number of closed intervals of length \(\varepsilon\) covering \(E_\lambda\). The exact covering-entropy asymptotic is
\[
 \boxed{\lim_{\varepsilon\downarrow0}
 \frac{\log N_\lambda(\varepsilon)\,\log\log(1/\varepsilon)}{\log(1/\varepsilon)}=\log2.}
\]
Moreover, for \(0<\lambda<\log2\), the open interval
\(\bigl(1-e^{-\lambda},e^{-\lambda}\bigr)\) is disjoint from \(E_\lambda\).

There is a quantitative finite-size version. Let \(\mathscr S_{\lambda,n}\) be the set of all probabilities attained by formulas of this fragment on \(G_n\), allowing the formula to vary with \(n\). With Hausdorff distance \(d_H\) on nonempty compact subsets of \([0,1]\),
\[
 d_H(\mathscr S_{\lambda,n},E_\lambda)\le \frac{\lambda+\lambda^2}{n}.
\]

## Assumptions and scope
All random directed arcs \((u,v)\), with \(u\ne v\), are independent; antiparallel arcs are distinct. The root \(o\) is deterministic, and \(n>\max\{1,\lambda\}\) ensures a valid edge probability. A successor is an out-neighbor. The language has no vertex propositions, no incoming-edge count, no named neighbors, and no nesting of counting modalities. Boolean negation and integer constants are allowed. A depth-zero formula is constant, so every depth-one integer-affine term is a function of the single outdegree \(D_n\). Exact-degree formulas, \((\#\top\ge k)\land\neg(\#\top\ge k+1)\), are admitted for fixed \(k\ge0\). The set \(\mathscr S_{\lambda,n}\) ranges over all formulas at that fixed \(n\), whereas a single formula is held fixed when defining its limiting probability.

## Proof
**1. Syntax and exact attainable values.** A Boolean combination of integer-affine inequalities in a nonnegative integer \(d\) is eventually constant in \(d\), because each nonconstant affine expression changes sign at most once. Thus its truth set \(A\subseteq\mathbb N_0\) is finite or cofinite. Conversely every finite subset is definable by a finite disjunction of exact-degree formulas and its complement is definable by negation. The root outdegree is exactly
\[
 D_n\sim\operatorname{Bin}(n-1,\lambda/n).
\]
For each fixed \(k\), its point mass tends to \(w_k\), and its distribution converges in total variation to \(\operatorname{Pois}(\lambda)\). Hence every Boolean degree predicate converges and all, and only, the displayed finite/cofinite subsums occur.

**2. Finite-model rate and closure.** Couple each Bernoulli variable of success probability \(p=\lambda/n\) with an independent \(\operatorname{Pois}(p)\) variable, using a maximal coupling. Their total variation distance is \(p(1-e^{-p})\le p^2\). Union bounding the \(n-1\) mismatches and then coupling \(\operatorname{Pois}((n-1)\lambda/n)\) to \(\operatorname{Pois}(\lambda)\) by adding an independent \(\operatorname{Pois}(\lambda/n)\) variable gives
\[
 d_{\mathrm{TV}}(D_n,\operatorname{Pois}(\lambda))
 \le (n-1)\lambda^2/n^2+\lambda/n
 \le(\lambda+\lambda^2)/n.
\]
For any subset \(A\subseteq\mathbb N_0\), its probability under these two laws differs by at most this amount. Every subset of the finite support of \(D_n\) is definable by a finite formula, and finite/cofinite subsets have probabilities dense in the Poisson subsum set. Applying the bound in both directions proves the Hausdorff estimate. Compactness of \(E_\lambda\) follows from continuity of the subsum map on \(\{0,1\}^{\mathbb N_0}\). Truncations show \(\overline{\mathscr S_\lambda}=E_\lambda\).

**3. Cantor structure.** Define the Poisson tail \(t_j=\sum_{k\ge j}w_k\). Since
\[
 \frac{t_{j+1}}{w_j}
 =\sum_{h\ge1}\frac{\lambda^h}{(j+1)(j+2)\cdots(j+h)}
 =O_\lambda(1/j),
\]
for some fixed \(K=K(\lambda)\) and every \(j\ge K\) we have \(w_j>2t_{j+1}\), and the sequence \((w_j)_{j\ge K}\) decreases. For every \(J\), the set \(E_\lambda\) lies in at most \(2^J\) intervals of length \(t_J\). Stirling's formula gives
\[
 t_J=w_J(1+O_\lambda(J^{-1})),\qquad
 -\log t_J=J\log J+O_\lambda(J).
\]
Therefore \(2^Jt_J\to0\) and \(E_\lambda\) has Lebesgue measure zero and no interval. Every point is a limit of distinct subsums obtained by toggling a single sufficiently late digit, so \(E_\lambda\) is perfect. It is compact and has no interval, hence it is nowhere dense and totally disconnected, and is homeomorphic to the usual Cantor set. The covering estimate also yields Hausdorff dimension and upper box dimension zero.

**4. Sharp precision entropy.** For \(\varepsilon\downarrow0\), let \(J\) be the least integer such that \(t_J\le\varepsilon\); then \(t_J\le\varepsilon<t_{J-1}\). Prefix sums on indices \(0,\ldots,J-1\) give \(N_\lambda(\varepsilon)\le2^J\). For the reverse bound, fix all digits below \(K\) to zero, vary digits \(K,\ldots,J-2\) freely, and fix all remaining digits to zero. There are \(2^{J-1-K}\) such sums. If two differ first at position \(j\), their distance is at least \(w_j-t_{j+1}>w_j/2\), which is at least \(w_{J-2}/2\). Since
\(w_{J-2}/t_{J-1}\to\infty\), these sums are more than \(\varepsilon\) apart for large \(J\). Thus
\[
 2^{J-1-K}\le N_\lambda(\varepsilon)\le2^J.
\]
Stirling's estimate and \(t_J\le\varepsilon<t_{J-1}\) imply
\(\log(1/\varepsilon)\sim J\log J\), and consequently
\(J\sim\log(1/\varepsilon)/\log\log(1/\varepsilon)\). This proves the boxed limit.

**5. A visible gap.** If \(0<\lambda<\log2\), the mass \(w_0=e^{-\lambda}\) exceeds \(1/2\). Any subsum omitting \(w_0\) is at most \(1-w_0\); any including it is at least \(w_0\). The stated interval is therefore omitted. Even for larger \(\lambda\), the zero-dimensional Cantor structure guarantees gaps at arbitrarily small scales.

## Verification
Run `python checker.py` in the folder containing this file and the standalone checker. The checker independently enumerates all loopless directed graphs on three and four vertices for selected rational parameters, compares their exact root-degree probabilities to the binomial formula, tests all finite degree predicates, checks numerical finite-size total variation bounds, and tests eventual tail domination. Its observed output was `ALL_CHECKS_OK tested_conditions= 300`. These finite tests are diagnostic only; the proof of the infinite results is the five-step argument above.

## Relationship to prior work
Ghosh and Schwarzentruber (2026) introduce model counting and convergence questions for a much richer counting-modal logic. Their inspected uniform-graph model and branching-factor tree limits do not provide the fixed-sparsity, proposition-free degree spectrum or its precision entropy here. Jones (2011) and subsequent achievement-set literature establish general topological principles for sets of subsums; these are classical ingredients and are not claimed as new. Larrauri and Perarnau (2024) concern first-order probabilities for random graphs with prescribed degree sequences, a different ensemble and sentence-level setting. The specific joint modal, Poisson, finite-size and sharp entropy statement is the contribution examined here. No exhaustive historical-priority claim is made.

## Limitations
The parameter \(\lambda\) is fixed as \(n\to\infty\); no uniform joint limit as \(\lambda\) varies is asserted. The spectrum result applies only to proposition-free, one-step outdegree counting; it does not classify nested modalities, graph-level first-order sentences, labels, incoming neighbors, or general graph neural networks. The precision-entropy result concerns the closure of attainable probabilities, not the syntactic length of shortest formulas. The finite checker is not a proof for all parameters, and the work has not undergone independent mathematical audit.

## References
1. A. Ghosh and F. Schwarzentruber, *On Counting Graphs for Modal Logic with Counting*, arXiv:2610.26187v1 (first public version, 2026-10-19), https://arxiv.org/abs/2610.26187.
2. R. Jones, *Achievement Sets of Sequences*, American Mathematical Monthly 118 (2011), 508–521, DOI:10.4169/amer.math.monthly.118.06.508.
3. M. Kula and P. Nowakowski, *Achievement Sets of Series in \(\mathbb R^2\)*, Results in Mathematics 79, 221 (2024), DOI:10.1007/s00025-024-02239-8.
4. A. Larrauri and G. Perarnau, *First Order Logic of Sparse Graphs with Given Degree Sequences*, arXiv:2405.14836 (2024), https://arxiv.org/abs/2405.14836.
