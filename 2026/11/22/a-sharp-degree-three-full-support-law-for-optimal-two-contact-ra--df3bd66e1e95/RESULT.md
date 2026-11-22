# A sharp degree-three full-support law for optimal two-contact randomized averaging

## Finding

Let \(G=(V,E)\) be any finite connected undirected **simple** graph, with \(n=|V|\ge2\), \(m=|E|\ge1\). At each of exactly two contacts, choose an edge independently from the same probability vector \(p\) and replace its two endpoint opinions by their arithmetic mean. If the initial mean-zero disagreement has covariance \(I-\mathbf1\mathbf1^{\mathsf T}/n\), minimize the expected squared disagreement after these two contacts over all \(p_e\ge0\) with \(\sum_ep_e=1\).

**Theorem.** If the maximum graph degree is at most three, the optimizer exists, is unique, and has **strictly positive probability on every edge**. More precisely, if \(C\) is the unsigned vertex-edge incidence matrix, \(Q=CC^{\mathsf T}\) its signless Laplacian, and
\[
 w=(2I+Q)^{-1}\mathbf1,\qquad
 Z=\sum_{\{u,v\}\in E}(w_u+w_v),
\]
then
\[
 \boxed{\ p_{\{u,v\}}^*=\frac{w_u+w_v}{Z}\ge\frac{1}{6m}>0\quad\text{for all }\{u,v\}\in E.\ }
\]
The maximum-degree cutoff three is sharp: the connected balanced double-star consisting of two adjacent hubs with three leaves at each hub (maximum degree four) has the **unique** two-contact optimizer with probability \(1/6\) on each of its six leaf edges and probability zero on the hub-to-hub bridge. Consequently its uniquely optimal sampling support is disconnected.

As an exact family-wide refinement, for the balanced double-star with \(k\ge1\) leaves at each hub, its unique optimizer gives every leaf edge probability \(a_k\) and the bridge probability \(b_k\), where
\[
 (a_k,b_k)=\begin{cases}
 \left(\dfrac{3}{5k+3},\dfrac{3-k}{5k+3}\right),&k=1,2,\\[4pt]
 \left(\dfrac{1}{2k},0\right),&k\ge3.
 \end{cases}
\]
At the sharp boundary \(k=3\), a bridge probability \(b\) with uniform leaf probabilities \((1-b)/6\) incurs the exact strictly positive excess \(3b^2/4\) in the two-contact objective.

## Assumptions and scope

The graph is finite, connected and simple, unweighted as a contact topology. Edge selection is fixed and independent with replacement, and exactly two pairwise arithmetic-mean updates are made. The random initial disagreement \(X_0\) has expectation zero and covariance \(\operatorname{Cov}(X_0)=I-\mathbf1\mathbf1^{\mathsf T}/n\); a centered isotropic field on the zero-sum subspace suffices. We minimize \(\mathbb E\|X_2\|_2^2\), including expectation over the two independently drawn edges and the initial field, not the worst-case initial state, long-run spectral rate, deterministic sweep, or per-vertex variance. The formula is asserted only for maximum degree at most three; the double-star is a sharp counterexample to universal full support at degree four, not a characterization of every higher-degree graph.

## Proof

**1. Exact two-contact objective and strict convexity.** For an edge \(e=\{u,v\}\), put \(b_e=e_u-e_v\) and \(P_e=I-b_eb_e^{\mathsf T}/2\). Each \(P_e\) is a symmetric projection fixing \(\mathbf1\). For independent \(e,f\) drawn according to \(p\), cyclicity of trace and \(P_e^2=P_e\) yield
\[
 \mathbb E\|P_fP_eX_0\|^2
 =\sum_{e,f}p_ep_f\bigl(\operatorname{tr}(P_eP_f)-1\bigr)
 =n-3+p^{\mathsf T}Ap,
\]
where \(A_{ee}=1\), \(A_{ef}=1/4\) if distinct edges share one endpoint, and \(A_{ef}=0\) otherwise. Since the unsigned incidence matrix \(C\) satisfies \((C^{\mathsf T}C)_{ee}=2\) and \((C^{\mathsf T}C)_{ef}=1\) for adjacent distinct edges,
\[
 A=\frac12 I_m+\frac14 C^{\mathsf T}C\succ0.
\]
Thus the quadratic objective is strictly convex on the probability simplex, and there is exactly one global minimizer.

**2. Interior stationary solution from the signless resolvent.** Put \(d=C\mathbf1_m\), the vertex-degree vector, and \(Q=CC^{\mathsf T}\). If \(Ap=\lambda\mathbf1_m\), then with \(t=4\lambda\) and \(s=Cp\),
\[
 2p+C^{\mathsf T}s=t\mathbf1_m,\qquad
 (2I_n+Q)s=td.
\]
Because \(Q\mathbf1_n=2d\), the unique solution is
\[
 s=t\bigl(\mathbf1_n/2-w\bigr),\qquad
 w=(2I_n+Q)^{-1}\mathbf1_n,
\]
and hence \(p_{\{u,v\}}=t(w_u+w_v)/2\). Whenever all sums \(w_u+w_v\) are positive, normalization gives the stated \(p^*\), an interior stationary point of a strictly convex problem, hence its unique global optimizer.

