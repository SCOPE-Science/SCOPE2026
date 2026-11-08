# Three-snapshot recovery and square-dimensional obstructions on Boolean Hamming shells

## Finding

Fix \(n\ge5\), \(2\le k\le n-2\), and observe the normalized-graph-heat evolution of a Walsh-degree-at-most-two signal at every vertex in a single Hamming shell \(\Omega_k\) at \(m\) consecutive equally spaced times. Put \(u=n-2k\), and define
\[
a_0=1+\mathbf1_{u\ne0}+\mathbf1_{u^2\ne n},\qquad a_1=1+\mathbf1_{u\ne0}.
\]
Then the exact complex rank of the observation operator is
\[
\boxed{\operatorname{rank}\mathcal M_m=\min(m,a_0)+(n-1)\min(m,a_1)+\frac{n(n-3)}2.}
\]
Consequently one snapshot always gives rank \(\binom n2\). At generic shells \(u\ne0\) and \(u^2\ne n\), two snapshots have codimension one and exactly three are necessary and sufficient for recovering every degree-two bandlimited initial signal. At the central shell \(u=0\), infinitely many snapshots leave a kernel of dimension \(n\). At the off-central square-dimensional resonances \(u^2=n\), infinitely many snapshots leave a kernel of dimension one. These are all obstructions.

## Assumptions and scope

