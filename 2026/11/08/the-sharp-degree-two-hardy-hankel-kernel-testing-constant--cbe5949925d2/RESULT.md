# The sharp degree-two Hardy Hankel kernel-testing constant

## Finding
For any nonzero degree-at-most-two analytic polynomial \(\psi(z)=az+bz^2\) on the unit disk with \(a,b\in\mathbb C\), define its Hardy Hankel operator \(H_{\overline\psi}:H^2(\mathbb D)\to H^2_-\) by \(H_{\overline\psi}f=P_-(\overline\psi f)\). Let the normalized Szegő kernel be \(k_w(z)=\sqrt{1-|w|^2}/(1-\overline w z)\), \(|w|<1\). Then the **optimal family-wide comparison** between kernel testing and operator norm is
\[
\boxed{\frac{5}{3\sqrt3}\,\|H_{\overline\psi}\|\le\sup_{w\in\mathbb D}\|H_{\overline\psi}k_w\|\le\|H_{\overline\psi}\|.}
\]
The left equality holds exactly for nonzero \(a,b\) satisfying \(|a|/|b|=1/\sqrt6\); all coefficient phases are allowed. In this case the squared kernel-testing-to-operator ratio is \(25/27\). The right equality holds exactly when \(a=0\) or \(b=0\). This is an exact minimax comparison across **all** nonzero quadratic symbols, rather than a selected example.

Equivalently, writing \(\|\psi\|_G\) for the Garsia seminorm and \(\|\psi\|_*\) for the Hardy-Hankel quotient/Nehari norm,
\[
\inf_{(a,b)\ne(0,0)}\frac{\|az+bz^2\|_G}{\|az+bz^2\|_*}=\frac{5}{3\sqrt3}.
\]

## Assumptions and scope
The Hardy norm is the standard coefficient \(\ell^2\) norm, the negative Hardy space is \(H^2_-=L^2(\partial\mathbb D)\ominus H^2\), and the projection \(P_-\) includes strictly negative Fourier modes. Every polynomial under consideration vanishes at the origin, so there is no irrelevant additive constant. The zero symbol is excluded from ratio statements, but satisfies the homogeneous inequality. Coefficients are arbitrary complex numbers and the reproducing-kernel supremum ranges over the entire open disk.

## Proof
**1. Exact two-dimensional reduction.** In input basis \(1,z\) and output basis \(z^{-1},z^{-2}\), the nonzero part of the Hankel matrix is
\[
A=\begin{pmatrix}\overline a&\overline b\\\overline b&0\end{pmatrix}.
\]
The operator annihilates \(z^j\) for \(j\ge2\). The two singular values depend only on \(s=|a|\), \(t=|b|\), and the largest is
\[
N:=\|H_{\overline\psi}\|=\frac{s+\sqrt{s^2+4t^2}}2.
\]
Indeed, the characteristic polynomial of \(A^*A\) is \(\lambda^2-(s^2+2t^2)\lambda+t^4\), whose larger square root is the displayed number. A rotation of the disk variable followed by a unimodular rescaling aligns the coefficient phases, so no phase restriction is introduced.

**2. Exact kernel testing.** For \(w\in\mathbb D\), the only two nonzero output coefficients of \(H_{\overline\psi}k_w\) are \(\sqrt{1-|w|^2}(\overline a+\overline b\,\overline w)\) and \(\sqrt{1-|w|^2}\,\overline b\). Therefore
\[
\sup_{w\in\mathbb D}\|H_{\overline\psi}k_w\|^2
=\max_{0\le r\le1}(1-r^2)\bigl((s+tr)^2+t^2\bigr).
\]
The phase of \(w\) can be chosen to align the two terms, and the endpoint \(r=1\) contributes zero. Dividing \(s,t\) by \(N>0\), we may assume \(N=1\). The quadratic equation \(N^2-sN-t^2=0\) then gives \(s=1-t^2\) and \(0\le t\le1\). Put
\[
F_t(r)=(1-r^2)\bigl((1-t^2+tr)^2+t^2\bigr).
\]

**3. Exact universal lower certificate.** Instead of optimizing \(F_t\) separately for each \(t\), test the admissible radius \(r=t/2\). Direct polynomial expansion gives the *identity*
\[
\boxed{F_t(t/2)-\frac{25}{27}=\frac{(8-3t^2)(3t^2-2)^2}{432}\ge0\qquad(0\le t\le1).}
\]
Since \(8-3t^2>0\) throughout the interval, the strict inequality holds unless \(t^2=2/3\). Thus the maximal kernel norm squared is at least \(25/27\) for every normalized symbol, and any potential equality must have \(t=\sqrt{2/3}\).