**3. Subcubic positivity via a contraction.** Suppose every vertex degree \(d_v\) lies in \(\{1,2,3\}\), as it must for a connected graph with at least two vertices and maximum degree at most three. The linear system \((2I+Q)w=\mathbf1\) is the fixed-point equation
\[
 w_v=F_v(w):=\frac{1-\sum_{u\sim v}w_u}{d_v+2}.
\]
On the closed cube \(\mathcal K=[0,1/3]^V\), each coordinate \(F_v(w)\) lies in \([0,1/3]\): its numerator lies between \(1-d_v/3\ge0\) and \(1\), while \(d_v+2\ge3\). Moreover,
\[
 \|F(x)-F(y)\|_\infty
 \le\max_v\frac{d_v}{d_v+2}\|x-y\|_\infty
 \le\frac35\|x-y\|_\infty.
\]
Therefore the unique fixed point \(w\) lies in \(\mathcal K\). For an arbitrary edge \(uv\), the fixed-point equations and the upper bound on the other neighbors imply
\[
 (d_u+2)w_u+w_v\ge1-\frac{d_u-1}{3}\ge\frac13,
\qquad
 w_u+(d_v+2)w_v\ge\frac13.
\]
Adding and using \(d_u,d_v\le3\) gives \(6(w_u+w_v)\ge2/3\), or \(w_u+w_v\ge1/9\). On the other hand, \(Z\le2m/3\). Hence every normalized probability obeys
\[
 p^*_{uv}\ge\frac{1/9}{2m/3}=\frac{1}{6m}>0.
\]
This finishes the universal subcubic statement.

**4. Sharp degree-four obstruction.** In the balanced double-star with \(k\) private leaves on either hub, strict convexity and graph automorphisms force all \(2k\) leaf-edge probabilities to equal \(a\), with bridge probability \(b\), so \(2ka+b=1\). The gradient quantity \((Ap)_e\) is \(((k+3)a+b)/4\) on every leaf edge, and \(b+ka/2\) on the bridge. An interior stationary point would require \((3-k)a=3b\), giving \(a=3/(5k+3)\) and \(b=(3-k)/(5k+3)\). It is feasible and unique for \(k=1,2\). When \(k\ge3\), the boundary point \(a=1/(2k),b=0\) satisfies the exact simplex KKT condition: each active leaf edge has gradient quantity \((k+3)/(8k)\), while the bridge has \(1/4\), not smaller; the inequality is equality at \(k=3\) and strict for \(k>3\). Positive definiteness of \(A\) proves global uniqueness even at equality. For \(k=3\), substitution gives \(p^{\mathsf T}Ap=1/4+3b^2/4\), establishing the quadratic bridge penalty and sharp cutoff.

## Verification

The accompanying standalone `check.py` uses standard-library exact rational arithmetic and direct linear solves. It enumerates **all labeled connected simple subcubic graphs on 2 through 5 vertices**, tests the resolvent bounds, the uniform positive lower bound, and the exact first-order stationarity equations, and adds the cube, \(K_{3,3}\), Petersen graph, eight balanced double-stars, and an exact four-vertex path benchmark. It reports 526 exact graph cases; the universal statement is proved analytically above, not inferred from this finite list. Run `python check.py` after extracting it alongside this document.

## Relationship to prior work

Boyd, Ghosh, Prabhakar and Shah introduced the independent-edge arithmetic-averaging matrices and optimize the **asymptotic spectral convergence rate** using an SDP. Their 2004 conference paper, Section IV, optimizes the second largest eigenvalue, not the expected isotropic squared error after exactly two contacts, and does not give the signless-resolvent positivity criterion or the degree-three support threshold. The 2013 paper *Towards optimal convex combination rules for gossiping* optimizes **the averaging coefficient** for periodically repeated deterministic schedules, not probabilities of independently selected edges. An earlier two-contact path calculation establishes the strictly convex quadratic objective and an explicit path-specific optimum. That result supplies the same two-step reduction but does not imply the signless-resolvent formula or the support guarantee over every subcubic graph; the path is a special case and the sharp degree-four counterexample is not a path. A separate double-star spectral-width design studies a different eigenvalue objective, so its bridge-deletion result does not imply this two-contact isotropic-optimality theorem.

## Limitations

The result does not assert long-run convergence of the degree-four boundary optimizer: indeed its optimal support is disconnected. It is not a worst-case initial-vector theorem, and its fixed-iid selection premise matters. At maximum degree four or above, some graphs still have full-support optima, so the bound is a sharp **universal** degree cutoff rather than an if-and-only-if test for each graph. The exact graph family and universal contraction proof are self-contained; undiscovered equivalent formulations of finite-horizon gossip sampling remain a bibliographic risk. No independent mathematical audit has been carried out.

## References

1. S. Boyd, A. Ghosh, B. Prabhakar, D. Shah, *Analysis and Optimization of Randomized Gossip Algorithms*, 43rd IEEE CDC (December 2004), freely accessible conference paper: https://web.stanford.edu/~boyd/papers/pdf/gossip_opt.pdf ; IEEE Xplore DOI https://doi.org/10.1109/CDC.2004.1429652 (listed online May 16, 2005).
2. S. Boyd, A. Ghosh, B. Prabhakar, D. Shah, *Randomized Gossip Algorithms*, IEEE Trans. Inform. Theory 52 (2006), 2508–2530: https://web.stanford.edu/~boyd/papers/gossip.html ; https://doi.org/10.1109/TIT.2006.874516.
3. *Towards optimal convex combination rules for gossiping*, 2013 conference work, full text at https://www.researchgate.net/publication/261162372_Towards_optimal_convex_combination_rules_for_gossiping.
