# Eccentric-perforation rigidity and a critical cusp in Bergman concentration

## Finding

Let \(A^2(\mathbb D)\) be the ordinary analytic Bergman space with norm \(\|f\|^2=\pi^{-1}\int_{\mathbb D}|f(z)|^2\,dA(z)\). For a measurable set \(\Omega\subset\mathbb D\), put \(T_\Omega=P(1_\Omega\cdot)\), where \(P\) is the Bergman projection, and write \(m(\Omega)=|\Omega|/\pi\). The constant function \(1\) has norm one and satisfies \(\langle T_\Omega1,1\rangle=m(\Omega)\); consequently \(\|T_\Omega\|\ge m(\Omega)\).

**Finite circular-perforation classification.** Let \(0<R<1\), and remove finitely many mutually disjoint open disks \(D(c_j,r_j)\), each of strictly positive radius and with closure contained in \(D(0,R)\). Then
\[
\left\|T_{D(0,R)\setminus\bigcup_jD(c_j,r_j)}\right\|=m\left(D(0,R)\setminus\bigcup_jD(c_j,r_j)\right)
\]
holds if and only if either there are no holes, or there is exactly one hole, it is centered at the origin, and \(r_1^2+R^2\le1\).

**Sharp eccentric stability and critical cusp.** For \(0<r<R<1\), \(|c|+r<R\), set \(\Omega_c=D(0,R)\setminus D(c,r)\), \(a=r^2\), \(b=R^2\), and \(m=b-a\). For every \(c\ne0\), \(\|T_{\Omega_c}\|>m\), with the explicit global bound
\[
\|T_{\Omega_c}\|\ge\frac{m+d(c)+\sqrt{(m-d(c))^2+8a^2|c|^2}}{2}>m,\qquad d(c)=b^2-a^2-2a|c|^2.
\]
When \(a+b<1\), this bound is asymptotically sharp, and
\[
\boxed{\|T_{\Omega_c}\|=m+\frac{2a^2}{m(1-a-b)}|c|^2+O_{a,b}(|c|^4)\quad(c\to0).}
\]
At the exact threshold \(a+b=1\), the growth changes to a cusp:
\[
\boxed{\|T_{\Omega_c}\|=m+\sqrt2\,a|c|+O_{a,b}(|c|^2)\quad(c\to0).}
\]
Thus moving a circular hole away from the origin immediately violates the area lower bound; its sharp local order changes from quadratic to linear precisely when the first two monomial concentration eigenvalues become degenerate.

## Assumptions and scope

All disks are Euclidean and open; sets differing by area-zero boundary circles define the same operator. The finitely many removed disks have pairwise disjoint interiors, positive radii, and lie strictly inside the fixed centered outer disk. The classification refers to \(A^2(\mathbb D)\), not to the Bergman space *of the perforated domain*. The local expansions require a fixed pair \(0<r<R<1\) and displacement tending to zero; the global lower bound holds for every legal displacement. No conclusion is asserted for arbitrary noncircular holes or arbitrary radial measurable sets.

## Proof

**1. Matrix entries and disk moments.** The normalized monomials \(e_n(z)=\sqrt{n+1}\,z^n\), \(n\ge0\), are an orthonormal basis. The mean-value property on a disk gives
\[
\frac1\pi\int_{D(c,r)}z^n\,dA(z)=r^2c^n\quad(n\ge0).
\]
Consequently, for the finite-hole domain,
\[
\langle T_\Omega e_n,e_0\rangle=-\sqrt{n+1}\sum_j r_j^2c_j^n\quad(n\ge1).
\]
For one hole, expanding \((u+c)^n(\bar u+\bar c)^\ell\) on \(|u|<r\) gives the exact matrix formula
\[
\langle T_{\Omega_c}e_n,e_\ell\rangle=
\delta_{n\ell}b^{n+1}-\sqrt{(n+1)(\ell+1)}
\sum_{k=0}^{\min(n,\ell)}\binom nk\binom\ell k
\frac{a^{k+1}}{k+1}c^{n-k}\bar c^{\ell-k}.
\tag{1}
\]
These are identities, not approximations. In particular the leading principal \(2\times2\) compression in \(\{1,\sqrt2z\}\) is
\[
\begin{pmatrix}m&-\sqrt2a\bar c\\-\sqrt2ac&d(c)\end{pmatrix},
\qquad d(c)=b^2-a^2-2a|c|^2.
\tag{2}
\]
Its larger eigenvalue is the displayed global lower bound. If \(c\ne0\), its off-diagonal is nonzero, and this eigenvalue strictly exceeds its first diagonal entry \(m\).

