# Critical-window coupling of careless and clumsy coupon collectors

## Finding

Fix \(c>0\). For every integer \(n>c\), let \(C^{(n)}_t\subseteq[n]\) be the **post-loss careless collector** starting from the empty set: independently at each integer time it acquires one uniform coupon and subsequently erases each held coupon independently with probability \(p_n=c/n^2\). Let \(B^{(n)}_t\subseteq[n]\) be the **clumsy collector** starting from the empty set: with probability \(\varepsilon_n=c/n\), erase one uniformly selected coupon, and otherwise acquire one uniformly selected coupon. All completion times refer to the first *post-update* time with all \(n\) coupons present; denote them by \(T_C^{(n)}\) and \(T_B^{(n)}\).

There is a coupling of these entire set-valued processes such that, for every fixed \(K\ge0\),
\[
\Pr\!\left\{\exists\,t\in\mathbb Z\cap[h_n,H_{n,K}]:C_t^{(n)}\ne B_t^{(n)}\right\}
=O_{c,K}\!\left(\frac{\log n}{\sqrt n}\right),
\qquad h_n=\left\lfloor\frac{n\log n}{2}\right\rfloor,\quad
H_{n,K}=\left\lceil n\log n+Kn\right\rceil.
\]
Consequently the distribution functions of their centered and rescaled first-completion times obey
\[
\sup_{|x|\le K}\left|\Pr\left\{\frac{T_C^{(n)}-n\log n}{n}\le x\right\}-\Pr\left\{\frac{T_B^{(n)}-n\log n}{n}\le x\right\}\right|
=O_{c,K}\!\left(\frac{\log n}{\sqrt n}\right).
\]
Using the *already established* critical-limit theorem for the clumsy model [2], the careless model therefore satisfies
\[
\frac{T_C^{(n)}-n\log n}{n}\ \Longrightarrow\ G+\tau_c.
\]
Here \(G\) is standard Gumbel, independent of \(\tau_c\), and \(\tau_c\) is the first hitting time of zero for the continuous-time birth-death chain started with \(\operatorname{Poisson}(c)\) individuals, with immigration rate \(c\) and per-individual death rate one. In particular, the non-Gumbel correction is not being claimed as new for the clumsy model: the new statement is its quantitative *pathwise* transfer to the distinct independent-erasure careless model.

## Assumptions and scope

The sampling law is uniform on \([n]\). There is a fixed constant \(c>0\) and \(n\to\infty\) with \(n>c\); on each careless round, independent erasures occur **after** acquisition, and the first completion is checked after erasures. The clumsy erasure probability is \(c/n\), not \(c/n^2\): the two models are compared at the matched total expected number of erasure marks per round. No claim is made for fixed positive per-coupon erasure probabilities, nonuniform coupons, or the convergence of completion-time moments. The coupling is stated at the level of labelled *sets*, not merely their sizes.

For finite \(n\), abbreviate
\[
\varepsilon=\frac cn,\quad p=\frac c{n^2}=\frac\varepsilon n,\quad
\alpha=1-\frac1n,\quad\beta=1-\frac{1-\varepsilon}{n},\quad
\delta=\varepsilon\big[1-(1-p)^{n-1}\big].
\]

## Proof

**1. Coupled loss-set laws.** Independently each round, draw a uniform acquisition label \(A\). A clumsy loss set \(D^0\) is empty with probability \(1-\varepsilon\) and each singleton \(\{j\}\) has probability \(\varepsilon/n=p\). A careless loss set \(D^1\) consists of independent Bernoulli-\(p\) labels. A maximal coupling of \(D^0,D^1\), independent of \(A\), has mismatch probability exactly
\[
\lVert\mathcal L(D^0)-\mathcal L(D^1)\rVert_{\mathrm{TV}}
=\varepsilon\big[1-(1-p)^{n-1}\big]=\delta\le\frac{c^2}{n^2}.
\tag{1}
\]
Indeed the overlap masses are \(1-\varepsilon\) at the empty set and \(np(1-p)^{n-1}\) over singleton sets; other sets have zero mass under \(D^0\). The inequality follows from the union bound for the \(n-1\) possible additional loss marks. Couple the pairs independently over rounds. The process obtained by adding \(A\) and then removing \(D^1\) has exactly the careless law, regardless of which labels were present before removal.

