# Weighted equality cases for the chromatic Kemeny bound

## Result

Let \(G\) be a finite connected undirected graph with positive edge weights, of order \(n\ge 2\). Write \(d_v\) for the weighted degree of \(v\), let \(M=D^{-1/2}AD^{-1/2}\) be the normalized adjacency matrix, and use
\[
K(G)=\sum_{j=2}^n\frac1{1-\lambda_j(M)}
\]
for Kemeny's constant in the convention of Abiad--Carmona--Encinas--Ghorbani--Jiménez--Samperio. Let \(r=\chi(G)\).

Their chromatic bound states
\[
K(G)\ge n-2+\frac1r.
\]
The equality cases for weighted graphs admit the following complete description.

### Theorem

The equality
\[
K(G)=n-2+\frac1r
\]
holds if and only if the underlying graph is complete \(r\)-partite, with a proper color partition
\[
V(G)=V_1\dot\cup\cdots\dot\cup V_r,
\]
and there are positive numbers \(a_v\) and a number \(A>0\) such that

\[
\sum_{v\in V_i}a_v=A\qquad (i=1,\ldots,r)
\]
and, for \(u\in V_i\), \(v\in V_j\), \(i\ne j\),
\[
\boxed{\quad w_{uv}=\frac{a_u a_v}{(r-1)A}.\quad}
\]
There are no edges inside the parts.

Moreover the parameters are intrinsic:
\[
a_v=d_v.
\]
Thus each color class has the same weighted volume \(A\), and the weight between two vertices in different classes is determined by their weighted degrees:
\[
\boxed{\quad
w_{uv}=\frac{d_ud_v}{(r-1)A}.
\quad}
\]

Equivalently, if \(P=D^{-1}A\) is the random-walk transition matrix, then
\[
P(u,v)=
\begin{cases}
\dfrac{a_v}{(r-1)A},&u,v\text{ lie in different parts},\\[2mm]
0,&u,v\text{ lie in the same part}.
\end{cases}
\]
Hence an equality walk first chooses one of the other \(r-1\) color classes uniformly, and then samples a vertex in that class from the fixed distribution \(a_v/A\).

This replaces cardinality balance in the unweighted equality theorem by stationary-mass balance in the weighted setting.

## Proof

Fix a proper \(r\)-coloring \(V_1,\ldots,V_r\), and write
\[
\operatorname{vol}(V_i)=\sum_{v\in V_i}d_v.
\]
For each color class define the unit vector
\[
s_i(v)=
\begin{cases}
\dfrac{\sqrt{d_v}}{\sqrt{\operatorname{vol}(V_i)}},&v\in V_i,\\
0,&v\notin V_i.
\end{cases}
\]
Let \(S=(s_1\ \cdots\ s_r)\) and let
\[
B=S^{T}MS
\]
be the degree-weighted quotient matrix.

Because every \(V_i\) is independent, \(B\) has zero diagonal and hence
\[
\operatorname{tr}B=0.
\]
Its Perron eigenvalue is \(1\). If its eigenvalues are
\[
1=\theta_1>\theta_2\ge\cdots\ge\theta_r,
\]
then
\[
\sum_{i=2}^r\theta_i=-1,\qquad
\sum_{i=2}^r(1-\theta_i)=r.
\]

Assume first that \(r<n\). The partition inequality and its equality condition from Theorem 3.3 of Abiad et al., specialized to a color partition, give
\[
K(G)\ge
\sum_{i=2}^r\frac1{1-\theta_i}+(n-r),
\]
and equality here holds precisely when
\[
\operatorname{Spec}(M)
=
\operatorname{Spec}(B)\uplus\{0^{(n-r)}\}.
\]
Applying Cauchy--Schwarz to the positive numbers \(1-\theta_i\) gives
\[
\sum_{i=2}^r\frac1{1-\theta_i}
\ge
\frac{(r-1)^2}{r}.
\]
Consequently
\[
K(G)\ge n-r+\frac{(r-1)^2}{r}
=n-2+\frac1r.
\]
If the final bound is an equality, both inequalities above are equalities. Equality in Cauchy--Schwarz forces
\[
\theta_2=\cdots=\theta_r=-\frac1{r-1}.
\]
Put
\[
\beta=-\frac1{r-1}.
\]

