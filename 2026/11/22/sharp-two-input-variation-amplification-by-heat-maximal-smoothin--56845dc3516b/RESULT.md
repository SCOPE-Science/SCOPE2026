# Sharp two-input variation amplification by heat maximal smoothing on the three-vertex path

## Finding

Let \(P_3\) be the unweighted path on three vertices, \(L\) its combinatorial Laplacian, and \(H_t=e^{-tL}\). For a nonnegative real vector \(f=(f_1,f_2,f_3)\), define the heat-flow maximal vector by
\[
(\mathcal M f)_i=\sup_{t\ge 0}(H_tf)_i,\qquad i=1,2,3.
\]
Write \(V(f)=|f_2-f_1|+|f_3-f_2|\). Then the exact two-input variation Lipschitz coefficient is
\[
\boxed{\sup_{f,g\in[0,\infty)^3,\;V(f-g)>0}\frac{V(\mathcal M f-\mathcal M g)}{V(f-g)}=\frac43.}
\]
The factor is attained at the strictly positive pairs \(f=(13,12,5)\) and \(g=(15,11,4)\): their maximal vectors are \(\mathcal M f=(13,12,10)\) and \(\mathcal M g=(15,11,10)\), giving input variation \(3\) and output variation \(4\). On the two-vertex unit path the corresponding exact factor is \(1/2\). Every individual heat step on \(P_3\) instead has variation norm \(e^{-t}\), showing that taking the pointwise supremum over times can destroy two-input variation nonexpansivity.

## Assumptions and scope

The graph has exactly three vertices and unit edge conductances, with ordinary counting measure. The heat semigroup is the continuous-time, unnormalized graph heat semigroup. The maximal operator acts on nonnegative data, so it agrees with the usual absolute-value-input heat maximal operator. The supremum includes the limit as \(t\to\infty\); it need not be reached at finite time. All two-input inequalities are for the adjacent-edge variation of the difference, not the difference of the separate variations. The same calculation applies to signed data if the definition uses \(\sup_t H_t f\) *without* applying absolute values first; no signed-data bound is claimed for the customary \(\sup_t H_t|f|\) operator.

## Proof

Set
\[
m=\frac{f_1+f_2+f_3}{3},\qquad u=\frac{f_1-f_3}{2},\qquad v=\frac{f_1+f_3-2f_2}{6}.
\]
The eigenvectors \((1,1,1)\), \((1,0,-1)\), and \((1,-2,1)\) of \(L\) have eigenvalues \(0,1,3\). Consequently, with \(z=e^{-t}\in(0,1]\),
\[
H_tf=(m+uz+vz^3,\ m-2vz^3,\ m-uz+vz^3),\qquad
V(f)=|u+3v|+|u-3v|=2\max\{|u|,3|v|\}.
\]
By continuity, the supremum over times is the maximum over \(z\in[0,1]\). Define
\[
h_+(u,v)=\max_{0\le z\le1}(uz+vz^3),\qquad
h_-(u,v)=\max_{0\le z\le1}(-uz+vz^3),\quad b(v)=\max\{0,-2v\}.
\]
Thus \(\mathcal Mf=(m+h_+,m+b,m+h_-)\). The two adjacent output differences are \(F_1=h_+-b\) and \(F_2=b-h_-\). These are globally Lipschitz functions of \((u,v)\), since each is assembled from maxima of affine functions over a compact parameter set.

