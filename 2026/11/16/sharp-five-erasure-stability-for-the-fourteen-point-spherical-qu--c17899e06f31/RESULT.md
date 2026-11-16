# Sharp five-erasure stability for the fourteen-point spherical quadrature

## Finding
Let \(X\subset S^2\) be the fourteen nodes
\[
X=\{\pm e_1,\pm e_2,\pm e_3\}\cup
\{(\varepsilon_1,\varepsilon_2,\varepsilon_3)/\sqrt3:\varepsilon_j\in\{-1,1\}\}.
\]
Assign weight \(w_x=1/15\) to each of the six coordinate-axis nodes and \(w_x=3/40\) to each of the eight cube nodes. Equip the nine-dimensional space \(\mathcal H_{\le2}=\mathcal H_0\oplus\mathcal H_1\oplus\mathcal H_2\) with normalized spherical \(L^2\) measure, and for a retained nine-node set \(S\subset X\), define the weighted evaluation operator \((E_Sf)(x)=\sqrt{w_x}\,f(x)\) for \(x\in S\).

Then the **sharp E-optimal nine-node bound** is
\[
\boxed{\max_{S\subset X,\ |S|=9}\lambda_{\min}(E_S^*E_S)=\frac15.}
\]
Equality holds for **exactly six** retained sets: the complements of
\[
T_{i,\sigma}=\{\sigma e_i\}\cup
\{(\varepsilon_1,\varepsilon_2,\varepsilon_3)/\sqrt3:\varepsilon_i=-\sigma\},
\qquad i\in\{1,2,3\},\quad\sigma\in\{-1,1\}.
\]
For each of these six optimizers, the spectrum of \(E_S^*E_S\), with multiplicities, is
\[
\boxed{\left\{1^{[4]},\ \left(\frac15\right)^{[2]},\ \frac12,\
\frac25+\frac{\sqrt3-1}{5\sqrt2},\
\frac25-\frac{\sqrt3-1}{5\sqrt2}\right\}.}
\]
Here exponent-like bracket notation \(\alpha^{[m]}\) denotes an eigenvalue \(\alpha\) of multiplicity \(m\). In particular every maximizing set is unisolvent for all real or complex degree-at-most-two spherical harmonics.

## Assumptions and scope
All points have Euclidean norm one and are distinguished as individually labeled sampling locations. The weighted sampling cost is fixed by the original positive cubature weights: weights are **not renormalized** after erasure, and coefficients are measured in the normalized spherical \(L^2\) norm \(\|f\|_2^2=(4\pi)^{-1}\int_{S^2}|f|^2\,d\omega\). The problem chooses **exactly nine of the fourteen existing nodes**, without moving nodes or optimizing weights. This is the minimal possible node count for unrestricted nine-dimensional linear reconstruction. Both the complex and real coefficient versions have identical eigenvalues.

## Proof
**1. The full fourteen-node sampling operator is an isometry.** The weights sum to one. By independent coordinate-sign symmetries, every odd-degree coordinate monomial of total degree at most five integrates and sums to zero. The nontrivial even moments are
\[
\sum_X w_x x_i^2=\frac13,\qquad
\sum_X w_x x_i^4=\frac15,\qquad
\sum_X w_x x_i^2x_j^2=\frac1{15}\quad(i\ne j).
\]
These are exactly the moments of normalized surface measure on \(S^2\); together they cover all monomials through degree five. In particular the weighted rule is exact on products of harmonics of degrees at most two. Thus the fourteen-row evaluation operator \(E_X\) satisfies \(E_X^*E_X=I_9\).

**2. Convert retained-set stability to a five-node projection problem.** The reproducing kernel for \(\mathcal H_{\le2}\) in probability-area normalization is
\[
K(x,y)=1+3(x\cdot y)+5P_2(x\cdot y)
=\frac{15(x\cdot y)^2+6(x\cdot y)-3}{2}.
\]
Let \(B=E_XE_X^*\), whose entries are \(B_{xy}=\sqrt{w_xw_y}\,K(x,y)\). It is an orthogonal projector of rank nine. If \(T=X\setminus S\) consists of the five erased nodes, then
\[
E_S^*E_S=I_9-E_T^*E_T,
\qquad\lambda_{\min}(E_S^*E_S)=1-\lambda_{\max}(B_T),
\]
where \(B_T\) is the principal submatrix on the erased nodes. Consequently it suffices to minimize the largest eigenvalue of the five-by-five matrix \(B_T\).

**3. Three forbidden erased pairs.** A pole has diagonal entry \(B_{aa}=3/5\), a cube node has diagonal entry \(B_{cc}=27/40\), and the following facts hold.

(a) Opposite cube nodes have off-diagonal entry \(9/40\), so their two-by-two principal block has largest eigenvalue \(9/10>4/5\).

(b) If an axis node \(a=\sigma e_i\) and a cube node \(c\) lie in the **same** coordinate hemisphere \(c_i=\sigma/\sqrt3\), their cross entry is \((1+\sqrt3)/(10\sqrt2)\). The determinant of \((4/5)I\) minus their two-by-two principal block is
\[
\left(\frac45-\frac35\right)\left(\frac45-\frac{27}{40}\right)
-\left(\frac{1+\sqrt3}{10\sqrt2}\right)^2
=\frac{1-2\sqrt3}{200}<0.
\]
Hence that block has an eigenvalue strictly larger than \(4/5\).

