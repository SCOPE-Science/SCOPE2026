# Exact spectral recovery from the areas of all isoptics of a smooth convex oval

## Finding
Let \(K\) be a strictly convex planar body with a \(C^2\) support function \(p\), positive curvature radius \(p+p''>0\), and no prescribed origin. For \(0<\alpha<\pi\), let \(\mathcal A_K(\alpha)\) be the area enclosed by the exterior isoptic consisting of points at which the two supporting tangents have outward-normal separation \(\alpha\); equivalently the body is seen under angle \(\pi-\alpha\). Define
\[
H_K(\alpha)=\frac{\sin^2\alpha}{\pi}\mathcal A_K(\alpha),\qquad
c_0=\frac1\pi\int_0^\pi H_K(\alpha)\,d\alpha,\quad
c_k=\frac2\pi\int_0^\pi H_K(\alpha)\cos(k\alpha)\,d\alpha\quad(k\ge1).
\]
These integrals uniquely recover the mean support radius \(R>0\) and **every nontranslational Fourier power** \(q_m=a_m^2+b_m^2\), where
\(p(t)=R+\sum_{m\ge1}(a_m\cos mt+b_m\sin mt)\), by the absolutely convergent expressions
\[
\boxed{q_{2j}=\frac{2}{(2j-1)(2j+1)}\sum_{\ell=j}^\infty(2\ell+1)c_{2\ell+1}},\qquad j\ge1,
\]
\[
\boxed{q_{2j+1}=-\frac{1}{j(j+1)}\sum_{\ell=1}^j\ell c_{2\ell}},\qquad j\ge1,
\]
\[
\boxed{R^2=-\frac12\sum_{\ell=0}^\infty(2\ell+1)c_{2\ell+1}}.
\]
Consequently two such ovals have the same isoptic-area function at **every** angle if and only if they have the same perimeter and all the same \(q_m\) for \(m\ge2\). Thus the function determines the perimeter, the original enclosed area and the complete nontranslational support-function power spectrum, but not the phases. For instance the two strictly convex analytic ovals with supports \(p_1(t)=20+\cos2t+\cos3t\) and \(p_2(t)=20+\cos2t+\sin3t\) are noncongruent yet have identical isoptic-area functions at every angle.

## Assumptions and scope
The support function is expressed against the outward unit normal \(n(t)=(\cos t,\sin t)\), with positive curvature radius \(\rho(t)=p(t)+p''(t)>0\). The tangent line at normal \(t\) is \(\langle x,n(t)\rangle=p(t)\). For every \(\alpha\in(0,\pi)\), the intersections of the two lines with normals \(t\) and \(t+\alpha\), as \(t\) varies, form the isoptic locus. Its enclosed area is the ordinary unsigned area. The parameter \(\alpha\) is the *normal-gap* angle, not the observed visual angle; the latter is \(\pi-\alpha\). Translation alters only the \(m=1\) harmonics, which are deliberately not claimed recoverable. The \(C^2\) and positive-curvature hypotheses suffice for all coefficient identities and weighted-series limits below.

