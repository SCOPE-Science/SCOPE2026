# Sharp tomography spectrum and a twelve-point projective \(2\)-design from tetrahedral rotations

## Finding
Let \(G\) be the order-\(12\) subgroup of \(\mathrm{SO}(3)\) consisting of products \(D_sC^k\), where \(k\in\{0,1,2\}\), \(C(x_1,x_2,x_3)=(x_2,x_3,x_1)\), and \(D_s=\operatorname{diag}(s_1,s_2,s_3)\) with \(s_j\in\{\pm1\}\) and \(s_1s_2s_3=1\). This is the rotational tetrahedral group, isomorphic to \(A_4\). For a unit vector \(v\in\mathbb C^3\), set \(P_g=(gv)(gv)^*\) and define the real self-adjoint frame operator on the nine-dimensional real Hilbert space of Hermitian matrices, with Frobenius inner product, by
\[
\mathcal T_v(X)=\sum_{g\in G}\operatorname{tr}(XP_g)P_g.
\]
Put \(p_j=|v_j|^2\), \(D=\sum_{j=1}^3p_j^2\), and
\[
C_v=(v_1\overline v_2)^2+(v_2\overline v_3)^2+(v_3\overline v_1)^2.
\]
The **complete real spectrum**, with multiplicities, is
\[
\boxed{\ 4^{[1]},\quad (6D-2)^{[2]},\quad \bigl(2(1-D)+4|C_v|\bigr)^{[3]},\quad \bigl(2(1-D)-4|C_v|\bigr)^{[3]}\ }.
\]
Consequently the twelve intensity measurements recover every Hermitian \(3\times3\) matrix if and only if \(D>1/3\) and \(|C_v|<(1-D)/2\). In the unit-vector class the **sharp maximum** of the least squared singular value is \(1\), attained **if and only if** \(D=1/2\) and \(C_v=0\).

One exact maximizer is
\[
v_* = \frac{1}{2\sqrt6}(2,2,-\sqrt7-3i).
\]
Its twelve distinct projective orbit points form an unweighted complex projective \(2\)-design, and for **every** Hermitian \(X\) one has the reconstruction formula
\[
\boxed{\quad X=\sum_{g\in G}\operatorname{tr}(XP_g)P_g-\frac14\Bigl(\sum_{g\in G}\operatorname{tr}(XP_g)\Bigr)I_3.\quad}
\]
All assertions concern this fixed tetrahedral action, equally weighted measurements and the stated unit normalization.

## Assumptions and scope
Vectors are complex; \(G\) acts through the displayed real orthogonal matrices. Projectors are rank-one and have Frobenius norm \(1\). The measurement analysis map takes a Hermitian \(X\) to twelve real intensities \((\operatorname{tr}(XP_g))_{g\in G}\); the frame operator is its adjoint times itself with no additional division by the number of samples. The four signed-diagonal matrices and the three cyclic permutations produce all twelve distinct group elements. Spectral multiplicities are listed even if exceptional parameter choices make distinct levels coincide.

## Proof
**Step 1: block decomposition by sign characters.** Take the real Frobenius-orthonormal Hermitian basis consisting of three diagonal matrix units and, for each cyclic pair \((1,2),(2,3),(3,1)\), its normalized real-symmetric and imaginary-skew-symmetric off-diagonal units. Conjugation by each \(D_s\) fixes the diagonal coordinates; its three nontrivial sign characters act separately on the three off-diagonal pairs. Summing \(\operatorname{tr}(XP_g)P_g\) over the four signs therefore kills all cross-character terms. Cyclic permutations then make the three two-dimensional off-diagonal blocks identical.

**Step 2: diagonal spectrum.** In diagonal coordinates the block is \(4\sum_{k=0}^2(C^kp)(C^kp)^T\), where \(p=(p_1,p_2,p_3)^T\). Since \(\sum p_j=1\), the constant direction has eigenvalue \(4\). The orthogonal two-plane has a double eigenvalue \(6(D-1/3)=6D-2\), from the cyclic-average identity or directly from the block trace.

**Step 3: off-diagonal spectrum.** For each cyclic pair put \(a_j=\sqrt2\operatorname{Re}(v_j\overline v_{j+1})\) and \(b_j=\sqrt2\operatorname{Im}(v_j\overline v_{j+1})\), with subscripts read modulo three. Every two-by-two block is
\[
4\begin{pmatrix}\sum a_j^2&\sum a_jb_j\\\sum a_jb_j&\sum b_j^2\end{pmatrix}.
\]
Its trace is \(4(1-D)\). For the inner matrix before multiplication by four, the complex combination \((\sum_j a_j^2-\sum_j b_j^2)+2i\sum_j a_jb_j=2C_v\). Therefore that inner matrix has eigenvalues \((1-D)/2\pm|C_v|\), and the displayed block has eigenvalues \(2(1-D)\pm4|C_v|\), each repeated three times. This proves the full spectrum without an exhaustive search.

