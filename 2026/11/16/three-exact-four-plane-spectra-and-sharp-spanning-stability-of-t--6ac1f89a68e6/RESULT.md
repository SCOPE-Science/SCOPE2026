# Three exact four-plane spectra and sharp spanning stability of the real eleven-plane harmonic fusion frame

## Finding

Consider the real equi-isoclinic tight fusion frame of eleven three-dimensional subspaces of \(\mathbb R^{11}\) constructed in Theorem 4.3 of Fickus–Iverson–Jasper–Mixon [1], with the explicit multiplicative character specified below. Let \(P_m\) denote the orthogonal projection onto the subspace indexed by \(m\in\mathbb F_{11}\). For every four-element set \(S\subset\mathbb F_{11}\), write

\[
A_S=\sum_{m\in S}P_m,\qquad q_S(t)=\det(tI_{11}-A_S).
\]

**Theorem.** The \(330=\binom{11}{4}\) polynomials \(q_S\) comprise exactly **three** distinct monic degree-eleven polynomials, of respective multiplicities **165**, **110**, and **55**. Their coefficients are specified exactly, without approximations, in the accompanying `spectra.json` as

\[
q_C(t)=\sum_{j=0}^{11}(a_{C,j}+b_{C,j}\tau)t^{11-j},
\quad \tau=\zeta_5^2+\zeta_5^3=-\frac{1+\sqrt5}{2},
\]

where \(C\in\{A,B,C\}\) and \(\zeta_5=e^{2\pi i/5}\). In this ordering, the classes have multiplicities 165, 110, 55. All eleven eigenvalues of \(A_S\) are strictly positive, so **every four planes span \(\mathbb R^{11}\)**. The sharp worst-case lower fusion-frame bound is the smallest positive root of \(q_A\), and is attained for exactly 165 subsets. Rigorous rational isolations of the smallest eigenvalue in each class are:

| Class | Count | Strict interval for least eigenvalue |
| --- | ---: | --- |
| \(A\) | 165 | \((389/10000,391/10000)\) |
| \(B\) | 110 | \((849/10000,850/10000)\) |
| \(C\) | 55 | \((1859/10000,1861/10000)\) |

The six square-affine orbits of four-subsets all have size 55, with representatives \(\{0,1,2,3\}\), \(\{0,1,2,4\}\), \(\{0,1,2,5\}\), \(\{0,1,2,6\}\), \(\{0,1,2,8\}\), \(\{0,1,3,4\}\), assigned respectively to classes \(B,A,A,C,B,A\).

## Assumptions and scope

Use \(\mathbb F_{11}=\mathbb Z/11\mathbb Z\), the primitive element \(2\in\mathbb F_{11}^{\times}\), and the multiplicative character determined by \(\chi(2)=e^{2\pi i/10}\). Let \(\zeta=e^{2\pi i/11}\), \(G_k=\sum_{x=1}^{10}\zeta^{-x}\chi(x)^k\), \(\omega=G_6/G_1\), \(c=\cos(2\pi/5)\), and \(s=\sin(2\pi/5)\). Write \(\ell(x)\) for the Legendre symbol modulo eleven. Define the eleven unit vectors \(\psi_x\in\mathbb C^3\) by

\[
\psi_0=(1,0,0)^T,\qquad
\psi_x=\sqrt{\frac{11}{30}}\begin{pmatrix}
\sqrt{8/11}\\
\chi(x)[c\ell(x)+is\omega]\\
\overline{\chi(x)}[c\ell(x)+is\overline\omega]
\end{pmatrix}\quad (x\ne0).
\]

Let \(\Phi_m\) be the eleven-by-three isometry with entries \(\Phi_m(x,r)=\sqrt{3/11}\,\zeta^{mx}\overline{\psi_x(r)}\), and \(P_m=\Phi_m\Phi_m^*\). These complex matrices realize the real fusion-frame subspaces of [1] up to a fixed basis transformation. The claim concerns this explicit code, its four-plane sums, and the full multisets of their nonzero singular-value squares; it does not concern arbitrary EITFFs with the same parameters.

## Proof

First, [1, Theorem 4.3 and the harmonic matrix-ensemble formula in its Section 3] establish that each \(\Phi_m\) is an isometry and that the corresponding fusion frame admits a real realization. The Gram matrix of the twelve chosen columns \(\bigl[\Phi_m\bigr]_{m\in S}\) is positive semidefinite, with characteristic polynomial \(t\,q_S(t)\); its eleven nonzero eigenvalues, when the rank is eleven, equal the eigenvalues of \(A_S\).

For a square \(a\in\{1,3,4,5,9\}\subset\mathbb F_{11}^{\times}\) and any \(b\in\mathbb F_{11}\), the replacement \(S\mapsto aS+b\) leaves the spectrum invariant. Indeed, \(\ell(a^{-1}x)=\ell(x)\) and \(\chi(a^{-1}x)=\chi(a^{-1})\chi(x)\). Row permutation by \(x\mapsto a^{-1}x\), modulation by \(\zeta^{ba^{-1}x}\), and a common diagonal unitary change of the three coefficient coordinates implement the same change simultaneously for all \(m\). An elementary exact finite-orbit enumeration gives precisely the six 55-element orbits listed in the theorem; they partition all 330 subsets.

