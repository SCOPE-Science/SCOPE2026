# Inner pullbacks of a strip logarithm: exact Hankel, essential, and Garsia norms

## Finding
Let \(B\) be any nonconstant inner function on \(\mathbb D\) satisfying \(B(0)=0\). The analytic function
\[
\psi_B(z)=\log\frac{1+B(z)}{1-B(z)}
=2\sum_{j=0}^{\infty}\frac{B(z)^{2j+1}}{2j+1},\qquad \psi_B(0)=0,
\]
uses the branch real at the origin. Then \(\psi_B\in\mathrm{BMOA}_0\) is unbounded and its Hardy-space Hankel operator has the exact **operator and essential norms**
\[
\|H_{\overline{\psi_B}}\|=\|H_{\overline{\psi_B}}\|_{\mathrm{ess}}=\pi.
\]
For every \(a\in\mathbb D\) and the normalized Szegő kernel \(k_a\),
\[
\boxed{\quad\|H_{\overline{\psi_B}}k_a\|_2^2
=\frac{\pi^2}{2}-2\left(\operatorname{Im}\psi_B(a)\right)^2.\quad}
\]
Consequently the exact Garsia/reproducing-kernel testing norm is \(\pi/\sqrt2\), strictly smaller than the essential and operator norms. **Every norming kernel is characterized**, without exception, by
\[
\{a:\|H_{\overline{\psi_B}}k_a\|_2=\pi/\sqrt2\}
=B^{-1}((-1,1)).
\]
This set includes the origin. For \(B(z)=z^m\) it is the union of \(m\) diameters through the origin. Thus the maximal kernel test is attained in the disk, even though the Hankel operator is maximally noncompact and the strong reproducing-kernel thesis fails by exactly the factor \(\sqrt2\).

## Assumptions and scope
The circle \(\mathbb T\) carries normalized Lebesgue measure \(dm\); \(H^2\) has orthonormal basis \(1,z,z^2,\ldots\), and \(H^2_-=L^2(\mathbb T)\ominus H^2\). For \(f\in H^\infty\), first define \(H_{\overline{\psi_B}}f=P_-(\overline{\psi_B}f)\). The proof gives its unique bounded extension. An inner function is analytic in \(\mathbb D\) and has unimodular boundary values almost everywhere. A point kernel is \(k_a(z)=\sqrt{1-|a|^2}/(1-\bar a z)\). The essential norm is distance to the compact operators. The Garsia seminorm is \(\|\psi\|_G^2=\sup_{a\in\mathbb D}[P(|\psi|^2)(a)-|\psi(a)|^2]\). No finite-degree, smoothness or Blaschke assumption is imposed on \(B\); singular inner factors are allowed if the product vanishes at the origin.

## Proof
**1. Hardy integrability and boundary strip values.** Since \(B\) is inner and \(B(0)=0\), its nonnegative powers form an orthonormal sequence in \(H^2\). In particular the displayed odd-power series defines \(\psi_B\in H^2\): its squared norm is \(4\sum_{j\ge0}(2j+1)^{-2}=\pi^2/2\). On the boundary, where \(|B|=1\) almost everywhere, \((1+B)/(1-B)\) is purely imaginary, except on a null set. The analytic logarithm therefore has \(\operatorname{Im}\psi_B=+\pi/2\) or \(-\pi/2\) almost everywhere, so \(|\operatorname{Im}\psi_B|=\pi/2\) almost everywhere. The vanishing of \(B(0)\) means its boundary distribution is Haar: all nonzero Fourier moments \(\int B^n\,dm=B(0)^n=0\), so both signs have positive measure and the logarithmic real part has unbounded essential supremum.

**2. A bounded symbol gives the upper bound.** The boundary function \(\overline{\psi_B}-\psi_B=-2i\operatorname{Im}\psi_B\) has essential supremum \(\pi\). Its Hankel projection equals that of \(\overline{\psi_B}\), because \(\psi_B\) is analytic. Hence the projection norm estimate gives \(\|H_{\overline{\psi_B}}\|\le\pi\). This simultaneously proves the claimed bounded extension and \(\psi_B\in\mathrm{BMOA}\) by the classical Nehari characterization.

**3. Universal compressed Hilbert block and lower bound.** The input functions \(e_k=B^{2k}\), \(k\ge0\), form an orthonormal system in \(H^2\). The output functions \(f_j=\overline B^{2j+1}\), \(j\ge0\), are an orthonormal system in \(H^2_-\). For all \(j,k\ge0\), Fourier/inner-power orthogonality gives the exact compressed matrix
\[
\langle H_{\overline{\psi_B}} e_k,f_j\rangle
=\frac{2}{2(j+k)+1}=\frac1{j+k+1/2}.
\]
The positive matrix \(A=(j+k+1/2)^{-1}\) on \(\ell^2(\mathbb N_0)\) has norm at least \(\pi\). Here is a self-contained lower-bound argument, independent of a general spectral theorem. Put \(x^{(L)}_j=j^{-1/2}\) on \(1\le j\le L\), zero elsewhere, so \(\|x^{(L)}\|_2^2=\log L+O(1)\). Comparing the monotone double sum with the corresponding integral (the derivative errors are absolutely summable) yields
\[
\langle Ax^{(L)},x^{(L)}\rangle
=\int_1^L\int_1^L\frac{dx\,dy}{\sqrt{xy}(x+y)}+O(1).
\]
After \(x=e^s,y=e^t\), this becomes
\[
\int_0^{\log L}\int_0^{\log L}\frac{ds\,dt}{2\cosh((s-t)/2)}+O(1)
=\pi\log L+O(1),
\]
since \(\int_{-\infty}^\infty[2\cosh(u/2)]^{-1}du=\pi\) and the kernel has a finite first moment. The quotient approaches \(\pi\). By compression, \(\|H_{\overline{\psi_B}}\|\ge\pi\); together with step 2 this proves the exact operator norm.