## Proof
**1. Exact area identity.** Put \(s=\sin\alpha\), \(z=\cos\alpha\), and \(\tau(t)=(-\sin t,\cos t)\). The intersection of the two tangent lines is
\[
X_\alpha(t)=p(t)n(t)+u_\alpha(t)\tau(t),\qquad
\nu_\alpha(t)=\frac{p(t+\alpha)-z p(t)}s.
\]
Because \(n'=\tau\), \(\tau'=-n\), Green's area formula gives
\[
2\mathcal A_K(\alpha)=\int_0^{2\pi}\big[p(t)(p(t)+\nu_\alpha'(t))-\nu_\alpha(t)(p'(t)-\nu_\alpha(t))\big]dt.
\]
The equality of the Green integral with the unsigned isoptic enclosed area is also guaranteed by the classical support-function isoptic area theorem. Periodic integration by parts and a shift of the integration variable yield
\[
\mathcal A_K(\alpha)=\frac1{\sin^2\alpha}\int_0^{2\pi}
\left[p(t)^2-p(t+\alpha)\big(p(t)\cos\alpha+p'(t)\sin\alpha\big)\right]dt.
\tag{1}
\]
This known forward identity appears in Michalska (2003), Eq. (1.1). We use it as a verified established starting point; the inverse theorem is the new claim.

**2. Fourier forward coefficients.** The Fourier convention in the finding and orthogonality in (1) give
\[
H_K(\alpha)=2R^2(1-\cos\alpha)+\sum_{m=2}^\infty q_m
\left[1-\cos(m\alpha)\cos\alpha-m\sin(m\alpha)\sin\alpha\right].\tag{2}
\]
The \(m=1\) summand vanishes identically. Using product-to-sum,
\[
H_K(\alpha)=2R^2(1-\cos\alpha)+\sum_{m\ge2}q_m
\left[1-\frac{m+1}{2}\cos((m-1)\alpha)+\frac{m-1}{2}\cos((m+1)\alpha)\right].\tag{3}
\]
Since \(p\in C^2\), Parseval yields \(\sum_{m\ge2}m^4q_m<\infty\); this justifies absolute uniform convergence and termwise cosine extraction. In particular
\[
c_1=-2R^2-\frac32q_2,\qquad
c_k=\frac{k-2}{2}q_{k-1}-\frac{k+2}{2}q_{k+1}\quad(k\ge2),\tag{4}
\]
with the convention \(q_1=0\) in this recurrence. Also \(c_0=2R^2+\sum_{m\ge2}q_m\).

**3. Recover the odd modes.** Set \(s_j=j(j+1)q_{2j+1}\) for \(j\ge1\), with \(s_0=0\). The even-indexed coefficients in (4) satisfy \(j c_{2j}=s_{j-1}-s_j\), hence \(s_j=-\sum_{\ell=1}^j\ell c_{2\ell}\). This gives the finite inversion for \(q_{2j+1}\) in the finding.

**4. Recover the even modes.** Set \(r_j=(4j^2-1)q_{2j}\) for \(j\ge1\). Formula (4) gives \(2(2j+1)c_{2j+1}=r_j-r_{j+1}\). By \(\sum m^4q_m<\infty\), \(r_j\to0\), and telescoping from \(j\) to infinity proves the displayed infinite reconstruction of \(q_{2j}\). Moreover \(\sum m^2q_m<\infty\) ensures the weighted sums of the \(c_k\) converge absolutely: each \(c_k\) is bounded by weighted neighboring \(q_m\).

**5. Recover the mean radius.** Taking \(j=1\) in step 4 gives \(\sum_{\ell=1}^\infty(2\ell+1)c_{2\ell+1}=\frac32q_2\). Combine this with \(c_1=-2R^2-3q_2/2\) to recover \(R^2\). Since the mean support is positive for every nonempty convex body, its positive square root is uniquely determined. Its perimeter is \(2\pi R\) by Cauchy's perimeter formula. Its enclosed area is then determined by the standard support-area identity
\[
\operatorname{area}(K)=\pi R^2-\frac\pi2\sum_{m\ge2}(m^2-1)q_m.
\]

**6. Exact ambiguity and example.** Formula (2) shows that matching \(R\) and \(q_m\) is sufficient, while steps 3–5 show it is necessary. The \(m=1\) coefficients are arbitrary translations and each vector \((a_m,b_m)\) may rotate independently along its fixed-radius circle provided \(p+p''>0\); these are exactly the remaining admissible phase ambiguities. For the two stated analytic support functions, \(\rho(t)=20-3\cos2t-8\cos3t\) or \(\rho(t)=20-3\cos2t-8\sin3t\), both at least \(9>0\). A Euclidean congruence acts by \(t\mapsto\pm t+\phi\), up to a first harmonic. To preserve the common second-harmonic term \(\cos2t\), it must have \(\phi\) a multiple of \(\pi\); no such rotation or reflection can map a third-harmonic cosine to a sine. Thus they are noncongruent.

## Verification
Running the included standalone `check_isoptic_area_inverse.py` with Python and NumPy prints `ISOPTIC_AREA_SPECTRAL_INVERSE_CHECKS_OK`. It independently constructs the tangent-intersection curve in the plane and computes the Green integral numerically at seven separated normal-gap angles, checking (2); checks the parity-telescoping reconstructions against a five-mode support function; and checks direct cosine integration of the area profile against coefficient extraction. Numerical checks support but do not replace the algebraic proof and established forward identity.

## Relationship to prior work
Michalska (2003) gives (1) and the forward Fourier identity (2), and investigates sufficient conditions for convexity of the isoptic-area function. These *forward statements are not new*. Csima and Szirmai (public preprint 2013) study isoptics of conics in constant-curvature geometries. Michalska and Mozgawa (2015) treat triangular isoptics and the envelope description of oval isoptics. Kurusa (2012) asks when the **full isoptic curve** determines the underlying body, a richer measurement than its scalar enclosed area. The present claim is the reverse, infinite-dimensional **scalar area-profile identifiability** statement, with explicit two-parity inverse formulas, perimeter recovery and sharp full-phase nonuniqueness. It is not asserted that a single isoptic area determines a body. Targeted mathematical-index and literature comparisons did not locate this reverse statement, but cannot establish definitive historical priority.

## Limitations
The inverse uses the full continuous area profile, not finitely many measurements, and does not offer noise-stable recovery of high-frequency coefficients. It does not recover phases or translations or reconstruct a unique planar body. Smoothness and strict positive curvature are used to control summability and geometric isoptics. Only similarity of the scalar area functions is claimed, not equality of isoptic curves as subsets. The preexisting forward Fourier identity is fully credited; claims of originality are confined to the inverse/ambiguity theorem and remain subject to independent priority assessment.

## References
1. M. Michalska, *A sufficient condition for the convexity of the area of an isoptic curve of an oval*, Rendiconti del Seminario Matematico della Università di Padova **110** (2003), 161–169. https://www.numdam.org/item/RSMUP_2003__110__161_0.pdf
2. G. Csima and J. Szirmai, *Isoptic curves of conic sections in constant curvature geometries*, arXiv:1301.6991, first posted 2013-01-29. https://arxiv.org/abs/1301.6991
3. M. Michalska and W. Mozgawa, *\(\alpha\)-isoptics of a triangle and their connection to \(\alpha\)-isoptic of an oval*, Rend. Sem. Mat. Univ. Padova **133** (2015), 159–172. https://doi.org/10.4171/RSMUP/133-8
4. Á. Kurusa, *Is a convex plane body determined by an isoptic?*, 2012. https://publicatio.bibl.u-szeged.hu/15946/1/bodyisop.pdf
