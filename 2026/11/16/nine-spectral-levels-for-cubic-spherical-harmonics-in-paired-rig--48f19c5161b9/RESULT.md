# Nine spectral levels for cubic spherical harmonics in paired right-angle lunes

## Finding
Let \(d\ge4\) be an integer, let \(S^{d-1}\subset\mathbb R^d\) carry probability-normalized surface measure, and let \(\mathcal H_3(d)\) denote complex restrictions of homogeneous harmonic polynomials of degree three. Observe on the two-antipodal-lune set
\[
\Omega_d=\{x\in S^{d-1}:x_1^2>x_2^2\}.
\]
The energy-concentration operator \(T_d=P_{\mathcal H_3}\mathbf1_{\Omega_d}|_{\mathcal H_3}\) has exactly **nine distinct eigenvalues**. Put
\[
R_d=\sqrt{\frac{7d+2}{d+2}},\quad
A_d=\frac{R_d+1}{3\pi},\quad B=\frac1\pi,\quad
C_d=\frac1\pi\sqrt{\frac d{d+2}},\quad
E_d=\frac{R_d-1}{3\pi}.
\]
Its complete spectrum, counting complex dimensions, is

| Eigenvalue | Multiplicity |
|---|---:|
| \(\tfrac12+A_d\), \(\tfrac12-A_d\) | \(1\) each |
| \(\tfrac12+B\), \(\tfrac12-B\) | \(d(d-3)/2\) each |
| \(\tfrac12+C_d\), \(\tfrac12-C_d\) | \(d-2\) each |
| \(\tfrac12+E_d\), \(\tfrac12-E_d\) | \(1\) each |
| \(\tfrac12\) | \(\binom{d}{3}\) |

For all such \(d\), \(A_d>B>C_d>E_d>0\). In particular, the largest and smallest eigenvalues are simple and the exact sharp energy condition number is
\[
\kappa_d=\frac{\tfrac12+A_d}{\tfrac12-A_d}.
\]
It increases strictly with \(d\) and tends to
\[
\frac{3\pi+2(\sqrt7+1)}{3\pi-2(\sqrt7+1)}=7.835969544162982\ldots.
\]
Consequently a complete degree-three eigenspace, whose dimension is \(d(d-1)(d+4)/6\), has a dimension-independent stable restriction to a disconnected region covering exactly half of the sphere. Exactly \(\binom{d}{3}\) independent modes always retain precisely half their energy.

## Assumptions and scope
The spherical dimension is arbitrary but \(d\ge4\). The observation set is an open inequality only to avoid boundary ambiguity; replacing it by \(x_1^2\ge x_2^2\) does not alter the operator. No measure is renormalized after restricting: eigenvalues are fractions of full-sphere energy, rather than conditional regional averages. Statements concern the *pure* homogeneous cubic harmonic eigenspace, not the full degree-at-most-three band. All multiplicities are over \(\mathbb C\). Both matching and nonmatching complex-valued harmonics are included.

## Proof
Write \(m=d-2\ge2\), \(z=x_1+ix_2=re^{i\theta}\), \(s=r^2\), and \(y=(x_3,\ldots,x_d)\), so that \(|y|^2=1-s\) on the unit sphere. The angular coordinate \(\theta\) is uniform on \([0,2\pi)\); independently \(s\) has \(\operatorname{Beta}(1,m/2)\) distribution, and the direction \(y/|y|\) is uniform on \(S^{m-1}\). These assertions follow by writing a standard \(d\)-dimensional Gaussian as its first two and remaining \(m\) coordinates and dividing by its norm.

For each \(j\), let \(\mathcal H_j(m)\) be the harmonics of degree \(j\) in the transverse variables. Separation of the degree-three Laplace equation gives an exhaustive orthogonal splitting into four types (each line is multiplied by all members of the corresponding transverse harmonic space):

- Transverse degree \(0\): \(z^3,\bar z^3,z(s-4|y|^2/m),\bar z(s-4|y|^2/m)\).
- Transverse degree \(1\): \(Y_1(y)z^2,Y_1(y)\bar z^2,Y_1(y)(s-2|y|^2/(m+2))\).
- Transverse degree \(2\): \(Y_2(y)z,Y_2(y)\bar z\).
- Transverse degree \(3\): \(Y_3(y)\).

