# Parity-sharp equatorial first-jet sampling and exact conditioning of pure spherical harmonics

## Finding
Let \(\ell\ge1\) and \(M\ge1\) be integers. On the standard unit two-sphere take the \(M\) equispaced equatorial sites with longitudes \(\phi_j=\phi_0+2\pi j/M\), where \(0\le j<M\). On the complex \((2\ell+1)\)-dimensional space \(\mathcal H_\ell(S^2)\) of *pure* degree-\(\ell\) spherical harmonics, measure at each site the value and the **meridional tangent derivative** (the derivative in increasing colatitude), scaled by \(1/\sqrt{\ell(\ell+1)}\). Let \(T_{\ell,M}\) be this two-channel operator, each channel carrying the common sample weight \(1/M\), and use probability-area \(L^2\) norm on the input.

**Complete rank and singular spectrum.** For every positive \(M\),
\[
\operatorname{rank}T_{\ell,M}=\begin{cases}
\min(M,\ell+1)+\min(M,\ell),&M\text{ odd},\\
\min(M,2\ell+1),&M\text{ even}.
\end{cases}
\]
Every nonzero eigenvalue of \(T_{\ell,M}^{*}T_{\ell,M}\) is a sum \(\sum_{m\in C}\lambda_{\ell,m}\), where \(C\) ranges over the nonempty classes of \(m\in\{-\ell,\ldots,\ell\}\) having both the same residue modulo \(M\) and the same parity of \(\ell+m\). Each such class contributes one eigenvalue, and the remaining \((2\ell+1)-\operatorname{rank}T_{\ell,M}\) eigenvalues are zero. The positive rational summands \(\lambda_{\ell,m}=\lambda_{\ell,|m|}\) are explicitly given below.

Thus exact injectivity holds **if and only if**
\[
\boxed{(M\text{ odd and }M\ge\ell+1)\quad\text{or}\quad(M\text{ even and }M>2\ell).}
\]
The least possible number of equatorial *sites* for injectivity is \(M_{\min}=\ell+1\) for even \(\ell\) and \(M_{\min}=\ell+2\) for odd \(\ell\). This is also minimal among all equally spaced equatorial configurations using precisely these two measurements per site. For an injective configuration the harmonic basis diagonalizes the sampling Gram matrix, with diagonal entries \(\lambda_{\ell,m}\) *independent of the number of sites and the initial longitude*. Its optimal upper and lower squared frame bounds are
\[
\boxed{B_\ell=(2\ell+1)\binom{2\ell}{\ell}4^{-\ell},\qquad
A_\ell=\frac{2}{\ell+1}B_\ell,\qquad
\frac{B_\ell}{A_\ell}=\frac{\ell+1}{2}.}
\]
At the minimum-site odd grid, reconstruction is therefore explicit by two discrete Fourier transforms and diagonal division; the squared observation condition number is exactly \((\ell+1)/2\). No extra sites on a *regular equatorial grid* improve this normalized conditioning after full rank is obtained.

## Assumptions and scope
Use spherical coordinates \((\theta,\phi)\), where \(\theta\in[0,\pi]\) is colatitude and the equator is \(\theta=\pi/2\). The sites are \(x_j=(\cos\phi_j,\sin\phi_j,0)\). The input norm is \(\|f\|^2=\int_{S^2}|f|^2\,d\sigma/(4\pi)\). The output is
\[
T_{\ell,M}f=\left(\left[\frac{f(x_j)}{\sqrt M}\right]_{j=0}^{M-1},
\left[\frac{\partial_\theta f(x_j)}{\sqrt{M\ell(\ell+1)}}\right]_{j=0}^{M-1}\right).
\]
For \(M=1,2\), the phrase equispaced sites simply means one or two equatorial samples; no polygon terminology is needed. The theorem is complex-linear, includes both positive and negative azimuthal orders, and uses **only the normal-to-equator component of the tangential gradient**, not the full gradient. It does **not** apply to the cumulative space of all degrees at most \(\ell\) or to unknown mixtures of degrees. Both measurement types are necessary for the stated sparse-grid injectivity; deleting either creates parity-blind harmonics. The scale \(1/\sqrt{\ell(\ell+1)}\) is the natural degree-\(\ell\) global Dirichlet normalization and is essential to the exact frame constants.

Let \(Z_{\ell,m}=\sqrt{4\pi}\,Y_{\ell,m}\) denote the standard complex spherical harmonics normalized to probability area, with \(-\ell\le m\le\ell\). Write \(s=|m|\). If \(\ell+s\) is even, put \(a=(\ell+s)/2\), \(b=(\ell-s)/2\) and set
\[
\lambda_{\ell,m}=\frac{2\ell+1}{4^\ell}\binom{2a}{a}\binom{2b}{b}.
\]
If \(\ell+s\) is odd, put \(a=(\ell+s-1)/2\), \(b=(\ell-s-1)/2\) and set
\[
\lambda_{\ell,m}=\frac{(2\ell+1)(2a+1)!(2b+1)!}{4^{\ell-1}(a!b!)^2\ell(\ell+1)}.
\]
All these quantities are positive. The labels \(\ell\), \(m\), \(M\) are integers within the stated ranges.

