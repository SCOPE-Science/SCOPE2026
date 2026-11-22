# Exact quadratic-harmonic sampling spectra on the centered Birkhoff vertex orbit

## Finding
Let \(n\ge4\). The normalized centered permutation-matrix orbit of the \(n\)-th Birkhoff polytope on the sphere of \((n-1)\)-by-\((n-1)\) doubly centered matrices has an exact three-Specht-sector quadratic-harmonic sampling spectrum. Define
\[
 d_1=n-1,\qquad d_2=\frac{n(n-3)}2,\qquad d_3=\frac{(n-1)(n-2)}2,\qquad m=(n-1)^2,
\]
\[
 h_2=\frac{(m-1)(m+2)}2,\qquad N=n!.
\]
For the normalized evaluation map \(E:\mathcal H_2(S^{m-1})\to\mathbb C^{N}\) specified below, the complete **nonzero squared singular spectrum** is
\[
 \boxed{\quad s_j^2=\frac{h_2}{n(n-2)d_j}\quad\text{with multiplicity }d_j^2,\quad j=1,2,3.\quad}
\]
Equal values are combined (the first and third coincide at \(n=4\)); all remaining singular values are zero. In particular,
\[
 \boxed{\operatorname{rank}E=\sum_{j=1}^3d_j^2,\qquad
 \dim\ker E=n(n-1)(n-2)-2.}
\]
The nonzero squared-singular-value condition number is exactly
\[
 \boxed{\kappa_{\mathrm{pos}}(n)=
 \begin{cases}3/2,&n=4,\\(n-2)/2,&n\ge5.\end{cases}}
\]
Although these vertices form a spherical \(2\)-design, they are not a spherical \(4\)-design: a nonzero degree-two harmonic is invisible to all vertices for **every** \(n\ge4\). The nullspace dimension grows cubically, while the fraction of the quadratic-harmonic space that is visible tends to one.

## Assumptions and scope
Write \(\mathbf1\in\mathbb R^n\) for the all-ones vector, \(J=\mathbf1\mathbf1^T\), and
\[
 V_n=\{M\in\mathbb R^{n\times n}:M\mathbf1=M^T\mathbf1=0\},\qquad \dim V_n=(n-1)^2=m.
\]
Equip \(V_n\) with the Frobenius inner product. For each permutation \(\pi\in S_n\), let \(P_\pi\) be its permutation matrix, and define
\[
 x_\pi=\frac{P_\pi-J/n}{\sqrt{n-1}}\in S(V_n).
\]
Let \(\mathcal H_2(S(V_n))\) denote restrictions of complex-valued homogeneous real-harmonic polynomials of degree two on \(V_n\), equipped with the \(L^2\) norm for normalized rotationally invariant spherical measure. Set
\[
 (EF)(\pi)=\frac{F(x_\pi)}{\sqrt{n!}},\qquad
 \|EF\|^2=\frac1{n!}\sum_{\pi\in S_n}|F(x_\pi)|^2.
\]
The spectrum above refers to \(E^*E\), including its kernel. The concentration condition number is taken only over positive eigenvalues, not over the whole space, where sampling is singular. No claim of reconstructing arbitrary data on all \(n!\) points is made.

## Proof
**1. Normalized zonal Gram matrix.** Each centered permutation matrix has squared Frobenius norm \(n-1\). If \(f(\tau)\) is the number of fixed points of \(\tau\in S_n\), then
\[
 \langle x_\pi,x_\sigma\rangle=\frac{f(\pi^{-1}\sigma)-1}{n-1}.
\]
The normalized degree-two spherical zonal polynomial in ambient dimension \(m\) is
\[
 Z_2(t)=\frac{mt^2-1}{m-1}.
\]
Indeed, this is the reproducing-kernel scalar for trace-free symmetric tensors, normalized by \(Z_2(1)=1\). Thus the \(N\)-by-\(N\) normalized Gram matrix \(G=(Z_2(\langle x_\pi,x_\sigma\rangle))\) is precisely
\[
 \boxed{G_{\pi\sigma}=\frac{f(\pi^{-1}\sigma)(f(\pi^{-1}\sigma)-2)}{n(n-2)}.}
\]
The actual evaluation Gram is \(EE^*=(h_2/N)G\), as the degree-two reproducing kernel is \(h_2Z_2\).

**2. Exhaustive character identity.** Let \(t(\tau)\) be the number of two-cycles. Denote by \(\chi_1,\chi_2,\chi_3\) the irreducible symmetric-group characters of partitions \((n-1,1)\), \((n-2,2)\), \((n-2,1,1)\) respectively. Their degrees are \(d_1,d_2,d_3\), and their character polynomials are
\[
 \chi_1=f-1,\quad
 \chi_2=\binom f2+t-f,\quad
 \chi_3=\binom f2-f+1-t.
\]
The first identity is the augmentation module of the point-permutation representation. The second follows by subtracting the point-permutation representation from the permutation representation on unordered pairs; the latter has three orbitals, so its complementary constituent is irreducible for \(n\ge4\). The third follows from the exterior square of the augmentation representation: \(\chi_{\wedge^2\mathrm{Std}}(\tau)=((f-1)^2-(f+2t-1))/2\). Consequently
\[
 \boxed{f(f-2)=\chi_1+\chi_2+\chi_3.}
\]
These are exactly three pairwise inequivalent irreducibles, including at the boundary \(n=4\).

