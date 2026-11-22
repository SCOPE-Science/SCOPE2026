# Multivariable Weyl-sum rigidity and an optimal coefficient-energy Calkin gap

## Finding
Let \(d\ge 2\), \(N\ge2\), and \(\mathcal F^2(\mathbb C^d)\) be the standard Gaussian Fock Hilbert space. Suppose the affine symbols \(\phi_j(z)=A_jz+b_j\), \(1\le j\le N\), are pairwise distinct, with \(A_j\in U(d)\) and \(b_j\in\mathbb C^d\). Let each \(\psi_j\) be an arbitrary nonzero entire function. On entire functions consider the finite weighted-composition expression
\[
Tf(z)=\sum_{j=1}^N\psi_j(z)f(A_jz+b_j).
\]
Then the following assertions are equivalent:

1. The displayed expression induces a bounded operator on \(\mathcal F^2(\mathbb C^d)\).
2. There exist unique nonzero constants \(c_j\in\mathbb C\) for which
\[
\psi_j(z)=c_j\exp\left(-\langle A_jz,b_j\rangle-\frac{\|b_j\|^2}{2}\right)
\quad (1\le j\le N,\ z\in\mathbb C^d).
\]

In this case each normalized summand \(V_j=W_{\exp(-\langle A_jz,b_j\rangle-\|b_j\|^2/2),\,A_jz+b_j}\) is unitary. More precisely, writing \(k_w(z)=\exp(\langle z,w\rangle-\|w\|^2/2)\), one has the **exact averaged coherent-state identity**
\[
\lim_{R\to\infty}\frac1{|B_R|}\int_{B_R}\|T^*k_w\|^2\,dV(w)
=\sum_{j=1}^N|c_j|^2,
\]
where \(B_R\subset\mathbb C^d\) is the Euclidean ball. Consequently,
\[
\boxed{\quad \|T\|_{\mathrm e}\ge\left(\sum_{j=1}^N|c_j|^2\right)^{1/2}>0.\quad}
\]
Here \(\|T\|_{\mathrm e}=\inf_{K\text{ compact}}\|T-K\|\). The coefficient \(1\) is optimal **for every cardinality** \(N\ge2\) and every dimension \(d\ge2\), even when all \(b_j=0\). In particular, distinct affine-Weyl unitaries are linearly independent modulo compact operators with a universal \(\ell_2\)-coefficient lower bound.

## Assumptions and scope
The Hermitian form \(\langle z,w\rangle=\sum_{q=1}^dz_q\overline{w_q}\) is linear in its first variable, and
\[
\|f\|_{\mathcal F^2}^2=\pi^{-d}\int_{\mathbb C^d}|f(z)|^2e^{-\|z\|^2}\,dV(z).
\]
All maps and weights are entire; no commutativity or separation-size condition is imposed on the unitary matrices or translations. Pairwise distinctness means \((A_i,b_i)\ne(A_j,b_j)\) for \(i\ne j\). The result is for **finite** sums and the Gaussian Hilbert norm, not for arbitrary contractions, infinite sums, or all integrability exponents. The proof uses only elementary Fock reproducing kernels, finite Gram-matrix positivity, entire-function Liouville rigidity, Fourier character cancellation, and standard integration principles; no published finite-sum classification is assumed.

## Proof

**1. Direct coherent-state Gram rigidity.** Boundedness of \(T\) determines all weights without assuming boundedness of any individual summand. For \(k_w(z)=\exp(\langle z,w\rangle-\|w\|^2/2)\), the reproducing property gives the exact finite expansion
\[
T^*k_w=\sum_{j=1}^N d_j(w)k_{A_jw+b_j},\qquad
d_j(w)=\overline{\psi_j(w)}\exp\left(\frac{\|A_jw+b_j\|^2-\|w\|^2}{2}\right).
\]
In particular, if \(h_j(z)=\psi_j(z)\exp(\langle A_jz,b_j\rangle)\) is entire, then
\[
|d_j(w)|=e^{\|b_j\|^2/2}|h_j(w)|.
\tag{1}
\]

Fix a unit vector \(v\) outside the finite union of proper complex-linear subspaces \(\ker(A_i-A_j)\) corresponding to pairs with \(A_i\ne A_j\). Such vectors form a dense open subset of the unit sphere. Consider the normalized kernel vectors \(k_{A_jtv+b_j}\), \(j=1,\ldots,N\), for a complex parameter \(t\) of large modulus. Partition the indices according to the common value of \(A_j\). Inside one block, the \(b_j\) are distinct. The corresponding finite family \(\{k_{b_j}\}\) is linearly independent: a relation between these Gaussian exponentials, restricted to a generic complex line \(z=su\) where the exponents \(\langle u,b_j\rangle\) are all distinct, would give a Vandermonde system with zero coefficients. Thus each within-block Gram matrix is strictly positive definite.

