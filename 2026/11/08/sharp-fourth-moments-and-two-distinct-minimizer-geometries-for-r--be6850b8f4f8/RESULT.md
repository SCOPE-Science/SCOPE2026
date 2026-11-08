# Sharp fourth moments and two distinct minimizer geometries for real matrix coefficients of \(\mathrm{SO}(4)\)

## Finding

Let \(R\) be Haar-uniform in the real special orthogonal group \(\mathrm{SO}(4)\), and let \(A\ne0\) be an arbitrary real \(4\times4\) matrix. Set \(F_A(R)=\operatorname{tr}(A^{\mathsf T}R)\), \(S=\operatorname{tr}(A^{\mathsf T}A)\), \(U=\operatorname{tr}((A^{\mathsf T}A)^2)\), and \(D=\det A\). With Haar probability normalization,

\[
\mathbb E F_A^2=\frac S4,\qquad
\mathbb E F_A^4=\frac{5S^2-2U}{24}+D,
\]

and the complete sharp fourth-moment interval is

\[
\boxed{2\ \le\ \frac{\mathbb E F_A^4}{(\mathbb E F_A^2)^2}\ \le\ 4.}
\]

Both constants are attained. **The lower equality occurs precisely for either a nonzero rank-one \(A\), or a nonzero scalar multiple of a determinant-negative orthogonal matrix**. These are inequivalent matrix orbits, with different ranks. **The upper equality occurs precisely for nonzero scalar multiples of matrices in \(\mathrm{SO}(4)\)** (equivalently, equal singular values and positive determinant).

If \(a_1,\dots,a_4\) are oriented signed singular values, meaning \(A=U\operatorname{diag}(a_1,\dots,a_4)V^{\mathsf T}\) for \(U,V\in\mathrm{SO}(4)\), the lower deficit is the exact three-square identity

\[
\frac{\mathbb E F_A^4}{(\mathbb E F_A^2)^2}-2
=\frac8{3S^2}\left[(a_1a_2+a_3a_4)^2+(a_1a_3+a_2a_4)^2+(a_1a_4+a_2a_3)^2\right].
\]

The upper deficit also splits into two explicit nonnegative spectral terms:

\[
4-\frac{\mathbb E F_A^4}{(\mathbb E F_A^2)^2}
=\frac4{3}\left(\frac U{S^2}-\frac14\right)+16\left(\frac1{16}-\frac D{S^2}\right).
\]

Let \(X=\{F_A:A\in\mathbb R^{4\times4}\}\subset L^4(\mathrm{SO}(4),dR;\mathbb R)\), a sixteen-dimensional real normed space. Its exact Banach--Mazur distance from a real sixteen-dimensional Hilbert space is
\[
\boxed{d_{\mathrm{BM}}(X,\ell_2^{16})=2^{1/4}.}
\]

## Assumptions and scope

All matrices and functions are real. The underlying group is \(\mathrm{SO}(4)\), **not** the disconnected group \(\mathrm O(4)\); orientation is essential. The Haar measure has total mass one. The scalar parameter multiplying an extremizing matrix can be any nonzero real number. The normed space \(X\) is equipped with the fourth-root of the Haar fourth moment, and the Hilbert comparison uses the usual real Banach--Mazur distance defined by optimal linear isomorphism distortion. Oriented signed singular values always exist by signed singular-value decomposition; their absolute values are the usual singular values and their product equals \(D\). All inequalities are asserted for every real nonzero \(4\times4\) matrix, without nonsingularity assumptions.

## Proof

