# An exponential localization threshold for Garsia-norm testing of sparse Hardy Hankel symbols

## Finding

For an integer \(m\ge2\) and a real amplitude \(t>0\), put
\[
\psi_{m,t}(z)=z+t z^m,\qquad z\in\mathbb D.
\]
Write \(H_{\overline\psi}:H^2\to H^2_-\) for the Hardy Hankel operator \(f\mapsto P_-(\overline\psi f)\), and put
\[
G_m(t)=\sup_{a\in\mathbb D}\|H_{\overline{\psi_{m,t}}}k_a\|_2,
\quad k_a(z)=\frac{\sqrt{1-|a|^2}}{1-\overline a z}.
\]
Thus \(G_m(t)\) is the Garsia seminorm of \(\psi_{m,t}\). The Hankel-operator norm is independent of \(m\):
\[
\boxed{\|H_{\overline{\psi_{m,t}}}\|=\frac{1+\sqrt{1+4t^2}}2.}
\]

There is an exact and sharply degree-dependent localization transition for the maximizing normalized kernel. Define
\[
T_3=\frac12,
\qquad
T_m=\frac{2(m-1)^2}{(m+1)^2}
\left(\frac{2(m-1)^2}{(m-3)(m+1)}\right)^{(m-3)/2}
\quad(m\ge4).
\]
For every \(m\ge3\),
\[
\boxed{\ G_m(t)^2=1+t^2\ \Longleftrightarrow\ 0<t\le T_m.\ }
\]
If \(t<T_m\), the unique maximizing kernel is \(k_0\). At \(m=3\), \(k_0\) remains the unique maximizer at \(t=T_3\) and the positive-radius maximizer is born continuously for \(t>T_3\). More precisely, for \(t>1/2\), the maximizing squared radius is
\[
\boxed{\ r^2=\frac{\sqrt{1+6t}-2}{3t}.\ }
\]
Its maximizing arguments satisfy \(e^{2i\theta}=1\).

For every \(m\ge4\), the transition instead occurs at a nonzero radius:
\[
\boxed{\ r_m^2=\frac{(m-3)(m+1)}{2(m-1)^2}.\ }
\]
At \(t=T_m\), the complete set of maximizing points consists of the origin and the \(m-1\) points \(r_m e^{2\pi i j/(m-1)}\), \(0\le j\le m-2\). For \(t>T_m\), the origin is not maximizing. The thresholds satisfy the exponential law
\[
\boxed{\ T_m=2^{(m-1)/2}\bigl(1+O(m^{-1})\bigr),\qquad m\to\infty.\ }
\]

The neighboring degree \(m=2\) never has \(k_0\) as a maximizer for any \(t>0\). Moreover, the strict strong-reproducing-kernel-thesis deficit has different sharp small-amplitude orders:
\[
\boxed{\ 
\|H_{\overline{\psi_{m,t}}}\|-G_m(t)
=\begin{cases}
\frac12 t^4+O(t^6),&m=2,\\
\frac12 t^2+O(t^4),&m\ge3,
\end{cases}\qquad t\downarrow0.\ }
\]
The second expansion is independent of \(m\ge3\) for all \(0<t\le1/2\), where the exact norm formula applies.

## Assumptions and scope

The circle carries normalized arc measure, \(H^2\) has orthonormal basis \(1,z,z^2,\ldots\), and \(H^2_-\) has orthonormal basis \(z^{-1},z^{-2},\ldots\). The scalar \(t\) is strictly positive. Complex nonzero coefficient ratios are reduced to positive \(t\) by rotations of the domain and unimodular multiplication; the displayed point locations use the positive-real normalization. All statements are exact in the infinite-dimensional Hardy space but reduce to finite Hankel matrices because the symbols are polynomials. The threshold statement addresses the *location of kernels maximizing the Garsia norm*, not the already-known qualitative failure of the strong reproducing kernel thesis for nonmonomial polynomial symbols.

## Proof

