# A reversible-switching exceptional point in a four-species quadratic population map

## Finding
Consider two successive generations of Jamilov-type quadratic stochastic inheritance on four species. In odd generations, the first two peripheral types are exchanged probabilistically; in even generations, the last two peripheral types are exchanged probabilistically. Each normalized one-season directional kernel is a symmetric (hence reversible) Markov matrix with real spectrum, but their two-generation product has a unique, genuine defective spectral collision. This is not a claim that either nonlinear quadratic map is invertible. The exact collision is
\[
\alpha_*=2\sqrt3-3,
\qquad \lambda_*=7-4\sqrt3\in(0,1).
\]
For \(0<\alpha<\alpha_*\) the two nonstationary two-generation multipliers are a nonreal conjugate pair, both with modulus \(1-2\alpha\); for \(\alpha_*<\alpha<1\) the two multipliers are real, distinct, nonnegative, and strictly less than one. At \(\alpha=\alpha_*\) the return map has a size-two Jordan block. In particular its generic convergence has a sharp polynomial prefactor multiplying exponential relaxation, not merely a sum of ordinary exponentials.

For an initial state with \(0<x_{4,0}<1\), set \(p_{j,t}=x_{j,t}/(1-x_{4,t})\), \(j=1,2,3\), and \(u=(1/3,1/3,1/3)^{\mathsf T}\). Define the matrix
\[
M_*=\begin{pmatrix}
\alpha_*&1-\alpha_*&0\\
\alpha_*(1-\alpha_*)&\alpha_*^2&1-\alpha_*\\
(1-\alpha_*)^2&\alpha_*(1-\alpha_*)&\alpha_*
\end{pmatrix},
\qquad z=p_0-u,
\qquad N=(M_*-\lambda_* I)|_{\{v:\sum_jv_j=0\}}.
\]
Then \(N\ne0\), \(N^2=0\), and for **every integer \(n\ge1\)**,
\[
\boxed{p_{2n}-u=\lambda_*^n z+n\lambda_*^{n-1}Nz.}
\]
Consequently, when \(Nz\ne0\),
\[
\lim_{n\to\infty}\frac{\|p_{2n}-u\|}{n\lambda_*^{n-1}}=\|Nz\|>0
\]
for any fixed norm on the sum-zero plane. The exceptional condition \(Nz=0\) is a proper line within that plane. Independently, the fourth-species coordinate obeys
\[
\boxed{x_{4,t}=\frac{1+(2x_{4,0}-1)^{2^t}}{2},\qquad t\ge0.}
\]
Thus the full state approaches \((1/6,1/6,1/6,1/2)\), with doubly exponential relaxation of the distinguished species and the exact two-generation spectral transition in the remaining normalized frequencies.

## Assumptions and scope
Let \(\Delta_3=\{x\in[0,1]^4:\sum_{i=1}^4x_i=1\}\), and fix \(0<\alpha<1\). For a transposition \(\pi\) of \(\{1,2,3\}\), define the quadratic stochastic map
\[
(V_{\alpha,\pi}(x))_j=2x_4\left(\alpha x_j+(1-\alpha)x_{\pi(j)}\right),\quad j=1,2,3,
\quad (V_{\alpha,\pi}(x))_4=x_4^2+(x_1+x_2+x_3)^2.
\]
Starting from \(x_0\), apply \(V_{\alpha,(12)}\), then \(V_{\alpha,(23)}\), then repeat the same two-step schedule indefinitely. The theorem concerns the interior transversal regime \(0<x_{4,0}<1\); it allows zero initial peripheral coordinates. No assertion of spectral irreversibility is made for either individual one-step map, and the result does not classify other switching schedules, dimensions, or stochastic perturbations.

## Proof
**1. Invariant scalar and normalized shape.** Put \(s_t=x_{4,t}\) and \(r_t=1-s_t\). Summing the first three components gives \(r_{t+1}=2s_tr_t\), while \(s_{t+1}=s_t^2+r_t^2\). Therefore \(b_t=2s_t-1\) satisfies \(b_{t+1}=b_t^2\), proving the exact scalar formula. For \(0<s_0<1\), every \(r_t>0\), so normalized directions are defined at every generation, and division by \(r_{t+1}\) gives
\[
p_{t+1}=\bigl[\alpha I+(1-\alpha)P_{\pi_t}\bigr]p_t,
\]
where \(P_{\pi_t}\) is the coordinate-permutation matrix. This exact decoupling works for arbitrary initial peripheral frequencies, without a linearization approximation.

**2. Two-step spectrum.** The first-season and second-season matrices are
\[
P_1=\begin{pmatrix}\alpha&1-\alpha&0\\1-\alpha&\alpha&0\\0&0&1\end{pmatrix},\quad
P_2=\begin{pmatrix}1&0&0\\0&\alpha&1-\alpha\\0&1-\alpha&\alpha\end{pmatrix}.
\]
Both are real symmetric and doubly stochastic. The return matrix is their noncommuting product
\[
M_\alpha=P_2P_1=
\begin{pmatrix}\alpha&1-\alpha&0\\\alpha(1-\alpha)&\alpha^2&1-\alpha\\(1-\alpha)^2&\alpha(1-\alpha)&\alpha\end{pmatrix}.
\]
Direct expansion gives the characteristic polynomial
\[
\det(\lambda I-M_\alpha)
=(\lambda-1)\bigl[\lambda^2-(\alpha^2+2\alpha-1)\lambda+(2\alpha-1)^2\bigr].
\]
The discriminant of the quadratic factor is
\[
\Delta(\alpha)=(1-\alpha)^2(\alpha^2+6\alpha-3).
\]
Its unique zero in the open interval \((0,1)\) is \(\alpha_*=2\sqrt3-3\). At that point the nonstationary double root is \(\lambda_*=(\alpha_*^2+2\alpha_*-1)/2=7-4\sqrt3\). For smaller \(\alpha\), the roots are conjugate and have common modulus \(\sqrt{\det(M_\alpha|_H)}=1-2\alpha\), where \(H=\{v:\sum_jv_j=0\}\). For larger \(\alpha\) the roots are distinct and real. Their sum is positive and their product is nonnegative in this range, hence both are nonnegative. They are strictly below one because \(M_\alpha^2\) has strictly positive entries: \(M_\alpha\) itself is nonnegative with all positive entries except its \((1,3)\) entry, and that missing entry becomes positive in its square. Perron–Frobenius therefore gives strict contraction on \(H\).

