# Strictly convex bodies admit no exponential Riesz bases

## Result

Let \(n\ge 2\), let \(K\subset\mathbb R^n\) be a compact strictly convex set with nonempty interior, and put
\[
\Omega=\operatorname{int} K.
\]
Then \(L^2(\Omega)\) admits no Riesz basis consisting of exponentials
\[
e_\lambda(x)=e^{2\pi i\lambda\cdot x}.
\]

No boundary smoothness is assumed.

The geometric input is the following translation lemma.

### Translation lemma

For every nonzero \(h\in\mathbb R^n\),
\[
\mathcal H^{n-1}\bigl(\partial K\cap(\partial K-h)\bigr)=0.
\]

Together with the boundary-measure criterion in Ortega-Cerdà, *There are no Riesz bases of exponentials in balls and triangles* (arXiv:2609.18426, Remark 6.4), this proves the theorem.

This gives a regularity-free strictly-convex counterpart to Ortega-Cerdà's \(C^2\)-convex theorem. The two statements are complementary: a \(C^2\) convex body may have flat boundary pieces and need not be strictly convex, while the theorem here applies to strictly convex bodies whose boundaries need not be \(C^2\). For example, for every \(1<p<2\),
\[
\Omega_p=\left\{x\in\mathbb R^n:\sum_{j=1}^n |x_j|^p<1\right\}
\]
is covered although its boundary is not \(C^2\) at points with a zero coordinate.

## Proof of the translation lemma

Fix \(h\ne0\). After an orthogonal change of coordinates write
\[
h=t e_n,\qquad t>0,
\]
and let \(\pi:\mathbb R^n\to\mathbb R^{n-1}\) be projection onto the first \(n-1\) coordinates. Put \(D=\pi(K)\).

For \(z\in D\), define the endpoints of the vertical section
\[
a(z)=\min\{s:(z,s)\in K\},\qquad
b(z)=\max\{s:(z,s)\in K\}.
\]
For \(z\in\operatorname{int}D\), the section is the nondegenerate interval
\[
K\cap(\{z\}\times\mathbb R)=\{z\}\times[a(z),b(z)].
\]
The function \(a\) is convex and \(b\) is concave on \(\operatorname{int}D\).

Strict convexity makes these inequalities strict. Indeed, if \(z_0\ne z_1\) are in \(\operatorname{int}D\), then
\[
p_i=(z_i,b(z_i))\in\partial K.
\]
For \(0<\lambda<1\), strict convexity places
\[
(1-\lambda)p_0+\lambda p_1
\]
in \(\operatorname{int}K\). At
\(z_\lambda=(1-\lambda)z_0+\lambda z_1\), its last coordinate is therefore strictly below \(b(z_\lambda)\). Thus \(b\) is strictly concave. The same argument at the lower endpoints shows that \(a\) is strictly convex. Consequently the chord-length function
\[
L(z)=b(z)-a(z)
\]
is strictly concave on \(\operatorname{int}D\).

Now set
\[
E=\partial K\cap(\partial K-t e_n).
\]
If \(x=(z,s)\in E\), then both \(x\) and \(x+t e_n\) lie on \(\partial K\). The point \(z\) cannot lie on \(\partial D\): otherwise the vertical section of \(K\) over \(z\) would have to contain two distinct points, hence a nontrivial boundary segment, contrary to strict convexity. Hence \(z\in\operatorname{int}D\).

For \(z\in\operatorname{int}D\), a point \((z,s)\) with
\[
a(z)<s<b(z)
\]
is an interior point of \(K\). Therefore the two boundary points in the same vertical section must be its two endpoints:
\[
s=a(z),\qquad s+t=b(z).
\]
In particular,
\[
L(z)=t.
\]
Thus
\[
E\subset \{(z,a(z)):z\in Z_t\},
\qquad
Z_t=\{z\in\operatorname{int}D:L(z)=t\}.
\]

A level set of a strictly concave function on a convex open set has zero \((n-1)\)-dimensional Lebesgue measure. To see this directly, restrict \(L\) to lines parallel to any fixed coordinate direction. On each such line it is strictly concave, so the equation \(L=t\) has at most two solutions. Fubini's theorem gives
\[
|Z_t|_{n-1}=0.
\]

