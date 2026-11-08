# Exact sensor multiplicity and Krylov volume for multipartite graph Fourier bands

## Finding
Let \(G=K_{n_1,\ldots,n_k}\) be a complete multipartite graph with \(k\ge2\) nonempty parts, and let \(\mathcal H\) be the \(k\)-dimensional space of functions constant on each part. This is an invariant graph spectral subspace, but is not necessarily the low-pass subspace for a cutoff of the normalized Laplacian. Evolve signals by the row-stochastic graph operator \(T=D^{-1}A\), where \(A\) is adjacency and \(D\) is the degree matrix. At a fixed set of vertices \(S\), observe \((T^tf)(v)\) for every \(v\in S\) and \(t=0,\ldots,k-1\).

Write \(E_s=\{i:n_i=s\}\), \(r_s=|E_s|\), and \(C(S)=\{i:S\cap V_i\ne\varnothing\}\). These observations determine every \(f\in\mathcal H\) if and only if \(S\ne\varnothing\) and
\[
|C(S)\cap E_s|\ge r_s-1\quad\text{for every occurring part size }s.
\]
Consequently the exact minimum number of vertex sensors is
\[
\boxed{m_* = \max\left\{1,\sum_s(r_s-1)\right\}.}
\]
When all part sizes are pairwise distinct, there are exactly \(N=\sum_i n_i\) minimum sensor sets (every individual vertex); otherwise the exact number is
\[
\boxed{\prod_{s:r_s\ge2} r_s s^{r_s-1}.}
\]
For one sensor at any vertex of part \(j\), let \(\mathcal O_j\) be the square \(k\)-by-\(k\) matrix with entries \((\mathcal O_j)_{t+1,i}=(P^t)_{ji}\), \(t=0,\ldots,k-1\), where \(P\) is the quotient evolution below. Then
\[
\boxed{
|\det\mathcal O_j|=\frac{\prod_{i\ne j}n_i}{(N-n_j)^{k-1}}
\prod_{\substack{a<b\\a,b\ne j}}
\left|\frac{n_b}{N-n_b}-\frac{n_a}{N-n_a}\right|.}
\]
An empty product is \(1\). In particular, a single vertex in part \(j\) gives stable full recovery exactly when all the *other* part sizes are pairwise distinct. The determinant is the exact product of all singular values of the square measurement operator and thus an exact volume-stability invariant.

## Assumptions and scope
Here \(V_i\) is part \(i\) of size \(n_i\in\mathbb N\), \(N=\sum_i n_i\), and every vertex in part \(i\) has degree \(d_i=N-n_i>0\). Real or complex initial values are allowed. We take complete, noiseless measurements at consecutive discrete times, including time zero; sensors are fixed across times. The function space consists solely of part-constant signals, not all \(N\)-vertex signals. Equip it with the norm inherited from \(\ell^2(V)\); since it is finite-dimensional, injectivity of the observation map is equivalent to strictly positive frame bounds.

Writing \(f|_{V_i}=c_i\), the induced evolution is the \(k\)-by-\(k\) rational matrix
\[
P_{ij}=\begin{cases} n_j/(N-n_i),&j\ne i,\\0,&j=i.\end{cases}
\]
Set \(\alpha_i=(N-n_i)^{-1}\), \(\beta_i=n_i\), and \(\theta_i=\alpha_i\beta_i=n_i/(N-n_i)\). Then \(P=\alpha\beta^\top-\operatorname{diag}(\theta_i)\). The map from a physical vertex sensor in part \(j\) to a row of the quotient observation matrix is exactly \(e_j^\top\), without an additional normalization factor.

## Proof
**Spectral decomposition.** The matrix \(P\) is similar to the symmetric normalized-adjacency compression, via the positive diagonal transform \(\operatorname{diag}(\sqrt{n_i(N-n_i)})\), so it is diagonalizable over \(\mathbb R\). For every size \(s\) occurring in \(r_s\ge2\) parts, the eigenspace for \(-s/(N-s)\) consists precisely of vectors supported on \(E_s\) whose coordinates sum to zero. Its dimension is \(r_s-1\). To see this, \(P+\operatorname{diag}(\theta)=\alpha\beta^\top\), and any such vector annihilates \(\beta^\top\). Conversely, diagonal-plus-rank-one spectral analysis gives no further eigenvectors at these pole values.

For all remaining eigenvalues, the determinant lemma produces the secular equation
\[
1-\sum_{s}\frac{r_s\,s/(N-s)}{\lambda+s/(N-s)}=0.
\]
Between consecutive poles its left side is strictly increasing and crosses from negative to positive infinity, and there is one final simple root above the largest pole. Thus it has exactly as many distinct simple nonpole roots as there are distinct part sizes. Every associated right eigenvector has coordinates proportional to \(\alpha_i/(\lambda+\theta_i)\), all nonzero. All pole eigenvalues and all simple nonpole eigenvalues are mutually distinct.

