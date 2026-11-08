# Two sharp Lu Qi-Keng thresholds for Jacobi-weighted disk kernels

## Finding
For each real \(a>-1\) and either boundary order \(m=1\) or \(m=2\), equip holomorphic functions on the unit disk with the norm
\[
\|f\|_{a,m}^{2}=\frac1\pi\int_{|z|<1}|f(z)|^2|z|^{2a}(1-|z|^2)^m\,dx\,dy.
\]
Put \(t=a+1>0\), and write \(s=z\overline w\). Its weighted Bergman kernel \(K_{a,m}(z,w)=\mathcal K_{t,m}(s)\) has exactly one *scalar* zero in \(|s|<1\) precisely in these two ranges:
\[
\begin{array}{c|c|c}
 m&\text{one scalar zero in }|s|<1&\text{zero-free in }|s|<1\\ \hline
 1&0<t<1/\sqrt2&t\ge1/\sqrt2\\
 2&0<t<(\sqrt7-1)/2&t\ge(\sqrt7-1)/2.
\end{array}
\]
Every interior scalar zero is simple and lies on the negative real axis. Every other scalar numerator root has modulus strictly greater than one. At the transition itself the distinguished zero is exactly \(s=-1\) and therefore lies *outside* the open scalar disk. The critical parameters are different: \(1/\sqrt2<(\sqrt7-1)/2\).

## Assumptions and scope
The measure is normalized planar area multiplied by \(|z|^{2a}(1-|z|^2)^m\). The disk is open; a scalar zero means a zero of \(s\mapsto\mathcal K_{t,m}(s)\) for \(|s|<1\), not a zero at some prescribed fixed \(w\). Each scalar zero \(s_0\) can be realized by a pair of interior points, for example \(z=\sqrt{|s_0|}\), \(w=-\sqrt{|s_0|}\). For \(a>-1\) the singularity at the origin is integrable, all point evaluations are bounded, and monomials are a complete orthogonal basis. Only the first two positive integer boundary orders \(m=1,2\) are asserted.

## Proof
**Moment and kernel calculation.** With \(t=a+1>0\), polar coordinates followed by \(u=|z|^2\) give for every integer \(n\ge0\)
\[
\|z^n\|_{a,m}^2=\int_0^1 u^{n+t-1}(1-u)^m\,du
=\mathrm B(n+t,m+1)=\frac{m!}{\prod_{j=0}^{m}(n+t+j)}.
\]
Angular orthogonality and Parseval show that the monomials are complete. The inverse moments yield the absolutely locally uniformly convergent kernel series
\[
\mathcal K_{t,m}(s)=\frac1{m!}\sum_{n=0}^{\infty}
\left(\prod_{j=0}^{m}(n+t+j)\right)s^n,
\qquad |s|<1.
\]
Summing the polynomial-in-\(n\) coefficients with \(\sum_{n\ge0}s^n=(1-s)^{-1}\) gives
\[
\mathcal K_{t,m}(s)=\frac{P_{m,t}(s)}{m!(1-s)^{m+2}},
\]
where the two explicitly normalized numerators are
\[
P_{1,t}(s)=t(t+1)+2(1-t^2)s+t(t-1)s^2
\]
and
\[
\begin{split}
P_{2,t}(s)={}&t(t+1)(t+2)+3(1-t)(t+1)(t+2)s\\
&+3t(t-1)(t+2)s^2-t(t-1)(t+1)s^3.
\end{split}
\]
They satisfy \(P_{1,t}(1)=2\), \(P_{2,t}(1)=6\), and
\[
P_{1,t}(-1)=2(2t^2-1),\qquad
P_{2,t}(-1)=2(2t+1)(2t^2+2t-3).
\]
The denominator never vanishes for \(|s|<1\), so the zero question is exactly a question about these polynomials.

**First boundary order.** If \(0<t<1\), then the quadratic's constant and linear coefficients are positive and its leading coefficient is negative. Consequently \(P_{1,t}(-x)\) strictly decreases from a positive value to negative infinity as \(x\) runs from zero to infinity, giving exactly one negative real root. Its positive real root is strictly greater than one because \(P_{1,t}(1)=2>0\) and the leading coefficient is negative. The negative root is interior exactly when \(P_{1,t}(-1)<0\), i.e. \(t<1/\sqrt2\). At \(t=1\), the numerator is the constant two. For \(t>1\), its discriminant is \(4(1-t^2)<0\). The conjugate roots have squared modulus
\[
\frac{t(t+1)}{t(t-1)}=\frac{t+1}{t-1}>1,
\]
so there are no disk zeros.