**1. Hankel norm.** Let \(e_j(z)=z^j\). In the negative Fourier basis \((z^{-1},\ldots,z^{-m})\) and the input basis \((1,\ldots,z^{m-1})\), the matrix of \(H_{\overline{\psi_{m,t}}}\) is
\[
A_m=E_{00}+tJ_m,
\]
where \(E_{00}\) has its only nonzero entry at the upper-left corner, and \(J_m\) reverses the \(m\) coordinates. The orthogonal complement of this input block is annihilated. On \(\operatorname{span}\{e_0,e_{m-1}\}\), the real symmetric matrix is
\[
\begin{pmatrix}1&t\\t&0\end{pmatrix}.
\]
On the remaining coordinates, it is \(t\) times a unitary involution. The two displayed eigenvalues are \((1\pm\sqrt{1+4t^2})/2\), and the positive one exceeds \(t\). This gives the asserted Hankel norm for every \(m\ge2\).

**2. Exact kernel-testing profile.** The Bonsall/Poisson-variance identity is
\[
\|H_{\overline\psi}k_a\|_2^2
=\mathcal P(|\psi|^2)(a)-|\psi(a)|^2.
\]
For \(a=re^{i\theta}\), inserting \(\psi(z)=z+t z^m\) gives
\[
\begin{aligned}
\|H_{\overline\psi}k_a\|_2^2
={}&1-r^2+t^2(1-r^{2m})\\
&+2t(1-r^2)r^{m-1}\cos((m-1)\theta).
\end{aligned}
\]
Because \(t>0\), a positive-radius maximizer must satisfy \(\cos((m-1)\theta)=1\). The radial maximum is therefore that of
\[
F_{m,t}(r)=1-r^2+2t(1-r^2)r^{m-1}+t^2(1-r^{2m}),
\quad0\le r\le1.
\]
The profile is continuous, equals zero at \(r=1\), and equals \(1+t^2\) at the origin. In particular a maximizing point always exists in the disk.

**3. The threshold.** For \(m\ge3\) and \(r>0\),
\[
\frac{F_{m,t}(r)-F_{m,t}(0)}{r^2}
=-1+2t(1-r^2)r^{m-3}-t^2r^{2m-2}.
\]
Regarding the right side as a downward-opening quadratic in \(t\), its discriminant has the sign of \(1-2r^2\). For \(r^2>1/2\), it is strictly negative. For \(0<r^2<1/2\), strict improvement over the origin occurs precisely when
\[
t_-(r)<t<t_+(r),
\quad
t_\pm(r)=r^{-(m+1)}\bigl(1-r^2\pm\sqrt{1-2r^2}\bigr).
\]
Rationalizing the smaller root gives
\[
t_-(r)=\frac{r^{3-m}}{1-r^2+\sqrt{1-2r^2}}.
\]
For \(m=3\), the infimum of \(t_-(r)\) is \(1/2\), approached only as \(r\downarrow0\). For \(m\ge4\), write \(s=\sqrt{1-2r^2}\). Differentiating \(\log t_-\) shows that its unique interior stationary point satisfies
\[
(m-3)s=2(1-s),\qquad s=\frac2{m-1}.
\]
Since \(t_-(r)\to\infty\) as \(r\downarrow0\), and the derivative changes from negative to positive at this stationary point, it is the unique global minimum. Substitution yields precisely \(r_m^2\) and \(T_m\) from the finding. At the threshold, a nonzero radius ties the origin exactly when \(m\ge4\) and \(r=r_m\). At every larger amplitude, continuity of the root intervals (or a perturbation of a point on the smaller-root level) supplies a positive radius for which \(F_{m,t}(r)>F_{m,t}(0)\). Below the threshold there is no such radius. This proves all the localization and tie statements, including the exact angular multiplicity.

When \(m=3\), the substitution \(x=r^2\) gives
\[
F_{3,t}(\sqrt{x})
=1+t^2+(2t-1)x-2tx^2-t^2x^3.
\]
The derivative in \(x\) is strictly decreasing on \([0,1]\). For \(t>1/2\) its unique positive zero is \(x=(\sqrt{1+6t}-2)/(3t)\); for \(t\le1/2\) the maximum is at \(x=0\).