(c) Opposite axis nodes form the block \(\bigl(\begin{smallmatrix}3/5&1/5\\1/5&3/5\end{smallmatrix}\bigr)\), whose top eigenvalue is exactly \(4/5\), with eigenvector \((1,1)\). Adding **any third erased node** strictly increases the top eigenvalue: its coupling to \((1,1)\) is \(-1/5\) if it is another axis node and \(1/(5\sqrt2)\) if it is a cube node, both nonzero. This follows directly from the kernel formula and the variational principle, by optimizing also over a small component on the new coordinate. Since every erased set has five nodes, any opposite-axis pair therefore forces \(\lambda_{\max}(B_T)>4/5\).

**4. The only sets without forbidden pairs.** Suppose a five-node erased set \(T\) contains none of the pairs in Step 3, and let \(k\) be its number of axis nodes. For \(k\ge4\), two axes are opposite, impossible. If \(k=0\), five cube nodes force an antipodal cube pair, impossible. If \(k=1\), every cube node must have the coordinate sign *opposite* that single axis; the four admissible cube nodes are exactly those in the opposite coordinate hemisphere, so \(T=T_{i,\sigma}\). If \(k=2\), there are at most two cube nodes opposite in both specified coordinate signs, but three cube nodes are required. If \(k=3\), at most one cube node opposes all three signs, but two are required. Thus **every** five-node set other than the six displayed \(T_{i,\sigma}\) contains a forbidden pair and has \(\lambda_{\max}(B_T)>4/5\).

**5. Exact spectral evaluation of the six survivors.** Fix \(T_{i,\sigma}\). The four cube nodes form a square: each has two cube neighbors at dot product \(1/3\), and the opposite cube neighbor at dot product \(-1/3\). Their four-by-four \(B_T\) block therefore has diagonal \(27/40\), adjacent entries \(1/40\), and opposite entries \(-1/8\). Its orthogonal square Fourier modes have eigenvalues \(3/5\) (constant), \(1/2\) (alternating), and \(4/5\) (twice). The erased pole couples with identical entry \((1-\sqrt3)/(10\sqrt2)\) to all four cube nodes, so it only mixes with the normalized constant mode; the resulting two-by-two block is
\[
\begin{pmatrix}
3/5 &(1-\sqrt3)/(5\sqrt2)\\
(1-\sqrt3)/(5\sqrt2)&3/5
\end{pmatrix}.
\]
Its eigenvalues are \(3/5\pm(\sqrt3-1)/(5\sqrt2)\), both strictly below \(4/5\). Thus the entire removed Gram spectrum is
\[
\operatorname{spec}(B_T)=\left\{\left(\frac45\right)^{[2]},\ \frac12,\
\frac35+\frac{\sqrt3-1}{5\sqrt2},\
\frac35-\frac{\sqrt3-1}{5\sqrt2}\right\}.
\]
The retained frame spectrum follows by subtracting these five eigenvalues from one and adding four eigenvalues equal to one. Its smallest eigenvalue equals \(1/5\). Together with Step 4, this proves the sharp bound and all six and only six equality sets. \(\square\)

## Verification
The self-contained `check_lebedev14.py` uses NumPy for an independently specified real orthonormal nine-function spherical-harmonic basis and enumerates every \(\binom{14}{9}=2002\) nine-node set. It finds exactly six maximizers, all the six displayed hemispherical complements, with minimum eigenvalue \(1/5\). It also records 1456 full-rank and 546 singular nine-node selections as a supplementary check, **not** as a premise of the proof. Separately, SymPy verifies all monomials of degree at most four in exact algebraic arithmetic, the identity \(B^2=B\), the special erased Gram characteristic polynomial, and the critical aligned-pair determinant. Run `python check_lebedev14.py` with NumPy and SymPy; the success prefix is `LEBEDEV14_VERIFY_OK`. The proof of optimality is analytic and finite-combinatorial, not inferred from floating-point enumeration.

## Relationship to prior work
Shimizu and Tsunoda's first public 2022 study of \(SO(3)\) quadrature explains the accuracy and efficiency of octahedrally symmetric Lebedev cubature, but does not optimize deleting five nodes from a quadratic spherical-harmonic sampling frame. Nafees, Khalid, Kennedy and McEwen (2017) address stable nine-dimensional spherical sampling by choosing points on latitude rings, a different admissible design and objective. The previously published *All-degree harmonic sampling and sharp stability on the radially normalized rhombic dodecahedron* studies **single exact degrees**, **unweighted**, with all nodes (and seven antipodal representatives), rather than the weighted cumulative-degree quadratic, nine-of-fourteen E-optimal problem. Known eleven-node guaranteed recovery results for the same vertex set likewise concern rank rather than the present optimal nine-node spectral bound. The full cubature geometry, reproducing kernel, and linear-algebra identities are standard ingredients and are not claimed as novel.

## Limitations
The theorem fixes the fourteen Lebedev nodes and original weights, exactly nine retained nodes, the spherical degree-zero-through-two space, and the normalized \(L^2\) metric. It says nothing about optimality over *all possible* nine-node spherical configurations, alternate reweightings, adaptive measurements, or worst-case noise when the noise covariance does not match the weighted measurements. Earlier specialty tables could contain an equivalent nine-node classification; bounded searching does not certify historical priority. Independent external mathematical validation has not been performed.

## References
1. N. Shimizu and Y. Tsunoda, *\(SO(3)\) quadratures in angular-momentum projection*, arXiv:2205.04119 (first posted 2022-05-09), section II.3, https://arxiv.org/abs/2205.04119 .
2. W. Nafees, Z. Khalid, R. A. Kennedy, and J. D. McEwen, *Optimal-Dimensionality Sampling on the Sphere: Improvements and Variations*, arXiv:1709.02497 (first posted 2017-09-08), https://arxiv.org/abs/1709.02497 .
3. *All-degree harmonic sampling and sharp stability on the radially normalized rhombic dodecahedron*, online research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-all-degree-harmonic-sampling-and-sharp-stability-on-the-radially--d466d2d286c1 .