**Second boundary order for \(0<t<1\).** The coefficients of \(P_{2,t}(-x)\) are positive for the constant term and strictly negative for each positive power of \(x\). Hence this polynomial is strictly decreasing for \(x\ge0\), and has a unique negative real root \(-r\), with \(r>0\). Its cubic discriminant is
\[
-216t(t-1)^2(t+1)(t+2)^2<0,
\]
so the other two roots are nonreal conjugates. Let \(R=(t+2)/(1-t)\). Since the negative linear term in \(P_{2,t}(-R)\) already exceeds the positive constant in magnitude, and the remaining terms are negative, \(P_{2,t}(-R)<0\); therefore \(r<R\). Vieta's product formula shows that the squared modulus of each conjugate root is \(R/r>1\). Thus no other root lies in the closed unit disk. The negative root is interior exactly when \(P_{2,t}(-1)<0\), or equivalently \(2t^2+2t-3<0\), which gives \(t<(\sqrt7-1)/2\).

**Second boundary order for \(t\ge1\).** At \(t=1\), \(P_{2,t}\) is the constant six. For \(t>1\), the cubic discriminant remains negative, so there is exactly one real root. Its leading coefficient is negative, and \(P_{2,t}(1)=6>0\); the real root \(r\) therefore satisfies \(r>1\). Let \(R=(t+2)/(t-1)>1\). Direct substitution gives
\[
P_{2,t}(R)=-\frac{6(t+2)(2t+1)}{(t-1)^2}<0,
\]
so \(1<r<R\). The other two roots are conjugates, each of squared modulus \(R/r>1\) by Vieta. Thus no zeros lie in the open scalar disk. In both orders, the interior negative root is simple (by the distinct-root arguments), and the boundary equality at the threshold is excluded since \(|s|=1\) is not attained for \(z,w\) inside the disk. The result follows.

## Verification
The standalone script `jacobi_kernel_check.py` uses Python's exact rational arithmetic to compare the closed numerator formulas with the inverse-Beta moment coefficients for both orders over twelve rational values of \(t\) and sixteen Taylor coefficients per case. It also checks root placement and both threshold identities. Invocation: `python jacobi_kernel_check.py`. The recorded execution returned `JACOBI_BERGMAN_KERNEL_PASS exact=432 root_and_threshold=59`. The script checks only finitely many instances; the preceding root-location proof handles every real \(t>0\).

## Relationship to prior work
Miña-Díaz (arXiv:2212.08118v1, 2022) derives formulas for disk weights formed from powers of Blaschke factors, including a power of the distance to an interior point; that weight class does not contain the additional \((1-|z|^2)^m\) factor. Perälä (arXiv:1703.05976v1, 2017) proves that radial Bergman kernels have only finitely many zeros and constructs radial weights producing prescribed finite counts; these conclusions do not determine the present exact thresholds for prescribed Jacobi weights. Beberok (2017) treats kernels of intersecting ellipsoids and integer-dimensional Jacobi representations, rather than this real continuum of interior singularity parameters.

The published result *Zero-free power-deficit radial Bergman kernels* proves nonvanishing for weights \(1-q|z|^{2\gamma}\), including the present special point \(a=0,m=1\) when \(q=\gamma=1\), but has no interior power singularity and does not imply either threshold. *Sharp Lu Qi-Keng transitions for Euclidean boundary-distance weighted disk kernels* treats \((1-|z|)^v\), not the weight \(|z|^{2a}(1-|z|^2)^m\), and does not give these transitions. This comparison is about the exact kernel statements and their implications, not similarity of terminology.

## Limitations
The exact classification is limited to boundary orders one and two and fixed \(a>-1\). For higher orders, additional numerator roots may enter and a general one-zero classification is not asserted. The number of zeros is a scalar-kernel zero count in \(|s|<1\); it is not the number of zeros in every fixed kernel section. The source comparison does not exclude a presently unlocated equivalent treatment in the classical theory of generalized Eulerian or hypergeometric polynomials. No independent mathematical audit has been performed.

## References
- E. Miña-Díaz, *A representation for the reproducing kernel of a weighted Bergman space*, arXiv:2212.08118v1 (first public 2022-12-15), https://arxiv.org/abs/2212.08118.
- A. Perälä, *Vanishing Bergman Kernels on the Disk*, arXiv:1703.05976v1 (2017), https://arxiv.org/abs/1703.05976.
- T. Beberok, *The Bergman kernel: Explicit formulas, deflation, Lu Qi-Keng problem and Jacobi polynomials*, Czechoslovak Mathematical Journal 67 (2017), 537–549, DOI:10.21136/CMJ.2017.0073-16.
- Y. E. Zeytuncu, *Weighted Bergman Projections and Kernels: Lp Regularity and Zeros*, arXiv:1009.2806v1 (2010), https://arxiv.org/abs/1009.2806.
- *Zero-free power-deficit radial Bergman kernels*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-zero-free-power-deficit-radial-bergman-kernels--19710ce10193.
- *Sharp Lu Qi-Keng transitions for Euclidean boundary-distance weighted disk kernels*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-lu-qi-keng-transitions-for-euclidean-boundary-distance-wei--b68d363f03d0.
