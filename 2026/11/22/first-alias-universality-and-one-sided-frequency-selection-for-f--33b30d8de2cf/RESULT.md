# First-alias universality and one-sided frequency selection for fractionally damped resolvents

## Finding

Let \(0<\alpha<1\), \(\lambda>0\), and let \(a:\mathbb R\to[0,\infty)\) be continuous, with \(a(y)/|y|^\alpha\to c_\pm>0\) as \(y\to\pm\infty\). On \(L^2(\mathbb R,dy)\), let \(B\) be multiplication by \(-a(y)+iy\) on its maximal domain, and write \(S_t=e^{tB}\). Let \(e_T\) denote the multiplier of the trapezoid-corrected resolvent error
\[
E_T=T(I-e^{-\lambda T}S_T)^{-1}-\tfrac{T}{2}I-(\lambda-B)^{-1}.
\]
Set \(\varepsilon_T=T^{1-\alpha}\), \(c_*=\min(c_+,c_-)\), and \(A_* = \{2\pi s:s\in\{-1,1\},\ c_s=c_*\}\).

**Complex profile at every fixed nonzero alias.** For each integer \(n\ne0\), locally uniformly in \(v\in\mathbb R\),
\[
T^{-\alpha} e_T\!\left(\frac{2\pi n+\varepsilon_T v}{T}\right)
\longrightarrow \frac{1}{c_{\operatorname{sgn}n}(2\pi |n|)^\alpha-iv}.
\]
If \(Ty\) tends to \(2\pi n\) with \(|Ty-2\pi n|/\varepsilon_T\to\infty\), the same scaled error tends to zero.

**Localization of all relative near-maximizers.** For any real frequencies \(y_T\),
\[
\frac{|e_T(y_T)|}{\|E_T\|}\longrightarrow1
\quad\Longleftrightarrow\quad
\operatorname{dist}(Ty_T,A_*)=o(\varepsilon_T).
\]
In particular, unequal damping coefficients select only the less-damped sign. The scalar supremum is achieved at a finite frequency for sufficiently small \(T\).

The normalization for these claims is \(T^{-\alpha}\|E_T\|\to[c_*(2\pi)^\alpha]^{-1}\). In the radial nondecreasing case this is an instance of the prior regular-variation first-alias law [1]. For the present two-sided assumptions, the norm limit follows by the same prior strip bound with a two-sided power lower envelope, as detailed below. The contribution here is the complex frequency profile and the classification of near-maximizers, not a new first-alias norm law.

## Assumptions and scope

All limits use arbitrary positive real sampling steps. Neither monotonicity nor a convergence-rate hypothesis is imposed on \(a\). The semigroup is strongly continuous by dominated convergence and contractive since \(a\ge0\). Its generator domain is \(\{f\in L^2:(-a(y)+iy) f(y)\in L^2\}\). In particular, since \(a(y)\) is bounded above and below by positive multiples of \(|y|^\alpha\) for large \(|y|\), maximizing \(|y|e^{-t a(y)}\) up to constants gives \(\|BS_t\|\asymp t^{-1/\alpha}\) as \(t\downarrow0\). No nonnormal, discrete-spectrum or endpoint claim is made. A scalar maximizer need not give an \(L^2\) norm-attaining vector.

## Proof

**Multiplier and normalization.** Write \(\xi=Ty\), \(u_T(\xi)=T(\lambda+a(\xi/T))\), and
\[
F_T(\xi)=T^{-\alpha}e_T(\xi/T)=\varepsilon_T h(u_T(\xi)-i\xi),\qquad
h(z)=\frac{1}{1-e^{-z}}-\frac12-\frac1z.
\]
This identity follows by evaluating the resolvents pointwise; both are bounded because \(\lambda>0\). Continuity makes the supremum of \(|F_T|\) equal to its essential supremum. The singularity of \(h\) at zero is removable; at each other integer multiple of \(2\pi i\) it has a simple pole of residue one. Also \(u_T\to0\) uniformly on bounded \(\xi\)-intervals, by \(a(y)=O(1+|y|^\alpha)\). On each compact subset of either open half-line the ratio \(u_T(\xi)/\varepsilon_T\) converges uniformly to \(c_{\operatorname{sgn}\xi}|\xi|^\alpha\), since \(|\xi|/T\) tends uniformly to infinity there.

For completeness, the strip and first-center argument of [1] gives the norm normalization here. For fixed \(0<\delta<\pi\), the strip \(|\xi|\le2\pi-\delta\) is away from the nonremovable poles, so \(\sup|F_T|=O_\delta(\varepsilon_T)\) in that strip. Outside it, use \(|1-e^{-u+i\xi}|\ge1-e^{-u}\), \((1-e^{-u})^{-1}\le1+u^{-1}\), and \(|u-i\xi|\ge|\xi|\). For any \(0<\eta<c_*\), the lower bound \(u_T(\xi)\ge(c_* -\eta)\varepsilon_T|\xi|^\alpha\) holds uniformly there for small \(T\). Thus
\[
|F_T(\xi)|\le \frac{1}{(c_* -\eta)|\xi|^\alpha}+\varepsilon_T\left(\frac32+\frac{1}{|\xi|}\right)
\qquad (|\xi|\ge2\pi-\delta).
\]
Letting \(\eta,\delta\downarrow0\) in the resulting upper limit gives \([c_*(2\pi)^\alpha]^{-1}\). At an alias \(\xi=2\pi s\) with \(c_s=c_*\), the first term of \(\varepsilon_T h(u_T-i\xi)\) tends to this number and the two corrections tend to zero. This proves the matching lower bound.

