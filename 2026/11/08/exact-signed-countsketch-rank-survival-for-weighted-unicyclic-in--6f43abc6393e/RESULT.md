# Exact signed CountSketch rank survival for weighted unicyclic incidence matrices

## Finding

**Theorem.** Let \(G\) be any finite connected simple unicyclic graph with \(n\geq3\) vertices and edges. Let its unique cycle \(C\) have length \(3\leq\ell\leq n\). Give each edge \(e\) an arbitrary positive row scale \(a_e\), orient the edges arbitrarily, and delete any one vertex column from the weighted oriented edge–vertex incidence matrix to obtain \(B\in\mathbb R^{n\times(n-1)}\). Independently hash each edge to a uniformly chosen one of \(s\geq1\) buckets, and give it an independent fair sign. Let \(S\in\mathbb R^{s\times n}\) be the resulting one-nonzero-per-column signed CountSketch matrix. Define \(F_j(s)=\prod_{i=0}^{j-1}(s-i)\) for \(0\le j\le s\), and \(F_j(s)=0\) for \(j>s\). Define

\[
T=\#\{\{e,f\}\subseteq C:e\ne f,\ a_e=a_f\},\qquad
K=\ell(n-\ell)+\binom{\ell}{2}-\frac{T}{2}.
\]

Then the **exact algebraic full-column-rank probability** is

\[
\boxed{\Pr(\operatorname{rank}(SB)=n-1)
=\frac{F_n(s)+K F_{n-1}(s)}{s^n}.}
\]

The dependence on positive edge scales is solely through the equality pattern of scales **on the cycle**, not through their numerical magnitudes or the attached tree topology. If all cycle scales are equal, then \(K=\ell(n-\ell)+\tfrac12\binom{\ell}{2}\); among all unweighted unicyclic graphs with fixed \(n\) and \(s\ge n-1\), the maximizing cycle lengths are the admissible integers nearest \((4n-1)/6\). If all cycle scales are pairwise distinct, \(K=\ell(n-\ell)+\binom{\ell}{2}\), and for \(n\ge4\) the maximizing cycle lengths are exactly \(n-1\) and \(n\). (For \(n=3\), only \(\ell=3\) is feasible.) When \(s<n-1\), all probabilities are zero and there is no strict optimizer.

Thus an arbitrarily small generic perturbation of equal cycle scales changes the exact rank-success probability at positive collision probability. It does **not** produce a comparable discontinuity in stable subspace embedding quality: the newly nonsingular sketches can be arbitrarily ill-conditioned.

## Assumptions and scope

The graph is simple, connected, undirected, and has exactly one cycle. No edge scale vanishes. The sketch uses fully independent uniform bucket assignments and independent Rademacher signs, both independently across all \(n\) edges. All ranks and singular values are over the real field in exact arithmetic. The rank event is weaker than a \((1\pm\varepsilon)\) norm-preserving subspace embedding event. The number \(s\) is a positive integer; the formula holds even when \(s<n-1\). Graph orientation, removed vertex column, cycle location, and attached tree arrangement are arbitrary.

## Proof

Let \(D\) be the unweighted oriented edge–vertex incidence matrix with any one vertex column removed. Since \(G\) is connected, \(D\) has column rank \(n-1\). Its left nullspace is one-dimensional and is spanned by an oriented unit circulation \(z\), with \(z_e\in\{+1,-1\}\) on cycle edges and \(z_e=0\) off the cycle. For \(B=\operatorname{diag}(a_e)D\), the left null vector is \(c_e=z_e/a_e\). Consequently

\[
\operatorname{col}(B)=\{x\in\mathbb R^n:c^\mathsf T x=0\}.
\]

A signed CountSketch has linearly independent nonzero rows because occupied buckets have disjoint edge supports. If \(u\) is the number of occupied buckets, then \(\dim\ker S=n-u\). Since \(\operatorname{col}(B)\) is a codimension-one hyperplane, \(SB\) has full column rank if and only if \(\ker S\cap c^\perp=\{0\}\). No collisions (\(u=n\)) always succeed; two or more bucket collisions in the sense \(n-u\ge2\) always fail by the dimension formula.

If \(u=n-1\), there is exactly one bucket holding exactly two edges \(e,f\), with all other buckets singleton. Its nullspace has generator \(\sigma_f\mathbf e_e-\sigma_e\mathbf e_f\), so full column rank is equivalent to

\[
\sigma_f c_e-\sigma_e c_f\ne0.
\]

When both edges are off the cycle the test fails. If exactly one edge lies on the cycle, the test always succeeds. If both lie on the cycle and \(a_e\ne a_f\), their nonzero circulation coefficients have unequal absolute values, so it always succeeds. If both lie on the cycle and \(a_e=a_f\), exactly one of the two possible relative signs succeeds. Thus the total effective number of successful unordered collision pairs, after averaging over signs, is \(\ell(n-\ell)+\binom\ell2-T/2=K\).

Each prescribed collision pair, with all other edges in distinct buckets, occurs with probability \(F_{n-1}(s)/s^n\). The collision-free event has probability \(F_n(s)/s^n\). The events indexed by pairs are disjoint. Summing them proves the exact formula.

