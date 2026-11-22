# Antipodal rigidity and a linear spectral cusp for four-mode Fourier observation on two arcs

## Finding
Let four consecutive circular Fourier characters be observed continuously and without weighting on two equal, nonoverlapping arcs of fixed total length. **Antipodal arc centers uniquely maximize the least captured energy and simultaneously uniquely minimize the greatest captured energy and the spectral condition number**, among all possible arc separations. The exact optimal observation spectrum consists of two double eigenvalues:
\[
\lambda_{\min}^{*}=\frac{2a-\sin(2a)}{\pi}\quad\text{(multiplicity two)},\qquad
\lambda_{\max}^{*}=\frac{2a+\sin(2a)}{\pi}\quad\text{(multiplicity two)}.
\]
Here \(a\in(0,\pi/2)\) is the common arc half-width. Every nonantipodal configuration has a *strictly smaller* least eigenvalue and a *strictly greater* largest eigenvalue. In particular the sharp squared observation condition number is
\[
\kappa_{*}=\frac{2a+\sin(2a)}{2a-\sin(2a)},\qquad
\kappa_{*}\sim\frac3{a^2}\quad(a\downarrow0).
\]
The spectral rigidity has a **linear angular cusp**: as \(\theta\uparrow\pi/2\), where \(\pm\theta\) are the centers,
\[
\begin{aligned}
\lambda_{\min}(a,\theta)&=\lambda_{\min}^{*}
 -\frac{4\sin^3a}{\pi}\cos\theta+O_a(\cos^2\theta),\\
\lambda_{\max}(a,\theta)&=\lambda_{\max}^{*}
 +\frac{4\sin a\cos^2a}{\pi}\cos\theta+O_a(\cos^2\theta).
\end{aligned}
\]
Both cusp slopes are strictly positive. This is distinct from the quadratic separation loss of the three-mode problem, and arises because both optimal spectral edges are double.

## Assumptions and scope
Work on \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), with normalized Haar measure \(dt/(2\pi)\), and let
\[
 V_4=\operatorname{span}_{\mathbb C}\{1,e^{it},e^{2it},e^{3it}\},\quad
 \|f\|_2^2=\frac1{2\pi}\int_0^{2\pi}|f(t)|^2dt.
\]
For every \(0<a<\pi/2\) and \(a\le\theta\le\pi/2\), take the two arcs
\[
 E_{a,\theta}=\bigl([\theta-a,\theta+a]\cup[-\theta-a,-\theta+a]\bigr)\pmod{2\pi}.
\]
Their interiors are disjoint, with total normalized measure \(2a/\pi\). A common rotation and swapping the arcs reduce every pair of equal-length, nonoverlapping arcs to this parameter range; meeting at an endpoint is allowed. Write \(G(a,\theta)\) for the Hermitian Gram operator of the captured-energy quadratic form
\[
\langle Gf,f\rangle=\frac1{2\pi}\int_{E_{a,\theta}}|f(t)|^2dt
\]
on the orthonormal Fourier coefficient space \(V_4\). Its eigenvalues are strictly positive because a nonzero trigonometric polynomial cannot vanish on an interval. The condition number means \(\lambda_{\max}/\lambda_{\min}\), not the square root of that ratio for the underlying restriction map.

## Proof
**Fourier moment normalization.** In the ordered basis \((1,e^{it},e^{2it},e^{3it})\), the exact Gram entries are
\[
 G_{jk}=\frac1{2\pi}\int_{E_{a,\theta}}e^{i(k-j)t}dt.
\]
They form a real symmetric Toeplitz matrix. Put
\[
 q=\frac{2a}{\pi},\quad h=\frac{2\sin a}{\pi},\quad c=\cos a\in(0,1),\quad u=\cos\theta\in[0,c].
\]
The elementary sine triple-angle identity gives
\[
 G=qI_4+hB,\qquad
 B=\begin{pmatrix}
 0&x&y&z\\x&0&x&y\\y&x&0&x\\z&y&x&0
 \end{pmatrix},
\]
where
\[
 x=u,\qquad y=c(2u^2-1),\qquad
 z=\frac{4c^2-1}{3}(4u^3-3u).
\]
At antipodal placement \(u=0\), one has \(x=z=0\), \(y=-c\). Hence \(B\) has the spectrum \((-c,-c,c,c)\), proving the displayed exact eigenvalues.

