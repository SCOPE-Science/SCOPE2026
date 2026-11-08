# Sharp displacement growth and the endpoint continuity transition in Gaussian mixed-norm Fock spaces

## Finding

For every \(\alpha>0\), let \(\mathcal F_{\alpha}^{\infty,q}\) be the space of entire functions equipped, for \(1\le q<\infty\), with
\[
\|f\|_{\alpha,\infty,q}^{q}
=q\alpha\int_0^\infty \left[e^{-\alpha r^2/2}\max_{|z|=r}|f(z)|\right]^q r\,dr,
\]
and, for \(q=\infty\), with \(\|f\|_{\alpha,\infty,\infty}=\sup_{z\in\mathbb C}|f(z)|e^{-\alpha|z|^2/2}\). Put
\[
(W_af)(z)=e^{\alpha\overline a z-\alpha|a|^2/2}f(z-a),\qquad a\in\mathbb C.
\]
Then each \(W_a\) is a bounded invertible operator on every one of these spaces. For each fixed \(1\le q<\infty\) there are constants \(0<c_q\le C_q<\infty\), independent of \(\alpha>0\) and \(a\in\mathbb C\), such that
\[
 c_q(1+\sqrt\alpha|a|)^{1/q}
 \le \|W_a\|_{\mathcal F_{\alpha}^{\infty,q}\to\mathcal F_{\alpha}^{\infty,q}}
 \le C_q(1+\sqrt\alpha|a|)^{1/q}.
\]
At \(q=\infty\), \(\|W_a\|=1\) exactly. More precisely, for finite \(q\), with \(A=|a|\), the constant function gives the exact lower bound
\[
 \|W_a\|^{q}\ge e^{-q\alpha A^2/2}
 +A\sqrt{\frac{\pi q\alpha}{2}}
 \left(1+\operatorname{erf}\left(A\sqrt{\frac{q\alpha}{2}}\right)\right),
\]
whose right side is asymptotic to \(\sqrt{2\pi q\alpha}\,A\) as \(A\to\infty\).

For every nonzero \(a\), and all \(1\le q\le\infty\), the spectrum is the entire unit circle:
\[
\sigma_{\mathcal F_{\alpha}^{\infty,q}}(W_a)=\{\lambda\in\mathbb C:|\lambda|=1\}.
\]
For finite \(q\), the projective displacement family is strongly continuous and \(\|W_a^n\|\asymp_{\alpha,q,a} n^{1/q}\) as \(n\to\infty\) for fixed nonzero \(a\). At \(q=\infty\) the family is isometric but is not strongly continuous at the identity on the full (large) endpoint space.

## Assumptions and scope

The complex plane has its usual Euclidean modulus. All functions are entire. The angular exponent is exactly \(p=\infty\), the radial exponent is in the complete Banach range \(1\le q\le\infty\), and the Gaussian is \(e^{-\alpha|z|^2/2}\) with \(\alpha>0\). The measure \(q\alpha r\,dr\) for finite \(q\) is a harmless normalization of the radial Gaussian mixed norm, chosen so that \(\|1\|=1\); using a constant multiple does not change operator norms. All implied constants in the two-sided bound depend only on \(q\). Spectral assertions concern a fixed nonzero displacement.

## Proof

**1. Reduction and local mass estimate.** The dilation \(z\mapsto \sqrt\alpha z\) conjugates the operators and norms to the case \(\alpha=1\), so prove the upper estimate in that case. Set \(h_f(z)=|f(z)|e^{-|z|^2/2}\) and \(M_f(s)=\max_{|z|=s}h_f(z)\). For fixed \(z\), the function \(w\mapsto f(z+w)e^{-\overline z w}\) is entire. Subharmonicity of its \(q\)-th absolute power and the unit-disk submean inequality imply
\[
h_f(z)^q\le \frac{e^{q/2}}\pi\int_{B(z,1)}h_f(u)^q\,dA(u).
\]
At a circle of radius \(v\), the angular measure of \(B(z,1)\) is bounded by a constant times \(\min\{1,v^{-1}\}\). Taking the maximum over \(|z|=s\) gives, with a constant \(L_q<\infty\),
\[
M_f(s)^q\le L_q\int_{\max(0,s-1)}^{s+1}M_f(v)^q\min(v,1)\,dv. \tag{1}
\]
This estimate is the analytic step that prevents arbitrarily thin radial spikes; it holds also for \(s=0\).

