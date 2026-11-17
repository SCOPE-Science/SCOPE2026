# Sharp origin-to-off-center transitions for kernel testing of two-frequency Hardy Hankel operators

## Finding

Let \(H^2\) be the complex Hardy space of the unit disk, let \(m\ge3\) be an integer, and let
\[\psi(z)=az+bz^m,\qquad a,b\in\mathbb C\setminus\{0\}.\]
For the antianalytic Hankel operator \(H_{\overline\psi}:H^2\to L^2(\mathbb T)\ominus H^2\), define its reproducing-kernel testing norm
\[G(\psi)=\sup_{w\in\mathbb D}\|H_{\overline\psi}k_w\|_2,
\qquad k_w(z)=\frac{\sqrt{1-|w|^2}}{1-\overline w z}.\]
Write \(c=|a|/|b|>0\). Define the sharp threshold
\[
C_3=2,
\quad
C_m=2^{-(m-1)/2}\left(\frac{m-3}{m-1}\right)^{(m-3)/2}
\left(\frac{m+1}{m-1}\right)^{(m+1)/2}\quad(m\ge4),
\]
and, for \(m\ge4\), the coexistence radius
\[R_m=\frac{\sqrt{(m-3)(m+1)}}{\sqrt2(m-1)}.\]
The point \(w=0\) is a maximizer in the definition of \(G(\psi)\) **if and only if** \(c\ge C_m\). More precisely:

1. If \(0<c<C_m\), all norming kernels have strictly positive radii, and \(G(\psi)^2>|a|^2+|b|^2\).
2. If \(c>C_m\), \(k_0\) is the unique norming kernel and \(G(\psi)^2=|a|^2+|b|^2\).
3. If \(c=C_m\) and \(m\ge4\), there are exactly \(m\) norming kernels: \(k_0\) and the \(m-1\) kernels at \(w=R_m e^{i\theta}\) with \((m-1)\theta\equiv\arg(a\overline b)\pmod{2\pi}\). Their common squared norm is \(|a|^2+|b|^2\).
4. If \(m=3\) and \(c=2\), \(k_0\) is the unique norming kernel. If \(0<c<2\), exactly two kernels are norming; their radius satisfies
\[|w|^2=\frac{-2c+\sqrt{c^2+6c}}3,\]
and their angles satisfy \(2\arg w\equiv\arg(a\overline b)\pmod{2\pi}\).

The degree-three transition is continuous: the off-center norming radius tends to zero as \(c\uparrow2\). In each degree \(m\ge4\), by contrast, every choice of off-center norming radii for \(c\uparrow C_m\) converges to the nonzero value \(R_m\). In fact, the origin remains a strict **local** maximizer for every \(c>0\) when \(m\ge4\), even when it is not a global maximizer. This gives an exact coexistence and discontinuous global-optimizer transition.

For comparison, the ordinary Hankel operator norm is independent of \(m\) and equals
\[\|H_{\overline\psi}\|=\frac{|a|+\sqrt{|a|^2+4|b|^2}}2.\]
As \(m\to\infty\), \(C_m\sim 2^{-(m-1)/2}\) and \(R_m\to1/\sqrt2\).

## Assumptions and scope

All norms use normalized arc measure on \(\mathbb T\). The Garsia testing norm is not the full operator norm: Bonsall's kernel identity states
\[\|H_{\overline\psi}k_w\|_2^2=P(|\psi|^2)(w)-|\psi(w)|^2.\]
The theorem determines the exact criterion for the **origin** to be globally norming, all norming kernels at and above the threshold, and the two norming kernels for cubic symbols below the threshold. It does not assert uniqueness of the off-center maximizing radius in every higher degree below the threshold.

The case \(a=0\) or \(b=0\) is excluded: for a single monomial, the origin is norming. The phase of \(a\overline b\) rotates the off-center maximizers but does not change their radii or the transition threshold.

## Proof

**Hankel norm.** In the orthonormal Hardy basis \(1,z,z^2,\ldots\), \(H_{\overline\psi}\) vanishes on monomials of degree at least \(m\). In the first \(m\) coordinates it has the conjugate of the matrix \(bJ_m+aE_{00}\), where \(J_m\) is the reversal permutation matrix. Multiplying by \(J_m\) reduces its nontrivial part to the \(2\times2\) triangular block \(\begin{psmallmatrix}b&0\\a&b\end{psmallmatrix}\); the remaining singular values equal \(|b|\). The larger singular value of the block is \((|a|+\sqrt{|a|^2+4|b|^2})/2\), proving the stated norm formula.

