# Sharp local and global Fourier-intensity stability of two equal intervals

## Finding

The squared Fourier-intensity map of an indicator of two equal intervals has an *exact global gap-distance modulus*, an *exact two-parameter local Gram spectrum*, and a *sharp noise-indistinguishability threshold*. Let \(\ell>0\), \(g>0\), and
\[
f_{\ell,g}(x)=\mathbf1_{[0,\ell]}(x)+\mathbf1_{[\ell+g,2\ell+g]}(x),\qquad
I_{\ell,g}(\xi)=|\widehat f_{\ell,g}(\xi)|^2.
\]
For \(g,h>0\) and \(\delta=|g-h|\), define \(D_\ell(\delta)=\|I_{\ell,g}-I_{\ell,h}\|_{L^2(\mathbb R)}^2\). Then \(D_\ell\) is independent of the base gap and
\[
D_\ell(\delta)=
\begin{cases}
4\ell\delta^2-2\delta^3,&0\le\delta\le\ell,\\
\frac83\ell^3-\frac23(2\ell-\delta)^3,&\ell\le\delta\le2\ell,\\
\frac83\ell^3,&\delta\ge2\ell.
\end{cases}
\]
It increases strictly on \([0,2\ell]\) and is constant thereafter. Thus every pair of gap parameters produces distinct data, but widely separated gaps remain only a fixed distance apart in the data space.

For any noise radius \(\varepsilon\ge0\), two gap parameters can be compatible with one observed datum \(Y\in L^2(\mathbb R)\), satisfying \(\|Y-I_{\ell,g}\|_2,\|Y-I_{\ell,h}\|_2\le\varepsilon\), **if and only if** \(D_\ell(|g-h|)\le4\varepsilon^2\). In particular the exact radius at which compatible gap distances become unbounded is
\[
\varepsilon_{\rm crit}=\sqrt{\frac{2\ell^3}{3}}.
\]
For \(0\le\varepsilon<\varepsilon_{\rm crit}\), the optimal upper bound on the gap difference is \(D_\ell^{-1}(4\varepsilon^2)<2\ell\), where the inverse is taken on \([0,2\ell)\); it is attained by suitable positive gaps and the midpoint datum. The local small-noise expansion of this sharp bound is \(\varepsilon/\sqrt\ell+O(\varepsilon^2/\ell^2)\).

For simultaneous changes of the width and gap, the real Fréchet differential of \((\ell,g)\mapsto I_{\ell,g}\in L^2(\mathbb R)\) has exact squared-norm matrix
\[
G_{\ell,g}=
\begin{pmatrix}
16\ell&4\min\{\ell,g\}\\
4\min\{\ell,g\}&4\ell
\end{pmatrix}.
\]
Its eigenvalues (squared singular values of the differential) are
\[
\lambda_{\pm}=2\left(5\ell\pm\sqrt{9\ell^2+4\min\{\ell,g\}^2}\right).
\]
In particular \(\lambda_->0\) for every \(\ell,g>0\); the local linearized condition number is \(\sqrt{\lambda_+/\lambda_-}\), rises as \(g/\ell\) grows from zero to one, and is exactly \(\sqrt{(5+\sqrt{13})/(5-\sqrt{13})}\) for \(g\ge\ell\). This shows that globally saturated gap separation and nondegenerate local differential stability coexist.

## Assumptions and scope

Fourier normalization is \(\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi i\xi x}\,dx\). The model consists of **exactly two** disjoint intervals with a **shared unknown positive length** \(\ell\) and a **positive interior gap** \(g\). Translation and reflection are fixed by the canonical placement above; both leave intensity unchanged. The data are complete continuous squared Fourier magnitudes as elements of real \(L^2(\mathbb R)\), using its ordinary Lebesgue norm. The global distance and noise-radius claims compare models with the same known width \(\ell\). The local Gram statement allows the width and gap to vary jointly.

## Proof

Put \(T_\ell(t)=(\ell-|t|)_+\). The inverse Fourier transform of \(I_{\ell,g}\) is the autocorrelation
\[
C_{\ell,g}(t)=2T_\ell(t)+T_\ell(t-\ell-g)+T_\ell(t+\ell+g).
\]
Indeed the two diagonal interval-pair correlations each equal \(T_\ell\); the two mixed correlations are its translates. As the Fourier transform is unitary on \(L^2(\mathbb R)\) under the stated convention,
\(\|I_{\ell,g}-I_{\ell,h}\|_2=\|C_{\ell,g}-C_{\ell,h}\|_2\).

