# First-alias universality and one-sided frequency selection for fractionally damped resolvents

## Finding
Let \(0<\alpha<1\), \(\lambda>0\), and let \(a:\mathbb R\to[0,\infty)\) be continuous. Assume that for some \(c_+,c_->0\),
\[
\lim_{y\to+\infty}\frac{a(y)}{y^\alpha}=c_+,
\qquad
\lim_{y\to-\infty}\frac{a(y)}{|y|^\alpha}=c_-.
\]
On \(H=L^2(\mathbb R,dy)\), define the normal multiplication generator \((Bf)(y)=(-a(y)+iy)f(y)\) on its maximal multiplication domain, and the contraction semigroup \(S_t=e^{tB}\). For every sampling step \(T>0\), put
\[
Q_T=T(I-e^{-\lambda T}S_T)^{-1},\qquad
E_T=Q_T-\tfrac T2 I-(\lambda-B)^{-1}.
\]
Write \(c_*:=\min(c_+,c_-)\). Then the *exact leading operator-norm constant* is
\[
\boxed{\lim_{T\downarrow0}\frac{\|E_T\|}{T^\alpha}
=\frac{1}{c_*(2\pi)^\alpha}.}
\]
Furthermore, write \(e_T(y)\) for the scalar multiplier of \(E_T\) and \(\varepsilon_T=T^{1-\alpha}\). For every integer \(n\ne0\), with \(c_{\operatorname{sgn}n}=c_+\) for positive \(n\) and \(c_-\) for negative \(n\), one has the locally uniform *complex alias profile*
\[
\boxed{\lim_{T\downarrow0}T^{-\alpha}
 e_T\!\left(\frac{2\pi n+\varepsilon_T v}{T}\right)
=\frac{1}{c_{\operatorname{sgn}n}(2\pi|n|)^\alpha-iv}}
\qquad(v\in\mathbb R).
\]
In particular, if \(y_T\) is any choice of frequency satisfying \(|e_T(y_T)|/\|E_T\|\to1\), then
\[
\operatorname{dist}\!\left(Ty_T,
\{2\pi s:s\in\{-1,1\},\ c_s=c_*\}\right)=o(\varepsilon_T).
\]
When the two high-frequency damping coefficients differ, only the less-damped sign can asymptotically maximize the error. The scalar supremum is achieved at a finite frequency for all sufficiently small \(T\).

## Assumptions and scope
All limits are as \(T\downarrow0\) through *arbitrary positive real sampling steps*, not only dyadic steps. The Hilbert-space measure is Lebesgue measure. The limits imposed on \(a\) are ordinary one-sided limits; no monotonicity, differentiability, parity or rate of convergence is required. Thus, for example, continuous lower-order damping perturbations are included. The generator has domain \(D(B)=\{f\in L^2:\,(-a(y)+iy)f(y)\in L^2\}\). Since \(a\ge0\), dominated convergence proves strong continuity and \(\|S_t\|\le1\). The growth assumption gives \(a(y)=O(1+|y|^\alpha)\) and \(a(y)\ge\kappa|y|^\alpha\) for large \(|y|\) and some \(\kappa>0\). Consequently \(\|BS_t\|\asymp t^{-1/\alpha}\) as \(t\downarrow0\): maximize \(|y|e^{-\kappa t|y|^\alpha}\) for the upper bound, and use \(|y|\asymp t^{-1/\alpha}\) for the lower bound. This is exactly the intermediate Crandall--Pazy regime, with neither endpoint \(\alpha=0\) nor \(\alpha=1\) covered by this theorem.

