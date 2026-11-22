# Sharp Hausdorff topology of the planar normal-line pseudometric at fixed perimeter

## Finding

Let \(K,L\subset\mathbb R^2\) be compact convex bodies with nonempty interior. Write \(P(K)\) for perimeter, \(\delta=d_H(K,L)\) for Euclidean Hausdorff distance, and \(d_N(K,L)\) for the Akopyan–Glazyrin normal-line pseudometric [1]. For the support function \(h_K(\theta)=\max_{x\in K}\langle x,(\cos\theta,\sin\theta)\rangle\), set \(f=h_K-h_L\).

**Theorem.** For every pair \(K,L\),
\[
d_N(K,L)=\frac12\int_0^{2\pi}|f'(\theta)|\,d\theta
\le\sqrt{2\pi\delta\bigl(P(K)+P(L)+2\pi\delta\bigr)}.
\]
Moreover \(d_N(K,L)=0\) precisely when \(f\) is constant, equivalently when one body is an outer Euclidean parallel body of the other. In particular, **on the class of all planar convex bodies of any one fixed positive perimeter \(P\)**, \(d_N\) is a genuine metric and
\[
\boxed{\delta\le d_N(K,L)\le 2\sqrt{\pi\delta(P+\pi\delta)}.}
\]
The coefficient \(1\) in the lower bound is optimal and strict whenever \(K\ne L\). The exponent \(1/2\) of the upper bound is optimal: for every \(\alpha>1/2\), no estimate \(d_N(K,L)\le C\delta^\alpha\) holds uniformly even among \(C^\infty\) strictly positively curved bodies of **one common perimeter \(3\pi/2\)** contained in the unit disk. Thus the normal-line metric and Hausdorff metric induce the same topology on every fixed-perimeter class, with an optimal uniform forward Hölder exponent.

## Assumptions and scope

