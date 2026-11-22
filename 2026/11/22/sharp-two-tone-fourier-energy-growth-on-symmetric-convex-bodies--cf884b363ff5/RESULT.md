# Sharp two-tone Fourier energy growth on symmetric convex bodies

## Finding
Let \(d\ge2\) and let \(K\subset\mathbb R^d\) be a centrally symmetric convex body with nonempty interior, centered at the origin. For \(0<r<R\), consider every nonzero two-tone plane wave
\[
 f(x)=a e^{i\langle\lambda,x\rangle}+b e^{i\langle\mu,x\rangle},\qquad a,b\in\mathbb C,\quad\lambda,\mu\in\mathbb R^d.
\]
Then the exact **frequency-unrestricted** squared-energy growth constant is
\[
 \boxed{\sup_f\frac{\int_{RK}|f(x)|^2\,dx}{\int_{rK}|f(x)|^2\,dx}=\left(\frac Rr\right)^{d+2}.}
\]
Every individual nonzero \(f\) has a *strict* inequality; the supremum is approached by the frequency-collision family \(f_\varepsilon(x)=1-e^{i\varepsilon\langle v,x\rangle}\) as \(\varepsilon\downarrow0\), for any nonzero \(v\).

For a *fixed nonzero* frequency difference \(w=\lambda-\mu\), write
\[
 \Phi_K(tw)=\frac1{|K|}\int_K\cos(t\langle w,y\rangle)\,dy.
\]
The **exact** coefficient-optimized growth constant (not just a bound) is
\[
 \boxed{\left(\frac Rr\right)^d\max\left\{\frac{1+\Phi_K(Rw)}{1+\Phi_K(rw)},\frac{1-\Phi_K(Rw)}{1-\Phi_K(rw)}\right\}.}
\]
At least one optimizing coefficient direction is \(a=b\) or \(a=-b\), according to the larger branch. In case of a tie all nonzero coefficient pairs optimize. Both branches are strictly smaller than \((R/r)^2\), so the unrestricted constant is unattained at fixed gap.

There is an exact **shape-dependent collision defect**. For a fixed nonzero direction \(v\), let \(m_j=|K|^{-1}\int_K\langle v,y\rangle^j\,dy\), for \(j=2,4\). If \(w=\varepsilon v\), the exact fixed-gap optimum satisfies
\[
 \boxed{\frac{\mathcal C_K(r,R;\varepsilon v)}{(R/r)^{d+2}}
 =1-\frac{m_4}{12m_2}(R^2-r^2)\varepsilon^2+O_{K,r,R,v}(\varepsilon^4).}
\]
Here \(m_2,m_4>0\). This coefficient makes the strict loss away from the universal optimum quantitative in every direction and for every symmetric convex shape.

## Assumptions and scope
All norms above are unnormalized Lebesgue squared-energy integrals. The symmetry center is the origin, and \(rK,RK\) denote homothetic dilates about that center. There is no restriction on the two real frequency vectors, their separation or the complex amplitudes, except that \(f\not\equiv0\). The dimension is at least two for the stated new geometric theorem; the one-dimensional interval version is included in the proof as an auxiliary known boundary case. Convexity enters solely through the symmetric unimodality of every one-dimensional projection of uniform measure on \(K\). Consequently the normalized-energy statement also applies to every centrally symmetric log-concave probability law with nondegenerate one-dimensional marginals; the Lebesgue factor \((R/r)^d\) is specific to convex-body dilates.

## Proof
**1. A strict scalar inequality.** Define \(\operatorname{sinc}(z)=\sin z/z\) for \(z\ne0\), with value one at zero. For both signs, the function
\[
 H_\pm(z)=\frac{1\pm\operatorname{sinc}z}{z^2}=\frac{z\pm\sin z}{z^3},\quad z>0,
\]
is strictly decreasing. Indeed
\[
 -z^4H_-'(z)=2z+z\cos z-3\sin z=:A(z),\qquad
 -z^4H_+'(z)=2z-z\cos z+3\sin z=:B(z).
\]
For \(0<z<\pi\), \(A(0)=A'(0)=A''(0)=0\) and \(A'''(z)=z\sin z>0\), so \(A(z)>0\); also \(B(z)\ge z+3\sin z>0\). For \(z\ge\pi\), both \(A(z),B(z)\ge z-3>0\). Thus for any \(s>0\), \(r\mapsto[1\pm\operatorname{sinc}(rs)]/r^2\) is strictly decreasing.

**2. Mixtures of symmetric intervals.** Let \(X\) be uniform on \(K\). For any \(w\ne0\), its scalar projection \(Y=\langle w,X\rangle\) has an even density nonincreasing on the positive half-axis. In dimension at least two this follows from the Brunn–Minkowski inequality: the \((d-1)\)-dimensional cross-sectional volume to the power \(1/(d-1)\) is concave on its interval of support, and even by central symmetry; hence its density is nonincreasing on the positive half-axis. Every such one-dimensional probability density is a mixture of centered uniform laws on \([-s,s]\), \(s>0\). To see this, write a decreasing right-continuous density as \(h(t)=\int_{[t,\infty)}\nu(ds)\) for \(t\ge0\); normalization gives \(\int 2s\,\nu(ds)=1\) and the mixing probability is \(2s\nu(ds)\). This argument also accommodates jumps and general monotone densities by Stieltjes measures.