**3. Complete spectral decomposition.** On the regular representation \(\mathbb C[S_n]\), convolution by the central character \(\chi_j\), normalized by \(1/N\), is \(1/d_j\) times the central orthogonal projection onto its isotypic component. This follows from finite-group character orthogonality, and that isotypic component has dimension \(d_j^2\). Thus \(G\) acts by \(N/[n(n-2)d_j]\) on the three respective components, and vanishes on all others. Multiplication by \(h_2/N\) yields the asserted \(E^*E\) nonzero spectrum and multiplicities, since \(EE^*\) and \(E^*E\) have identical positive spectra. Summing the three squared degrees and subtracting from \(h_2\) simplifies to
\[
 \dim\ker E=h_2-(d_1^2+d_2^2+d_3^2)=n(n-1)(n-2)-2>0.
\]
For \(n=4\), \(d_2=2\) and \(d_1=d_3=3\); for \(n\ge5\), \(d_1<d_2<d_3\). The positive condition number is therefore the claimed piecewise expression. The rank fraction tends to one because the kernel grows as \(n^3\) but \(h_2\) as \(n^4/2\).

**4. Design contrast.** The left-right \(S_n\times S_n\)-action on \(V_n\) is the external tensor product of two real augmentation representations and is irreducible. The orbit mean is zero; invariance and irreducibility force its covariance to be \(m^{-1}I\). These are the defining first- and second-moment identities of a spherical \(2\)-design. If the orbit were a spherical \(4\)-design, degree-four polynomial exactness applied to \(|F|^2\) for every \(F\in\mathcal H_2\) would give \(\|EF\|^2=\|F\|^2\). The strictly positive kernel dimension contradicts this, hence it is never a spherical \(4\)-design.

## Verification
Two standalone programs accompany this result. `verify_characters.py` checks every integer character identity and all pairwise character orthogonality sums by exhaustive permutation enumeration for \(4\le n\le8\), together with exact dimension, rank and nullity arithmetic. `verify_birkhoff.py` independently constructs the complete normalized zonal Gram matrices on the permutations for \(n=4,5,6\) and checks their full numerical spectra; maximum absolute discrepancies are approximately \(1.2\times10^{-15}\), \(2.7\times10^{-15}\), and \(1.1\times10^{-14}\), respectively. Both checks passed. The infinite family is proved by the preceding representation-theoretic identities, not by the finite checks.

## Relationship to prior work
Xiao and Zhuang (2023), *Spherical Framelets from Spherical Designs*, give the motivating spherical-design sampling and framelet framework. Their treatment of general evaluation and spherical sampling is not this permutation-matrix orbit calculation. Mohammadpour and Waldron (2023), *Complex Spherical Designs from Group Orbits*, develop the general harmonic-Molien group-orbit framework and investigate design conditions, but not the evaluated three-Specht quadratic sampling spectrum here. The character identities, normalized Gegenbauer kernel, and finite-group central projection are classical and **not** claimed as new. Published exact endpoint norms for the quadratic Specht Fourier block on the symmetric group evaluate a different \(\ell^\infty\) character projection norm, not the degree-two spherical sampling Gram operator on Birkhoff vertices. The present claim is the explicit complete Birkhoff-vertex spectrum, its harmonic nullity and sharp positive stability ratio, not a new character decomposition theorem.

## Limitations
This is a degree-two theorem for real-sphere harmonics and uniform equal-weight sampling, not an all-degree statement and not an assertion of historical priority beyond the searched literature. The sampling map has a substantial kernel, so the positive condition number applies to the observable subspace only. The basic character identities are already standard; an unindexed equivalent Birkhoff-orbit specialization might exist.

## References
1. Y. Xiao and X. Zhuang, *Spherical Framelets from Spherical Designs*, arXiv:2303.05365, initially posted March 9, 2023; SIAM Journal on Imaging Sciences 16 (2023), 2072–2104, DOI:10.1137/22M1542362.
2. M. Mohammadpour and S. Waldron, *Complex Spherical Designs from Group Orbits*, arXiv:2308.02499, initially posted July 21, 2023. Relevant: group-orbit design criterion and harmonic Molien series in Sections 2–3.
3. Classical spherical addition theorem and normalized second-degree Gegenbauer polynomial for trace-free symmetric tensors.
4. Classical character polynomials and orthogonality of the three Specht representations indexed by \((n-1,1)\), \((n-2,2)\), \((n-2,1,1)\).
