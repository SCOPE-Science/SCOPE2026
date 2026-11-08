# Exact half-density Gabor-frame classification of Gaussian–first-Hermite mixtures

## Finding
For any complex coefficients \(A,B\), not both zero, let
\[
 g_{A,B}(t)=(At+B)e^{-\pi t^2},\qquad t\in\mathbb R.
\]
For every \(a,b>0\) with \(ab=1/2\), write
\[
 \mathcal G(g_{A,B},a,b)=\{M_{mb}T_{na}g_{A,B}:m,n\in\mathbb Z\},
 \quad T_xf(t)=f(t-x),\quad M_\xi f(t)=e^{2\pi i\xi t}f(t).
\]
Then the complete frame classification is
\[
 \boxed{\mathcal G(g_{A,B},a,b)\text{ is a frame for }L^2(\mathbb R)
 \quad\Longleftrightarrow\quad B\ne0.}
\]
This includes all complex Gaussian–first-Hermite mixtures and all rectangular lattice aspect ratios of area \(1/2\). In particular, an arbitrarily small nonzero Gaussian component removes the obstruction of the pure first Hermite window at this critical rational oversampling.

## Assumptions and scope
The coefficients \(A,B\) are arbitrary complex numbers with \(|A|+|B|>0\). The lattice is rectangular, with \(a>0\), \(b>0\), and exactly \(ab=1/2\). A frame means the existence of constants \(0<C\le D<\infty\) such that, for every \(f\in L^2(\mathbb R)\),
\[
 C\|f\|_2^2\le\sum_{m,n\in\mathbb Z}|\langle f,M_{mb}T_{na}g_{A,B}\rangle|^2\le D\|f\|_2^2.
\]
The result does not assert uniform positive lower bounds as \(B\to0\), or classify arbitrary polynomial–Gaussian windows of higher degree.

## Proof
**1. Dilation and Zak criterion.** The unitary dilation \(D_af(t)=\sqrt a\,f(at)\) carries the lattice \((a,b)\) to \((1,1/2)\) and the window to a nonzero constant multiple of \((t-\delta)e^{-\pi\lambda t^2}\), with \(\lambda=a^2>0\) and \(\delta=-B/(aA)\) when \(A\ne0\). Write the Zak transform
\[
 Zf(x,\omega)=\sum_{k\in\mathbb Z}f(x-k)e^{2\pi i k\omega}.
\]
At lattice \((1,1/2)\), the integer-lattice Zak/Parseval criterion states that a Schwartz window \(f\) generates a frame precisely when
\[
 \inf_{(x,\omega)\in[0,1]^2}\big(|Zf(x,\omega)|^2+|Zf(x,\omega+1/2)|^2\big)>0.
\]
The supremum is automatically finite by continuity and quasi-periodicity. This criterion follows directly by splitting modulations into their integer and half-integer cosets and applying Fourier-series Parseval in Zak coordinates.

**2. The exact two-parity Wronskian.** For \(\lambda>0\), introduce
\[
 E=\sum_{j\in2\mathbb Z}e^{-\pi\lambda(x-j)^2}e^{2\pi i j\omega},\quad
 O=\sum_{k\in2\mathbb Z+1}e^{-\pi\lambda(x-k)^2}e^{2\pi i k\omega},
\]
\[
 H_E=\sum_{j\in2\mathbb Z}(x-j)e^{-\pi\lambda(x-j)^2}e^{2\pi i j\omega},\quad
 H_O=\sum_{k\in2\mathbb Z+1}(x-k)e^{-\pi\lambda(x-k)^2}e^{2\pi i k\omega}.
\]
All sums converge locally uniformly with derivatives. The two Zak values vanish simultaneously for \(f(t)=(t-\delta)e^{-\pi\lambda t^2}\) exactly when
\[
 H_E-\delta E=0\quad\text{and}\quad H_O-\delta O=0.
\]
Consequently, simultaneous vanishing forces \(W:=H_EO-H_OE=0\). Expand the double sum, set \(j=2r\), \(k=2s+1\), and group by \(m=r+s\). With \(\phi_\lambda(t)=e^{-2\pi\lambda t^2}\), this yields the **exact identity**
\[
 W(x,\omega)=C_\lambda e^{2\pi i\omega}
 Z\phi_\lambda(x-1/2,2\omega+1/2),
\quad C_\lambda=\sum_{r\in\mathbb Z}(4r+1)e^{-\pi\lambda(4r+1)^2/2}.
\]
Indeed, for fixed \(m\), the difference \(k-j\) ranges through integers congruent to \(1\pmod4\) when \(m\) is even, and through integers congruent to \(3\pmod4\) when \(m\) is odd. Their weighted sums are \(C_\lambda\) and \(-C_\lambda\), respectively, and the Gaussian product is
\[
 e^{-\pi\lambda((x-j)^2+(x-k)^2)}
 =e^{-2\pi\lambda(x-m-1/2)^2}e^{-\pi\lambda(k-j)^2/2}.
\]