For equal cycle scales, maximizing success with fixed \(n\) and \(s\ge n-1\) is equivalent to maximizing

\[
K_{\rm equal}(\ell)=\ell(n-\ell)+\frac14\ell(\ell-1)
=\ell\left(n-\frac14\right)-\frac34\ell^2.
\]

This is a strictly concave quadratic with real maximizer \((4n-1)/6\); restrict to integers \(3\le\ell\le n\). For pairwise distinct cycle scales, \(K_{\rm distinct}(\ell)=\ell(n-\ell)+\binom\ell2\), whose discrete increment is \(K_{\rm distinct}(\ell+1)-K_{\rm distinct}(\ell)=n-1-\ell\). Hence its only maximizing lengths are \(n-1,n\) for \(n\ge4\).

Finally, fix a collision of two cycle edges and signs for which equal scales cause rank loss. Perturb one edge scale by \(\delta\). If the two scales become unequal, the same hash/sign outcome becomes full rank. Yet the change in \(SB\) has operator norm at most \(\sqrt2|\delta|\), since it changes only one incidence row of norm at most \(\sqrt2\). Weyl's singular-value inequality gives \(\sigma_{\min}(SB_\delta)\le\sqrt2|\delta|\) when \(SB_0\) was singular. Therefore full rank can reappear without any uniform positive singular-value bound.

## Verification

The standalone `verify.py` performs exact Fraction-based rank elimination and compares the formula to all bucket/sign configurations in 27 scenarios with \(n=3,4\), three sketch sizes, and multiple equality patterns. It additionally performs 3,780 independently seeded, exactly ranked structural trials for \(n=5,6\) and 94 exact checks of the discrete cycle-length optimizers. Execute with `python verify.py` (Python standard library only). Its recorded output is in `verification_output.txt`.

For example, with \(n=6\), \(s=5\), the unweighted cycle of length six has exact survival probability \(36/625\); an unweighted unicyclic graph with cycle length four has \(264/3125\). If the six-cycle's six positive scales are pairwise distinct, its probability is \(72/625\), exactly twice the equal-scale value. This is an algebraic-rank benchmark; no norm-distortion estimate is implied.

## Relationship to prior work

Hu, Ubaru, Gittens, Clarkson, Horesh and Kalantzis (2021) analyze sparse graph-derived subspace embeddings and compare them with the one-nonzero-per-column CountSketch. Their arXiv manuscript (Sections 1–4) gives general high-probability norm embeddings and empirical distortion, not the present graph-incidence-specific exact rank law. Clarkson and Woodruff's foundational sparse embedding work develops generic input-sparsity sketches, not an explicit weighted-unicyclic occupancy classification. Woodruff's February 2024 course note gives a birthday-collision rank obstruction for an independent-row example; the present incidence family has exactly one row dependency, permitting specific signed collisions to preserve rank. Chen, Khanna and Li (2022) investigate graph sparsification under a different notion of incidence sketches acting on edge weights. Zhao, Kaba, Vidal, Robinson and Mallada (2018) study sparse recovery with incidence matrices and graph-cycle conditions, not the same signed row-hashing rank event in their abstract. These abstract-only comparisons are not evidence that their full texts lack related observations.

## Limitations

This classifies exact algebraic rank, **not** subspace embedding distortion, numerical rank in floating-point arithmetic, least-squares accuracy, or graph sparsification. It assumes uniform independent hash buckets and signs; limited-independence implementations need not have the same exact probability. The weighted rank jump is deliberately unstable under rounding or conditioning because the smallest singular value can vanish with the perturbation. Larger cycle rank, multigraphs, and sketches with more than one nonzero per column are not covered. Independent publication-precedence verification has not been performed; an equivalent matroid/hashed-incidence treatment could cover the claim.

## References

1. D. Hu, S. Ubaru, A. Gittens, K. L. Clarkson, L. Horesh and V. Kalantzis, *Sparse graph based sketching for fast numerical linear algebra*, arXiv:2102.05758, first public 2021-02-10, https://arxiv.org/abs/2102.05758 .
2. K. L. Clarkson and D. P. Woodruff, *Low rank approximation and regression in input sparsity time*, arXiv:1207.6365, first public 2012-07-26, https://arxiv.org/abs/1207.6365 .
3. D. P. Woodruff and N. Kocurek, *Algorithms for Big Data*, lecture notes dated 2024-02-01, https://www.cs.cmu.edu/afs/cs/user/dwoodruf/www/teaching/15851-spring24/lec6.pdf .
4. Y. Chen, S. Khanna and H. Li, *On weighted graph sparsification by linear sketching*, arXiv:2209.07729, first public 2022-09-16, https://arxiv.org/abs/2209.07729 .
5. M. Zhao, M. D. Kaba, R. Vidal, D. P. Robinson and E. Mallada, *Sparse recovery over graph incidence matrices*, arXiv:1803.09631, first public 2018-03-26, https://arxiv.org/abs/1803.09631 .
