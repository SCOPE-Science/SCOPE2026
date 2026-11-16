# Exact zero-free residues and sharp Fourier norms for two-edge matchings in \(K_{3,n}\)

## Finding
Fix an integer \(n\ge2\). Let \(G_n=\mathbb F_2^{3n}\) have coordinates indexed by the edges \((i,a)\), where \(i\in\{1,2,3\}\) and \(a\in\{1,\ldots,n\}\), of the complete bipartite graph \(K_{3,n}\). Let \(\mathcal M_n\subseteq G_n\) consist of the incidence vectors of its two-edge matchings, and define its unnormalized Walsh transform by
\[
 W_n(x)=\sum_{m\in\mathcal M_n}(-1)^{\langle m,x\rangle},\qquad x\in G_n.
\]
Put \(s_{ia}=(-1)^{x_{ia}}\), \(S_i=\sum_{a=1}^{n}s_{ia}\), and \(C_{ij}=\sum_{a=1}^{n}s_{ia}s_{ja}\). Every coefficient is explicitly
\[
 \boxed{W_n(x)=\sum_{1\le i<j\le3}(S_iS_j-C_{ij}).}
\]
More precisely, all coefficients satisfy the uniform congruence
\[
 \boxed{W_n(x)\equiv 3n(n-1)\pmod4.}
\]
The exact zero-free classification is
\[
 \boxed{W_n(x)\ne0\text{ for every }x\in G_n\quad\Longleftrightarrow\quad n\equiv2,3\pmod4.}
\]
Equivalently, ordinary convolution by \(\mathbf1_{\mathcal M_n}\) is invertible on functions on \(G_n\) exactly for these two residue classes. In the zero-free cases, every Walsh coefficient has exact two-adic valuation one. In the other cases (\(n\ge4\)), there are explicit sign assignments with coefficient zero.

Let \(P_n\) be the Fourier multiplier on functions on \(G_n\) that retains precisely the characters indexed by \(\mathcal M_n\). Its sharp endpoint norms have an exact finite formula and a Gaussian limit:
\[
 \boxed{\|P_n\|_{\ell^1\to\ell^1}=\|P_n\|_{\ell^\infty\to\ell^\infty}
 =2^{-3n}\sum_{x\in G_n}|W_n(x)|,\qquad
 \lim_{n\to\infty}\frac{\|P_n\|}{n}=\frac2{\sqrt3}.}
\]
This is a statement about the operator norm of the Fourier projection, not the invertibility of that projection; it is the separate convolution operator by \(\mathbf1_{\mathcal M_n}\) whose invertibility is characterized above.

An exact coefficient-multiplicity and norm formula of polynomial-size summation complexity is also available. Let \(\mathscr U=\{-1,1\}^3\) and let \(\mathbf t=(t_u)_{u\in\mathscr U}\) range over nonnegative integers with \(\sum_ut_u=n\). Set
\[
 A_i(\mathbf t)=\sum_ut_uu_i,\quad B_{ij}(\mathbf t)=\sum_ut_uu_iu_j,\quad
 F(\mathbf t)=\sum_{i<j}\big(A_i(\mathbf t)A_j(\mathbf t)-B_{ij}(\mathbf t)\big).
\]
For every integer \(v\), the number of characters whose Walsh coefficient equals \(v\) is exactly
\[
 \boxed{\sum_{\mathbf t:F(\mathbf t)=v}\frac{n!}{\prod_ut_u!}.}
\]
In particular,
\[
 \boxed{\|P_n\|=8^{-n}\sum_{\mathbf t:\sum t_u=n}\frac{n!}{\prod_ut_u!}|F(\mathbf t)|.}
\]
These are complete all-\(n\) formulas, not only asymptotic descriptions.

