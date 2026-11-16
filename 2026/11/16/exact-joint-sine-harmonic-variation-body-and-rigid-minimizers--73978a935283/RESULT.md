# Exact joint sine-harmonic variation body and rigid minimizers

## Finding
Let \(n\ge1\) be an integer and let \(f:\mathbb T\to\mathbb R\) be a real function of bounded variation on the circle \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\). Its standard real sine coefficients are
\[
b_k(f)=\frac1\pi\int_0^{2\pi}f(t)\sin(kt)\,dt\qquad (k\ge1).
\]
Define the normalized adjacent-harmonic data \(X=\pi n b_n(f)\), \(Y=2\pi n b_{2n}(f)\). Then the exact set of possible \((X,Y)\) when \(\operatorname{Var}_{\mathbb T}(f)\le1\) is
\[
\mathcal K=\left\{(X,Y)\in\mathbb R^2:\ |X|\le1,\quad |Y|\le1-\bigl(\max\{0,2|X|-1\}\bigr)^2\right\}.
\]
In particular, the individually sharp inequalities \(|X|,|Y|\le1\) are not jointly sharp on the four outer corners of their bounding square. The area of \(\mathcal K\) is exactly \(10/3\).

Equivalently, prescribing arbitrary real data \((X,Y)\), the *minimum circular total variation* over all periodic real BV interpolants is
\[
\mathsf V_*(X,Y)=\begin{cases}
|Y|,& |Y|\ge2|X|,\\[2pt]
\displaystyle\frac{4|X|^2}{4|X|-|Y|},&0\le|Y|\le2|X|,\quad |X|>0,\\[5pt]
0,&X=Y=0.
\end{cases}
\]
At the common boundary \(|Y|=2|X|\), the branches agree. The minimum is attained. The prescribed frequencies \(n\) and \(2n\) are arbitrary; none of the constants depends on \(n\).

The upper boundary \(Y>0\) has the following rigidity property. If \(\operatorname{Var}_{\mathbb T}(f)=1\) and \((X,Y)\) lies on that boundary, write the Jordan decomposition of its distributional circular derivative as \(df=\nu_+-\nu_-\). Push forward the probability measures \(2\nu_+\) and \(2\nu_-\) by \(u=\cos(nt)\): call them \(p_+\) and \(p_-\). For \(|X|\le1/2\) and \(Y=1\), necessarily
\[
p_+=\frac{1+2X}{2}\delta_1+\frac{1-2X}{2}\delta_{-1},\qquad p_-=\delta_0.
\]
For \(1/2<|X|\le1\) and \(Y=1-(2|X|-1)^2\), necessarily
\[
p_+=\delta_{\operatorname{sgn}X},\qquad
p_-=\delta_{\operatorname{sgn}X\,(1-2|X|)}.
\]
Conversely each such pair is realized by a circular step function with two or three jumps. The lower boundary follows by reversing the signed derivative and reflecting \(u\mapsto-u\). These are complete descriptions of the *pushforward* Jordan measures, not unique locations on the original circle: for \(n>1\), a cosine value has several preimages.

## Assumptions and scope
The circle variation is defined as the total mass \(\|df\|_{\mathrm{TV}}\) of the distributional derivative of a periodic real BV function. A canonical right-continuous representative may be used; pointwise changes on exceptional sets do not change its Fourier data. Derivatives are real finite signed Borel measures on \(\mathbb T\) of total mass zero. Conversely, every real finite signed measure with zero total mass is the circular distributional derivative of some periodic BV function, unique up to an additive constant. No smoothness, monotonicity or parity of \(f\) is assumed. Both frequencies are positive and distinct by construction.

## Proof
**1. Circular Stieltjes reduction.** Periodic integration by parts gives, for every positive integer \(k\),
\[
k\int_0^{2\pi} f(t)\sin(kt)\,dt=\int_{\mathbb T}\cos(kt)\,df(t).
\]
Thus, writing \(\nu=df\) and \(u(t)=\cos(nt)\),
\[
X=\int u\,d\nu,\qquad
Y=\int(2u^2-1)\,d\nu=2\int u^2\,d\nu.
\]
The constant in the second expression disappears because \(\nu(\mathbb T)=0\).

**2. The two moment bodies.** If \(\|\nu\|_{\mathrm{TV}}\le1\), the positive and negative Jordan masses both equal \(m\le1/2\). To describe the attainable set, augment both parts by the same positive measure of mass \(1/2-m\), leaving their difference unchanged. Consequently every attainable \((X,Y)\) has the form
\[
X=(a-b)/2,\qquad Y=r-s,
\]
where \(a,b\in[-1,1]\), \(a^2\le r\le1\), \(b^2\le s\le1\). These inequalities characterize the first two moments of probability measures on \([-1,1]\): \(\operatorname{Var}(u)\ge0\), \(u^2\le1\), and every intermediate second moment occurs by mixing a point mass at the mean with a suitable mixture at the two endpoints. Conversely, any such pair of probability measures can be lifted through a measurable choice of the preimages of \(u=\cos(nt)\), and half their signed difference has total variation at most one and total mass zero. Its circular antiderivative supplies the required BV function. This proves equivalence rather than just a bound.