**A simultaneous two-sided determinant obstruction.** Denote by \(R\) the coordinate reversal matrix. The matrix \(B\) commutes with \(R\), and each of the symmetric and antisymmetric eigenspaces of \(R\) is two-dimensional. For the matrix \(cI_4+B\) the two restricted blocks, in natural orthonormal coordinates, are
\[
 C_{+}=\begin{pmatrix}c+z&x+y\\x+y&c+x\end{pmatrix},\qquad
 C_{-}=\begin{pmatrix}c-z&x-y\\x-y&c-x\end{pmatrix}.
\]
For \(cI_4-B\) they are
\[
 D_{+}=\begin{pmatrix}c-z&-x-y\\-x-y&c-x\end{pmatrix},\qquad
 D_{-}=\begin{pmatrix}c+z&-x+y\\-x+y&c+x\end{pmatrix}.
\]
Direct determinant expansion, valid for arbitrary real \(x,y,z,c\), yields the common identity
\[
\det C_++\det C_- = \det D_++\det D_-
 =2(c^2+xz-x^2-y^2).
\]
The exact trigonometric parameterization forces the nonstandard but elementary quartic cancellation
\[
 \boxed{\ c^2+xz-x^2-y^2
 =-\frac43(1-c^2)u^4.\ }
\]
If \(u>0\), both determinant sums are negative. Each pair of blocks therefore contains at least one negative determinant, and the corresponding symmetric \(2\times2\) block has a negative eigenvalue. Thus \(cI_4+B\) is not positive semidefinite and \(cI_4-B\) is not positive semidefinite, proving simultaneously
\[
 \lambda_{\min}(B)<-c,\qquad \lambda_{\max}(B)>c.
\]
As \(h>0\), this proves the unique antipodal maximum of \(\lambda_{\min}(G)\) and minimum of \(\lambda_{\max}(G)\). Since all eigenvalues of \(G\) are positive, their strict inequalities also prove the uniquely minimal condition number.

**Sharp cusp and small-width behavior.** At \(u=0\) the \(-c\)-eigenspace of \(B\) has normalized basis \((1,0,1,0)/\sqrt2\), \((0,1,0,1)/\sqrt2\); the \(+c\)-eigenspace has basis \((1,0,-1,0)/\sqrt2\), \((0,1,0,-1)/\sqrt2\). The first \(u\)-derivative of \(B\) restricts to \(\bigl(\begin{smallmatrix}0&2(1-c^2)\\2(1-c^2)&0\end{smallmatrix}\bigr)\) on the first space and \(\bigl(\begin{smallmatrix}0&2c^2\\2c^2&0\end{smallmatrix}\bigr)\) on the second. Standard perturbation of the separated double eigenvalues (or direct expansion of the two reversal blocks) gives
\[
 \lambda_{\min}(B)=-c-2(1-c^2)u+O_a(u^2),\qquad
 \lambda_{\max}(B)=c+2c^2u+O_a(u^2).
\]
Multiplying by \(h\) proves the cusp formula. Finally \(2a-\sin2a=(4/3)a^3+O(a^5)\), whereas \(2a+\sin2a=4a+O(a^3)\), giving the sharp conditioning law.

## Verification
A standalone checker `CHECK.py` (requirements in `requirements.txt`) independently builds the integrated Fourier Gram and verifies the two symbolic reversal-block determinant identities, their quartic cancellation, and direct Fourier-moment integration. It also numerically confirms the strict two-sided spectral inequalities for a grid of permissible widths and separations, as well as the double optimal eigenvalues and the narrow-width law. A completed run reports `FOUR_MODE_TWO_ARC_CHECKS_PASS 1106`. This finite set of tests is a consistency check, not a replacement for the global proof above.

## Relationship to prior work
Marceca, Romero and Speckbacher study general Fourier concentration operators on two domains and provide nonasymptotic estimates for the number of intermediate spectral eigenvalues, rather than the exact four-character two-arc placement or simultaneous extremal optimization. Asipchuk and Drezels construct exponential Riesz bases on unions of intervals; their results do not give this fixed finite-band two-arc min/max eigenvalue theorem. A published finite-band two-arc observability analysis proves asymptotic antipodal optimality for each *odd* \((2m+1)\)-character band and exact all-width optimality for three characters, without covering this four-character simultaneous-edge theorem. Another related three-character result gives a quadratic (rather than linear) separation loss and compares its frame potential. The four-character proof here requires the quartic reflection-block identity and establishes a new even-band, double-edge rigidity mechanism not obtained by applying any of those statements as a corollary.

## Limitations
The result assumes exactly four consecutive Fourier characters, two equal-length nonoverlapping unweighted observation arcs, and a fixed total observation measure. It does not optimize arbitrary measurable observation sets, unequal widths, variable weights or higher Fourier bandwidths. The sharp condition number concerns exact noiseless linear observation and is not a probabilistic noise guarantee. The historical-priority assessment remains conditional on accessible indexed sources; an equivalent result in unindexed optimal-design or prolate literature cannot be ruled out. Independent mathematical review has not been performed.

## References
1. O. Asipchuk and V. Drezels, *Examples of exponential bases on union of intervals*, arXiv:2211.03821, first posted 2022-11-07. https://arxiv.org/abs/2211.03821
2. F. Marceca, J. L. Romero and M. Speckbacher, *Eigenvalue estimates for Fourier concentration operators on two domains*, arXiv:2301.11685, first posted 2023-01-27. https://arxiv.org/abs/2301.11685
3. *Sharp two-arc Fourier observability: a Legendre constant and asymptotic antipodal design*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-two-arc-fourier-observability-a-legendre-constant-and-asym--900ee56c5370
4. *Antipodal maximin sampling and a quarter-circle tightness bifurcation for three Fourier modes*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-antipodal-maximin-sampling-and-a-quarter-circle-tightness-bifurc--1c5e863c7cba
5. *Antipodal two-arc observation uniquely optimizes three-mode Fourier stability*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-antipodal-two-arc-observation-uniquely-optimizes-three-mode-four--87a22b9723ef