## Assumptions and scope
All matching edges are distinct, with neither a common left endpoint nor a common right endpoint. The cardinality of \(\mathcal M_n\) is \(3n(n-1)\): choose an unordered pair of left vertices, then an ordered choice of two distinct right vertices. The Walsh transform is unnormalized, and expectations over signs use the uniform distribution on \(G_n\). The Fourier projection uses multiplier \(\mathbf1_{\mathcal M_n}\); the associated convolution kernel is \(2^{-3n}W_n\). Both counting and probability normalizations give the same finite-dimensional endpoint operator norms.

## Proof
**1. Exact transform and multiplicities.** Every two-edge matching consists of \((i,a)\) and \((j,b)\) with \(i<j\) and \(a\ne b\). Its Walsh sign is \(s_{ia}s_{jb}\). Thus the contribution from the pair \((i,j)\) is
\[
 \sum_{a\ne b}s_{ia}s_{jb}
 =\left(\sum_as_{ia}\right)\left(\sum_bs_{jb}\right)-\sum_as_{ia}s_{ja}
 =S_iS_j-C_{ij},
\]
and summing the three row pairs proves the transform formula. A sign assignment can be encoded uniquely by its \(n\) column vectors in \(\mathscr U\); given the eight column multiplicities \(\mathbf t\), the number of assignments is \(n!/\prod_ut_u!\). This proves the exact spectrum and norm sums.

**2. The mod-four obstruction.** A single sign flip at edge \(e=(i,a)\) changes \(W_n\) by
\[
 -2s_e\sum_{f\text{ disjoint from }e}s_f.
\]
Exactly \(2(n-1)\) edges are disjoint from \(e\), an even number. Therefore this change is a multiple of four. Every signing is obtained from the all-positive signing by flips, while the all-positive value is \(3n(n-1)\). Hence the asserted congruence holds everywhere. For \(n\equiv2,3\pmod4\), one has \(3n(n-1)\equiv2\pmod4\), so a zero is impossible and every coefficient has valuation one.

**3. Zeros in all remaining dimensions.** Consider four columns with sign vectors
\[
 (1,1,1),\ (1,-1,-1),\ (-1,1,-1),\ (-1,-1,1).
\]
Their three row sums and their three pairwise column inner-product sums all vanish. If \(n=4k\), concatenate \(k\) such blocks. Then every \(S_i\) and \(C_{ij}\) is zero, so \(W_n=0\). If \(n=4k+1\), append one arbitrary sign column \(u\). Then \(S_i=u_i\) and \(C_{ij}=u_iu_j\), so each difference \(S_iS_j-C_{ij}\) is zero. As \(n\ge2\), these constructions cover precisely the remaining congruence classes. Fourier diagonalization of convolution proves the invertibility equivalence.

**4. Exact endpoint norm.** On the finite Abelian group \(G_n\), the idempotent multiplier \(\mathbf1_{\mathcal M_n}\) has convolution kernel \(K_n(x)=2^{-3n}W_n(x)\). Translation invariance shows every absolute row sum and every absolute column sum of the convolution matrix is \(\sum_x|K_n(x)|\), proving both endpoint equalities sharply. A point mass attains the \(\ell^1\) norm, while a sign choice aligned with one row attains the \(\ell^\infty\) norm.

**5. Gaussian limit and its exact constant.** Choose all \(s_{ia}\) independently and uniformly from \(\{-1,1\}\). Write \(X_{i,n}=S_i/\sqrt n\). The three variables \(X_{i,n}\) are independent, and the central limit theorem gives joint convergence to independent standard normals \(Z_1,Z_2,Z_3\). The correlation term has the exact second-moment estimate
\[
 \mathbb E\left|n^{-1}\sum_{i<j}C_{ij}\right|^2=\frac3n,
\]
since each column contributes three pairwise orthogonal mean-zero products. Therefore
\[
 n^{-1}W_n\ \Longrightarrow\ Q=Z_1Z_2+Z_1Z_3+Z_2Z_3.
\]
Walsh-character orthogonality also gives \(\mathbb E W_n^2=|\mathcal M_n|=3n(n-1)\); hence \(n^{-1}W_n\) has uniformly bounded second moments. Its absolute values are uniformly integrable, so \(\mathbb E|W_n|/n\to\mathbb E|Q|\).

