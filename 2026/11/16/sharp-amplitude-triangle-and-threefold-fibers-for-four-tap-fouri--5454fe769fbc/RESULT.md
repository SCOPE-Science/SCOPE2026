# Sharp amplitude triangle and threefold fibers for four-tap Fourier–Pauli data

## Finding

Fix four strictly positive real numbers \(A,B,C,D\). An admissible four-tap polynomial is
\[
f(z)=a+bz+cz^2+dz^3,\qquad (|a|,|b|,|c|,|d|)=(A,B,C,D).
\]
Its measurements consist of these four moduli and the entire continuous intensity \(I_f(t)=|f(e^{it})|^2\), for \(t\in\mathbb R\). Count different signals modulo multiplication by a single complex scalar of modulus one. A *nontrivial pair* is also inequivalent under conjugate reversal of the four coefficients.

**Theorem.** Every fiber of these measurements has at most three phase classes. There exists a nontrivial pair with the prescribed four positive moduli if and only if
\[
\boxed{\ |AC-BD|<|A^2-D^2|<AC+BD\ } . \tag{1}
\]
A fiber of exactly three phase classes exists if and only if
\[
\boxed{\ AC=BD=|A^2-D^2|\ } . \tag{2}
\]
Every three-point fiber has vanishing first and second nonzero autocorrelations. For one choice of magnitudes satisfying (2), with \(\omega=e^{2\pi i/3}\), its three distinct signals are
\[
f_j(z)=1-\frac32\omega^{-j}z+3\omega^jz^2+2z^3,\qquad j=0,1,2.
\]
Each has the same ordered coefficient moduli \((1,3/2,3,2)\) and the same intensity
\[
|f_j(e^{it})|^2=\frac{65}{4}+4\cos(3t).
\]
For signals supported on at most three consecutive sites with nonzero endpoint taps, the two measurements determine the signal up to common phase and conjugate reversal. Hence four taps is the first possible length for genuinely nontrivial partners.

## Assumptions and scope

The theorem is about nonzero four-entry complex sequences on the *integer line*, equivalently degree-three polynomials sampled in magnitude at **all** points of the unit circle, not a four-point periodic discrete Fourier transform. Every listed magnitude is strictly positive, so both endpoints are nonzero. Aperiodic autocorrelation is
\[
R_k=\sum_{j=0}^{3-k}f_{j+k}\overline{f_j},\qquad 0\le k\le3,
\]
where \((f_0,f_1,f_2,f_3)=(a,b,c,d)\). Continuous Fourier intensity is equivalent to the complete tuple \((R_0,R_1,R_2,R_3)\). Conjugate reversal sends \((a,b,c,d)\) to \((\bar d,\bar c,\bar b,\bar a)\). It preserves the ordered moduli only when \(A=D\) and \(B=C\). Integer shifts are excluded by fixing the nonzero support at \(\{0,1,2,3\}\).

## Proof

Multiply by a common phase so \(a=A>0\). The datum \(R_3=d\bar a=Ad\) now fixes \(d=De^{i\delta}\). The datum \(R_0=A^2+B^2+C^2+D^2\) adds no constraint. Write
\[
r=AC,\quad s=BD,\quad U=Ac,\quad V=d\bar b,\quad z=R_2=U+V,\quad k=(D^2-A^2)e^{2i\delta}.
\]
The constraints are \(|U|=r\), \(|z-U|=s\). Conversely any such \(U\) reconstructs uniquely
\[
c=U/A,\qquad b=\overline{(z-U)/d}.
\]
Direct substitution into the first autocorrelation gives the **exact reconstruction identity**
\[
AdR_1=A^2e^{2i\delta}\bar z+U(z-U)+k\bar U. \tag{3}
\]

First suppose \(z\ne0\). Two circles intersect in at most two points. At distinct intersection points \(U_+,U_-\), the circle equations yield
\[
U_++U_-=z+\frac{r^2-s^2}{\bar z},\qquad
\frac{\overline{U_+-U_-}}{U_+-U_-}=-\frac{\bar z}{z}.
\]
Subtracting (3) for the two points, their \(R_1\) values agree precisely when
\[
(s^2-r^2)z=k\bar z^{\,2}. \tag{4}
\]
If \(r\ne s\), this forces \(k\ne0\) and \(|z|=|s^2-r^2|/|k|\). The circle intersection is nondegenerate exactly when \(|r-s|<|z|<r+s\). Thus two different solutions require, and are possible precisely under,
\[
|r-s|<|k|<r+s. \tag{5}
\]
Sufficiency is constructive: set \(z=|s^2-r^2|/|k|>0\), choose \(e^{2i\delta}\in\{1,-1\}\) so (4) holds, and take the two different intersection points. They satisfy (3) and all required magnitudes. If \(r=s\) with \(z\ne0\), (4) instead forces \(k=0\). Then \(A=D\), \(B=C\), and the two intersection points exchange \(U\) with \(V=z-U\); they are precisely normalized conjugate reversals, not a nontrivial pair.

