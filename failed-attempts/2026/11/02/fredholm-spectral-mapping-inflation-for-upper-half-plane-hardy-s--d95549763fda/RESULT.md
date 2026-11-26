# Fredholm spectral-mapping inflation for upper-half-plane Hardy–Sobolev dilations

## Finding
For each integer \(n\ge1\), the dilation composition group on the inhomogeneous Hilbert Hardy–Sobolev space \(H_n^2(\mathbb C^+)\) exhibits an exact mismatch between the Fredholm spectrum of its generator and those of its positive-time operators. Writing \(\alpha=-\tfrac12\) and \(\beta=n-\tfrac12\), its generator \(A\) and the positive-time dilation \(U_s\) satisfy
\[
\begin{aligned}
\sigma(A)&=\{\lambda:\alpha\le\operatorname{Re}\lambda\le\beta\},\\
\sigma_{\mathrm F}(A)&=\{\operatorname{Re}\lambda=\alpha\}\cup\{\operatorname{Re}\lambda=\beta\},\\
\sigma(U_s)&=\sigma_{\mathrm F}(U_s)=\{\zeta:e^{s\alpha}\le |\zeta|\le e^{s\beta}\},\qquad s>0.
\end{aligned}
\]
In the open strip \(A-\lambda I\) is Fredholm of index \(-1\), with zero-dimensional kernel and one-dimensional cokernel. In the open annulus \(U_s-\zeta I\) is injective with infinite-dimensional cokernel. Therefore the ordinary equality \(e^{s\sigma(A)}=\sigma(U_s)\) holds, but the Fredholm-essential spectral mapping equality fails in the strongest possible radial fashion:
\[
e^{s\sigma_{\mathrm F}(A)}=\{|\zeta|=e^{s\alpha}\}\cup\{|\zeta|=e^{s\beta}\}
\subsetneq\sigma_{\mathrm F}(U_s).
\]
The group norms and generator resolvent norm are also sharp:
\[
\|U_s\|=\begin{cases}e^{s\beta},&s\ge0,\\e^{s\alpha},&s\le0,\end{cases}
\qquad
\|(A-\lambda I)^{-1}\|={1\over\operatorname{dist}(\operatorname{Re}\lambda,[\alpha,\beta])}
\]
for all \(\operatorname{Re}\lambda\notin[\alpha,\beta]\).

