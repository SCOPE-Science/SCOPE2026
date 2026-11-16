# First-harmonic sharp circular mixed-Fourier stability for every real exponent \(q\ge 9\)

## Finding
For every real \(q\ge9\) and each integer \(k\ge0\), define the convergent Bessel moment
\[
I_k(q)=\int_0^\infty r\,|J_k(r)|^q\,dr.
\]
The **unique maximizing positive-order moment** is the first:
\[
\boxed{I_1(q)>I_k(q)\quad\text{for all real }q\ge9\text{ and integers }k\ge2.}
\]
Consequently, the optimal quadratic stability coefficient in the planar radial–angular mixed-norm Fourier extension inequality is
\[
\boxed{\Gamma_{2,q}=4\pi^2\left(I_0(q)^{2/q}-I_1(q)^{2/q}\right)\qquad(q\ge9).}
\]
This determines the exact maximizing nonconstant degree and every equality class for the entire indicated continuous range, including noninteger exponents. The known sharp global constant is \(C_{2,q}=2\pi I_0(q)^{1/q}\).

## Assumptions and scope
The Bessel functions \(J_k\) have integer orders; all exponents in the assertion are real and finite. On the unit circle with **unnormalized** arclength \(d\sigma\), let
\[
(Ef)(x)=\int_{\mathbb S^1}e^{-ix\cdot\omega}f(\omega)\,d\sigma(\omega),
\qquad
\|Ef\|_{q,2}=\left(\int_0^\infty\left(\int_{\mathbb S^1}|Ef(r\theta)|^2d\sigma(\theta)\right)^{q/2}r\,dr\right)^{1/q}.
\]
Let \(P_0\) denote orthogonal projection in \(L^2(\mathbb S^1,d\sigma)\) onto constants. For all complex-valued \(f\) in this Hilbert space, the sharp inequality is
\[
C_{2,q}^2\|f\|_2^2-\|Ef\|_{q,2}^2
\ge \Gamma_{2,q}\|f-P_0f\|_2^2.
\]
The coefficient is optimal. Equality holds for zero, all constants, and all nonzero pure first harmonics (the complex span of \(e^{i\theta}\) and \(e^{-i\theta}\)); no sum with both a nonzero constant and a nonzero first harmonic gives equality.

## Proof
Write \(M_k(p)=I_k(p)\). The new estimate is obtained from three **strict rational separators**:
\[
\boxed{M_1(9)>137/10000,\qquad M_1(6)<109/1000,\qquad M_k(6)<1/10\ (k\ge2),}
\]
and an all-order amplitude bound \(\sup_{r\ge0}|J_k(r)|<1/2\) for every \(k\ge2\). Each separator is established below and is reproduced by the standalone exact-rational checker.

**1. Lower ninth moment.** For \(0\le r\le7/2\), the alternating Bessel series has the polynomial lower bound
\[
J_1(r)\ge L(r)=\sum_{m=0}^{5}\frac{(-1)^m(r/2)^{2m+1}}{m!(m+1)!}>0.
\]
The first omitted term is positive, and subsequent term magnitudes decrease. To see positivity, set \(t=r^2/4\le49/16\); then \(2L(r)/r=1-t/2+t^2/12-t^3/144+t^4/2880-t^5/86400\). The first four terms decrease as a function of \(t\ge0\) and at \(t=49/16\) equal \(29999/589824>0\); the final pair is nonnegative for \(t\le30\). Thus
\[
M_1(9)\ge\int_0^{7/2}rL(r)^9\,dr>\frac{137}{10000}.
\]
The final inequality is an exact integral of a rational polynomial, evaluated in `CHECK.py` without numerical quadrature.