**2. Classification of finite circular perforations.** Suppose the norm equals \(m(\Omega)\). As \(T_\Omega\) is positive and \(\langle T_\Omega1,1\rangle=\|T_\Omega\|\), the equality case of the positive Rayleigh bound forces \(T_\Omega1=m(\Omega)1\). Thus all the nonconstant disk moments in step 1 vanish. Combine holes with the same nonzero center, writing their total strictly positive squared-radius weights as \(A_j\), with pairwise distinct nonzero centers \(d_j\). If there are \(q\) such centers, the identities for \(n=1,\dots,q\) read \(\sum_{j=1}^qA_jd_j^n=0\). The coefficient matrix is a Vandermonde matrix multiplied by the invertible diagonal \(\operatorname{diag}(d_j)\); hence each \(A_j=0\), a contradiction. All centers therefore equal zero, and disjointness allows at most one nonempty hole.

If no hole exists, disk concentration is diagonal with eigenvalues \(b^{n+1}\), so its norm is \(b=m(\Omega)\). If one central hole exists, the monomial eigenvalues are
\[
\lambda_n=b^{n+1}-a^{n+1}=m\,S_n,\qquad
S_n=\sum_{j=0}^{n}b^{n-j}a^j.
\]
Here \(S_0=1\), \(S_1=a+b\), and \(S_{n+1}=aS_n+b^{n+1}\le(a+b)S_n\). Thus \(a+b\le1\) implies \(S_n\le1\) for every \(n\); conversely \(a+b>1\) gives \(\lambda_1>\lambda_0\). This proves the if-and-only-if classification.

**3. The nondegenerate quadratic law.** Let \(a+b<1\). From the recurrence above, \(\lambda_0=m\) is a simple top eigenvalue, separated from the rest by the strictly positive gap
\[
\Delta=\lambda_0-\lambda_1=m(1-a-b).
\]
In a neighborhood of \(c=0\), equation (1), or the integral of rank-one Bergman kernel evaluations over a translated compact disk, gives a real-analytic family in trace norm. Hence the isolated top eigenvalue has the usual convergent perturbation expansion. For real \(c=t\), the diagonal \(\langle T_{\Omega_t}e_0,e_0\rangle=m\) is constant, while the first derivative of \(T_{\Omega_t}e_0\) has only one nonzero excited-mode component, \(-\sqrt2a e_1\). The second-order simple-eigenvalue formula therefore gives exactly \(2a^2/\Delta\) as the coefficient of \(t^2\). Rotational unitary equivalence makes the norm a function of \(|c|\), and analyticity makes its expansion in a real displacement even; the remainder is \(O(|c|^4)\).

**4. The degenerate cusp.** If \(a+b=1\), then \(\lambda_0=\lambda_1=m\), but \(\lambda_2=m(1-ab)<m\) and all subsequent eigenvalues are smaller. The top eigenspace at zero is exactly \(\operatorname{span}\{e_0,e_1\}\). The compression of the first derivative along a real displacement to this eigenspace is
\[
\begin{pmatrix}0&-\sqrt2a\\-\sqrt2a&0\end{pmatrix}.
\]
Degenerate perturbation theory for the isolated double eigenvalue gives top branches \(m\pm\sqrt2a t+O(t^2)\) for signed real \(t\); the largest is \(m+\sqrt2a|t|+O(t^2)\). Rotation transfers this to every complex direction, proving the cusp formula.