For \(m=2\), \(F'_{2,t}(0)=2t>0\), so the origin is never maximizing. The radial profile is strictly concave for \(r\ge0\), because
\[
F''_{2,t}(r)=-2-12tr-12t^2r^2<0.
\]
Its unique maximizing radius solves
\[
r-t+3tr^2+2t^2r^3=0.
\]

**4. Large-degree threshold and small-amplitude deficit.** For \(m\ge4\), set \(s=2/(m-1)\). The threshold formula from Step 3 reads
\[
T_m=\frac2{(1+s)^2}\left(\frac2{1-s^2}\right)^{(m-3)/2}.
\]
Taking logarithms and expanding \(\log(1\pm s)\) with \(s=O(1/m)\) gives
\[
\log T_m=\frac{m-1}{2}\log2+O(m^{-1}),
\]
which yields the exponential law. For all \(m\ge3\), \(T_m\ge1/2\), hence for sufficiently small \(t\), \(G_m(t)=\sqrt{1+t^2}\). The exact Hankel norm in Step 1 therefore gives the quadratic deficit \(\frac12t^2+O(t^4)\).

For \(m=2\), the implicit-function theorem applied to the displayed cubic gives
\[
r(t)=t-3t^3+O(t^5).
\]
Substituting into \(F_{2,t}\) yields
\[
G_2(t)^2=1+2t^2-2t^4+O(t^6),
\qquad
G_2(t)=1+t^2-\tfrac32t^4+O(t^6).
\]
The operator norm expands as \(1+t^2-t^4+O(t^6)\), proving the quartic deficit.

## Verification

The standalone standard-library script `CHECK.py` checks the exact finite Hankel-matrix/kernel-vector identity, the spectral quadratic, the proposed origin-dominating region over a large test grid, critical-radius ties, above-threshold improvement, the degree-three optimizer and the small-amplitude expansions. Run `python CHECK.py` from the directory containing this file. The code is finite consistency evidence; the proofs in Steps 1–4 are responsible for all statements quantified over every degree, amplitude and kernel point.

## Relationship to prior work

Dyakonov's September 2026 paper poses the strong reproducing kernel thesis for Hardy Hankel operators and states the Bonsall identity, including an example of qualitative failure for a quadratic two-term polynomial. The previous general classification of polynomial SRKT symbols as monomials and the stronger finite-rank shifted-Blaschke classification both imply that nonzero binomial symbols here are not SRKT, but neither gives the exact Garsia maximizer location, the discontinuous transition for degrees at least four, or the exponential transition amplitude. These earlier classifications are used as context rather than presented as contributions of this result. The Garsia-extremality work of Dyakonov and the maximal-norm Hankel work of Brevig and Seip concern different equalities and do not directly determine these quantitative radial profiles. The profile is derived here directly from the Poisson identity, not inferred from a failed literature search.

## Limitations

The statement concerns the sparse two-term family with first exponent one and the standard Hardy norm. It does not give a quantitative stability theory for arbitrary polynomial symbols, weighted Hardy spaces, or general compact Hankel operators. Beyond the critical amplitude for degrees at least four, it establishes that the origin ceases to maximize but does not classify the number or location of every positive-radius local maximizer. The numerical script is not a general-purpose proof certificate. Originality remains subject to independent priority checking, especially against historical BMO/Garsia extremal polynomial work.

## References

1. K. M. Dyakonov, *The strong reproducing kernel thesis for Hankel operators and the Garsia norm*, arXiv:2609.33242v1 (first submitted 2026-09-27), §§1–2.
2. K. M. Dyakonov, *Extremal problems in BMO and VMO involving the Garsia norm*, arXiv:2404.05565v2 (initial submission 2024-04-08), J. Funct. Anal. 288 (2025), 110833.
3. O. F. Brevig and K. Seip, *Maximal norm Hankel operators*, arXiv:2301.07937v1 (first submitted 2023-01-19), J. Math. Anal. Appl. 529 (2024), 127221.
4. *Monomial rigidity for polynomial-symbol Hankel operators obeying the strong reproducing kernel thesis*, publicly indexed mathematical note, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-monomial-rigidity-for-polynomial-symbol-hankel-operators-obeying--bc8369ca1a24.
5. *Shifted-Blaschke classification of finite-rank SRKT Hankel operators*, publicly indexed mathematical note, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-shifted-blaschke-classification-of-finite-rank-srkt-hankel-opera--c64bd5a5783f.