**3. Exact vertical optimization.** Fix \(X\in[-1,1]\). The constraint \(a-b=2X\) makes the possible negative-part means \(b\) range over
\[
[-1,1]\cap[-1-2X,1-2X].
\]
For such \(b\), the largest possible \(Y=r-s\) is \(1-b^2\), and its maximizer uses \(r=1\), \(s=b^2\). Minimizing \(|b|\) over this interval gives \(\max\{0,2|X|-1\}\). Hence
\[
Y\le1-\bigl(\max\{0,2|X|-1\}\bigr)^2.
\]
Changing \(\nu\) to minus its pushforward under \(u\mapsto-u\) preserves \(X\) and negates \(Y\); the lower bound is the negative of the upper. The attainable set is convex, since signed derivative measures of variation at most one form a convex set. Therefore every point between the two sharp endpoints at each \(X\) is attainable. Integration of this vertical width yields \(4[1/2+1/2-1/6]=10/3\) for the area.

**4. Sharp inverse variation.** The feasible body at variation budget \(V\ge0\) is \(V\mathcal K\) by homogeneity. Put \(a=|X|\), \(b=|Y|\). In the flat branch the smallest feasible \(V\) is \(b\), which lies in that branch exactly if \(b\ge2a\). In the curved branch \(a\le V\le2a\), the inequality reads
\[
b\le V\left[1-\left(\frac{2a}{V}-1\right)^2\right]
=4a\left(1-\frac{a}{V}\right).
\]
Solving at equality gives \(V=4a^2/(4a-b)\), which belongs to \([a,2a]\) when \(0\le b\le2a\). This proves the stated sharp norm and establishes that each prescribed data pair has a minimum-variation realization.

**5. Equality supports and finite-jump attainment.** A nonzero point on the boundary of the full-dimensional convex body \(\mathcal K\) requires full variation one; otherwise radial enlargement would stay in \(\mathcal K\), contradicting boundary extremality. Equality in Step 3 forces \(r=1\), hence positive-part support in \(\{-1,1\}\), and \(s=b^2\), hence negative-part support at its mean alone. For \(|X|<1/2\) the unique optimal mean is \(b=0\), and the positive endpoint weights are fixed by \(a=2X\). For \(|X|>1/2\), the unique optimal mean is \(b=\operatorname{sgn}(X)(1-2|X|)\), forcing \(a=\operatorname{sgn}(X)\) and hence an endpoint point mass. The boundary formulas, including their meeting points, follow. Their supports are disjoint and can be lifted to two or three points of \(\mathbb T\), so they are genuine Jordan decompositions with exactly the required variation. Interior points follow by mixing the two bounding step derivatives, requiring at most six atom locations before cancellations. All minimizers for nonzero prescribed data are obtained by scaling these boundary descriptions to \(\mathsf V_*(X,Y)\). The zero data have the constant functions as their zero-variation minimizers. This completes the classification.

## Verification
A standalone standard-library script checks the rational versions of both boundary constructions, exact moments, symmetry maps, convex combinations, and the inverse-variation formula using fractions. The finite tests probe the derived formulas but do not replace Steps 1–5, which prove the continuum and all-frequency statements. Run `python3 CHECK.py` from the directory containing this document and the script; no external packages are necessary.

## Relationship to prior work
V. Sluchak, *Bounds for Orthogonal Expansion Coefficients via Weighted Primitives*, arXiv:2611.04067v1 (November 2, 2026), proves sharp **one-coefficient** variation bounds by integration by parts (Theorem 1, Section 5.1) and uses those bounds simultaneously as sufficient constraints in Section 10.2. These bounds alone give the square \(|X|,|Y|\le1\); they do not state its nonrectangular exact attainable subset, inverse minimum-variation formula, or the equality support classification. The positive one-dimensional truncated moment problem and Jordan decomposition are classical; the argument explicitly uses them rather than presenting them as new. In contrast with the standard positive measure moment problem, the current problem concerns a *zero-mass signed derivative* with its total variation budget split equally between positive and negative parts, and computes its full two-harmonic image and minimizers.

## Limitations
Only the real sine coefficients at frequencies \(n\) and \(2n\) are constrained; the cosine coefficients, other frequency ratios, complex BV functions, and continuous extremizer attainment are not classified. In the continuous BV subclass the same compact region is the closure of the attainable set, but the jump extremizers may be unattained. Location uniqueness on \(\mathbb T\) is not claimed for \(n>1\). A general convex-moment framework is classical, and an older equivalent two-coordinate formula under another name remains a publication-priority risk.

## References
- Vladimir Sluchak, *Bounds for Orthogonal Expansion Coefficients via Weighted Primitives*, arXiv:2611.04067v1 (2026), https://arxiv.org/html/2611.04067v1 . Relevant: Theorem 1, Sections 5.1 and 10.2.
- Paul Catala, Mathias Hockmann, Stefan Kunis and Markus Wageringel, *Approximation and Interpolation of Singular Measures by Trigonometric Polynomials*, arXiv:2203.10531 (2022), https://arxiv.org/abs/2203.10531 . General context on finite trigonometric moments and signed-measure interpolation, not the present exact variation body.
- NIST Digital Library of Mathematical Functions, §1.4(v), *Functions of Bounded Variation*, https://dlmf.nist.gov/1.4 . Standard variation facts.
