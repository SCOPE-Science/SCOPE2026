# Quadratic vertex-covariance anisotropy of wheel spanning-tree polytopes

## Finding
For every integer \(m\ge3\), let \(W_{m+1}=K_1\vee C_m\) be the wheel with one hub and \(m\) rim vertices, and let \(P_m\subset\mathbb R^{2m}\) be the convex hull of the edge-indicator vectors of its spanning trees. Let \(X_m\) be uniform on the distinct vertices of \(P_m\), with covariance \(C_m\). Its kernel is exactly the constant edge vector; hence it has \(2m-1\) positive eigenvalues.

The full finite-dimensional spectrum is given below by explicit \(2\)-by-\(2\) Fourier blocks involving a single algebraic number. Put \(\lambda_{\min}^+(m)\) for the smallest positive eigenvalue and \(\lambda_{\max}(m)\) for the largest. Then
\[
\lim_{m\to\infty}m^2\lambda_{\min}^+(m)=\frac{\pi^2}{\sqrt5},\qquad
\lim_{m\to\infty}\lambda_{\max}(m)=\frac4{5\sqrt5},\qquad
\boxed{\lim_{m\to\infty}\frac{\kappa(C_m)}{m^2}=\frac4{5\pi^2}},
\]
where \(\kappa(C_m)=\lambda_{\max}(m)/\lambda_{\min}^+(m)\) is the intrinsic covariance condition number. For all sufficiently large \(m\), the maximum eigenvalue is simple with direction the difference between the total spoke and total rim edge counts; the minimum positive eigenvalue has real multiplicity two, arising from the first cyclic harmonics.

More precisely, the two spectral branches of the limiting Fourier symbol, with frequency \(0\le\theta\le\pi\), are
\[
\boxed{\Lambda_\pm(\theta)=\frac2{\sqrt5}\,
 \frac{3-2\cos^2(\theta/2)\pm\cos(\theta/2)}{9-4\cos^2(\theta/2)}}.
\]
The minus branch increases strictly and the plus branch decreases strictly with \(\theta\) in \((0,\pi)\). In particular, the spectral anisotropy arises from the quadratic vanishing of the minus branch at zero frequency, not from a vanishing one-edge inclusion probability.

## Assumptions and scope
The edge coordinates use the standard unweighted Euclidean metric. The \(m\) spoke edges precede the \(m\) rim edges in a fixed cyclic order. The law is **uniform over the distinct spanning-tree incidence vectors**, not uniform volume in \(P_m\), nor the distribution of a random minimum spanning tree with edge weights. No edge weights or asymmetric wheels are included. The zero eigenvalue corresponding to the fixed tree size is excluded from \(\kappa\).

For an exact formula valid for every \(m\ge3\), put
\[
a=\frac{3-\sqrt5}{2},\qquad
g_d=\frac{a^d+a^{m-d}}{\sqrt5(1-a^m)}\quad(0\le d<m),
\]
with subscripts extended modulo \(m\); define \(h_d=2g_d-g_{d-1}-g_{d+1}\) and \(q_d=g_d-g_{d+1}\). Set \(\zeta_j=e^{2\pi i j/m}\). For \(j=0,\ldots,m-1\), form the Hermitian matrix
\[
H_j=\begin{pmatrix}
g_0-\sum_{d=0}^{m-1}g_d^2\zeta_j^d &-\sum_{d=0}^{m-1}q_d^2\zeta_j^d\\
-\sum_{d=0}^{m-1}q_d^2\overline{\zeta_j}^{\,d}&h_0-\sum_{d=0}^{m-1}h_d^2\zeta_j^d
\end{pmatrix}.
\]
The multiset of eigenvalues of \(C_m\), including its single zero, is exactly the union of the two eigenvalues of each \(H_j\). Thus this formula specifies every finite eigenvalue without numerical diagonalization of a \(2m\)-dimensional matrix.

## Proof
**1. Tree-incidence covariance.** Let \(E\) be the \(m\)-by-\(2m\) reduced oriented edge-incidence matrix obtained by deleting the hub row. For the cyclic shift \(S e_j=e_{j+1}\), its spoke and rim blocks are \(E=[I\;I-S]\), and
\[
L=EE^\mathsf T=3I-S-S^\mathsf T.
\]
The matrix-tree theorem and Cauchy--Binet give the weighted tree partition function \(Z(w)=\det(E\operatorname{diag}(w)E^\mathsf T)\). Every contributing squared maximal minor is \(1\). Differentiating \(\log Z(w)\) twice with respect to the logarithmic edge weights \(\log w_e\) and \(\log w_f\) at unit weights therefore yields, for \(G=L^{-1}\) and \(K=E^\mathsf TGE\),
\[
\operatorname{Cov}(X_{m,e},X_{m,f})=\mathbf1_{e=f}K_{ee}-K_{ef}^{\,2}.
\]
This is also the two-edge transfer-current identity, here derived directly from the determinant rather than assumed.

