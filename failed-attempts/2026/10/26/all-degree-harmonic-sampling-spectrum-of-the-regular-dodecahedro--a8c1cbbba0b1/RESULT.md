# All-degree harmonic sampling spectrum of the regular dodecahedron

## Finding

Let \(X\subset S^2\) be the twenty vertices of a regular dodecahedron centered at the origin. For every integer \(\ell\ge0\), let \(P_\ell\) be the Legendre polynomial with \(P_\ell(1)=1\), and form the \(20\)-by-\(20\) matrix
\[
G_\ell=\bigl[P_\ell(\langle x,y\rangle)\bigr]_{x,y\in X}.
\]
Write \(u_\ell=P_\ell(1/3)\) and \(v_\ell=P_\ell(\sqrt5/3)\). If \(\ell\) is even, the ten potentially nonzero eigenvalues of \(G_\ell\), with multiplicities, are
\[
2(1+6u_\ell+3v_\ell)\ (1),\quad
2(1+u_\ell-2v_\ell)\ (4),\quad
2(1-2u_\ell+v_\ell)\ (5).
\]
If \(\ell\) is odd, they are
\[
2(1-3u_\ell)\ (4),\quad
2(1+2u_\ell-\sqrt5v_\ell)\ (3),\quad
2(1+2u_\ell+\sqrt5v_\ell)\ (3).
\]
In either case the other ten eigenvalues of the full matrix are zero, because of antipodal parity. The displayed eigenvalues are nonnegative at every degree. Their complete rank classification is
\[
\operatorname{rank}G_\ell=
\begin{cases}
1,&\ell=0,\\
3,&\ell=1,\\
5,&\ell=2,\\
7,&\ell=3,\\
9,&\ell\in\{4,8,14\},\\
6,&\ell=5,\\
10,&\text{otherwise}.
\end{cases}
\]
Consequently, every exact-degree spherical-harmonic sampling map onto the ten-dimensional antipodally compatible data sector is surjective for \(\ell\ge15\), and degree \(15\) is the sharp *persistent* threshold. The nine-dimensional rank at degree \(14\) shows that a mere dimension count is insufficient.

## Assumptions and scope

The vertex set may be rotated or reflected without changing the assertion. One concrete unit-sphere realization is obtained by dividing all coordinates below by \(\sqrt3\): the eight triples \((\pm1,\pm1,\pm1)\), and the twelve triples
\[
(0,\pm\varphi^{-1},\pm\varphi),\quad
(\pm\varphi^{-1},\pm\varphi,0),\quad
(\pm\varphi,0,\pm\varphi^{-1}),\qquad
\varphi=(1+\sqrt5)/2.
\]
The signs within each displayed family are independent. The matrix \(G_\ell\) uses the unweighted Legendre Gram normalization, not an orthonormal harmonic-evaluation normalization. If \(\mathcal H_\ell\) has the probability-surface-measure \(L^2\) inner product, and \(E_\ell f=(f(x)/\sqrt{20})_{x\in X}\), the addition theorem gives
\[
E_\ell E_\ell^*=\frac{2\ell+1}{20}\,G_\ell.
\]
Hence the squared nonzero singular values of \(E_\ell\) are exactly the displayed eigenvalues multiplied by \((2\ell+1)/20\). Nothing is asserted about simultaneous interpolation across different degrees or uniqueness of the input harmonic.

## Proof

**1. Ten antipodal pairs and two inner-product distances.** Select one representative \(z_i\) of each of the ten antipodal pairs, using the representative whose first nonzero coordinate is positive, for \(1\le i\le10\). Direct substitution in the displayed coordinates shows that for \(i\ne j\),
\[
\langle z_i,z_j\rangle\in\{\pm1/3,\ \pm\sqrt5/3\}.
\]
Each representative has six others at absolute inner product \(1/3\) and three at absolute inner product \(\sqrt5/3\). Define two symmetric unsigned zero-diagonal integer matrices \(A_u,A_v\), indicating those two absolute inner products; and the signed matrices \(B_u,B_v\), whose nonzero entries are respectively the signs of the inner products. The following identities follow by multiplying the explicit integer matrices (the included independent standard-library checker reconstructs all ten representatives and verifies every entry):
\[
A_u=J-I-A_v,\qquad A_v^2=2I-A_v+J,
\]
\[
B_u^2=6I-B_u,\qquad B_uB_v=2B_v,\qquad B_v^2=B_u+3I.
\]
Here \(I\) is the ten-by-ten identity and \(J\) is the all-ones matrix. Their truth is also checked directly by counting common representatives in the two angle classes. In particular, \(A_v\) is the adjacency matrix of the Petersen graph on the ten threefold symmetry axes, but this graph identification is not needed for the verification.