We next extract the rigidity hidden in the spectral equality. Complete \(S\) to an orthogonal matrix \((S\ T)\). In this basis write
\[
M=
\begin{pmatrix}
B&C\\ C^T&E
\end{pmatrix}.
\]
Since the spectrum of \(M\) is the spectrum of \(B\) together with \(n-r\) zeros,
\[
\operatorname{tr}(M^2)=\operatorname{tr}(B^2).
\]
But
\[
\operatorname{tr}(M^2)
=
\operatorname{tr}(B^2)+2\|C\|_F^2+\|E\|_F^2.
\]
Thus \(C=0\) and \(E=0\), so
\[
M=SBS^T.
\]

Now set
\[
c_i=\sqrt{\frac{\operatorname{vol}(V_i)}{\operatorname{vol}(G)}}.
\]
The vector \(c=(c_1,\ldots,c_r)^T\) is a positive unit eigenvector of \(B\) for eigenvalue \(1\). Since every other eigenvalue of \(B\) equals \(\beta\),
\[
B=\beta I+(1-\beta)cc^T.
\]
The diagonal entries of \(B\) vanish. Hence, for every \(i\),
\[
0=\beta+(1-\beta)c_i^2,
\]
and therefore
\[
c_i^2=\frac1r.
\]
All color classes consequently have the same volume
\[
\operatorname{vol}(V_i)=A:=\frac{\operatorname{vol}(G)}r.
\]
For \(i\ne j\),
\[
B_{ij}=\frac1{r-1}.
\]

Take \(u\in V_i\) and \(v\in V_j\), \(i\ne j\). From \(M=SBS^T\),
\[
M_{uv}
=
\frac1{r-1}\frac{\sqrt{d_ud_v}}A.
\]
Since \(M_{uv}=w_{uv}/\sqrt{d_ud_v}\),
\[
w_{uv}=\frac{d_ud_v}{(r-1)A}.
\]
Every weighted degree is positive, so every cross-part weight is positive. Thus the underlying graph is complete \(r\)-partite. Taking \(a_v=d_v\) gives the asserted form.

If \(r=n\), every color class is a singleton. The same Cauchy argument can be applied directly to the \(n-1\) non-Perron eigenvalues of \(M\): their sum is \(-1\), so equality implies that they are all \(-1/(n-1)\). If \(u\) is the positive unit Perron vector, then
\[
M=-\frac1{n-1}I+\frac n{n-1}uu^T.
\]
The zero diagonal of \(M\) forces \(u_v^2=1/n\) for every vertex. Hence the weighted degrees are all equal and all edge weights are equal. This is exactly the displayed formula with \(r=n\) and singleton parts.

Conversely, suppose a partition and positive masses \(a_v\) satisfy
\[
\sum_{v\in V_i}a_v=A
\]
for every \(i\), and define the cross-part weights by
\[
w_{uv}=\frac{a_ua_v}{(r-1)A}.
\]
For \(u\in V_i\),
\[
d_u
=
\sum_{j\ne i}\sum_{v\in V_j}
\frac{a_ua_v}{(r-1)A}
=a_u.
\]
Let \(S\) again have columns \(s_i(v)=\sqrt{a_v/A}\) on \(V_i\). Then
\[
M=S\frac{J_r-I_r}{r-1}S^T.
\]
Therefore
\[
\operatorname{Spec}(M)
=
\left\{
1,\,
\left(-\frac1{r-1}\right)^{(r-1)},\,
0^{(n-r)}
\right\}.
\]
It follows that
\[
K(G)
=(n-r)+(r-1)\frac{r-1}{r}
=n-2+\frac1r.
\]
This proves the theorem.

## Consequences

### Every complete multipartite shape admits equality weights