**2. Exact finite Green kernel and Fourier blocks.** The difference equation \(3g_d-g_{d-1}-g_{d+1}=\mathbf1_{d=0}\) on the cycle has the unique solution stated above. Indeed \(a+a^{-1}=3\) and \(3-2a=\sqrt5\); periodizing the infinite-line Green kernel \(a^{|d|}/\sqrt5\) gives the expression for \(g_d\). From \(K=E^\mathsf TGE\), the spoke/spoke, rim/rim and spoke/rim transfer currents at cyclic displacement \(d\) are \(g_d\), \(h_d\) and \(q_d\), respectively, up to reversing the cyclic index on the mixed block. Applying the covariance identity, the four covariance blocks are circulant. Their discrete Fourier transform is exactly the family \(H_j\), proving the claimed finite spectrum.

Each spanning tree has exactly \(m\) edges, so \(C_m\mathbf1=0\). There are no further null directions. To see this without a numerical rank assertion, observe that every pair of wheel edges belongs to some simple cycle. For a cycle containing edges \(e\ne f\), extend all its edges except \(e\) to a spanning tree \(T\). Replacing \(f\) by \(e\) gives another spanning tree, whose incidence-vector difference is the coordinate difference \(\mathbf e_e-\mathbf e_f\). Such differences span the hyperplane \(\mathbf1^\perp\). Any vector with zero variance of its inner product with \(X_m\) is orthogonal to all such differences and therefore constant. Hence \(\ker C_m=\operatorname{span}\{\mathbf1\}\).

**3. Limiting symbol, including the algebraic simplification.** On the two-sided infinite rim, the Green kernel is \(g_d^{(\infty)}=a^{|d|}/\sqrt5\). The corresponding diagonal coefficients of the covariance Fourier symbol, with \(x=\cos\theta\) and \(D=1-2a^2x+a^4\), are
\[
A(x)=\frac1{\sqrt5}-\frac{1-a^4}{5D},
\qquad
B(x)=\frac{2(1-a)}{\sqrt5}-\frac{4(1-a)^2}{5}-\frac{2(1-a)^4(x-a^2)}{5D}.
\]
The mixed coefficient has absolute value
\[
|Q(\theta)|=\frac{(1-a)^2(1-a^2)}{5D}\sqrt{2+2x}.
\]
Use \((1-a)^2=a\), \(a+a^{-1}=3\), \(1-a^2=\sqrt5a\), and \(D=a^2(7-2x)\). Direct substitution simplifies both diagonal coefficients to
\[
A(x)=B(x)=\frac2{\sqrt5}\frac{2-x}{7-2x},
\qquad |Q(\theta)|=\frac2{\sqrt5}\frac{\cos(\theta/2)}{7-2x}
\quad(0\le\theta\le\pi).
\]
The eigenvalues \(A\pm|Q|\) are precisely \(\Lambda_\pm\) above.

Write \(t=\cos(\theta/2)\in[0,1]\). Differentiating \((3-2t^2\pm t)/(9-4t^2)\) gives numerators \((2t-3)^2\) for the plus sign and \(-(2t+3)^2\) for the minus sign, both over the positive denominator \((9-4t^2)^2\). Thus \(\Lambda_+\) increases strictly with \(t\), while \(\Lambda_-\) decreases strictly with \(t\). Since \(t\) decreases as \(\theta\) increases, the stated monotonicity follows. The endpoint values are
\[
\Lambda_-(0)=0,\quad\Lambda_+(0)=\frac4{5\sqrt5},\quad
\Lambda_\pm(\pi)=\frac2{3\sqrt5}.
\]
Near zero, \(t=1-\theta^2/8+O(\theta^4)\), so
\[
\Lambda_-(\theta)=\frac{\theta^2}{4\sqrt5}+O(\theta^4).
\]

