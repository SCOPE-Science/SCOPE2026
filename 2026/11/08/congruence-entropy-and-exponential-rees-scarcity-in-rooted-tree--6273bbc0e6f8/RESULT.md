# Congruence entropy and exponential Rees scarcity in rooted-tree graph inverse semigroups

## Finding

Let \(T\) be a finite rooted tree with every edge directed away from the root, and let \(G(T)\) be its graph inverse semigroup. Write \(\mathcal C(T)\) for its congruence set. For a congruence represented by an acyclic Wang pair \((H,W)\), let \(|H|\) be the number of vertices collapsed into the zero ideal and \(|W|\) the number of eligible vertices selected for a non-Rees identification. Define
\[
F_T(u,v)=\sum_{\rho\in\mathcal C(T)}u^{|H(\rho)|}v^{|W(\rho)|}.
\]
For the rooted child subtrees \(T_1,\ldots,T_d\), with \(n_i=|V(T_i)|\), the polynomial satisfies the exact branching identity
\[
\boxed{F_T(u,v)=u^{|V(T)|}+\prod_{i=1}^{d}F_{T_i}(u,v)
+v\sum_{i=1}^{d}\bigl(F_{T_i}(u,v)-u^{n_i}\bigr)
\prod_{j\ne i}u^{n_j}.}
\]
The empty product is \(1\); for one vertex \(F_T(u,v)=1+u\). Thus this polynomial counts every congruence, not only Rees congruences, on every finite outward-oriented rooted tree.

For the complete outward \(b\)-ary tree \(T_{b,h}\) of height \(h\), suppose \(b\ge2\), and put
\[
N_h=|V(T_{b,h})|=\frac{b^{h+1}-1}{b-1},\quad
C_h=|\mathcal C(T_{b,h})|,\quad
R_h=\#\{\text{Rees congruences on }G(T_{b,h})\}.
\]
Then \(C_0=R_0=2\) and, for every integer \(h\ge0\),
\[
\boxed{C_{h+1}=1+C_h^b+b(C_h-1),\qquad R_{h+1}=1+R_h^b.}
\]
The limits
\[
\lambda_b=\lim_{h\to\infty}b^{-h}\log C_h,\quad
\mu_b=\lim_{h\to\infty}b^{-h}\log R_h,\quad
\kappa_b=\lambda_b-\mu_b
\]
exist, are finite, and satisfy \(\kappa_b>0\). In fact the probability that a uniformly selected congruence is Rees has the sharp form
\[
\boxed{\frac{R_h}{C_h}=\exp\bigl(-\kappa_b b^h+o(1)\bigr).}
\]
Equivalently it decays exponentially in the number \(N_h\) of vertices, at rate \(\kappa_b(b-1)/b>0\). For instance, \(\kappa_2\approx0.221043134102127\) and the per-vertex rate is approximately \(0.110521567051064\).

## Assumptions and scope

A graph inverse semigroup is the inverse semigroup with zero whose nonzero elements are formal products \(\alpha\beta^{-1}\) for finite directed paths with a common terminal vertex, subject to the usual prefix-cancellation multiplication. A *congruence* is a multiplication-compatible equivalence relation on this entire semigroup. A *Rees congruence* collapses one ideal to one class and leaves elements outside it as singleton classes. The orientation, finite acyclicity, and lack of loops or multiple edges are essential to the stated tree decomposition. All congruences are counted as distinct relations, without quotienting by graph automorphisms.

The acyclic specialization of Wang's graph-congruence classification [1] provides a bijection between congruences and pairs \((H,W)\), where \(H\) is hereditary (if a directed edge starts in \(H\), its endpoint also lies in \(H\)) and \(W\) is *any* subset of those vertices in \(V(T)\setminus H\) with exactly one outgoing edge into \(V(T)\setminus H\). The third, cycle-data component in Wang's general classification is absent because the graph has no directed cycles. Under this classification, Rees congruences are exactly those with \(W=\varnothing\). This foundational classification is prior mathematics, not part of the novelty claim.

## Proof

**1. Branching identity.** Let \(r\) be the root and \(T_1,\ldots,T_d\) its outgoing child subtrees. If \(r\in H\), heredity forces \(H=V(T)\) and \(W=\varnothing\), contributing \(u^{|V(T)|}\). If \(r\notin H\), each child subtree receives an independently admissible pair \((H_i,W_i)\). If \(r\notin W\), these choices contribute \(\prod_iF_{T_i}\). If \(r\in W\), exactly one child root must remain outside \(H\), because this is exactly the condition that the root have one outgoing edge into the complement. Choose that child \(i\); its subtree contributes \(F_{T_i}-u^{n_i}\), because its root belongs to \(H_i\) only for the all-hereditary choice. Every other child root belongs to \(H_j\), forcing the entire child subtree into \(H_j\), contributing \(u^{n_j}\). The factor \(v\) marks \(r\in W\). The three cases are disjoint and exhaustive, proving the formula with all coefficient multiplicities.

**2. Complete branching.** In \(T_{b,h+1}\) the root has \(b\) identical child subtrees of height \(h\). Substitution gives the polynomial recurrence
\[
F_{h+1}(u,v)=u^{1+bN_h}+F_h(u,v)^b+bv\,u^{(b-1)N_h}\bigl(F_h(u,v)-u^{N_h}\bigr),\qquad F_0=1+u.
\]
Evaluating at \((u,v)=(1,1)\) produces the claimed recurrence for \(C_h\). Setting \(v=0\) and then \(u=1\) gives \(R_h\), because it selects exactly pairs with \(W=\varnothing\).