**The scalar kernel profile.** Writing \(w=re^{i\theta}\), expansion of the Poisson integral in the kernel identity gives
\[
\begin{aligned}
\|H_{\overline\psi}k_w\|_2^2
={}&|a|^2(1-r^2)+|b|^2(1-r^{2m})\\
&+2(1-r^2)\operatorname{Re}(\overline a b\,w^{m-1}).
\end{aligned}
\]
For fixed \(r>0\), this is maximal exactly when \((m-1)\theta\equiv\arg(a\overline b)\pmod{2\pi}\). The maximal squared value divided by \(|b|^2\) is
\[F_{m,c}(r)=c^2(1-r^2)+1-r^{2m}+2cr^{m-1}(1-r^2).\]
It extends continuously to \([0,1]\), with \(F_{m,c}(1)=0\) and \(F_{m,c}(0)=c^2+1>0\). Hence the testing norm is attained in the open disk and
\[G(\psi)^2=|b|^2\max_{0\le r\le1}F_{m,c}(r).\]

**The origin versus off-center comparison.** For \(0<r<1\),
\[F_{m,c}(r)-F_{m,c}(0)
=r^2[-c^2-r^{2m-2}+2cr^{m-3}(1-r^2)].\]
For \(r>1/\sqrt2\) the bracket is strictly negative, as its quadratic discriminant in \(c\) is negative. At \(r=1/\sqrt2\) it can be zero for one coefficient ratio, but cannot be positive. For \(0<r<1/\sqrt2\), define
\[c_\pm(r)=r^{m-3}\big((1-r^2)\pm\sqrt{1-2r^2}\big).\]
Then \(F_{m,c}(r)>F_{m,c}(0)\) precisely when \(c_-(r)<c<c_+(r)\). In particular, any coefficient ratio for which off-center points can exceed the origin must lie below \(\sup_r c_+(r)\).

Put \(t=\sqrt{1-2r^2}\in(0,1)\). A direct factorization yields
\[c_+(r)=2^{-(m-1)/2}(1-t)^{(m-3)/2}(1+t)^{(m+1)/2}.\]
Its logarithmic derivative in \(t\) is
\[\frac{2-(m-1)t}{1-t^2}.\]
For \(m\ge4\), this expression vanishes exactly once, at \(t=2/(m-1)\), with positive sign before and negative after. Thus \(c_+\) has the unique strict maximum \(C_m\), occurring at \(r=R_m\). For \(m=3\), the displayed derivative is positive throughout \((0,1)\), so \(\sup c_+=2\) is approached only as \(r\downarrow0\) and never attained at positive radius.

If \(c>C_m\), every positive radius loses to \(r=0\). If \(c=C_m\) and \(m\ge4\), equality can occur only at \(R_m\): the branch \(c_-(r)\) is strictly below \(c_+(r)\le C_m\), and the upper branch reaches \(C_m\) only at \(R_m\). For \(m=3\), both branches are strictly below \(2\) at positive radii. The aligned-angle condition gives exactly \(m-1\) off-center maximizers when \(m\ge4\) and \(c=C_m\).

It remains to verify that every \(0<c<C_m\) admits strict off-center improvement, rather than merely ruling out ratios above \(C_m\). For \(m\ge4\), as \(r\downarrow0\), both branches \(c_\pm(r)\) tend to zero, and \(c_+(r)\) increases continuously to \(C_m\) along \(0<r<R_m\). For any fixed \(c\in(0,C_m)\), choose \(r\in(0,R_m)\) where \(c_+(r)=c\); since \(c_-(r)<c\), moving \(r\) slightly toward \(R_m\) makes \(c_-(r)<c<c_+(r)\). For \(m=3\), \(c_+(r)\to2\) and \(c_-(r)\to0\) as \(r\downarrow0\), so the same strict inequality holds at sufficiently small positive \(r\). The origin therefore fails to be globally norming for every \(c<C_m\).

**Cubic radii.** For \(m=3\), put \(x=r^2\). The derivative of \(F_{3,c}\) with respect to \(x\) is \(2c-c^2-4cx-3x^2\). If \(0<c<2\), this strictly decreasing expression has exactly one positive zero, located at \(x=(-2c+\sqrt{c^2+6c})/3\), and \(F_{3,c}\) increases before and decreases after that zero. The aligned phase condition gives precisely two maximizing kernels. As \(c\uparrow2\), the radius tends to zero.