Here polynomial variables are interpreted in the ambient \(\mathbb R^d\) before restricting to the sphere. Each polynomial is harmonic: for instance \(\Delta(zs)=8z\) and \(\Delta(z|y|^2)=2mz\), while \(\Delta(Y_1s)=4Y_1\) and \(\Delta(Y_1|y|^2)=2(m+2)Y_1\). All products of harmonics in disjoint variable sets remain harmonic. Angular and transverse-harmonic orthogonality makes the displayed summands mutually orthogonal. Their dimensions sum to
\[
4+3m+2\dim\mathcal H_2(m)+\dim\mathcal H_3(m)
=\frac{d(d-1)(d+4)}6=\dim\mathcal H_3(d),
\]
so the decomposition is complete.

Let \(h(\theta)=\operatorname{sgn}(\cos2\theta)\). Almost everywhere, \(\mathbf1_{\Omega_d}=(1+h)/2\). Its relevant angular Fourier coefficients are
\[
\widehat h(0)=0,\qquad \widehat h(\pm2)=\frac2\pi,\quad
\widehat h(\pm4)=0,\quad \widehat h(\pm6)=-\frac2{3\pi}.
\]
Only angular differences through six are possible in the above cubic basis; no higher coefficients enter. Therefore \(T_d=\tfrac12I+\pi^{-1}K\), where \(K\) splits into the following small self-adjoint matrices.

For transverse degree zero, choose normalized angular order \((-3,-1,1,3)\). The respective radial factors are \(s^{3/2}\) and \(s^{1/2}(s-4/(m+4))\). Their normalized radial correlation is positive and obeys
\[
\eta_0^2=\frac{m}{3(m+4)}=\frac{d-2}{3(d+2)}.
\]
The block is
\[
K_0=\begin{pmatrix}
0&\eta_0&0&-1/3\\
\eta_0&0&1&0\\
0&1&0&\eta_0\\
-1/3&0&\eta_0&0
\end{pmatrix}.
\]
Its reversal-even and reversal-odd two-dimensional subspaces show that its eigenvalues are
\[
\pm\frac{R_d+1}{3},\qquad \pm\frac{R_d-1}{3}.
\]

For each transverse linear harmonic, the normalized angular order \((0,-2,2)\) has radial factors \((1-s)^{1/2}(s-2/(m+4))\) and \((1-s)^{1/2}s\). Their positive normalized radial correlation satisfies
\[
\eta_1^2=\frac{m+2}{2(m+4)}=\frac{d}{2(d+2)}.
\]
The corresponding block and its eigenvalues are
\[
K_1=\begin{pmatrix}0&\eta_1&\eta_1\\\eta_1&0&0\\\eta_1&0&0\end{pmatrix},
\qquad \operatorname{Spec}(K_1)=\{0,\pm\sqrt{d/(d+2)}\}.
\]
Each transverse degree-two harmonic yields \(K_2=\begin{pmatrix}0&1\\1&0\end{pmatrix}\), with eigenvalues \(\pm1\); each transverse degree-three harmonic yields the scalar zero block. These statements use angular orthogonality and the fact that the two radial functions in the degree-two sector are identical.

For completeness, both radial correlations are exact elementary beta-moment identities. If \(\mathbb E[s^j]=j!/(1+m/2)_j\), with \((a)_j\) the rising factorial, then \(\eta_0\) is the correlation of \(s^{3/2}\) and \(s^{1/2}(s-4/(m+4))\). Likewise \(\eta_1\) is the correlation of \((1-s)^{1/2}s\) and \((1-s)^{1/2}(s-2/(m+4))\). Substitution, cancellation, and positivity give the displayed squares; `verification/symbolic_check.py` reconstructs both identities exactly.

