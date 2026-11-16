# Parity-complete Fourier invertibility and sharp spectral gap for ladder spanning trees

## Finding

For each integer \(n\ge1\), let \(L_n=P_n\square K_2\) be the two-rail ladder with \(2n\) vertices and \(3n-2\) edges (with \(L_1=K_2\)). Let \(\mathcal T_n\subseteq\mathbb F_2^{E(L_n)}\) be the binary incidence vectors of its spanning trees. For every frequency \(\omega\in\mathbb F_2^{E(L_n)}\), write
\[
W_n(\omega)=\sum_{T\in\mathcal T_n}(-1)^{\sum_{e\in T}\omega_e}.
\]
Then the Fourier multiplier \(W_n\) is nowhere zero **if and only if** \(n\) is odd. In fact, for odd \(n\),
\[
\min_{\omega}|W_n(\omega)|=1,
\]
and the minimum is attained by changing the sign of every rung and of no rail edge. The resulting coefficient, for every \(n\), is exactly
\[
W_n(\omega_{\rm rung})=-\sin(\pi n/2).
\]
For even \(n=2m\), at least \(2^{m-1}\) distinct frequencies have \(W_n(\omega)=0\): give every rung sign \(-1\), give both copies of each odd-indexed horizontal edge sign \(+1\), and assign independently either sign to both copies of each even-indexed horizontal edge.

Consequently, for the unnormalized convolution operator \(C_nh=\mathbf1_{\mathcal T_n}*h\) on \(\ell^2(\mathbb F_2^{E(L_n)})\),
\[
\begin{aligned}
&n\text{ odd}: &&\|C_n\|_{2\to2}=\tau_n,\quad \|C_n^{-1}\|_{2\to2}=1,\quad\kappa_2(C_n)=\tau_n,\\
&n\text{ even}:&&C_n\text{ is singular},
\end{aligned}
\]
where the established ordinary ladder spanning-tree count is
\[
\tau_n=\frac{(2+\sqrt3)^n-(2-\sqrt3)^n}{2\sqrt3}.
\]

## Assumptions and scope

The Fourier group is the Boolean edge cube, with counting-measure (unnormalized) convolution and Walsh transform. Each edge frequency independently specifies a sign \(s_e=(-1)^{\omega_e}\). The rail edges have labels \(j\leftrightarrow j+1\), \(1\le j<n\), on each rail. A rung joins the two vertices of column \(j\). No probability normalization is used in \(W_n\) or \(C_n\); the spectral condition number is the product of the operator norms of \(C_n\) and its inverse. The theorem includes the one-rung case \(n=1\).

## Proof

**1. Fourier coefficients are signed tree sums.** For a sign assignment \(s_e\in\{-1,1\}\), the weighted matrix-tree theorem gives
\[
W_n(\omega)=\sum_{T\text{ spanning}}\prod_{e\in T}s_e
=\text{any cofactor of }\mathcal L(s),
\]
where \(\mathcal L(s)\) is the signed-weight Laplacian (weighted degree on the diagonal; negative of the edge weight off diagonal). Equivalently, if the graph has \(N\) vertices, \(W_n(\omega)\) is the coefficient of \(t\) in \(\det(\mathcal L(s)+tI)\), divided by \(N\). This coefficient identity holds for negative weights as well, including when additional zero eigenvalues occur.

**2. A two-rail determinant factorization.** Assign each horizontal edge \(j\leftrightarrow j+1\) weight \(a_j\in\{-1,1\}\) on both rails and each rung weight \(-1\). Let \(H_n(a)\) be the weighted path Laplacian of the length-\(n\) rail. The full weighted ladder Laplacian is
\[
\mathcal L(s)=\begin{pmatrix}H_n(a)-I&I\\I&H_n(a)-I\end{pmatrix}.
\]
The symmetric and antisymmetric rail subspaces give the exact polynomial factorization
\[
\det(\mathcal L(s)+tI)=\det(H_n(a)+tI)\det(H_n(a)-2I+tI).
\]
Because a path has exactly one spanning tree, its weighted tree sum equals \(\prod_{j=1}^{n-1}a_j\), so the coefficient of \(t\) in \(\det(H_n(a)+tI)\) is \(n\prod a_j\). The coefficient of \(t\) in the ladder determinant is therefore \(n(\prod a_j)\det(H_n(a)-2I)\). Dividing by \(2n\) proves
\[
W_n(\omega_a)=\frac12\left(\prod_{j=1}^{n-1}a_j\right)\det(H_n(a)-2I).
\tag{1}
\]
For \(n=1\), products over the empty set are interpreted as \(1\).

**3. The exact minimum for odd lengths.** With all \(a_j=1\), the path Laplacian has eigenvalues \(2-2\cos(k\pi/n)\), \(0\le k<n\). Hence
\[
\det(H_n(1)-2I)=\prod_{k=0}^{n-1}\big(-2\cos(k\pi/n)\big)=-2\sin(\pi n/2).
\]
(The final equality also follows from the tridiagonal continuant.) Equation (1) gives \(W_n(\omega_{\rm rung})=-\sin(\pi n/2)\), of magnitude \(1\) at every odd length.

