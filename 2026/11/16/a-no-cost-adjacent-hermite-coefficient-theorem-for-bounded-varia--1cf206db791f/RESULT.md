# A no-cost adjacent Hermite coefficient theorem for bounded variation

## Finding
Let \(\operatorname{He}_k\) denote the probabilists' Hermite polynomial and let \(\phi(x)=(2\pi)^{-1/2}e^{-x^2/2}\). For every real bounded-variation function \(f:\mathbb R\to\mathbb R\), every integer \(n\ge1\), and the normalized Gaussian-Hermite coefficients
\[
a_k(f)=\frac1{\sqrt{k!}}\int_{\mathbb R}f(x)\operatorname{He}_k(x)\phi(x)\,dx,
\]
write \(r_n=0\) when \(n\) is odd, and let \(r_n\) be the least positive zero of \(\operatorname{He}_n\) when \(n\) is even. Then the **sharp simultaneous two-coefficient estimate** is
\[
\boxed{\sqrt{a_n(f)^2+a_{n+1}(f)^2}\le C_n\operatorname{Var}(f),\qquad C_n=\frac{e^{-r_n^2/2}|\operatorname{He}_{n-1}(r_n)|}{\sqrt{2\pi n!}}.}
\]
The constant is exactly the sharp constant for the single coefficient \(a_n\), so adjoining the next Hermite coefficient costs nothing in the Euclidean sharp norm. The property ends immediately: for every \(n\ge1\), the sharp Euclidean norm of the block \((a_n,a_{n+1},a_{n+2})\), and of every longer consecutive block, is **strictly greater** than \(C_n\).

When \(n\) is odd, equality with positive variation occurs exactly for single-jump functions at zero, modulo additive constants and nonzero scalar multiples. When \(n\) is even, equality occurs exactly for two-jump functions supported at the two locations \(\pm r_n\), with opposite jump signs and arbitrary nonnegative relative magnitudes (including a zero magnitude), again modulo constants and nonzero scaling.

For odd \(n=2m+1\), the constant is explicit:
\[
C_{2m+1}=\frac{(2m)!}{2^m m!\sqrt{2\pi(2m+1)!}}.
\]
All assertions hold uniformly over the complete real bounded-variation class on the line, not only over step functions or finite-dimensional polynomial inputs.

## Assumptions and scope
Here \(\operatorname{Var}(f)\) is total variation over the whole real line. Functions of finite variation are bounded and have finite limits at both ends, so every coefficient integral is absolutely convergent. The Gaussian normalization is essential: \(\int\operatorname{He}_k^2\phi=k!\). The continuous derivative-free Stieltjes measure \(df\) is allowed to have absolutely continuous, singular-continuous, or jump components. All the indices \(n\) are positive integers. Equality concerns nonconstant real functions with \(\operatorname{Var}(f)>0\).

## Proof
**Primitive reduction.** Rodrigues' identity gives
\[
\int_{-\infty}^x\frac{\phi(t)\operatorname{He}_k(t)}{\sqrt{k!}}\,dt=-\frac{\phi(x)\operatorname{He}_{k-1}(x)}{\sqrt{k!}}\quad (k\ge1).
\]
Stieltjes integration by parts (the primitives vanish at both ends) expresses each coefficient as an integral of this primitive against \(-df\). Therefore the sharp operator norm from scalar total variation to any finite Euclidean coefficient block is the supremum of the Euclidean length of its primitive vector. A unit jump at any chosen point attains the corresponding length.