Finally, a finite convex function is locally Lipschitz in the interior of its domain. Exhaust \(\operatorname{int}D\) by compact subsets \(D_j\Subset\operatorname{int}D\). On each \(D_j\), the graph map
\[
z\longmapsto (z,a(z))
\]
is Lipschitz. Hence the image of \(Z_t\cap D_j\), which has zero \((n-1)\)-dimensional Lebesgue measure, has zero \(\mathcal H^{n-1}\)-measure. Taking the countable union over \(j\) yields
\[
\mathcal H^{n-1}(E)=0.
\]
This proves the translation lemma.

## Deduction of the Riesz-basis obstruction

Let
\[
S=\partial K,\qquad \nu=\mathcal H^{n-1}|_S.
\]
A convex body has boundary of \(n\)-dimensional Lebesgue measure zero and finite positive surface measure, so \(\nu\) is a finite nonzero positive Borel measure. The translation lemma gives
\[
\nu\bigl(S\cap(S-\theta)\bigr)=0
\qquad(\theta\ne0).
\]

Every neighborhood of every \(x\in S\) meets \(\Omega\) in a set of positive Lebesgue measure: choose an interior point arbitrarily close to \(x\), then use openness. It also meets \(\mathbb R^n\setminus K\) in a set of positive measure, because a supporting hyperplane at \(x\) leaves an open half-neighborhood outside \(K\).

Therefore all hypotheses of Ortega-Cerdà's boundary-measure criterion (Remark 6.4 of arXiv:2609.18426) hold with surface measure on the entire boundary. That criterion excludes an exponential Riesz basis in \(L^2(\Omega)\).

## Context and comparison with recent work

Ortega-Cerdà (arXiv:2609.18426, submitted 16 September 2026) proved nonexistence for balls, triangles, and every nonempty bounded convex open set with \(C^2\) boundary. His Remark 6.4 isolates the more general boundary-measure condition used above. In the \(C^2\) convex case, his Section 8 obtains the required translation non-overlap from a positively curved patch.

Wan (arXiv:2609.16674, submitted in September 2026) independently proved nonexistence for balls and triangles and for several broader families, including certain convex polytopes, spherical shells, finite unions, affine images, and products. The theorem stated there does not include arbitrary strictly convex bodies.

Positive results for convex polytopes go in a different direction: Debernardi and Lev proved that centrally symmetric convex polytopes whose faces of every dimension are centrally symmetric admit exponential Riesz bases. Such polytopes are not strictly convex when \(n\ge2\), so there is no conflict.

## Scope of the contribution

The standard convex-geometry facts used above (convex/concave section endpoints, local Lipschitz regularity of finite convex functions, and basic surface-measure properties of convex bodies) are not claimed as new. Ortega-Cerdà's boundary-measure criterion is also not claimed as new.

The contribution is the translation lemma for arbitrary strictly convex bodies in the form needed by that criterion, and the resulting removal of all boundary-regularity assumptions in the strictly convex class.

## Limitations

- The theorem requires \(n\ge2\). In one dimension an interval has an orthogonal exponential basis.
- It does not subsume Ortega-Cerdà's \(C^2\)-convex result, since a smooth convex body can contain flat boundary pieces and fail strict convexity.
- It gives a nonexistence result, not quantitative lower bounds on Riesz constants.
- It does not classify general nonsmooth convex bodies with boundary segments or higher-dimensional faces.
- Originality is asserted only to the best of our knowledge. The two principal September 2026 preprints are very recent, so contemporaneous unindexed observations remain a residual risk.

## References

1. J. Ortega-Cerdà, *There are no Riesz bases of exponentials in balls and triangles*, arXiv:2609.18426 (2026). https://arxiv.org/abs/2609.18426
2. Z. Wan, *Sets with no Riesz bases of exponentials*, arXiv:2609.16674 (2026). https://arxiv.org/abs/2609.16674
3. A. Debernardi and N. Lev, *Riesz bases of exponentials for convex polytopes with symmetric faces*, J. Eur. Math. Soc. 24 (2022), 3017–3029. https://doi.org/10.4171/JEMS/1158
