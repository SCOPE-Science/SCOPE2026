# Sharp finite-field two-line Fourier conditioning and a golden-ratio stability gap

## Finding
Let \(q\ge2\) be a prime power, let \(V=\mathbb F_q^2\) with its standard nondegenerate bilinear dot product, and choose any nontrivial additive character \(\psi\) of \(\mathbb F_q\). For two distinct one-dimensional subspaces \(L_1,L_2\le V\), put \(S=L_1\cup L_2\), with the common origin included once. The Fourier sampling operator with the same spatial and frequency mask is
\[
 A_S=\frac1q\bigl(\psi(x\cdot y)\bigr)_{x,y\in S}\in\mathbb C^{(2q-1)\times(2q-1)}.
\]
An invertible operator has Euclidean condition number \(\kappa(A_S)=\sigma_{\max}(A_S)/\sigma_{\min}(A_S)\). The following **complete stability classification of all invertible two-line samplers** holds.

Write \(\varphi=(1+\sqrt5)/2\) and let \(L^\perp\) be the orthogonal complement of a line. An *isotropic line* is one on which every vector has self-dot-product zero. Every invertible \(A_S\) belongs to exactly one of the following three geometries:

1. **Perpendicular lines** \(L_2=L_1^\perp\), necessarily both nonisotropic. The squared singular values are \(1\) twice, \(1/q\) exactly \(2q-4\) times, and \(1/q^2\) once. Thus \(\kappa(A_S)=q\).
2. **Two distinct isotropic lines**, possible only when \(q\) is odd with \(q\equiv1\pmod4\). The squared singular values and condition number are *identical* to the perpendicular case.
3. **Exactly one isotropic line**, with the second nonisotropic. The squared singular values are
\[
 1,\qquad
 \left(\frac{\sqrt{4q+1}+1}{2q}\right)^2,\qquad
 \left(\frac{\sqrt{4q+1}-1}{2q}\right)^2,
 \qquad \frac{\varphi^2}{q}\ \ (q-2\text{ times}),
 \qquad \frac{\varphi^{-2}}{q}\ \ (q-2\text{ times}).
\]
For \(q\ge4\), the condition number is exactly \(\kappa(A_S)=\varphi\sqrt q\). For \(q=2\), the last two groups are absent and \(\kappa(A_S)=2\).

Every other two-line self-sampler is singular. In particular, the **sharp best conditioning among all invertible two-line samplers** is
\[
\boxed{
\min_{L_1\ne L_2,\ A_S\text{ invertible}}\kappa(A_S)
=\begin{cases}
2,&q=2,\\
q,&q\equiv3\pmod4,\\
\varphi\sqrt q,&q\ge4\text{ and }(q\text{ even or }q\equiv1\pmod4).
\end{cases}}
\]
When \(q\equiv3\pmod4\), the minimizing pairs are precisely the \((q+1)/2\) perpendicular pairs. For odd \(q\equiv1\pmod4\), exactly \(2(q-1)\) isotropic–nonisotropic pairs minimize; for even \(q\ge4\), exactly \(q\) such pairs minimize. For \(q=2\), all three line pairs are invertible and tie. Thus the improvement from a perpendicular sampler to a best-conditioned isotropic sampler is the unbounded factor \(\sqrt q/\varphi\) whenever the latter geometry exists.

## Assumptions and scope
The underlying field is any finite field of prime-power order, including characteristic two and extension fields. The Fourier kernel uses a complex additive character (not a finite-field-valued discrete transform); the ambient unitary Fourier operator on \(\mathbb C^{q^2}\) has entries \(q^{-1}\psi(x\cdot y)\). The operator \(A_S\) is its principal compression to the \(2q-1\) spatial/frequency positions in \(S\). Orthogonality and isotropy use the bilinear dot product over \(\mathbb F_q\); singular values, invertibility and conditioning use complex Euclidean linear algebra. Both line generators may be rescaled without changing \(S\). Every pair of distinct lines is included, with no generic-position assumption.