**2. An intermediate dominating process.** Given the common \(A_t,D^0_t\), construct \(V_t\) by **always** inserting \(A_t\) and then removing \(D^0_t\). Construct \(B_t\) by inserting \(A_t\) only when \(D^0_t=\varnothing\); when \(D^0_t=\{j\}\), it instead erases \(j\) with no insertion. Starting both empty, \(B_t\subseteq V_t\) at every time, because the two updates are monotone in their input sets. When \(D^0_s=D^1_s\) for all \(s\le t\), \(C_s=V_s\) for every \(s\le t\). A discrepancy \(V_t\setminus B_t\) can arise only at a clumsy loss round \(s\) when the auxiliary acquisition label \(A_s\) is absent from \(B_{s-1}\). It ceases to be a discrepancy once that label is next acquired on a nonloss round (possibly earlier via an erasure).

**3. A one-label marginal and the pointwise discrepancy bound.** Because the clumsy chain refreshes a selected coupon to absent with probability \(\varepsilon\) and to present otherwise, for each fixed label \(j\) its exact probability of being absent at time \(s\) is
\[
 u_s:=\Pr(j\notin B_s)=\varepsilon+(1-\varepsilon)\alpha^s.
\tag{2}
\]
A given label avoids successful acquisition over \(r\) subsequent rounds with probability \(\beta^r\). Therefore a union bound over all possible births of discrepancies yields, for every integer \(t\ge1\),
\[
\begin{aligned}
\Pr(B_t\ne V_t)
&\le\varepsilon\sum_{s=1}^t u_{s-1}\beta^{t-s}\\
&\le\frac{\varepsilon^2n}{1-\varepsilon}
+\varepsilon(1-\varepsilon)t\beta^{t-1},
\end{aligned}
\tag{3}
\]
where \(\alpha\le\beta\) was used in the geometric sum. The acquisition events after the discrepancy's creation are independent of its past, justifying the \(\beta^{t-s}\) factor even though the full set process is dependent over time.

**4. Entire critical-window coupling, with an explicit finite bound.** For integers \(1\le h\le H\), if \(B_h=V_h\) and no later loss step creates an extra acquisition, then \(B_t=V_t\) throughout \([h,H]\). Equations (1)–(3) and monotonicity of \(u_s\) imply the **finite-\(n\) certificate**
\[
\begin{split}
\Pr\{\exists t\in[h,H]:B_t\ne C_t\}\le{}&H\delta+\frac{\varepsilon^2n}{1-\varepsilon}
+\varepsilon(1-\varepsilon)h\beta^{h-1}\\
&+\varepsilon(H-h)\big[\varepsilon+(1-\varepsilon)\alpha^h\big].
\end{split}
\tag{4}
\]
Set \(h=h_n=\lfloor n\log n/2\rfloor\) and \(H=H_{n,K}=\lceil n\log n+Kn\rceil\), with \(K\) fixed. Then \(H=O_K(n\log n)\), \(\delta=O_c(n^{-2})\), \(\alpha^h=O(n^{-1/2})\), and \(\beta^{h-1}=O_c(n^{-1/2})\). The right side of (4) is \(O_{c,K}(\log n/\sqrt n)\). This proves the pathwise assertion.

