# Eight-cycle resonance in degree-two Lipschitz Fourier projection

## Finding
For each integer \(n\ge5\), let \(C_n=\mathbb Z/n\mathbb Z\) have unit shortest-path distance. Equip the real Banach space \(X_n=\operatorname{Lip}_0(C_n)\) with the norm
\[
\|f\|_{\operatorname{Lip}}=\max_{j\in C_n}|f(j+1)-f(j)|,\qquad f(0)=0.
\]
Let \(E_n\subset X_n\) consist of the real degree-at-most-two trigonometric functions, normalized to vanish at zero: it is spanned by the four functions obtained from \(\cos(2\pi k j/n)\) and \(\sin(2\pi k j/n)\), \(k=1,2\), by subtracting their value at \(j=0\). Define the relative projection constant
\[
\lambda_n=\inf\{\|Q\|_{X_n\to X_n}:Q^2=Q,\ \operatorname{ran}Q=E_n\}.
\]
Then the canonical real Fourier projector onto the first two nonconstant harmonic pairs is a minimum-norm projection, and
\[
\boxed{\lambda_n=\frac1n\min_{c\in\mathbb R}\sum_{j=0}^{n-1}\left|1+2\cos\frac{2\pi j}{n}+2\cos\frac{4\pi j}{n}-c\right|.}\tag{1}
\]
The **sharp universal projection bound across all finite cycles** is
\[
\boxed{\sup_{n\ge5}\lambda_n=\lambda_8=1+\frac{1}{\sqrt2},}\tag{2}
\]
and equality in (2) occurs at **exactly** the eight-cycle. More quantitatively, \(\lambda_n<17/10\) for every integer \(n\ge5\) other than eight, whereas \(\lambda_8>17/10\). Furthermore,
\[
\boxed{\lim_{n\to\infty}\lambda_n=\frac5\pi.}\tag{3}
\]
Thus the worst finite sampling has a strictly larger projection norm than the continuous-circle limit.

## Assumptions and scope
Scalars are real throughout. The cyclic edge length is one and the underlying norm is the Lipschitz seminorm modulo constants, made a norm by \(f(0)=0\). All four retained real harmonic generators are independent for \(n\ge5\); when \(n=5\), they span the entire \(X_5\) and \(\lambda_5=1\). The infimum defining \(\lambda_n\) ranges over **every** real linear projection with range \(E_n\), not just Fourier multipliers or positive operators. The Fourier projector uses normalized counting measure. Frequencies are understood modulo \(n\), with no aliasing among \(0,\pm1,\pm2\) for \(n\ge5\).

## Proof
**1. Invariant projection and the mean-zero derivative space.** For \(f\in X_n\), define \((Df)_j=f(j+1)-f(j)\). The map \(D\) is a linear isometry onto
\[
H_n=\left\{g\in\mathbb R^n:\sum_{j=0}^{n-1}g_j=0\right\}
\]
with the coordinate maximum norm. Every \(g\in H_n\) integrates to a periodic function, uniquely after normalization at zero. The isometries \((R_hf)(j)=f(j+h)-f(h)\) represent cyclic rotations of \(C_n\). They preserve \(E_n\). Given any projection \(Q\) onto \(E_n\), the average \(n^{-1}\sum_h R_h^{-1}QR_h\) is still a projection onto \(E_n\), has norm at most \(\|Q\|\), and commutes with all rotations. In the complexification of \(H_n\), the cyclic shift has distinct one-dimensional eigenspaces for the nonzero Fourier characters. Hence the only commuting projection fixing the real \(\pm1,\pm2\) harmonic subspace and vanishing onto all other characters is its Fourier spectral projector. Consequently the Fourier projector minimizes the projection norm.

**2. Exact median formula.** Write
\[
D_2(t)=1+2\cos t+2\cos(2t).
\]
Under the derivative isometry, the spectral projection onto frequencies \(\pm1,\pm2\) is cyclic convolution with \(D_2(2\pi j/n)/n\): the constant term acts as zero on \(H_n\). Every output row is a translate of the same functional, and finite-dimensional quotient duality gives
\[
\sup_{\substack{\|g\|_\infty\le1\\\sum_jg_j=0}}\left|\frac1n\sum_{j=0}^{n-1}D_2(2\pi j/n)g_j\right|
=\frac1n\inf_{c\in\mathbb R}\sum_{j=0}^{n-1}|D_2(2\pi j/n)-c|.
\]
For completeness, the upper inequality follows by subtracting any constant from the row. The reverse inequality follows from the standard linear-programming dual of the cube intersected with the zero-sum hyperplane, or directly by assigning signs above and below a median and choosing entries in \([-1,1]\) at ties to make the sum zero. A minimizing \(c\) is any median of the \(n\) real kernel values. This proves (1).