Now suppose \(z=0\). The circles require \(r=s>0\) and \(V=-U\). Identity (3) becomes
\[
AdR_1=-U^2+k\bar U,\qquad |U|=r.
\]
Multiplying by \(U\) produces a cubic
\[
U^3+AdR_1U-kr^2=0. \tag{6}
\]
Hence at most three phase classes exist in this case. If two different points \(U_+,U_-\) on the circle give the same \(R_1\), then
\[
U_++U_-=k\frac{\overline{U_+-U_-}}{U_+-U_-}.
\]
Writing \(U_\pm=r e^{i(\phi\pm\theta)}\), this reads
\[
2r\cos\theta\,e^{3i\phi}=-k. \tag{7}
\]
If \(k\ne0\), two distinct points solving (7) exist exactly when \(0<|k|<2r\): take \(0<\theta<\pi/2\) with \(2r\cos\theta=|k|\) and choose \(\phi\) to realize the phase on the right. Since here \(r=s\), this is again (5). If \(k=0\), the only possible distinct pair is \(U,-U\), and \(A=D,B=C\) make it conjugate reversal. The boundary \(|k|=2r\) has only a repeated point and is not ambiguous.

Combining both cases and noting \(r=AC,s=BD,|k|=|A^2-D^2|\) proves (1). The conditions in (1) force \(A\ne D\), so conjugate reversal cannot identify the constructed pair. For three distinct points, we must have \(z=0\), and all three must solve (6) with modulus \(r\). Their sum is zero by Vieta, so they form an equilateral triple \(U_j=r\xi\omega^j\). Their pairwise product sum vanishes, making \(AdR_1=0\). Their product has modulus \(r^3\), while (6) says it equals \(kr^2\); therefore \(|k|=r=s\), proving necessity of (2). Conversely, when (2) holds, choose \(z=R_1=0\) and \(\delta\) arbitrarily. Equation (6) is \(U^3=kr^2\) and has three distinct points of modulus \(r\). Reconstruction gives three signals with identical Fourier intensity and coefficient magnitudes. The displayed cube-root family gives a rational-coefficient instance.

For at most three consecutive nonzero taps, normalize the initial coefficient to positive real. The highest autocorrelation fixes the last coefficient, and the first autocorrelation is an equation \(A b+d\bar b=R_1\) in the remaining middle coefficient \(b\). This is an invertible real-linear equation if \(A\ne|d|\). If the endpoint magnitudes agree, its intersection with the circle of prescribed \(|b|\) has at most two points, which are exchanged by conjugate reversal. Lengths one and two are immediate.

## Verification

The standalone `pauli4_checker.py` computes the displayed triple in the exact Eisenstein field \(\mathbb Q(\omega)\), verifying precisely \((R_0,R_1,R_2,R_3)=(65/4,0,0,2)\). It independently reconstructs nontrivial partners from the circle-intersection and zero-correlation parametrizations, then compares all coefficient magnitudes and all four complex autocorrelations. Its deterministic integer grid and randomized real tests check hundreds of admissible amplitude vectors. These finite checks support, but do not replace, the quantified proof above. Python 3 standard library suffices.

## Relationship to prior work

Beinert and Plonka (2016), Corollary 3.5, prove almost-everywhere uniqueness from Fourier intensity and all coefficient moduli; Theorem 3.6 already constructs exceptional examples for every length greater than three. Their 2020 survey, Example 24.3, **already exhibits a three-solution four-tap fiber**, so neither the bare existence of partners nor a threefold example is new. Katz, Rahman and Ward (2023/2025), Theorem 1.1, give a general zero-factorization description of equicorrelational sequence families; it does not classify fixed four-entry modulus vectors. Novikov and Xu (2026) construct nontrivial Pauli partners by finite difference operators without a prescribed-four-moduli necessary-and-sufficient criterion. The contribution here is the explicit *sharp open triangle region of admissible magnitudes*, its complementary uniqueness regime, a universal three-point fiber bound and a necessary-and-sufficient condition for that maximum.

## Limitations

The theorem assumes all four coefficients are nonzero, a fixed consecutive support, and the complete continuous-circle Fourier intensity. It makes no claim for signals with zero taps, longer supports, finite cyclic sampling with aliasing, noisy data, or quantitative conditioning. Prior factorization theory and a prior three-solution four-tap example must not be attributed to this finding. An unindexed or uninspected earlier special-case calculation might contain the same triangle criterion; independent mathematical and literature review are not performed here.

## References

- R. Novikov and T. Xu, *On Phase Retrieval for Continuous and Discrete Fourier Transforms*, arXiv:2604.25662v1 (first public 2026-04-28), https://arxiv.org/html/2604.25662v1 .
- R. Beinert and G. Plonka, *Enforcing uniqueness in one-dimensional phase retrieval by additional signal information in time domain*, arXiv:1604.04493v1 (2016), https://arxiv.org/html/1604.04493v1 .
- R. Beinert and G. Plonka, *One-Dimensional Discrete-Time Phase Retrieval*, open-access book chapter (2020), https://doi.org/10.1007/978-3-030-34413-9_24 .
- D. J. Katz, A. Rahman and M. J. Ward, *Sequences with identical autocorrelation functions*, arXiv:2308.07467 (2023), https://arxiv.org/html/2308.07467v3 .
