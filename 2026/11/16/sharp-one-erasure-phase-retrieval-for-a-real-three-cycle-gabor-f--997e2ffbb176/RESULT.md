# Sharp one-erasure phase retrieval for a real three-cycle Gabor family

## Finding

For each real parameter \(s\), define \(g_s=(1,1,s)\in\mathbb R^3\) and the nine time-frequency shifts on \(\mathbb Z_3\)
\[
 (M_mT_kg_s)(j)=e^{2\pi i mj/3}g_s(j-k),\qquad k,m,j\in\mathbb Z_3.
\]
Given any one phase-space point \((k_0,m_0)\), the eight intensities
\[
 \bigl\{|\langle x,M_mT_kg_s\rangle|^2:(k,m)\in\mathbb Z_3^2\setminus\{(k_0,m_0)\}\bigr\}
\]
determine **every** \(x\in\mathbb C^3\) uniquely up to a global unit-modulus factor if and only if
\[
 s\notin\{1,-1,-\tfrac12\}.
\]
At each of the three exceptional real parameters, not even all nine intensities phase-retrieve every complex signal. The number eight is optimal among **all** phaseless linear measurement systems on \(\mathbb C^3\): no seven intensity measurements can globally phase-retrieve every vector. The statement is uniform over which of the nine samples is erased, and includes the two-tap window \(g_0=(1,1,0)\).

## Assumptions and scope

The signal and measurement spaces are complex. The parameter \(s\) is real (not a generic complex perturbation). Inner products are the standard Hermitian products and measured squared moduli are not normalized; multiplying the window by a nonzero scalar does not alter injectivity. Time and frequency indices are modulo three. Phase equivalence means \(x\sim e^{i\phi}x\), with zero a singleton class. The result asserts exact noiseless injectivity, not a quantitative noise-stability constant.

## Proof

Let \(\mathcal H_3\) be the nine-dimensional **real** vector space of Hermitian \(3\times3\) matrices. For a selected measurement set \(\Lambda\), let
\[
 \mathcal L_{s,\Lambda}(H)=\bigl(\langle M_mT_kg_s,H M_mT_kg_s\rangle\bigr)_{(k,m)\in\Lambda}.
\]
The familiar rank-two kernel criterion says that the intensity map is injective modulo phase precisely when \(\ker\mathcal L_{s,\Lambda}\) has no nonzero Hermitian matrix of rank at most two. Indeed, two identical intensity sets give a kernel element \(xx^*-yy^*\); conversely, any nonzero indefinite Hermitian rank-two element has such a decomposition, while a semidefinite kernel element forces all measurement vectors into its nullspace and hence failure of spanning.

Use the Hermitian real basis consisting, in order, of the three coordinate diagonal matrices, the three symmetric matrices with off-diagonal pairs \((01),(02),(12)\), and their imaginary skew counterparts with upper entries \(i\sqrt3\). Write \(A_s\) for the nine-by-nine real matrix of \(\mathcal L_{s,\mathbb Z_3^2}\), with rows ordered \((0,0),(0,1),(0,2),(1,0),\ldots,(2,2)\). All entries of \(A_s\) are polynomials in \(s\) with integer coefficients. Direct expansion yields the exact factorization
\[
 \det A_s=-5832(s-1)^6(s+1)^2(2s+1)^2(s^2+2).
\]
Consequently \(A_s\) is invertible exactly outside the stated exceptional set. At \(s=1,-1,-\tfrac12\), its respective real ranks are \(3,7,7\). The kernel then has dimension at least two, which cannot be phase-retrievable: on the unit circle in any two-dimensional real kernel subspace the determinant is a continuous odd function and therefore vanishes at a nonzero singular Hermitian matrix. If the measurements span \(\mathbb C^3\), that singular matrix is necessarily indefinite of rank two; if they do not span, phase retrieval already fails.

For \(s\) outside the exceptional set, delete the row \((0,0)\). The resulting eight-row matrix has rank eight. Its one-dimensional Hermitian kernel is spanned by the following explicit real symmetric matrix, where \(a=(s+1)(s^2+2)\):
\[
 H_s=\begin{pmatrix}
 -(2s+1)&-(s+1)a&sa\\
 -(s+1)a&-(2s+1)&sa\\
 sa&sa&(2s+1)(s^2+1)
 \end{pmatrix}.
\]
The determinant is exactly
\[
 \det H_s=-(s^2+s+1)^4\bigl(2s^4+2s^3+5s^2+6s+3\bigr).
\]
Its quartic factor is strictly positive for all real \(s\), because
\[
 2s^4+2s^3+5s^2+6s+3
 =2(s^2+s/2)^2+\tfrac92(s+2/3)^2+1>0.
\]
Also \(s^2+s+1>0\), so \(H_s\) has rank three; thus this eight-row family is phase retrievable. Conjugation by any Weyl time-frequency shift permutes the nine rank-one projectors, mapping the missing point \((0,0)\) to any other point. Rank and singularity of the Hermitian kernel are preserved, proving the same assertion for all nine erasures.

Finally, in any system with at most seven real-valued intensity measurements on \(\mathbb C^3\), the real-linear measurement map on \(\mathcal H_3\) has a kernel of dimension at least two. The same odd-determinant argument gives a nonzero singular element and precludes universal phase retrieval. Eight is therefore the sharp universal minimum.

## Verification

The standalone `verify.py` reconstructs the entire nine-by-nine measurement matrix without floating-point arithmetic and checks the full determinant factorization, the eight-row kernel identity, the rank-three determinant factorization, the strict sum-of-squares positivity identity, exceptional ranks, and all nine erased-row ranks at \(s=2\). It ran successfully with SymPy. These polynomial identities are global identities in a real indeterminate, not evidence extrapolated from finitely many parameter tests. The argument above supplies the remaining rank and phase-injectivity implications.

## Relationship to prior work

Bojarovska and Flinth (2015) give the standard lifted-kernel criterion and a sufficient condition for phase retrieval using the **full** Gabor orbit. Li and colleagues (2016) give connectivity-based phase-retrieval conditions for multiwindow STFT data. Salanevich (first public July 3, 2023) studies efficient multiwindow Gabor injectivity and gives an asymptotic measurement reduction. A separate exact rank-discriminant result on one-coordinate cyclic Gabor systems covers full-orbit linear spans; such information alone does **not** imply that the kernel left after one intensity erasure is invertible. The present contribution is the sharp one-erasure phase diagram and the explicit nonsingular kernel certificate, including the critical two-tap instance.

## Limitations

Only real windows of the displayed one-parameter family and the three-point cyclic group are classified. No claim is made for complex \(s\), for larger cyclic orders, for arbitrary multiwindow systems, or for numerical noise robustness. Historical-priority uncertainty remains for specialist unpublished or poorly indexed small-dimensional measurement tables. The calculation is an exact deterministic proof, not an independent external mathematical audit.

## References

- I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800 (2015), https://arxiv.org/html/1503.05800v2.
- L. Li, C. Cheng, D. Han, Q. Sun and G. Shi, *Phase Retrieval from Multiple-Window Short-Time Fourier Measurements*, arXiv:1605.07046 (2016), https://arxiv.org/html/1605.07046v1.
- P. Salanevich, *Injectivity of Multi-window Gabor Phase Retrieval*, arXiv:2307.00834 (first public July 3, 2023), https://arxiv.org/abs/2307.00834.
