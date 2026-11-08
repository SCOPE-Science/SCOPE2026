# A sharp boundary-defect phase diagram for two-periodic unilateral weighted shifts

## Finding
On complex Hilbert space \(\ell^2(\mathbb N_0)\), let \(S\) be the bounded forward weighted shift with positive weights
\[
(t,u,b,a,b,a,b,a,\ldots),\qquad a,b,t,u>0.
\]
Set \(\kappa=t^2+(1+b/a)u^2-(a+b)^2\), \(c=ab\), \(c_0=bu\), \(d=a^2+b^2\), and \(d_0=t^2+u^2\). There is an exact transition:

* **Bulk regime:** if \(\kappa\le0\), then \(w(S)=(a+b)/2\) and \(W(S)=\{z\in\mathbb C:|z|<(a+b)/2\}\). In particular, the boundary is **not attained**, including at equality.
* **Localized regime:** if \(\kappa>0\), the polynomial equation
\[
c+(d-d_0)r+(c-c_0^2/c)r^2=0
\]
has exactly one root \(r\in(0,1)\), and
\[
w(S)=\tfrac12\sqrt{d+c(r+r^{-1})},\qquad
W(S)=\{z\in\mathbb C:|z|\le w(S)\}.
\]
The norming vector for the positive boundary direction has exponentially decaying even and odd subsequences.

A sharp onset law accompanies the transition. Fix \(a,b,u>0\) such that
\(t_c^2=(a+b)^2-(1+b/a)u^2>0\); for \(t^2=t_c^2+\kappa\) as \(\kappa\downarrow0\),
\[
w(S)=\frac{a+b}{2}+\frac{a^3}{4b(a+b)u^4}\kappa^2+O(\kappa^3).
\]

## Assumptions and scope
The weights are all **strictly positive**, the scalar field is complex, the shift is unilateral, and the pattern begins exactly with the two boundary weights \(t,u\) followed by the repeating two-weight tail \(b,a\). The numerical range is \(W(S)=\{\langle Sx,x\rangle:\|x\|=1\}\), and its numerical radius is \(w(S)=\sup\{|z|:z\in W(S)\}\). The onset expansion is restricted to a positive critical \(t_c\) with fixed \(a,b,u\); it does not assert a two-sided analytic expansion at nonpositive \(t_c^2\).

## Proof
**1. Circularity and a Jacobi reduction.** For every angle \(\theta\), the diagonal unitary with entries \(e^{in\theta}\) conjugates \(S\) to \(e^{i\theta}S\). The Toeplitz–Hausdorff convexity theorem therefore makes \(W(S)\) a circular disk, possibly missing its boundary. Positivity of all shift weights and the estimate \(|\langle Sx,x\rangle|\le\langle S|x|,|x|\rangle\) give
\[
2w(S)=\|S+S^*\|.
\]
Split \(\ell^2\) into even and odd coordinates. The self-adjoint operator \(S+S^*\) is unitarily equivalent to \(\begin{psmallmatrix}0&B^*\\B&0\end{psmallmatrix}\), with the upper-bidiagonal operator
\[
B=\begin{pmatrix}t&u&0&\cdots\\0&b&a&\cdots\\0&0&b&a&\cdots\\\vdots&&\ddots&\ddots\end{pmatrix}.
\]
Consequently \(4w(S)^2=\|BB^*\|\), where \(J=BB^*\) is the Jacobi matrix with diagonal \((d_0,d,d,\ldots)\) and upper/lower off-diagonal \((c_0,c,c,\ldots)\).

**2. Essential edge and above-band eigenvalues.** The finite-rank perturbation \(J-J_{\mathrm{tail}}\), where \(J_{\mathrm{tail}}\) is the constant-coefficient half-line Jacobi matrix, has the same essential spectrum
\[
\sigma_{\mathrm{ess}}(J)=[d-2c,d+2c]=[(a-b)^2,(a+b)^2].
\]
For an eigenvalue \(\lambda>(a+b)^2\), the unique square-summable tail solution obeys \(y_j=r^{j-1}\) for \(j\ge1\), with \(0<r<1\) and
\[
\lambda=d+c(r+r^{-1}).
\]
The rows at indices zero and one require
\[
y_0=\frac{c}{c_0r}y_1,\qquad \lambda-d_0=\frac{c_0^2}{c}r.
\]
Eliminating \(\lambda\) gives precisely
\(c+(d-d_0)r+(c-c_0^2/c)r^2=0\). Conversely, any root in \((0,1)\) constructs a positive square-summable eigenvector and hence an eigenvalue strictly above the essential band.