For \(g,h>0\), the *positive-lag* translated triangles have supports \([g,g+2\ell]\) and \([h,h+2\ell]\); the *negative-lag* triangles have negative supports. Hence positive and negative differences do not overlap, and the common central term cancels. Translation invariance gives
\[
\|C_{\ell,g}-C_{\ell,h}\|_2^2
=2\|T_\ell(\cdot)-T_\ell(\cdot-\delta)\|_2^2
=4\bigl(R_\ell(0)-R_\ell(\delta)\bigr),
\]
where \(R_\ell(\delta)=\int_{\mathbb R}T_\ell(t)T_\ell(t-\delta)\,dt\). Direct integration at its three breakpoints yields
\[
R_\ell(\delta)=
\begin{cases}
\frac23\ell^3-\ell\delta^2+\frac12\delta^3,&0\le\delta\le\ell,\\
\frac16(2\ell-\delta)^3,&\ell\le\delta\le2\ell,\\
0,&\delta\ge2\ell.
\end{cases}
\]
Substitution proves the global cubic formula, including continuity at both breakpoints. Its first derivative is \(8\ell\delta-6\delta^2>0\) for \(0<\delta<\ell\), and \(2(2\ell-\delta)^2>0\) for \(\ell<\delta<2\ell\); the constant plateau is thus sharp.

For any two points of the Hilbert space \(L^2\), their closed radius-\(\varepsilon\) balls intersect exactly when their separation is at most \(2\varepsilon\): necessity is the triangle inequality; sufficiency follows by choosing their midpoint. Apply this to the intensity functions and the just-proved formula. The plateau \(D_\ell=8\ell^3/3\) proves the exact critical radius. The expansion at zero follows by inversion of \(D_\ell(\delta)=4\ell\delta^2+O(\delta^3)\).

For the differential, on the positive half-axis and at almost every \(t>0\), differentiation of the triangle translates yields
\[
\partial_\ell C_{\ell,g}(t)
=2\mathbf1_{(0,\ell)}(t)+2\mathbf1_{(g+\ell,g+2\ell)}(t),
\quad
\partial_g C_{\ell,g}(t)
=-\mathbf1_{(g,g+\ell)}(t)+\mathbf1_{(g+\ell,g+2\ell)}(t).
\]
Both derivatives are even in \(t\). A moving piecewise-linear breakpoint contributes \(O(|\Delta|^{3/2})\) in \(L^2\) after subtracting its linearized term; thus these a.e. derivatives are the actual Fréchet derivative in the data Hilbert space, not merely formal pointwise derivatives. Their squared norms are \(16\ell\) and \(4\ell\), respectively. Their inner product equals
\(4\bigl(\ell-(\ell-g)_+\bigr)=4\min\{\ell,g\}\), because the negative strip overlaps the central interval in length \((\ell-g)_+\). Plancherel gives the same Gram matrix for the Fourier-intensity derivative. The characteristic polynomial of this real symmetric matrix yields the displayed two eigenvalues. For \(m=\min\{\ell,g\}\le\ell\), \(\sqrt{9\ell^2+4m^2}<5\ell\), proving positivity; monotonicity in \(m\) proves the local condition-number claims.

## Verification

The accompanying `CHECK.py` independently integrates the original piecewise-linear autocorrelation difference (without assuming its distance formula), independently integrates each derivative inner product, compares eigenvalues with the proposed matrix, checks L² finite-difference approximations and numerically inverts the analytic Fourier-intensity formula by quadrature. It reports **616 successful deterministic assertions**. The universally quantified theorem follows from the piecewise-integration proof above, not from a finite parameter scan. Run with Python 3 and NumPy 2 or later as described by `requirements.txt`.

## Relationship to prior work

Xia and Xu (2026, arXiv:2606.19855, first public June 18, 2026) prove uniqueness of up-to-two-interval indicators from their Fourier magnitudes and give nonsharp, small-noise estimates for general two-interval configurations (Theorem 1.3). Their Remark 1.5 identifies nonuniformity for widely separated gaps. The present theorem does **not** claim their uniqueness result anew: it computes a sharp **global** fixed-equal-width intensity distance, an exact critical indistinguishability noise radius, and the **complete local two-parameter singular spectrum**. These exact numerical invariants are not implied by the bounds displayed in their Theorem 1.3 or Remark 1.5.

Grohs, Koppensteiner and Rathmair (2019 preprint; 2020 survey, arXiv:1901.07911) review general uniqueness and stability mechanisms for phase retrieval and Fourier measurements; their reviewed results do not specify the above equal-interval gap geometry or threshold. Classical triangle-convolution and Plancherel identities are used without originality claims.

## Limitations

The formula is specifically for equal, positive interval lengths; unequal lengths need a different piecewise analysis. The global gap modulus assumes *fixed width* for the two candidates; the local Gram allows simultaneous small width/gap perturbations. Intensity errors are measured in the complete continuum \(L^2(\mathbb R)\) norm. No discrete sampling, bandwidth truncation, noisy estimator, statistically optimal estimator, or recovery for arbitrary finite unions is provided. Global noise ambiguity does not contradict local invertibility. Independent literature priority and independent mathematical auditing remain open; elementary covariogram identities could have been used elsewhere to derive an equivalent formula.

## References

1. Yu Xia and Zhiqiang Xu, *Fourier Phase Retrieval for Finite Unions of Intervals*, arXiv:2606.19855 (first public June 18, 2026), https://arxiv.org/abs/2606.19855.
2. Philipp Grohs, Sarah Koppensteiner, Martin Rathmair, *Phase Retrieval: Uniqueness and Stability*, arXiv:1901.07911 (first public January 23, 2019), SIAM Review 62 (2020), https://arxiv.org/abs/1901.07911.