**3. Nonzero factor for every aspect ratio.** Put
\[
 P_\lambda(u)=\sum_{r\in\mathbb Z}e^{-8\pi\lambda(r+u)^2}.
\]
Termwise differentiation gives \(P_\lambda'(1/4)=-4\pi\lambda C_\lambda\). By Poisson summation,
\[
 P_\lambda(u)=(8\lambda)^{-1/2}\vartheta_3(\pi u,q),
 \quad q=e^{-\pi/(8\lambda)}\in(0,1).
\]
Jacobi's triple product expresses the theta factor as
\[
 \vartheta_3(\pi u,q)=\prod_{n\ge1}
 (1-q^{2n})\bigl(1+2q^{2n-1}\cos(2\pi u)+q^{4n-2}\bigr).
\]
Every factor is positive for real \(u\). Differentiating its logarithm shows that \(P_\lambda'(u)<0\) for \(0<u<1/2\), since each summand is a strictly negative multiple of \(\sin(2\pi u)>0\). Hence \(C_\lambda>0\) for **every** \(\lambda>0\).

**4. The only Wronskian zeros.** The same triple product, applied to
\[
 Z\phi_\lambda(u,v)=e^{-2\pi\lambda u^2}\vartheta_3(\pi v-2\pi i\lambda u,e^{-2\pi\lambda}),
\]
shows that this Gaussian Zak transform vanishes for real \(u,v\) exactly when \(u\equiv 1/2\pmod1\) and \(v\equiv1/2\pmod1\). The identity in step 2 therefore implies
\[
 W(x,\omega)=0\quad\Longleftrightarrow\quad
 x\in\mathbb Z,\quad2\omega\in\mathbb Z.
\]
At all these points, parity symmetry of the Gaussian gives \(H_E=H_O=0\), while \(E\) and \(O\) are nonzero: the modulation phases are constant on each parity class and the corresponding Gaussian sums have strictly positive magnitudes. Thus \(H_E-\delta E=H_O-\delta O=0\) at such a point forces \(\delta=0\). For \(\delta\ne0\), both Zak values cannot vanish anywhere, and the compact Zak criterion gives a strictly positive lower frame bound.

**5. Boundary coefficient cases.** If \(A\ne0\) and \(B=0\), then \(\delta=0\); at \(x=\omega=0\), parity symmetry gives \(H_E=H_O=0\), hence the two Zak values both vanish and the lower frame inequality fails. If \(A=0\) and \(B\ne0\), the window is a nonzero Gaussian. Its Zak transform has precisely one zero per fundamental Zak cell at \((1/2,1/2)\), whereas the half-frequency-shifted Zak transform is nonzero there, so the Zak criterion again yields a frame. All cases are covered.

## Verification
The standalone `CHECK.py` uses the defining parity sums, independently computes their Wronskian, and compares it to the regrouped Gaussian Zak expression for multiple positive decay parameters and non-symmetric phase-space locations. It also checks the first-Hermite simultaneous zero and samples nonzero mixtures. Execute `python3 CHECK.py` with the Python standard library. The sample checks are not an infinite proof; steps 1–5 give the full analytical argument, including the global zero classification and strict positivity for all \(\lambda>0\).

## Relationship to prior work
Faulhuber and Petersen determine the frame set of the **pure first Hermite** window and prove its failure at rational lattice product \(1/2\). The Gaussian frame theorem establishes the opposite endpoint. The result here classifies the **entire complex two-dimensional span of the first two Hermite windows at the exceptional product** and all rectangular aspect ratios, neither of which follows by openness from a nonframe endpoint. The known vector-valued two-window Hermite frame theorem concerns two separately analyzed windows and does not imply a single-mixture frame. Lemvig's November 2026 degree-based theorem proves rational safety when the reduced denominator-minus-numerator exceeds the polynomial degree; here the difference and degree are both one, so that theorem does not cover the claim. The exact parity-Wronskian identity and its theta zero geometry supply the distinguishing argument.

## Limitations
The classification is confined to a polynomial of degree at most one, a Gaussian of fixed profile up to dilation, rectangular lattices, and lattice product exactly \(1/2\). It gives no explicit optimal numerical frame bounds and is not uniform as \(B\to0\). A previously unindexed theta-function or Zak-transform formulation could contain an equivalent result; independently establishing publication priority remains necessary. The use of known Gaussian Zak zeros and the standard Zak frame criterion is acknowledged.

## References
1. M. Faulhuber and P. Petersen, *The frame set of the first Hermite function*, arXiv:2609.02610, first submitted 2 September 2026, revised 1 October 2026; https://arxiv.org/html/2609.02610v2 .
2. K. Gröchenig, J. L. Romero, and J. Stöckler, *Sharp Results on Sampling with Derivatives in Shift-Invariant Spaces and Multi-Window Gabor Frames*, Constructive Approximation 51 (2020), first published 11 March 2019; https://doi.org/10.1007/s00365-019-09456-3 .
3. J. Lemvig, *On the Gabor frame set of polynomial–Gaussian windows*, arXiv:2611.05337v1, first submitted 3 November 2026; https://arxiv.org/pdf/2611.05337 .
4. A. Horst, J. Lemvig, and A. E. Videbæk, *On the non-frame property of Gabor systems with Hermite generators and the frame set conjecture*, Applied and Computational Harmonic Analysis 76 (2025); https://doi.org/10.1016/j.acha.2025.101747 .