**Sensor criterion.** Decompose any input into the distinct eigenspaces. If all its samples at times \(0,\ldots,k-1\) vanish, Vandermonde inversion in the distinct eigenvalues separates each eigencomponent at every sensor: the projection of each component onto every observed part must vanish. A nonpole eigenspace is one-dimensional and visible at every vertex, provided \(S\ne\varnothing\). A pole eigenspace supported on \(E_s\) is invisible to \(S\) only when at least two part indices of that equal-size group have no sensor, allowing a nonzero zero-sum vector supported there. This gives the stated necessary-and-sufficient criterion. The converse is an actual invisible eigenvector, so longer observation times cannot overcome a failing sensor set.

**Minimum and counting.** For each repeated-size group \(E_s\), exactly \(r_s-1\) distinct parts must be hit. If any group is repeated, selecting precisely one vertex in each of \(r_s-1\) parts of every repeated group attains the minimum; for a group of equal size \(s\), its number of choices is \(r_s s^{r_s-1}\). Different groups multiply. If no group is repeated, a single vertex anywhere suffices, giving \(N\) choices.

**Exact determinant.** The transpose of \(P\) is \(P^\top=\beta\alpha^\top-\operatorname{diag}(\theta_i)\). For a fixed part \(j\) and every \(i\ne j\), induction gives
\[
\bigl((P^\top)^r e_j\bigr)_i
=\alpha_j\beta_i\,q_{r-1}(-\theta_i),\qquad r\ge1,
\]
where \(q_{r-1}\) is a monic polynomial of degree \(r-1\), the same for all \(i\ne j\). Indeed the first step is \(\alpha_j\beta_i\), and each subsequent multiplication by \(P^\top\) multiplies the existing polynomial by \(-\theta_i\) and adds a constant independent of \(i\). Expanding the determinant of the Krylov columns \(e_j,P^\top e_j,\ldots,(P^\top)^{k-1}e_j\) along the first column leaves a monic-polynomial Vandermonde matrix in the nodes \(-\theta_i\), \(i\ne j\). Factoring \(\alpha_j\beta_i\) from its columns/rows yields exactly the stated absolute determinant. The physical observation matrix \(\mathcal O_j\) is the transpose of this Krylov matrix, so its determinant has the same magnitude. Since \(n\mapsto n/(N-n)\) is strictly increasing for \(0<n<N\), the determinant vanishes exactly when two part sizes outside \(j\) coincide.

## Verification
Run `python3 CHECK.py`. It performs exact rational arithmetic throughout, independently builds every quotient matrix, and verifies row-stochasticity, the necessary-and-sufficient sensor rank criterion, the determinant factorization, and the exact minimum-sensor enumerator for all ordered part-size tuples of lengths \(2\) through \(5\) with sizes in \(\{1,2,3\}\). Additional six-part tuples test more complicated collision patterns. The standalone checker produces `PASS 15308 exact assertions`.

This finite enumeration is a consistency check, not an inference about unbounded part sizes. The general proof above uses the rank-one spectral decomposition and Vandermonde determinant identity for arbitrary \(k\) and arbitrary positive integer part sizes.

## Relationship to prior work
Cabrelli, Bulai, Cordero, Molter, and Saliani (2026) study dynamical sampling of graph spectral spaces, establishing the motivation for exact finite-graph sampling conditions. Only its publicly available abstract was accessible for comparison. Cabrelli, Molter, Paternostro, and Philipp (2017), Theorem 4.1, establish a general eigenprojection criterion for finite-dimensional dynamical frames; applying that criterion still requires an explicit graph-specific eigenspace analysis and gives no evaluated Krylov-volume formula. Mousavi, Haeri, and Mesbahi (2018/2020) classify controllability of full Laplacian dynamics on cographs, which contain complete multipartite graphs, but their model is the full-graph (combinatorial) Laplacian dynamics, not the restricted random-walk Fourier band considered here. The present formula is an exact quotient-band placement classification and a determinant evaluation, not a claim to invent the general spectral observability test, the rank-one update method, or the Vandermonde determinant.

## Limitations
The theorem does not recover signals varying within a part. All temporal samples are assumed exact; the determinant describes the volume factor but does not alone give the smallest singular value. The number of time samples is sufficient; except for the one-sensor case where \(k\) samples are necessary by dimension, no globally minimal temporal budget is asserted. Earlier literature may contain a reformulation of this particular quotient result not discovered in the cited searches. The full text of the motivating 2026 paper could not be inspected; independent publication-priority verification is not performed.

## References
1. I. M. Bulai, C. Cabrelli, E. Cordero, U. Molter, S. Saliani, *Dynamical Sampling in Graph Paley--Wiener Spaces*, arXiv:2609.25472, first submitted 2026-09-21, https://arxiv.org/abs/2609.25472.
2. C. Cabrelli, U. Molter, V. Paternostro, F. Philipp, *Dynamical Sampling on Finite Index Sets*, arXiv:1702.03384 (2017), especially Section 4 and Theorem 4.1, https://arxiv.org/abs/1702.03384.
3. S. S. Mousavi, M. Haeri, M. Mesbahi, *Laplacian Dynamics on Cographs: Controllability Analysis through Joins and Unions*, arXiv:1802.03599 (first submitted 2018, revised 2020), especially Sections III--IV, https://arxiv.org/html/1802.03599v2.
