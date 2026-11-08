# Exact essential norms of finite composition sums on discrete Hardy trees

## Finding

Let \(1\le p<\infty\), let \(T\) be a \((q+1)\)-homogeneous rooted tree, \(q\ge2\), and let \(Q=\sum_{i=1}^{r}a_i C_{\phi_i}\) be a finite complex linear combination of individually bounded composition operators on the discrete Hardy space \(\mathbb T_p\). For each pair of vertices define the aggregate coefficient \(A(v,w)=\sum_{i:\phi_i(v)=w}a_i\), and for levels \(n,m\) let \(A_{n,m}=(A(v,w))_{v\in D_n,w\in D_m}\).

With \(c_n=|D_n|\), the adjoint exponent \(p'=p/(p-1)\) for \(p>1\), and \(p'=\infty\) for \(p=1\), the **exact essential norm** is

\[
\boxed{\|Q\|_{\mathrm{ess}}=\lim_{R\to\infty}\sup_{n\ge0}\;\sup_{\|y\|_{\ell^{p'}(D_n)}\le1}\frac{1}{c_n^{1/p}}\sum_{m>R}c_m^{1/p}\|A_{n,m}^{*}y\|_{\ell^{p'}(D_m)}.}
\]

For each fixed \(n\) the sum is finite, and \(A_{n,m}^{*}\) is the conjugate transpose. In particular, for any bounded single composition operator \(C_\phi\), writing \(N_\phi(n,w)=|\{v\in D_n:\phi(v)=w\}|\),

\[
\boxed{\|C_\phi\|_{\mathrm{ess}}^{p}=\lim_{R\to\infty}\sup_{n\ge0}\frac1{c_n}\sum_{m>R}c_m\max_{w\in D_m}N_\phi(n,w).}
\]

An empty sum is zero. These identities include operators with cancellations among symbols and give exact nonzero values, not merely a compactness test.

As a quantitative contrast with the exponent-independent compactness theorem, on the \(4\)-homogeneous tree there are sphere-preserving bijections \(\tau\) for which \(I-C_\tau\) has essential norm \(2\) on \(\mathbb T_1\) but \(\sqrt3\) on \(\mathbb T_2\).

## Assumptions and scope

The root is denoted \(o\), the level \(D_n=\{v\in T:|v|=n\}\), and \(c_0=1\), \(c_n=(q+1)q^{n-1}\) for \(n\ge1\). Define

\[
\mathbb T_p=\{f:T\to\mathbb C:\|f\|_p:=\sup_{n\ge0}(c_n^{-1}\sum_{v\in D_n}|f(v)|^p)^{1/p}<\infty\}.
\]

For a self-map \(\phi:T\to T\), \(C_\phi f=f\circ\phi\). Each \(C_{\phi_i}\) is assumed bounded; the coefficients \(a_i\in\mathbb C\) may vanish or cancel. The norm \(\|Q\|_{\mathrm{ess}}\) means the distance to compact linear operators on the full Banach space \(\mathbb T_p\). No tree-continuity or graph-homomorphism assumption is imposed on \(\phi_i\). The formula is for \(1\le p<\infty\), not for the quasi-Banach range or the distinct little Hardy subspace.

## Proof

**1. Finite-block structure.** The normalized restrictions to levels identify \(\mathbb T_p\) isometrically with the \(\ell_\infty\)-sum of finite-dimensional spaces \(E_m=(\mathbb C^{D_m},c_m^{-1/p}\ell^p(D_m))\). Let \(P_R f\) equal \(f\) on the first \(R+1\) levels and zero elsewhere. Every \(P_R\) is a norm-one finite-rank projection. Since each fixed output vertex \(v\) samples only the finitely many vertices \(\phi_1(v),\ldots,\phi_r(v)\), the output restriction of \(Q(I-P_R)\) to a given finite level \(D_n\) involves finitely many input levels.

**2. Exact finite dual problem.** The norm of the map from the input \(\ell_\infty\)-sum of blocks \(E_m\), \(m>R\), into \(E_n\) is, by finite-dimensional duality,

\[
\frac1{c_n^{1/p}}\sup_{\|y\|_{p'}\le1}\sum_{m>R}c_m^{1/p}\|A_{n,m}^{*}y\|_{p'}.
\]

Indeed \(\|z\|_{\ell^p(D_n)}=\sup_{\|y\|_{p'}\le1}|\langle z,y\rangle|\). For a fixed dual vector, each input block may be independently chosen with \(\ell^p\)-norm at most \(c_m^{1/p}\) and phase aligned to attain its dual norm; only finitely many blocks occur. Taking the supremum over output levels gives exactly \(\|Q(I-P_R)\|\). These norms decrease in \(R\); denote their limit by \(L\).

**3. Upper essential bound.** The operator \(QP_R\) is finite rank, so \(\|Q\|_{\mathrm{ess}}\le\|Q-QP_R\|=\|Q(I-P_R)\|\) for each \(R\). Hence \(\|Q\|_{\mathrm{ess}}\le L\).

**4. Matching lower bound.** Choose recursively increasing cutoffs \(R_j\) and finitely supported unit vectors \(f_j\), each supported entirely above \(R_j\), with disjoint level supports and \(\|Qf_j\|\ge L-1/j\). This is possible because the norm \(\|Q(I-P_{R_j})\|\) is a supremum over finite output rows; a nearly maximizing row uses only finitely many input vertices, and after choosing \(f_j\) the next cutoff may lie beyond its support. Disjoint level supports make \((t_j)\mapsto\sum_j t_jf_j\) an isometric embedding of \(c_0\) into \(\mathbb T_p\); the sum converges in the \(\mathbb T_p\) norm for \((t_j)\in c_0\). Since the canonical basis of \(c_0\) is weakly null, so is \((f_j)\) in \(\mathbb T_p\). Every compact operator \(K\) sends \(f_j\) to a norm-null sequence. Thus \(\|Q-K\|\ge\limsup_j\|(Q-K)f_j\|\ge L\). Taking the infimum over compact \(K\) proves equality.

**5. Single-symbol reduction.** For \(Q=C_\phi\), the restriction of \(C_\phi(I-P_R)\) to \(D_n\) partitions the output coordinates by their sampled input vertex. Under independent unit-ball constraints on each input sphere, the \(p\)-th output norm is largest when each input sphere places its entire \(p\)-mass \(c_m\) at a vertex \(w\in D_m\) maximizing \(N_\phi(n,w)\). Its normalized value is exactly \(c_n^{-1}\sum_{m>R}c_m\max_{w\in D_m}N_\phi(n,w)\). Supremizing over \(n\), then taking the limit, gives the second boxed identity.

**6. Sharp examples.** First, fix \(w\in D_2\) and let \(\phi(v)=w\) on \(D_2\) and \(\phi(v)=v\) elsewhere. Then \(C_\phi-I\) has finite rank, so \(\|C_\phi\|_{\mathrm{ess}}=1\), while \(\|C_\phi\|=c_2^{1/p}\), a strict discrepancy. Second, take \(q=3\) and define \(\tau\) to fix the first two levels and cyclically permute the three children of each vertex within every subsequent level. This is a levelwise bijection. The operator \(I-C_\tau\) is the \(\ell_\infty\)-sum of blocks \(I-P_3\), where \(P_3\) cyclically permutes three coordinates. The \(\ell^1\)-operator norm of this block is \(2\), while \((I-P_3)^*(I-P_3)=3I-J\) gives \(\ell^2\)-operator norm \(\sqrt3\). Such blocks recur on arbitrarily high levels, so the essential-norm identity yields exactly \(2\) and \(\sqrt3\), respectively.

## Verification

All estimates above are analytic and quantify over every cutoff and all levels. The accompanying pure-Python exact finite checker reconstructs sample level matrices and coefficient multiplicities, verifies the \(3\)-cycle Gram identity and its cubic relation, and tests the sphere-collapse normalization for several branch parameters. Execute `python3 checks/tree_essential_norm_check.py` in a directory containing the extracted file. Exact finite checks are corroborative, not exhaustive evidence for the infinite-dimensional theorem.

## Relationship to prior work

Liu and Ma's 2026 Theorem 3.3 establishes a necessary and sufficient **zero-limit compactness** criterion for finite composition sums, with associated coefficient counts. Its Theorem 3.8 proves exponent independence of *whether* such a sum is compact. It does not state an exact positive essential-norm formula or the dual block optimization, nor the exponent-dependent essential-norm example.

Muthukumar and Ponnusamy (2020) establish an exact **operator norm** for individual composition maps on these spaces, but not the distance to compacts. Muthukumar, Sharma, and Kumar (2021) treat boundedness and compactness of weighted composition maps on weighted tree Hardy spaces; that is not the present exact essential norm for finite sums. Related tree Lipschitz multiplier and atomic sequence-space essential-norm results concern different Banach norms and do not imply these block-level formulas without an additional argument.

## Limitations

The formulas require finite sums of bounded composition operators, rather than arbitrary bounded operators on \(\mathbb T_p\). The lower-bound argument uses row-finiteness; it must not be transferred without proof to arbitrary operators on an \(\ell_\infty\)-sum. The expression for a general combination contains finite-dimensional optimizations and is not always reducible to counts alone because complex coefficient cancellation matters. No independent mathematical review or priority certification is claimed. A broadly phrased older general matrix-operator approximation theorem could entail the structural part; the precise literature overlap is a remaining risk.

## References

1. L. Liu and W. Ma, *Compactness of composition operators on Hardy spaces of homogeneous rooted trees*, arXiv:2610.33717v1 (first public 2026-10-24), especially Theorems 3.3 and 3.8. https://arxiv.org/abs/2610.33717
2. P. Muthukumar and S. Ponnusamy, *Composition operators on Hardy spaces of the homogenous rooted trees*, arXiv:2004.03171v1 (2020-04-07), especially Theorem 4. https://arxiv.org/abs/2004.03171
3. P. Muthukumar, A. K. Sharma, and V. Kumar, *Weighted composition operators between weighted Hardy spaces on rooted trees*, arXiv:2112.08323v1 (2021-12-15). https://arxiv.org/abs/2112.08323