**2. Parity block diagonalization.** After arranging the twenty sites as \((z_1,\ldots,z_{10},-z_1,\ldots,-z_{10})\), the identity \(P_\ell(-t)=(-1)^\ell P_\ell(t)\) shows that the antipodally incompatible ten-dimensional subspace is in the kernel of \(G_\ell\). On the compatible subspace its matrix, after an isometric change of basis, is
\[
2(I+u_\ell A_u+v_\ell A_v)\quad(\ell\text{ even}),\qquad
2(I+u_\ell B_u+v_\ell B_v)\quad(\ell\text{ odd}).
\]
The first set of identities implies that \(A_v\) has eigenvalues \(3,1,-2\) with multiplicities \(1,5,4\) (use \(A_v\mathbf1=3\mathbf1\), the quadratic relation on \(\mathbf1^\perp\), and \(\operatorname{tr}A_v=0\)). The relation \(A_u=J-I-A_v\) yields the three even-degree branches in the finding.

For the signed matrices, \(B_u^2=6I-B_u\), \(\operatorname{tr}B_u=0\), and dimension ten force eigenvalues \(2\) (multiplicity six) and \(-3\) (multiplicity four). The identity \(B_v^2=B_u+3I\) makes \(B_v\) zero on the latter four-dimensional space and gives eigenvalues \(\pm\sqrt5\) on the former six-dimensional space. Since \(\operatorname{tr}B_v=0\), the two nonzero eigenvalues have multiplicity three each. The remaining identity \(B_uB_v=2B_v\) gives the three odd-degree branches. This proves the spectral formulas exactly, including all multiplicities.

**3. A uniform analytic cutoff.** For \(|t|<1\), the Laplace integral for the Legendre polynomial is
\[
P_\ell(t)=\frac1\pi\int_0^\pi
\bigl(t+i\sqrt{1-t^2}\cos s\bigr)^\ell\,ds.
\]
For every integer \(\ell\ge1\), taking absolute values, using \((1-z)^{\ell/2}\le e^{-\ell z/2}\) and \(\sin s\ge2s/\pi\) on \([0,\pi/2]\), then extending a Gaussian integral to infinity, gives
\[
|P_\ell(t)|\le\sqrt{\frac{\pi}{2\ell(1-t^2)}}.
\]
Thus
\[
|u_\ell|\le\frac{3\sqrt\pi}{4\sqrt\ell},\qquad
|v_\ell|\le\frac{3\sqrt\pi}{\sqrt{8\ell}}.
\]
The absolute departure of each one of the six possible unscaled eigenvalue branches from \(1\) is bounded by
\[
\Delta_\ell=\sqrt{\frac\pi\ell}\left(\frac92+\frac9{\sqrt8}\right).
\]
Indeed this controls all even branches, and also exceeds the odd coefficients \(3|u_\ell|\) and \(2|u_\ell|+\sqrt5|v_\ell|\). Using the elementary rational estimates \(\pi<22/7\) and \(\sqrt8>707/250\), one checks \(\Delta_\ell<1\) for every \(\ell\ge186\). Hence the ten parity-compatible eigenvalues are strictly positive for **all** degrees at least \(186\).

