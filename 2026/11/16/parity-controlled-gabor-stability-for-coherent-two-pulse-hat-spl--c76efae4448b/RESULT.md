# Parity-controlled Gabor stability for coherent two-pulse hat-spline windows

## Finding
Let \(h(t)=(1-|t|)_+\). For each integer \(d\geq1\) and complex \(c\), put \(g_{d,c}(t)=h(t)+c h(t-d)\) and consider the rectangular Gabor system \(\{e^{\pi i m t}g_{d,c}(t-n):m,n\in\mathbb Z\}\) on \(L^2(\mathbb R)\). Write \(\rho=|c|\) and \(D=1+\rho^2\). Its frame operator has spectrum exactly \([A_{d,c},B_{d,c}]\), with the following sharp endpoints (the value \(A=0\) denotes failure of the lower frame inequality).

For even \(d\),
\[
 A_{d,c}=(\rho-1)^2,\qquad B_{d,c}=2(\rho+1)^2.
\]
Consequently it is a frame exactly when \(\rho\ne1\).

For odd \(d\), define \(m_d(\phi)=\min_{\theta\in[0,2\pi]}\cos\theta\cos(d\theta-\phi)\), with \(\phi=\arg c\) when \(c\ne0\). Then
\[
 A_{d,c}=D+2\rho m_d(\phi),\qquad B_{d,c}=2D.
\]
For \(c=0\), interpret \(A=1\) and \(B=2\). This Gabor system is a frame for every \(c\ne-1\), and is not a frame for \(c=-1\). In both parity classes, **all** the nonframe systems remain complete in \(L^2(\mathbb R)\) but are not frames.

Among \(c\ne0\) and all positive integer delays, every frame has sharp frame-operator condition number \(B_{d,c}/A_{d,c}\ge2\), with equality **if and only if** \(d=1\) and \(c\) is real positive. Thus positive adjacent superposition is the unique nontrivial member of the entire two-pulse design class that preserves the optimal condition number \(2\) of the original hat. More explicitly,
\[
 A_{1,c}=1+|c|^2+\operatorname{Re}c-|c|,\qquad B_{1,c}=2(1+|c|^2).
\]
For positive real \(c\) and delay \(d=3\), the sharp bounds instead are \(A_{3,c}=1+c^2-9c/8\) and \(B_{3,c}=2(1+c^2)\). For example, at \(c=1\), the adjacent design has condition number \(2\), whereas delay three has condition number \(32/7\).

The singular boundary has a distinct parity-dependent transverse scaling. Write \(c=-1+u+iv\), with real \(u,v\to0\). At each fixed odd \(d\),
\[
 A_{d,-1+u+iv}=u^2+\frac{v^2}{d^2+1}+O_d\big((|u|+|v|)^3\big).
\]
For even \(d\), along \(c=-1+iv\), the lower bound is instead \(v^4/4+O(v^6)\). Hence a small imaginary phase perturbation lifts the odd-delay singularity quadratically, but lifts the even-delay singularity only quartically.

## Assumptions and scope
The window is the centered, unit-height order-two cardinal B-spline; the delay \(d\) is an **integer** at least one; the amplitude \(c\) may be any complex number; and the Gabor lattice is fixed at translation step \(a=1\), modulation step \(b=1/2\), with the modulation convention \(M_bf(t)=e^{2\pi ibt}f(t)\). Lower and upper bounds refer to squared-analysis-energy inequalities, not their square roots. The exact spectrum is as a bounded positive operator on \(L^2(\mathbb R)\). The theorem does not classify noninteger delays or other lattice densities.

For each fixed odd delay, the one-variable extremum defining \(m_d\) is a finite exact problem: it is attained at one of the finitely many solutions, modulo \(2\pi\), of
\[
 \sin\theta\cos(d\theta-\phi)+d\cos\theta\sin(d\theta-\phi)=0.
\]
Thus the formula gives the optimal endpoint for every complex amplitude without any infinite-dimensional optimization. For algebraic unit phase it can be reduced to algebraic equations; no assertion is made that a uniformly elementary closed radical exists for arbitrary delay.