To compute their spectra without any floating point, work in the cyclotomic field \(K=\mathbb Q(\zeta_{55})\). Set \(w_0=4/15\), \(w_1=w_2=11/30\) and, for \(x\ne0\), let

\[
v_x=(1,\chi(x)(c\ell(x)+is\omega),\overline{\chi(x)}(c\ell(x)+is\overline\omega))^T.
\]

Define \(B_0=\operatorname{diag}(1,0,0)\) and \(B_x(r,s)=v_x(r)\overline{v_x(s)}w_s\) for nonzero \(x\). This is the simultaneous diagonal similarity of the rank-one projectors \(\psi_x\psi_x^*\) by \(\operatorname{diag}(\sqrt{w_0},\sqrt{w_1},\sqrt{w_2})\). Consequently the twelve-by-twelve block Gram matrix for \(S=\{m_1,\ldots,m_4\}\) is similar to the block matrix with \((i,j)\)-block

\[
M_{m_j-m_i}=\frac3{11}\sum_{x=0}^{10}\zeta^{(m_j-m_i)x}B_x.
\]

The attached `certificate.py` constructs all these matrices over \(K\) and computes their characteristic coefficients with the Faddeev–LeVerrier recurrence. For all six representatives, each of the twelve coefficients is verified exactly equal to the claimed \(tq_C(t)\), including a single zero constant coefficient. Its degree-one coefficient is nonzero for all three classes, proving rank eleven. It also proves that the three coefficient vectors are distinct and that exactly the asserted orbits merge into each class.

Finally, the Sturm root counts of the three exact polynomials in the real quadratic subfield \(\mathbb Q(\sqrt5)\) are zero on \((0,L_C]\) and one on \((0,U_C]\), where \((L_C,U_C)\) are the rational isolating intervals in the table. Because \(A_S\) is positive semidefinite and has full rank, these are strictly positive smallest eigenvalues, and the three nonoverlapping intervals show that class \(A\) uniquely realizes the worst bound. All computations are exact field or rational-algebraic operations; numerical eigenvalues are not used as proof.

## Verification

With Python 3 and SymPy installed, run `python certificate.py --all` and `python certificate.py --roots` from the directory containing the two standalone artifacts. The first command checks the orbit partition and the six exact cyclotomic characteristic polynomials against `spectra.json`. The second checks nonzero constant coefficients and exact Sturm root isolations. The recurrence uses the actual input field \(\mathbb Q(\zeta_{55})\), not numeric approximations. The algebraic computations have been replayed from the packaged artifact paths. The tables include coefficients of every degree, so they are independently reconstructible without the proof code.

## Relationship to prior work

Fickus–Iverson–Jasper–Mixon [1] construct the real \(\operatorname{EITFF}(11,11,3)\) and establish its equi-isoclinicity, but their inspected construction and appendix do not furnish the complete four-subspace spectrum, its orbit multiplicities, or sharp four-plane spanning bound. Their subsequent treatment of symmetric Grassmannian codes [2] discusses block restricted isometry as a question but studies different constructions. Relevant published Paley-plane and nine-plane fusion-frame rank results [3,4] have different ambient dimensions and rank-three versus rank-two blocks, and neither statement implies this exact eleven-plane three-dimensional case. An absence of matched indexed results is not a general proof of novelty.

## Limitations

This is one specific explicit eleven-plane family. It does not assert the same profile for other character generators, general real equi-isoclinic frames, arbitrary subsets of other cardinalities, or optimal noisy reconstruction with a nonuniform measurement model. The result is a finite exact classification, not an all-dimension statement. Historical priority relative to inaccessible specialized literature remains subject to independent confirmation. Independent mathematical audit has not been performed.

## References

1. M. Fickus, J. W. Iverson, J. Jasper, and D. G. Mixon, *Harmonic Grassmannian codes*, arXiv:2112.14267v1 (first public 2021-12-28), Section 3, Theorem 4.3, Appendix A. https://arxiv.org/html/2112.14267v1
2. M. Fickus, J. W. Iverson, J. Jasper, and D. G. Mixon, *Equi-isoclinic subspaces from symmetry*, arXiv:2406.19542v1 (first public 2024-06-27), introduction's block-restricted-isometry discussion. https://arxiv.org/abs/2406.19542
3. *Three-block rigidity and the four-block spectral profile of real Paley harmonic fusion planes*, published published-finding corpus finding, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-three-block-rigidity-and-the-four-block-spectral-profile-of-real--e1ffd8f9e8e9
4. *The square-orbit block-rank dichotomy for order-nine harmonic fusion frames*, published published-finding corpus finding, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-square-orbit-block-rank-dichotomy-for-order-nine-harmonic-fu--601f40ffaaeb