**3. Existence and sharpness of entropy constants.** Define
\[
\varepsilon_h=\log\left(1+\frac{b(C_h-1)+1}{C_h^b}\right),\qquad
\delta_h=\log\left(1+R_h^{-b}\right).
\]
Then \(\log C_{h+1}=b\log C_h+\varepsilon_h\) and \(\log R_{h+1}=b\log R_h+\delta_h\). Both sequences \(C_h,R_h\) grow to infinity and both \(\varepsilon_h,\delta_h\) are positive and tend to zero. Therefore the absolutely convergent series
\[
\lambda_b=\log2+\sum_{h\ge0}b^{-h-1}\varepsilon_h,\qquad
\mu_b=\log2+\sum_{h\ge0}b^{-h-1}\delta_h
\]
are the stated limits. More precisely,
\[
0\le\lambda_b b^h-\log C_h
=\sum_{k\ge h}b^{h-k-1}\varepsilon_k
\le\frac{\sup_{k\ge h}\varepsilon_k}{b-1}\longrightarrow0,
\]
and the same calculation holds with \(\mu_b,R_h,\delta_h\). Subtracting establishes the stated ratio with \(o(1)\) in its exponent, not merely an unspecified subexponential factor.

**4. Strict entropy gap.** At height one,
\[
C_1=2^b+b+1,\qquad R_1=2^b+1.
\]
Since \(\varepsilon_h>0\), \(\lambda_b\ge b^{-1}\log C_1\). Since \(R_h\) increases, \(\delta_h\le\log(1+R_1^{-b})\) for \(h\ge1\), so
\[
\mu_b\le b^{-1}\log R_1+
\frac{\log(1+R_1^{-b})}{b(b-1)}.
\]
Consequently
\[
\boxed{\kappa_b\ge\frac1b\log\left(1+\frac{b}{2^b+1}\right)-\frac1{b(b-1)}\log\left(1+(2^b+1)^{-b}\right)>0.}
\]
The final strict inequality follows because \(b/(2^b+1)>(2^b+1)^{-b}\) and \(b-1\ge1\). Since \(b^h=((b-1)N_h+1)/b\), the same limit yields a strictly positive decay rate per tree vertex. This completes the proof.

## Verification

Running `python3 verify.py` prints `VERIFY_OK`. The verifier uses two different counting representations: direct enumeration of hereditary subsets and eligible \(W\)-subsets on complete binary trees through height three and ternary trees through height two; and an independent symbolic polynomial recursion. Their complete bivariate coefficient arrays agree. It also constructs multiplication tables of the corresponding graph inverse semigroups and independently enumerates *all* equivalence relations for three small graphs, retaining only congruences under left and right multiplication. These direct semigroup checks agree with the Wang counts, including the two-leaf fork with exactly \(7\) congruences and \(5\) Rees congruences.

For complete binary trees the exact pairs \((C_h,R_h)\) at heights \(0,1,2,3\) are respectively \((2,2),(7,5),(62,26),(3967,677)\); for complete ternary trees at heights \(0,1,2\) they are \((2,2),(12,9),(1762,730)\). Finite checks do not establish the infinite-height convergence; the series and inequalities above do.

## Relationship to prior work

Wang [1] provides the general congruence-triple classification and thus the underlying bijection used in the proof; Mesyan and Mitchell [2] explain the existence and structural role of non-Rees congruences on graph inverse semigroups. Luo, Wang, and Wei [3] analyze congruence-lattice distributivity, and Anagnostopoulou-Merkouri, Mesyan, and Mitchell [4] characterize further lattice properties. None of the inspected pertinent statements provides the displayed bivariate tree polynomial, the complete-branching numerical recursion, or the positive sharp Rees-scarcity entropy constant. The conclusion is an enumerative and asymptotic refinement of known structural classification, not an independent classification of congruences.

## Limitations

The general polynomial formula assumes a finite rooted out-arborescence. The entropy theorem assumes a fixed integer branching factor \(b\ge2\) and height tending to infinity; it does not address arbitrary sequences of graphs or orientations. The proof relies on the established Wang classification. Priorities may be affected by unlocated enumerative consequences of that classification or other broader results. Computational checks are finite and are not an independent audit.

## References

[1] Zheng-Pan Wang, *Congruences on graph inverse semigroups* (first public 2018-06-28), arXiv:1806.10721, https://arxiv.org/abs/1806.10721.

[2] Zachary Mesyan and James D. Mitchell, *The Structure of a Graph Inverse Semigroup* (first public 2014-09-15), arXiv:1409.4380, https://arxiv.org/abs/1409.4380.

[3] Yongle Luo, Zhengpan Wang, and Jiaqun Wei, *Distributivity in congruence lattices of graph inverse semigroups* (first public 2023-03-28), arXiv:2303.15797, https://arxiv.org/abs/2303.15797.

[4] Marina Anagnostopoulou-Merkouri, Zachary Mesyan, and James D. Mitchell, *Properties of congruence lattices of graph inverse semigroups* (first public 2021-08-18), arXiv:2108.08277, https://arxiv.org/abs/2108.08277.