**2. A sharp radial transport bound.** The exact modulus identity \(h_{W_af}(z)=h_f(z-a)\) yields, for \(A=|a|\),
\[
M_{W_af}(r)\le \sup_{|r-A|\le s\le r+A}M_f(s).
\]
Apply (1) to each \(s\) and enlarge the interval of integration (all integrands are nonnegative). Tonelli's theorem then gives
\[
\int_0^\infty M_{W_af}(r)^q r\,dr
 \le L_q\int_0^\infty M_f(v)^q\min(v,1)J_A(v)\,dv,
\]
where
\[
J_A(v)=\frac12\left[(A+v+1)^2-\big(\max\{0,|A-v|-1\}\big)^2\right].
\]
Indeed, the allowed radii are exactly \(\max\{0,|A-v|-1\}\le r\le A+v+1\). The interval length is at most \(2\min(A+1,v+1)\) and its maximum radius is \(A+v+1\). Splitting into \(v\le1\), \(1<v\le A\), and \(v>\max(1,A)\) proves the uniform elementary estimate
\[
\min(v,1)J_A(v)\le 8(1+A)v\qquad (A\ge0,\ v>0). \tag{2}
\]
Therefore \(\|W_af\|_{1,\infty,q}^q\le8L_q(1+A)\|f\|_{1,\infty,q}^q\). Scaling back proves the asserted upper bound uniformly in \(\alpha\).

**3. Exact test function and optimality.** The constant function has norm one. Its displacement satisfies \(h_{W_a1}(z)=e^{-|z-a|^2/2}\) at \(\alpha=1\), so the supremum on radius \(r\) equals \(e^{-(r-A)^2/2}\). Completing the square, for \(c=q\alpha/2\), gives
\[
\|W_a1\|^q=q\alpha\int_0^\infty r e^{-c(r-A)^2}\,dr
=e^{-cA^2}+A\sqrt{\pi c}(1+\operatorname{erf}(A\sqrt c)).
\]
The ratio is continuous, positive at \(A=0\), and grows like \(\sqrt{2\pi q\alpha}A\). Hence it gives the matching lower power for every \(A\ge0\), and proves that the exponent \(1/q\) cannot be decreased.

**4. Projective group and spectrum.** Direct substitution shows
\[
W_aW_b=e^{i\alpha\operatorname{Im}(\overline a b)}W_{a+b},
\qquad W_a^{-1}=W_{-a},\qquad W_a^n=W_{na}.
\]
Thus the spectral radii of \(W_a\) and \(W_a^{-1}\) both equal one by the norm bounds and the Banach-space spectral radius formula. Since \(W_a\) is invertible, its nonempty spectrum is contained in the unit circle. Conjugation gives
\[
W_bW_aW_b^{-1}=e^{2i\alpha\operatorname{Im}(\overline b a)}W_a.
\]
For \(a\ne0\), the phase spans the entire circle as \(b\) varies. Similarity therefore makes the nonempty spectrum invariant under all unit rotations; it must be the whole unit circle. For \(q=\infty\), the identity for \(h_{W_af}\) makes every \(W_a\) an isometry, so the same spectral argument applies.