## Verification

Equation (1) is independently reconstructed in the included `verify.py` from the binomial disk-integral identity. The script compares finite monomial compressions against the exact concentric spectrum, tests the global two-mode lower bound and the finite-hole moment obstruction, and checks approach to both local asymptotic coefficients. Its finite-dimensional eigenvalues are diagnostics, not a substitute for the infinite-dimensional operator perturbation proof. The two expansions are justified by trace-norm analyticity and the respective simple/double isolated eigenvalue gaps.

As representative values, \(r=0.3\), \(R=0.7\) yield the exact quadratic coefficient \(0.0964285714285714\ldots\); \(r=0.4\), \(R=\sqrt{0.84}\) yield the exact cusp slope \(0.226274169979695\ldots\). The code checks convergence without asserting finite cutoffs are exact norms.

## Relationship to prior work

Ramos and Tilli's wavelet/Bergman Faber–Krahn work, first made public as arXiv:2205.07998 on 2022-05-16, explicitly discusses the reverse Euclidean-area concentration problem and an inverse geometric question at its unweighted endpoint. Their main theorem is a *maximal* hyperbolic-measure concentration result. In the discussion after their Theorem 4.1, they additionally state that every radial Euclidean-measure domain attains the lower area bound; this is too broad for ordinary Bergman concentration: a centered annulus with \(r^2+R^2>1\) has \(\lambda_1>\lambda_0=m\). The criterion proved here identifies the sharp boundary for single circular holes and quantifies eccentric displacement. The earlier inverse localization analysis of Abreu and Dörfler, arXiv:1202.5841, treats simply connected domains and obtains a concentric-annulus implication when one of two nested circular boundaries is already centered. These statements cover part of the one-hole rigidity mechanism, but neither supplies the all-finite-hole classification together with the exact area-optimality threshold and quadratic-to-linear perturbative transition. The broader literature on radial Toeplitz eigenvalue sequences provides context but does not itself imply the displacement coefficients.

A related indexed Gaussian-Fock result concerns a conical spectral crossing for an *eccentric Gaussian localization annulus*. That is an analogous phenomenon with a different Hilbert-space measure and Gaussian monomial spectrum; it does not imply the Euclidean Bergman threshold \(r^2+R^2=1\), the coefficients above, or the multi-hole necessity. These are best-knowledge distinctions, not a claim that every older result on circular quadrature domains has been exhaustively excluded.

## Limitations

The classification assumes the outer disk is centered and holes are literal, pairwise disjoint Euclidean disks of strictly positive radius. Arbitrary irregular multiply connected regions, overlapping holes, weighted Bergman variants, and global monotonicity of the norm with hole displacement are not addressed. The one-hole concentricness implication is not claimed new in isolation. The local coefficients are asymptotic at the center and do not determine the full spectrum for eccentric holes. Numerical Galerkin experiments only test finite compressions. Historical priority is provisional pending specialist review; no independent mathematical audit has been performed.

## References

1. J. P. G. Ramos and P. Tilli, *A Faber–Krahn inequality for wavelet transforms*, arXiv:2205.07998 (first submitted 2022-05-16); *Bull. London Math. Soc.* 55 (2023), 2018–2034. https://arxiv.org/abs/2205.07998 ; https://doi.org/10.1112/blms.12833
2. L. D. Abreu and M. Dörfler, *An inverse problem for localization operators*, arXiv:1202.5841 (2012); *Inverse Problems* 28 (2012), 115001. https://arxiv.org/abs/1202.5841 ; https://doi.org/10.1088/0266-5611/28/11/115001
3. D. Suárez, *The eigenvalues of limits of radial Toeplitz operators*, *Bull. London Math. Soc.* 40 (2008), 631–641. https://doi.org/10.1112/blms/bdn042