**4. Exact finite calculation.** At the remaining \(186\) degrees \(0\le\ell\le185\), there is no floating-point step. Both \(P_\ell(1/3)\) and, according to parity, \(P_\ell(\sqrt5/3)\) or \(\sqrt5P_\ell(\sqrt5/3)\) are rational. Starting from \(P_0(t)=1\), \(P_1(t)=t\), the exact recurrence
\[
(\ell+1)P_{\ell+1}(t)=(2\ell+1)tP_\ell(t)-\ell P_{\ell-1}(t)
\]
produces rational coefficients in \(\mathbb Q(\sqrt5)\). Evaluating the six explicit eigenvalue formulas with integer-fraction arithmetic establishes nonnegativity and precisely the finite list of deficient ranks
\[
(\ell,\operatorname{rank}G_\ell)=
(0,1),(1,3),(2,5),(3,7),(4,9),(5,6),(8,9),(14,9).
\]
All other degrees through \(185\) have rank ten. Combining with Step 3 completes the all-degree theorem. The file `verify_dodecahedron.py` contains the coordinate reconstruction, exact integer matrix identities, exact fraction recurrences, all finite sign assertions, and a rational tail-bound check; it runs without third-party packages.

## Verification

Run `python3 verify_dodecahedron.py` in the same directory as this document. The program reconstructs the two unsigned and two signed angle matrices from the exact twenty-vertex coordinates, checks every matrix identity, and evaluates the eigenvalue signs and ranks for every integer \(0\le\ell\le185\) over \(\mathbb Q(\sqrt5)\). It checks the displayed exceptional-rank list, then independently bounds the infinite tail by the strict rational inequality
\[
\frac{22}{7}\left(\frac92+\frac{2250}{707}\right)^2<186.
\]
The checker prints `ALL_CHECKS_PASS` on success. The finite test is exhaustive **only for those 186 degrees**; the proof for all larger degrees is the analytic estimate in Step 3. Numerically the least positive unscaled branch among these finite degrees is approximately \(0.0019406356177512336\), at degree \(13\), but this decimal is illustrative and not used in any proof.

## Relationship to prior work

The harmonic addition theorem and spherical-design/association-scheme ideas are classical; the rank problem is motivated by their application to exact-degree spherical sampling. Cohan's 1958 treatment of icosahedral-group spherical harmonics explicitly reports representation expansions through degree \(14\), with one additional symmetric degree; its accessible abstract/extract does not give the above all-degree dodecahedral evaluation spectrum, although the unavailable complete paper remains an originality risk. Hitchin's public June 2007 preprint studies nodal sets of degree-three harmonics containing icosahedron vertices, not sampling all degrees at the vertices of the dual dodecahedron. Bilbao-Ahedo and collaborators study covariance ranks for several spherical pixelizations, especially icosahedral meshes and sums over degrees, not this exact-degree dodecahedral spectrum. An earlier exact-degree *icosahedral* vertex-sampling result has a different twelve-point Gram spectrum and does not logically imply the twenty-point dodecahedral Gram formulas.

## Limitations

Only the regular dodecahedron on the ordinary unit two-sphere is classified, and only one harmonic degree at a time. The parity-incompatible half of the twenty sample coordinates is necessarily inaccessible from any fixed degree. No claim is made of a universal frame optimum, novel representation theory of the icosahedral group, or a complete historical uniqueness search. One closely related 1958 paper was accessible only by its original publisher extract; comparison with its entire text remains a residual literature risk. No independent mathematical validation has been performed.

## References

1. N. V. Cohan, “The spherical harmonics with the symmetry of the icosahedral group,” *Mathematical Proceedings of the Cambridge Philosophical Society* **54** (1958), 28–38. DOI: 10.1017/S0305004100033156. Publisher extract reports tabulations through degree \(14\).
2. N. Hitchin, “Spherical harmonics and the icosahedron,” arXiv:0706.0088v1, first public 2007-06-01. Relevant full-text discussion: §§1–3 and the explicit harmonic-cubic arguments.
3. P. Delsarte, J. M. Goethals, and J. J. Seidel, “Spherical codes and designs,” *Geometriae Dedicata* **6** (1977), 363–388. DOI: 10.1007/BF03187604.
4. J. D. Bilbao-Ahedo et al., “On the regularity of the covariance matrix of a discretized scalar field on the sphere,” arXiv:1701.06617, first publicly submitted 2017-01-23; see §§2–4 and §4.2.