**2. Upper sixth moment of the first order.** The integer-order Fourier integral for \(J_1\) shows \(|J_1^{(a)}(r)|\le1\) for every nonnegative integer derivative order. Hence, for \(F(r)=rJ_1(r)^6\),
\[
|F^{(4)}(r)|\le4\cdot6^3+r6^4.
\]
The composite Simpson sum on \([0,60]\) at step \(1/100\), with exact integer-rational enclosures for all its Bessel values, is strictly below \(1036/10000\). Its absolute integration error is at most
\[
\frac{60}{180}(1/100)^4(4\cdot6^3+60\cdot6^4)=0.00026208.
\]
For \(r>1\), the classical Watson–Nicholson modulus bound gives
\[
|J_1(r)|^2\le\frac{2}{\pi\sqrt{r^2-1}}.
\]
Thus the tail beyond 60 satisfies
\[
\int_{60}^\infty r|J_1(r)|^6dr
\le\left(\frac2\pi\right)^3\frac1{\sqrt{60^2-1}}<\frac8{27\cdot59}.
\]
A strict rational comparison now yields
\[
M_1(6)<\frac{1036}{10000}+0.00026208+\frac8{27\cdot59}<\frac{109}{1000}.
\]
The checker implements the ascending Bessel series with outward-rounded fixed-point integer intervals, 145 terms per node, scale \(10^{70}\), and an explicit first-omitted-term enclosure. At every node the omitted terms are decreasing, because their ratio from index 145 is at most \(900/(146\cdot147)<1\).

**3. All-order sixth-moment separator.** The inequality \(M_k(6)<1/10\) for \(k\ge2\) was established in the published sixth-power modal comparison listed in References. Independently, the accompanying checker reproduces its bounded-order inequalities: for \(2\le k\le11\), a rational Simpson certificate gives a sum below \(7/100\), its integration error below \(1/500\), and the Watson tail below \(1/100\). This yields \(M_k(6)<41/500<1/10\). For all \(k\ge12\), Xu's fifth-moment estimate \(M_k(5)<13/40\) (equation (3.87), valid for \(k\ge4\)) and Landau's uniform bound \(\sup|J_k|<(7/10)k^{-1/3}\) imply
\[
M_k(6)<\frac{91}{400k^{1/3}}\le\frac{91}{400\,12^{1/3}}<\frac1{10}.
\]
The last strict inequality is checked by cubing positive rational quantities, so the finite computation is not used to infer an infinite assertion.