## Assumptions and scope
Let \(\mathbb C^+=\{z\in\mathbb C:\operatorname{Im}z>0\}\). For an integer \(n\ge1\), put
\[
\mathcal H_n=\{F\text{ holomorphic on }\mathbb C^+:F^{(k)}\in H^2(\mathbb C^+)\text{ for }0\le k\le n\},\qquad
\|F\|_n^2=\sum_{k=0}^n\|F^{(k)}\|_{H^2}^2.
\]
The Hardy norm is \(\sup_{y>0}\int_{\mathbb R}|F(x+iy)|^2dx\). For all real \(s\), set \(U_sF(z)=F(e^sz)\). Its generator has graph domain \(\mathcal D(A)=\{F\in\mathcal H_n:zF'\in\mathcal H_n\}\). The Fredholm spectrum \(\sigma_{\mathrm F}\) consists of the complex parameters where the closed operator minus that parameter is not Fredholm; in particular, the generator is treated with its graph domain, not as a bounded operator.

## Proof
**1. Exact weighted translation model.** The positive-frequency Paley–Wiener isometry identifies \(\mathcal H_n\) with \(L^2((0,\infty),2\pi W_n(t)dt)\), where
\[
W_n(t)=\sum_{k=0}^{n}t^{2k},\qquad F(z)=\int_0^\infty g(t)e^{izt}dt.
\]
Under the composition dilation the frequency-side function becomes \(g(t)\mapsto e^{-s}g(e^{-s}t)\). Taking \(x=\log t\), the unitary map \(g\mapsto h\) with \(h(x)=(2\pi)^{1/2}e^{x/2}\sqrt{W_n(e^x)}g(e^x)\) gives
\[
(V_sh)(x)=e^{-s/2}\sqrt{\frac{W_n(e^x)}{W_n(e^{x-s})}}h(x-s).
\tag{1}
\]
The multipliers are strictly positive and uniformly bounded above and below for fixed \(s\). Translation density proves strong continuity. Differentiation of (1) on \(C_c^\infty(\mathbb R)\) gives a generator unitarily equivalent to
\[
L=-\frac{d}{dx}+b_n(x),\quad\mathcal D(L)=H^1(\mathbb R),\quad
b_n(x)=-\frac12+\frac{\sum_{k=0}^n k e^{2kx}}{\sum_{k=0}^n e^{2kx}}.
\tag{2}
\]
Here \(b_n\) is real, smooth and bounded, and \(b_n(-\infty)=\alpha\), \(b_n(+\infty)=\beta\). Its derivative is twice the variance of \(k\) under the positive probabilities proportional to \(e^{2kx}\), hence \(b_n\) is strictly increasing. Since its multiplication term is bounded, (2) has exactly the indicated Sobolev domain. From (1), the ratio \(W_n(t)/W_n(e^{-s}t)\) has supremum \(e^{2ns}\) for \(s>0\) and supremum \(1\) for \(s<0\); thus the displayed exact group norms follow.

**2. The generator: spectrum and Fredholm index.** For \(\lambda\in\mathbb C\), an integrating factor for \(L-\lambda I\) is
\[
\phi_\lambda(x)=\frac{e^{-(\lambda+1/2)x}\sqrt{W_n(e^x)}}{\sqrt{W_n(1)}},\qquad (L-\lambda I)\phi_\lambda=0.
\tag{3}
\]
For \(\alpha<\operatorname{Re}\lambda<\beta\), \(\phi_\lambda\) grows exponentially at both ends, so the kernel on \(L^2\) is zero. Conversely, \(\phi_\lambda^{-1}\in L^2(\mathbb R)\) exactly for these parameters, because
\[
\int_{\mathbb R}|\phi_\lambda(x)^{-1}|^2dx
=W_n(1)\int_0^\infty \frac{t^{2\operatorname{Re}\lambda}}{W_n(t)}dt<\infty
\quad\Longleftrightarrow\quad\alpha<\operatorname{Re}\lambda<\beta.
\tag{4}
\]
The adjoint \(L^*=d/dx+b_n(x)\) therefore has the single eigenvector \(\overline{\phi_\lambda^{-1}}\) for eigenvalue \(\overline\lambda\); the adjoint eigenspace has dimension one.

To prove closed range, let \(g\in L^2(\mathbb R)\) satisfy \(\int_{\mathbb R}g(y)\phi_\lambda(y)^{-1}dy=0\). Define
\[
u(x)=\begin{cases}
-\phi_\lambda(x)\displaystyle\int_{-\infty}^x\frac{g(y)}{\phi_\lambda(y)}dy,&x\le0,\\[3pt]
\phantom{-}\phi_\lambda(x)\displaystyle\int_x^\infty\frac{g(y)}{\phi_\lambda(y)}dy,&x\ge0.
\end{cases}
\tag{5}
\]
The two traces at zero agree exactly because the integral of \(g/\phi_\lambda\) vanishes. The kernel ratios on each half-line have an exponentially decaying majorant away from a bounded interval, since the end limits of \(b_n-\operatorname{Re}\lambda\) are strictly separated from zero. Young's inequality and the bounded contribution of the finite middle interval yield \(\|u\|_2\le C_\lambda\|g\|_2\). Then \(u'= (b_n-\lambda)u-g\in L^2\), so \(u\in H^1\), and \((L-\lambda I)u=g\). Conversely, integration against \(\phi_\lambda^{-1}\) annihilates every range vector. Thus the range is precisely a closed codimension-one hyperplane and the index is \(-1\).

On the two boundary lines, use wide normalized oscillatory bumps translated toward the corresponding infinite end, where \(b_n\) approaches the boundary value. They form weakly null singular sequences for \(L-\lambda I\) with vanishing residuals. A closed Fredholm operator with zero kernel cannot admit such approximate null vectors, and the same conclusion follows after any finite-dimensional kernel correction: the boundary lines are not Fredholm. Outside the strip, the group Laplace resolvent formula and its exact exponential bounds yield an inverse with norm at most the reciprocal horizontal distance. The spectrum already includes every point of the closed strip; the standard spectral-distance lower bound for the resolvent gives equality. This proves all assertions for \(A\).

**3. Fixed-time spectrum and infinite cokernel.** For \(s>0\), the exact powers \(\|V_s^m\|=e^{ms\beta}\) and \(\|V_s^{-m}\|=e^{-ms\alpha}\) constrain the spectrum to the stated closed annulus. Every point \(\zeta\) with \(e^{s\alpha}<|\zeta|<e^{s\beta}\) can be written as \(e^{s\overline\lambda}\) for infinitely many distinct \(\lambda\) in the generator's open strip, differing by integer multiples of \(2\pi i/s\). Their nonzero adjoint eigenvectors from (4) are linearly independent (their ratios are distinct Fourier characters in the logarithmic variable), and all obey
\[
V_s^*\overline{\phi_\lambda^{-1}}=e^{s\overline\lambda}\overline{\phi_\lambda^{-1}}.
\]
Hence every open-annulus point lies in the infinite-dimensional adjoint point spectrum of \(V_s\), making \(V_s-\zeta I\) non-Fredholm. It is injective: solving the eigenfunction equation by iteration on each orbit modulo \(s\) forces incompatible square-summable behavior at the two ends, even when \(\zeta\) is on a boundary circle. More precisely, forward growth is asymptotic to \(e^{s\beta}/|\zeta|\) and backward growth is asymptotic to \(|\zeta|/e^{s\alpha}\). Both cannot be less than one. At each boundary circle, weakly null wide oscillatory bumps translated far to the corresponding end yield approximate eigenvectors, so these circles are also in the Fredholm essential spectrum. Thus the full spectrum and Fredholm essential spectrum are the entire annulus. The strict essential spectral mapping failure follows.

## Verification
All formulas derive from the exact unitary model (1). The boundedness, generator domain, integrating factor, end growth, closed-range formula, and fixed-time adjoint eigenmultiplicity are proved above for every integer \(n\ge1\). An accompanying finite checker independently verifies 1,482 algebraic derivative and multiplier inequalities across sample dimensions and parameters; its checks do not replace the infinite-dimensional arguments. The Fredholm notion for the generator is the graph-domain Fredholm notion.

## Relationship to prior work
Liang, Li and Qian (2026), Theorem 4.13, supply the frequency-side Hardy–Sobolev model and study boundedness of weighted composition operators, not this generator's Fredholm spectrum. Chalendar and Partington (2022/2023), Section 3, provide a general weighted-Laplace method for annular spectra of fixed composition dilations, together with adjoint eigenvector arguments. Their theorem's Zen-space weights are obtained by positive-measure Laplace transforms, unlike the increasing polynomial \(W_n\) here; moreover the annular fixed-time mechanism is already known in related contexts and is not offered alone as a novelty claim. The added result is the exact graph-domain Fredholm index and resolvent classification of the dilation generator, and the explicit shift from one-dimensional generator cokernels to infinite-dimensional sampled cokernels, giving a strict Fredholm-essential spectral mapping mismatch on the same natural function space. Schroderus (2016) covers spectra of individual half-plane composition maps on classical Hardy, weighted Bergman and homogeneous weighted Dirichlet spaces; Arvanitidis (2011) describes the generator on ordinary Hardy spaces. Neither cited analysis yields the paired inhomogeneous Hardy–Sobolev generator/sampled Fredholm classification.

## Limitations
The statements are for the Hilbert case, integer Sobolev orders \(n\ge1\), and pure real positive dilations only. They do not address arbitrary composition semigroups or multiplication perturbations. Fredholm-essential spectral mapping can fail for abstract semigroups; no claim of an abstract first example is made. The annulus is a related familiar fixed-time phenomenon; publication priority for this exact integrated generator-and-sampling classification could depend on broader asymptotically constant coefficient operator literature not explicitly indexed in searches. All verification beyond the analytic argument consists of finite self-checks; no independent validation is asserted.

## References
1. H. Liang, H. Li, and T. Qian, *Banach Hardy–Sobolev Spaces on the Upper Half-plane and Operator Theory*, arXiv:2603.13983v1 (first public March 14, 2026), especially Theorem 4.13 and Section 5. https://arxiv.org/html/2603.13983v1
2. I. Chalendar and J. R. Partington, *Composition operators on function spaces on the halfplane: spectra and semigroups*, arXiv:2204.05894v2, especially Sections 3–4. https://arxiv.org/pdf/2204.05894
3. R. Schroderus, *Spectra of linear fractional composition operators on the Hardy and weighted Bergman spaces of the half-plane*, arXiv:1605.01859v3. https://arxiv.org/pdf/1605.01859
4. A. G. Arvanitidis, *Semigroups of Composition Operators on Hardy Spaces of the Half-plane*, arXiv:1109.5275v1. https://arxiv.org/pdf/1109.5275