## Proof
**1. Equatorial parity and channel isolation.** The normalized basis satisfies
\[
Z_{\ell,m}(\theta,\phi)=C_{\ell,m}P_\ell^{|m|}(\cos\theta)e^{im\phi}
\]
up to a harmless constant phase, where \(|C_{\ell,m}|^2=(2\ell+1)(\ell-|m|)!/(\ell+|m|)!\). Rodrigues' formula and parity of \(P_\ell\) show that \(P_\ell^{|m|}(0)\ne0\) exactly when \(\ell+|m|\) is even, whereas \((P_\ell^{|m|})'(0)\ne0\) exactly when \(\ell+|m|\) is odd. Since \(\partial_\theta=-\partial_{\cos\theta}\) at the equator, each basis harmonic occupies **exactly one** of the two measured channels. For either channel its dependence on longitude is the Fourier character \(e^{im\phi}\). The two nonzero equatorial amplitude squares, including the degree-normalized derivative, are precisely the positive numbers \(\lambda_{\ell,m}\) displayed above. For clarity the standard double-factorial evaluations used here are
\[
P_\ell^s(0)=(-1)^{(\ell+s)/2}\frac{(\ell+s-1)!!}{(\ell-s)!!}\quad(\ell+s\text{ even}),
\]
\[
(P_\ell^s)'(0)=(-1)^{(\ell+s-1)/2}\frac{(\ell+s)!!}{(\ell-s-1)!!}\quad(\ell+s\text{ odd}).
\]
These identities, with \((-1)!!=0!!=1\), follow by differentiating Rodrigues' formula. Squaring, inserting \(|C_{\ell,m}|^2\), and dividing the derivative channel by \(\ell(\ell+1)\) gives the binomial/factorial formulas. Signs have no effect on eigenvalues.

**2. Fourier block decomposition.** For \(r\in\mathbb Z/M\mathbb Z\), the vectors \(M^{-1/2}(e^{im\phi_j})_{j=0}^{M-1}\) and \(M^{-1/2}(e^{in\phi_j})_{j=0}^{M-1}\) are orthogonal unless \(m\equiv n\pmod M\), in which case they are scalar multiples. Combining this with the two orthogonal measurement channels yields one rank-one block for each occupied pair \((r,\ell+m\bmod2)\). Its unique positive Gram eigenvalue is the sum of the squared column norms \(\lambda_{\ell,m}\) in that block. This proves the asserted complete spectrum including all zeros, without assuming injectivity or any special initial longitude.

**3. Rank and sharp site threshold.** When \(M\) is even, two congruent orders have the same parity, so the number of occupied blocks equals the number of distinct residues in the consecutive interval \([-\ell,\ell]\), namely \(\min(M,2\ell+1)\). When \(M\) is odd, the \(\ell+1\) orders in one parity class and the \(\ell\) in the other form progressions with step two; because two is invertible modulo odd \(M\), their distinct-residue counts are \(\min(M,\ell+1)\) and \(\min(M,\ell)\). Therefore rank equals \(2\ell+1\) exactly under the displayed odd/even criterion. The least odd integer at least \(\ell+1\) is \(\ell+1\) for even \(\ell\) and \(\ell+2\) for odd \(\ell\); all admissible even integers exceed \(2\ell\). This proves minimality within the specified class. At an injective grid every block is a singleton, proving diagonalization and independence from \(M\).

