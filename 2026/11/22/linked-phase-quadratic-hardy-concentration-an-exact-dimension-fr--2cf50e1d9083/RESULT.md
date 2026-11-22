# Linked-phase quadratic Hardy concentration: an exact dimension-free spectrum

## Finding
For every integer \(d\ge3\), write \(\sigma\) for Haar probability measure on \(S^{2d-1}\subset\mathbb C^d\). The exact-degree-two holomorphic space \(\mathcal H_{2,d}\) is equipped with its full-sphere \(L^2(\sigma)\) norm. Consider the simultaneous phase-alignment cell
\[
\Omega_d=\{z:\operatorname{Re}(z_1\overline{z_2})>0,\quad\operatorname{Re}(z_1\overline{z_3})>0\}.
\]
For the restriction Gram operator \(T\) determined by \(\langle Tf,g\rangle=\int_{\Omega_d}f\overline g\,d\sigma\), the *complete* spectrum is as follows. The six eigenvalues of \(B_2\) below occur once each; the three eigenvalues of \(B_1\) occur \(d-3\) times each; \(1/4\) occurs \((d-3)(d-2)/2\) times. Zero multiplicities are omitted when \(d=3\). The dimensions sum to \(d(d+1)/2\).

In the normalized monomial ordering \(z_1^2,z_1z_3,z_3^2,z_1z_2,z_2z_3,z_2^2\), each monomial individually normalized in \(L^2(S^{2d-1})\), the first block is
\[
B_2=\begin{pmatrix}
\frac14&a&0&a&b&0\\
a&\frac14&a&c&\frac18&0\\
0&a&\frac14&0&e&0\\
a&c&0&\frac14&\frac18&a\\
b&\frac18&e&\frac18&\frac14&e\\
0&0&0&a&e&\frac14
\end{pmatrix},\quad
 a=\frac{3\sqrt2}{32},\quad b=\frac{\sqrt2}{8\pi},\quad c=\frac1{4\pi},\quad e=\frac{3\sqrt2}{16\pi}.
\]
The first-degree internal block, in the normalized ordering \(z_1,z_3,z_2\), is
\[
 B_1=\begin{pmatrix}\frac14&\frac18&\frac18\\\frac18&\frac14&\frac1{4\pi}\\\frac18&\frac1{4\pi}&\frac14\end{pmatrix}.
\]
The coordinate swap \(z_2\leftrightarrow z_3\) reduces \(B_2\) to a symmetric \(4\times4\) block and an antisymmetric \(2\times2\) block:
\[
B_+=\begin{pmatrix}
\frac14&\frac3{16}&0&\frac{\sqrt2}{8\pi}\\
\frac3{16}&\frac14+\frac1{4\pi}&\frac{3\sqrt2}{32}&\frac{\sqrt2}8\\
0&\frac{3\sqrt2}{32}&\frac14&\frac3{8\pi}\\
\frac{\sqrt2}{8\pi}&\frac{\sqrt2}8&\frac3{8\pi}&\frac14
\end{pmatrix},\quad
B_-=\begin{pmatrix}\frac14-\frac1{4\pi}&\frac{3\sqrt2}{32}\\\frac{3\sqrt2}{32}&\frac14\end{pmatrix}.
\]
The quartic eigenvalues (the roots of \(\det(tI-B_+)\)) lie, one each, in the **rigorously certified** rational intervals \((0.049,0.050)\), \((0.119,0.121)\), \((0.271,0.273)\), \((0.638,0.640)\). The two eigenvalues of \(B_-\) lie in \((0.071,0.073)\), \((0.348,0.350)\). The three eigenvalues of \(B_1\) are
\[
\frac14-\frac1{4\pi},\qquad\frac{1+2\pi\pm\sqrt{1+2\pi^2}}{8\pi}.
\]
Consequently, the sharp extrema belong to \(B_+\), and the sharp squared condition number of restriction is exactly \(\kappa=\lambda_{\max}(B_+)/\lambda_{\min}(B_+)\approx13.0302552642263\), independent of \(d\).

## Assumptions and scope
Coordinates have the complex Hermitian norm and the sign inequalities hold almost everywhere; phase angles on coordinate-zero sets are immaterial. The harmonics are **holomorphic homogeneous quadratics**, not real spherical harmonics of total degree two. The measure is normalized to total mass one. The operator eigenvalues measure fractions of full-space squared \(L^2\)-energy; \(\kappa\) is therefore the ratio of extreme **squared** singular values, not the ratio of unsquared singular values. No assertion is made for weighted measures, other phase apertures, or polynomial degrees other than two.