**1. Exact moments from the quaternion double cover.** Identify \(\mathbb R^4\) with the real quaternion algebra. For unit quaternions \(q,p\in\mathbb S^3\), define the proper rotation \(R_{q,p}:x\mapsto qx\bar p\). The map \(\mathbb S^3\times\mathbb S^3\to\mathrm{SO}(4)\) is a surjective homomorphism with finite kernel; independent uniform unit quaternions push forward to Haar probability. For quaternion basis \(e_0=1,e_1=i,e_2=j,e_3=k\), let \(H_{ab}\) be the matrix \(x\mapsto e_a x\bar e_b\), and define
\[
B_{ab}=\operatorname{tr}(A^{\mathsf T}H_{ab}),\qquad 0\le a,b\le3.
\]
Then \(F_A(R_{q,p})=q^{\mathsf T}Bp\). The sixteen signed-permutation matrices \(H_{ab}\) satisfy \(\langle H_{ab},H_{cd}\rangle_{\mathrm F}=4\delta_{ac}\delta_{bd}\), hence \(\operatorname{tr}(B^{\mathsf T}B)=4S\). The sphere moment identities, for independent uniform \(q,p\in\mathbb S^3\), give
\[
\mathbb E(q^{\mathsf T}Bp)^2=\frac{\operatorname{tr}(B^{\mathsf T}B)}{16},\qquad
\mathbb E(q^{\mathsf T}Bp)^4=\frac{\operatorname{tr}(B^{\mathsf T}B)^2+2\operatorname{tr}((B^{\mathsf T}B)^2)}{192}.
\]
These follow by conditioning on \(p\) and applying twice the standard identity \(\mathbb E\,u_i u_j u_k u_l=(\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})/24\) for \(u\) uniform on \(\mathbb S^3\). No asymptotics or unproved integral identities are used.

**2. The exceptional orientation term.** The fourth-degree polynomial \(G(A)=\operatorname{tr}((B^{\mathsf T}B)^2)\) is invariant under \(A\mapsto UAV^{\mathsf T}\) for \(U,V\in\mathrm{SO}(4)\), by Haar invariance and the preceding moment formula. On oriented diagonal singular-value matrices, a homogeneous invariant quartic is a linear combination of \(S^2\), \(U\), and \(D\): signed permutations of determinant one yield symmetry under permutations and even sign changes, whose degree-four monomials are precisely symmetric quadratic polynomials in squared diagonal entries and the full product. Evaluate these three coefficients at \(A=e_0e_0^{\mathsf T}\) (where \(B=I_4\), \(G=4\)), at \(A=I_4\) (where \(B=4e_0e_0^{\mathsf T}\), \(G=256\)), and at \(A=\operatorname{diag}(1,1,1,-1)\) (where \(B=\operatorname{diag}(2,2,2,-2)\), \(G=64\)). Solving the resulting three equations yields exactly
\[
G(A)=12S^2-8U+96D.
\]
Substituting in the conditional fourth moment proves both claimed moment formulas and gives
\[
K(A):=\frac{\mathbb E F_A^4}{(\mathbb E F_A^2)^2}
=\frac{10}{3}-\frac4{3}\frac U{S^2}+16\frac D{S^2}.
\]
As an independent exact check, the accompanying standalone program expands and matches all coefficients of this quartic identity in sixteen independent matrix entries.

**3. Both bounds and all equality cases.** Let \(a_i\) be oriented signed singular values and \(S=\sum_i a_i^2>0\). Since \(S^2-U=2\sum_{i<j}a_i^2a_j^2\) and \(D=\prod_i a_i\), expanding the three indicated squares gives exactly the lower deficit in the Finding. It is nonnegative. Its simultaneous vanishing means \(a_1a_2=-a_3a_4\), \(a_1a_3=-a_2a_4\), \(a_1a_4=-a_2a_3\). If at most one \(a_i\) is nonzero, all three vanish. If exactly two or three are nonzero, one of the three sums is nonzero. If all four are nonzero, multiplying and comparing the equalities forces \(|a_1|=\cdots=|a_4|\) and a negative product; conversely every such oriented singular quadruple makes all three sums zero. This proves the two and only two lower equality families.