**4. Exact sharp conditioning.** The nonnegative-order weights have two monotone interleaved sequences. In the value channel, with \(a=(\ell+s)/2\), \(b=(\ell-s)/2\), their ratio when \(s\) grows by two is
\[
\frac{\lambda_{\ell,s+2}}{\lambda_{\ell,s}}=\frac{b(2a+1)}{(a+1)(2b-1)}>1\qquad(b\ge1).
\]
In the derivative channel, with \(a=(\ell+s-1)/2\), \(b=(\ell-s-1)/2\), the corresponding ratio is
\[
\frac{\lambda_{\ell,s+2}}{\lambda_{\ell,s}}=\frac{b(2a+3)}{(a+1)(2b+1)}<1\qquad(b\ge1).
\]
The strict inequalities use \(a-b=s\ge0\). The central weights are equal: \(\lambda_{\ell,0}=\lambda_{\ell,1}\). To see this without factorial manipulation, use \(P_\ell^1(x)=-\sqrt{1-x^2}P_\ell'(x)\), the Legendre equation at \(x=0\), and the normalization ratio \(|C_{\ell,1}/C_{\ell,0}|^2=1/[\ell(\ell+1)]\). If \(\ell\) is odd, the identity compares the derivative of order zero with the value of order one; if \(\ell\) is even it compares the value of order zero with the derivative of order one. Thus the global maximum occurs at \(s=\ell\), and the global minimum occurs at \(s=\ell-1\), with possible equal central weights for the smallest degrees. The factorial formulas give
\[
\lambda_{\ell,\ell}=(2\ell+1)\binom{2\ell}{\ell}4^{-\ell},\qquad
\frac{\lambda_{\ell,\ell}}{\lambda_{\ell,\ell-1}}=\frac{\ell+1}{2}.
\]
These are actual attained eigenvalues, so the frame constants and squared condition number are sharp. As \(\ell\to\infty\), Stirling's formula gives \(B_\ell\sim2\sqrt{\ell/\pi}\) and \(A_\ell\sim4/\sqrt{\pi\ell}\). The assertions cover \(\ell=1\), where both bounds equal \(3/2\), and \(\ell=2\), where the smallest eigenvalue occurs also at order zero.

## Verification
The included standalone `VERIFY.py` uses exact integer/fraction arithmetic to check the binomial coefficients, symmetry, sharp extrema and analytic rank/count identities for degrees \(1\le\ell\le64\) and all \(1\le M\le4\ell+4\). Independently it constructs the **actual two-channel matrices** using SciPy's spherical-harmonic evaluations and meridional derivatives for degrees \(1\le\ell\le11\), and for every \(1\le M\le2\ell+4\) checks all eigenvalues, exact ranks and, where applicable, diagonal Gram entries. It printed `EQUATOR_JET_PASS exact_assertions=22848 direct_matrices=176 max_spectral_error=1.47e-14`. These finite computations corroborate the analytic arguments, but do not replace the universal proof. Requirements: Python 3, NumPy, SciPy; execute `python3 VERIFY.py` from the extracted artifact directory.

## Relationship to prior work
Adcock and Sui (2017, arXiv:1712.06645v1) establish sparse reconstruction guarantees for gradient-augmented orthogonal polynomial measurements on tensor domains, including Fourier extensions; the present result addresses a different, *deterministic*, single-eigenspace, equatorial first-jet measurement operator. Zandieh, Han and Avron (2022, arXiv:2202.12995v1) recover low-pass spherical harmonic expansions from randomized **values**, rather than the present pure-degree values plus a single meridional derivative. Khalid, Kennedy and McEwen (2014, arXiv:1403.4661v2) design multiple iso-latitude rings for the whole band; their transforms and sample count are not an equatorial two-channel exact-degree theorem. The 2021 regular-grid Wigner D-function paper (DOI:10.1007/s43670-021-00006-2) uses spherical-harmonic derivatives to optimize point placement but does not assert this deterministic first-jet rank or condition number. The previously published results on a rectangular **Hopf torus in \(S^3\)** and on **two meridians of \(S^2\)** share Fourier-aliasing ideas but concern value-only sampling of other domains; neither theorem applies by restriction to the present equatorial value-plus-derivative operator. No equivalence or stronger covering assertion was identified in the inspected materials; this is not a proof of historical priority.

## Limitations
The theorem concerns one known exact harmonic degree, a special regular grid on a *fixed equator*, both of the specified observation channels, and the stated relative normalization. It does not give a reconstruction theorem for a mixed-degree band, an arbitrary latitude, irregular sampling geometries, or minimax optimality among all possible observation designs. The bounded literature search cannot exclude an unindexed equivalent formulation; an independent mathematical and bibliographic audit has not been performed. The full-rank theorem is analytic; finite computations are only checks of instances.

## References
1. B. Adcock and Y. Sui, *Compressive Hermite interpolation: sparse, high-dimensional approximation from gradient-augmented measurements*, arXiv:1712.06645v1, first posted 2017-12-18. https://arxiv.org/abs/1712.06645
2. A. Zandieh, I. Han and H. Avron, *Near Optimal Reconstruction of Spherical Harmonic Expansions*, arXiv:2202.12995v1, first posted 2022-02-25. https://arxiv.org/html/2202.12995v1
3. Z. Khalid, R. A. Kennedy and J. D. McEwen, *An Optimal-Dimensionality Sampling Scheme on the Sphere with Fast Spherical Harmonic Transforms*, arXiv:1403.4661v2, 2014. https://arxiv.org/html/1403.4661v2
4. *Tight bounds on the mutual coherence of sensing matrices for Wigner D-functions on regular grids*, 2021. https://doi.org/10.1007/s43670-021-00006-2
5. *Parity-sharp rectangular Hopf-grid interpolation of exact spherical harmonics*, published finding 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-parity-sharp-rectangular-hopf-grid-interpolation-of-exact-spheri--78e042407020
6. *Exact angular resonances and minimal two-meridian sampling of pure spherical harmonics*, published finding 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-angular-resonances-and-minimal-two-meridian-sampling-of-pu--f7a6d1cb41a5
