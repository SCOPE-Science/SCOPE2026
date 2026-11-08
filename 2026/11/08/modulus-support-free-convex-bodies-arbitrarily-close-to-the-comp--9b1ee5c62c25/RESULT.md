# Modulus-support-free convex bodies arbitrarily close to the complex \(c_0\) unit ball

## Finding
Let \(E=c_0(\mathbb C)\) with its usual supremum norm and closed unit ball \(B\). For \(n\geq1\), put \(t_n=2^{-(n+1)}\), and define the complex-linear operator
\[
 (Az)_n=\sum_{k=1}^{\infty}t_n^k z_k.
\]
For every real \(0<\tau<3\), define the **real-linear** operator and convex body
\[
 R_\tau z=z+\tau A(\overline z),\qquad K_\tau=R_\tau(B).
\]
Then \(R_\tau\) is a bounded real-linear automorphism and its perturbation of the identity is real-nuclear. Moreover,
\[
 \|R_\tau-I\|=\frac{\tau}{3},\qquad
 (1-\tau/3)B\subseteq K_\tau\subseteq(1+\tau/3)B,
 \qquad d_H(K_\tau,B)\leq\tau/3.
\]
Every \(K_\tau\) is nonempty, bounded, closed, convex, centrally symmetric, and has nonempty interior. For **every nonzero continuous complex-linear functional** \(f\in E^*\), the supremum
\[
 \sup_{y\in K_\tau}|f(y)|
\]
is **not attained**. In particular, for each \(\delta>0\) there is such a convex body within Hausdorff distance \(\delta\) of \(B\), obtained from \(B\) by a real-nuclear perturbation of the identity of operator norm less than \(\delta\).

## Assumptions and scope
All scalars in \(E\) and \(E^*\) are complex, but convexity and linearity of \(R_\tau\) are over the real field. The operator \(z\mapsto\overline z\) conjugates each coordinate. The unit ball is \(B=\{z\in E:\|z\|_\infty\leq1\}\). Hausdorff distance is measured using \(\|\cdot\|_\infty\). Real-nuclear means a norm-convergent sum of real rank-one maps with summable products of operator and functional norms. There is **no claim** that \(K_\tau\) is balanced under multiplication by every complex scalar; such a claim would conflict with complex Bishop–Phelps norm attainment.

## Proof
**Step 1: a nuclear moment operator.** For each \(n\), the coordinate functional \(\rho_n(z)=\sum_{k\geq1}t_n^k z_k\) has norm
\[
 \|\rho_n\|=\sum_{k\geq1}t_n^k=\frac{t_n}{1-t_n}.
\]
Since \(0<t_n\leq1/4\) and \(\sum_{n\geq1}t_n=1/2\),
\[
 \sup_n\|\rho_n\|=1/3,\qquad
 \sum_{n\geq1}\|\rho_n\|\leq\frac43\sum_{n\geq1}t_n=\frac23.
\]
Thus \(A=\sum_{n\geq1}e_n\rho_n\) converges in nuclear norm, maps \(E\) into \(E\), and has \(\|A\|=1/3\) (the first row yields equality on finitely supported vectors approaching the constant-one vector). The conjugate-linear map \(A\circ\mathrm{conj}\) is real-nuclear: each complex coordinate row splits into its real and imaginary scalar coordinate functionals, so its real nuclear norm is at most \(2\sum_n\|\rho_n\|\leq4/3\).

**Step 2: the near-identity real automorphism.** We have \(\|R_\tau-I\|=\tau/3<1\), and the Neumann series on the underlying real Banach space yields
\[
 R_\tau^{-1}=\sum_{m=0}^{\infty}\bigl(-\tau A\circ\mathrm{conj}\bigr)^m,
 \qquad \|R_\tau^{-1}\|\leq(1-\tau/3)^{-1}.
\]
Consequently \(R_\tau(B)\) is closed (as the image under a homeomorphism), bounded, real-convex and symmetric. The inverse bound gives the inner ball inclusion, the direct bound the outer inclusion. For \(z\in B\), its image \(R_\tau z\in K_\tau\) lies within \(\tau/3\) of \(z\); the same pairing, in the other direction, proves \(d_H(K_\tau,B)\leq\tau/3\).