## Proof
The normalized monomial basis is \(e_\alpha(z)=\sqrt{(d)_2/\alpha!}\,z^\alpha\), where \((d)_2=d(d+1)\) and \(|\alpha|=2\). Write \(c(0)=1/2\) and \(c(j)=\sin(\pi j/2)/(\pi j)\) for nonzero integers. Decompose complex Gaussian vectors into independent coordinate phases and radii; division by their common norm produces Haar measure on the sphere. Dirichlet moments then show that, for equal outside multi-indices \(\alpha_{4:d}=\beta_{4:d}\),
\[
\langle Te_\alpha,e_\beta\rangle
=c(\alpha_2-\beta_2)c(\alpha_3-\beta_3)
\prod_{j=1}^d\frac{\Gamma(1+(\alpha_j+\beta_j)/2)}{\sqrt{\alpha_j!\beta_j!}}.
\]
For unequal outside multi-indices the entry vanishes by integration over a free outside phase. The phase variables \(\arg z_1-\arg z_2\) and \(\arg z_1-\arg z_3\) are independent uniform angles, explaining the product of the two Fourier coefficients. The ratio of radial moments cancels all factors involving the ambient dimension. By grouping basis monomials according to their exponents in coordinates four through \(d\), the only possible internal total degrees are \(2,1,0\). The corresponding matrices are \(B_2,B_1,(1/4)\); their multiplicities are respectively \(1,d-3,\binom{d-2}{2}\). Direct substitution in the displayed moment formula gives every block entry.

The involution swapping coordinates two and three commutes with the restriction operator. On the six-dimensional internal quadratic sector, its eigenspaces have dimensions four and two. Orthogonal combinations of the six normalized monomials yield exactly \(B_+\oplus B_-\). Their characteristic polynomials are computed symbolically in the supplementary checker; an exact rational interval computation uses Machin's alternating-series enclosure of \(\pi\) and sign changes at the stated endpoints. Four disjoint intervals for the quartic and two for the quadratic exhaust their degrees and prove distinctness, positivity and strict separation.

For completeness, these six values contain both *global* extremes. The nonnegative irreducible \(B_1\) has largest row sum \(1/2\), with some smaller row sums, so Perron–Frobenius gives \(\lambda_{\max}(B_1)<1/2\). Its three explicit eigenvalues are all greater than \(1/16\); for the smaller radical eigenvalue this follows by squaring \(2+3\pi>2\sqrt{1+2\pi^2}\). The \(3\times3\) principal submatrix of \(B_2\) on \(z_1^2,z_1z_3,z_3^2\) has least eigenvalue \(1/16\), so \(\lambda_{\min}(B_2)\le1/16\). A Rayleigh quotient on the sum of normalized modes indexed \(1,2,4,5\) (one-based) of \(B_2\) exceeds \(1/2\), so \(\lambda_{\max}(B_2)>1/2\). The scalar block is \(1/4\). The certified spectral intervals place both \(B_2\) extrema in \(B_+\), proving their simplicity and the exact sharp quotient.

## Verification
The standalone program `check.py` reproduces symbolic orthogonal block diagonalization, characteristic factorization, complete matrix construction in dimensions \(3,4,5,8\), and a certified root-isolation test. The root test encloses \(\pi\) via Machin's identity and alternating rational arctangent partial sums, then performs exact rational interval arithmetic at all endpoints. An independent Gaussian-sphere simulation with a fixed seed and \(350000\) samples compares the original *geometric mask* against the derived six-dimensional block, with maximum observed matrix discrepancy less than \(0.0014\) (a numerical check, not part of the proof). All computations were run from the supplied program in the present analysis. The proof itself is the integral identity, symmetry reduction and exact interval argument, not the simulation.

## Relationship to prior work
The study is motivated by finite-degree compressions of angular Toeplitz symbols in holomorphic spaces. Quiroga-Barranco (first public version June 3, 2021) gives general representation-theoretic invariant-block machinery on weighted Bergman spaces (not this evaluated simultaneous-relative-phase quadratic concentration). Bauer–Hagger–Vasilevski (first public August 30, 2018) analyze structured operator algebras on complex balls, rather than this explicit six-root linked-phase restriction. Published single-relative-phase wedge spectra have different angular symbols; real-sphere quarter-wedge calculations concern a different polynomial representation. General monomial integral methods can underlie this calculation, but they do not themselves state the numerical exact root ordering, all multiplicities, or sharp dimension-free stability constant.

## Limitations
The exact result is restricted to degree two, to two right-half-plane relative-phase comparisons sharing the first coordinate, and to unweighted Haar probability measure. All eigenvalues are exact roots of explicitly displayed matrices, but the four eigenvalues of \(B_+\) are not given as unwieldy quartic radicals. This is a same-author mathematical verification, not independent certification. Related generic Toeplitz results might permit a derivation of this special case, and unindexed equivalent literature remains a priority risk.

## References
1. R. Quiroga-Barranco, *Toeplitz operators, \(\mathbb T^m\)-invariance and quasi-homogeneous symbols*, arXiv:2106.01980, first posted June 3, 2021, https://arxiv.org/abs/2106.01980. Relevant full preprint: Introduction and Proposition 4.10.
2. W. Bauer, R. Hagger, N. Vasilevski, *Algebras of Toeplitz operators on the \(n\)-dimensional unit ball*, arXiv:1808.10372, first posted August 30, 2018, https://arxiv.org/html/1808.10372v1. Inspected Introduction, Sections 2–3, and stated operator-algebra objectives.
3. Standard Gaussian–Dirichlet moment formula and Machin identity; the calculations used in this finding are fully supplied and reproducible in `check.py`.
