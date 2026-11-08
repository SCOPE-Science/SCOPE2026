# Sharp negative-type exponent and Euclidean rank of complete multipartite graph metrics

## Finding

Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph, where \(r\ge2\) and every \(n_i\ge1\), with its unweighted shortest-path metric \(d\). Write \(N=\sum_i n_i\), \(q_i=1-1/n_i\), and \(\wp(G)=\sup\{p\ge0:d^p\text{ is of negative type}\}\). If all \(n_i=1\), then \(\wp(G)=\infty\) and negative type is strict for every finite \(p\). Otherwise let \(n_{\max}=\max_i n_i\) and \(k=\#\{i:n_i=n_{\max}\}\).

**Repeated largest part (\(k\ge2\)).** The sharp exponent and boundary nullity are
\[
\wp(G)=\log_2\frac{n_{\max}}{n_{\max}-1},\qquad
\dim\ker\left(-d^{\wp(G)}\big|_{\mathbf1^\perp}\right)=k-1.
\]
The kernel consists exactly of vectors constant within each largest part, zero on all other parts, whose total sum is zero.

**Unique largest part (\(k=1\)).** Relabel so \(n_1>n_2\ge\cdots\ge n_r\). Put \(\theta_i=(1-1/n_i)^{-1}\), with \(\theta_i=\infty\) when \(n_i=1\). There is exactly one \(\rho_*\in(\theta_1,\theta_2)\) satisfying
\[
\sum_{i=1}^r\frac{1}{1-\rho_*(1-1/n_i)}=0.
\]
Then \(\wp(G)=\log_2\rho_*\), and the boundary kernel is one-dimensional: a generating vector takes the value \(1/[n_i(1-\rho_*q_i)]\) at every vertex in part \(i\).

In every noncomplete case, \(d^p\) is **strictly** of negative type for \(0\le p<\wp(G)\), is of non-strict negative type at \(p=\wp(G)\), and fails negative type for \(p>\wp(G)\). For the snowflaked metric \(d^{\wp(G)/2}\), the minimal Euclidean embedding dimension is \(N-k\) when the largest part repeats, and \(N-2\) when it is unique.

An algebraic determination independent of rational functions is the smallest real root \(\rho>1\) of
\[
P(\rho)=\sum_{i=1}^r n_i\prod_{j\ne i}\bigl(n_j-\rho(n_j-1)\bigr).
\]
It is understood that the complete-graph case has no such root. This polynomial characterization includes simultaneous vanishing denominators.

## Assumptions and scope

The graph has at least two nonempty parts. Distances between vertices in distinct parts are \(1\), and distances between distinct vertices in the same part are \(2\). For \(p\ge0\), \(D_p\) is the real symmetric matrix with entries \(d(u,v)^p\) for distinct vertices and zero diagonal. A kernel or inertia on \(\mathbf1^\perp\) refers to the restriction of the quadratic form \(-x^TD_px\) to the \((N-1)\)-dimensional zero-sum subspace, not an unrestricted matrix kernel. Negative type means \(x^TD_px\le0\) for all real \(x\) with \(\sum_v x_v=0\); strict negative type means equality is possible only for \(x=0\).

## Proof

**1. Exact orthogonal block decomposition.** Set \(\rho=2^p\). For a zero-sum vector \(x\), put \(S_i=\sum_{v\in V_i}x_v\) and \(y_v=x_v-S_i/n_i\) for \(v\in V_i\). Because \(\sum_i S_i=0\) and each block of \(y\) sums to zero, expanding intra- and inter-part pairs gives
\[
 x^TD_px=(\rho-1)\sum_i S_i^2-\rho\sum_v x_v^2,
\]
and therefore the *identity*, with no omitted normalizing factor,
\[
\boxed{-x^TD_px=\rho\sum_v y_v^2+\sum_{i=1}^r c_i(\rho)S_i^2,\qquad
 c_i(\rho)=1-\rho q_i,\quad \sum_i S_i=0.}
\]
The decomposition \(x_v=y_v+S_i/n_i\) is unique. Every admissible vector of part sums \(S\) with total zero is realized by a vector constant within parts. Hence positivity, nullity, and its failure reduce *exactly* to the diagonal form \(Q_\rho(S)=\sum_i c_i(\rho)S_i^2\) on \(H=\{S:\sum_i S_i=0\}\). The deviation contribution is strictly positive unless all \(y_v=0\).

**2. Complete graph and initial strictness.** If all parts are singletons, \(q_i=0\), hence \(Q_\rho(S)=\sum_iS_i^2>0\) on nonzero \(H\) for all \(\rho\ge1\). If some part is non-singleton, put \(\theta_1=1/\max_i q_i=n_{\max}/(n_{\max}-1)>1\). Every \(c_i(\rho)>0\) for \(1\le\rho<\theta_1\), so negative type is strict throughout that range.

**3. Tied largest parts.** If exactly \(k\ge2\) parts attain the largest size, at \(\rho=\theta_1\) their coefficients \(c_i\) vanish, and all other coefficients are strictly positive. Thus \(Q\) on \(H\) is positive semidefinite with kernel the \((k-1)\)-dimensional zero-sum subspace on those \(k\) indices. For \(\rho>\theta_1\), the vector \(S\) supported with opposite entries on two largest parts gives \(Q_\rho(S)<0\). Hence \(\theta_1\) is the exact threshold and the asserted kernel description follows from Step 1.

**4. Unique largest part.** Relabel so \(q_1>q_2\ge\cdots\ge q_r\). At \(\rho=\theta_1\), \(c_1=0\), \(c_i>0\) for \(i\ge2\), and the zero-sum constraint forces any vector with \(Q=0\) to be zero. Thus strictness persists at \(\theta_1\). For \(\theta_1<\rho<\theta_2\), the coefficient \(c_1<0\), while \(c_i>0\) for all \(i\ge2\). Set
\[
F(\rho)=\sum_i\frac1{c_i(\rho)},\qquad T(\rho)=\sum_{i=2}^r\frac1{c_i(\rho)}>0.
\]
Writing \(S_1=-\sum_{i\ge2}S_i\), the matrix of \(Q\) in the remaining coordinates is \(\operatorname{diag}(c_2,\ldots,c_r)+c_1\mathbf1\mathbf1^T\). By the elementary rank-one criterion (congruence by the positive diagonal square root), this is positive definite when \(1+c_1T>0\), positive semidefinite of nullity one when equality holds, and indefinite with precisely one negative direction when \(1+c_1T<0\). As \(1+c_1T=c_1F\), the three cases correspond respectively to \(F<0\), \(F=0\), and \(F>0\).

On \((\theta_1,\theta_2)\),
\[
F'(\rho)=\sum_i\frac{q_i}{c_i(\rho)^2}>0,\quad
\lim_{\rho\downarrow\theta_1}F(\rho)=-\infty.
\]
If \(q_2>0\), \(F\to+\infty\) as \(\rho\uparrow\theta_2\); if \(q_2=0\), all remaining parts are singletons and \(F(\rho)\to r-1>0\) as \(\rho\to\infty\). Therefore precisely one \(\rho_*\) satisfies \(F(\rho_*)=0\). Its kernel is spanned by \(S_i=1/c_i(\rho_*)\): the sum is zero by construction and \(Q\)'s Euler equations \(c_i S_i=\text{constant}\) hold. Step 1 gives the corresponding vertex weights.

For every \(\rho>\rho_*\), keep this *fixed* nonzero vector of part sums and note
\[
Q_\rho(S)=Q_{\rho_*}(S)-(\rho-\rho_*)\sum_i q_i S_i^2
=-(\rho-\rho_*)\sum_i q_i S_i^2<0,
\]
because \(q_1>0\) and \(S_1\ne0\). Thus negative type fails at every higher exponent, including after other denominators vanish.

**5. Polynomial form and Euclidean rank.** The determinant of \(Q\) on \(H\), in coordinates \(S_1=-\sum_{i\ge2}S_i\), is
\[
\sum_{i=1}^r\prod_{j\ne i}c_j(\rho)=\frac{P(\rho)}{\prod_i n_i}.
\]
This polynomial identity remains valid when coefficients vanish. The preceding sign-and-kernel analysis proves that its first root beyond \(1\) is the asserted \(\rho_*\) (including ties). By Schoenberg's finite Euclidean distance criterion, \(d^p\) is a squared Euclidean distance matrix precisely at the nonnegative-type exponents, and the embedding dimension is the rank of \(-D_p\) on the zero-sum subspace. The displayed kernels have dimensions \(k-1\) and \(1\), respectively, so the minimal dimensions are \(N-k\) and \(N-2\). This establishes every assertion.

## Verification

The accompanying `checker.py` uses Python, SymPy, and NumPy. Running `python checker.py` passes **1,730 finite diagnostic assertions** involving exact rational quadratic-form identities, polynomial factorizations, and eigenvalue tests of the independent zero-sum Gram matrix for many small part-size tuples. Example polynomials are \(P_{(3,2,1)}(\rho)=2(\rho^2-7\rho+9)\), \(P_{(3,2,2)}(\rho)=(\rho-2)(11\rho-18)\), and \(P_{(3,3,3)}(\rho)=9(2\rho-3)^2\). In particular, \(\rho_*(3,2,1)=(7-\sqrt{13})/2\) with nullity one, whereas \(\rho_*(3,3,3)=3/2\) with nullity two. The unbounded-dimensional proof is Steps 1–5, not this finite experimentation.

As a cross-check, for \(r=2\), the polynomial root is \(\rho_*=2n_1n_2/(2n_1n_2-n_1-n_2)\), reproducing the published bipartite theorem. For a single part of size \(n>1\) and \(s\ge1\) singleton parts, \(\rho_*=n(s+1)/[s(n-1)]\).

## Relationship to prior work

Kiyonori Gomi, *Excess inertia of finite metric spaces*, arXiv:2610.18132v1 (2026), introduces a systematic treatment of excess inertia and classifies possible signatures of finite metrics up to nine points; it does not state the complete multipartite exponent and boundary-rank classification. Stephen Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1 (2011), Corollary 2.4 and Theorem 3.1, gives a general determinant test and the exact \(K_{m,n}\) formula. The present result includes that formula but claims novelty only for arbitrary numbers of parts together with the two distinct boundary nullity regimes and all-parameter strictness. Earlier Deza–Maehara methods express graph truncated-metric Euclidean thresholds through general characteristic polynomials; this gives broad algorithmic coverage, but no identical multipartite structural classification was identified in the accessible material. Deza–Grishukhin investigated negative-type cones for general two-distance spaces; full-text access to that paper was unavailable, so independent historical priority requires checking it.

## Limitations

The theorem concerns the shortest-path metrics of complete multipartite graphs, not arbitrary graph metrics, weighted multipartite edges, or Hilbert distortion when negative type fails. It gives Euclidean embedding *dimension* at the critical snowflake exponent but not a coordinate construction or higher-exponent optimal distortion. The critical exponent can require solving an algebraic polynomial rather than a radical formula. No claim is made that generic determinant algorithms, the known bipartite special case, or Schoenberg's criterion are new. Priority relative to inaccessible older full text remains an explicitly unresolved risk, and no independent mathematical audit has been conducted.

## References

1. K. Gomi, *Excess inertia of finite metric spaces*, arXiv:2610.18132v1, first submitted 2026-10-13, https://arxiv.org/html/2610.18132v1.
2. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1, 2011, https://arxiv.org/html/1108.0451v1, especially Theorem 3.1.
3. M. Deza and H. Maehara, *Metric transforms and Euclidean embeddings*, Trans. Amer. Math. Soc. 317 (1990), 661–671, doi:10.1090/S0002-9947-1990-0974513-6 (general method; full text not inspected).
4. M. Deza and V. Grishukhin, *Hypermetric two-distance spaces* (2000), https://micheldeza.altervista.org/withSlava/two-dist/htd.pdf (abstract inspected; complete text unavailable).
5. I. J. Schoenberg, *Metric spaces and positive definite functions*, Trans. Amer. Math. Soc. 44 (1938), 522–536.