**Two-mode energy.** Set \(y(x)=\phi(x)\operatorname{He}_{n-1}(x)/\sqrt{n!}\). Then \(y'=-\phi\operatorname{He}_n/\sqrt{n!}\) and the Hermite equation yields
\[
y''+xy'+ny=0.
\]
The squared primitive-vector length is \(F=y^2+y'^2/(n+1)\). Compare it to the Sonin energy \(H=y^2+y'^2/n\). Direct differentiation yields
\[
H'=-\frac{2x}{n}y'^2,\qquad F'=\frac{2y'}{n+1}(y-xy').
\]
Both \(F\) and \(H\) are even. The energy \(H\) is strictly decreasing on positive intervals of nonzero length. Moreover \(F\le H\), with equality precisely at zeros of \(\operatorname{He}_n\).

If \(n\) is odd, \(\operatorname{He}_n(0)=0\), so \(F(0)=H(0)\) and \(F(x)\le H(x)<H(0)\) for every \(x>0\). Thus zero is the unique maximizer.

If \(n=2m\) is even, let \(0<r_1<\cdots<r_m\) be the positive zeros of \(\operatorname{He}_n\), and set \(r_n=r_1\). Its product representation and differential equation imply
\[
\frac{\operatorname{He}_n'(x)}{n\operatorname{He}_n(x)}=-\frac{2x}{n}\sum_{j=1}^{m}\frac1{r_j^2-x^2},\qquad \frac2n\sum_{j=1}^{m}\frac1{r_j^2}=1.
\]
Hence \(\operatorname{He}_n'(x)/(n\operatorname{He}_n(x))<-x\) for \(0<x<r_1\). As \(\operatorname{He}_{n-1}=\operatorname{He}_n'/n\), this makes \(y'\) and \(y-xy'\) have the same sign. Therefore \(F'>0\) throughout \((0,r_1)\). For \(x>r_1\), the energy comparison gives \(F(x)\le H(x)<H(r_1)=F(r_1)\). Thus exactly \(\pm r_n\) maximize \(F\). The value of \(F\) at these points yields the stated constant. The same argument with \(H\) alone shows the scalar coefficient \(a_n\) has the identical sharp constant.

**Equality.** At an extremizer, equality in the vector-measure triangle inequality requires all nonzero parts of \(df\) to be supported on the maximizing primitive locations and their primitive vectors to be aligned after applying jump signs. In the odd case there is one such location, zero. In the even case \(\operatorname{He}_n(\pm r_n)=0\) and \(\operatorname{He}_{n-1}\) is odd, so the two primitive vectors are exactly opposites. This gives precisely the stated jump classifications.

**Three-mode strictness.** At any maximizing point \(r=r_n\), the Hermite recurrence gives \(\operatorname{He}_{n+1}(r)=-n\operatorname{He}_{n-1}(r)\ne0\). The third primitive component, corresponding to coefficient \(a_{n+2}\), is therefore nonzero at that point. A single unit jump there gives a three-block Euclidean norm strictly larger than \(C_n\), and adding further components cannot decrease it.

## Verification
A standalone checker (`CHECK.py`) independently reconstructs the first several probabilists' Hermite polynomials from their recurrence, checks the exact polynomial identity for \(F'\), computes all positive roots, and compares the proposed maxima to numerical sample points. The proof above supplies all-degree statements; the finite checker is supplementary and not an infinite certificate.

## Relationship to prior work
Sluchak, arXiv:2611.04067 (first public November 2, 2026), formulates the sharp *individual* bounded-variation coefficient norm via cumulative primitives and discusses orthogonal expansions, but does not give this sharp **simultaneous consecutive Gaussian-Hermite** norm, its parity-dependent equality structure, or the exact two-to-three-block discontinuity. The scalar Sonin energy argument and the monotonic decay of individual Gaussian-derivative extremal heights are classical (Szegő, *Orthogonal Polynomials*, §7.6, and an explicit 2017 discussion on Math Stack Exchange); the present paired norm needs the extra comparison \(F\le H\), a strict first-root analysis for even \(n\), and a third-mode obstruction. The ordinary Laguerre sharp-BV analyses concern a different orthogonal system, while neighboring Hermite concentration results concern different norms and operators.

## Limitations
This is a sharp real-BV-to-two-coefficient theorem, not a uniform approximation theorem for Hermite expansions. Its no-cost property relies on the Gaussian and precisely the probability-orthonormal Hermite normalization; arbitrary coefficient weights or nonadjacent modes are not covered. Equality functions have jumps, while continuous bounded-variation functions approach but cannot attain the sharp norm. Historical publication priority remains provisional, particularly regarding possible older formulations as a two-component Sonin or Gaussian-derivative energy inequality.

## References
1. V. Sluchak, *Bounds for Orthogonal Expansion Coefficients via Weighted Primitives*, arXiv:2611.04067, first version November 2, 2026, §§3–4, 9–11.
2. G. Szegő, *Orthogonal Polynomials*, 4th ed., AMS Colloquium Publications 23, 1975, §7.6 (classical Sonin-type amplitude comparisons).
3. *Extremas of derivatives of Gaussian*, Mathematics Stack Exchange question 2256158 (2017), exposition of the classical Sonin–Butlewski–Pólya energy argument.
4. T. H. Koekoek, *Hermite polynomials*, Delft special-functions lecture notes, definitions and recurrence identities.