**5. Continuity transition.** For finite \(q\), polynomials are dense in the Gaussian mixed-norm space (also obtainable by radial dilation and Taylor approximation). On a polynomial, \(W_af\to f\) in norm as \(a\to0\) by pointwise convergence and an integrable Gaussian majorant uniform for \(|a|\le1\). The local uniform operator bound extends this convergence to every function, proving strong continuity. Conversely, at \(\alpha=1\), the function \(f(z)=e^{z^2/2}\) has \(\|f\|_{1,\infty,\infty}=1\). For every nonzero real \(t\), evaluation on the real axis shows
\[
\|W_{it}f-f\|_{1,\infty,\infty}\ge 1+e^{-t^2};
\]
indeed \((W_{it}f)(x)e^{-x^2/2}=e^{-t^2}e^{-2itx}\), and choose \(x=\pi/(2t)\). Hence strong continuity fails at this endpoint.

## Verification

The accompanying standalone `CHECK.py` numerically tests the exact coherent-state norm identity, the projective Weyl composition law, the radial transport inequality (2), and the explicit endpoint discontinuity witness. All calculations are checks of finite instances and not substitutes for the analytical argument above. The source normalization can be changed by a constant factor without affecting the operator-bound conclusion.

## Relationship to prior work

Fang and Tien, *Sharp Gaussian Mixed-Norm Theory for Fock Spaces* (2026, arXiv:2609.26821), establish the ambient radial-angular spaces, endpoint norms, completeness, and polynomial density; their principal results concern growth, atomic decomposition, Carleson measures, and duality. Fang and Tien, *Sampling and Interpolation in Gaussian Mixed-Norm Fock Spaces* (2026, arXiv:2609.23572), prove density criteria for sampling and interpolation, not displacement-operator norm growth. Dileep, Fang and Tien, *Positive Toeplitz Operators Between Gaussian Mixed-Norm Fock Spaces* (2026, arXiv:2610.40236), characterize positive Toeplitz operators rather than the Gaussian-compensated translation group.

Seyoum and Mengestie, *Spectrums and Uniform Mean Ergodicity of Weighted Composition Operators on Fock Spaces* (2022, DOI:10.1007/s40840-021-01203-x), determine the unit-circle spectrum for ordinary one-exponent Fock spaces; this **already covers the classical diagonal endpoint** and is not claimed as new here. The issue addressed here is instead the sharp, nonuniform polynomial displacement growth and the continuity transition on the distinct radial-supremum/outer-radial mixed-norm family. A published result on weighted translations for radial power Fock norms likewise concerns a different, single-exponent norm. The standard Weyl cocycle and its Banach-spectral consequences are classical ingredients, not claimed as independent discoveries.

## Limitations

The result gives the optimal **growth exponent**, not the exact operator norm or its limiting leading constant. The spectral circle is shared with classical Weyl representations; the new conclusion concerns the different mixed-norm growth and endpoint regularity. Strong continuity is stated only for the Banach radial range \(1\le q<\infty\). The theorem does not assert estimates for finite angular exponent \(p\), arbitrary radial weights, or higher-dimensional mixed norms. Equivalent coverage in older weighted-composition literature remains a publication-priority risk, and independent validation has not been performed.

## References

1. X. Fang and P. T. Tien, *Sharp Gaussian Mixed-Norm Theory for Fock Spaces*, arXiv:2609.26821, first submitted 2026-09-20. https://arxiv.org/abs/2609.26821
2. X. Fang and P. T. Tien, *Sampling and Interpolation in Gaussian Mixed-Norm Fock Spaces*, arXiv:2609.23572, first submitted 2026-09-20. https://arxiv.org/abs/2609.23572
3. D. K. Dileep, X. Fang and P. T. Tien, *Positive Toeplitz Operators Between Gaussian Mixed-Norm Fock Spaces*, arXiv:2610.40236, first submitted 2026-10-29. https://arxiv.org/abs/2610.40236
4. W. Seyoum and T. Mengestie, *Spectrums and Uniform Mean Ergodicity of Weighted Composition Operators on Fock Spaces*, Bull. Malays. Math. Sci. Soc. 45 (2022), 455–481. https://doi.org/10.1007/s40840-021-01203-x
