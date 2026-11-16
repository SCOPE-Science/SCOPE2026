# Balanced-orthant concentration of quadratic spherical harmonics: a complete spectrum and the dimension-twelve switch

## Finding
Let \(d\ge4\) be even. Give \(\mathbb S^{d-1}\) normalized rotation-invariant measure \(\sigma\), and define the balanced-orthant region
\[
\Omega_d=\{x\in\mathbb S^{d-1}:\#\{i:x_i>0\}=d/2\}.
\]
Write \(p_d=\sigma(\Omega_d)=2^{-d}\binom d{d/2}\). On the pure real degree-two spherical-harmonic space \(\mathcal H_2\), define the concentration operator \(T_d\) by
\[
\langle T_df,g\rangle_{L^2(\sigma)}=\int_{\Omega_d}f(x)g(x)\,d\sigma(x),\qquad f,g\in\mathcal H_2.
\]
The *conditional concentration operator* \(K_d=T_d/p_d\) has the following complete spectrum, including multiplicities. Put
\[
 a_d=1-\frac{4(d-2)}{\pi(d-1)}+\frac{6(d-2)}{\pi^2(d-1)},\quad
 b_d=1-\frac{2(d-4)}{\pi(d-1)}-\frac{12}{\pi^2(d-1)},\quad
 c_d=1+\frac4{\pi(d-1)}+\frac{12}{\pi^2(d-1)(d-3)},
\]
\[
 g_d=\frac{\sqrt{2(d-2)}}{\pi(d-1)},\qquad
 \ell_{d,\pm}=\frac{1+b_d\pm\sqrt{(1-b_d)^2+4g_d^2}}2.
\]
The eigenvalues and multiplicities are \(a_d\) (multiplicity \(1\)), \(\ell_{d,-}\) and \(\ell_{d,+}\) (multiplicity \(d-1\) each), and \(c_d\) (multiplicity \(d(d-3)/2\)). All are positive. Their exact ordering is
\[
\begin{array}{ll}
\ell_{d,-}<a_d<\ell_{d,+}<c_d,&d=4,6,8,10,\\
 a_d<\ell_{d,-}<\ell_{d,+}<c_d,&d=12,14,16,\ldots.
\end{array}
\]
Hence the sharp squared restriction condition number (largest eigenvalue divided by smallest) is
\[
\kappa_d=\begin{cases}c_d/\ell_{d,-},&d=4,6,8,10,\\c_d/a_d,&d\ge12\text{ even},\end{cases}
\qquad
\lim_{d\to\infty\atop d\text{ even}}\kappa_d=\frac1{1-4/\pi+6/\pi^2}=2.98786130147\ldots.
\]
These formulas also hold for complexifications of \(\mathcal H_2\). The actual eigenvalues of \(T_d\), rather than \(K_d\), are all multiplied by \(p_d\).

## Assumptions and scope
The sphere has normalized surface measure; boundaries of coordinate orthants have measure zero. Only pure degree-two harmonics are included, not constants or other degrees. Every \(d\ge4\) must be an even integer. The domain consists of exactly \(\binom d{d/2}\) orthants out of the \(2^d\) coordinate orthants. The condition number is a *squared* singular-value condition number of restriction \(f\mapsto f|_{\Omega_d}\), and is unchanged by the scalar normalization \(p_d\). No optimality is claimed among other observation regions.

## Proof
**1. Matrix model and normalization.** Every \(f\in\mathcal H_2\) is uniquely \(f_A(x)=x^\top A x\) for a real symmetric traceless \(d\)-by-\(d\) matrix \(A\). The uniform-sphere fourth moments imply
\[
\int_{\mathbb S^{d-1}}f_Af_B\,d\sigma=\frac{2\operatorname{tr}(AB)}{d(d+2)}.
\]
Thus a Frobenius-orthonormal basis of traceless symmetric matrices induces, after the common factor \(\sqrt{d(d+2)/2}\), an orthonormal harmonic basis. Conditional on \(\Omega_d\), write \(x_i=S_iR_i\). The sign vector \(S\) is uniform among the \(\binom d{d/2}\) vectors with exactly \(d/2\) positive entries; its magnitudes \(R_i=|x_i|\) are independent of \(S\) and retain the ordinary spherical law. Direct counting gives, for distinct indices,
\[
\mathbb E[S_iS_j]=-\frac1{d-1},\qquad
\mathbb E[S_iS_jS_kS_l]=\frac3{(d-1)(d-3)}.
\]
The independent magnitude moments needed below are
\[
\begin{split}
\mathbb E R_i^4&=\frac3{d(d+2)},\quad
\mathbb E R_i^2R_j^2=\frac1{d(d+2)},\\
\mathbb E R_i^3R_j&=\frac4{\pi d(d+2)},\quad
\mathbb E R_i^2R_jR_k=\frac2{\pi d(d+2)},\\
\mathbb E R_iR_jR_kR_l&=\frac4{\pi^2d(d+2)}.
\end{split}
\]
They follow by applying the Dirichlet \((1/2,\ldots,1/2)\) moment formula to \((R_i^2)\). Consequently, conditional concentration is a strictly positive quadratic form: a nonzero polynomial cannot vanish on the open union \(\Omega_d\).

**2. Four invariant spectral bands.** Split the Frobenius model into traceless diagonal matrices (dimension \(d-1\)) and off-diagonal symmetric matrices (dimension \(\binom d2\)). The diagonal-to-diagonal block is \(I\). Index the orthonormal off-diagonal basis by unordered pairs \(\{i,j\}\). Its Gram entries are \(1\) for the same edge, \(-2/[\pi(d-1)]\) for distinct edges sharing one index, and \(12/[\pi^2(d-1)(d-3)]\) for disjoint edges. In other words the block belongs to the three-dimensional Johnson-scheme algebra on two-subsets. The adjacency matrix of pairs sharing one endpoint has eigenvalues \(2(d-2),d-4,-2\), on sectors of dimensions \(1,d-1,d(d-3)/2\). The disjoint-edge adjacency eigenvalues on the same sectors are \((d-2)(d-3)/2,-(d-3),1\). The resulting off-diagonal eigenvalues are respectively \(a_d,b_d,c_d\).

The diagonal-to-edge cross block sends a traceless diagonal vector \((u_i)\) to the edge coordinates
\[
-\frac{\sqrt2}{\pi(d-1)}(u_i+u_j).
\]
On the standard \((d-1)\)-dimensional sector the incidence map \((u_i)\mapsto(u_i+u_j)_{i<j}\) has squared singular value \(d-2\). Therefore each standard sector contributes the matrix
\[
\begin{pmatrix}1&-g_d\\-g_d&b_d\end{pmatrix},
\]
whose eigenvalues are \(\ell_{d,\pm}\). The trivial and \((d-2,2)\) edge sectors have no diagonal partner, giving \(a_d,c_d\). The multiplicities sum to \(d(d+1)/2-1=\dim\mathcal H_2\), proving completeness.

**3. Exact extrema and the dimensional threshold.** Since \(b_d<1<c_d\) and \(g_d>0\), the standard-block eigenvalues satisfy \(\ell_{d,-}<1<\ell_{d,+}\). We also have \(0<a_d<1\). To compare the top sector, a direct factorization gives
\[
(c_d-1)(c_d-b_d)-g_d^2
=\frac{6(d-2)\left[\pi^2(d-3)^2+12\pi(d-3)+24\right]}{\pi^4(d-3)^2(d-1)^2}>0.
\]
Because \(c_d>\max(1,b_d)\), the shifted standard matrix \(c_dI-\begin{psmallmatrix}1&-g_d\\-g_d&b_d\end{psmallmatrix}\) is positive definite. Hence \(c_d>\ell_{d,+}\) for every admissible \(d\), and this is the strict global maximum.

Moreover \(b_d-a_d=2d(\pi-3)/[\pi^2(d-1)]>0\), and
\[
(1-a_d)(b_d-a_d)-g_d^2
=\frac{2(d-2)\left[d(4\pi^2-18\pi+18)-\pi^2\right]}{\pi^4(d-1)^2}.
\]
The sign of this determinant decides whether the smaller standard-block eigenvalue is below or above \(a_d\). The coefficient \(4\pi^2-18\pi+18\) is positive; the threshold \(d_*=\pi^2/(4\pi^2-18\pi+18)\) lies strictly between \(10\) and \(12\) (already the classical rational bounds \(223/71<\pi<22/7\) suffice). Thus precisely the four even dimensions \(4,6,8,10\) have \(\ell_{d,-}<a_d\), and every even \(d\ge12\) has the reverse inequality. This proves the claimed extrema and their multiplicities, with no equalities in integer dimensions.

**4. Limit.** As even \(d\to\infty\), \(a_d\to1-4/\pi+6/\pi^2\), \(c_d\to1\), \(b_d\to1-2/\pi\), and \(g_d\to0\). Since \(1-4/\pi+6/\pi^2<1-2/\pi\), the minimum eventually equals \(a_d\), giving the displayed limit. Stirling also yields \(p_d\sim\sqrt{2/(\pi d)}\); the normalized condition numbers remain bounded even though the unnormalized observed region has vanishing area fraction.

## Verification
Run `python CHECK.py` with `numpy` installed. The program builds a Frobenius-orthonormal basis of every pure quadratic harmonic space in dimensions \(4,6,8,10\), computes its restriction Gram matrix directly from enumerated balanced sign vectors and independent Dirichlet moments, and compares **all** eigenvalues, with multiplicities, against the formulas above. It checks positivity, the extremal ordering, and the crossover side, with maximum absolute spectral error below \(3\times10^{-15}\) across the tested dimensions. Symbolic determinants and the \(d\)-independent inequalities in the proof, not the finite tests, establish the theorem in all even dimensions.

## Relationship to prior work
The spherical Slepian framework of Simons, Dahlen and Wieczorek (2006) defines the corresponding concentration-operator question for arbitrary regions, but does not specify balanced sign-chamber masks. Jaming and Speckbacher (first public version 2020-04-06; Theorem 4.4) give general concentration bounds on compact two-point homogeneous spaces, not a complete exact spectrum for these regions. Aslam and Khalid (2020) construct spatial Slepian transforms and tight rotated families but do not classify this fixed-region trace-free-quadratic spectrum. A previously published positive-single-orthant degree-two result concerns one orthant, while the present mask is an equal union of all middle-sign-count orthants; its sign correlations and its finite-dimensional crossover are different. General Johnson association-scheme formulas are used as established tools, not claimed as new. Priority for this specific balanced-orthant formula is provisional pending wider historical comparison of harmonic moment and association-scheme treatments.

## Limitations
The finding covers only pure degree two, even dimensions at least four, and the exactly balanced sign-count mask. It does not assert a uniform lower bound for the *unnormalized* restriction energies: each eigenvalue of \(T_d\) is \(p_d\) times its conditional counterpart and \(p_d\to0\). No minimax optimality among arbitrary spherical sampling regions is asserted. The high-dimensional assertion is a limit, not an exact finite-dimensional equality. The external literature review did not exhaust all older harmonic design and association-scheme literature, and the available summaries of some similar mathematical records do not replace full-text inspection.

## References
- P. Jaming and M. Speckbacher, *Concentration estimates for finite expansions of spherical harmonics on two-point homogeneous spaces via the large sieve principle*, arXiv:2004.02474v1 (first submitted 2020-04-06), especially Theorems 4.2 and 4.4; https://arxiv.org/abs/2004.02474 .
- A. Aslam and Z. Khalid, *Spatial-Slepian Transform on the Sphere*, arXiv:2010.07266v1 (2020-10-14); https://arxiv.org/abs/2010.07266 .
- F. J. Simons, F. A. Dahlen and M. A. Wieczorek, *Spatiospectral Concentration on a Sphere*, SIAM Review **48** (2006), 504–536, DOI:10.1137/S0036144504445765.