For fixed \(t\), translating **all** coherent states in one block by the common vector \(A_jtv\) amounts to applying one Weyl unitary and individual unimodular phases. Hence its Gram matrix is diagonally unitarily conjugate to the fixed Gram matrix of \(\{k_{b_j}\}\); in particular, the smallest eigenvalue is a positive block constant independent of \(t\). Between different blocks, our choice of \(v\) ensures \((A_i-A_j)v\ne0\). The normalized-kernel overlap has modulus
\[
|\langle k_{A_itv+b_i},k_{A_jtv+b_j}\rangle|
=\exp\left(-\frac12\|t(A_i-A_j)v+b_i-b_j\|^2\right)\longrightarrow0
\quad(|t|\to\infty).
\]
Since the number of indices is finite, the full Gram matrix of \(\{k_{A_jtv+b_j}\}_{j=1}^N\) therefore has smallest eigenvalue at least some \(\eta_v>0\) whenever \(|t|\ge R_v\). This is an exact positive-definiteness argument, not a claim that a finite experiment establishes infinite independence.

Apply the Gram estimate to \(T^*k_{tv}\): for every \(|t|\ge R_v\),
\[
\eta_v\sum_{j=1}^N|d_j(tv)|^2
\le\|T^*k_{tv}\|^2\le\|T\|^2.
\]
By (1), each entire one-variable function \(t\mapsto h_j(tv)\) is bounded outside a disk and hence bounded everywhere (continuity on the disk handles the remaining points). Liouville's theorem makes it constant, with value \(h_j(0)=\psi_j(0)\). This applies to every \(j\) and every generic \(v\); the union of these complex lines is dense in \(\mathbb C^d\). By continuity \(h_j(z)\equiv\psi_j(0)\) globally. Since \(\psi_j\not\equiv0\), necessarily \(\psi_j(0)\ne0\). Put \(c_j=\psi_j(0)e^{\|b_j\|^2/2}\), obtaining the asserted unique Gaussian-Weyl weight form. No one-variable finite-sum theorem or later literature is required for this deduction.

**2. Sufficiency and normalization.** Define
\[
(V_{A,b}f)(z)=e^{-\langle Az,b\rangle-\|b\|^2/2}f(Az+b).
\]
For unitary \(A\), the identity
\[
|e^{-\langle Az,b\rangle-\|b\|^2/2}|^2e^{-\|z\|^2}
=e^{-\|Az+b\|^2}
\]
and the volume-preserving change of variables \(y=Az+b\) show that \(V_{A,b}\) is a surjective isometry, hence unitary. Thus \(T=\sum_j c_jV_{A_j,b_j}\) is bounded.

**3. Coherent-state coefficient energy.** Standard reproducing-kernel identities give
\[
V_{A,b}^*k_w=e^{i\operatorname{Im}\langle Aw,b\rangle}k_{Aw+b},\qquad
|\langle k_x,k_y\rangle|=e^{-\|x-y\|^2/2}.
\]
For distinct \((A_i,b_i)\) and \((A_j,b_j)\), the averaged cross term
\[
\frac1{|B_R|}\int_{B_R}\langle V_i^*k_w,V_j^*k_w\rangle\,dV(w)
\]
tends to zero. Indeed, if \(A_i\ne A_j\), its integrand has modulus
\[
\exp\left(-\frac12\|(A_i-A_j)w+b_i-b_j\|^2\right).
\]
Substituting \(w=Ru\) and applying dominated convergence on the unit ball works because the kernel of the nonzero matrix \(A_i-A_j\) has Lebesgue measure zero. If \(A_i=A_j=A\), necessarily \(b_i\ne b_j\), and direct substitution into the normalized kernel inner product gives the cross term
\[
\exp\left(-\frac12\|b_i-b_j\|^2\right)
\exp\left(i\left[2\operatorname{Im}\langle Aw,b_i-b_j\rangle+
\operatorname{Im}\langle b_j,b_i\rangle\right]\right).
\]
Its normalized ball average tends to zero by the Riemann--Lebesgue lemma, as \(w\mapsto 2\operatorname{Im}\langle Aw,b_i-b_j\rangle\) is a nonzero real linear form. The diagonal terms are identically \(1\). Expanding the finite squared norm therefore proves the exact averaged identity.

**4. Passage to compact perturbations.** As \(\|w\|\to\infty\), \(k_w\rightharpoonup0\) in Fock space: this follows first against normalized monomials and then by their density. For every compact \(K\), \(\|K^*k_w\|\to0\) uniformly off sufficiently large balls. Hence the normalized ball mean of \(\|K^*k_w\|^2\) tends to zero. The triangle inequality in the Hilbert space of square-integrable vector fields yields
\[
\|T-K\|\ge\lim_{R\to\infty}\left(\frac1{|B_R|}\int_{B_R}\|(T-K)^*k_w\|^2dV(w)\right)^{1/2}
=\left(\sum_j|c_j|^2\right)^{1/2},
\]
where equality in the final limit uses Step 3 and the vanishing compact contribution. Infimizing over \(K\) proves the Calkin bound.