For the upper endpoint, \(U\ge S^2/4\) by Cauchy--Schwarz on the four nonnegative squared singular values, with equality exactly when they are all equal. Also \(D\le |D|\le S^2/16\) by arithmetic--geometric mean on the same four numbers, with equality in the last combined inequality exactly when all singular values are equal and \(D>0\). The displayed upper deficit is therefore nonnegative and vanishes exactly for nonzero scalar multiples of proper orthogonal matrices. This proves sharpness and every equality case. For example \(A=e_0e_0^{\mathsf T}\) and \(A=\operatorname{diag}(1,1,1,-1)\) give \(K=2\), whereas \(A=I_4\) gives \(K=4\).

**4. Optimal Euclidean distortion.** By orthogonality of matrix coefficients, the linear correspondence \(A\mapsto F_A\) is injective. The fourth-moment bounds show that the ratio \(\|F_A\|_{L^4}/\|A\|_{\mathrm F}\) has maximum-to-minimum quotient exactly \((4/2)^{1/4}=2^{1/4}\). To see that a different Euclidean structure cannot improve it, let \(E\) be any Euclidean norm on the coefficient matrix space with \(mE(A)\le\|F_A\|_4\le ME(A)\). Apply the same inequalities to every \(UAV^{\mathsf T}\) and average the quadratic form \(E(UAV^{\mathsf T})^2\) over \(U,V\in\mathrm{SO}(4)\). The averaged form must be a scalar multiple of \(\|A\|_{\mathrm F}^2\): invariance under independent proper rotations of rows and columns forces scalarity. Averaging the squared inequalities preserves \(m\) and \(M\), so \(M/m\ge2^{1/4}\). The Frobenius structure attains equality. This establishes the exact Banach--Mazur distance.

## Verification

Run `python3 verify_so4.py` from the directory containing the accompanying file. It uses only the Python standard library and exact integer/rational arithmetic. The program constructs all sixteen quaternion multiplication matrices, checks their complete Gram matrix, expands the quartic identity in independent symbolic matrix entries using sparse integer polynomials, and checks the moment values at both lower geometries, the upper geometry, and two additional matrices via a separate double-sphere integration formula. The key coefficient comparison is exhaustive within a specified polynomial identity (not a finite-sample substitute for a universal inequality); global sharpness and equality classifications are proved above.

## Relationship to prior work

Collins and Śniady's 2004 preprint provides general Haar integration machinery for orthogonal matrix groups. The 2006 preprint of Fujii, Oike and Suzuki analyzes the double cover of \(\mathrm{SO}(4)\) by two copies of \(\mathrm{SU}(2)\). Their underlying techniques are used here, and neither the quaternion cover nor the elementary sphere-moment identities are claimed to be new. The specific orientation-sensitive full-matrix fourth-moment interval, the disjoint rank-one/reflection lower-equality geometries, its exact three-square deficit, and the sixteen-dimensional optimal Euclidean distortion are the combined finding. General group-moment integration formulas alone do not state the global optimizer classification; the derivation and search limitations are documented separately in `REVIEW.md` and `AUDIT.json`.

## Limitations

The claim is for real \(4\times4\) coefficients, Haar probability on \(\mathrm{SO}(4)\), and moment exponent four. It does not assert the same sharp constants for general \(\mathrm{SO}(n)\), \(\mathrm O(4)\), complex coefficient matrices, or other moments. Established general Weingarten formulas may provide an alternative derivation of the moment identity; the classification and norm geometry are the asserted specific contribution. No independent external mathematical audit has been performed.

## References

1. B. Collins and P. Śniady, *Integration with respect to the Haar measure on unitary, orthogonal and symplectic group*, arXiv:math-ph/0402073 (first public version 2004-02-26), https://arxiv.org/abs/math-ph/0402073 . General orthogonal Haar moments.
2. K. Fujii, H. Oike, and T. Suzuki, *More on the Isomorphism \(SU(2)\otimes SU(2)\cong SO(4)\)*, arXiv:quant-ph/0608186 (first public version 2006-08-24), https://arxiv.org/html/quant-ph/0608186v2 . Representation of the four-dimensional rotation group.
