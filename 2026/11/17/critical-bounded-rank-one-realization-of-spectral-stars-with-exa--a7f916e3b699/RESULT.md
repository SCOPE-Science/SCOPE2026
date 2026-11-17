# Critical bounded rank-one realization of spectral stars with exact weak-Schatten density

## Finding

For each integer \(m\ge2\), put \(H=\ell^2(\mathbb N)\) with orthonormal basis \((e_n)_{n\ge1}\), and define the compact weighted forward shift
\[
S_m e_n=n^{-1/m}e_{n+1}\qquad(n\ge1).
\]
For \(a\in\mathbb C\), prescribe the scalar entire secular function \(G_a(z)=e^{az^m}-1\) for perturbations \(F=e_1\otimes\varphi\), meaning \(Fx=\varphi(x)e_1\). A bounded linear functional \(\varphi\) satisfying
\[
\sum_{k\ge0}\varphi(S_m^ke_1)z^{k+1}=G_a(z)
\]
exists **if and only if** \(|a|\le1/m\), and is uniquely determined. For any \(0<|a|\le1/m\), the resulting \(F_a\) is nonzero, rank one, and satisfies \(F_a^2=0\).

For every \(\alpha\in\mathbb C\), the compact operator \(A_{m,a,\alpha}=S_m+\alpha F_a\) has the following exact nonzero spectrum. If \(\alpha=0\) or \(\alpha=-1\), its spectrum is \(\{0\}\). Otherwise let \(L\) be any logarithm of \(1+1/\alpha\); then
\[
\sigma(A_{m,a,\alpha})\setminus\{0\}
=\left\{\lambda\ne0:\ \lambda^m=\frac{a}{L+2\pi i k},\quad k\in\mathbb Z\right\}.
\]
Every nonzero eigenvalue has algebraic multiplicity one. In particular, for fixed \(\alpha\notin\{0,-1\}\), the number of eigenvalues with modulus at least \(r\), counted with algebraic multiplicity, obeys the **bounded-remainder law**
\[
N_{m,a,\alpha}(r)=\frac{m|a|}{\pi}\,r^{-m}+O_{m,a,\alpha}(1)
\qquad(r\downarrow0).
\]
All singular values satisfy \(s_n(A_{m,a,\alpha})\sim n^{-1/m}\), so the eigenvalue-to-singular-value counting ratio tends to \(m|a|/\pi\). At the sharp bounded-realization boundary \(|a|=1/m\), this ratio is exactly \(1/\pi\), irrespective of \(m\) and of nonexceptional \(\alpha\). At \(\alpha=-1\) the eigenvalue counting density vanishes abruptly, although the singular-value asymptotic remains unchanged.

If \(\theta=\arg a\), the normalized angular counting measures of nonzero eigenvalues with modulus at least \(r\) tend, as \(r\downarrow0\), to equal mass \(1/(2m)\) on each of the \(2m\) rays of arguments
\[
\frac{\theta-\pi/2+2\pi j}{m},\quad
\frac{\theta+\pi/2+2\pi j}{m},\qquad j=0,\ldots,m-1.
\]

## Assumptions and scope

All operators act on complex Hilbert space \(\ell^2(\mathbb N)\), with \(m\) any integer at least two, \(a\) any complex number, and \(\alpha\) any complex coupling. The functional is complex linear, with \(\varphi(e_k)=\gamma_k\). A rank-one perturbation here is specifically of the form \(e_1\otimes\varphi\), and the realization threshold is asserted only for this prescribed direction and entire function, not for arbitrary rank-one ranges or arbitrary entire functions. For the spectral and counting assertions assume \(a\ne0\) and \(|a|\le1/m\). The counting asymptotics fix all parameters before \(r\downarrow0\); they are not uniform as \(\alpha\to-1\).

## Proof

**1. The baseline operator.** Since the weights decrease to zero, \(S_m\) is compact; for every \(k\ge1\),
\[
\|S_m^k\|=(k!)^{-1/m},\qquad s_n(S_m)=n^{-1/m}.
\]
The first identity follows because consecutive weight products are maximized starting at \(n=1\). The spectral radius formula gives \(r(S_m)=0\).

**2. Exact realization and its sharp endpoint.** The equality \(S_m^{k}e_1=(k!)^{-1/m}e_{k+1}\) forces the unique Taylor coefficient choice
\[
\gamma_{mj}=\frac{a^j\Gamma(mj)^{1/m}}{j!}\quad(j\ge1),
\qquad \gamma_k=0\ \text{if }m\nmid k.
\]
Stirling's formula gives, for \(a\ne0\),
\[
|\gamma_{mj}|\sim
(2\pi)^{\frac1{2m}-\frac12}m^{-\frac1{2m}}
(m|a|)^j j^{-\frac{m+1}{2m}}.
\]
Consequently \((\gamma_k)\in\ell^2\) precisely when \(m|a|\le1\): the endpoint has squared-power exponent \((m+1)/m>1\), while beyond it the coefficients grow exponentially. For \(a=0\) the zero functional realizes the zero function. Cauchy–Schwarz proves boundedness, and Taylor-coefficient uniqueness proves necessity. Since \(\gamma_1=0\) for \(m\ge2\), the nonzero bounded perturbation satisfies \(F_a^2=\varphi(e_1)F_a=0\). Substitution now gives
\[
\sum_{k\ge0}\varphi(S_m^ke_1)z^{k+1}
=\sum_{j\ge1}\frac{a^jz^{mj}}{j!}=e^{az^m}-1.
\]

