# Exact half-space Fourier support of Schröder diagonal-column counts

## Finding
For every integer \(n\geq 1\), let \(\mathcal P_n\) be the Schröder lattice paths from \((0,0)\) to \((n,n)\) using north \((0,1)\), east \((1,0)\), and diagonal \((1,1)\) steps, entirely in \(y\geq x\). Encode a path by \(d(P)\in(\mathbb Z/2\mathbb Z)^n\), where \(d_i(P)=1\) precisely when the path has a diagonal step with starting horizontal coordinate \(i\), for \(0\leq i<n\). Let \(\mu_n(v)=\#\{P\in\mathcal P_n:d(P)=v\}\), counting paths with multiplicity, and let \(T_n\) be unnormalized XOR convolution by \(\mu_n\).

For \(\xi\in(\mathbb Z/2\mathbb Z)^n\), define \(\lambda_n(\xi)=\sum_v\mu_n(v)(-1)^{\sum_i\xi_iv_i}\). Then
\[
\lambda_n(\xi)=0\quad\Longleftrightarrow\quad\xi_0=1.
\]
If \(\xi_0=0\), its Fourier multiplier is a **strictly positive even integer**, with the sharp minimum \(2\), attained at the unique frequency \((0,1,\ldots,1)\). The unique largest multiplier is the large Schröder number \(R_n=\#\mathcal P_n\), at \(\xi=0\). Consequently
\[
\operatorname{rank}(T_n)=\operatorname{nullity}(T_n)=2^{n-1},
\qquad
\min_{\lambda\ne0}|\lambda|=2,
\qquad
\kappa_2(T_n|_{\operatorname{ran}T_n})=\frac{R_n}{2}.
\]
The range is exactly the functions independent of the first binary coordinate. Equivalently, the diagonal-column statistic \(d_0\) is a fair bit independent of the joint vector \((d_1,\ldots,d_{n-1})\) under the uniform path law, and convolution by its latter marginal is invertible.

## Assumptions and scope
The kernel \(\mu_n\) is the **counting push-forward** of the path family; it is not the indicator of the set of possible incidence vectors. Each \(\mu_n(v)\) is positive. XOR convolution means \((T_n g)(x)=\sum_v\mu_n(v)g(x+v)\). Fourier characters are \(\chi_\xi(v)=(-1)^{\xi\cdot v}\), and the transform is unnormalized. The operator acts on the complex Hilbert space of functions on \((\mathbb Z/2\mathbb Z)^n\) with counting measure. The condition number is that of the restriction to its range, not of the singular full operator. All conclusions include \(n=1\).

## Proof
For each path, mark the unique step that increments the horizontal coordinate from \(i\) to \(i+1\). Before this step there are \(a\geq0\) north steps. Let \(h_i=y_i-i\geq0\) denote the height difference immediately after the preceding horizontal increment (at \(i=0\), \(h_0=0\)). Thus \(h_n=0\), and necessarily \(0\leq h_i\leq n-i\). If the horizontal-increment step is east, \(h_{i+1}=h_i+a-1\); if diagonal, \(h_{i+1}=h_i+a\). Their character weights are respectively \(1\) and \(z_i=(-1)^{\xi_i}\). Therefore, for admissible heights, the exact signed transition is
\[
K_i(h,h')=\mathbf1_{h'\geq h-1}+z_i\mathbf1_{h'\geq h},
\qquad 0\leq h'\leq n-i-1.
\]
Summing over all height histories from \(h_0=h_n=0\) gives \(\lambda_n(\xi)\) exactly, since each such sequence together with its choice of east or diagonal at each column uniquely determines the path.

In the first column \(h_0=0\), so every allowable transition has weight \(1+z_0\). If \(\xi_0=1\), all signed paths cancel and \(\lambda_n(\xi)=0\). If \(\xi_0=0\), this first weight is \(2\). For each subsequent column \(i\geq1\), a downward height transition \(h'=h-1\) has weight \(1\). A flat or upward transition \(h'\geq h\) has weight \(1+z_i\), which is \(0\) or \(2\). All signed transition weights are therefore nonnegative integers.

The height history \(h_1=n-1,h_2=n-2,\ldots,h_n=0\) is always admissible. Its weight is exactly \(2\), so \(\lambda_n(\xi)\geq2\) whenever \(\xi_0=0\). If every later \(\xi_i=1\), only downward transitions survive and this is the sole possible history: \(\lambda_n(0,1,\ldots,1)=2\). Conversely, if \(\xi_i=0\) for some \(1\leq i<n\), the distinct admissible height history that begins at \(h_1=n-2\), descends by one until column \(i\), stays flat in column \(i\), and then descends to zero contributes \(2\cdot2=4\). This is in addition to the preceding contribution \(2\), proving uniqueness of the smallest nonzero multiplier.

For every binary vector \(v\), the path obtained by using a diagonal step at \((i,i)\) if \(v_i=1\), and a north step then an east step from \((i,i)\) if \(v_i=0\), is admissible. Hence \(\mu_n(v)>0\) for all \(v\). Triangle inequality then gives \(|\lambda_n(\xi)|<\lambda_n(0)=R_n\) for every nonzero \(\xi\): the character takes both signs on the full positive support. This proves the unique maximum.

Characters diagonalize group convolution. Exactly the \(2^{n-1}\) characters with \(\xi_0=0\) survive, and all have positive eigenvalues. Their span is the subspace of functions invariant under flipping coordinate zero, proving the range statement. Since convolution is normal with real nonnegative eigenvalues, the nonzero singular values have minimum \(2\) and maximum \(R_n\), proving the stated restricted condition number. The vanishing of all characters with \(\xi_0=1\) proves by Fourier inversion that \(\mu_n(0,w)=\mu_n(1,w)\) for every \(w\), establishing the asserted independence.

## Verification
The standalone standard-library script `verify_schroder.py` enumerates every path through \(n=8\), computes the integer Walsh--Hadamard transform, and compares every multiplier with an independently implemented column-transfer recurrence. For \(9\leq n\leq14\), it checks every frequency using the recurrence and independently evaluates \(R_n=\sum_{k=0}^n\binom{2n-k}{k}\frac{1}{n-k+1}\binom{2(n-k)}{n-k}\). All computations use exact integers. The script verifies all zeros, unique minimizing frequencies, full rank, and positive support. It reports 33,021 coefficient comparisons or histogram equalities; the infinite theorem follows from the preceding proof rather than this finite computation.

## Relationship to prior work
The Schröder paths and their total counts are classical. Bandlow--Egge--Killpatrick study an area-weighted bijection with pattern-avoiding permutations; Yan studies peak restrictions and pattern-avoiding partitions; Schroeder--Smith studies the path encoding of stack-sortable permutations; Alekseyev studies Catalan--Schröder lattice path enumeration. These sources supply the combinatorial context, but none of the inspected statements asserts the exact column-incidence Walsh zero set, strict positivity on its complement, or the sharp nonzero gap. The result is different from a general Schröder-number count or a specialization by the *total* number of diagonal steps: the signs here depend on the specific starting columns.

## Limitations
The theorem concerns the weighted path-counting push-forward, not a support indicator, area-weighted path law, little Schröder paths, or general step weights. It does not provide a closed elementary formula for every positive Fourier eigenvalue or an endpoint \(\ell^1\)-projection norm. Multivariate Schröder enumerators not indexed in the searched sources could already imply the statement; historical priority beyond the compared material is unresolved. No independent audit has been performed.

## References
1. S. H. F. Yan, *Schröder Paths and Pattern Avoiding Partitions*, arXiv:0805.2465, initially posted 2008-05-16. https://arxiv.org/abs/0805.2465
2. M. W. Schroeder and R. Smith, *A Bijection on Classes Enumerated by the Schröder Numbers*, arXiv:1511.00189, initially posted 2015-10-31. https://arxiv.org/abs/1511.00189
3. M. A. Alekseyev, *On Enumeration of Paths in Catalan--Schröder Lattices*, arXiv:1601.06158, initially posted 2016-01-22. https://arxiv.org/abs/1601.06158
4. J. Bandlow, E. S. Egge, and K. Killpatrick, *A Weight-Preserving Bijection Between Schröder Paths and Schröder Permutations*, *Annals of Combinatorics* 6 (2002), 235--248. https://www.ericegge.net/papers/schroderperm.pdf