## Proof
**1. Scalar reduction and normalization.** Put \(p(y)=\lambda+a(y)-iy\), whose real part is at least \(\lambda\). Both the sampled and exact resolvents are bounded multipliers; their difference has multiplier
\[
 e_T(y)=T h(Tp(y)),\qquad
 h(z)=\frac{1}{1-e^{-z}}-\frac12-\frac1z
=\frac12\coth(z/2)-\frac1z.
\]
The function \(h\) has a removable singularity at zero, with \(h(z)=z/12+O(z^3)\), and simple poles of residue one at the nonzero multiples of \(2\pi i\). Set \(\varepsilon=T^{1-\alpha}\), \(\xi=Ty\), and \(u_T(\xi)=\lambda T+T a(\xi/T)\). The norm is the supremum over \(\xi\in\mathbb R\) of
\[
 F_T(\xi):=T^{-\alpha}e_T(\xi/T)
=\varepsilon h(u_T(\xi)-i\xi).
\]
By continuity of \(a\), this supremum equals the essential supremum. Uniformly on compact subsets of either half-line away from zero,
\[
\frac{u_T(\xi)}{\varepsilon}\longrightarrow
c_{\operatorname{sgn}\xi}|\xi|^\alpha.
\]
Moreover \(u_T(\xi)\to0\) uniformly on every bounded \(\xi\)-interval.

**2. The finite-alias windows.** For a fixed nonzero integer \(n\), substitute \(\xi=2\pi n+\varepsilon v\). Uniformly for \(v\) in compact sets,
\[
 u_T(\xi)=\varepsilon c_{\operatorname{sgn}n}(2\pi|n|)^\alpha+o(\varepsilon),
\quad
 u_T(\xi)-i\xi=-2\pi i n+\varepsilon\bigl(c_{\operatorname{sgn}n}(2\pi|n|)^\alpha-iv\bigr)+o(\varepsilon).
\]
The pole residue of \(h\) gives the claimed complex profile. Thus the peak height in the \(n\)-th window is asymptotically \(1/[c_{\operatorname{sgn}n}(2\pi|n|)^\alpha]\). To justify that no intermediate scales are missed, choose a fixed small neighborhood \(|\xi-2\pi n|\le\delta\). For sufficiently small \(T\), \(u_T(\xi)\le1\); the exact identity
\[
 |1-e^{-u+i\xi}|^2=(1-e^{-u})^2+2e^{-u}(1-\cos\xi)
\]
shows that \(|1-e^{-u+i\xi}|\ge C^{-1}\sqrt{u^2+(\xi-2\pi n)^2}\) on that neighborhood. Because \(|u_T(\xi)-i\xi|\) stays uniformly away from zero,
\[
 |F_T(\xi)|\le
C\frac{\varepsilon}{\sqrt{u_T(\xi)^2+(\xi-2\pi n)^2}}+C\varepsilon.
\]
It follows that when \(|\xi-2\pi n|/\varepsilon\to\infty\) in such a neighborhood, \(F_T(\xi)\to0\). When this quotient stays bounded, the locally uniform profile applies. This exhausts all subsequences near each nonzero alias. On compact sets away from the nonzero aliases, the holomorphic function \(h\) is uniformly bounded (including near its removable zero singularity), and \(F_T\to0\) uniformly.

**3. Uniform exclusion of high aliases.** For \(u>0\) and real \(\xi\), \(|1-e^{-u+i\xi}|\ge1-e^{-u}\) and \((1-e^{-u})^{-1}\le1+u^{-1}\). For \(|\xi|\ge R\ge\pi\), therefore,
\[
 |F_T(\xi)|\le\varepsilon\left(\frac{1}{u_T(\xi)}+\frac32+\frac1R\right).
\]
Given any \(\eta\in(0,c_*)\), the one-sided damping assumptions imply that, when \(R\) is fixed and \(T\) is sufficiently small,
\[
 u_T(\xi)\ge(c_*-\eta)\varepsilon|\xi|^\alpha
\qquad(|\xi|\ge R).
\]
Hence
\[
 \limsup_{T\downarrow0}\sup_{|\xi|\ge R}|F_T(\xi)|
\le\frac{1}{(c_*-\eta)R^\alpha}.
\]
Letting \(R\to\infty\) excludes all escaping alias numbers. The finite-window analysis now shows
\[
\limsup_{T\downarrow0}\sup_{\xi\in\mathbb R}|F_T(\xi)|
\le\max_{n\in\mathbb Z\setminus\{0\}}
\frac{1}{c_{\operatorname{sgn}n}(2\pi|n|)^\alpha}
=\frac{1}{c_*(2\pi)^\alpha}.
\]
Evaluating the profile at \(v=0\) for the \(n=+1\) or \(n=-1\) whose coefficient equals \(c_*\) yields the matching lower bound, hence the exact norm limit.

