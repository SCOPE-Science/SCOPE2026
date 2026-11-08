# Essential-maximal numerical ranges of coordinatewise real-linear operators

## Finding
Let \(\Phi:\ell^2(\mathbb N;\mathbb C)\to\ell^2(\mathbb N;\mathbb C)\) be a bounded real-linear coordinate operator
\[
  (\Phi x)_j=a_jx_j+b_j\overline{x_j},\qquad j\geq1,
\]
for arbitrary bounded complex sequences \((a_j)\) and \((b_j)\). Write \(F\subset\mathbb C^2\) for the nonempty compact set of all subsequential limits of \((a_j,b_j)\) along indices tending to infinity, and put
\[
 r=\max_{(a,b)\in F}(|a|+|b|).
\]
Then \(r=\|\Phi\|_{\mathrm e}\), where the essential norm is taken in the real-linear operator algebra. Let \(\mathbb T=\{w\in\mathbb C:|w|=1\}\), and define
\[
 \Gamma=\{(a,b,w)\in F\times\mathbb T:|a+bw|=r\},
 \quad G=\{a+bw:(a,b,w)\in\Gamma\}.
\]
The essential maximal numerical range is **exactly**
\[
 \boxed{W_{\mathrm{e,max}}(\Phi)=\operatorname{conv}G.}
\]
In particular, for \(r>0\), \(G\) is a nonempty compact subset of \(r\mathbb T\). If \(F\) contains \((0,b)\) with \(|b|=r\), the answer is the full disk \(r\overline{\mathbb D}\). Otherwise it has the simpler phase-only formula
\[
 W_{\mathrm{e,max}}(\Phi)=r\operatorname{conv}
 \left\{\frac{a}{|a|}:(a,b)\in F,\ |a|+|b|=r\right\}.
\]
Thus the phase of the antilinear coefficient cannot change the resulting geometry. All the sets obtainable as \(W_{\mathrm{e,max}}(\Phi)\) at essential norm \(r\) are **precisely** the sets \(\operatorname{conv}E\), where \(E\) is any nonempty compact subset of \(r\mathbb T\). At \(r=0\), the only possibility is \(\{0\}\).

The exact ordinary essential numerical range of the same operator is
\[
 \boxed{W_{\mathrm e}(\Phi)=\operatorname{conv}\bigcup_{(a,b)\in F}
       \{z\in\mathbb C:|z-a|\leq |b|\}.}
\]
For \(r>0\), the two invariants obey the exact **outer-contact reconstruction identity**
\[
 \boxed{W_{\mathrm{e,max}}(\Phi)=\operatorname{conv}
 \bigl(W_{\mathrm e}(\Phi)\cap r\mathbb T\bigr).}
\]
Thus the essential-maximal range can be recovered from the extremal boundary contacts of the ordinary essential range in this diagonal class.

This distinction can be maximally unstable. Let \(C\) denote coordinatewise conjugation on \(\ell^2\), and for \(0<\varepsilon<1\) set \(\Phi_\varepsilon=\varepsilon I+(1-\varepsilon)C\), with \(\Phi_0=C\). All these operators have essential norm one. Nevertheless,
\[
 W_{\mathrm{e,max}}(\Phi_0)=\overline{\mathbb D},\qquad
 W_{\mathrm{e,max}}(\Phi_\varepsilon)=\{1\},\qquad
 d_{\mathrm H}\bigl(W_{\mathrm{e,max}}(\Phi_\varepsilon),W_{\mathrm{e,max}}(\Phi_0)\bigr)=2,
\]
while
\[
 \|\Phi_\varepsilon-\Phi_0\|=2\varepsilon,\qquad
 d_{\mathrm H}\bigl(W_{\mathrm e}(\Phi_\varepsilon),W_{\mathrm e}(\Phi_0)\bigr)=2\varepsilon.
\]
The jump of two is maximal for compact sets inside the closed unit disk.

## Assumptions and scope
All Hilbert spaces, weak convergence, inner products and compact operators here are over the standard complex \(\ell^2\), but the maps are only required to be **real-linear**. The inner product is linear in its first variable. Boundedness means \(\sup_j(|a_j|+|b_j|)<\infty\). The essential maximal numerical range has the precise definition
\[
 W_{\mathrm{e,max}}(\Phi)=\{\lambda\in\mathbb C:\ \exists\,x^{(k)}\in\ell^2,
 \ \|x^{(k)}\|=1,\ x^{(k)}\rightharpoonup0,\
 \|\Phi x^{(k)}\|\to\|\Phi\|_{\mathrm e},\
 \langle\Phi x^{(k)},x^{(k)}\rangle\to\lambda\}.
\]
The ordinary essential numerical range omits the norm-extremizing condition. The convex hull of a compact planar set is understood as its (already closed) finite convex hull. The formula covers repeated coefficients, alternating coefficients, nonconvergent coefficient sequences, vanishing linear or antilinear parts, and essential norm zero. No finite-dimensional result or assertion about arbitrary nondiagonal real-linear operators is claimed.