The transverse harmonic dimensions are \(\dim\mathcal H_1(m)=m\), \(\dim\mathcal H_2(m)=(m+2)(m-1)/2\), and \(\dim\mathcal H_3(m)=m(m-1)(m+4)/6\). Thus the \(K_1\) zero modes plus \(K_3\) zero modes have dimension
\[
m+\frac{m(m-1)(m+4)}6=\binom{d}{3}.
\]
All remaining eigenvalues and multiplicities follow by applying \(\tfrac12+\pi^{-1}(\cdot)\) to these blocks. The strict ordering is elementary: \(R_d>2\) for \(d>2\) implies \(A_d>1/\pi\); \(1>\sqrt{d/(d+2)}\); and \(E_d<(\sqrt7-1)/(3\pi)<\sqrt{3/5}/\pi\le C_d\). Finally \(R_d^2=7-12/(d+2)\) grows strictly and remains below seven. This proves both sharp norm bounds and the claimed monotone finite limit. No finite-dimensional numerical observation is used to justify any universal quantifier.

## Verification
Run from this directory with Python 3 and the indicated open-source packages:

```bash
python verification/symbolic_check.py
python verification/gram_check.py
```

The symbolic checker requires SymPy. It verifies both beta-moment normalization identities, the exact four-by-four characteristic polynomial, total multiplicity and the essential strict inequality. The Gram checker requires NumPy and SciPy. It independently builds the full degree-three harmonic space as the image of the exact harmonic projection \(P\mapsto P-|x|^2\Delta P/(2(d+2))\), computes all full and masked monomial moments from beta and incomplete-beta integrals, and diagonalizes the resulting full-size generalized Gram problem for dimensions \(3\) through \(8\). The dimension-three numerical comparison is a boundary consistency check, not part of the new theorem. Each tested maximum eigenvalue difference is below \(4\times10^{-15}\). These computations are independent finite checks of the symbolic proof, not substitutes for its all-dimensional argument.

## Relationship to prior work
Classical spherical Slepian theory sets up concentration as a finite spectral-domain eigenproblem on arbitrary observation regions, but its evaluated examples emphasize the two-sphere and axisymmetric caps [1]. Michel–Plattner–Seibert [2] give a unified scalar/vector/tensor formulation and commuting operators for spherical caps, again on the two-sphere, without the present all-dimensional paired-lune block reduction or exact cubic spectral values. A distinct earlier calculation on the ordinary two-sphere gives the complete pure cubic spectrum for a single right-angle quarter-lune. By antipodal symmetry, doubling its spectrum gives the present formula when \(d=3\), so **that case is deliberately excluded**. The general-dimensional quadratic-lune results and all-dimensional cubic antipodal-*cap* results consider different degrees or differently shaped masks, and do not entail the current nine-level cubic paired-lune statement. The prior general eigenproblem alone does not evaluate these four blocks. Known spherical-harmonic decompositions and beta moments are used as standard ingredients, not claimed as new.

## Limitations
The result covers only pure cubic harmonics, this exactly specified two-antipodal-lune observation set, and integer dimensions at least four. It does not classify arbitrary lune apertures, arbitrary angular masks, mixed-degree low-pass spaces or independently verified scientific priority. General multidegree Slepian methods may calculate such spectra numerically without these closed formulas. Unindexed or inaccessible equivalent earlier calculations cannot be excluded by a finite search. The supplied checkers verify small dimensions and exact algebraic identities but do not constitute a separate human or independent mathematical audit.

## References
1. F. J. Simons, F. A. Dahlen, M. A. Wieczorek, *Spatiospectral concentration on a sphere*, SIAM Review (2006), first preprint 2004-08-31, https://arxiv.org/abs/math/0408424.
2. V. Michel, A. Plattner, K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, first public version 2021-03-26, https://arxiv.org/abs/2103.14650.
3. P. J. Roddy, J. D. McEwen, *Slepian Scale-Discretised Wavelets on the Sphere*, first public version 2021-06-03, https://arxiv.org/abs/2106.02023.
4. A. Zandieh, I. Han, H. Avron, *Near Optimal Reconstruction of Spherical Harmonic Expansions*, first public version 2022-02-25, https://arxiv.org/abs/2202.12995.