## Proof
**Multiplicative-character decomposition.** Choose nonzero \(v\in L_1\), \(w\in L_2\), and abbreviate \(a=v\cdot v\), \(b=w\cdot w\), \(c=v\cdot w\). Because \(v,w\) form a basis, \(ab-c^2=\det[v\ w]^2\ne0\) in every characteristic. Use the orthonormal basis consisting of the point mass at zero and, for each multiplicative character \(\chi\) of \(\mathbb F_q^*\), the two unit vectors whose respective values at \(tv\) or \(tw\) are \(\chi(t)/\sqrt{q-1}\) for \(t\ne0\).

For every nontrivial \(\chi\), define \(G_\chi=\sum_{t\ne0}\chi(t)\psi(t)\). The Gauss-sum orthogonality identity gives \(|G_\chi|^2=q\). The Fourier map carries the pair of \(\chi\)-input vectors to the pair of \(\chi^{-1}\)-output vectors by \((G_\chi/q)B_\chi\), where
\[
 B_\chi=\begin{pmatrix}j_\chi(a)&j_\chi(c)\\j_\chi(c)&j_\chi(b)\end{pmatrix},\qquad
 j_\chi(u)=\begin{cases}\chi(u)^{-1},&u\ne0,\\0,&u=0.\end{cases}
\]
Hence its two squared singular values are the eigenvalues of \(B_\chi^*B_\chi/q\). Distinct character blocks are orthogonal, even when \(\chi\) and \(\chi^{-1}\) differ.

The trivial-character sector has orthonormal basis \(e_0,e_{1,1},e_{2,1}\) and matrix \(C/q\), with \(h=\sqrt{q-1}\),
\[
 C=\begin{pmatrix}
 1&h&h\\ h&E(a)&E(c)\\h&E(c)&E(b)
 \end{pmatrix},\qquad
 E(u)=\begin{cases}q-1,&u=0,\\-1,&u\ne0.\end{cases}
\]
It is a real symmetric matrix, so its squared singular values are the squares of its real eigenvalues divided by \(q^2\).

**Exhaustive invertibility criterion.** If \(a,b,c\) are all nonzero, the last two rows of \(C\) coincide, so \(A_S\) is singular. If \(c=0\), nondegeneracy forces \(ab\ne0\): these are the perpendicular lines. If \(c\ne0\), the remaining ways to have a zero Gram entry are \(a=0\) or \(b=0\), exactly the isotropic geometries. For each such case, the block calculations below have strictly positive singular values, proving that the list exhausts every invertible pair.

**Perpendicular and doubly isotropic cases.** When \(c=0\), each \(B_\chi\) is diagonal with unit-modulus entries. When \(a=b=0\), each \(B_\chi\) is off-diagonal with unit-modulus entries. Thus every nontrivial character gives two squared singular values \(1/q\). For perpendicular lines, the eigenvalues of \(C\) are \(q,-q,-1\); for two isotropic lines, they are \(q,q,-1\). Their squares yield two eigenvalues \(1\) and one \(1/q^2\) in either case. This proves the first two spectral formulas and condition number \(q\), including \(q=2\) where the nontrivial sectors are empty.

**Exactly one isotropic line.** Without loss of generality \(a=0\), \(b,c\ne0\). For each nontrivial \(\chi\), the matrix \(B_\chi\) has the form \(\bigl(\begin{smallmatrix}0&u\\u&v\end{smallmatrix}\bigr)\), with \(|u|=|v|=1\). Its squared singular values are the roots of \(t^2-3t+1=0\), namely \(\varphi^2\) and \(\varphi^{-2}\), independently of the field, line slopes and additive character. For this geometry,
\[
\det(tI-C)=(t-q)(t^2+t-q).
\]
Its three eigenvalues are \(q,(-1+\sqrt{4q+1})/2,(-1-\sqrt{4q+1})/2\), proving the listed spectrum. For \(q\ge4\), the smallest squared singular value is \(\varphi^{-2}/q\): the lower trivial-sector value obeys
\[
 q\left(\frac{\sqrt{4q+1}-1}{2q}\right)^2
 =\frac{\sqrt{4q+1}-1}{\sqrt{4q+1}+1}
 \ge \frac{3-\sqrt5}{2}=\varphi^{-2}.
\]
The largest squared singular value is \(1\), because \(A_S\) compresses a unitary and the trivial block itself has eigenvalue \(1\). Therefore \(\kappa(A_S)=\varphi\sqrt q\). When \(q=2\), there are no nontrivial multiplicative characters and the three squared singular values are \(1,1,1/4\).