## Proof
**1. Local scalar norming set.** For \(a,b\in\mathbb C\), the scalar real-linear map \(z\mapsto az+b\bar z\) has operator norm \(|a|+|b|\). For \(|z|=1\), writing \(w=\bar z^2\in\mathbb T\) gives
\[
 (az+b\bar z)\bar z=a+bw,\qquad |az+b\bar z|=|a+bw|.
\]
Equality \(|a+bw|=|a|+|b|\) is exactly equality in the triangle inequality. If \(a\ne0\) and \(|a|+|b|=r\), it forces the numerical value \(a+bw=r a/|a|\) (including \(b=0\)); if \(a=0\), the numerical values of scalar norming vectors form the full circle \(r\mathbb T\). This is the explicit local description of \(G\).

**2. Essential norm.** Let \(P_N\) truncate to the first \(N\) coordinates. The finite-rank real-linear operator \(P_N\Phi\) satisfies
\[
 \|\Phi-P_N\Phi\|=\sup_{j>N}(|a_j|+|b_j|),
\]
so \(\|\Phi\|_{\mathrm e}\leq\limsup_j(|a_j|+|b_j|)=r\). Choose increasing indices \(j_k\) on which the scalar norms approach \(r\), and unit vectors supported in those coordinates with norming phases. These vectors converge weakly to zero, and every compact real-linear operator takes them to a norm-null sequence. Their images under \(\Phi\) have norms approaching \(r\). Thus the reverse inequality holds.

**3. Upper inclusion for the essential maximal range.** Fix a defining weakly null unit sequence \(x^{(k)}\) for a point \(\lambda\) of \(W_{\mathrm{e,max}}(\Phi)\). For each \(j,k\), set \(t_{kj}=|x_j^{(k)}|^2\); choose \(w_{kj}\in\mathbb T\) so that \(w_{kj}=\overline{x_j^{(k)}}^2/|x_j^{(k)}|^2\) when \(x_j^{(k)}\ne0\), and choose it arbitrarily otherwise. Then
\[
 \sum_jt_{kj}=1,\quad
 \|\Phi x^{(k)}\|^2=\sum_jt_{kj}|a_j+b_jw_{kj}|^2,\quad
 \langle\Phi x^{(k)},x^{(k)}\rangle=\sum_jt_{kj}(a_j+b_jw_{kj}).
\]
Regard these sums as integrals against probability measures \(\mu_k=\sum_jt_{kj}\delta_{(a_j,b_j,w_{kj})}\) on the compact product of the bounded coefficient closure and \(\mathbb T\). By subsequence extraction, these probability measures converge weakly to a probability measure \(\mu\). Because \(x^{(k)}\rightharpoonup0\), every fixed finite coordinate set carries asymptotically zero mass. Therefore the coefficient marginal of \(\mu\) is supported on the tail cluster set \(F\). Continuity of the two displayed integrands yields
\[
 \int |a+bw|^2\,d\mu=r^2,
 \qquad\int(a+bw)\,d\mu=\lambda.
\]
On \(F\times\mathbb T\), \(|a+bw|\leq |a|+|b|\leq r\). Equality of its squared average with \(r^2\) forces \(\mu(\Gamma)=1\). Hence \(\lambda\) is a barycenter of \(G\) and belongs to \(\operatorname{conv}G\). The argument also works for \(r=0\).

**4. Lower inclusion.** Take any \((a,b,w)\in\Gamma\). Choose indices \(j_k\to\infty\) with \((a_{j_k},b_{j_k})\to(a,b)\) and choose unit phases \(z_k\) such that \(\bar z_k^2=w\). The supported vectors \(x^{(k)}=z_ke_{j_k}\) are weakly null, their image norms tend to \(r\), and their numerical values tend to \(a+bw\). Thus every point of \(G\) belongs to the essential maximal numerical range. For any finite convex combination of such points, use mutually distinct tail coordinates approximating the prescribed coefficient-phase pairs and assign the corresponding squared coordinate magnitudes as convex weights. Its image norm squared tends to the convex combination of \(r^2\), hence to \(r^2\), and its numerical value tends to the desired convex combination. Since \(\operatorname{conv}G\) is compact, a diagonal-sequence argument proves the reverse inclusion.

**5. The ordinary essential range.** Repeat Steps 3 and 4 without the norm-saturation condition. The scalar values \(a+bw\) form the circle centered at \(a\) with radius \(|b|\), and planar convexification fills the disk. This proves the stated formula for \(W_{\mathrm e}(\Phi)\).

For the outer-contact identity, every point of the preceding convex hull has modulus at most \(r\). A convex combination of points of the closed disk \(r\overline{\mathbb D}\) can lie on its boundary circle only if every positively weighted point is the same boundary point. Consequently \(W_{\mathrm e}(\Phi)\cap r\mathbb T=G\) when \(r>0\). Combining with Steps 3–4 gives the stated reconstruction identity.