**3. Exact eight-cycle value and finite extremizer.** When \(n=8\), the eight values of \(D_2\), in cyclic order, are
\[
5,\ 1+\sqrt2,\ -1,\ 1-\sqrt2,\ 1,\ 1-\sqrt2,\ -1,\ 1+\sqrt2.
\]
Any number between \(1-\sqrt2\) and \(1\) is a median, so \(c=1/2\) is admissible. The absolute-deviation sum is \(8+4\sqrt2\), giving \(\lambda_8=1+1/\sqrt2\). The zero-sum edge gradient
\[
g=(1,1,-1,-1,1,-1,-1,1)
\]
has coordinate maximum norm one and attains the corresponding row norm. Integrating it around the cycle yields an explicit real input on which the Fourier projection attains the sharp norm; the maximum in (2) is therefore an actual norm, not merely a limit.

**4. A continuous-median identity.** Put \(F(t)=|D_2(t)-1/2|\). Its four zeros on \([0,2\pi)\) occur at
\[
\theta,\quad\theta+\frac\pi2,\quad\frac{3\pi}{2}-\theta,\quad2\pi-\theta,
\qquad\cos\theta=\frac{\sqrt7-1}{4},\quad\sin\theta=\frac{\sqrt7+1}{4}.
\]
The positive and negative sets of \(D_2-1/2\) each have length \(\pi\), so \(1/2\) is a median under continuous uniform measure. An antiderivative of \(D_2-1/2\) is \(A(t)=t/2+2\sin t+\sin(2t)\). Using \(\sin\theta-\cos\theta=1/2\), \(\sin(2\theta)=3/4\), and the four zero locations yields
\[
\int_0^{2\pi}F(t)\,dt=10.
\]
It follows that
\[
\min_{c\in\mathbb R}\frac1{2\pi}\int_0^{2\pi}|D_2(t)-c|\,dt=\frac5\pi.\tag{4}
\]
All medians for the finite samples lie in the fixed range \([-5/4,5]\). On this compact interval in \(c\), the equally spaced Riemann sums for the jointly continuous function \(|D_2(t)-c|\) converge uniformly to the integral, by uniform continuity and the fact that the integrand is one-Lipschitz in \(c\). Taking minima proves (3).

**5. A dimension-uniform strict bound away from eight.** Because \(c=1/2\) is a legal comparison constant in (1), set
\[
B_n=\frac1n\sum_{j=0}^{n-1}F(2\pi j/n),\qquad\lambda_n\le B_n.\tag{5}
\]
The function \(F\) is continuous and periodic, with piecewise smooth derivative. Since
\[
D'_2(t)=-2\sin t-4\sin(2t),\qquad D''_2(t)=-2\cos t-8\cos(2t),
\]
we have \(\max|D'_2|\le6\) and \(\int_0^{2\pi}|D''_2(t)|dt\le40\). At the four simple zeros of \(D_2-1/2\), the derivative of \(F\) jumps by at most \(12\). Therefore the total variation of the periodic derivative satisfies \(\operatorname{Var}(F')\le88\). Integration by parts twice in the distributional sense gives the Fourier coefficient bound
\[
|\widehat F(k)|\le\frac{88}{2\pi k^2}\qquad(k\ne0).
\]
The Fourier series of \(F\) is absolutely convergent. Averaging its Fourier series over the \(n\)-grid retains exactly the multiples of \(n\), whence
\[
B_n\le\frac5\pi+\frac{44\pi}{3n^2}.\tag{6}
\]
For all \(n\ge21\), the elementary rational bounds \(157/50<\pi<22/7\) imply
\[
B_n<\frac{250}{157}+\frac{44}{3\cdot21^2}\frac{22}{7}
=\frac{2467226}{1453977}<\frac{17}{10}.\tag{7}
\]
For the fifteen remaining dimensions \(5\le n\le20\), \(n\ne8\), the accompanying exact-rational verifier proves the stronger inequality \(B_n<163/100\). It employs Machin's arctangent identity with alternating-series enclosures for \(\pi\), the Taylor polynomial of degree thirty with a rigorous degree-thirty-two remainder for each cosine sample, and rational interval upper bounds for absolute values. Thus this is a finite verified system of strict rational inequalities, not floating-point enumeration. The full script and its independently rerunnable assertions are included as `verify.py`. Together (7) and the finite certificate show \(\lambda_n<17/10\) whenever \(n\ne8\). Finally, \(1+1/\sqrt2>17/10\), because \(1/2>(7/10)^2\). The eight-cycle is the unique global maximizer, completing (2).