**3. Defective collision and exact powers.** The sum-zero plane is invariant under \(M_*\). Its characteristic polynomial is \((\lambda-\lambda_*)^2\), so Cayley–Hamilton on this two-dimensional space gives \(N^2=0\). The collision is not scalar: with \(e_1=(1,0,0)^{\mathsf T}\),
\[
\bigl(N(e_1-u)\bigr)_1=-8+\frac{14\sqrt3}{3}\ne0.
\]
Thus \(N\ne0\), its kernel is one-dimensional in \(H\), and the restricted matrix has exactly one size-two Jordan block. Binomial expansion of \(M_*|_H=\lambda_*I+N\) yields
\[
M_*^nz=\lambda_*^nz+n\lambda_*^{n-1}Nz
\]
exactly for all \(n\ge1\). The second term dominates whenever \(Nz\ne0\); the stated norm limit follows by homogeneity and continuity of the norm.

**4. Full-population limit.** Since \(|2s_0-1|<1\), the exact scalar formula implies \(s_t\to1/2\) at doubly exponential speed. The return matrix is primitive for \(0<\alpha<1\), so \(p_{2n}\to u\); also \(p_{2n+1}=P_1p_{2n}\to u\). Therefore each peripheral raw coordinate tends to \((1/2)(1/3)=1/6\), completing the claim.

## Verification
The companion `checker.py` verifies symbolically the characteristic polynomial, discriminant factorization, exact Jordan nilpotence on two spanning sum-zero vectors, the nonzero Jordan coefficient, and the power identity at eight positive integers. It additionally runs 220 rational four-species two-season trajectories, verifying the normalized matrix recurrence and the exact scalar formula without floating-point arithmetic. Reproduce by running `python3 checker.py` with SymPy installed. These finite checks corroborate, but do not replace, the general proof above.

## Relationship to prior work
Jamilov, *A family of non-Volterra quadratic operators corresponding to permutations*, arXiv:2210.05107, Eq. (4) and Theorem 3.5, establishes the one-permutation family and its autonomous long-term behavior; the definition and qualitative autonomous results are prior work. The present claim changes the permutation each season, so the two reversible one-step directional kernels do not commute and their product acquires a new parameter-sharp defective transition.

Aralova and Jamilov, *The dynamics of superposition of non-Volterra quadratic stochastic operators*, DOI:10.1080/10236198.2022.2126316, treats a distinct superposition family on the two-dimensional simplex. Jamilov and Mukhitdinov, *Dynamics of a Convex Combination and Superposition of Non-Volterra Quadratic Stochastic Operators*, DOI:10.68381/jca32052, gives full formulas for another two-dimensional-simplex pair. Neither specifies the minimal four-species, three-peripheral-coordinate alternating transpositions or the spectral discriminant above. General Markov-chain spectral theory already permits complex eigenvalues and defective eigenmodes in nonreversible chains; no novelty is claimed for that general phenomenon.

## Limitations
The result applies to deterministic period-two switching with equal mixing parameter in the two seasons and \(0<\alpha<1\), not to arbitrary seasonal coefficients. The polynomial prefactor is generic, not universal over initial frequencies: exactly the proper eigendirection \(Nz=0\) lacks it. The extreme initial strata \(x_{4,0}=0\) or \(1\) are excluded from normalized coordinates. The formula does not claim a sharp global mixing-time bound outside the stated regime. Priority against unpublished or inaccessible papers cannot be guaranteed; a separate independent mathematical audit has not been performed.

## References
1. U. U. Jamilov, *A family of non-Volterra quadratic operators corresponding to permutations*, Communications in Mathematics 31 (2023), 31–41; first available October 11, 2022 as arXiv:2210.05107; https://arxiv.org/pdf/2210.05107.
2. K. A. Aralova and U. U. Jamilov, *The dynamics of superposition of non-Volterra quadratic stochastic operators*, Journal of Difference Equations and Applications 28 (2022), 1178–1192; https://doi.org/10.1080/10236198.2022.2126316.
3. U. U. Jamilov and R. T. Mukhitdinov, *Dynamics of a Convex Combination and Superposition of Non-Volterra Quadratic Stochastic Operators*, Journal of Convex Analysis 32 (2025), 975–988; https://journalofconvexanalysis.com/articles/jca32052/jca32052.pdf.
4. E. Seabrook and L. Wiskott, *A Tutorial on the Spectral Theory of Markov Chains*, arXiv:2207.02296, particularly Section 4.3 on nonreversible transition matrices; https://arxiv.org/pdf/2207.02296.