Its characteristic function is therefore a mixture of \(\operatorname{sinc}(rs)\). Applying Step 1 inside that mixture shows that for either sign
\[
 r\longmapsto\frac{1\pm\Phi_K(rw)}{r^2}
\]
is strictly decreasing on positive \(r\). No positivity of \(\Phi_K\) is needed.

**3. Exact two-eigenvalue reduction.** Symmetry gives real Fourier correlation. For \(A_0=|a|^2+|b|^2\) and \(T=2\operatorname{Re}(a\overline b)\), direct integration yields
\[
 \int_{rK}|f|^2=r^d|K|\bigl(A_0+T\Phi_K(rw)\bigr),\qquad |T|\le A_0.
\]
For \(w\ne0\) the correlation satisfies \(|\Phi_K(rw)|<1\) because \(K\) has interior. Diagonalizing the associated \(2\times2\) Gram forms in the coefficient directions \((1,1)\) and \((1,-1)\) gives exactly the maximum of the two ratios in the Finding, including its equality cases. Strict decay in Step 2 proves that each ratio is strictly less than \((R/r)^2\), yielding the global inequality. When \(w=0\), the signal is a single exponential or zero, and its nonzero energy grows as \((R/r)^d\), also strictly less than the stated bound.

**4. Exact sharpness and the gap defect.** For \(f_\varepsilon(x)=1-e^{i\varepsilon\langle v,x\rangle}\), dominated Taylor expansion on bounded \(K\) gives \(|f_\varepsilon(x)|^2=\varepsilon^2\langle v,x\rangle^2+O(\varepsilon^4|\langle v,x\rangle|^4)\). Its energy quotient tends to \((R/r)^{d+2}\), since the second moment is positive. Moreover
\[
 1-\Phi_K(t\varepsilon v)=\tfrac12m_2t^2\varepsilon^2-\tfrac1{24}m_4t^4\varepsilon^4+O(\varepsilon^6).
\]
The minus branch of Step 3 tends to \((R/r)^{d+2}\), while the plus branch tends to \((R/r)^d\). Hence the minus branch is the unique maximizing eigenvalue for all sufficiently small nonzero \(\varepsilon\). Dividing the two minus-branch series proves the claimed quadratic shape-dependent defect, including its positive coefficient. The fourth-order remainder follows by expanding two even analytic functions on the bounded set.

## Verification
The complete proof is analytic. The supplementary standard-library `CHECK.py` performs deterministic checks for uniform measures on cubes in dimensions two through five, including the exact fixed-gap generalized eigenvalue formula, random complex amplitudes, the universal upper bound and collision sharpness. It also tests a non-product planar diamond with characteristic projection \(2(1-\cos t)/t^2\). Finite calculations are not used as a substitute for the universal proof.

## Relationship to prior work
Zhang's 2026 sparse-Fourier extrapolation paper proves general frequency-independent bounds for arbitrary numbers of tones and studies exterior \(L^2\)-transfer, but does not give this sharp geometry-independent two-tone dilation constant, its convex-projection argument or the directional fourth-to-second moment collision coefficient. The published 2026 *Tight exterior-energy resonances and parity switching for two-frequency Fourier sums* already supplies the exact **one-dimensional** two-tone symmetric exterior-energy spectrum. That interval case, and hence its equivalent fixed-gap nested-interval formula, are **not** claimed new here; the contribution assessed is the universal multidimensional convex-body theorem and its direction-sensitive gap defect. The published *Sharp two-frequency exterior Fourier leverage and the quadratic collision defect* concerns point evaluation, which is not an integrated energy inequality, and likewise does not control arbitrary symmetric convex observation bodies. Borwein and Erdélyi's earlier Remez/Nikolskii inequalities concern real-exponent classes and nonexact pointwise bounds, not the present arbitrary-real-frequency geometric identity. The precise implications and overlap are described in the review.

## Limitations
No claim is made for three or more Fourier atoms, general nonsymmetric convex observation bodies, or arbitrary non-unimodal marginal laws. The universal growth constant is a supremum, not a maximum. The directional small-gap expansion holds for each fixed shape and direction and is not asserted uniformly over degenerating convex bodies or directions. The one-dimensional fixed-gap formula was previously published. Possible differently phrased older convex-body two-tone inequalities remain a residual bibliography risk; no independent external validation has been performed.

## References
1. Ruizhe Zhang, *Optimal Extrapolation Bounds for Sparse Fourier Sums*, arXiv:2607.10501, first public 2026-07-11, https://arxiv.org/abs/2607.10501.
2. *Tight exterior-energy resonances and parity switching for two-frequency Fourier sums*, public research result, 2026-11-16, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-tight-exterior-energy-resonances-and-parity-switching-for-two-fr--bf78fc92d364.
3. *Sharp two-frequency exterior Fourier leverage and the quadratic collision defect*, public research result, 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-two-frequency-exterior-fourier-leverage-and-the-quadratic--517d41b07a68.
4. Peter Borwein and Tamás Erdélyi, *Pointwise Remez- and Nikolskii-type inequalities for exponential sums*, Mathematische Annalen 316 (2000), 39–60, https://doi.org/10.1007/s002080050003.
