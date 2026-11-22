# Unique three-point minimax sampling on a mean-zero Sobolev interval

## Finding
Let
\[
\mathcal H=\left\{f\in H^1(0,1;\mathbb R):\int_0^1f(t)\,dt=0\right\},\qquad
\|f\|_{\mathcal H}^2=\int_0^1|f'(t)|^2\,dt.
\]
For a triple of distinct, unordered sample sites \(X=\{x_1,x_2,x_3\}\subset[0,1]\), define the squared joint trace norm
\[
C(X)^2=\sup_{f\in\mathcal H\setminus\{0\}}
\frac{\sum_{x\in X}|f(x)|^2}{\int_0^1|f'(t)|^2\,dt}.
\]
Let \(a_*\) be the unique root in \((1/9,1/8)\) of
\[
3a^3+6a^2-9a+1=0,
\qquad a_*=0.121561325176484\ldots.
\]
Then
\[
\boxed{\min_{|X|=3}C(X)^2=a_*},\qquad
\boxed{X_*=\left\{\tfrac12-a_*,\tfrac12,\tfrac12+a_*\right\}}.
\]
The unordered triple \(X_*\) is the **only** minimizer, including configurations allowed to use endpoints. Its sharp joint trace norm is \(\sqrt{a_*}=0.348656457241916\ldots\). The optimal three-by-three Gram matrix has spectrum
\[
\boxed{\left\{2a_*^2-2a_*+\tfrac14,\ a_*,\ a_*\right\}}.
\]
Thus the maximum eigenvalue is attained with multiplicity exactly two. If coincident locations are admitted as indexed observations, they cannot give a better value or another minimizer.

## Assumptions and scope
Functions are real, with the continuous representative of each \(H^1\) class. The only normalization is zero Lebesgue mean, and the only seminorm in the denominator is the ordinary first-derivative energy. All three observations have unit weight, the output carries the Euclidean \(\ell^2\) norm, and locations vary over the **whole closed interval**. The optimization is over three distinct points and does not assume symmetry.

Write \(S_X f=(f(x_1),f(x_2),f(x_3))\). The reproducing kernel for \(\mathcal H\) is
\[
K(x,y)=\frac13+\frac{x^2+y^2}{2}-\max\{x,y\}.
\]
Consequently \(C(X)^2\) is the largest eigenvalue of the positive-semidefinite Gram matrix \(G_X=(K(x_i,x_j))_{i,j=1}^3\). Equality in the sharp trace inequality for the minimizing triple is attained precisely by the nonzero functions in the two-dimensional top eigenspace of \(S_{X_*}^*S_{X_*}\), described explicitly below.

## Proof
**1. Derivation of the kernel.** For every \(f\in\mathcal H\), integration by parts and the zero-mean constraint yield
\[
f(x)=\int_0^1 f'(t)\bigl(t-\mathbf1_{\{t\ge x\}}\bigr)\,dt.
\]
Hence the derivative of the evaluation representer \(k_x\) equals \(t-\mathbf1_{\{t\ge x\}}\) almost everywhere. Integrating the product of two such derivatives gives exactly \(K(x,y)\) above. The identity \(\|S_X\|^2=\lambda_{\max}(G_X)\) follows from \(S_X S_X^*=G_X\).

**2. Universal two-mode lower certificates.** Order the sites \(x_1\le x_2\le x_3\) and set
\[
L=x_3-x_1,\quad M=\frac{x_1+x_3-1}{2},\quad
 d=x_2-\frac{x_1+x_3}{2}.
\]
Thus \(0\le L\le1\) and \(|d|\le L/2\). In the observation space choose the unit vectors
\[
u=\frac{(1,0,1)}{\sqrt2},\qquad
v=(0,1,0),\qquad z=\frac{(1,0,-1)}{\sqrt2}.
\]
Direct substitution of \(K\) into the Gram matrix gives
\[
z^{\mathsf T}G_Xz=\frac L2,
\]
and the compression to \(\operatorname{span}\{u,v\}\) is
\[
H_X=\begin{pmatrix}
A_0(L)+2M^2& B_0(L)+\dfrac{M^2+(M+d)^2}{\sqrt2}\\
B_0(L)+\dfrac{M^2+(M+d)^2}{\sqrt2}&\dfrac1{12}+(M+d)^2
\end{pmatrix},
\]
where
\[
A_0(L)=\frac{L^2}{2}-\frac L2+\frac16,\qquad
B_0(L)=\frac{L^2/4-L/2+1/6}{\sqrt2}.
\]
These are identities for **every** ordered triple, with no symmetry hypothesis.

**3. The exact balancing point.** Define \(p(a)=3a^3+6a^2-9a+1\). The rational signs \(p(1/9)>0\), \(p(1/8)<0\), and \(p'(a)<0\) on \([0,1/6]\) establish the unique specified root \(a_*\). At the centered symmetric triple with \(L=2a_*\), the vector \(z\) is an eigenvector of \(G_{X_*}\) of eigenvalue \(a_*\). The matrix on its orthogonal complement is
\[
H_0(2a_*)=\begin{pmatrix}
2a_*^2-a_*+1/6&(a_*^2-a_*+1/6)/\sqrt2\\
(a_*^2-a_*+1/6)/\sqrt2&1/12
\end{pmatrix}.
\]
Direct expansion yields
\[
\det\!\left(H_0(2a)-aI\right)=-\frac a6p(a).
\]
Its eigenvalues at \(a=a_*\) are therefore \(a_*\) and \(2a_*^2-2a_*+1/4\); the latter is strictly between zero and \(a_*\) by \(1/9<a_*<1/8\). This proves \(C(X_*)^2=a_*\) and the stated spectrum.

**4. Global sharpness and uniqueness.** If \(L>2a_*\), the antisymmetric certificate from Step 2 gives
\[
\lambda_{\max}(G_X)\ge L/2>a_*.
\]
For \(0\le L\le2a_*<1/4\), the entries of the centered compression
\[
H_0(L)=\begin{pmatrix}A_0(L)&B_0(L)\\B_0(L)&1/12\end{pmatrix}
\]
are positive. Both \(A_0(L)\) and \(B_0(L)\) are strictly decreasing over this interval. As the three indicated corrections to \(H_0(L)\) are all nonnegative, entrywise comparison with the strictly positive Perron eigenvector of \(H_0(L)\) gives
\[
\lambda_{\max}(G_X)\ge\lambda_{\max}(H_X)
\ge\lambda_{\max}(H_0(L))
\ge\lambda_{\max}(H_0(2a_*))=a_*.
\]
The final inequality is strict when \(L<2a_*\), since the positive upper-left and off-diagonal entries strictly decrease with \(L\). At \(L=2a_*\), the middle inequality is strict unless \(M=0\) and \(d=0\): whenever either is nonzero, at least one entry increases, and a strictly positive Perron eigenvector detects that increase in its Rayleigh quotient. Thus equality forces exactly \(X=X_*\), completing the global classification.

**5. All extremizing functions.** Let \(k_x\) denote the mean-zero evaluation representer and put
\[
\rho=\frac{B_0(2a_*)}{a_*-1/12}>0.
\]
All nonzero equality functions at \(X_*\) are precisely the linear combinations, with real coefficients not both zero, of
\[
\frac{k_{1/2-a_*}-k_{1/2+a_*}}{\sqrt2}
\quad\text{and}\quad
\frac{k_{1/2-a_*}+k_{1/2+a_*}}{\sqrt2}+\rho k_{1/2}.
\]
Indeed their coefficient vectors form the two-dimensional largest-eigenvalue eigenspace of \(G_{X_*}\); the remaining Gram eigenvalue is strictly smaller.

## Verification
The standalone `verify.py` symbolically reconstructs the compressed Gram entries, the antisymmetric Rayleigh quotient, and the balancing cubic. It independently integrates exact rational kernel products on a finite grid and checks further rational site configurations. Its reproducible output contains **1,999 exact algebraic/rational assertions** and a numerical bisection of the unique root. To execute: `python verify.py` with Python 3 and SymPy installed. Finite tests and a numerical root calculation do not establish the universal theorem; the proof is Steps 1–5.

## Relationship to prior work
Gauthier and Bay (2012) give an RKHS spectral method for interpolation and the finite-dimensional Gram eigenvalue framework (especially their Section 5), without optimizing the three Neumann-interval evaluation positions or deriving this cubic threshold. Gauthier and Pronzato (2014) treat integrated predictive variance of kernel interpolation designs, which is not the same objective as the largest **forward** Gram eigenvalue; only the accessible abstract was inspected. Santin (2022) proves equally spaced points optimal for a **Dirichlet Brownian-bridge interpolation power function**, a different boundary condition and a different loss. In contrast, the present mean-zero Neumann three-site forward trace objective has a unique centrally clustered minimizer and a double largest eigenvalue. Translation-invariant circular Sobolev kernels likewise differ: an interval Neumann kernel cannot be substituted into a circular three-gap theorem.

## Limitations
The theorem classifies only three unit-weight point observations in the specified real mean-zero derivative-energy Sobolev space. No claim is made for more sites, unequal observation weights, different boundary conditions, fractional orders, interpolation error, or statistical estimation risk. The historical-priority comparison is necessarily qualified by incomplete full-text access to the Gauthier–Pronzato integrated-variance paper and possible unindexed equivalent results. The mathematical proof is self-contained and has not undergone independent external audit.

## References
1. B. Gauthier and X. Bay, “Spectral approach for kernel-based interpolation,” *Annales de la Faculté des sciences de Toulouse* 21 (2012), 439–479. Public online date 2012-10-23. https://doi.org/10.5802/afst.1341 ; full text https://www.numdam.org/item/AFST_2012_6_21_3_439_0.pdf
2. B. Gauthier and L. Pronzato, “Spectral approximation of the IMSE criterion for optimal designs in kernel-based interpolation models,” *SIAM/ASA Journal on Uncertainty Quantification* 2 (2014), 805–825. https://doi.org/10.1137/130928534
3. G. Santin, “Equally spaced points are optimal for Brownian Bridge kernel interpolation,” arXiv:2210.15959, first public version 2022-10-28. https://arxiv.org/abs/2210.15959