For arbitrary nonempty part sizes \(n_1,\ldots,n_r\), choose positive masses with equal total mass in every part. The theorem then supplies equality weights. Thus, for \(r\ge3\), the weighted equality class contains complete \(r\)-partite graphs of arbitrarily unbalanced cardinalities, even though the unweighted equality theorem permits only balanced complete \(r\)-partite graphs.

For example, assigning mass \(1/n_i\) to every vertex of \(V_i\) gives \(A=1\) and
\[
w_{uv}=\frac1{(r-1)n_i n_j}
\qquad
(u\in V_i,\ v\in V_j).
\]

### Bipartite specialization

For \(r=2\), equality holds exactly when the positive bipartite weight matrix has rank one. Indeed,
\[
w_{uv}=\frac{a_ua_v}{A}.
\]
In particular every positive weighting of a star attains
\[
K(G)=n-\frac32,
\]
whereas a general positive weighting of \(K_{p,q}\) with \(p,q\ge2\) need not.

### Dimension of the equality family

For a fixed complete \(r\)-partite underlying graph on \(n\) vertices, the equality weights are parameterized uniquely by the positive weighted-degree vector
\[
(a_v)_{v\in V(G)}
\]
subject to the \(r-1\) independent linear conditions that all part sums agree. Hence the equality cone has dimension
\[
n-r+1.
\]
Since common rescaling of every edge weight leaves the normalized adjacency matrix and Kemeny's constant unchanged, the equality family modulo global scale has dimension
\[
n-r.
\]

### Recovery of the unweighted theorem

When all edge weights equal one, the factorized formula collapses to the unweighted equality cases identified by Abiad et al.: arbitrary complete bipartite graphs for \(r=2\), and balanced complete \(r\)-partite graphs for \(r\ge3\).

## Verification

The proof is exact and does not depend on computation. A compact numerical verifier in `artifacts/verify_weighted_kemeny.py` constructs several equality graphs with unequal part sizes and nonuniform vertex masses, checks that the prescribed masses equal the resulting weighted degrees, computes the normalized adjacency spectrum, and verifies
\[
K(G)=n-2+\frac1r.
\]
The recorded output is in `artifacts/verification.txt`.

## Literature context and limitations

Abiad, Carmona, Encinas, Ghorbani, Jiménez and Samperio introduced the chromatic Kemeny bound for connected weighted graphs and explicitly stated the equality classification only for the unweighted case. Their equality theorem for the partition bound supplies the spectral starting point used above.

Ciardo, Dahl and Kirkland proved the earlier unweighted bipartite bound and characterized complete bipartite equality graphs. Sun and Das studied normalized-Laplacian spectra of unweighted complete multipartite graphs. Work on degree-corrected block matrices contains algebraically related rank-one block factorizations, but the searches performed for this result found no statement equivalent to the weighted Kemeny/chromatic equality classification above.

Originality is therefore asserted only to the best of our knowledge. The main residual risk is an older weighted-spectral or reversible-Markov-chain result phrased without Kemeny's constant or chromatic terminology, or very recent parallel work following the September 2026 preprint. No independent validation is asserted.

## References

1. A. Abiad, Á. Carmona, A. M. Encinas, E. Ghorbani, M. J. Jiménez, Á. Samperio, *Kemeny's constant via matrix compression and eigenvalue interlacing*, arXiv:2609.17481 (2026). https://arxiv.org/abs/2609.17481
2. L. Ciardo, G. Dahl, S. Kirkland, *On Kemeny's constant for trees with fixed order and diameter*, Linear and Multilinear Algebra 70 (2022), 2331--2353. https://doi.org/10.1080/03081087.2020.1796905
3. S. Sun, K. C. Das, *Normalized Laplacian spectrum of complete multipartite graphs*, Discrete Applied Mathematics 284 (2020), 234--245. https://doi.org/10.1016/j.dam.2020.03.041
4. D. Fasino, F. Tudisco, *The expected adjacency and modularity matrices in the degree corrected stochastic block model*, Special Matrices 6 (2018), 110--121. https://doi.org/10.1515/spma-2018-0010