## Verification
Run `python3 verify.py` with any standard Python 3 installation. The verifier uses only exact rational arithmetic for all fifteen finite exceptional dimensions, producing `CERTIFIED_FINITE_N5_TO_N20_EXCEPT_N8_PASS`; it also checks the analytic large-dimension rational envelope, the exact eight-cycle norming edge gradient, and direct sampled-median diagnostics for dimensions 5 through 100. The latter floating-point diagnostics are corroborative only. The infinite family follows from the analytic inequality (6), and the limiting identity from (4) and uniform Riemann-sum convergence.

## Relationship to prior work
Godefroy and Kalton's *Lipschitz-free Banach spaces* (2003) develops the Banach-space setting and complementation background but does not identify Fourier band subspaces of finite metric cycles. Bonami and Révész's *Integral Concentration of idempotent trigonometric polynomials with gaps* (first posted 2007-07-20) treats Dirichlet kernels and finite cyclic grids in a different, \(L^p\)-concentration problem, not the relative projection constant in (2).

The publicly available *Sharp harmonic projection constants on finite metric cycles* determines minimum projection norms for **one** real harmonic pair; its statement does not treat the simultaneous first and second harmonic pairs. *Exact endpoint norms and residue law for consecutive cyclic Fourier projections* determines the full-space \(\ell^\infty\) norm of every finite Fourier-band convolution. That is an upper bound on, but not the same as, the mean-zero-edge quotient norm in (1). For instance, the five-character full-space endpoint norm on the seven-cycle is approximately \(1.71256\), already larger than the asserted unique eight-cycle Lipschitz optimum; the previous endpoint bound alone cannot prove the new universal result. The published *Exact three-frequency Fourier projection norm on every cyclic group* concerns three, rather than five, retained characters. None of these inspected statements implies the present unique global eight-cycle maximizer or exact limiting median identity.

## Limitations
The theorem concerns real scalars, unit-edge cyclic metrics, a fixed low-frequency band with two harmonic pairs, and linear projections with that specified range. It does not establish analogous global extremal cycles for higher Fourier bandwidths, irregularly weighted cycles, or complex-valued Lipschitz spaces. The analytic proof certifies only the stated universal bound and limit, not an elementary residue-class closed form for every \(n\). Mathematical priority remains subject to the usual risk of an unindexed older formulation of finite cyclic projection norms; exact finite computations by themselves do not resolve that question.

## References
1. A. Bonami and S. Gy. Révész, *Integral Concentration of idempotent trigonometric polynomials with gaps*, arXiv:0707.3023v1, first public 2007-07-20, https://arxiv.org/abs/0707.3023 .
2. G. Godefroy and N. J. Kalton, *Lipschitz-free Banach spaces*, *Studia Mathematica* **159** (2003), 121–141, DOI:10.4064/sm159-1-6, https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/159/1/90209/lipschitz-free-banach-spaces .
3. *Sharp harmonic projection constants on finite metric cycles*, publicly available mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-harmonic-projection-constants-on-finite-metric-cycles--616f4adc601f .
4. *Exact endpoint norms and residue law for consecutive cyclic Fourier projections*, publicly available mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-endpoint-norms-and-residue-law-for-consecutive-cyclic-four--8f1466cba7af .
5. *Exact three-frequency Fourier projection norm on every cyclic group*, publicly available mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-three-frequency-fourier-projection-norm-on-every-cyclic-gr--b176a6018242 .
