# Exact endpoint instability for radius-three Boolean Hamming-ball convolution

## Finding
Let \(G_n=\mathbb F_2^n\) with \(n\ge3\), let \(B_{3,n}=\{x\in G_n:|x|\le3\}\), and let \(C_n\) be unnormalized counting convolution by \(1_{B_{3,n}}\). At any Walsh frequency \(\xi\) of Hamming weight \(k\), its exact multiplier is
\[
\widehat{1_{B_{3,n}}}(\xi)=\frac{(n-2k+1)((n-2k+1)^2-3n+5)}6.
\]
Consequently the rank is exactly
\[
2^n-\sum_{\substack{0\le k\le n\\ (n-2k+1)((n-2k+1)^2-3n+5)=0}}\binom nk.
\]
In particular every odd dimension is singular; every even dimension for which \(3n-5\) is not a square is invertible.

The sharper result concerns the infinite family of odd dimensions \(n=2m+1\ge5\) satisfying \(3n-5\) **not** a perfect square. In those dimensions precisely the Walsh layer \(h=m+1\) is missing. Write \(\Lambda_n\) for the least operator norm of any linear projection of \(\ell^\infty(G_n)\) onto \(\operatorname{ran}C_n\), and likewise for the analogous \(\ell^1(G_n)\) minimum. These two minimum norms coincide, are attained by the canonical translation-invariant Fourier projection, and equal
\[
\boxed{\Lambda_{2m+1}=1+\binom{2m+1}{m+1}(2^{-m}-2^{-2m}).}
\]
Along this density-one subsequence of odd dimensions,
\[
\boxed{\Lambda_n\sim\frac2{\sqrt\pi}\frac{2^{n/2}}{\sqrt n},\qquad
\frac{\operatorname{nullity}C_n}{2^n}\sim\sqrt{\frac2{\pi n}}.}
\]
Thus relative Fourier nullity tends to zero while the sharp endpoint complementability cost increases exponentially. The exact closed projection-norm evaluation, rather than the general Fourier-projection principle or classical Krawtchouk zero formula, is the distinctive claim.

## Assumptions and scope
All functions are real or complex valued on the finite binary group, equipped with unnormalized counting \(\ell^1\) or maximum \(\ell^\infty\) norms. Walsh characters are \(\chi_\xi(x)=(-1)^{\xi\cdot x}\), and the unnormalized Fourier transform is \(\widehat f(\xi)=\sum_{x\in G_n}f(x)\chi_\xi(x)\), with inverse \(f(x)=2^{-n}\sum_\xi\widehat f(\xi)\chi_\xi(x)\). Convolution \(f*g(x)=\sum_y f(y)g(x-y)\) has precisely the multipliers above. Relative projection constants are taken inside the stated ambient \(\ell^p(G_n)\), not as absolute Banach-space projection constants.

The binomial expression for \(\Lambda_n\) is claimed only when \(n\ge5\) is odd and \(3n-5\) is nonsquare. In resonant odd dimensions and singular even dimensions the rank formula remains exact but no formula for the minimum endpoint projection norm is asserted. No spectral gap or inverse-condition estimate is asserted.

## Proof
**Walsh multiplier and zero layers.** Write \(t=n-2k\). The sums of signs over weight-zero through weight-three input vectors are the binary Krawtchouk polynomials
\[
K_0=1,\quad K_1=t,\quad K_2=(t^2-n)/2,\quad K_3=(t^3-(3n-2)t)/6.
\]
Adding and factoring gives \((t+1)((t+1)^2-(3n-5))/6\). Walsh diagonalization shows that each zero weight \(k\) contributes multiplicity \(\binom nk\), giving the rank identity. For odd \(n\), \(t+1=0\) at \(k=(n+1)/2\). If \(3n-5\) is nonsquare there are no other roots. If \(n\) is even and \(3n-5\) nonsquare, the first factor cannot vanish because \(t+1\) is odd, so the operator is invertible. (For square cases, the displayed rank formula remains valid, and may be used without assumptions about admissible root indices.)

**Sharpness over every projection.** Fix \(n=2m+1\ge5\) with nonsquare \(3n-5\), and put \(h=m+1\), \(N=2^n\), \(r=\binom nh\). The range \(Y\) consists of all functions whose Walsh coefficients vanish exactly on \(\{\xi:|\xi|=h\}\). Its canonical projection is \(P=I-E_h\), where \(E_h\) is the Fourier projection onto that layer. For any linear projection \(Q\) onto \(Y\), average its conjugates over all translations of \(G_n\). Because translations are \(\ell^1\)- and \(\ell^\infty\)-isometries, the averaged projection has norm at most \(\|Q\|\). Every translation-equivariant linear operator is a Fourier multiplier; being a projection onto \(Y\) forces multiplier one on every allowed character and zero on every excluded character. Therefore the average equals \(P\). The minimum projection norm is exactly \(\|P\|\) in either endpoint space.