## Proof
**1. Exact fiberization.** Use the unitary integer Zak transform \(Zf(x,\theta)=\sum_{n\in\mathbb Z}f(x+n)e^{-in\theta}\) on \(0\le x<1\), \(0\le\theta<2\pi\), with normalized frequency measure. At integer time translation and half-integer modulation, the frame operator is unitarily equivalent to multiplication by
\[
 E_g(x,\theta)=|Zg(x,\theta)|^2+|Zg(x,\theta+\pi)|^2.
\]
This follows by grouping even and odd modulations and applying Parseval in each integer-translation Fourier series. With \(h(t)=(1-|t|)_+\), for \(0\le x\le1\) direct evaluation of its two nonzero integer translates gives
\[
 Zh(x,\theta)=(1-x)+xe^{i\theta},\qquad Z(h(\cdot-d))(x,\theta)=e^{-id\theta}Zh(x,\theta).
\]
Therefore, writing \(H_\pm=(1-x)\pm xe^{i\theta}\) and \(F_\pm=1+(\pm1)^d c e^{-id\theta}\),
\[
 E_{d,c}(x,\theta)=|F_+H_+|^2+|F_-H_-|^2.
\]
The continuous function \(E\) on the compact two-torus has spectrum equal to its connected range, the interval between its minimum and maximum. The endpoints are consequently the exact optimal frame bounds whenever the minimum is positive.

**2. Even-delay class.** If \(d\) is even, \(F_+=F_-\) and
\[
 E_{d,c}(x,\theta)=2\big((1-x)^2+x^2\big)|1+ce^{-id\theta}|^2.
\]
The first factor ranges from \(1\) to \(2\), and the modulus factor ranges independently between \((\rho-1)^2\) and \((\rho+1)^2\); these extremes are simultaneously attainable. This gives both asserted bounds and the unit-circle failure condition.

**3. Odd-delay class.** If \(d\) is odd, put \(t=2x(1-x)\in[0,1/2]\) and \(P_d(\theta)=\cos\theta\cos(d\theta-\phi)\). Expanding the two terms exactly gives
\[
 E_{d,c}(x,\theta)=2D(1-t)+4\rho t P_d(\theta).
\]
For each angle this is affine in \(t\). As \(D\ge2\rho\) and \(|P_d|\le1\), its maximum is \(2D\), achieved at \(x=0\). Its minimum is attained at \(t=1/2\), and equals \(D+2\rho\min P_d\). Equality \(A=0\) requires \(\rho=1\) and \(\min P_d=-1\). The product \(P_d=-1\) requires \(|\cos\theta|=1\), hence \(\theta\in\{0,\pi\}\), and then forces \(\cos\phi=-1\), so \(c=-1\). Conversely \(c=-1\) gives zeros at those angles. For \(d=1\), the identity \(P_1(\theta)=[\cos\phi+\cos(2\theta-\phi)]/2\) yields the explicit adjacent-window bound. For \(d=3\) with real positive \(c\), writing \(v=\cos^2\theta\) gives \(P_3=4v^2-3v\), minimized at \(v=3/8\) with value \(-9/16\), proving that example.

**4. Completeness at the singularities.** Under the Zak unitary, the system's analysis has zero kernel precisely when multiplication by \(E\) has zero kernel, i.e., when the zero set of \(E\) has planar measure zero. For even \(d\) with \(\rho=1\), this set is a finite union of vertical frequency lines. For odd \(d\) with \(c=-1\), it consists of the two points \((x,\theta)=(1/2,0),(1/2,\pi)\) on a fundamental torus. Both sets have measure zero; since \(E\) is continuous with a zero, the system is complete but not bounded below.