**4. Exact sharpness and equality.** At the forced value \(t=\sqrt{2/3}=\sqrt6/3\), one has \(s=1/3\) and the following second polynomial identity, valid for every real \(r\):
\[
\boxed{\frac{25}{27}-F_{\sqrt{2/3}}(r)=\frac23\left(r-\frac1{\sqrt6}\right)^2\left(r^2+\frac{2\sqrt6}{3}r+\frac43\right).}
\]
The last factor is strictly positive for \(0\le r\le1\), and equality occurs at the interior point \(r=1/\sqrt6\). Hence the maximal kernel-norm square is exactly \(25/27\) for that symbol, and the universal bound is optimal. Because equality in step 3 was possible only at this \(t\), the optimizers are precisely those with \(s/t=(1/3)/(\sqrt6/3)=1/\sqrt6\), up to their arbitrary nonzero common scale and coefficient phases.

The upper inequality is simply the restriction of the operator norm to unit-norm test vectors. If exactly one coefficient vanishes, the kernel at \(w=0\) attains the operator norm. If both coefficients are nonzero, the finite-rank norming-kernel argument (or direct strictness in the two-dimensional matrix) shows the kernel supremum is strictly below the operator norm: \(H^*H\) has range in \(\operatorname{span}\{1,z\}\), so a norming kernel must be \(k_0=1\), which would require \(1\) to be an eigenvector of \(H^*H\). Its off-diagonal entry is nonzero when \(ab\ne0\), so this is impossible. The kernel-testing norm vanishes as \(|w|\uparrow1\), ensuring that an attained maximum exists in the disk. This proves the right-equality classification as well.

## Verification
The attached `check_quadratic_hankel.py` evaluates both polynomial identities **symbolically**, with exact arithmetic in \(\mathbb Q(\sqrt6)\); it also checks the normalization and the extremal bound at many finite points. It is standalone Python 3, requires no packages, and prints `QUADRATIC_HANKEL_EXACT_CHECK_OK 2006 checks`. The finite checks do not prove the universal theorem; the exact symbolic certificate identities plus the rank-two reduction, phase maximization, positivity and equality arguments above supply the proof. Run `python3 check_quadratic_hankel.py`.

## Relationship to prior work
Dyakonov's 2026 paper (arXiv:2609.33242, Section 2 and Addendum) formulates the strong reproducing kernel thesis for Hardy Hankel operators, identifies kernel testing with the Garsia norm, observes a strict quadratic example, and, in its Addendum, gives the qualitative polynomial monomial-only equality condition. The present conclusion does **not** claim a new qualitative classification: it establishes the **sharp uniform degree-two lower comparison constant** and the complete set of coefficients at which the largest relative deficit occurs. That numerical value and minimax optimization are not contained in the inspected paper.

A public polynomial-symbol result titled *Monomial rigidity for polynomial-symbol Hankel operators obeying the strong reproducing kernel thesis* proves the zero-deficit characterization but provides no quantitative lower constant for all degree-two symbols. A public *Shifted-Blaschke classification of finite-rank SRKT Hankel operators* likewise characterizes exact equality in the kernel test, not its worst nonzero relative deficit. A public *Exact square-root-two SRKT gap for the logarithmic Hilbert Hankel symbol* has an exact ratio for one **infinite-rank**, logarithmic symbol, which cannot imply the sharp degree-two ratio. General reproducing-kernel testing equivalences for Hardy Hankel operators establish comparability without this exact rank-two sharp constant.

## Limitations
The constant is optimal **only within the degree-at-most-two analytic polynomial family**. It is not the universal best constant for all bounded Hankel operators or symbols of higher degree, and is not asserted to improve general BMO estimates. Novelty is a best-knowledge assessment: a more general older sharp two-dimensional Hankel-testing theorem could subsume this particular minimax computation even if indexed under different terminology. No independent publication-priority verification or independent mathematical audit has been performed.

## References
1. K. M. Dyakonov, *The strong reproducing kernel thesis for Hankel operators and the Garsia norm*, arXiv:2609.33242v3 (first public version 2026-09-27), §§1–3. https://arxiv.org/abs/2609.33242
2. F. F. Bonsall, *Boundedness of Hankel matrices*, J. London Math. Soc. 29 (1984), 289–300, cited for the Garsia/kernel-testing identity.
3. *Monomial rigidity for polynomial-symbol Hankel operators obeying the strong reproducing kernel thesis*, public research note, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-monomial-rigidity-for-polynomial-symbol-hankel-operators-obeying--bc8369ca1a24
4. *Shifted-Blaschke classification of finite-rank SRKT Hankel operators*, public research note, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-shifted-blaschke-classification-of-finite-rank-srkt-hankel-opera--c64bd5a5783f
5. *An exact square-root-two SRKT gap for the logarithmic Hilbert Hankel symbol*, public research note, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-an-exact-square-root-two-srkt-gap-for-the-logarithmic-hilbert-ha--80a74524cde0
6. A. Čolović, *Reproducing Kernel Thesis of Hankel Operators on Weighted Hardy Spaces*, arXiv:2406.03106 (2024).