**Discontinuous higher-degree transition.** For \(m\ge4\) and \(c\) in a fixed compact interval about \(C_m>0\), the expansion
\[F_{m,c}(r)-F_{m,c}(0)=-c^2r^2+O(r^{m-1})\qquad(r\downarrow0)\]
is uniform. Thus the origin is a strict local maximizer for every positive \(c\), and for \(c\) sufficiently close to \(C_m\), no global off-center maximizing radius can approach zero. If \(c_j\uparrow C_m\), any sequence of off-center maximizing radii has convergent subsequences in \([0,1]\). Continuity forces each limit to be an equality radius at \(C_m\); the uniform exclusion near zero and the value \(F_{m,C_m}(1)=0\) leave only \(R_m\). Hence all radii converge to \(R_m\).

Finally, the displayed closed forms immediately give \(R_m\to1/\sqrt2\) and \(C_m/2^{-(m-1)/2}\to1\): for the latter, take logarithms and use \(\log(1\pm2/(m-1))=\pm2/(m-1)+O(m^{-2})\).

## Verification

The algebraic reduction to a one-variable profile, discriminant factorization, critical-point derivative, all-degree monotonicity, uniqueness at the boundary, cubic root formula, and uniform small-radius exclusion are explicit above. Reproducibility uses the included standalone Python 3 standard-library script `checker.py`: run `python3 checker.py`. It checks finite complex-coefficient variance identities, the Hankel block norm, threshold equalities, radial branch maxima, and numerical examples on both sides of the transition for degrees three through nineteen. These finite diagnostics supplement but do not replace the proof for every integer \(m\ge3\).

## Relationship to prior work

Dyakonov's 2026 discussion introduces the strong reproducing kernel thesis and states the Bonsall Poisson-variance identity; its addendum records a qualitative classification of compact Hankel operators that satisfy exact equality between operator norm and kernel testing norm. A published polynomial-symbol rigidity result likewise establishes that exact equality holds only for monomials. Neither characterization determines where the **strictly smaller** kernel testing norm is maximized for nonmonomial symbols, its sharp coefficient transition, or the exceptional continuous-versus-discontinuous behavior in degrees three versus four and above.

The independently accessible finite-rank shifted-Blaschke classification characterizes operator-norm-saturating kernels for SRKT operators. Its hypotheses and conclusion do not determine the optimizer set for the two-frequency non-SRKT symbols here. Dyakonov's earlier work on Garsia-norm extremality studies equality with a sup norm and extreme points of a function-space unit ball; those are different inequalities from the present kernel base-point optimization.

The quadratic case \(m=2\) is outside the theorem. The multidegree threshold and positive coexistence radius established here concern precisely the higher-degree family.

## Limitations

The result treats exactly two nonzero monomials in degrees one and \(m\ge3\); it does not classify arbitrary polynomial symbols, other exponent pairs, or norming radii in the entire subcritical regime for every \(m\ge4\). The finite-dimensional checker is diagnostic, not a proof for unbounded degrees. The theorem concerns which reproducing kernels maximize the Garsia/kernel-testing norm; it does not assert the strong reproducing kernel thesis for these nonmonomial Hankel operators. Priority remains conditional on the availability of additional literature under equivalent Poisson-variance optimization terminology.

## References

1. K. M. Dyakonov, *The strong reproducing kernel thesis for Hankel operators and the Garsia norm*, arXiv:2609.33242v3 (first public 27 September 2026), especially equation (4) and §3 addendum. https://arxiv.org/abs/2609.33242
2. K. M. Dyakonov, *Extremal problems in BMO and VMO involving the Garsia norm*, arXiv:2404.05565 (first public 2024); J. Funct. Anal. 288 (2025), 110833. https://arxiv.org/abs/2404.05565
3. *Monomial rigidity for polynomial-symbol Hankel operators obeying the strong reproducing kernel thesis*, public mathematical research note (October 2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-monomial-rigidity-for-polynomial-symbol-hankel-operators-obeying--bc8369ca1a24
4. *Shifted-Blaschke classification of finite-rank SRKT Hankel operators*, public mathematical research note (October 2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-shifted-blaschke-classification-of-finite-rank-srkt-hankel-opera--c64bd5a5783f
5. F. F. Bonsall, *Boundedness of Hankel matrices*, J. London Math. Soc. (2) 29 (1984), 289–300 (kernel testing identity cited in [1]).