**Sharp optimization and exact numbers of minimizers.** For odd \(q\), isotropic projective lines exist exactly when \(-1\) is a square, that is, when \(q\equiv1\pmod4\); there are precisely two. For even \(q\), \(v\cdot v=(v_1+v_2)^2\), so precisely one line is isotropic. The orthogonal-complement involution fixes exactly the isotropic lines and pairs up all nonisotropic lines. Consequently, if \(q\equiv3\pmod4\), the only invertible pairs are the \((q+1)/2\) perpendicular ones. If odd \(q\equiv1\pmod4\), there are \((q-1)/2\) perpendicular pairs, one pair of distinct isotropic lines, and \(2(q-1)\) pairs containing exactly one isotropic line. If \(q\) is even there are \(q/2\) perpendicular pairs and \(q\) pairs containing the unique isotropic line. Since \(\varphi\sqrt q<q\) for every prime power \(q\ge4\), the asserted optimal configurations and their exact multiplicities follow. The \(q=2\) comparison was computed above. This completes the exhaustive proof.

## Verification
The standalone file `check_two_line_conditioning.py` constructs the full complex Fourier matrices directly, without using the block proof, for *every* unordered pair of projective lines over fields of orders \(2,3,4,5,7,8,9,11,13,16,17\). It compares sorted squared singular values and condition numbers in all invertible cases, verifies the count of optimal geometries, and checks the arithmetic nullity in singular cases. A direct run checked 589 complete matrices; see `check_output.txt`. Run `python check_two_line_conditioning.py` in an environment with Python 3 and NumPy (see `requirements.txt`). These finite computations are corroboration, not a substitute for the all-prime-power proof.

## Relationship to prior work
Lai, Liu and Prince [1] study Fourier frames and exponential bases for unions of two Euclidean linear supports, motivating the need to distinguish the geometry of intersecting components; their objects are continuous additive measures, not principal finite-field Fourier compressions. Iosevich and Mayeli [2] study restriction-based uncertainty principles and sparse recovery on finite abelian groups, including annihilator subspaces, but do not calculate these two-line condition numbers. Biswas et al. [3] study spark of two-dimensional Fourier sampling matrices with line or rectangular *row* patterns rather than the same two-line set on both sides. A published exact two-line **rank and nullity** classification [4] already supplies a multiplicative-character block decomposition; in particular, its kernel and incidence results are acknowledged as prior art. Its explicitly stated limitations exclude singular values, condition numbers and best-conditioned designs. The present theorem identifies the complete singular spectra in all invertible cases, sharp quantitative conditioning in every characteristic, an unbounded stability separation, and counts of *optimizers*; those are not consequences of a rank or nullity statement alone. The prior block matrices make the present diagonalizations short, and thus limit the conceptual novelty; an equivalent spectral treatment outside the checked literature cannot be excluded.

## Limitations
The sharp results concern **only the principal restriction to a union of two *linear* lines through the origin**, with identical spatial and frequency sets and the specified nondegenerate bilinear form. They classify stability only for the invertible cases; no claim is made about noise amplification on the observable subspaces of singular cases, arbitrary affine translates, rectangular masks, three or more lines, or general Fourier frames. Numeric checks cover eleven field orders, not all fields. Historical priority remains provisional and no independent expert validation has been performed.

## References
[1] C.-K. Lai, B. Liu and H. Prince, *Spectral properties of some unions of linear spaces*, arXiv:2005.13802, first submitted 2020-05-28, https://arxiv.org/abs/2005.13802.

[2] A. Iosevich and A. Mayeli, *Uncertainty Principles on Finite Abelian Groups, Restriction Theory, and Applications to Sparse Signal Recovery*, arXiv:2311.04331, first submitted 2023-11-07, https://arxiv.org/abs/2311.04331.

[3] S. Biswas, S. Dasgupta, M. Jacob and R. Mudumbai, *Spark under 2-D Fourier Sampling*, EUSIPCO 2015, https://doi.org/10.1109/EUSIPCO.2015.7362899.

[4] *Arithmetic rank and exact failure distribution for two-line finite Fourier sampling*, published scientific result, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-arithmetic-rank-and-exact-failure-distribution-for-two-line-fini--754730fed24a.