At almost every \((u,v)\), choose active maximizing values \(x,y\in[0,1]\) for \(h_+,h_-\), respectively, and put \(\beta=1\) when \(v<0\) and \(\beta=0\) when \(v>0\). The envelope derivative gives
\[
dF_1=x\,du+(x^3+2\beta)\,dv,\qquad
dF_2=y\,du-(y^3+2\beta)\,dv.
\]
The induced norm from \(2\max(|du|,3|dv|)\) to \(|dF_1|+|dF_2|\) is
\[
\frac12\max_{\sigma,\tau\in\{-1,1\}}\left(
|\sigma x+\tau y|+\frac13|\sigma(x^3+2\beta)-\tau(y^3+2\beta)|\right).
\]
When \(\sigma=\tau\) this is \((x+y)/2+|x^3-y^3|/6\le1\). Indeed, assuming \(x\ge y\), the expression multiplied by six is \(3(x+y)+x^3-y^3\), increasing in \(x\); at \(x=1\) it becomes \(4+3y-y^3\le6\). When \(\sigma=-\tau\), the expression becomes
\[
\frac{|x-y|}{2}+\frac{x^3+y^3+4\beta}{6}\le\frac43.
\]
For \(x\ge y\), the inequality \(3(x-y)+x^3+y^3\le4\) follows by increasing \(x\) to \(1\), then using \(y^3\le3y\). The other ordering is symmetric and \(\beta\le1\). Hence the Jacobian norm is everywhere bounded by \(4/3\) where it exists. Local Lipschitz regularity, Rademacher's theorem, and integration of the bounded weak derivative (or mollification) give the same global bound between arbitrary inputs. Constant-translation components cancel in variation.

For sharpness, at \(f=(13,12,5)\) one has \((m,u,v)=(10,4,-1)\), and at \(g=(15,11,4)\) one has \((10,11/2,-1/2)\). In both cases the first-coordinate maximum is at \(z=1\), the middle at \(z=1\), and the last is the limiting value at \(z=0\). Thus their outputs are exactly as stated and the ratio is \(4/3\).

For the two-vertex path, with mean \(m=(f_1+f_2)/2\), \(\mathcal M f=(\max\{f_1,m\},\max\{f_2,m\})\), and \((\mathcal M f)_1-(\mathcal M f)_2=(f_1-f_2)/2\). This proves the exact coefficient \(1/2\). Finally, on the three-vertex path the edge-difference vector of \(H_tf\) evolves by the matrix exponential of \(\left(\begin{smallmatrix}-2&1\\1&-2\end{smallmatrix}\right)\), a nonnegative matrix whose columns sum to \(e^{-t}\). It follows that the variation norm of every fixed \(H_t\) is exactly \(e^{-t}\).

## Verification

The self-contained `check_heat_maximal.py` independently evaluates every coordinate maximum by the endpoints and any interior cubic stationary point. It checks the exact rational witness, the two-vertex equality, 20,000 deterministic pseudorandom input pairs, the generalized derivative bound on 20,402 grid configurations, and agreement with an independent 5,001-point time grid on 250 inputs. All assertions passed. The infinite-dimensional or all-input conclusion comes from the analytical Jacobian argument; finite tests alone would not establish it.

## Relationship to prior work

Carneiro and Svaiter (arXiv:1309.1529, first posted 6 September 2013) prove *one-input* variation inequalities for heat-flow maximal operators on the infinite discrete lattice. Their Theorem 3 and proof do not evaluate the two-input variation seminorm of the finite reflected path operator. González-Riquelme and Madrid (arXiv:2005.03146) obtain sharp one-input variation norms for finite-graph *ball-average* maximal operators, a different family of averaging kernels. Liu and Zhang (2022) also study graph-ball maximal operators, primarily for directed graphs. None of these inspected statements implies the \(4/3\) two-input heat-flow value. In particular, one-input \(V(\mathcal M f)\le V(f)\) cannot be substituted for the Lipschitz inequality \(V(\mathcal M f-\mathcal M g)\le V(f-g)\).

## Limitations

Only the smallest nontrivial finite open path, equal vertex masses, unit conductances and the adjacent \(\ell^1\) variation are treated. No claim is made for longer paths, weighted edges, Poisson maximal operators or the customary absolute-value-input maximal map on arbitrary signed data. Historical priority cannot be guaranteed against unindexed or inaccessible sources; no independent audit has been performed.

## References

- E. Carneiro and B. F. Svaiter, *On the variation of maximal operators of convolution type*, arXiv:1309.1529 (initial submission 2013-09-06), https://arxiv.org/abs/1309.1529.
- C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146 (2020), https://arxiv.org/html/2005.03146v3.
- F. Liu and X. Zhang, *Variation Inequalities for the Hardy–Littlewood Maximal Function on Finite Directed Graphs*, Mathematics 10 (2022), 950, https://doi.org/10.3390/math10060950.