**5. Sharp conditioning.** For even \(d\) and \(\rho>0\), the ratio is strictly greater than \(2\) whenever it is finite, because \((1+\rho)^2>(1-\rho)^2\). For odd \(d\), the ratio is \(2D/(D+2\rho m_d)\). If \(d\ge3\), then \(P_d\) is a nonconstant trigonometric polynomial of integral zero on the circle, so its minimum is strictly negative. Hence its ratio is strictly greater than \(2\). If \(d=1\), \(m_1=(\cos\phi-1)/2\le0\), with equality precisely when \(\phi=0\), proving the unique positive-adjacent optimum for nonzero \(c\). The case \(c=0\) has ratio \(2\) for all delays and is excluded from the uniqueness assertion.

**6. Singularity unfolding.** For odd \(d\), let \(\phi=\pi+\delta\) and write \(\min P_d=-M_d(\delta)\) with \(M_d(\delta)=\max_\theta\cos\theta\cos(d\theta-\delta)\). At \(\delta=0\), the only maxima of value \(1\) modulo \(2\pi\) are \(\theta=0,\pi\), both nondegenerate, with second derivative \(-(d^2+1)\). Taylor expansion near \(\theta=0\), followed by completing the square in \(\theta\), gives
\[
 M_d(\delta)=1-\frac{\delta^2}{2(d^2+1)}+O_d(\delta^4).
\]
Uniform strict separation from the other angles makes this the global maximum for small \(\delta\). Thus \(A=(\rho-1)^2+\rho\delta^2/(d^2+1)+O_d(\delta^4)\). For \(c=-1+u+iv\), \(\rho-1=-u+O(u^2+v^2)\) and \(\delta=O(v)\) with \(\delta^2=v^2+O((|u|+|v|)^3)\), which yields the stated quadratic normal form. In the even class, \(A=(\sqrt{1+v^2}-1)^2=v^4/4+O(v^6)\) on the imaginary line.

## Verification
A standalone `CHECK.py` implements the direct Zak-fiber formula, the derived parity formula and numerical extremal searches for multiple delays and complex amplitudes. Its saved-package replay passed 3,536 finite assertions. These finite tests verify normalization and sample boundary cases; the infinite-dimensional statement, global extrema, and parameter-uniform claims follow from the analytic steps above. The only externally required Python dependency for the checker is SciPy (standard library otherwise).

## Relationship to prior work
The recent hat-spline Zak-zero and Gabor-frame results of Stangl and Frederick (arXiv:2609.00481, first submitted August 31, 2026) and Hasannasab and Lemvig (arXiv:2609.13116, first submitted September 11, 2026) treat the **unmodified** B-spline at varying lattice parameters. Their main results do not supply the exact delay-parity and complex-coefficient frame spectrum for the **coherently filtered** generator here. Christensen, Kim and Kim (arXiv:1708.04803) study scaled splines and *separate approximate dual windows* formed from linear combinations; that construction does not entail the claimed sharp bounds, singular classification, or unique conditioning optimum for the double-hat analysis generator. The standard Zak/Zibulski–Zeevi fiber method is prior work and is explicitly used here; only the resulting complete two-pulse classification is claimed.

## Limitations
All delay indices are integral and the redundancy is exactly two with translation step one. The general odd-delay lower bound requires a finite one-variable trigonometric minimization, which is explicit but need not simplify into radicals. No novelty proof can be extracted solely from the absence of matching keywords; equivalent formulations in older finite-impulse-response-filter/Gabor literature remain possible. There is no independent mathematical audit. The finite checker is not a substitute for the analytic proof.

## References
1. A. Stangl and C. Frederick, *The frameset of the second-order B-Spline along \(ab=1/q\)*, arXiv:2609.00481v1 (August 31, 2026); https://arxiv.org/abs/2609.00481.
2. M. Hasannasab and J. Lemvig, *The zero set of the Zak transform of B-splines with applications to Gabor frames*, arXiv:2609.13116v1 (September 11, 2026); https://arxiv.org/abs/2609.13116.
3. O. Christensen, H. O. Kim and R. Y. Kim, *B-spline approximations of the Gaussian, their Gabor frame properties, and approximately dual frames*, arXiv:1708.04803 (August 16, 2017); https://arxiv.org/abs/1708.04803.
4. K. Gröchenig, *Foundations of Time-Frequency Analysis*, Birkhäuser, 2001 (standard Zak-frame background).