The established ladder enumeration gives \(\tau_1=1\), \(\tau_2=4\), and \(\tau_n=4\tau_{n-1}-\tau_{n-2}\) for \(n\ge3\), yielding the displayed closed form and \(\tau_n\equiv\tau_{n-2}\pmod2\). Thus \(\tau_n\) is odd for odd \(n\). Since changing any spanning-tree sign changes a summand by an even integer,
\[
W_n(\omega)\equiv\tau_n\equiv1\pmod2
\]
for **every** frequency when \(n\) is odd. All coefficients are then nonzero integers with absolute value at least \(1\); the explicitly evaluated rung frequency attains that bound.

**4. Exponentially many zeros for even lengths.** Let \(n=2m\). Choose \(a_j=1\) for every odd \(j\), while the \(m-1\) even-indexed values are arbitrary elements of \(\{-1,1\}\). Set \(u=(1,-1,-1,1,1,-1,-1,1,\ldots)\in\mathbb R^n\), truncated at length \(2m\). Across any even-indexed rail edge the adjacent entries of \(u\) are equal, so the edge contributes zero to \(H_n(a)u\). Across each odd-indexed edge the weight is \(+1\) and the adjacent entries have opposite signs; each vertex belongs to exactly one such edge. Therefore \(H_n(a)u=2u\). The nonzero vector \(u\) lies in the kernel of \(H_n(a)-2I\), so (1) gives \(W_n(\omega_a)=0\). There are \(2^{m-1}\) different such sign assignments and thus that many distinct Fourier zeros.

**5. Exact \(\ell^2\) stability.** Walsh characters diagonalize convolution by \(\mathbf1_{\mathcal T_n}\) with eigenvalues \(W_n(\omega)\). The triangle inequality gives \(\max_\omega|W_n(\omega)|\le\tau_n\), with equality at the trivial frequency. When \(n\) is odd, Step 3 gives \(\min_\omega|W_n(\omega)|=1\). Thus \(\|C_n\|_{2\to2}=\tau_n\), \(\|C_n^{-1}\|_{2\to2}=1\), and \(\kappa_2(C_n)=\tau_n\). Step 4 establishes noninvertibility for even \(n\).

## Verification

Run the standalone, standard-library-only script `ladder_walsh_check.py` using `python3 ladder_walsh_check.py`. It independently enumerates spanning trees by a disjoint-set cycle test, performs the full integer Walsh–Hadamard transform for \(1\le n\le7\), checks all parity and extreme-modulus assertions, and checks the explicitly constructed even-length zeros. The complete computed zero counts at lengths \(n=2,4,6\) are respectively \(6,200,7378\), used only as finite consistency checks and **not** asserted as an infinite zero-count formula. Separate exact integer determinant calculations check the special rung sign for \(1\le n\le13\); the witness eigenvector is checked over every flexible even-length sign assignment up to \(n=22\). The program prints `LADDER_SPANNING_TREE_WALSH_EXACT_CHECKS_PASS` on success.

## Relationship to prior work

The ordinary ladder spanning-tree enumeration and recurrence are established in work on grid graphs by Desjarlais–Molina and explicitly developed in Raff's 2008 preprint. The weighted matrix-tree theorem is classical; the present argument does not claim it or the path Laplacian spectrum as new. The distinct point is the evaluation of the **entire signed Walsh multiplier's zero-free dimensions**, the explicit many-zero mechanism in complementary dimensions, and the attained minimum absolute multiplier that gives exact inverse stability. General signed-tree and weighted-tree determinant theory enables the reduction but does not itself state these conclusions for this Boolean edge-cube family. Existing results for other spanning-tree orbits (including wheel graphs) concern distinct graphs and have no implication giving these ladder assertions.

## Limitations

No general formula for the total number of zero coefficients at even lengths is claimed, beyond the proved lower bound. No \(\ell^1\) or \(\ell^\infty\) convolution-inverse norm is claimed. The statement concerns two-rail **open** ladders, not cylindrical ladders or grids of larger fixed width. The novelty comparison is bounded by the examined literature and published mathematical records; an unindexed equivalent signed-ladder specialization cannot be excluded.

## References

1. P. Raff, *Spanning Trees in Grid Graphs*, arXiv:0809.2551v1, first posted 15 September 2008, especially §4 (ordinary ladder recurrence), https://arxiv.org/abs/0809.2551.
2. M. Desjarlais and R. Molina, *Counting Spanning Trees in Grid Graphs*, Congressus Numerantium **145** (2000), 177–186. Accessible partial text: https://www.yumpu.com/en/document/view/52170177/counting-spanning-trees-in-grid-graphs-alma-college.
3. S. Klee and M. T. Stamps, *Linear Algebraic Techniques for Weighted Spanning Tree Enumeration*, arXiv:1903.03575 (2019), especially Theorem 1 (weighted matrix-tree identity), https://arxiv.org/abs/1903.03575.
4. S. Mallik, *Matrix Tree Theorem for the Net Laplacian Matrix of a Signed Graph*, arXiv:2210.03711 (2022), especially §3, https://arxiv.org/abs/2210.03711.