**4. Exact essential norm.** Repeat the same comparison for vectors supported on \(L\le j\le L^2\), with coefficients \(j^{-1/2}\). Their squared norms equal \(\log L+O(1)\), and the compressed quadratic forms equal \(\pi\log L+O(1)\). Their normalized lifts \(\sum_j c_j e_j\) are weakly null in \(H^2\), because the \(e_j\) are orthonormal and the supports escape to infinity. Every compact operator sends this sequence to zero in norm, while the compressed Hankel Rayleigh quotients approach \(\pi\). Thus the essential norm is at least \(\pi\), hence equals \(\pi\) by step 2.

**5. Kernel testing and complete norming locus.** For analytic \(\psi\in H^2\), the Bonsall/Poisson identity is
\[
\|H_{\overline\psi}k_a\|_2^2=P(|\psi|^2)(a)-|\psi(a)|^2.
\]
Equivalently, it follows by expanding the analytic Taylor series and the normalized Szegő kernel. At each \(a\), the centered harmonic real and imaginary parts of \(\psi_B\) have the same Poisson variance: \(P((\psi_B-\psi_B(a))^2)(a)=0\). The boundary imaginary part has square \(\pi^2/4\) almost everywhere, and its Poisson mean is \(\operatorname{Im}\psi_B(a)\). Therefore the sum of the two centered variances equals
\[
2\left(\frac{\pi^2}{4}-(\operatorname{Im}\psi_B(a))^2\right),
\]
proving the identity. Equality in the maximal value \(\pi^2/2\) occurs precisely when \(\operatorname{Im}\psi_B(a)=0\). The conformal strip map \(w\mapsto\log[(1+w)/(1-w)]\) has zero imaginary part exactly on \((-1,1)\), giving the asserted preimage locus. As \(B(0)=0\), the supremum is attained at \(a=0\). For powers \(B(z)=z^m\), the condition \(z^m\in(-1,1)\) gives the \(m\) diameters.

## Verification
Run `python3 CHECK.py` (standard Python only). It checks Poisson integrals for several monomial inner functions and interior test points, the universal Hilbert compression's increasing finite Rayleigh quotients, the \(H^2\) series, and the predicted norming rays. The run passed **107 finite checks**. These are numerical checks, not proofs of the uniform infinite-inner or essential-norm statements; steps 1–5 supply those proofs. The integral comparison and the weak-null argument are essential for the infinite-dimensional claim.

## Relationship to prior work
Dyakonov's September 2026 paper poses the strong reproducing-kernel thesis (SRKT) and gives the Poisson/Hankel identity. A public October 2026 research result for the **single-boundary** logarithm \(-\log(1-z)\) proves the same ratio \(\pi/\sqrt2\) but obtains the testing supremum only as a boundary limit. That result and the classical Hilbert-matrix norm are *not* new here. The present theorem instead gives a uniform full-inner-function family, an exact **interior-attainment locus** and an **exact essential norm** simultaneously. The published 2025 Garsia-extreme-point theorem covers the general consequence that a Garsia-norm-attaining function is an extreme point, not these exact Hardy Hankel values or norming sets. Earlier studies of logarithms of univalent functions, generalized Hilbert matrices and inner-function composition are related, but inspected statements do not imply this particular three-part quantitative classification.

## Limitations
The claim is restricted to inner functions fixing zero and this canonical logarithmic strip map. It does not classify all unbounded analytic symbols satisfying or failing SRKT, nor all Garsia-extreme elements. The ratio \(1/\sqrt2\) is not asserted to be universal among Hankel operators. Previous general inner-composition principles may permit alternative shorter proofs; an equivalent theorem could exist under older Nehari or boundary-step terminology. No independent mathematical audit has been performed.

## References
1. K. M. Dyakonov, *The strong reproducing kernel thesis for Hankel operators and the Garsia norm*, arXiv:2609.33242v1 (first public September 27, 2026), especially Section 1 and Problem 1, https://arxiv.org/abs/2609.33242.
2. K. M. Dyakonov, *Extremal problems in BMO and VMO involving the Garsia norm*, arXiv:2404.05565v2, Sections 1–2 (first public April 8, 2024), https://arxiv.org/html/2404.05565v2.
3. *An exact square-root-two SRKT gap for the logarithmic Hilbert Hankel symbol*, published-finding corpus public research record, October 11, 2026 (single-boundary comparison).
4. F. F. Bonsall, *Boundedness of Hankel matrices*, J. London Math. Soc. 29 (1984), 289–300 (classical kernel/Poisson identity).
5. D. Girela, *Integral means and BMOA-norms of logarithms of univalent functions*, J. London Math. Soc. 33 (1986), 117–132 (related earlier logarithmic-function literature; its full text was not evaluated for the present exact theorem).
