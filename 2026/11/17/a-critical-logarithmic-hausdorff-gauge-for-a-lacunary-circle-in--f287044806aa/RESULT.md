# A critical logarithmic Hausdorff gauge for a lacunary circle in \(\ell_p\)

## Finding
For every real \(0<p<1\), define a curve in the complex sequence space \(\ell_p(\mathbb C)\) by
\[
F_p(t)=\bigl(2^{-n}e^{i2^nt}\bigr)_{n\ge0},\qquad t\in\mathbb R/(2\pi\mathbb Z).
\]
Equip this space with the genuine metric \(d_p(x,y)=\sum_{n\ge0}|x_n-y_n|^p\), and write \(E_p=F_p(\mathbb R/(2\pi\mathbb Z))\). Then, uniformly in the base point as \(h\to0\),
\[
d_p(F_p(t+h),F_p(t))=|h|^p\left(\frac{\log(1/|h|)}{\log2}+O_p(1)\right).
\]
For the Hausdorff gauge \(g_p(r)=[r/\log(1/r)]^{1/p}\) at sufficiently small positive \(r\), with the standard diameter-cover normalization,
\[
\boxed{\mathcal H^{g_p}(E_p)=\frac{2\pi}{(p\log2)^{1/p}}},\qquad
\boxed{\dim_H(E_p,d_p)=\frac1p}.
\]
If \(N_p(\varepsilon)\) is the smallest number of subsets of \(d_p\)-diameter at most \(\varepsilon\) that cover \(E_p\), then
\[
\boxed{N_p(\varepsilon)\sim2\pi\left(\frac{\log(1/\varepsilon)}{p(\log2)\varepsilon}\right)^{1/p}}.
\]
Every scalar coordinate of \(F_p\) is real analytic, but \(F_p\) is nowhere differentiable in the \(\ell_p\) quasi-norm. Its precise near-Lipschitz loss is
\[
\|F_p(t+h)-F_p(t)\|_p\sim\frac{|h|[\log(1/|h|)]^{1/p}}{(\log2)^{1/p}}.
\]

## Assumptions and scope
The parameter \(p\) is fixed in \((0,1)\). The complex \(\ell_p\) quasi-norm is \(\|x\|_p=(\sum_n|x_n|^p)^{1/p}\). The induced function \(d_p=\|x-y\|_p^p\) is a metric because \(|u+v|^p\le |u|^p+|v|^p\). All logarithms are natural. Extend the gauge arbitrarily to a continuous nondecreasing function away from zero; its large-scale values cannot change the measure. Hausdorff gauge measure uses the infimum of sums of \(g_p(\operatorname{diam}U_i)\) over countable covers of small diameter, without additional geometric normalization factors. In the entropy formula covers can use arbitrary subsets, not necessarily balls. The source date and MSC are associated with the motivating differentiability literature, not with a claimed publication of this theorem.

## Proof
**1. Exact increment and uniform endpoint asymptotic.** By phase cancellation,
\[
D_p(h):=d_p(F_p(t+h),F_p(t))=\sum_{n=0}^\infty2^{-np}|e^{i2^nh}-1|^p,
\]
independent of \(t\). Let \(0<|h|<1/2\) and \(J=\lfloor\log_2(1/|h|)\rfloor\). For \(0\le n\le J\), Taylor's theorem for \(2\sin(u/2)/u\), uniform on \([-1,1]\), gives
\[
2^{-np}|e^{i2^nh}-1|^p=|h|^p\bigl(1+O_p(2^{2n}h^2)\bigr).
\]
The total error on these indices is \(O_p(|h|^p)\) because \(\sum_{n\le J}2^{2n}h^2=O(1)\). For \(n>J\), the bound \(|e^{iu}-1|\le2\) and a geometric series give an additional \(O_p(2^{-Jp})=O_p(|h|^p)\). Hence
\[
D_p(h)=|h|^p\bigl(J+1+O_p(1)\bigr)
=|h|^p\left(\frac{\log(1/|h|)}{\log2}+O_p(1)\right).
\]
This is uniform in \(t\), and the same estimate applies to the smaller circular difference of any two parameters. In particular, if \(c_p=(p\log2)^{-1/p}\), then
\[
\lim_{h\to0}\frac{g_p(D_p(h))}{|h|}=c_p.
\]
Because \(F_p\)'s first coordinate is \(e^{it}\), its period is exactly \(2\pi\) and it is injective on the parameter circle.