**4. Universal amplitude gap.** For \(k\ge3\), Landau's bound directly implies \(\sup_r|J_k(r)|<(7/10)3^{-1/3}<1/2\). For \(k=2\) and \(0\le r\le3\), its alternating series yields \(0\le J_2(r)\le U(r^2)\), where
\[
U(s)=s/8-s^2/96+s^3/3072-s^4/184320+s^5/17694720.
\]
The derivative of \(U(9t)\) has strictly positive Bernstein coefficients for \(0\le t\le1\), and \(U(9)<1/2\). For \(r\ge3\), the Sonin quantity
\[
S(r)=J_2(r)^2+\frac{J_2'(r)^2}{1-4/r^2}
\]
satisfies \(S'(r)=-2J_2'(r)^2/[r(1-4/r^2)^2]\le0\). Exact Bessel series bounds at \(r=3\) give \(|J_2(3)|<49/100\), \(|J_2'(3)|<1/50\), so
\[
|J_2(r)|^2\le S(3)<(49/100)^2+(9/5)(1/50)^2<1/4.
\]
Thus the amplitude bound holds for all positive integer orders beyond one.

**5. Interpolation across every real exponent \(q\ge9\).** Hölder log-convexity of the moments with respect to \(r\,dr\) gives
\[
M_1(q)\ge M_1(9)\left(\frac{M_1(9)}{M_1(6)}\right)^{(q-9)/3}.
\]
Because \((137/10000)/(109/1000)>1/8\), the two rational moment separators yield
\[
M_1(q)>\frac{137}{10000}2^{-(q-9)}.
\]
For every \(k\ge2\), the sixth-moment and supremum bounds yield
\[
M_k(q)<\frac1{10}2^{-(q-6)}.
\]
Finally, \(137/10000>1/80=(1/10)2^{-3}\), so the first lower bound strictly exceeds the second upper bound for all real \(q\ge9\). This proves the claimed unique maximizing positive order.

**6. Sharp stability.** Xu's diagonal Fourier–Bessel decomposition and sharp planar stability theorem give the optimal coefficient in spectral form
\[
\Gamma_{2,q}=4\pi^2\left(M_0(q)^{2/q}-\max_{k\ge1}M_k(q)^{2/q}\right).
\]
The strict ordering from step 5 identifies the maximum uniquely at \(k=1\). The equality classes stated above follow from the strict convexity of the radial \(L^{q/2}\) norm in the spectral reduction, together with Xu's equality characterization. The result concerns the mixed norm only.

## Verification
Run `python3 CHECK.py` with Python 3 (standard library only). It verifies, with exact integer/fraction arithmetic, the ninth- and tenth-moment polynomial lower bounds, the sixth-moment rational Simpson enclosure, the elementary Bernstein and Sonin inequalities, and the independent finite-order sixth-moment certificates. The analytic extension to infinitely many orders uses explicitly cited published Landau and Xu estimates; the extension to all real exponents uses Hölder. Finite tests alone are not presented as infinite proofs.

## Relationship to prior work
Xu (first public October 14, 2026), Theorems 1.2–1.3 and Remark 3, proves zero-mode dominance throughout \(q>4\) and the optimal stability coefficient in spectral form, but notes that the maximizing nonzero circle degree is not known throughout that range. Xu's Proposition 3.11 orders the first three positive modes for \(4<q\le6\), without the present all-order, all-real-exponent range. The published *First-harmonic sharp sixth-power stability for circular mixed Fourier extension* proves the needed sixth-moment separator only at \(q=6\). The published *The first harmonic gives the sharp planar mixed-norm Fourier stability gap for every exponent \(q\ge27\)* proves the continuous interval starting at 27. Neither its statement nor the fixed sixth-power result implies the continuous interval \(9\le q<27\). The new ninth-moment certificate, sixth-moment upper bound and log-convex amplification bridge that gap. Carneiro–Oliveira e Silva–Sousa (2019) and Ciccone–Sousa (2025) establish other zeroth-mode dominance ranges, not this sharp positive-degree stability classification.

## Limitations
The sufficient threshold \(q=9\) is **not asserted optimal**. Nothing is proved here about the unique largest positive order for \(4<q<9\), including the interval between the known sixth exponent and 9. The theorem neither implies a fully descending sequence among all orders nor determines the unmixed planar \(L^q\) Fourier extension extremizers. The proof imports Landau's uniform bound, Xu's fifth-moment and modulus estimates, and the published spectral stability theorem. Publication priority remains provisional because an older equivalent Bessel-moment ordering under a different normalization might exist. Independent mathematical audit has not been performed.

## References
1. Z. Xu, *Sharp radial–angular mixed norm Fourier extension and global stability on spheres*, arXiv:2610.19648v1, first submitted October 14, 2026; Theorems 1.2–1.3, Proposition 3.11, Lemma 3.7, equation (3.87), Remark 3. https://arxiv.org/abs/2610.19648.
2. E. Carneiro, D. Oliveira e Silva and M. Sousa, *Sharp mixed norm spherical restriction*, arXiv:1710.10365v1, first submitted October 28, 2017; Adv. Math. 341 (2019), 583–608. https://arxiv.org/abs/1710.10365.
3. V. Ciccone and M. Sousa, *Global and local maximizers for some Fourier extension estimates on the sphere*, arXiv:2312.07309v1, first submitted December 12, 2023; J. Fourier Anal. Appl. 31 (2025), article 70. https://arxiv.org/abs/2312.07309.
4. *First-harmonic sharp sixth-power stability for circular mixed Fourier extension*, publicly accessible research record, November 1, 2026: https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-first-harmonic-sharp-sixth-power-stability-for-circular-mixed-fo--02fc40e0dcf1.
5. *The first harmonic gives the sharp planar mixed-norm Fourier stability gap for every exponent \(q\ge27\)*, publicly accessible research record, November 1, 2026: https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-the-first-harmonic-gives-the-sharp-planar-mixed-norm-fourier-sta--6d1a20405441.
6. L. J. Landau, *Bessel functions: monotonicity and bounds*, J. Lond. Math. Soc. 61 (2000), 197–215, doi:10.1112/S0024610799008352.