To decide existence and uniqueness without guessing polynomial branches, use the square-summable tail Weyl coefficient
\[
m(\lambda)=\frac{\lambda-d-\sqrt{(\lambda-d)^2-4c^2}}{2c^2},
\qquad\lambda>d+2c.
\]
The boundary eigenvalue equation is \(F(\lambda)=\lambda-d_0-c_0^2m(\lambda)=0\). Here \(m(\lambda)>0\) strictly decreases from \(1/c\) to zero, so \(F\) strictly increases to infinity. An above-band eigenvalue exists if and only if
\[
F((a+b)^2+)= (a+b)^2-d_0-c_0^2/c=-\kappa<0.
\]
When it exists, it is unique. Otherwise the norm of the nonnegative self-adjoint \(J\) equals the essential upper edge \((a+b)^2\).

**3. Attainment and the exact disk.** The Jacobi eigenvector above the band is positive and in \(\ell^2\). Combining it with \(B^*y/\sqrt\lambda\) produces a maximizing vector for \(S+S^*\), so the numerical-radius boundary is attained when \(\kappa>0\). At \(\kappa\le0\), no eigenvalue lies above the band; at its endpoint \(\lambda=(a+b)^2\) every eventual tail solution has the form \(A+Bj\), which cannot be in \(\ell^2\) unless it is zero. Positivity of \(c,c_0\) then forces the entire eigenvector to vanish. Thus the endpoint is not attained. Rotational symmetry and convexity prove the stated open or closed circular disk descriptions.

**4. Quadratic onset.** Write \(r=1-s\) with \(s\downarrow0\), and let \(t^2=t_c^2+\kappa\) while \(a,b,u\) remain fixed. The boundary equation rearranges **exactly** to
\[
\kappa=\frac{c_0^2}{c}s+\frac{c s^2}{1-s},\qquad
4w(S)^2-(a+b)^2=\frac{c s^2}{1-s}.
\]
Since \(c,c_0>0\), the implicit function theorem gives \(s=(c/c_0^2)\kappa+O(\kappa^2)\). Expanding the positive square root yields
\[
w(S)-\frac{a+b}{2}=\frac{c^3}{4(a+b)c_0^4}\kappa^2+O(\kappa^3)
=\frac{a^3}{4b(a+b)u^4}\kappa^2+O(\kappa^3).
\]
This proves all claims.

## Verification
The finite checker `check_boundary.py` uses Python's standard library and independently tests exact rational boundary and eigenvalue identities in two above-band cases, finite Jacobi-section Rayleigh estimates for nine parameter choices across and at the threshold, and convergence toward the quadratic coefficient. Run `python3 check_boundary.py`. The observed output is `TWO_EDGE_PERIODIC_TAIL_CHECK_OK 32 assertion groups; exact identities and finite sections`. The finite checks support, but cannot substitute for, the infinite-dimensional spectrum and endpoint argument given above.

## Relationship to prior work
Wang and Wu (2011) give general qualitative numerical-range criteria for weighted shifts (Theorem 3.1 and Theorem 4.3), including split-periodic tails, and exact one-exceptional-weight constant-tail examples (Theorem 4.6 and Corollaries 4.7–4.8). These results are important antecedents. Their stated formulas do not display the two independently varying boundary weights together with an alternating bulk, its four-parameter quadratic boundary equation, and the exact quadratic outlier onset. The one-exceptional-weight constant-tail limits of this calculation are known and are not separately asserted to be novel. The 2026 article of Audeh, Kittaneh and Moradi establishes integral identities and inequalities for numerical radius and treats finite alternating paths; its accessible abstract does not establish the half-line periodic-tail defect classification. An earlier published calculation for a single exceptional first weight on \(\ell_p\) treats a constant tail and, at Hilbert exponent two, recovers a classical special case, not the general present matrix.

## Limitations
The result is for scalar, positive, complex-Hilbert unilateral shifts with precisely two freely varying leading weights and a positive two-periodic tail. It does not cover arbitrary finite defects, sign-changing/general complex weights without gauge reduction, or non-Hilbert \(\ell_p\). The onset expansion assumes positive \(t_c^2\). General Jacobi-matrix resolvent or old weighted-shift literature may imply the formula under different notation; no independent priority or publication certification is asserted. The finite tests alone do not prove any infinite-dimensional statement.

## References
1. W. Audeh, F. Kittaneh and H. R. Moradi, *Integral Representations and Sharp Numerical Radius Inequalities for Hilbert Space Operators*, arXiv:2610.15242, first submitted 2026-10-11, https://arxiv.org/abs/2610.15242 (abstract inspected).
2. K.-Z. Wang and P. Y. Wu, *Numerical ranges of weighted shifts*, Journal of Mathematical Analysis and Applications 381 (2011), 897–909, doi:10.1016/j.jmaa.2011.04.010 (full open-access primary text inspected).
3. A. Sharif, *On the numerical radius of weighted shifts on \(\ell^2\) as a norm on \(\ell^\infty\) and connections to Banach limits*, arXiv:2303.00876 (abstract and related cited introductory comparison).
4. *Sharp numerical-radius and attainment thresholds for one-edge perturbations of \(\ell_p\) shifts*, publicly available mathematical research record, 2026 (complete scientific-result text inspected; constant-tail one-exceptional-weight comparison).