**6. Realization and sharp instability.** For any prescribed nonempty compact \(E\subset r\mathbb T\), choose a sequence \((u_j)\subset E\) whose tail cluster set is \(E\) (for example, repeat successively finer finite nets). Set \(a_j=u_j/2\), \(b_j=r/2\). The coefficients have scalar norms exactly \(r\) and nonzero linear parts, so the local norming values are exactly \(u_j\). Consequently \(W_{\mathrm{e,max}}(\Phi)=\operatorname{conv}E\). Conversely Steps 1–4 show that every diagonal essential-maximal range has this form. At \(r=0\), all tail coefficients vanish and both ranges equal \(\{0\}\).

For the final example, \(\Phi_\varepsilon\) has the constant coefficient pair \((\varepsilon,1-\varepsilon)\). For \(\varepsilon>0\), its scalar norming numerical value is the single point \(1\); for \(\varepsilon=0\), all norming phases are possible. Step 5 gives \(W_{\mathrm e}(\Phi_\varepsilon)=\varepsilon+(1-\varepsilon)\overline{\mathbb D}\). Directly \(\|I-C\|=2\) (attained on a purely imaginary unit coordinate), so \(\|\Phi_\varepsilon-\Phi_0\|=2\varepsilon\). Hausdorff distances follow from the opposite boundary points and the elementary disk support functions. Every pair of compact subsets of \(\overline{\mathbb D}\) has Hausdorff distance at most two; hence the displayed discontinuity is largest possible.

## Verification
The proof uses only scalar equality in the triangle inequality, finite-rank truncation, weak nullness of remote coordinate supports, compactness of probability measures on compact metric spaces, and planar convex hulls. A direct reproducibility checker in `verify_examples.py` evaluates scalar norming identities for 3,000 deterministic complex pairs and the exact conjugation-perturbation profile at five positive rational perturbation parameters. These finite checks are diagnostics; they do not substitute for the measure-concentration or realization arguments above.

## Relationship to prior work
Majumdar and Müller, arXiv:2610.16823v1 (October 12, 2026), introduce the real-linear essential maximal numerical range and prove its compact convexity (Section 5), but do not give the diagonal cluster-parameter formula, the complete norm-circle shape classification, or this mixed linear/antilinear discontinuity. Kołaczek and Müller, arXiv:2508.04347v1, establish convexity of ordinary real-linear numerical ranges and a disk-inclusion principle, not the essential norming constraint. Carvalho, Diogo, Mendes and Soares, arXiv:2212.11659v1, determine essential numerical ranges for complex-linear block diagonal operators; that covers a different invariant and operator class. Fong's 1979 paper treats essential maximal numerical ranges for complex-linear operators and proves an upper-semicontinuity principle; the present Hausdorff jump is a failure of lower semicontinuity and is consistent with that principle. The abstract of Amara, Liu and Zhu's 2025 study concerns maximal numerical ranges of purely antilinear operators; full text was not available for verification. No independence or publication-priority certification is asserted.

## Limitations
The classification is restricted to coordinatewise real-linear operators on separable complex \(\ell^2\), not arbitrary real-linear or block-mixing maps. It describes essential maximal numerical ranges, not the ordinary maximal range in the presence of isolated norm-attaining coordinates. The ordinary essential numerical range formula is contextual and relates to known block-diagonal range methods; its separate novelty is not asserted. The scalar pure-conjugation discontinuity is a concrete consequence of the classification, not a claim that all failures of semicontinuity are new. Some older antilinear maximal-range literature was accessible only through abstracts. Independent mathematical and publication-priority review remains outstanding.

## References
1. A. Majumdar and V. Müller, *Some Generalized Numerical Ranges of Real-linear Operators on Hilbert Spaces*, arXiv:2610.16823v1, first public October 12, 2026. https://arxiv.org/abs/2610.16823
2. D. Kołaczek and V. Müller, *Real linear operators and numerical ranges*, arXiv:2508.04347v1, first public August 6, 2025. https://arxiv.org/abs/2508.04347
3. L. Carvalho, C. Diogo, S. Mendes and H. Soares, *A note on the essential numerical range of block diagonal operators*, arXiv:2212.11659v1, first public December 22, 2022. https://arxiv.org/abs/2212.11659
4. C. K. Fong, *On the essential maximal numerical range*, Acta Sci. Math. 41 (1979), 307–315. https://acta.bibl.u-szeged.hu/14726/1/math_041_fasc_003_004_307-315.pdf
5. Z. Amara, T. Liu and S. Zhu, *Maximal numerical ranges of antilinear operators*, J. Math. Anal. Appl. 556 (2026), article 130116. https://doi.org/10.1016/j.jmaa.2025.130116