All support functions are taken relative to a common fixed origin, although the assertions are translation independent when both bodies are translated together. The convex bodies need not be smooth or strictly convex. The derivative \(f'\) exists almost everywhere and is integrable. The normal-line pseudometric is \(\frac12\int_0^{2\pi}\operatorname{dist}(\ell_\theta(K),\ell_\theta(L))\,d\theta\), with almost-everywhere unique normal lines at the supporting points, exactly as defined in [1]. Hausdorff distance is measured without optimizing translations or rotations. A common perimeter is required only for the lower bound and metric nondegeneracy, not for the upper bound.

## Proof

**1. Normal-line identity.** Put \(u(\theta)=(\cos\theta,\sin\theta)\) and \(v(\theta)=(-\sin\theta,\cos\theta)\). At almost every normal direction the unique support point of \(K\) has coordinates \(h_Ku+h'_Kv\); see the support parametrization [3, §2], or obtain the tangential coefficient by differentiating \(h_K=\langle x_K,u\rangle\) at a differentiability direction. Its normal line, parallel to \(u\), meets the \(v\)-axis at tangential offset \(h'_K\). Consequently two such parallel lines are separated by \(|h'_K-h'_L|\). Integrating gives the first equality. In particular \(d_N=0\) if and only if \(f'=0\) almost everywhere, hence \(f\) is constant because support functions are Lipschitz. If \(h_K-h_L=c\ge0\), \(K=L+cB\); if \(c<0\), \(L=K+(-c)B\), using the additivity and injectivity of support functions.

**2. A bounded-variation interpolation inequality.** For any \(2\pi\)-periodic Lipschitz \(f\) whose distributional second derivative is a finite signed measure, write \(V=\lVert f''\rVert_{\mathrm{TV}}\) and \(\epsilon=\lVert f\rVert_\infty\). For every \(a>0\), the fundamental theorem of calculus with measure-valued second derivative gives, for almost every \(\theta\),
\[
 f(\theta+a)-f(\theta)=a f'(\theta)+\int_{(0,a)}(a-s)\,df''(\theta+s).
\]
Taking absolute values and integrating over one period, periodic Fubini gives
\[
\int_0^{2\pi}|f'|\le\frac{4\pi\epsilon}{a}+\frac{aV}{2}.
\]
The first term uses \(|f(\theta+a)-f(\theta)|\le2\epsilon\). The second uses \(\int_0^a(a-s)\,ds=a^2/2\) and translation invariance of the total mass of \(|f''|\). If \(V=0\), periodicity forces \(f\) to be constant. Otherwise optimizing at \(a=\sqrt{8\pi\epsilon/V}\) yields
\[
 \frac12\int_0^{2\pi}|f'|\le\sqrt{2\pi\epsilon V}.
\]
No restriction on \(a\) is necessary: \(f\) and its derivative measures are periodically extended to the real line.

**3. Apply curvature positivity.** For any planar convex body \(K\), the distribution \(\mu_K=h_K''+h_K\,d\theta\) is a nonnegative curvature-radius measure of total mass \(P(K)\). This follows first for smooth strictly convex curves from the radius-of-curvature formula and Cauchy's perimeter identity [3], then for all convex bodies by smooth support approximation or the standard distributional support-function characterization [4]. In particular,
\[
f''=\mu_K-\mu_L-f\,d\theta,
\qquad
\lVert f''\rVert_{\mathrm{TV}}\le P(K)+P(L)+2\pi\delta,
\]
since \(\lVert f\rVert_\infty=\delta\). Apply step 2 with \(\epsilon=\delta\) to obtain the stated bound. When \(P(K)=P(L)=P\), the upper bound reduces to \(2\sqrt{\pi\delta(P+\pi\delta)}\).

**4. Inverse estimate and strictness.** Cauchy's perimeter formula gives \(\int_0^{2\pi}f=P(K)-P(L)=0\) under equal perimeters. Write \(M=\max f\), \(m=\min f\). Unless \(f\equiv0\), \(m<0<M\). One full traverse of the circle goes from a minimum to a maximum and back, so \(\int|f'|\ge2(M-m)\). Thus \(d_N\ge M-m>\max\{|m|,M\}=\delta\) if \(K\ne L\), while both vanish for \(K=L\). This also proves that equal-perimeter zero pairs coincide.

**5. Sharpness of the inverse coefficient.** Fix \(r=3/4\). For \(0<\eta<1\), let \(b_\eta\) be a nonnegative, smooth, single-peaked, circular bump supported on an arc of angular radius \(\eta\), with maximum \(1\), increasing then decreasing, and mean \(c_\eta=(2\pi)^{-1}\int b_\eta\to0\). Put \(g_\eta=b_\eta-c_\eta\). Choose a sufficiently small \(s_\eta>0\) that the support functions \(h_0=r\) and \(h_1=r+s_\eta g_\eta\) satisfy \(h_1+h_1''>0\) and \(h_1<1\) everywhere. Both yield smooth strictly positively curved bodies contained in the unit disk, with the same perimeter \(2\pi r=3\pi/2\). Since \(\int|g_\eta'|=2\) and \(\lVert g_\eta\rVert_\infty=1-c_\eta\) for sufficiently small \(\eta\),
\[
 \frac{d_N(K_0,K_1)}{d_H(K_0,K_1)}=\frac{1}{1-c_\eta}\longrightarrow1.
\]
Thus the lower coefficient cannot be increased, despite strict inequality for distinct pairs.

**6. Sharpness of the Hölder exponent on one fixed-perimeter class.** For every integer \(n\ge2\), set \(r=3/4\), \(e_n=3/[8(n^2-1)]\), and choose the disk \(K_n\) and smooth body \(L_n\) with respective support functions \(h_{K_n}=r\) and \(h_{L_n}=r+e_n\cos(n\theta)\). The second curvature radius is
\[
 h_{L_n}+h_{L_n}''=r-(n^2-1)e_n\cos(n\theta)
 =\frac34-\frac38\cos(n\theta)\ge\frac38.
\]
The two bodies have exactly the same perimeter \(3\pi/2\), and both lie in the unit disk because \(r+e_n\le7/8\). Directly,
\[
 d_H(K_n,L_n)=e_n,\qquad d_N(K_n,L_n)=\frac{e_n n}{2}\int_0^{2\pi}|\sin(n\theta)|\,d\theta=2ne_n.
\]
For any fixed \(\alpha>1/2\), the ratio \(d_N/e_n^\alpha=2n e_n^{1-\alpha}\) diverges like a positive multiple of \(n^{2\alpha-1}\). Hence no greater uniform Hölder exponent is possible, even on one smooth, uniformly positively curved, fixed-perimeter family.

## Verification

The standalone file `verify_geometry.py` uses rational arithmetic to check all 399 harmonic witness parameter values from \(n=2\) through \(n=400\), numerical normal-line quadrature for the first 16 harmonics, four smooth-bump concentration regimes, and 75 deterministic random smooth positively curved support-function differences. It checks inclusion, positive curvature, exact harmonic distances and the proposed two-sided inequality. The verifier was run from the decoded attached file. These finite calculations are corroboration only; the universal bounds and optimal exponents follow from the six analytical steps above.

## Relationship to prior work

Akopyan and Glazyrin [1] introduced the normal-line pseudometric, its triangle inequality and Minkowski convexity, and used it for a planar total-perimeter inequality. Their paper does not formulate a Hausdorff stability estimate or resolve topology on fixed-perimeter classes. Hug and Schneider [2] proved sharp \(1/2\)-Hölder Hausdorff continuity for **support measures in a bounded-Lipschitz distance**; their metric is on measures of the normal bundle, not the \(L^1\) normal-line displacement of [1], and their statement does not yield either the displayed formula or the sharp inverse inequality. The support parametrization and curvature identities in [3,4] are classical inputs, not newly claimed discoveries. The one-dimensional bounded-variation interpolation in step 2 is elementary; the geometric contribution is the resulting complete comparison and its two independent sharpness witnesses for the pseudometric of [1].

## Limitations

The numerical coefficient in the upper bound is explicit but not claimed optimal. The result addresses planar convex bodies and the normal-line pseudometric, not Hausdorff estimates for higher-dimensional normal congruences. The inverse estimate is false without a perimeter normalization, as distinct Euclidean outer parallel bodies have zero normal-line distance. Existing abstract interpolation estimates may supply alternative proofs; exhaustive priority over all terminology and unpublished results is not asserted. Independent audit is not yet performed.

## References

1. A. Akopyan and A. Glazyrin, *On the total perimeter of disjoint convex bodies*, arXiv:2308.16340v1, first submitted 2023-08-30. https://arxiv.org/html/2308.16340v1
2. D. Hug and R. Schneider, *Hölder continuity for support measures of convex bodies*, arXiv:1501.06214, 2015. https://arxiv.org/abs/1501.06214
3. J. Allemann, N. Hungerbühler and M. Wasem, *Equilibria of Plane Convex Bodies*, Journal of Nonlinear Science 31 (2021), Article 86, §2. https://link.springer.com/article/10.1007/s00332-021-09740-2
4. I. Ftouhi and E. Zuazua, *Optimal Design of Sensors via Geometric Criteria*, Journal of Geometric Analysis 33 (2023), Article 253, §2.1. https://link.springer.com/article/10.1007/s12220-023-01301-1