**5. Transfer from paths to first completion.** Couple both models to the same independent uniform proposed acquisitions \(A_t\), including unused proposals on loss rounds. If either collector becomes complete before time \(h\), all \(n\) labels must already have appeared among \(A_1,\ldots,A_h\). Let \(M_h\) count labels still unseen in this classical collection. Then
\[
\mathbb EM_h=n\alpha^h,\qquad
\operatorname{Var}(M_h)\le n\alpha^h,
\]
because the pairwise unseen-label covariance is nonpositive: \((1-2/n)^h\le\alpha^{2h}\). Chebyshev gives
\[
\Pr(M_h=0)\le\frac1{n\alpha^h}.
\tag{5}
\]
If neither collector completed before \(h\), and their entire configurations agree on \([h,H]\), their first-completion events through any \(t\in[h,H]\) coincide. Hence, for every such \(t\),
\[
\begin{split}
\left|\Pr(T_C\le t)-\Pr(T_B\le t)\right|
\le{}&\frac2{n\alpha^h}+H\delta+\frac{\varepsilon^2n}{1-\varepsilon}\\
&+\varepsilon(1-\varepsilon)h\beta^{h-1}
+\varepsilon(H-h)\big[\varepsilon+(1-\varepsilon)\alpha^h\big].
\end{split}
\tag{6}
\]
With \(h=h_n\), the first term is \(O(n^{-1/2})\); all other terms have the bound established above. This is the uniform centered first-completion distribution comparison for fixed compact intervals of \(x\).

**6. Limit law.** Attrill and Garoni [2, Theorem 4.10] prove \((T_B^{(n)}-n\log n)/n\Rightarrow G+\tau_c\) for this clumsy process with \(\varepsilon_n=c/n\). Equation (6) transfers its distribution functions at every continuity point to the careless process. The limit therefore holds with exactly the same independent Gumbel and immigration–death first-zero law. This step *uses* the earlier theorem; it is not a separate derivation of its critical limit.

## Verification

The standalone file `checker.py` contains exact-rational checks of: the full loss-set total-variation identity (1) for finite values of \(n,c\); the clumsy single-label marginal (2); the set inclusion \(B_t\subseteq V_t\) and both marginals of the coupled Markov chain; the pointwise upper bound (3); and the independent-erasure transition law. Execute `python checker.py` from the directory containing the file. The checker ran successfully with **1,813 exact-rational assertions**. These finite checks do not replace the all-\(n\) coupling proof, Chebyshev estimate or cited limit theorem.

## Relationship to prior work

Cruciani and Dudeja [1] introduce the post-loss careless collector and study expected completion-time scales and metastability. Attrill and Garoni [2] establish the critical \(G+\tau_c\) distribution for the *clumsy*, single-label-refresh collector. Long [3] proves fixed-positive-loss stationary-entry laws for the careless and clumsy models, not the \(p_n=c/n^2\) critical window. The present result is a quantitative coupling **between** the two different dynamics over the entire completion window, transferring [2]'s limiting distribution to the original careless model. In particular, [2]'s theorem by itself has different update rules and does not imply the careless conclusion without a comparison argument. Related reset-type coupon collectors operate through global resets rather than independent per-label erasure, so their renewal laws do not supply this pathwise comparison.

## Limitations

The source-model limit for the clumsy process is invoked from [2], not independently re-proved. The discrepancy probability is bounded in the indicated window and need not be small over arbitrary earlier or supercritical times. The \(O_{c,K}\) constant may depend on the fixed loss-intensity \(c\) and window radius \(K\). The conclusion is weak convergence only; it does not assert expectation convergence, optimality of the coupling error, or any result for nonuniform sampling and more frequent losses. Earlier general perturbation or coupling results might encompass the statement implicitly; definitive bibliographic priority has not been established by the available comparison.

## References

[1] E. Cruciani and A. Dudeja, *The Careless Coupon Collector's Problem*, arXiv:2602.20705 (first posted 2026-02-24), https://arxiv.org/abs/2602.20705.

[2] L. J. Attrill and T. M. Garoni, *The Clumsy Coupon Collector's Problem*, arXiv:2605.14206 (first posted 2026-05-14), especially Lemma 4.9 and Theorem 4.10, https://arxiv.org/abs/2605.14206.

[3] C. D. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors*, arXiv:2605.14511 (first posted 2026-05-14), especially Sections 4 and 5, https://arxiv.org/abs/2605.14511.