**2. Exact gauge measure.** The map is a homeomorphism of the compact parameter circle onto \(E_p\). Given \(\eta>0\), uniform asymptotics above imply that every pair of parameters whose circular separation is sufficiently small satisfies
\[
(c_p-\eta)\,\delta\le g_p(d_p(F_p(s),F_p(t)))\le(c_p+\eta)\,\delta,
\]
where \(\delta\) denotes their shorter circular arc distance. Consider an arbitrary sufficiently fine cover of \(E_p\) by sets. Intersect each set with \(E_p\), lift its preimage to the parameter circle and enclose that preimage in a shortest small arc. The length of this arc equals its maximum pairwise circular distance (for sufficiently small diameters, as follows already from the first coordinate), and the arcs cover the full circle. Thus the sum of their lengths is at least \(2\pi\); the lower displayed inequality gives a covering cost at least \((c_p-\eta)2\pi\). Conversely, subdividing the parameter circle into \(m\) equal arcs and covering their images yields total cost at most \((c_p+\eta)2\pi\), using the supremum of the uniform small-distance bound over each arc. Let \(m\to\infty\) and then \(\eta\downarrow0\). This proves the exact gauge measure.

**3. Dimension and sharp covering entropy.** The gauge \(g_p(r)=r^{1/p}[\log(1/r)]^{-1/p}\) has regular-variation index \(1/p\). Positive finite \(\mathcal H^{g_p}\) implies \(\dim_H(E_p,d_p)=1/p\) by comparison with the gauges \(r^s\) for \(s\ne1/p\). Let \(h_\varepsilon\) be any asymptotic inverse scale for \(D_p\), namely
\[
h_\varepsilon=\left(\frac{p(\log2)\varepsilon}{\log(1/\varepsilon)}\right)^{1/p}.
\]
The increment asymptotic shows \(D_p(h_\varepsilon)\sim\varepsilon\). Regular variation with positive index, uniformly for small separations, shows that every set of \(d_p\)-diameter at most \(\varepsilon\) has preimage contained in an arc of length at most \((1+o(1))h_\varepsilon\), while parameter arcs of length \((1-o(1))h_\varepsilon\) have images of \(d_p\)-diameter at most \(\varepsilon\). Counting lengths in a cover of the full circle gives \(N_p(\varepsilon)\sim2\pi/h_\varepsilon\), as asserted.

**4. Nowhere quasi-norm differentiability.** If \(F_p\) had a derivative in \(\ell_p\) at a point, continuous coordinate evaluation would force the derivative vector to have coordinates \(i e^{i2^nt}\) for every \(n\ge0\). All have modulus one, so this vector is not in \(\ell_p\). This contradiction holds at every point. Taking the \(p\)-th root of the uniform increment formula proves the sharp quasi-norm modulus.

## Verification
The independent elementary components of the proof are the geometric tail bound, Taylor-error summability, circle-arc cover comparison, and the inverse-scale calculation. The accompanying standalone `CHECK.py` evaluates the convergent increment sum against its proven leading term for multiple exponents and scales; these numerical checks are illustrative only and are not used as infinite proof. The full argument above covers every fixed \(0<p<1\), with no unstated genericity or numerical cutoff.

## Relationship to prior work
Albiac, Ansorena and Wald (arXiv:2609.26992, first public 22 September 2026) study differentiability of curves in quasi-Banach spaces, including the distinction between the quasi-norm and the natural \(p\)-metric, and give decoupled-coordinate differentiability results. Their relevant Sections 6 and 7 do not state the sharp logarithmic metric entropy or positive finite critical Hausdorff gauge of this explicit analytic-coordinate lacunary circle. Classical results on regularity of affine fractal curves address different finite-dimensional self-affine objects, rather than this infinite-coordinate translation-invariant metric circle. A separate recorded lacunary-trace endpoint modulus concerns scalar hyperbolic traces, without the present metric gauge and dimension conclusion. The general covering argument is elementary, but its exact input coefficient here comes from the explicitly analyzed infinite series.

## Limitations
This is an explicit model, not a classification of all quasi-Banach curves or of arbitrary lacunary frequency/amplitude sequences. It does not produce a Lipschitz curve in the \(\ell_p\) quasi-norm or the metric \(d_p\); it quantifies a critical near-Lipschitz boundary. No assertion of publication priority or independent mathematical validation is made. Earlier equivalent results in vector-valued lacunary series or metric-embedding literature remain a possible priority risk.

## References
1. F. Albiac, J. L. Ansorena and P. Wald, *Differentiability of Lipschitz curves in \(p\)-Banach spaces*, arXiv:2609.26992v1 (22 September 2026), Sections 2, 6 and 7, https://arxiv.org/abs/2609.26992.
2. F. Albiac and J. L. Ansorena, *Lipschitz extensions into \(p\)-Banach spaces, and canonical embeddings of Lipschitz-free \(p\)-spaces for \(0<p<1\)*, arXiv:2603.28193v1 (30 March 2026), Introduction, https://arxiv.org/abs/2603.28193.
3. B. Bárány, G. Kiss and I. Kolossváry, *Pointwise regularity of parameterized affine zipper fractal curves*, Nonlinearity 31 (2018), 1705–1733, DOI:10.1088/1361-6544/aaa497 (comparison from abstract/metadata; full article not examined).