Identify the Boolean cube with \(X=\{-1,1\}^n\). Define \(\Omega_k=\{x\in X:\#\{i:x_i=-1\}=k\}\), and \(\chi_S(x)=\prod_{i\in S}x_i\). The domain \(\mathcal B_{\le2}=\operatorname{span}_{\mathbb C}\{\chi_S:|S|\le2\}\) has dimension \(1+n+\binom n2\). Let \(L=I-n^{-1}\sum_{i=1}^n T_i\), where \(T_i\) flips coordinate \(i\). Thus \(L\chi_S=2|S|\chi_S/n\). Fix \(\tau>0\) and integer \(m\ge1\). The operator \(\mathcal M_m\) sends \(f\) to the array \(\{(e^{-j\tau L}f)(x):0\le j<m,\ x\in\Omega_k\}\). Rank is algebraic over \(\mathbb C\), independently of normalization of these measurements.

## Proof

Set \(T(x)=\sum_i x_i\). On \(\Omega_k\), \(T(x)=u=n-2k\). Decompose each Walsh homogeneous degree into three mutually independent permutation-symmetry types: the scalar type, the centered-coordinate type, and, in degree two, the edge-harmonic type.

The scalar-type degree-zero, -one, and -two basis functions restrict respectively to
\[
1,\qquad T=u,\qquad \sum_{i<j}x_ix_j=(u^2-n)/2.
\]
Therefore exactly \(a_0\) of these three homogeneous components have nonzero spatial restriction. At time \(j\), their multipliers are the distinct geometric sequences \(1\), \(e^{-2j\tau/n}\), and \(e^{-4j\tau/n}\). The scalar observation block consequently has rank \(\min(m,a_0)\) by the Vandermonde determinant.

For each coefficient vector \(a=(a_i)\) with \(\sum_i a_i=0\), the standard-type degree-one function is \(\sum_i a_ix_i\). Its degree-two partner has coefficients \(a_i+a_j\), so the identity
\[
\sum_{i<j}(a_i+a_j)x_ix_j=T(x)\sum_i a_ix_i
\]
shows that its restriction is \(u\) times the same standard function. Since \(1\le k\le n-1\), restriction of the centered coordinate space is injective: if \(\sum_i a_i x_i\) vanishes at every point on the shell, swapping one negative and one positive coordinate forces every \(a_i\) equal, and hence all are zero. The time block on each of the \(n-1\) standard dimensions has rank \(\min(m,1+\mathbf1_{u\ne0})\).

To handle the remaining degree-two component, let \(c=(c_{ij})_{i<j}\) satisfy \(\sum_{j\ne i}c_{\min(i,j),\max(i,j)}=0\) for each \(i\). This edge-harmonic space has dimension \(\binom n2-n=n(n-3)/2\), because the unsigned incidence matrix of the complete graph has rank \(n\) for \(n\ge3\). On the shell, put \(A(x)=\{i:x_i=-1\}\). By the row-sum conditions,
\[
\sum_{i<j}c_{ij}x_ix_j=4\sum_{\{i,j\}\subset A(x)}c_{ij}.
\]
For a uniformly random \(k\)-subset \(A\), counting ordered pairs of edges according to intersection size gives
\[
\mathbb E\left|\sum_{\{i,j\}\subset A}c_{ij}\right|^2
=\left(\frac{(k)_2}{(n)_2}-2\frac{(k)_3}{(n)_3}+\frac{(k)_4}{(n)_4}\right)\sum_{i<j}|c_{ij}|^2
=\frac{k(k-1)(n-k)(n-k-1)}{n(n-1)(n-2)(n-3)}\sum_{i<j}|c_{ij}|^2.
\]
Here \((z)_r\) denotes a falling factorial, with the convention \((k)_r=0\) for \(r>k\). For \(2\le k\le n-2\) the coefficient is positive. Thus the degree-two edge-harmonic component is injectively visible already at a single snapshot. Its image is orthogonal on the uniform shell to both the scalar and centered-coordinate images: the same row-sum conditions and permutation invariance annihilate their cross moments. Its rank contribution is \(n(n-3)/2\).

The three image types are mutually orthogonal and the heat operator preserves each homogeneous degree. Their space-time ranks therefore add, giving the displayed formula for all \(m\ge1\). With \(a_0\in\{2,3\}\), \(a_1\in\{1,2\}\), the formula directly gives the one-snapshot, two-snapshot, and asymptotic ranks. The full source dimension is \(1+n+\binom n2\). In the generic regime, \(a_0=3\), \(a_1=2\): two snapshots miss only one scalar direction while three have full rank. If \(u=0\), \(a_0=2\), \(a_1=1\), yielding an eventual deficit of \(n\). If \(u^2=n\ne0\), \(a_0=2\), \(a_1=2\), yielding an eventual deficit of one. These exhaust all cases. In particular the off-center obstruction occurs exactly at integer square dimensions with interior levels \(k=(n\pm\sqrt n)/2\).

## Verification

Run `python3 CHECK.py` using a standard Python 3 installation. The standalone checker constructs the complete time-stacked Walsh observation matrix, replaces the three distinct positive heat eigenmultipliers with the algebraically equivalent test sequence \(1,2,4\) (the rank formula depends only on distinctness), and compares 56 computed finite-field matrix ranks to the formula for all \(n=5,6,7,8\), all eligible \(k\), and \(m=1,2,3,4\). It also checks three arithmetic resonances. Finite-field tests are corroboration only; the exact dimension-independent proof above establishes the theorem.

## Relationship to prior work

Bulai, Cabrelli, Cordero, Molter and Saliani (2026) establish the graph Paley--Wiener and finite dynamical-sampling framework, and examine path-graph conditioning. Their accessible abstract does not state the Hamming-shell quadratic-band rank law. The general finite-index dynamical-sampling characterization of Cabrelli and collaborators provides an abstract frame condition but not these explicit shell-dependent arithmetic ranks. Published work entitled *Square-dimension spectral resonances for quadratic-band Walsh concentration on Hamming shells* treats the one-snapshot static concentration spectrum, including spectral coincidences governed by a different square condition, whereas the present theorem determines all numbers of temporally separated heat observations and a sharp restoration threshold. Published work on all-degree \(q\)-ary Hamming-sphere sampling likewise concerns static restriction, not the temporal block decomposition here.

## Limitations

The result concerns the full single shell with \(2\le k\le n-2\), Walsh degree at most two, and heat evolution at distinct equispaced times. It gives exact ranks and injectivity, not optimal condition numbers or robustness to measurement noise. Its distinct-time conclusions apply to any diagonal evolution whose degree-zero, -one, and -two multipliers are pairwise distinct and have a Vandermonde trajectory. No statement is made about higher Walsh degrees. The full texts of several relevant sources were not accessible in this review, and equivalent earlier expressions using Krawtchouk matrices or observability criteria remain a publication-priority risk; independent audit has not been performed.

## References

1. I. M. Bulai, C. Cabrelli, E. Cordero, U. Molter, S. Saliani, *Dynamical Sampling in Graph Paley--Wiener Spaces*, arXiv:2609.25472, first posted 2026-09-21.
2. C. Cabrelli, U. Molter, V. Paternostro, F. Philipp, *Dynamical Sampling on Finite Index Sets*, arXiv:1702.03384.
3. *Square-dimension spectral resonances for quadratic-band Walsh concentration on Hamming shells*, published mathematical research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-square-dimension-spectral-resonances-for-quadratic-band-walsh-co--7e1319aedf95.
4. *An all-degree spectral law for Fourier sampling on q-ary Hamming spheres*, published mathematical research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-an-all-degree-spectral-law-for-fourier-sampling-on-q-ary-hamming--f3d01cadaa90.
5. S. Rao, *The Fourier Transform of Restrictions of Functions on the Slice*, arXiv:2111.03213.