**Step 3: absence of modulus-support functionals.** Fix nonzero \(f_a(y)=\sum_{n\geq1}a_ny_n\), where \(a\in\ell_1(\mathbb C)\). Then
\[
 f_a(R_\tau z)=\sum_{k\geq1}\left(a_k z_k+\tau b_k\overline{z_k}\right),
 \qquad b_k=\sum_{n\geq1}a_n t_n^k.
\]
All rearrangements are absolute, because
\[
 \sum_{k\geq1}|b_k|\leq\sum_{n\geq1}|a_n|\frac{t_n}{1-t_n}
 \leq\frac13\|a\|_1.
\]
Suppose this modulus has a maximum at \(z\in B\). For any index \(k\) with \(|z_k|<1\) and any sufficiently small complex \(w\), both \(z+we_k\) and \(z-we_k\) belong to \(B\). With \(v=a_kw+\tau b_k\overline w\), the parallelogram identity shows
\[
 |f_a(R_\tau(z+we_k))|^2+|f_a(R_\tau(z-we_k))|^2
 =2|f_a(R_\tau z)|^2+2|v|^2.
\]
Maximality forces \(v=0\) for every complex \(w\). Taking \(w\) real and purely imaginary yields \(a_k=b_k=0\). As \(z_k\to0\), this holds for all sufficiently large \(k\). In particular \(a\) has finite support.

Choose its smallest nonzero index \(n_0\). Strict decrease of \(t_n\) gives
\[
 \frac{b_k}{t_{n_0}^k}=a_{n_0}+\sum_{n>n_0}a_n\left(\frac{t_n}{t_{n_0}}\right)^k
 \longrightarrow a_{n_0}\neq0
 \quad(k\to\infty),
\]
where the sum is finite. Hence \(b_k\neq0\) for all sufficiently large \(k\), contradicting the necessary eventual vanishing above. Thus no nonzero \(f_a\) attains its maximum modulus on \(K_\tau\).

## Verification
The proof covers every real \(0<\tau<3\) and every nonzero \(a\in\ell_1(\mathbb C)\). The essential infinite-dimensional step is the dominance of the first nonzero coefficient in the finite exponential sum for \(b_k\); finite checks are not used to extrapolate this limit. The standalone script `check_finite_profiles.py` reproduces exact-rational finite row-norm, Vandermonde-tail and convergence identities; it tests examples only and is **not** an infinite proof.

## Relationship to prior work
Luo's 2026 example established the existence of a bounded closed convex set in complex \(c_0\) with no modulus-support functionals. It uses \(T(B_{c_0(\mathbb R)})+iB_{c_0(\mathbb R)}\), a product of two real balls. The present construction instead deforms the **standard complex unit ball itself** by a real-nuclear operator of arbitrarily small norm; its Hausdorff and ball-inclusion estimates do not follow from the displayed bounds in Luo's theorem. The finite-moment domination mechanism is related to Luo's row argument, but the complex-conjugate coupling and near-unit-ball conclusion are different. Golinskii and Kadets (2020) analyzed a separate complex \(c_0\) convex hull with nontrivial modulus-support functionals, so that example does not supply this conclusion. The original Lomonosov obstruction lived in a different complex Banach space. No claim of exhaustive publication-priority certification is made.

## Limitations
The claim concerns real-convex bodies; it does not furnish a complex-balanced unit ball or contradict the usual complex norm-attainment theorem. The upper Hausdorff bound is not claimed to be the exact Hausdorff distance. The construction is for \(c_0(\mathbb C)\), not an arbitrary complex Banach space. Relevant earlier equivalent formulations of nearly spherical modulus-support-free bodies cannot be completely excluded by a literature search.

## References
- Xin Luo, *A Bounded Closed Convex Set in \(c_0(\mathbb C)\) without Modulus Support Functionals*, arXiv:2610.36771v1 (first posted 2026-10-27), https://arxiv.org/abs/2610.36771.
- L. Golinskii and V. Kadets, *Modulus support functionals, Rajchman measures and peak functions*, arXiv:2008.00845 (2020), https://arxiv.org/abs/2008.00845.
- V. Lomonosov, *A counterexample to the Bishop–Phelps theorem in complex spaces*, Israel Journal of Mathematics 115 (2000), 25–28, https://doi.org/10.1007/BF02810578.