**4. Localization and existence of finite-frequency maxima.** Let \(\xi_T=Ty_T\) for relative near-maximizers. The uniform tail bound makes \(\xi_T\) bounded; all its accumulation points must be nonzero aliases, by the compact-set bound. Their limiting heights exclude every \(|n|\ge2\) and any sign with \(c_{\operatorname{sgn}n}>c_*\). The off-profile estimate then forces \((\xi_T-2\pi n)/\varepsilon\) to stay bounded near each remaining alias; the strict maximum of \(|c_*(2\pi)^\alpha-iv|^{-1}\) at \(v=0\) forces this ratio to tend to zero. Finally, at any fixed \(T>0\), the scalar error multiplier tends to \(T/2\) in modulus as \(|y|\to\infty\). The just-proved norm asymptotic is larger than \(T/2\) for all sufficiently small \(T\), since \(\alpha<1\). Continuity therefore places the maximum at some finite \(y\). This completes the proof.

## Verification
The independent scalar identity \(h(z)=\tfrac12\coth(z/2)-z^{-1}\) and its Laurent residues establish all normalization factors, including the \(2\pi\) in the alias center. The included \(\texttt{verify_first_alias.py}\) uses only the Python standard library and checks 168 finite numerical instances for symmetric and asymmetric damping with lower-order perturbations, multiple alias indices, the complex profiles, and selection of the less-damped sign. Execute \(\texttt{python3 verify_first_alias.py}\) to reproduce the diagnostics. The uniform compact/tail argument above, **not** finite sampling, establishes the full infinite-dimensional result.

## Relationship to prior work
Castillo, *Sampled resolvents of \(C_0\)-semigroups: aliasing and sharp rates on the Crandall--Pazy scale* (arXiv:2611.15563v1, 11 November 2026), Theorem 5.9 establishes the optimal order \(O(T^\alpha)\) and Proposition 5.10 obtains dyadic-sequence lower bounds for a different **discrete-spectrum** normal generator; its numerical section discusses individual first-alias contributions. Those results motivate but do not directly imply the sharp all-step limit for continuous asymptotically two-sided damping, the complete lobe profiles or the sign-selection theorem. Trefethen and Weideman (2014) develop trapezoidal-quadrature and contour-operator-function theory, including Section 18; their contour quadrature is distinct from directly sampling a semigroup's Laplace integral. Wakaiki (2024) studies Crandall--Pazy regularity and Crank--Nicolson iteration rather than this sampled-resolvent constant.

## Limitations
The statement concerns normal multiplication semigroups whose spectral damping has positive two-sided fractional-power asymptotes. It does **not** claim the same constant for arbitrary (possibly nonnormal) Crandall--Pazy semigroups, for discrete spectra, or for the endpoint values \(\alpha=0,1\). Frequencies that maximize the scalar multiplier need not yield an \(L^2\) norm-attaining vector. An unindexed prior equivalent of the asymptotic norm statement cannot be ruled out absolutely.

## References
1. N. Castillo, *Sampled resolvents of \(C_0\)-semigroups: aliasing and sharp rates on the Crandall--Pazy scale*, arXiv:2611.15563v1 (first posted 2026-11-11), https://arxiv.org/html/2611.15563v1, especially Theorem 5.9, Proposition 5.10 and Section 7.
2. L. N. Trefethen and J. A. C. Weideman, *The Exponentially Convergent Trapezoidal Rule*, SIAM Review 56 (2014), 385--458, https://doi.org/10.1137/130932132, especially Sections 15--18.
3. M. Wakaiki, *Characterizations of the Crandall--Pazy Class of \(C_0\)-semigroups on Hilbert Spaces and Their Application to Decay Estimates*, arXiv:2410.19387, https://arxiv.org/abs/2410.19387.