**An exact absolute-sum identity.** Write
\[
K_h(x;n)=\sum_{j=0}^h(-1)^j\binom xj\binom{n-x}{h-j}.
\]
The convolution kernel of \(P\) is \(p(z)=\mathbf1_{z=0}-2^{-n}K_h(|z|;n)\). Since \(0<r<N\), its entry at zero is \(1-r/N>0\), so
\[
\|P\|_{\ell^1\to\ell^1}=\|P\|_{\ell^\infty\to\ell^\infty}
=1-\frac{2r}{N}+\frac1N\sum_{x=0}^n\binom nx|K_h(x;n)|.
\]
Both endpoint operator norms equal the absolute sum of the convolution kernel. By counting signed pairs of subsets in two orders, the Krawtchouk duality identity is
\[\binom nx K_h(x;n)=\binom nh K_x(h;n).\]
When \(n=2m+1\) and \(h=m+1\), the generating polynomial for the last coefficients is
\[
\sum_{x=0}^{n}K_x(h;n)z^x=(1-z)^{m+1}(1+z)^m=(1-z)(1-z^2)^m.
\]
Its even and odd coefficients are respectively \((-1)^j\binom mj\) and \(-(-1)^j\binom mj\), so their absolute values sum to \(2\sum_{j=0}^m\binom mj=2^{m+1}\). Hence \(\sum_x\binom nx|K_h(x;n)|=r2^{m+1}\). Substitute \(N=2^{2m+1}\) to obtain \(\|P\|=1+r(2^{-m}-2^{-2m})\), as asserted.

**Asymptotics and exceptions.** The central binomial estimate gives \(r/2^n\sim\sqrt{2/(\pi n)}\). The preceding exact expression therefore has leading term \(2^{m+1}\sqrt{2/(\pi n)}=(2/\sqrt\pi)2^{n/2}/\sqrt n\). The odd resonant dimensions solve \(3n-5=s^2\) for an even integer \(s\), and hence have counting function \(O(\sqrt X)\) up to \(X\); consequently the nonsquare odd subsequence has relative density one among odd dimensions. The nullspace consists precisely of the \(h\)-th Walsh layer, so its relative dimension is \(r/2^n\). All asymptotic conclusions follow.

## Verification
The standalone `CHECK.py` computes the binary radius-three indicator and an independent fast Walsh transform for all \(3\le n\le15\), checking \(65{,}528\) exact Fourier multipliers and their zero multiplicities. For every qualifying odd dimension in that range, it independently inverse-transforms the excluded-frequency support and compares the exact rational absolute kernel sum with the closed formula (five cases). It also verifies \(3{,}315\) integer Krawtchouk dualities at dimensions through eighty. Expected output: `HAMMING_RADIUS3_RANGE_PROJECTION_PASS walsh= 65528 norms= 5 dualities= 3315`. These finite tests do not prove the infinite statement; the algebraic argument above does.

## Relationship to prior work
Binary Krawtchouk identities and the Lloyd-polynomial description of Hamming balls are classical; their existence and general form are **not new claims**. Feinsilver and Schott supply Krawtchouk transform and convolution calculus. Defant, Galicer, Mansilla, Mastyło and Muro prove an arbitrary-Walsh-spectrum projection-kernel formula and translation-averaging minimality, which fully subsume those general steps of this proof. Those authors' full manuscript was inspected and its broader coverage accounted for: the more specific result here is the explicit closed binomial evaluation for the natural convolution range that loses just the middle layer, coupled to a sharp arithmetic criterion for that regime and the exponential versus asymptotically negligible-nullity separation. The available manuscript did not state this specialized closed value. The indexed exact radius-three Hamming-ball Turán result optimizes a *positive-definite function supported on the ball*, not projection onto the range of convolution by its indicator; its full published result was compared. A corresponding Hamming-cube Lipschitz-free-space Walsh projection theorem concerns a different Banach-space norm, and cannot directly give the present \(\ell^1/\ell^\infty\) value. Classical Lloyd-polynomial notes were checked for their documented radius-three roots; no novelty is asserted for those root identities. Searches cannot establish exhaustive historical priority, and an earlier evaluation of the middle-layer absolute Krawtchouk sum or the exact complement projection norm remains possible.

## Limitations
The new closed endpoint constant holds on the stated nonsquare odd subsequence only. The rank identity works for all \(n\ge3\) but comes from elementary classical Fourier and Krawtchouk machinery. No projection constant is determined for arithmetic resonance dimensions. General Fourier-projection minimality is prior work, not independently original. The result is self-reviewed; no independent validation or exhaustive historical-priority certification is claimed.

## References
1. R. de Wolf, *A Brief Introduction to Fourier Analysis on the Boolean Cube*, Theory of Computing Library, Graduate Surveys 1 (2008), published 2008-09-25, https://cims.nyu.edu/~regev/toc/articles/gs001/index.html.
2. P. Feinsilver and R. Schott, *Krawtchouk transforms and Convolutions*, arXiv:1409.4715, first public 2014-09-16, https://arxiv.org/abs/1409.4715.
3. A. Defant, D. Galicer, M. Mansilla, M. Mastyło and S. Muro, *Asymptotic insights for projection, Gordon-Lewis and Sidon constants in Boolean cube function spaces*, arXiv:2302.00233, first public 2023-02-01, https://arxiv.org/abs/2302.00233, especially Theorem 3.1 and Section 4.
4. N. D. Elkies, *The Lloyd polynomial and perfect codes*, teaching notes https://people.math.harvard.edu/~elkies/M256.13/lloyd.pdf (publication date not verified; used only for mathematical comparison).