An orthogonal rotation of the Gaussian coordinates diagonalizes \(Q\) as \(U^2-(V^2+T^2)/2\), where \(U,V,T\) are independent standard normals. The variable \(Y=(V^2+T^2)/2\) is independent of \(U\) and has the exponential law of mean one. Thus
\[
 \begin{aligned}
 \mathbb E|U^2-Y|&=\mathbb E(U^2+Y)-2\mathbb E\min(U^2,Y)\\
 &=2-2\mathbb E(1-e^{-U^2})=2\mathbb E e^{-U^2}=\frac2{\sqrt3}.
 \end{aligned}
\]
This establishes the sharp asymptotic constant for both endpoint norms.

## Verification
Run `python3 verify.py` using only the Python standard library. The script constructs the full Walsh transform independently from the frequency indicator for \(2\le n\le5\), compares it with the eight-column multinomial formula, and independently evaluates the signed-matching polynomial on random columns. It computes exact coefficient multiplicities, Walsh second moments, zero criteria, congruences, and rational endpoint norms through \(n=12\); explicit zero constructions are checked through \(n=64\). A Gaussian Monte Carlo calculation checks only the numerical constant, not the analytic limit.

The exact checker output ends with `K3N_TWO_MATCHING_WALSH_ALL_CHECKS_PASS`. The infinite assertions are justified by the proof above, independently of these computations.

## Relationship to prior work
Goodall's *Graph polynomials and Tutte-Grothendieck invariants: an application of elementary finite Fourier analysis* (arXiv:0806.4848v1, publicly available 2008-06-30), particularly Sections 4–5, provides finite-Abelian Fourier conventions, convolution duality and graphical Fourier applications. Its coefficient-norm applications concern graph polynomials and Tutte-type invariants; it does not evaluate the matching-orbit transform for \(K_{3,n}\).

Nourdin, Peccati and Reinert's *Stein's method and stochastic analysis of Rademacher functionals* (arXiv:0810.2890, originally posted 2008-10-16) develops Gaussian approximation for Rademacher functionals. The limit here is a non-Gaussian, indefinite quadratic Gaussian chaos, not their claimed Gaussian approximation for low-influence second-order forms.

The published result *Exact degree-two Hamming projection norms and the Gaussian–Poisson crossover* (published-finding corpus identifier `2026/10/11/SCOPE-exact-degree-two-hamming-projection-norms-and-the-gaussian-poiss--cd09d9ad5ea2`) treats all pairs of Hamming coordinates and q-ary radial kernels. The current frequency set is the strict bipartite-matching subset of the binary degree-two shell, with a positive fraction of frequency pairs excluded as \(n\to\infty\); the Hamming coefficient and norm formulas therefore do not imply this sign classification or constant. Existing results for four- and six-cycle orbits of \(K_{3,n}\) also concern disjoint frequency families and different polynomial degrees.

## Limitations
The exact zero/nonzero classification is for **two-edge matchings** in \(K_{3,n}\), not arbitrary matching sizes or arbitrary bipartite graphs. The asymptotic norm has no rate claimed. The multinomial sum is a finite exact specification, not a constant-size closed form. Exhaustive priority over differently named signed matching and finite Fourier literature is not asserted; an unlocated equivalent formula is a residual historical risk. The numerical checks are finite and not independent mathematical validation.

## References
1. A. Goodall, *Graph polynomials and Tutte-Grothendieck invariants: an application of elementary finite Fourier analysis*, arXiv:0806.4848v1 (30 June 2008), https://arxiv.org/abs/0806.4848.
2. I. Nourdin, G. Peccati and G. Reinert, *Stein's method and stochastic analysis of Rademacher functionals*, arXiv:0810.2890 (16 October 2008 first version), https://arxiv.org/abs/0810.2890.
3. *Exact degree-two Hamming projection norms and the Gaussian–Poisson crossover*, published record 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-degree-two-hamming-projection-norms-and-the-gaussian-poiss--cd09d9ad5ea2.