**Step 4: invertibility and sharpness.** The Cauchy–Schwarz inequality gives \(D\ge1/3\) and the Gram structure of Step 3 gives \(|C_v|\le(1-D)/2\). All nontrivial levels are strictly positive precisely under the claimed two strict conditions. Since the scalar eigenvalue is \(4\) and the total trace is \(\sum_g\|P_g\|_F^2=12\), the remaining eight eigenvalues sum to \(8\). Hence the smallest eigenvalue is at most \(1\). Attaining \(1\) forces all eight traceless eigenvalues equal to \(1\), hence \(6D-2=1\), \(2(1-D)\pm4|C_v|=1\), equivalently \(D=1/2\) and \(C_v=0\). Conversely these conditions give spectrum \(\{4,1^{[8]}\}\).

**Step 5: explicit equality and reconstruction.** The displayed \(v_*\) has squared coordinate moduli \((1/6,1/6,2/3)\), so \(D=1/2\). Its three squared cyclic products are
\[
\frac1{36},\qquad\frac{-1-3i\sqrt7}{72},\qquad\frac{-1+3i\sqrt7}{72},
\]
which sum to zero. Thus \(\mathcal T_{v_*}\) is the identity on traceless matrices and multiplies scalars by \(4\), equivalently \(\mathcal T_{v_*}(X)=X+\operatorname{tr}(X)I_3\). The group average \(\sum_gP_g=4I_3\) gives \(\sum_g\operatorname{tr}(XP_g)=4\operatorname{tr}(X)\), yielding the reconstruction formula. Since the projectors span a nine-dimensional space, their orbit cannot have a stabilizer of order \(2\) or \(3\); hence all twelve projectors are distinct. By the standard second-moment identity, \(\frac1{12}\sum_gP_g^{\otimes2}=(I+\mathrm{Swap})/12\), so the orbit is a complex projective \(2\)-design.

## Verification
Run `python verify.py` with Python 3, SymPy and NumPy. The verifier constructs the twelve actual group matrices, checks closure, verifies the explicit \(v_*\) and the identity \(\mathcal T_{v_*}(E_{ij})=E_{ij}+\delta_{ij}I_3\) exactly on all nine complex matrix units using symbolic radicals, and independently compares the full nine eigenvalues against the formula on fifty seeded generic complex vectors. The symbolic check is exact; the randomized spectral comparisons corroborate the formula but do not replace the block proof above.

## Relationship to prior work
The motivating finite-group phase-retrieval literature establishes group-orbit recovery questions and criteria for nilpotent or prime-field affine groups [1,2]. The tetrahedral group is nonnilpotent and, although isomorphic to the affine group of the four-element field, is not a prime-field affine group in the stated theorems of [2]. The general operator-frame and projective-design reconstruction identities are classical [3], so neither the trace bound nor the abstract equivalence to a design is claimed as new. The contribution is the **complete tetrahedral-orbit spectral formula, its exact equality locus, and an explicit optimally conditioned twelve-orbit fiducial**. No inspected result states this specific complete formula or construction.

## Limitations
The least-eigenvalue optimum refers to **linear tomography of arbitrary Hermitian matrices**, a stronger property than phase retrieval of pure states; it does not establish a universal minimal number of pure-state phase-retrieval measurements. The claim does not optimize over arbitrary sets of twelve unit vectors, only over the specified tetrahedral orbits. Under the chosen Frobenius and sample-weight normalization the optimum is exactly one; rescaling measurements changes it. General existence of complex projective designs is previously known, and historical priority for this particular orbit may depend on additional, unindexed group-covariant design literature. No independent audit has been performed.

## References
[1] H. Führ and V. Oussa, *Phase retrieval for nilpotent groups*, arXiv:2201.08654, first public 2022-01-21, https://arxiv.org/abs/2201.08654.

[2] D. Bartusel, H. Führ and V. Oussa, *Phase retrieval for affine groups over prime fields*, arXiv:2109.07123, first public 2021-09-15, https://arxiv.org/abs/2109.07123.

[3] A. J. Scott, *Tight informationally complete quantum measurements*, arXiv:quant-ph/0604049, first public 2006-04-07, https://arxiv.org/abs/quant-ph/0604049.