**4. Uniform finite-size control and extreme modes.** Choose for each cyclic displacement its representative of absolute value at most \(m/2\). The periodized Green kernel differs from \(a^{|d|}/\sqrt5\) by at most a constant times \(a^{m/2}\); the same holds for its first differences. Squaring, summing the \(m\) coefficients in each Fourier block and bounding the omitted infinite tails gives, uniformly in \(j\),
\[
\|H_j-H^{(\infty)}(2\pi j/m)\|_{\mathrm{op}}\le C m a^{m/2}
\]
for an absolute finite \(C\) and the infinite symbol interpreted periodically. Eigenvalue perturbation obeys the same bound. The strict monotonicity just proved, plus the \(m^{-2}\)-sized separation between the first two nonzero low frequencies and between the top zero-frequency and next frequency, shows that for all sufficiently large \(m\), the smallest positive eigenvalues occur exactly at \(j=1,m-1\), and the largest occurs exactly at \(j=0\). The two conjugate low-frequency blocks give a real eigenspace of dimension two; at \(j=0\), the unique nonconstant mode is the uniform spoke-minus-rim vector because the other direction is the fixed-size null vector.

Finally \(\theta_1=2\pi/m\) gives
\[
\lambda_{\min}^+(m)=\Lambda_-(2\pi/m)+O(m a^{m/2})
=\frac{\pi^2}{\sqrt5\,m^2}+O(m^{-4}+m a^{m/2}),
\]
and \(\lambda_{\max}(m)=4/(5\sqrt5)+O(m a^{m/2})\). Dividing proves the claimed sharp quadratic condition-number law.

## Verification
The accompanying standalone `verify.py` uses only the Python standard library. It separately enumerates every spanning tree and computes the exact rational vertex covariance for each wheel with \(3\le m\le7\); those matrices agree entry-by-entry with the rational inverse-Laplacian determinant formula. It also compares all 525 closed-form finite Fourier block eigenvalue pairs against Fourier transforms of separately assembled covariance matrices, checks nullity and conjugate frequencies, and compares large finite spectra with the analytical limiting symbol and asymptotic constant. On replay it reports `WHEEL_SPANNING_TREE_INERTIA_CHECKS_PASSED` with \(1343\) enumerated spanning trees across five graph sizes and \(495\) checked nonzero Fourier blocks. The limit and the eventual extremizer statements are proved analytically above; finite checks are not substituted for that proof.

To reproduce, run `python3 verify.py` in the directory containing this file and the script.

## Relationship to prior work
Spanning-tree polytopes are standard graphic-matroid base polytopes. Chaourar (2019) studies their facets, and classical Kirchhoff/transfer-current theory determines inclusion probabilities and pair covariances for arbitrary graphs. Wheel Laplacian eigenvalues are also known. Those statements are inputs to the calculation, not new claims here. The contribution of this result is the **explicit wheel-specific vertex-covariance Fourier dispersion**, its monotone limiting two-band structure, the eventual exact types of extreme eigenspaces, and the sharp constant \(4/(5\pi^2)\) in quadratic anisotropy. Generic transfer-current formulas do not themselves identify that constant or the eigenaxis classification. Earlier equivalent treatments under electrical-network or structure-factor terminology cannot be completely ruled out.

## Limitations
The result concerns the canonical unweighted wheel and its vertex-uniform measure only. It does not claim a finite explicit threshold for when the asymptotic extremal eigenspaces stabilize. A finite closed formula specifies all eigenvalues, but does not order them for every small \(m\). The claim does not characterize arbitrary graph spanning-tree polytopes. Literature priority has not been independently certified; the transfer-current identity and wheel Laplacian background are prior results.

## References
- B. Chaourar, *The facets of the spanning trees polytope*, first public version 18 March 2019, arXiv:1903.07292, https://arxiv.org/abs/1903.07292 .
- Y. Wigderson, *Uniform Spanning Trees and Determinantal Point Processes*, expository notes, https://ywigderson.math.ethz.ch/math/static/UniformSpanningTrees.pdf .
- L. Avena and A. Gaudillière, *A proof of the transfer-current theorem in absence of reversibility*, Statistics & Probability Letters 142 (2018), 17–22, DOI:10.1016/j.spl.2018.06.007 .
- *On Laplacian Eigenvalues of Wheel Graphs*, Symmetry 15 (2023), article 1737, https://doi.org/10.3390/sym15091737 .
- *Fairest edge usage and minimum expected overlap for random spanning trees*, Discrete Mathematics (2021), DOI:10.1016/j.disc.2020.112282 .