**3. Full nonzero spectrum and simplicity.** For any \(\lambda\ne0\), the resolvent \((\lambda I-S_m)^{-1}\) exists, and the rank-one resolvent identity makes \(\lambda\) an eigenvalue of \(S_m+\alpha F_a\) exactly when
\[
1=\alpha\,\varphi((\lambda I-S_m)^{-1}e_1)
=\alpha(e^{a/\lambda^m}-1).
\]
If \(\alpha=0\), no solution exists; for \(\alpha=-1\), it would require \(e^{a/\lambda^m}=0\), which is impossible. For every other nonzero \(\alpha\), solving the exponential equation gives the displayed exact spectrum. The scalar denominator of the rank-one resolvent has derivative \(\alpha ma\lambda^{-m-1}e^{a/\lambda^m}\ne0\) at each nonzero root, so the resolvent has a simple pole of rank one there. Hence all nonzero eigenvalues are algebraically simple. Compactness ensures that the remaining spectral point is exactly zero.

**4. Counting and singular values.** With \(R=|a|r^{-m}\), each integer \(k\) with \(|L+2\pi ik|\le R\) gives exactly \(m\) different eigenvalues of modulus at least \(r\). The intersection of this regularly spaced vertical lattice with the disk of radius \(R\) contains \(R/\pi+O(1)\) points as \(R\to\infty\). Thus
\[
N_{m,a,\alpha}(r)=m\#\{k\in\mathbb Z:|L+2\pi ik|\le|a|r^{-m}\}
=\frac{m|a|}{\pi}r^{-m}+O(1).
\]
For \(n\ge2\), the rank-one approximation-number inequalities give
\[
s_{n+1}(S_m)\le s_n(S_m+\alpha F_a)\le s_{n-1}(S_m).
\]
Together with \(s_n(S_m)=n^{-1/m}\), these show \(s_n(A_{m,a,\alpha})\sim n^{-1/m}\), including the exceptional coupling. The singular-value counting function is asymptotic to \(r^{-m}\), proving the stated density ratio.

**5. Angular distribution.** For large positive (respectively negative) integers \(k\), \(\arg(L+2\pi ik)\to\pi/2\) (respectively \(-\pi/2\)). Taking the \(m\) roots of \(a/(L+2\pi ik)\) gives the displayed two collections of rays. The number of contributing positive and negative integers is asymptotically the same, and each contributes one root on every branch; weak convergence of the finite atomic angular measures follows.

## Verification

The proof requires no finite enumeration. The reproducible file `check_spectral_ladders.py` tests the finite-section rank-one determinant formula, secular functions, the nilpotence identity, singular-value interlacing, the spectral lattice count and endpoint coefficient decay in multiple small cases. It is supplementary evidence only. The exact endpoint \(|a|=1/m\), infinitely many eigenvalues, and asymptotic counting rest on the displayed analytic arguments rather than finite tests.

## Relationship to prior work

Hansmann [1] establishes broad inverse spectral realization by rank-one perturbations of a suitably chosen background operator, using holomorphic resolvent coefficients. That general existence theorem does not fix the compact factorial weighted shift, its singular-value order, or a sharply bounded coefficient functional; it neither states nor implies the present explicit critical realization and exact density without further constructive work. Tcaciuc [2,3] previously gave the degree-one exponential example with weights \(1/n\), functional coordinates \(1/n\), and one exceptional scalar. This result fixes an explicit operator, treats every integer \(m\ge2\), and provides the exact coefficient threshold, nilpotent perturbation, counting and angular laws.

## Limitations

This is an explicit constructive family, not a classification of all quasinilpotent shifts or all rank-one perturbations. Its coefficient threshold is relative to the prescribed exponential secular function and range \(\mathbb Ce_1\). Spectral asymptotics are pointwise in the parameters. Earlier work on cyclic companion roots, perturbation determinants, or entire-function spectral realization could contain equivalent formulations that require further bibliographic assessment. No independent verification is asserted.

## References

[1] M. Hansmann, *Prescribed spectral configurations under rank-one perturbations*, arXiv:2610.33630v1, first submitted 2026-10-24. https://arxiv.org/abs/2610.33630

[2] A. Tcaciuc, *On quasinilpotent operators and the invariant subspace problem*, arXiv:1805.03277v1, first submitted 2018-05-08. https://arxiv.org/abs/1805.03277

[3] A. Tcaciuc, *On quasinilpotent operators and the invariant subspace problem*, Journal of Mathematical Analysis and Applications **477** (2019), 187–195, doi:10.1016/j.jmaa.2019.04.026. https://doi.org/10.1016/j.jmaa.2019.04.026