**5. Optimality for each \(N\).** Fix any integer \(N\ge2\), set \(\omega=e^{2\pi i/N}\), \(A_j=\omega^jI_d\), \(b_j=0\), with \(j=0,\dots,N-1\). Define unimodular chirp coefficients
\[
c_j=\begin{cases}
\exp(\pi i j^2/N),&N\ \text{even},\\
\exp(\pi i j(j+1)/N),&N\ \text{odd}.
\end{cases}
\]
They extend periodically in \(j\) modulo \(N\), and for each nonzero residue \(h\) their cyclic autocorrelation vanishes:
\[
\sum_{j=0}^{N-1}c_{j+h}\overline{c_j}
=\text{(unimodular constant)}\sum_{j=0}^{N-1}\omega^{jh}=0.
\]
Therefore their discrete Fourier transform \(\lambda_n=\sum_{j=0}^{N-1}c_j\omega^{jn}\) has constant modulus \(|\lambda_n|=\sqrt N\) at every integer \(n\). The operator \(\sum_jc_jC_{\omega^jI_d}\) is diagonal on the homogeneous polynomial subspace of total degree \(n\), with scalar \(\lambda_n\). Each residue class of degrees appears infinitely often; indeed all degrees occur. Thus its norm and essential norm both equal \(\sqrt N\), exactly \((\sum_j|c_j|^2)^{1/2}\). This proves optimality for every allowed \(N\) and \(d\).

## Verification
The necessity argument is a direct multi-variable proof and does not assume one-dimensional finite-sum rigidity. Its nonstandard step is the uniform positive lower Gram bound along generic complex rays: it explicitly partitions equal linear parts, proves positive definiteness within each block by Vandermonde, shows invariance under common Weyl translation and controls the off-block entries by Gaussian distance. The Calkin inequality follows from a complete analytic calculation of all cross terms and the compact weak-kernel test. The chirp construction has an exact finite-character proof for every \(N\), not an extrapolation from computations. The reproducible supplementary `checker.py` evaluates the chirp spectra at multiple sizes and normalized coherent-kernel phase identities for noncommuting unitary examples; its finite calculations are diagnostics only.

## Relationship to prior work
Bayart--Wang--Yao [1, Introduction and Theorems 1.1, 3.4] study several-variable **unweighted** Fock composition semigroups and identify their affine contraction and unitary boundary structure. The present question arises when allowing entire compensating weights on that boundary and adding multiple distinct symbols. Tien--Khoi [2, Theorems 3.8--3.9] characterize **individual** several-variable weighted compositions and estimate their essential norms, without deciding cancellation in finite sums. Cho--Choe--Koo--Tien [3, introduction and Theorem 1.1], published after the cited October source, prove one-variable finite weighted-sum rigidity and explicitly leave the several-variable problem open. The independent one-variable finite-sum study of Lin--Lu--Yang--Zu [4, Theorems 1.1--1.2] likewise does not cover several variables and has symbol-dependent essential norm constants. These two November papers are comparison sources, not prerequisites for the direct Gram proof. Earlier several-variable finite-sum results described in [3, Introduction] concern constant coefficients and unweighted composition operators. The present theorem establishes a natural unitary-affine multivariable case with arbitrary entire weights, together with an optimal coefficient-energy separation in the Calkin algebra. Single-operator Gaussian weights, standard coherent states and finite Fourier chirps are acknowledged as classical ingredients rather than claimed original.

## Limitations
The matrices are assumed unitary and the number of summands finite. There is no assertion about nonunitary contractions, nonlinear entire maps, general several-variable Fock exponents, exact essential norms for all coefficient choices, or uniqueness of earlier discoveries outside the inspected literature. The proof is self-contained apart from standard reproducing-kernel and entire-function facts. The lower Calkin estimate need not equal the full operator norm for arbitrary noncommuting unitary symbols. The mathematical verification presented here does not amount to independent external validation or an exhaustive priority search.

## References
1. Frédéric Bayart, Maofa Wang, and Xingxing Yao, *Semigroup of composition operators on the Fock space of several complex variables*, arXiv:2610.26349v1 (first public 19 October 2026), https://arxiv.org/abs/2610.26349.
2. Pham Trong Tien and Le Hai Khoi, *Weighted composition operators between Fock spaces in several variables*, arXiv:1801.08279v1 (first public 25 January 2018), https://arxiv.org/abs/1801.08279.
3. Hong Rae Cho, Boo Rim Choe, Hyungwoon Koo, and Pham Trong Tien, *The rigidity phenomenon for weighted composition operators on the Fock spaces*, arXiv:2611.26206v1 (19 November 2026), https://arxiv.org/html/2611.26206v1 (post-source literature comparison only).
4. Zhaopeng Lin, Yufeng Lu, Rong Yang, and Chao Zu, *Finite Sums of Weighted Composition Operators on the Fock Space*, arXiv:2611.19948v1 (15 November 2026), https://arxiv.org/html/2611.19948v1 (post-source literature comparison only).