**Complex alias profiles.** For \(\xi=2\pi n+\varepsilon_T v\), uniformly on bounded sets of \(v\),
\[
u_T(\xi)-i\xi=-2\pi i n+\varepsilon_T\bigl(c_{\operatorname{sgn}n}(2\pi|n|)^\alpha-iv+o(1)\bigr).
\]
The coefficient of \(\varepsilon_T\) stays separated from zero since its limiting real part is positive. The Laurent expansion at \(-2\pi i n\) gives the stated complex limit. In a fixed small neighborhood of \(2\pi n\), \(n\ne0\), \(u_T\) tends uniformly to zero. The bounded regular part of the same Laurent expansion shows
\[
|F_T(\xi)|\le\frac{\varepsilon_T}{\sqrt{u_T(\xi)^2+(\xi-2\pi n)^2}}+O(\varepsilon_T)
\]
there (choose the neighborhood small enough for the expansion). This tends to zero when the scaled displacement tends to infinity. On compact sets away from the nonzero aliases the boundedness of \(h\) gives uniform convergence of \(F_T\) to zero.

**Near-maximizers.** The strip estimate outside \(|\xi|\le R\) bounds the limiting supremum there by \(1/((c_* -\eta)R^\alpha)\), so the \(Ty_T\) of any relative near-maximizing family are bounded. Every convergent subsequence of these scaled frequencies must limit to a nonzero alias. On such a subsequence, the off-profile bound rules out unbounded scaled displacement, and every further subsequential displacement limit \(v\) gives a limiting magnitude
\[
\frac{1}{\sqrt{c_{\operatorname{sgn}n}^{\,2}(2\pi|n|)^{2\alpha}+v^2}}.
\]
It equals the norm constant only for \(|n|=1\), \(c_{\operatorname{sgn}n}=c_*\), and \(v=0\). Applying this to subsequences proves the stated distance requirement; the locally uniform profiles at the finitely many aliases in \(A_*\) give the converse even if the family alternates signs. Finally, for each fixed \(T\), \(a(y)\to\infty\) and \(e_T(y)\to T/2\) as \(|y|\to\infty\). The small-\(T\) supremum exceeds \(T/2\) by the norm asymptotic, so continuity gives a finite maximizer.

## Verification

The Laurent expansion fixes the phase and all normalization factors; the tail and local estimates are needed to classify every near-maximizer. The accompanying standard-library `verify_first_alias.py` tests specified power laws with lower-order perturbations and finite samples of the complex profiles and selected sign. Such finite diagnostics do not prove the theorem, nor do they exhaust the frequency domain.

## Relationship to prior work

The previous continuous-spectrum first-alias law [1, Finding and Proof Steps 2–5] already gives the exact all-step norm asymptotic \([\lambda+a(2\pi/T)]^{-1}\) for continuous nondecreasing radial damping regularly varying with index less than one. Its power-law example gives the exact symmetric constant. Its norm proof also supplies the bounds used above with a two-sided lower envelope; no novelty is claimed for that norm-only deduction. Castillo [3, Theorem 5.9 and Proposition 5.10] gives the general order estimate and a discrete-spectrum dyadic sharpness construction, with first-alias contributions discussed in Section 7. The discrete boundary-layer result [2] obtains Lorentzian limits for operator norms with geometrically spaced frequencies and with the mesh ratio as the rescaled variable. The result here instead resolves the **complex multiplier as a function of frequency displacement** at every fixed nonzero alias on a continuous spectrum, and identifies all relative near-maximizers, including unequal signs, to a scale smaller than the profile width. This is a bounded priority comparison.

## References

1. *A first-alias law for sampled resolvents with slowly varying spectral damping*, Resultary, 17 November 2026, [record 5fe679bc2f74](https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-a-first-alias-law-for-sampled-resolvents-with-slowly-varying-spe--5fe679bc2f74).
2. *Radix-arithmetic sampling spikes and Lorentzian boundary layers for a diagonal semigroup*, Resultary, 17 November 2026, [record 6ef73b584999](https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-radix-arithmetic-sampling-spikes-and-lorentzian-boundary-layers--6ef73b584999).
3. N. Castillo, *Sampled resolvents of \(C_0\)-semigroups: aliasing and sharp rates on the Crandall–Pazy scale*, [arXiv:2611.15563v1](https://arxiv.org/html/2611.15563v1), 11 November 2026.
